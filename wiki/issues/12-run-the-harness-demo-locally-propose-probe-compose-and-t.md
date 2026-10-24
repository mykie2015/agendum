---
type: Agendum Action
title: "Run the Harness² demo locally: Propose–Probe–Compose and the improvement library"
description: "Worth validating the loop with the local demo this week and extracting a method checklist; full benchmarks and Vertex cost go in a separate issue."
resource: https://github.com/mykie2015/agendum/issues/12
tags: [experiment, p1, ai, agent, harness]
status: draft
issue: 12
action_type: experiment
priority: p1
state: open
created: 2026-10-18
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://arxiv.org/abs/2610.14224 }
  - { id: s2, resource: https://github.com/google-research/harness2 }
  - { id: s3, resource: https://harness2.github.io }
  - { id: s4, resource: https://x.com/Saboo_Shubham_/status/2111691139011223640 }
  - { id: s5, resource: https://github.com/google-research/rrsi }
  - { id: s6, resource: https://arxiv.org/abs/2609.24972 }
---

# Decision

Worth validating the loop with the local demo this week and extracting a method checklist; full benchmarks and Vertex cost go in a separate issue. The paper's gain numbers are marked "paper tables, not verified locally."

# Summary

This is an open-source, locally demoable framework that recursively edits the harness and makes the editing process itself transferable. This week's goal: get the demo running and extract the Propose–Probe–Compose and library-entry templates into personal harness / JEV notes; do not run JobBench in full.

# Used in insights

* [Where harness changes do raise accuracy, the mechanism is an independent check against real state](../insights/accuracy-gains-come-from-an-independent-second-look.md)
* [At a strong base model, the harness is mostly a cost lever, not an accuracy lever](../insights/harness-is-a-cost-lever-at-a-strong-base.md)

# Limits

Paper figures such as +11.5 / +4.5 / +11.8pp are as reported in the paper and not reproduced locally; a full run needs GCP/model costs.

# Next steps

- [ ] `uv venv` + `uv pip install -e '.[render]'`, then run `harness2-demo --output runs/demo --k 2`
- [ ] Read the Abstract + §2 (two recursive layers and eight components), and compare with the demo output directory
- [ ] Write 5–8 rules that carry over to a personal harness / JEV (contrastive edits, scoped Propose, the library does not automatically inherit H*)
- [ ] Decide clearly: whether to open a JobBench/LAB subset experiment this week (default no)

# Updates

- Imported comment from the upstream issue (2026-10-20), translated into English.
- Imported comment from the upstream issue (2026-10-21), translated into English.
- Imported comment from the upstream issue (2026-10-22), translated into English.

# Sources

- https://arxiv.org/abs/2610.14224
- https://github.com/google-research/harness2
- https://harness2.github.io
- https://x.com/Saboo_Shubham_/status/2111691139011223640
- https://github.com/google-research/rrsi
- https://arxiv.org/abs/2609.24972

# Tracking

[Issue #12](https://github.com/mykie2015/agendum/issues/12) · EXPERIMENT · P1 · S · 1–2 hours · open

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md), [harness](../topics/harness.md)
