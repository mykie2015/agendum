---
type: Agendum Action
title: "Anthropic: Claude traced the origin of the NIST elliptic-curve seeds in half an hour (method and self-verification)"
description: "Worth reading, mainly as material for writing and research methods."
resource: https://github.com/mykie2015/agendum/issues/32
tags: [read, p2, ai, content]
status: draft
issue: 32
action_type: read
priority: p2
state: open
created: 2026-10-20
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:41:17+08:00 }
sources:
  - { id: s1, resource: https://www.anthropic.com/research/ecdsa-curve-origins }
---

# Decision

Worth reading, mainly as material for writing and research methods. Anthropic officially reports that an internal research model found the origin of the NIST elliptic-curve seeds in under half an hour: the answer is that a 1990s C library random number generator, lrand48, was seeded with Unix timestamps, which explains a question that had puzzled the cryptography community for more than twenty years. The post also discloses the model's thinking at the time: it first suspected it was in a test environment, then ruled out coincidence by direct computation. It is a very concrete first-hand case for understanding both "AI doing research" and "models knowing they may be tested."

# Summary

A cryptographic mystery of more than twenty years was solved by a model in half an hour, and the answer is plain: an old random number generator seeded by timestamps. What is worth taking away is the problem-solving method and the model's self-verification process, with no security action involved.

# Limits

Anthropic itself says this is not a cryptographic break and not a weakness in the curves; the B-163 seed and the P-224/P-256/P-384/P-521 base points remain unexplained; why some usable candidate curves were skipped is unknown; no public review by outside cryptographers was seen (not checked in this slot).

# Next steps

- [ ] Read the full text and excerpt the model's thinking snippets and the three-step method
- [ ] Optional: run the reproduction code at the end locally and confirm the P-256 seed output
- [ ] Decide whether it becomes writing material for the Official Account or X, and record the conclusion in a comment

# Sources

- https://www.anthropic.com/research/ecdsa-curve-origins

# Tracking

[Issue #32](https://github.com/mykie2015/agendum/issues/32) · READ · P2 · XS · 30–60 minutes · open

Topics: [ai](../topics/ai.md), [content](../topics/content.md)
