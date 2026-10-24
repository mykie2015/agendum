---
type: Insight
title: "Where harness changes do raise accuracy, the mechanism is an independent check against real state"
description: "Handoffs, contrastive probes, sub-agent verification and positive controls all gain from a second look at actual files or behavior, not from more orchestration. A fresh context alone helped in one study."
tags: [harness, verification, agents, evaluation]
status: draft
confidence: medium-low
issues: [28, 34, 12, 5, 14]
generated: { by: reference_agent/claude-sonnet-5-5, at: 2026-10-24T08:46:50+08:00 }
sources:
  - { id: cascade, resource: https://ykwon0407.github.io/posts/harness-cascade/, title: "Harness Cascade: Switching Harnesses Mid-Run Boosts Accuracy and Cuts Cost", author: "Kwon, Srivastava, Zhu, Hasan, Zou" }
  - { id: harness2, resource: https://arxiv.org/abs/2610.14224, title: "Harness^2: Recursive Agent Harnessing for an Open World" }
  - { id: doc2harness, resource: https://arxiv.org/abs/2610.20344, title: "Doc2Harness", author: "Ge et al." }
  - { id: subagents, resource: https://arxiv.org/abs/2610.10263, title: "When Sub-Agents Work in Parallel" }
---

# Claim

The accuracy gains in these studies do not come from more structure. They come from a second pass that checks the work against what is actually on disk or in the behavior, in a context that has not already agreed with the first pass. Adding agents, trees or modules without that check gave little.

# Evidence

| Case | What it shows | Strength |
| --- | --- | --- |
| [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) Harness Cascade | In one task every GLM solo run failed (0 of 12) because a 39-nt sequence was counted as 37. After a handoff the second harness checked the file and fixed the boundary. The authors write that the handoff summary was wrong and what helped was that the second harness checked it.[^cascade] | Authors' blog; one task as a worked case |
| [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) fresh context alone | On DeepSeek, restarting the same harness (CC-low to CC-low) beat running it alone by 6.0 points (p = 0.008). The 16 handoffs averaged 2.4 points over the finishing harness alone (p = 0.007), and on GLM and DeepSWE accuracy was unchanged within noise.[^cascade] | Authors' statistics; one model for the significant result |
| [#34](../issues/34-deep-read-the-sub-agent-concurrency-paper-short-tasks-sl.md) Sub-agent concurrency | The gains appear in three conditions: complementary parallel work, alternative-approach exploration, and independent verification and correction. Elsewhere concurrency cost more tokens and could hurt. | Paper; as recorded in the issue |
| [#12](../issues/12-run-the-harness-demo-locally-propose-probe-compose-and-t.md) Harness² | The Probe step runs candidate edits and compares behavior, not a correctness score, because open-world tasks have no ground-truth verifier.[^harness2] | Abstract read; gains reported by the authors |
| [#5](../issues/05-deep-read-doc2harness-and-a-checklist-of-harness-failure.md) Doc2Harness | Scoring uses four observable channels (requests, files, exit code, output) and positive controls so that a check cannot pass vacuously.[^doc2harness] | Abstract read |

# Tension

- [#14](../issues/14-deep-read-apple-epfl-how-much-harness-does-a-strong-base.md) found that a strong coding agent already does adaptive search by itself, so extra machinery adds little. A second look may be the one layer that survives at a strong base, but [#14](../issues/14-deep-read-apple-epfl-how-much-harness-does-a-strong-base.md) did not test it.
- The significant accuracy results come from one model family. They may be partly a property of DeepSeek's cheap cached input, which makes restarts cheap to try.

# So what for me

- Add a check step to long tasks. At turn N, start a fresh session from the task, a short summary, and the file state. Tell it the summary is a lead and the files win. This is the handoff rule from [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md).
- Make sure every check can fail. Run it once against a known-bad result, as the positive controls in [#5](../issues/05-deep-read-doc2harness-and-a-checklist-of-harness-failure.md) do.
- Use a sub-agent mainly as an independent verifier, with its own working directory. [#34](../issues/34-deep-read-the-sub-agent-concurrency-paper-short-tasks-sl.md)
- The experiment in [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) tests this directly: record whether the handoff note had errors and whether the second pass corrected them.

# What would change my mind

- A handoff where the second harness had no access to files, only the summary, and still improved accuracy.
- Multiple runs per setup showing that the 6.0 and 2.4 point gains do not repeat.

# Gaps

- The mechanism is inferred from the authors' description and one worked case, not isolated by an ablation.
- Accuracy gains were small and from a single model family; the authors themselves advise caution.
- It connects to the wider point that verification is the bottleneck: see [Verification, not generation, is now the bottleneck](verification-is-the-bottleneck-not-generation.md).

[^cascade]: Blog by Kwon, Srivastava, Zhu, Hasan and Zou, 2026-10-17; figures checked against the blog text on 2026-10-24.
[^harness2]: Abstract of arXiv 2610.14224.
[^doc2harness]: Abstract of arXiv 2610.20344.
