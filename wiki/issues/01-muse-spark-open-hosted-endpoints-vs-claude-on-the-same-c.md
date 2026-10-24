---
type: Agendum Action
title: "Muse Spark Open hosted endpoints vs Claude on the same coding task"
description: "Worth testing on a real coding task instead of chasing leaderboards: the result directly decides whether it enters the default harness."
resource: https://github.com/mykie2015/agendum/issues/1
tags: [experiment, p1, ai, agent, opensource]
status: stable
issue: 1
action_type: experiment
priority: p1
state: closed
created: 2026-10-16
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://research.meta.ai/blog/muse-spark-open }
  - { id: s2, resource: https://pytorch.org/blog/muse-spark-open/ }
  - { id: s3, resource: https://x.com/finkd/status/2110778025629347999 }
  - { id: s4, resource: https://modal.com/blog/meta-muse-spark-open-now-available-on-modal }
  - { id: s5, resource: https://www.lmsys.org/blog/2026-10-15-meta-muse-spark-open }
  - { id: s6, resource: https://machinelearning.apple.com/research/mlx-distributed-inference }
  - { id: s7, resource: https://news.ycombinator.com/item?id=50107379 }
  - { id: s8, resource: https://x.com/AIatMeta/status/2110779754274292212 }
---

# Decision

Worth testing on a real coding task instead of chasing leaderboards: the result directly decides whether it enters the default harness.

# Summary

Muse Spark Open turns "open-weight coding agent base" from a slogan into something you can test in two hours. The real question is whether, on one real task, its step count, human intervention, cost, and reliability can approach Claude/Codex. The answer decides whether it enters your default toolchain, and it is also material for a harness article with first-hand data.

# Next steps

- [ ] Read the Meta / PyTorch posts closely; confirm the license and the safety post-training boundary
- [ ] Pick one hosted entry point (Modal first, or any on the Day-0 list)
- [ ] Prepare one coding task you know well, with acceptance criteria
- [ ] Run Muse Spark Open and Claude (or Codex) separately; record step count, failure points, human intervention, rough cost, and felt latency
- [ ] Write a 5–10 line note on whether it goes into the default toolchain

# Sources

- https://research.meta.ai/blog/muse-spark-open
- https://pytorch.org/blog/muse-spark-open/
- https://x.com/finkd/status/2110778025629347999
- https://modal.com/blog/meta-muse-spark-open-now-available-on-modal
- https://www.lmsys.org/blog/2026-10-15-meta-muse-spark-open
- https://machinelearning.apple.com/research/mlx-distributed-inference
- https://news.ycombinator.com/item?id=50107379
- https://x.com/AIatMeta/status/2110779754274292212

# Tracking

[Issue #1](https://github.com/mykie2015/agendum/issues/1) · EXPERIMENT · P1 · S · 1–2 hours · closed

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
