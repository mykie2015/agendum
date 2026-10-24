---
type: Agendum Action
title: "Minimal observability with your own LLM proxy: can agent/harness calls be seen?"
description: "Worth a minimal \"run your own LLM proxy\" experiment: point at least one path (Claude Code / Codex / Cursor, etc.) at a proxy you control and confirm whether you can see which key, which client, which model, and cache hi…"
resource: https://github.com/mykie2015/agendum/issues/26
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 26
action_type: experiment
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/ }
  - { id: s2, resource: https://news.ycombinator.com/item?id=50145507 }
---

# Decision

Worth a minimal "run your own LLM proxy" experiment: point at least one path (Claude Code / Codex / Cursor, etc.) at a proxy you control and confirm whether you can see which key, which client, which model, and cache hits/failures. This directly serves harness cost and the #8 credential boundary; Experiment before Build.

# Summary

Spend 1–2 hours checking whether "seeing the calls" changes your judgment about the harness and costs; whether it runs or fails, leave a clear yes/no.

# Limits

The essay is short and manifesto-like; it gives no reproducible configuration. The experiment must choose a specific open-source/self-hosted implementation and record its version in the notes.

# Next steps

- [ ] Choose the self-hosted option and record the version/deployment method (local or an existing machine)
- [ ] Create a virtual key; point 1 coding agent at that endpoint
- [ ] Run 1 small task and record whether the log contains: time, model, client, status, approximate tokens/cost
- [ ] Half-page note: keep the proxy or not; how it cross-links with #7/#8

# Updates

- Imported comment from the upstream issue (2026-10-22), translated into English.

# Sources

- https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/
- https://news.ycombinator.com/item?id=50145507

# Tracking

[Issue #26](https://github.com/mykie2015/agendum/issues/26) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
