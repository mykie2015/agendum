---
type: Agendum Action
title: "Deep read: Doc2Harness and a checklist of harness failure modes"
description: "Worth a close read to extract failure modes, not worth running the full benchmark this week: first turn \"how to split cross-cutting modules and how to prevent vacuous passes\" into an executable checklist."
resource: https://github.com/mykie2015/agendum/issues/5
tags: [read, p1, ai, agent, harness]
status: draft
issue: 5
action_type: read
priority: p1
state: open
created: 2026-10-17
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.20344 }
  - { id: s2, resource: https://geyuyao.com/doc2harness/ }
  - { id: s3, resource: https://github.com/YuyaoGe/doc2harness }
  - { id: s4, resource: https://x.com/HuggingPapers/status/2110765616101540224 }
  - { id: s5, resource: https://x.com/ComputerPapers/status/2110973887458541658 }
  - { id: s6, resource: https://x.com/al3rez/status/2111268459107733706 }
---

# Decision

Worth a close read to extract failure modes, not worth running the full benchmark this week: first turn "how to split cross-cutting modules and how to prevent vacuous passes" into an executable checklist.

# Summary

This is the first hard yardstick that evaluates harness engineering ability, rather than coding on a fixed harness. The goal of a close read is not to reproduce all 328 cases, but to extract failure modes and positive-control ideas that transfer to a personal harness checklist.

# Used in insights

* [Where harness changes do raise accuracy, the mechanism is an independent check against real state](../insights/accuracy-gains-come-from-an-independent-second-look.md)
* [At a strong base model, the harness is mostly a cost lever, not an accuracy lever](../insights/harness-is-a-cost-lever-at-a-strong-base.md)

# Next steps

- [ ] Read the Abstract, §2 (two stages / positive control), and §4.1–4.3 (results and architecture correlations)
- [ ] Skim the YuyaoGe/doc2harness README and confirm the smallest runnable local scope (no full reproduction required this week)
- [ ] Write 5–10 rules that transfer to a personal harness (cross-cutting splits, four-channel observation, preventing vacuous passes)
- [ ] Decide whether to open a separate EXPERIMENT for a subset (open it only with a clear subset and budget; do not do it by default in this issue)

# Sources

- https://arxiv.org/abs/2610.20344
- https://geyuyao.com/doc2harness/
- https://github.com/YuyaoGe/doc2harness
- https://x.com/HuggingPapers/status/2110765616101540224
- https://x.com/ComputerPapers/status/2110973887458541658
- https://x.com/al3rez/status/2111268459107733706

# Tracking

[Issue #5](https://github.com/mykie2015/agendum/issues/5) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
