---
type: Agendum Action
title: "Deep read: the sub-agent concurrency paper: short tasks slower and costlier, only long tasks pay off; set one default rule"
description: "Worth a close read, and use it to set one default rule for my own multi-agent usage."
resource: https://github.com/mykie2015/agendum/issues/34
tags: [read, p1, ai, agent, harness]
status: draft
issue: 34
action_type: read
priority: p1
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.10263 }
  - { id: s2, resource: https://arxiv.org/abs/2608.00267 }
  - { id: s3, resource: https://x.com/zhou_xiaoma/status/2112363831284650435 }
  - { id: s4, resource: https://canberk.me/news/coding-agent-sub-agents-parallel-concurrency-study/ }
---

# Decision

Worth a close read, and use it to set one default rule for my own multi-agent usage. This is the first study to run a controlled experiment on turning sub-agent concurrency on and off across three native implementations (Codex, Claude Code, Kimi Code): 354 tasks, 2124 runs, over $20,000 spent. The conclusions are concrete: for small tasks, sub-agents give no benefit and can even hurt; long tasks gain, while tokens always cost 1.41 to 3.31 times more. The paper also organizes 650 problematic concurrent trajectories into 4 categories, 13 subcategories, and 28 failure modes; it reads like a backend concurrency incident list and can be used directly to check the multi-agent division of labor of Hongzhong, Yaoji, and Agendum.

# Summary

Sub-agent concurrency is a tool for long tasks, not a default speed-up key. On short tasks concurrency is slower, costlier, and possibly worse; for long tasks, first fix ownership, isolation, and merge points the way you would for a multithreaded program. The best-value use is to send an independent sub-agent to verify.

# Used in insights

* [Where harness changes do raise accuracy, the mechanism is an independent check against real state](../insights/accuracy-gains-come-from-an-independent-second-look.md)
* [At a strong base model, the harness is mostly a cost lever, not an accuracy lever](../insights/harness-is-a-cost-lever-at-a-strong-base.md)

# Limits

Each condition was run only once, sampling 20% to 25% of each benchmark; the agent and model combinations were fixed in July 2026 and later versions may change; the LoopsBench gain corresponds to 4 of 28 tasks, a small sample; ProgramBench task pass rate is 0% for all three. The X post's claim that "the most common failures are budget exhaustion, sub-agents killed early, and overwriting each other's artifacts" match…

# Next steps

- [ ] Read Section 4 (RQ1) and the Section 6 failure taxonomy table closely, and pick 5 of the 28 modes relevant to my own usage
- [ ] Read the cases for the three conditions for gains in Section 7 closely
- [ ] Write a default rule for "when to spawn sub-agents" (no more than 6 lines), with a 4-item checklist to run before enabling concurrency
- [ ] Compare with the trial designs of #27 / #9 and mark where isolation or verification needs to be added

# Updates

- Imported comment from the upstream issue (2026-10-23), translated into English.
- Imported comment from the upstream issue (2026-10-23), translated into English.

# Sources

- https://arxiv.org/abs/2610.10263
- https://arxiv.org/abs/2608.00267
- https://x.com/zhou_xiaoma/status/2112363831284650435
- https://canberk.me/news/coding-agent-sub-agents-parallel-concurrency-study/

# Tracking

[Issue #34](https://github.com/mykie2015/agendum/issues/34) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
