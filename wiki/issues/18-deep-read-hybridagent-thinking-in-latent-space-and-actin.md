---
type: Agendum Action
title: "Deep read: HybridAgent, thinking in latent space and acting in text, against harness boundaries"
description: "Worth a close read this week."
resource: https://github.com/mykie2015/agendum/issues/18
tags: [read, p1, ai, agent, harness]
status: draft
issue: 18
action_type: read
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.18861 }
  - { id: s2, resource: https://github.com/togethercomputer/HybridAgent }
  - { id: s3, resource: https://huggingface.co/collections/togethercomputer/hybridagent }
  - { id: s4, resource: https://news.ycombinator.com/item?id=50145337 }
  - { id: s5, resource: https://x.com/Jiaru_Zou/status/2110400256647340476 }
---

# Decision

Worth a close read this week. Stanford / Together AI / UIUC offer a reproducible architecture that "thinks in latent space and calls tools in text," with open-sourced code and 8B/14B weights. It directly answers how the harness research should split "internal reasoning medium vs external interface"; compare it with #12 Harness² and #14 (minimal coding agent) in the same week, without opening a parallel training project.

# Summary

Not another chase of a latent CoT hot post, but "silent inner thinking + text for external use" written as an open-source comparable agent architecture. Finish reading this week and leave a comparison table; decide on a small inference EXPERIMENT only if a GPU is available.

# Limits

Author-reported metrics are not independently reproduced; the server side needs extension to support multi-turn hybrid; training needs multiple GPUs; some HN comments question the "Most Forbidden Technique" and the difficulty of alignment auditing (the paper claims latent can be audited via pseudo-text)

# Next steps

- [ ] Read the arXiv Abstract, §3, §6, §8, and note three contrasts with #12/#14
- [ ] Skim the repo README and the `interpretable_latent_mode` sample output to see what pseudo-text auditing looks like
- [ ] Decide: just close this READ, or open an EXPERIMENT to run the 8B on one question locally/in the cloud (needs a GPU and a Tavily key)

# Sources

- https://arxiv.org/abs/2610.18861
- https://github.com/togethercomputer/HybridAgent
- https://huggingface.co/collections/togethercomputer/hybridagent
- https://news.ycombinator.com/item?id=50145337
- https://x.com/Jiaru_Zou/status/2110400256647340476

# Tracking

[Issue #18](https://github.com/mykie2015/agendum/issues/18) · READ · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
