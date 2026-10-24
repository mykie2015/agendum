---
type: Agendum Action
title: "Try Claude Mods in 1–2h: turn the harness into a human-side Attention Interface"
description: "Worth a small experiment."
resource: https://github.com/mykie2015/agendum/issues/51
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 51
action_type: experiment
priority: p1
state: open
created: 2026-10-22
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://www.latent.space/p/claude-mods }
  - { id: s2, resource: https://code.claude.com/docs/en/plugins/mods/reference }
---

# Decision

Worth a small experiment. A first-hand methods post by swyx / Latent Space: Claude Mods flips the agent harness from "machine-facing" to "human attention-facing": programmable middleware (TS/JS) hooks the prompt/tool/UI and decides what interrupts you and what is shown. It has a built-in `you-should-know` side-channel agent + a self-built ModSmith template, and a comparison can be run on Claude Code in 1–2 hours; it is not yet another TUI wrapper. The open experiments on the same topic do not cover the "human-side Attention Interface / Mods."

# Summary

This week open `you-should-know` in Claude Code, then try one self-built/template mod, and note whether the interruptions help judgment; write the result into harness notes, without expanding into a platform BUILD.

# Limits

Mods not enabled on this machine; the state of the ModSmith repo goes by the links in the text at the time; "the harness becomes a platform" is the author's judgment, not an experimental conclusion

# Next steps

- [ ] Read the Mods reference and confirm the steps to enable `you-should-know`
- [ ] On a real small task, compare missed items and disturbance with the side-channel observer on vs off
- [ ] Optional: use plugin-authoring to have Claude generate a minimal "next step" button mod
- [ ] Write 3–5 transferable rules; comment the comparison against #14/#49

# Sources

- https://www.latent.space/p/claude-mods
- https://code.claude.com/docs/en/plugins/mods/reference

# Tracking

[Issue #51](https://github.com/mykie2015/agendum/issues/51) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
