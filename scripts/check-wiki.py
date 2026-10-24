#!/usr/bin/env python3
"""Check that wiki/ is a conformant OKF v0.2 bundle.

Checks: every concept has frontmatter with a non-empty `type`; timestamps are ISO 8601
with an explicit offset; relative links and images resolve; the root index declares okf_version.
"""
import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
RESERVED = {"index.md", "log.md"}
ISO = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})")
errors = []

root = (WIKI / "index.md").read_text() if (WIKI / "index.md").exists() else ""
if not re.match(r'---\nokf_version: "0\.2"\n---', root):
    errors.append("wiki/index.md must start with an okf_version: \"0.2\" block")

for f in sorted(WIKI.rglob("*.md")):
    rel = f.relative_to(WIKI)
    text = f.read_text()
    if f.name not in RESERVED:
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{rel}: missing frontmatter")
        else:
            fm = m.group(1)
            t = re.search(r"^type:\s*(.+)$", fm, re.M)
            if not t or not t.group(1).strip():
                errors.append(f"{rel}: empty type")
            for ts in re.findall(r"\b(?:at|last_modified):[ \t]*([^\s,}]*)", fm):
                if not ISO.fullmatch(ts):
                    errors.append(f"{rel}: bad or empty timestamp: {ts!r}")
            if rel.parts[0] == "insights" and f.name != "index.md" and not re.search(r"^issues:\s*\[\s*\d", fm, re.M):
                errors.append(f"{rel}: an insight must list its issues")
    elif f.name == "index.md" and f.parent != WIKI and text.startswith("---"):
        errors.append(f"{rel}: only the root index.md may carry frontmatter")
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        if not (f.parent / target.split("#")[0]).resolve().exists():
            errors.append(f"{rel}: broken link {target}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"wiki ok: {len(list(WIKI.rglob('*.md')))} markdown files")
