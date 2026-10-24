---
type: Agendum Action
title: "Run pi-durable-news-agent offline: the Hype / Facts / Signal three-score system vs Agendum's gates"
description: "Worth running the offline mode locally once and comparing it with Agendum's filtering gates."
resource: https://github.com/mykie2015/agendum/issues/36
tags: [experiment, p1, ai, agent, opensource]
status: stable
issue: 36
action_type: experiment
priority: p1
state: closed
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://github.com/disler/pi-durable-news-agent }
  - { id: s2, resource: https://youtu.be/OLqP8jxJ0Wc }
  - { id: s3, resource: https://www.npmjs.com/package/@earendil-works/pi-durable }
---

# Decision

Worth running the offline mode locally once and comparing it with Agendum's filtering gates. disler's newly open-sourced pi-durable-news-agent is almost another implementation of Agendum: cron wakes a resumable agent on a schedule, scans 28 sources (including HN and GitHub releases), uses jev for cheap judgments at every gate, merges duplicate stories, takes the top 7 and sends research sub-agents to dig deeper, and finally gives each one three scores: Hype / Facts / Signal. Its "Signal = information you can act on right now" and Agendum's "from signals to things worth doing" are the same goal, and it splits judgment into 6 independent jev commands, which is just right for checking the judgment steps now mixed together in Agendum's single large skill.

# Insight

This is a clearly structured open-source "signal filtering agent" with almost the same goal as Agendum. Run it offline first, look at its 6 small gates and the three-score system, then decide whether Agendum should split one big judgment into several small ones.

# Limits

The repo is very new with few stars and no independent reproduction; real mode needs an OpenRouter key, and whether jev itself needs an extra service was not verified in this slot; it needs Node 24 and just; the default scan every 5 minutes is far more frequent than Agendum's 6 daytime slots, so the cost bases cannot be compared directly; the unit price in the author's README is self-reported.

# Next steps

- [ ] Read the README and `prompt_engineering/jev/*/command.json`, and note what each of the 6 jev commands asks
- [ ] In a sandbox install Node 24 + just, run `just combos dev` (offline, fake model, fixed news samples), and take a screenshot of the card UI
- [ ] Write a comparison table: which Agendum step each of its gates corresponds to, and which step Agendum lacks
- [ ] Give a conclusion: should the Hype / Facts / Signal three-score system be added to Agendum's issue gate (a suggestion; the user decides)

# Sources

- https://github.com/disler/pi-durable-news-agent
- https://youtu.be/OLqP8jxJ0Wc
- https://www.npmjs.com/package/@earendil-works/pi-durable

# Tracking

[Issue #36](https://github.com/mykie2015/agendum/issues/36) · EXPERIMENT · P1 · S · 1–2 hours · closed

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [opensource](../topics/opensource.md)
