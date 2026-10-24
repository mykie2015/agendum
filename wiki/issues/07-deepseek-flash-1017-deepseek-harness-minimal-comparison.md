---
type: Agendum Action
title: "DeepSeek Flash-1017 × DeepSeek Harness minimal comparison"
description: "Worth 1–2 hours for a minimal \"same model, different harness\" comparison: run the same small task with DeepSeek-V4.1-Flash-1017 on DeepSeek Harness (≥0.2.1-rc.1) and on Claude Code / Codex, and try the Search/Fetch API…"
resource: https://github.com/mykie2015/agendum/issues/7
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 7
action_type: experiment
priority: p1
state: open
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://api-docs.deepseek.com/zh-cn/updates/ }
  - { id: s2, resource: https://github.com/deepseek-ai/deepseek-harness }
  - { id: s3, resource: https://deepseek-harness.github.io/deepseek-harness/ }
  - { id: s4, resource: https://deepseek.com/harness }
  - { id: s5, resource: https://aihot.news/story/f8045374-7106-49b1-8fd8-ce824a952e45 }
  - { id: s6, resource: https://x.com/leo114119/status/2111484227648881109 }
---

# Decision

Worth 1–2 hours for a minimal "same model, different harness" comparison: run the same small task with DeepSeek-V4.1-Flash-1017 on DeepSeek Harness (≥0.2.1-rc.1) and on Claude Code / Codex, and try the Search/Fetch API along the way. This directly tests whether "model and harness co-training / co-optimization" is perceptible, and it is orthogonal and complementary to #5 Doc2Harness (which scores harness engineering).

# Summary

The actionable edge of Flash-1017 is harness co-optimization and a time-limited free Search API, not reading another release post. Spend 1–2 hours testing whether "same model across harnesses" is perceptible, then decide whether to add it to the daily stack.

# Used in insights

* [Scope words and multipliers inflate between a vendor's text and its retellings](../insights/launch-claims-inflate-between-source-and-retelling.md)

# Limits

For example @leo114119's pelican test claims Flash-1017 is better on DeepSeek Harness/Codex (https://x.com/leo114119/status/2111484227648881109). Use it only as a "worth testing yourself" signal and do not adopt its numbers

# Next steps

- [ ] After reading SAFETY.md / the official Web UI guide, get it running locally with `npx `@deepseek-ai/dsh` web` or upgrade to ≥0.2.1-rc.1
- [ ] Fix one small, verifiable task (for example: change the layout of an existing small page and write 3 tests, or generate a CLI and run it yourself)
- [ ] Run the same task once on DeepSeek Harness and once on Claude Code (or Codex); record wall-clock time, rough tokens/cost, whether it passed acceptance on the first try, and subjective sticking points
- [ ] Call Search and Fetch 1–2 times each; record latency and result usefulness (no production integration)
- [ ] Produce a half-page note: whether to keep deepseek-flash as a low-cost fallback; which differences look caused by the harness and which look like noise

# Updates

- Imported comment from the upstream issue (2026-10-18), translated into English.
- Imported comment from the upstream issue (2026-10-19), translated into English.
- Imported comment from the upstream issue (2026-10-19), translated into English.
- Imported comment from the upstream issue (2026-10-20), translated into English.
- Imported comment from the upstream issue (2026-10-20), translated into English.

# Sources

- https://api-docs.deepseek.com/zh-cn/updates/
- https://github.com/deepseek-ai/deepseek-harness
- https://deepseek-harness.github.io/deepseek-harness/
- https://deepseek.com/harness
- https://aihot.news/story/f8045374-7106-49b1-8fd8-ce824a952e45
- https://x.com/leo114119/status/2111484227648881109

# Tracking

[Issue #7](https://github.com/mykie2015/agendum/issues/7) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
