#!/usr/bin/env python3
"""Build the Agendum wiki: an Open Knowledge Format (OKF) v0.2 bundle made from GitHub issues.

Each issue becomes one concept page in wiki/issues/. Topic digests, a priority queue,
an index, a log, and two SVG charts are generated from the same data.
Hand-written pages in wiki/concepts/ and wiki/images/issue-*.svg are never overwritten.

Usage:
    python3 scripts/build-wiki.py                  # fetch issues with gh, rewrite wiki/
    python3 scripts/build-wiki.py --from FILE.json # use saved `gh issue list --json` output
"""
import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
REPO = "mykie2015/agendum"
OKF_VERSION = "0.2"
ACTOR = "process:agendum-wiki/1"
TYPES = ["read", "research", "experiment", "build", "write", "post", "update", "domain", "buy", "watch"]
PRIOS = ["p0", "p1", "p2"]
TOPICS = ["ai", "agent", "harness", "opensource", "product", "content", "website", "apple", "wealth"]
URL_RE = re.compile(r"https?://[^\s)>\]`\"']+")


def yq(value):
    """Double-quoted YAML scalar."""
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sections(body):
    """Split an issue body on level-3 headings."""
    out, name, buf = {}, None, []
    for line in body.splitlines():
        if line.startswith("### "):
            if name is not None:
                out[name] = "\n".join(buf).strip()
            name, buf = line[4:].strip(), []
        elif name is not None:
            buf.append(line)
    if name is not None:
        out[name] = "\n".join(buf).strip()
    return out


def first_line(text):
    for line in (text or "").splitlines():
        if line.strip() and line.strip() != "_No response_":
            return line.strip()
    return ""


def clean(text):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]|\[([^\]]*)\]\([^)]*\)", r"\1", text or "")).strip()


def first_sentence(text, limit=220):
    text = clean(text)
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def evidence_section(sec):
    for key in sec:
        if key.lower().startswith("evidence"):
            return sec[key]
    return ""


def limits_text(evidence):
    lines = evidence.splitlines()
    for i, line in enumerate(lines):
        if re.search(r"limits|unverified", line, re.I):
            tail = line.split(":", 1)[1].strip() if ":" in line and not line.startswith("#") else ""
            if not tail and i + 1 < len(lines):
                tail = lines[i + 1].strip()
            tail = clean(tail.lstrip("-* "))
            if tail:
                tail = tail[0].upper() + tail[1:]
                return tail if len(tail) <= 420 else tail[:419].rstrip() + "…"
    return ""


def checklist(text):
    return [(m.group(1) == "x", m.group(2).strip()) for m in re.finditer(r"^\s*- \[([ x])\] (.+)$", text or "", re.M)]


def parse(issue):
    m = re.match(r"^\[(\w+)\]\s*(\d{4}-\d{2}-\d{2})\s*·\s*(.*)$", issue["title"])
    kind, date, headline = (m.group(1).lower(), m.group(2), m.group(3)) if m else ("watch", issue["createdAt"][:10], issue["title"])
    sec = sections(issue["body"])
    labels = [l["name"] for l in issue["labels"]]
    prio = next((l for l in labels if l in PRIOS), "watch")
    evidence = evidence_section(sec)
    urls = []
    for u in URL_RE.findall(evidence):
        u = u.rstrip(".,;:*")
        if u not in urls and "github.com/mykie2015/agendum" not in u:
            urls.append(u)
    judgment = sec.get("Core judgment", "")
    return {
        "number": issue["number"], "url": issue["url"], "state": issue["state"].lower(),
        "type": kind, "date": date, "headline": headline, "prio": prio,
        "effort": first_line(sec.get("Effort", "")), "topics": [l for l in labels if l in TOPICS],
        "judgment": judgment, "summary": sec.get("Summary", ""),
        "limits": limits_text(evidence), "urls": urls[:8],
        "steps": checklist(sec.get("Next step", "")),
        "result": sec.get("Result / review", "").strip(), "followup": first_line(sec.get("Follow-up decision", "")),
        "comments": [first_line(re.sub(r"^#+\s*", "", c["body"])) for c in issue["comments"]],
        "closed": issue.get("closedAt"),
        "slug": "%02d-%s" % (issue["number"], re.sub(r"[^a-z0-9]+", "-", headline.lower()).strip("-")[:56].strip("-")),
    }


def page(front, body):
    return "---\n" + "\n".join(front) + "\n---\n\n" + body.rstrip() + "\n"


def issue_page(a, at, used_in=()):
    desc = first_sentence(a["judgment"]) or a["headline"]
    front = [
        "type: Agendum Action", f"title: {yq(a['headline'])}", f"description: {yq(desc)}",
        f"resource: {a['url']}", "tags: [" + ", ".join([a["type"], a["prio"]] + a["topics"]) + "]",
        f"status: {'stable' if a['state'] == 'closed' else 'draft'}",
        f"issue: {a['number']}", f"action_type: {a['type']}", f"priority: {a['prio']}", f"state: {a['state']}",
        f"created: {a['date']}", f"generated: {{ by: {ACTOR}, at: {at} }}",
    ]
    if a["urls"]:
        front.append("sources:")
        for i, u in enumerate(a["urls"], 1):
            front.append(f"  - {{ id: s{i}, resource: {u} }}")
    b = [f"# Decision\n\n{a['judgment'] or a['headline']}"]
    if a["summary"]:
        b.append(f"# Summary\n\n{a['summary']}")
    if used_in:
        b.append("# Used in insights\n\n" + "\n".join(f"* [{t}](../insights/{f})" for t, f in used_in))
    if a["limits"]:
        b.append(f"# Limits\n\n{a['limits']}")
    if a["steps"]:
        b.append("# Next steps\n\n" + "\n".join(f"- [{'x' if d else ' '}] {s}" for d, s in a["steps"]))
    if a["result"] and a["result"] != "_No response_":
        b.append(f"# Result\n\n{a['result']}" + (f"\n\nFollow-up: {a['followup']}" if a["followup"] else ""))
    if a["comments"]:
        b.append("# Updates\n\n" + "\n".join(f"- {clean(c)[:200]}" for c in a["comments"] if c))
    if a["urls"]:
        b.append("# Sources\n\n" + "\n".join(f"- {u}" for u in a["urls"]))
    b.append("# Tracking\n\n" + (
        f"[Issue #{a['number']}]({a['url']}) · {a['type'].upper()} · {a['prio'].upper()} · {a['effort'] or 'effort not set'} · {a['state']}"
        + ("\n\nTopics: " + ", ".join(f"[{t}](../topics/{t}.md)" for t in a["topics"]) if a["topics"] else "")))
    return page(front, "\n\n".join(b))


def listing(items, base="issues/"):
    return "\n".join(
        f"* [#{a['number']} {a['headline']}]({base}{a['slug']}.md) - {first_sentence(a['judgment'], 160)}" for a in items)


def topic_page(topic, items, at):
    items = sorted(items, key=lambda a: -a["number"])
    openn = sum(a["state"] == "open" for a in items)
    front = ["type: Topic Digest", f"title: {yq(topic)}", f"description: {yq(f'{len(items)} actions tagged {topic} ({openn} open).')}",
             f"tags: [{topic}]", f"generated: {{ by: {ACTOR}, at: {at} }}"]
    return page(front, f"# Actions tagged {topic}\n\n" + listing(items, "../issues/"))


def queue_page(actions, at):
    rows = [a for a in actions if a["state"] == "open"]
    order = {"p0": 0, "p1": 1, "p2": 2, "watch": 3}
    rows.sort(key=lambda a: (order.get(a["prio"], 3), -a["number"]))
    front = ["type: Report", 'title: "Open action queue"', f"description: {yq(f'{len(rows)} open actions by priority, with the first unchecked step.')}",
             f"generated: {{ by: {ACTOR}, at: {at} }}"]
    out = []
    for prio in ["p0", "p1", "p2", "watch"]:
        group = [a for a in rows if a["prio"] == prio]
        if not group:
            continue
        out.append(f"# {prio.upper()} ({len(group)})\n")
        for a in group:
            step = next((s for d, s in a["steps"] if not d), "no open step")
            out.append(f"* [#{a['number']} {a['headline']}](issues/{a['slug']}.md) - {a['type']}; next: {clean(step)[:140]}")
        out.append("")
    return page(front, "\n".join(out))


def bar_svg(title, rows, path, color_open="#4f46e5", color_done="#9ca3af"):
    w, row_h, left = 720, 26, 130
    h = 70 + row_h * len(rows)
    peak = max([o + c for _, o, c in rows] + [1])
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">',
             '<style>text{font:13px -apple-system,Segoe UI,sans-serif;fill:#1f2937}.t{font-weight:600;font-size:16px}</style>',
             f'<rect width="{w}" height="{h}" fill="#ffffff"/>', f'<text class="t" x="16" y="28">{title}</text>',
             f'<rect x="{left}" y="40" width="10" height="10" fill="{color_open}"/><text x="{left + 14}" y="49">open</text>',
             f'<rect x="{left + 70}" y="40" width="10" height="10" fill="{color_done}"/><text x="{left + 84}" y="49">closed</text>']
    for i, (label, o, c) in enumerate(rows):
        y = 62 + i * row_h
        scale = (w - left - 60) / peak
        parts.append(f'<text x="16" y="{y + 14}">{label}</text>')
        parts.append(f'<rect x="{left}" y="{y}" width="{o * scale:.1f}" height="18" fill="{color_open}"/>')
        parts.append(f'<rect x="{left + o * scale:.1f}" y="{y}" width="{c * scale:.1f}" height="18" fill="{color_done}"/>')
        parts.append(f'<text x="{left + (o + c) * scale + 6:.1f}" y="{y + 14}">{o + c}</text>')
    parts.append("</svg>")
    path.write_text("\n".join(parts) + "\n")


def read_insights():
    """Hand-written insight pages: wiki/insights/*.md with an `issues: [..]` list."""
    out = []
    for f in sorted((WIKI / "insights").glob("*.md")):
        if f.name == "index.md":
            continue
        text = f.read_text()
        title = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
        desc = re.search(r'^description:\s*"?(.*?)"?\s*$', text, re.M)
        nums = re.search(r"^issues:\s*\[(.*?)\]", text, re.M)
        conf = re.search(r"^confidence:\s*([\w-]+)", text, re.M)
        out.append({"file": f.name, "title": title.group(1) if title else f.stem, "desc": desc.group(1) if desc else "",
                    "issues": [int(n) for n in re.findall(r"\d+", nums.group(1))] if nums else [],
                    "conf": conf.group(1) if conf else "unrated"})
    return out


def link_issue_tokens(actions):
    """Turn bare [#N] tokens in insight pages into links to the issue pages."""
    slugs = {a["number"]: a["slug"] for a in actions}
    for f in (WIKI / "insights").glob("*.md"):
        text = f.read_text()
        new = re.sub(r"\[#(\d+)\](?!\()", lambda m: f"[#{m.group(1)}](../issues/{slugs[int(m.group(1))]}.md)" if int(m.group(1)) in slugs else m.group(0), text)
        if new != text:
            f.write_text(new)


def build(issues):
    at = now_iso()
    actions = sorted((parse(i) for i in issues if i["labels"] and any(l["name"] == "action" for l in i["labels"])), key=lambda a: a["number"])
    for d in ("issues", "topics", "concepts", "images", "insights"):
        (WIKI / d).mkdir(parents=True, exist_ok=True)
    for old in (WIKI / "issues").glob("*.md"):
        old.unlink()
    link_issue_tokens(actions)
    insights = read_insights()
    used = defaultdict(list)
    for ins in insights:
        for n in ins["issues"]:
            used[n].append((ins["title"], ins["file"]))
    for a in actions:
        (WIKI / "issues" / f"{a['slug']}.md").write_text(issue_page(a, at, used.get(a["number"], ())))
    by_topic = defaultdict(list)
    for a in actions:
        for t in a["topics"]:
            by_topic[t].append(a)
    for old in (WIKI / "topics").glob("*.md"):
        old.unlink()
    for t, items in by_topic.items():
        (WIKI / "topics" / f"{t}.md").write_text(topic_page(t, items, at))
    (WIKI / "queue.md").write_text(queue_page(actions, at))
    tcount = {t: Counter(a["state"] for a in actions if a["type"] == t) for t in TYPES}
    bar_svg("Actions by type", [(t, c["open"], c["closed"]) for t, c in tcount.items() if c], WIKI / "images" / "actions-by-type.svg")
    pcount = {t: Counter(a["state"] for a in items) for t, items in by_topic.items()}
    bar_svg("Actions by topic", sorted(((t, c["open"], c["closed"]) for t, c in pcount.items()), key=lambda r: -(r[1] + r[2])), WIKI / "images" / "actions-by-topic.svg")

    concepts = []
    for f in sorted((WIKI / "concepts").glob("*.md")):
        fm = re.search(r"^description:\s*\"?(.*?)\"?\s*$", f.read_text(), re.M)
        concepts.append(f"* [{f.stem.replace('-', ' ').title()}](concepts/{f.name}) - {fm.group(1) if fm else ''}")
    openn = sum(a["state"] == "open" for a in actions)
    covered = {n for ins in insights for n in ins["issues"]}
    idx = [f'---\nokf_version: "{OKF_VERSION}"\n---\n', "# Agendum wiki\n",
           f"What the {len(actions)} Agendum actions ({openn} open) add up to. Insight pages make claims across related issues; issue pages are the evidence ledger. Format: Open Knowledge Format v{OKF_VERSION}.\n",
           "# Insights\n"]
    idx += [f"* [{i['title']}](insights/{i['file']}) - {i['desc']} (confidence: {i['conf']}; issues: {', '.join('#' + str(n) for n in i['issues'])})" for i in insights] or ["* none yet"]
    idx += ["", f"Issues not yet synthesized into an insight: {len(actions) - len(covered & {a['number'] for a in actions})} of {len(actions)}. List: [insights/index.md](insights/index.md).\n",
            "# Evidence and views\n", "* [Open action queue](queue.md) - open actions by priority with the next step",
            f"* [All actions](issues/index.md) - one page per issue ({len(actions)})"]
    idx += [f"* [{t}](topics/{t}.md) - {len(v)} actions" for t, v in sorted(by_topic.items(), key=lambda kv: -len(kv[1]))]
    if concepts:
        idx += ["", "# Concepts\n"] + concepts
    idx += ["", "![Actions by type](images/actions-by-type.svg)\n", "![Actions by topic](images/actions-by-topic.svg)"]
    (WIKI / "index.md").write_text("\n".join(idx) + "\n")
    todo = [a for a in sorted(actions, key=lambda a: ({"p0": 0, "p1": 1, "p2": 2}.get(a["prio"], 3), -a["number"])) if a["number"] not in covered]
    (WIKI / "insights" / "index.md").write_text("# Insights\n\n" + "\n".join(f"* [{i['title']}]({i['file']}) - {i['desc']}" for i in insights)
        + "\n\n# Waiting for synthesis\n\nIssues with no insight page yet (open first, by priority):\n\n"
        + "\n".join(f"* [#{a['number']} {a['headline']}](../issues/{a['slug']}.md) - {a['state']}" for a in todo) + "\n")
    (WIKI / "issues" / "index.md").write_text("# Actions\n\n" + listing(sorted(actions, key=lambda a: -a["number"]), "") + "\n")

    log = WIKI / "log.md"
    today = at[:10]
    entry = f"* **Update**: Rebuilt from {len(actions)} issues ({openn} open)."
    text = log.read_text() if log.exists() else "# Wiki Update Log\n"
    if f"## {today}" in text:
        text = re.sub(rf"(## {today}\n)(\* \*\*Update\*\*: Rebuilt[^\n]*\n)?", lambda m: m.group(1) + entry + "\n", text, count=1)
    else:
        text = text.replace("# Wiki Update Log\n", f"# Wiki Update Log\n\n## {today}\n{entry}\n", 1)
    log.write_text(text if text.endswith("\n") else text + "\n")
    print(f"wrote {len(actions)} issue pages, {len(by_topic)} topic pages, queue, index, charts")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", help="saved gh issue list JSON")
    args = ap.parse_args()
    if args.src:
        issues = json.loads(Path(args.src).read_text())
    else:
        r = subprocess.run(["gh", "issue", "list", "-R", REPO, "--state", "all", "--limit", "500", "--json",
                            "number,title,state,labels,body,createdAt,closedAt,comments,url"], capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stderr)
        issues = json.loads(r.stdout)
    build(issues)


if __name__ == "__main__":
    main()
