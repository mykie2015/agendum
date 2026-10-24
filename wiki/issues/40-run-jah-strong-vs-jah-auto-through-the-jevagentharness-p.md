---
type: Agendum Action
title: "Run jah-strong vs jah-auto through the JevAgentHarness proxy: does tiered routing save money on my tasks"
description: "Worth a small experiment."
resource: https://github.com/mykie2015/agendum/issues/40
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 40
action_type: experiment
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.21412 }
  - { id: s2, resource: https://github.com/JevAgentHarness/JevAgentHarness }
  - { id: s3, resource: https://huggingface.co/JevAgentHarness }
---

# Decision

Worth a small experiment. JevAgentHarness (JAH for short) puts a Jev-style "decision model" inside a local OpenAI-compatible proxy: at every step the coding agent takes, a small model first asks "is this step routine or hard?"; routine steps go to a cheap model and hard ones stay with the strong model, with no change to the harness itself. Both the paper and the README report the failing configurations too: when the price gap is not large enough, or the strong model is already fully using the prompt cache, it saves almost nothing or is even slower. That answers "should my own coding agent use tiered routing?", and running jah-strong against jah-auto once is more useful than reading a few more routing articles.

# Summary

Tiered routing can save money, provided the unit price gap between the two tiers is large and the strong model is not already made cheap by caching. JAH lays out both positive and negative results, and it is a local proxy that does not change the harness. Run jah-strong vs jah-auto once on one small task of your own, look at the strong-model share and the cost, and that decides whether routing goes into the daily coding-agent workflow.

# Limits

Each harness ran only once on the 74 Terminal-Bench 2.0 test tasks, with wide confidence intervals, and the author says the success-rate column can only be read as "no obvious drop seen"; the Terminus-2 baseline row has 53/74 timeouts, which the author marks as inconclusive; Codex + GPT-6.1 Sol / GPT-6 Luna was tested on only 20 tasks, saving 6.5% while taking 47% longer; AgentDecision-4B is under a non-commercial l…

# Next steps

- [ ] Install with `pip install -e .` and generate a config with `jah init`; start with the `{type: rules}` decision mode (no decision-model key), pick strong and fast tiers from models you already have keys for, aiming for a price gap above 4×
- [ ] With pi or DeepSeek Harness (shared environment with #7), pick 1 small task in your own repo and run `jah-strong` and `jah-auto` once each
- [ ] Record with `jah report`: steps, strong-model share, cost, LLM time, whether it finished; add a Jev decision group if you have an OpenRouter key
- [ ] Comment the conclusion on this issue, and add a note in #26 on "can JAH logs serve as the proxy observability layer"

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.
- Imported comment from the upstream issue (2026-10-23), translated into English.
- Imported comment from the upstream issue (2026-10-23), translated into English.

# Sources

- https://arxiv.org/abs/2610.21412
- https://github.com/JevAgentHarness/JevAgentHarness
- https://huggingface.co/JevAgentHarness

# Tracking

[Issue #40](https://github.com/mykie2015/agendum/issues/40) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
