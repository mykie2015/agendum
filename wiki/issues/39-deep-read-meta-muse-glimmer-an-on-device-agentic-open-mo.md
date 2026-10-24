---
type: Agendum Action
title: "Deep read: Meta Muse Glimmer, an on-device agentic open model and its distillation recipe"
description: "Worth a close read of Meta's first-hand material: the technical report and launch post for Muse Glimmer (about 30B, Apache-2.0, aimed at local agents on a single consumer GPU)."
resource: https://github.com/mykie2015/agendum/issues/39
tags: [read, p1, ai, agent, opensource]
status: stable
issue: 39
action_type: read
priority: p1
state: closed
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model }
  - { id: s2, resource: https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/ }
  - { id: s3, resource: https://arxiv.org/abs/2610.24628 }
  - { id: s4, resource: https://huggingface.co/meta-models/Muse-Glimmer-30B }
---

# Decision

Worth a close read of Meta's first-hand material: the technical report and launch post for Muse Glimmer (about 30B, Apache-2.0, aimed at local agents on a single consumer GPU). The point is not chasing another leaderboard score but its **distillation recipe** (logit / full-KL co-distillation from Muse Spark → mid-training with long-horizon agent trajectories → post-training that mixes on-policy distillation and RL) and its capability claims on "failure recovery / tool calling / scaffold compatibility," which on-device Personal AI actually uses. Model-company articles get priority by default (the #15 preference); in this slot an AINews resurgence brought up the arXiv technical report (2610.24628, about 2026-10-17), and no issue had been created in the morning ledger.

# Summary

Meta has opened the weights and training story of the on-device agentic model Glimmer. This week spend one to two hours reading the blog + report abstract, extract notes on distillation and the hardware bar, and then decide whether to open a separate local-run EXPERIMENT.

# Limits

The blog date says August while the technical report is October, so go by the report and the HF card; specific scores such as MCP Atlas / DeepSearch / SWE-Bench were not checked table by table in this slot; weights were not downloaded locally; do not confuse it with the closed/internal "Muse Wonder Full" Arena variant

# Next steps

- [ ] Finish the Meta blog + the research page Abstract; skim the main arXiv evaluation table (mark "paper numbers, not reproduced locally")
- [ ] Note the hardware bar and inference stack options (llama.cpp / MLX / Ollama etc., per official docs)
- [ ] Write a half-page comparison: Glimmer (change weights by distillation) vs #12 Harness² (change the harness)
- [ ] Decide clearly: whether to open a separate EXPERIMENT (default no, unless this machine has ≥24GB VRAM/unified memory and a clear task)

# Updates

- Imported comment from the upstream issue (2026-10-20), translated into English.

# Sources

- https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
- https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/
- https://arxiv.org/abs/2610.24628
- https://huggingface.co/meta-models/Muse-Glimmer-30B

# Tracking

[Issue #39](https://github.com/mykie2015/agendum/issues/39) · READ · P1 · S · 1–2 hours · closed

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
