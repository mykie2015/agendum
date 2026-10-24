---
type: Agendum Action
title: "Run DeskMind Brain locally: Jev-style decisions + harness co-training comparison"
description: "Worth one minimal local experiment (start Brain, watch probabilistic decisions and escalation), not worth reproducing the $600 training this week."
resource: https://github.com/mykie2015/agendum/issues/6
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 6
action_type: experiment
priority: p1
state: open
created: 2026-10-17
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://deskmind.dev/zh/blog/launch/ }
  - { id: s2, resource: https://github.com/deskmind-ai/brain }
  - { id: s3, resource: https://deskmind.dev }
  - { id: s4, resource: http://www.ruanyifeng.com/blog/2026/10/weekly-issue-415.html }
---

# Decision

Worth one minimal local experiment (start Brain, watch probabilistic decisions and escalation), not worth reproducing the $600 training this week. First write "the option space includes ask-the-user + completion is checked against state" into the personal harness checklist.

# Summary

DeskMind gives an executable path: a small decision model plus writing "ask the user / verify completion" into the harness's option space, instead of only piling on prompts. This week's goal is not to reproduce the full training but to start the Brain service locally, get one `/v1/systemone` call working, and note how the ask/verify interface carries over to a personal harness.

# Next steps

- [ ] Clone `deskmind-ai/brain` and start `/v1/systemone` with MLX per the README (or the minimal path in the docs)
- [ ] Send one multiple-choice question from the examples and record the 0.8B→4B escalation behavior (if local memory is not enough, only read the code path and mark it DEGRADED)
- [ ] From the blog, extract the "ask-the-user option / completion-state verification / label-smoothing pitfall" into a checklist of at least 5 items
- [ ] Decide: open a separate Hands/App experiment, or WATCH the training details for now

# Sources

- https://deskmind.dev/zh/blog/launch/
- https://github.com/deskmind-ai/brain
- https://deskmind.dev
- http://www.ruanyifeng.com/blog/2026/10/weekly-issue-415.html

# Tracking

[Issue #6](https://github.com/mykie2015/agendum/issues/6) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
