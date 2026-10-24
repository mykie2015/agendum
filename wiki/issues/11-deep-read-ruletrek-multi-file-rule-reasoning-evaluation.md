---
type: Agendum Action
title: "Deep read: RuleTrek, multi-file rule-reasoning evaluation and agent failure modes"
description: "Worth a close read to extract evaluation design and failure modes; no full reproduction by default this week (few ★, expensive per run)."
resource: https://github.com/mykie2015/agendum/issues/11
tags: [read, p1, ai, agent, harness]
status: stable
issue: 11
action_type: read
priority: p1
state: closed
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.19698 }
  - { id: s2, resource: https://github.com/yuan247/RuleTrek }
  - { id: s3, resource: https://aiweekly.co/editors-blog/found-first-frontier-llms-score-up-to-55-end-to-end-on-multi-file-rule-reasoning }
---

# Decision

Worth a close read to extract evaluation design and failure modes; no full reproduction by default this week (few ★, expensive per run). Open a separate EXPERIMENT if there is budget for a subset.

# Insight

This is a rule-reasoning yardstick for multi-file, real-domain rules in an interactive workspace. The goal of a close read is to extract the RI/RD/E2E layering and the failure clusters and carry them into a personal agent / JEV / evaluation checklist, not to run all 240 cases this week.

# Next steps

- [ ] Read the Abstract, §3 (construction pipeline), and §4.2–4.5 (main results and failure analysis)
- [ ] Skim the yuan247/RuleTrek README and confirm the smallest runnable local scope (no full run forced this week)
- [ ] Write 5–8 rules that carry over to a personal agent / evaluation (RI≠RD, cross-file evidence, compounding failures)
- [ ] Decide: open a separate EXPERIMENT for a small subset (only with budget)

# Sources

- https://arxiv.org/abs/2610.19698
- https://github.com/yuan247/RuleTrek
- https://aiweekly.co/editors-blog/found-first-frontier-llms-score-up-to-55-end-to-end-on-multi-file-rule-reasoning

# Tracking

[Issue #11](https://github.com/mykie2015/agendum/issues/11) · READ · P1 · S · 1–2 hours · closed

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
