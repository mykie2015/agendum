---
type: Agendum Action
title: "Deep read: OpenAI on agents suppressing misalignment-monitoring alerts and denying removing monitoring in coding tasks"
description: "Deep read: OpenAI on agents suppressing misalignment-monitoring alerts and denying removing monitoring in coding tasks"
resource: https://github.com/mykie2015/agendum/issues/42
tags: [read, p1, ai, agent]
status: draft
issue: 42
action_type: read
priority: p1
state: open
created: 2026-10-21
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/ }
  - { id: s2, resource: https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization }
  - { id: s3, resource: https://x.com/Marcus_J_W/status/2112695138199966084 }
---

# Decision

Deep read: OpenAI on agents suppressing misalignment-monitoring alerts and denying removing monitoring in coding tasks

# Summary

OpenAI published the full trajectories of two internal coding agents weakening misalignment monitoring: one turned off alerts using "don't send messages," and one removed monitoring while aligning with a reference implementation and denied it. What to read is the failure paths and the hard-gate design, not the buzz. It can be combined with #37 into a "overreach / turning off monitoring" topic, and you can also check whether your own agents can change monitoring and permissions.

# Used in insights

* [A proactive agent is defined by where its approval boundary sits and what happens when it fails](../insights/proactive-agents-are-defined-by-their-approval-boundary.md)

# Limits

Neither case was P0 and neither trajectory was killed automatically; OpenAI has not concluded that this was "specifically to evade monitoring"; many internal harness details are redacted; the X posts are mostly second-hand reposts, so go by the Alignment original.

# Next steps

- [ ] Read the two incidents + Investigation and response closely
- [ ] Compare with #37 and decide whether to merge them into one "coding agent overreach / turning off monitoring" topic (a suggestion only, no tweeting)
- [ ] Decide whether to open a separate EXPERIMENT: check whether my Claude Code / Codex / personal agents can change logs, alerts, or allow-rules

# Updates

- Imported comment from the upstream issue (2026-10-23), translated into English.

# Sources

- https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/
- https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization
- https://x.com/Marcus_J_W/status/2112695138199966084

# Tracking

[Issue #42](https://github.com/mykie2015/agendum/issues/42) · READ · P1 · S · 45–60 minutes · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
