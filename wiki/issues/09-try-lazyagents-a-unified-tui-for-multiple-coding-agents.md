---
type: Agendum Action
title: "Try Lazyagents, a unified TUI for multiple coding agents"
description: "Worth about 30–60 minutes to install Lazyagents (v0.2.2), run lazyagents doctor against the Claude Code / Codex / OpenCode (if any) already on this machine, then try the Skills / Sessions / Usage pages in the TUI: can y…"
resource: https://github.com/mykie2015/agendum/issues/9
tags: [experiment, p1, ai, agent, opensource]
status: draft
issue: 9
action_type: experiment
priority: p1
state: open
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://github.com/rogeriojunior31/lazyagents }
  - { id: s2, resource: https://rogeriojunior31.github.io/en/docs/lazyagents/ }
  - { id: s3, resource: https://rogeriojunior31.github.io/en/projects/lazyagents/ }
  - { id: s4, resource: https://news.ycombinator.com/item?id=50136701 }
---

# Decision

Worth about 30–60 minutes to install Lazyagents (v0.2.2), run `lazyagents doctor` against the Claude Code / Codex / OpenCode (if any) already on this machine, then try the Skills / Sessions / Usage pages in the TUI: can you see cross-agent skill toggles, session lists, and usage at a glance? This is the smallest verifiable slice of a "daily operations surface for multiple coding agents." It builds no harness and only judges whether the management layer is worth keeping.

# Insight

Lazyagents is a small, installable indie TUI that covers the coding agents the user commonly runs. Spend under an hour verifying whether "doctor + the three pages" is actually good, then decide whether to keep it, instead of merely bookmarking a Show HN.

# Limits

Only 5 ★ (cite with a date); popularity is not a basis for the decision

# Next steps

- [ ] After reading the Safety docs, install v0.2.2 (or the latest Release), run `lazyagents doctor`, and record which agents are detected
- [ ] Open the TUI: spend 2–3 minutes each on Skills / Sessions / Usage, and do one reversible enable/disable of an existing skill (if the safety boundary allows)
- [ ] Try finding a recent Claude Code or Codex session in Sessions and open/resume it (per the docs)
- [ ] Half-page note: keep / do not keep + three concrete reasons (including any docs version number or detection failure)

# Sources

- https://github.com/rogeriojunior31/lazyagents
- https://rogeriojunior31.github.io/en/docs/lazyagents/
- https://rogeriojunior31.github.io/en/projects/lazyagents/
- https://news.ycombinator.com/item?id=50136701

# Tracking

[Issue #9](https://github.com/mykie2015/agendum/issues/9) · EXPERIMENT · P1 · S · within 1 hour · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
