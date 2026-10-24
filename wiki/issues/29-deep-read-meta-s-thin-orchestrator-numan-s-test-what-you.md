---
type: Agendum Action
title: "Deep read: Meta's thin orchestrator + Numan's \"test what you ship\": a health check for my own agent system"
description: "Worth a close read and one self-check."
resource: https://github.com/mykie2015/agendum/issues/29
tags: [read, p1, ai, agent, harness]
status: draft
issue: 29
action_type: read
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/ }
  - { id: s2, resource: https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith }
  - { id: s3, resource: https://aihot.news/items/qh6pvehounuylklti7i0zl124 }
  - { id: s4, resource: https://aihot.news/items/nk19eo4eud45d47tmwxm684iu }
---

# Decision

Worth a close read and one self-check. Meta's engineering blog distills production-agent experience into one transferable rule: the "dumber" the orchestrator, the more reliable it is; routing and gates are all deterministic, and domain reasoning goes into context-isolated specialist subagents. Numan's first-hand retrospective gives the other half of the same structure (a supervisor + specialist subagents) from the evaluation side: evaluation must run on the same graph that runs in production, and the scarce asset is the evaluation standard, not the prompt. Read together, they are a good basis for a health check of the skill / routine structure of Agendum and the digital employees.

# Insight

Keep the orchestration layer thin and deterministic and leave domain judgment to isolated specialist agents; run evaluation on what actually ships and look at it by category. Together the two articles are a checklist for a health check of a personal agent system.

# Limits

Meta has not released code and the results are self-reported; "three or four days down to under an hour" refers to the configuration preparation step, not the whole process; about two thirds of changes needed no major manual edits, meaning a third still need human changes. Numan is a customer case on LangChain's official blog and carries the vendor's stance; its simulated-conversation layer is still a prototype and…

# Next steps

- [ ] Read Meta's full text closely and copy down the 7-step protocol and the 5 "How to apply" items
- [ ] Read Numan's evaluation layering and the "test what you ship" part closely
- [ ] Run a self-check on one Agendum slot: list whether each step is deterministic or needs judgment, and mark where the two are mixed
- [ ] Write 3 improvement suggestions, and let the user decide whether to change the skill / routine

# Sources

- https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/
- https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith
- https://aihot.news/items/qh6pvehounuylklti7i0zl124
- https://aihot.news/items/nk19eo4eud45d47tmwxm684iu

# Tracking

[Issue #29](https://github.com/mykie2015/agendum/issues/29) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
