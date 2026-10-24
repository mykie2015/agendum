---
type: Agendum Action
title: "xerj local retrieval layer: test whether it saves coding-agent tokens"
description: "Worth 1–2 hours to index one of my own small or mid-sized repos with xerj (Apache-2.0) on this machine, then run the same coding-agent task twice: \"default grep / read files\" versus \"retrieval through xerj/MCP.\" Record…"
resource: https://github.com/mykie2015/agendum/issues/10
tags: [experiment, p1, ai, agent, opensource]
status: draft
issue: 10
action_type: experiment
priority: p1
state: open
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://github.com/xerj-org/xerj }
  - { id: s2, resource: https://xerj.org }
  - { id: s3, resource: https://xerj.org/case-studies/reference-coding.html }
  - { id: s4, resource: https://x.com/thedevfeed/status/2111493032868790775 }
---

# Decision

Worth 1–2 hours to index one of my own small or mid-sized repos with xerj (Apache-2.0) on this machine, then run the same coding-agent task twice: "default grep / read files" versus "retrieval through xerj/MCP." Record only local output tokens / wall-clock time / whether it passed acceptance. The goal is not to chase stars but to check the harness/cost proposition "is a retrieval layer cheaper than switching models?" Any marketing "40×" claim is not adopted; go by the official case study's 2.7× and the numbers measured here.

# Insight

xerj deserves one A/B on my own repo, using local numbers to decide whether a retrieval middle layer joins the default coding-agent stack, and refusing to treat trending multiples as conclusions.

# Limits

★7842 must be cited with a date; an unusually high star count is not a reason to adopt it immediately

# Next steps

- [ ] Install the single binary per the official docs and get indexing working on one small or mid-sized own repo (record index time and index size)
- [ ] Fix one verifiable task (for example: locate and fix a known small bug, or answer "the call chain of some module" and submit a minimal diff)
- [ ] With the same agent and the same prompt skeleton, run once without xerj and once with xerj (MCP or the docs' recommended integration); record output tokens (or proxy bill), wall-clock time, and whether it passed acceptance on the first try
- [ ] Half-page note: yes/no keep + the local relative difference + an explicit list of unadopted claims such as 40×

# Sources

- https://github.com/xerj-org/xerj
- https://xerj.org
- https://xerj.org/case-studies/reference-coding.html
- https://x.com/thedevfeed/status/2111493032868790775

# Tracking

[Issue #10](https://github.com/mykie2015/agendum/issues/10) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
