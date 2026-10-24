# Agendum

<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="Agendum: a personal signal-to-action system that turns information into evidence-backed decisions and concrete next steps.">
</p>

> **From signals to things worth doing.**

Agendum is the decision layer for GeekJourney's personal research workflow.

It collects signals from HN, AI news, X, GitHub, newsletters, saved reading, and project discovery; verifies the evidence; decides what matters; and turns the few signals worth attention into concrete actions.

The goal is simple:

**Don't give me more information. Help me decide what to do next.**

---

## The loop

```text
Signals
  HN · AIHot · X · GitHub · Newsletters · Ideas
                         ↓
         /last30days <topic>   (first step: collect)
                         ↓
                    Aggregate
                         ↓
                 Deduplicate / Cluster
                         ↓
                  Verify Evidence
                         ↓
                     Judge
                         ↓
                    Decide
                         ↓
                      Act
                         ↓
              Read · Research · Test
          Build · Write · Post · Update
                    · Buy · Watch
```

Agendum sits after the information radars and before the work itself.

| Layer | Role |
| --- | --- |
| **Radar** | Find signals worth looking at. Start with `/last30days <topic>` |
| **Agendum** | Decide which signals deserve attention and action |
| **GitHub Issues** | Turn decisions into a visible action queue |
| **Projects / Content / Experiments** | Produce the real-world outcome |

---

## What counts as an action?

A signal becomes an Agendum only when there is a clear decision and a useful next step.

Typical actions:

- **READ** — read something worth understanding deeply
- **TRANSLATE** — translate a high-value article when appropriate
- **RESEARCH** — investigate a technology, trend, or opportunity
- **EXPERIMENT** — run a small test before committing to a build
- **BUILD** — create a product, tool, or open-source project
- **WRITE** — turn a validated observation into an article
- **POST** — share a useful insight on X
- **UPDATE** — improve a project, README, or personal website
- **DOMAIN** — evaluate or acquire a domain when the opportunity is real
- **BUY** — purchase a tool or service when there is a concrete reason
- **WATCH** — keep observing without forcing an action

The system should prefer **few high-confidence actions over a large backlog**.

---

## Evidence before action

Every meaningful decision should be traceable:

```text
Signal
  ↓
Original source
  ↓
Independent verification
  ↓
Context
  ↓
Reasoning
  ↓
Decision
  ↓
Next action
```

Primary evidence is preferred:

1. Official announcement
2. Official documentation
3. GitHub repository / release / commit
4. Original paper
5. Author or maintainer post
6. Hacker News discussion
7. High-quality secondary reporting

A popular post is a signal.

**Evidence is what makes it a decision.**

---

## Issue-driven workflow

GitHub Issues are the operational queue. An issue exists so a reader can decide in a minute, execute, and record what happened. The form follows that order:

**decision → trust / evidence → understand → act → learn**

| Stage | What to record |
| --- | --- |
| **Decision** | Type, priority (`P0` / `P1` / `P2` / `WATCH`), effort, the one-line judgment, and why it is worth doing now |
| **Trust / evidence** | Evidence chain, then the channel where the signal was found |
| **Understand** | What happened, the breakdown, and a summary of at most three sentences |
| **Act** | The next step, the expected result, and the standard for done |
| **Learn** | Progress log, result / review, and the follow-up decision |

`WATCH` as priority means keep observing and apply no `p0` / `p1` / `p2` label.

Recommended titles use `[TYPE] YYYY-MM-DD · one-line decision / action`:

```text
[READ] Deep read: ...
[RESEARCH] Investigate: ...
[EXPERIMENT] Test: ...
[BUILD] Prototype: ...
[WRITE] Article: ...
[POST] X thread: ...
[UPDATE] Website / README: ...
[DOMAIN] Evaluate: ...
[WATCH] Monitor: ...
```

Agents that create Issues through the API should start from [docs/issue-body-skeleton.md](docs/issue-body-skeleton.md). Those `###` headings must match the form output exactly. The label workflow reads only the first non-empty line under `### Event type` and `### Priority`.

If the decision, the evidence, and the next step cannot be filled in, the signal should not become an Issue yet.

---

## Research inputs

Agendum is designed to consume multiple upstream sources rather than becoming another news feed.

**First step: `/last30days <topic>`.** It pulls Reddit, X, YouTube, HN, GitHub, and the web for the last 30 days. Agendum triages that output and turns the few items that pass into issues. See [docs/last30days-intake.md](docs/last30days-intake.md).

### Core

- Hacker News signals
- AI / Agent / Harness research
- AIHot
- GitHub projects and releases
- X first-hand signals
- X bookmarks and saved items
- X discussions from followed accounts
- Gmail / Outlook newsletters and high-value email
- Weekly Wisereads
- Ruan Yifeng's weekly (Tech Enthusiast Weekly)
- Small creative projects and product opportunities

### Focus

Particular attention goes to:

- Agent and Coding Agent
- Harness engineering
- RSI / RRSI
- Model capability and post-training
- Agent benchmarks and evaluation
- Cost / task, steps, cache, latency, and long-running execution
- Developer tools and open source
- AI-native products
- Independent development and distribution
- Content systems and personal websites
- AI video and creative tooling
- Apple / iOS / Apple Watch experiments

---

## Decision rules

### Signal Value > Popularity

High points, stars, likes, or reposts do not automatically make something important.

### Experiment before building

When an idea can be tested cheaply, create an **EXPERIMENT** before a **BUILD**.

### One signal, one decision

If HN, X, GitHub, and AI news all describe the same development, consolidate the evidence into one decision.

### No forced actions

A quiet day is a valid result.

If nothing deserves action, record:

```text
Today: No Action
```

### Time is the scarce resource

The system should optimize for:

**less noise → better judgment → better use of time**

---

## Priority

| Priority | Meaning |
| --- | --- |
| **P0** | Act today; time-sensitive or strategically important |
| **P1** | Worth doing this week |
| **P2** | Useful backlog item |
| **WATCH** | Keep observing; no commitment yet |

The default bias is toward **P1 and small experiments**, not large commitments.

---

## Daily decision memo

The final daily output should be short:

```text
GeekJourney Action — YYYY-MM-DD

Valid signals: X
Actions created: X

P0
1. ...

P1
1. ...

Most important decision
...

Best thing to do today
...

Watch
...
```

The output is a decision memo, not a news dump.

---

## Weekly review

Once a week, consolidate:

- the strongest signals
- repeated patterns
- useful saved reading
- new projects
- emerging product opportunities
- unfinished actions
- decisions that changed
- actions to keep, drop, or double down on

The objective is to move from:

```text
Daily signals
    ↓
Weekly patterns
    ↓
Monthly trends
    ↓
Strategic thesis
```

---

## Wiki: what the issues add up to

`wiki/` is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (v0.2) bundle. Its point is **insight**, not a record of the workflow. Start at [wiki/index.md](wiki/index.md).

- **Insight pages** (`wiki/insights/`) are the product. Each one makes a claim across one or more related issues, and gives the evidence with its strength, the tension, what to do, what would change my mind, and the gaps. They are written, not extracted, and they start as `status: draft` with a stated `confidence`.
- **Issue pages** (`wiki/issues/`) are the evidence ledger: decision, summary, limits, next steps, result. They are generated from the issues and link back to the insights that use them.
- **Views**: topic digests, the open-action queue, an `insights/index.md` list of issues that still wait for synthesis, and two charts.
- **Concepts** (`wiki/concepts/`) hold hand-written fact sheets and diagrams, for example the Claude Duet verified-scope table for #62.

```bash
python3 scripts/build-wiki.py   # fetch issues with gh and rewrite generated pages
python3 scripts/check-wiki.py   # check OKF v0.2 conformance
```

To add an insight, create `wiki/insights/<claim>.md` with `type: Insight`, an `issues: [..]` list, and `confidence`. Write `[#N]` in the body and the build turns it into a link to the issue page. A good insight states a claim someone could disagree with, shows evidence from at least one issue, names a counter-case, and ends with an action. A page that only restates what an issue did is not an insight.

- Generated: `wiki/issues/`, `wiki/topics/`, `wiki/queue.md`, `wiki/index.md`, `wiki/insights/index.md`, `wiki/log.md`, `wiki/images/actions-by-*.svg`.
- Never overwritten: `wiki/insights/<claim>.md`, `wiki/concepts/`, `wiki/images/issue-*.svg`.
- `.github/workflows/build-wiki.yml` rebuilds the generated pages whenever an issue changes.
- Pages state who produced them and carry no `verified` key, so they are unverified until a person reviews them.

---

## Repository structure

```text
agendum/
├── README.md
├── assets/
│   └── readme/
│       └── hero.svg
├── docs/
│   ├── issue-body-skeleton.md
│   └── last30days-intake.md
├── wiki/                 (OKF bundle: insights, issue ledger, concepts)
├── scripts/
│   ├── build-wiki.py
│   └── check-wiki.py
├── reports/
│   └── YYYY/
│       └── MM/
│           └── DD.md
├── weekly/
│   └── YYYY-WXX.md
├── actions/
│   └── YYYY/
│       └── MM/
│           └── DD.md
└── evidence/
    └── YYYY/
        └── MM/
```

The repository can evolve as the workflow becomes more automated.

---

## Operating principle

> **Information is cheap. Attention is expensive. Action is the goal.**

Agendum is the layer that turns a growing stream of information into a smaller, clearer queue of things worth doing.



## Email is a signal source, not an inbox to summarize

Newsletter and email are part of Agendum's upstream information system.

The goal is **not** to produce another inbox digest. For Gmail / Outlook and other newsletter sources:

1. Scan the available high-signal newsletters and relevant email.
2. Deduplicate stories that already appeared in HN, AIHot, X, GitHub, or other sources.
3. Identify the few items that deserve the user's attention.
4. Verify important claims against the original source.
5. Decide whether each item should become **READ / RESEARCH / EXPERIMENT / BUILD / WRITE / POST / UPDATE / DOMAIN / BUY / WATCH**.
6. Create an Issue only when there is a concrete decision and useful next action.

The desired transformation is:

```text
Newsletter / Email
      ↓
Signal extraction
      ↓
Deduplication
      ↓
Evidence verification
      ↓
Judgment
      ↓
Decision
      ↓
Action Issue
```

**Email is an information source, not an inbox to summarize. Extract the few signals worth acting on.**

## Issue-driven operations

Agendum uses a structured GitHub Issue form as the bridge from research to execution.

Each Action records:

**decision → trust / evidence → understand → act → learn**

The repository also maintains a small machine-readable label vocabulary for action type, priority, and topic. See [Issue Label Specification](.github/ISSUE_LABELS.md). API-created issues use the headings in [docs/issue-body-skeleton.md](docs/issue-body-skeleton.md).

The intended workflow is:

```text
Signal
  ↓
Evidence
  ↓
Decision
  ↓
GitHub Issue
  ↓
Progress
  ↓
Result
  ↓
Next Decision
```
