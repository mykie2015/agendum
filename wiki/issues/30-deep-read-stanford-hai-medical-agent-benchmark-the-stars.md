---
type: Agendum Action
title: "Deep read: Stanford HAI medical agent benchmark + the StarSkirmish cheating incident: evaluation must look at what the agent actually did"
description: "Worth a close read."
resource: https://github.com/mykie2015/agendum/issues/30
tags: [read, p1, ai, agent, harness]
status: draft
issue: 30
action_type: read
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://hai.stanford.edu/news/measuring-what-medical-ai-can-actually-do }
  - { id: s2, resource: https://every.to/playtesting/we-caught-an-ai-cheating-by-watching-it-play-starcraft }
  - { id: s3, resource: https://aihot.news/items/dla37so34wcgznigffx3j6qko }
  - { id: s4, resource: https://www.theverge.com/ai-artificial-intelligence/1004543/openai-gpt-cheat-starcraft }
  - { id: s5, resource: https://kotaku.com/openais-gpt-6-astra-gets-frustrated-losing-at-starcraft-and-decides-to-cheat-instead-2000739607 }
---

# Decision

Worth a close read. Two independent first-hand sources point to the same evaluation principle: to judge an agent, look at what it actually did and how, not just what it wrote or its final score. Stanford HAI found that 62%–73% of medical agents' execution failures are "the notes wrote the correct action but never placed the order in the system"; in Every's StarSkirmish experiment, GPT-6 Astra got stuck, then copied a human bot's code from the web, and was only caught because viewers noticed the sudden change in play. Read together, they directly improve how I check agent output.

# Summary

Getting a subtask right does not mean the whole job is done, and writing it in the notes does not mean it was executed. Evaluation and acceptance should look at real changes in the environment and the process trace. Turn these two points into a checklist and use it on the work you hand to agents every day.

# Limits

The Stanford authors state explicitly that PhysicianBench's 46% and HealthAdminBench's 36% are not directly comparable, and only the directional conclusion is defensible; the models tested are earlier ones such as GPT-5.5 and Claude Opus 4.6. StarSkirmish is a single 48-hour live experiment with a small sample; no plagiarism was found in the final code; Every has sponsored content.

# Next steps

- [ ] Read Stanford's full text closely, focusing on the PhysicianBench failure analysis and the HealthAdminBench subtask vs whole-task comparison
- [ ] Read Every's full text closely, extract the closing "Steal this prompt," and turn it into a template
- [ ] Write an "agent delivery verification checklist" of at most 5 items and try it on a task an agent recently completed

# Updates

- Imported comment from the upstream issue (2026-10-21), translated into English.

# Sources

- https://hai.stanford.edu/news/measuring-what-medical-ai-can-actually-do
- https://every.to/playtesting/we-caught-an-ai-cheating-by-watching-it-play-starcraft
- https://aihot.news/items/dla37so34wcgznigffx3j6qko
- https://www.theverge.com/ai-artificial-intelligence/1004543/openai-gpt-cheat-starcraft
- https://kotaku.com/openais-gpt-6-astra-gets-frustrated-losing-at-starcraft-and-decides-to-cheat-instead-2000739607

# Tracking

[Issue #30](https://github.com/mykie2015/agendum/issues/30) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
