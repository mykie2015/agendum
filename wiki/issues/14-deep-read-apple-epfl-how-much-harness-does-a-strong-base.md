---
type: Agendum Action
title: "Deep read: Apple/EPFL \"how much harness does a strong base need\": a minimal coding agent vs #12 Harness²"
description: "Worth a close read this week, laid side by side with #12 in a comparison table."
resource: https://github.com/mykie2015/agendum/issues/14
tags: [read, p1, ai, agent, harness]
status: draft
issue: 14
action_type: read
priority: p1
state: open
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://machinelearning.apple.com/research/harness-autonomous-ml-engineering }
  - { id: s2, resource: https://arxiv.org/abs/2609.40303 }
  - { id: s3, resource: https://arxiv.org/abs/2607.03691 }
  - { id: s4, resource: https://news.ycombinator.com/item?id=50139872 }
---

# Decision

Worth a close read this week, laid side by side with #12 in a comparison table. The conclusion applies only to "strong base + coding-agent environment + MLE-type tasks"; cite it with its boundary conditions. Numbers in the paper are as in the original and were not reproduced locally.

# Summary

A paper with ablations, matched comparisons, and a limitations section arguing that a minimal harness is enough. This week's goal is to read the abstract, the §4 ablations, the §5 comparison, and Limitations, and produce a table of "which harness layers earn their keep," lined up item by item against #12's eight components. No experiment reproduction (it needs thousands of GPU hours).

# Limits

Mainly based on MLE-bench (known bugs and contamination risk, partly mitigated by the authors) and NatureBench (few models and methods).

# Next steps

- [ ] Read the abstract + Contributions + §4 (the four ablations)
- [ ] Read §5 (comparison with MLEvolve / AiScientist / Arbor / ScienceFlow) + Limitations
- [ ] Build a comparison table: layers this paper cuts vs the eight components of #12 Harness², marking each "earns its keep / redundant / depends on base strength"
- [ ] Write 3–5 personal-harness slimming rules (for example: give it a shell + filesystem first, then consider outer orchestration)

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.

# Sources

- https://machinelearning.apple.com/research/harness-autonomous-ml-engineering
- https://arxiv.org/abs/2609.40303
- https://arxiv.org/abs/2607.03691
- https://news.ycombinator.com/item?id=50139872

# Tracking

[Issue #14](https://github.com/mykie2015/agendum/issues/14) · READ · P1 · S · about 1.5 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
