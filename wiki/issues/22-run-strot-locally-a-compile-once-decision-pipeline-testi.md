---
type: Agendum Action
title: "Run STROT locally: a compile-once decision pipeline, testing a zero-marginal-cost runtime"
description: "Worth one minimal local experiment this week."
resource: https://github.com/mykie2015/agendum/issues/22
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 22
action_type: experiment
priority: p1
state: open
created: 2026-10-19
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://github.com/strot-ai/Project-STROT }
  - { id: s2, resource: https://pypi.org/project/strot-ai/ }
  - { id: s3, resource: https://arxiv.org/abs/2505.01636 }
  - { id: s4, resource: https://news.ycombinator.com/item?id=50148396 }
---

# Decision

Worth one minimal local experiment this week. STROT synthesizes "classification / routing / scoring" decisions once at compile time with a large model, then at runtime uses a 144M local model (about 60 ms, zero marginal LLM calls) to output typed JSON with confidence. It aims straight at harness cost and the judgment that "an agent should not burn a large model on every record"; Experiment before Build.

# Summary

Not chasing Show HN buzz, but using 1–2 hours to verify whether "decision-type tasks can compile once." Either result is a conclusion; if it fails, close it and record the failure modes.

# Limits

Still early at 21★; some HN comments say the README is still hard to follow / "better to just have the LLM write a program"; compile time still depends on a large-model API and labeled samples; not run locally; numbers not independently reproduced

# Next steps

- [ ] `pip install strot-ai==0.11.1` and compile the minimal `strot.run` ticket-triage sample from the README once
- [ ] Record: compile time / whether it calls an external LLM, runtime latency per record, number of abstains, and the shape of the artifact files
- [ ] A three-line comparison note: cost intuition versus "Claude/DeepSeek on every record"; whether it is worth comparing with #7/#12; if it fails, close it and write the reason

# Sources

- https://github.com/strot-ai/Project-STROT
- https://pypi.org/project/strot-ai/
- https://arxiv.org/abs/2505.01636
- https://news.ycombinator.com/item?id=50148396

# Tracking

[Issue #22](https://github.com/mykie2015/agendum/issues/22) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
