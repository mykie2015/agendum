---
type: Agendum Action
title: "OpenAI on low-resource-language coding: two designs from MultiLangBench and the COBOL migration evaluation"
description: "Worth one read, focusing on the evaluation design."
resource: https://github.com/mykie2015/agendum/issues/31
tags: [read, p2, ai, agent]
status: draft
issue: 31
action_type: read
priority: p2
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:34:53+08:00 }
sources:
  - { id: s1, resource: https://openai.com/index/low-resource-programming-languages }
  - { id: s2, resource: https://aihot.news/items/tzuiybo7a45sm87wj4rec2mvo }
---

# Decision

Worth one read, focusing on the evaluation design. OpenAI officially says its new model improves greatly on low-resource languages such as COBOL, Fortran, and Visual Basic, and open-sourced MultiLangBench. For someone with a backend architecture background, the two evaluation designs are more valuable than the scores: using a database file as a unified cross-language interface for grading, and requiring byte-for-byte identical output for a migration task to count as a success. Both tricks can be borrowed when building my own agent evaluations.

# Insight

The scores are OpenAI's self-report, so treat them as reference only; what is worth taking away is the two evaluation designs: grade across languages through a reference implementation, and catch behavior drift with byte-for-byte equality.

# Limits

Both evaluations were built by OpenAI with no third-party reproduction; the COBOL migration evaluation is near saturation (97.9%); the article itself says production use still needs expert review and business-rule testing; no comparison with other labs' models.

# Next steps

- [ ] Read the full text and note the two evaluation designs
- [ ] Open the MultiLangBench repo and see how the tests are organized (no need to run it)
- [ ] Think of a scenario in my own projects where "grading by a reference implementation" could apply (for example comparing md2wechat render output), and note it in one line

# Sources

- https://openai.com/index/low-resource-programming-languages
- https://aihot.news/items/tzuiybo7a45sm87wj4rec2mvo

# Tracking

[Issue #31](https://github.com/mykie2015/agendum/issues/31) · READ · P2 · XS · 30–60 minutes · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
