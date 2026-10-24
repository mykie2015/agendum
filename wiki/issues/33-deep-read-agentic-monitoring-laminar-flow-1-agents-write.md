---
type: Agendum Action
title: "Deep read: Agentic Monitoring + Laminar flow-1: agents write monitoring specs, deterministic execution, traces queried like a repo"
description: "Worth a close read, plus a comparison against Agendum itself."
resource: https://github.com/mykie2015/agendum/issues/33
tags: [read, p1, ai, agent, harness]
status: draft
issue: 33
action_type: read
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://benjamincongdon.me/blog/2026/10/19/Agentic-Monitoring/ }
  - { id: s2, resource: https://laminar.sh/blog/flow-1 }
  - { id: s3, resource: https://news.ycombinator.com/item?id=50154029 }
  - { id: s4, resource: https://github.com/lmnr-ai/lmnr }
  - { id: s5, resource: https://news.ycombinator.com/item?id=50153225 }
---

# Decision

Worth a close read, plus a comparison against Agendum itself. Two first-hand sources approach the same thing from both ends: using agents to watch systems and to watch other agents. Ben Congdon's practice piece gives a structural conclusion: a pure agent loop is not the best form of monitoring; better to have the agent write a spec for "how to monitor" and let a deterministic system run that spec. Laminar's Launch HN gives the other half: treat one agent trace as a code repository and each span (one model call or tool call) as a file, and let a small model grep, read, and conclude like a coding agent. This is the same line as #29 Meta's thin orchestrator, "deterministic routing + a few steps that need judgment."

# Summary

Agents watching systems and watching agents are already usable; the key is the division of labor: the agent writes the "what to watch" spec and explains anomalies, while a deterministic program executes the spec and keeps the records. Laminar applies this division to agent traces and pushes the unit price low enough to run on everything. For Agendum, the smallest landing is a one-page monitoring spec plus a check script.

# Limits

Congdon's quoted Anthropic "superfans" passage was not checked against the original post; his prototype is not open-sourced and gives no numbers for "regression detection precision and latency." Laminar's benchmark is a self-built set of 523 traces with self-reported results; in the table Claude Opus 5's detection F1 (.890) is above flow-1's (.835), and flow-1's advantage is unit price (888 traces per dollar versus…

# Next steps

- [ ] Read Congdon's full text closely and excerpt the "spec + deterministic execution" passage and the three secrets
- [ ] Read Laminar's flow-1 blog benchmark table and 4 cases closely, noting the types it catches and misses
- [ ] Write a one-page monitoring spec draft for Agendum, listing 5 rules that can be checked deterministically
- [ ] Let the user decide whether to make the check script a separate EXPERIMENT

# Updates

- Imported comment from the upstream issue (2026-10-23), translated into English.

# Sources

- https://benjamincongdon.me/blog/2026/10/19/Agentic-Monitoring/
- https://laminar.sh/blog/flow-1
- https://news.ycombinator.com/item?id=50154029
- https://github.com/lmnr-ai/lmnr
- https://news.ycombinator.com/item?id=50153225

# Tracking

[Issue #33](https://github.com/mykie2015/agendum/issues/33) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
