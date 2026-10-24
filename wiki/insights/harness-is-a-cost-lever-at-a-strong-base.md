---
type: Insight
title: "At a strong base model, the harness is mostly a cost lever, not an accuracy lever"
description: "Across five harness studies, elaborate harnesses add no accuracy at a strong base but change cost by tens of percent. Accuracy gains appear where the harness content is edited or a second pass checks the work."
tags: [harness, agents, cost, evaluation]
status: draft
confidence: medium-low
issues: [14, 28, 40, 34, 29, 12, 5, 7]
generated: { by: reference_agent/claude-sonnet-5-5, at: 2026-10-24T08:46:50+08:00 }
sources:
  - { id: apple, resource: https://arxiv.org/abs/2609.40303, title: "How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?", author: "Brilliantov, Hernandez-Cano, Abbe" }
  - { id: cascade, resource: https://ykwon0407.github.io/posts/harness-cascade/, title: "Harness Cascade: Switching Harnesses Mid-Run Boosts Accuracy and Cuts Cost", author: "Kwon, Srivastava, Zhu, Hasan, Zou" }
  - { id: jah, resource: https://arxiv.org/abs/2610.21412, title: "JevAgentHarness", author: "Zhu et al." }
  - { id: subagents, resource: https://arxiv.org/abs/2610.10263, title: "When Sub-Agents Work in Parallel", author: "Li, Li, Jiang, Lou" }
  - { id: harness2, resource: https://arxiv.org/abs/2610.14224, title: "Harness^2: Recursive Agent Harnessing for an Open World" }
  - { id: doc2harness, resource: https://arxiv.org/abs/2610.20344, title: "Doc2Harness", author: "Ge et al." }
---

# Claim

When the base model is strong, picking or adding a harness layer rarely changes how many tasks get solved, but it can change what each task costs by a third or more. Optimizing the harness for accuracy first is the wrong order. Measure cost per task by harness, then add machinery only where the evidence says it earns its keep.

# Evidence

| Case | What it shows | Strength |
| --- | --- | --- |
| [#14](../issues/14-deep-read-apple-epfl-how-much-harness-does-a-strong-base.md) Apple and EPFL | Under equal budget and the same frontier base, open-source SOTA harnesses gave no advantage over a minimal read/write/bash coding agent. The authors conclude the machinery layers are redundant in that setting.[^apple] | Paper abstract read; MLE-bench and NatureBench only |
| [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) Harness Cascade | Two harnesses both solved 77.9%, but one cost 73% more per task. Switching harness mid-run reached 82.0% at 30% lower cost than the dearer one. Prompt tokens fell 61%.[^cascade] | Authors' blog; Terminal-Bench 2.1; one run per setup |
| [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md) JevAgentHarness | A routing proxy cut cost 28% to 64% across three harnesses with success rates within noise. With only a 2.7x price gap it saved 7 to 13%, and with an auto-cached strong model it saved 6.5% and ran 47% slower.[^jah] | README results, self-reported; 74 tasks, one run each |
| [#34](../issues/34-deep-read-the-sub-agent-concurrency-paper-short-tasks-sl.md) Sub-agent concurrency | Enabling concurrent sub-agents cost 1.41 to 3.31 times the tokens and gave no gain on short tasks. Gains appeared only on long tasks.[^sub] | Paper; figures as recorded in the issue after reading its results sections |
| [#29](../issues/29-deep-read-meta-s-thin-orchestrator-numan-s-test-what-you.md) Meta thin orchestrator | Meta reports a thin, deterministic orchestrator with specialist subagents worked better than one agent that knew everything. | Vendor self-report; read through the issue only |

# Tension

- [#12](../issues/12-run-the-harness-demo-locally-propose-probe-compose-and-t.md) Harness² reports accuracy gains of up to 11.5, 4.5 and 11.8 points from editing the harness once, on GLM-5 and Gemini 3.5 Flash.[^harness2] That looks like a counter-case. The reconciliation I use is that [#14](../issues/14-deep-read-apple-epfl-how-much-harness-does-a-strong-base.md) cut outer machinery (search trees, orchestrators) at a strong base, while Harness² edits inner content (prompts, guardrails, memory, skills) and tests weaker or different bases. [#14](../issues/14-deep-read-apple-epfl-how-much-harness-does-a-strong-base.md) itself says weaker bases still gain from hand-written priors. This reading is mine; nobody tested both on one benchmark.
- [#5](../issues/05-deep-read-doc2harness-and-a-checklist-of-harness-failure.md) Doc2Harness shows that building a harness is hard for models: the best scored 53.05% and the weakest 27.44%, and failures cluster around how cross-cutting features are split into modules.[^doc2harness] That is about the builder model, not about whether a built harness helps.

# So what for me

- Log tokens and dollars per task for every harness I use before tuning for accuracy. [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md) shows a per-step log is a natural place for it.
- Start with a shell and a file system. Add orchestration only for long tasks, and spawn sub-agents mainly to verify, not to speed up. [#34](../issues/34-deep-read-the-sub-agent-concurrency-paper-short-tasks-sl.md)
- Check task length and the price of cached input before expecting a saving from restarts or routing. On short Terminal-Bench tasks with DeepSeek's cached input at 1/50 of the price, most self-restarts cost 12 to 22% more. On long DeepSWE tasks a restart of the same harness cut cost 37%. [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md)
- Route to a cheaper tier only when the price gap is large and the strong model is not already cached. [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md)
- Test the prediction below with the open experiments [#7](../issues/07-deepseek-flash-1017-deepseek-harness-minimal-comparison.md), [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) and [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md).

# Prediction to test

If this holds, then in [#7](../issues/07-deepseek-flash-1017-deepseek-harness-minimal-comparison.md), [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) and [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md) the cost per task will differ by tens of percent between setups while the pass rates stay within noise on a small task set. If a setup beats the others on accuracy by several points with no change in cost, the claim is weaker than I rate it.

# What would change my mind

- A strong-base study where a harness change lifts accuracy a lot and cost stays flat.
- A rerun of [#28](../issues/28-run-harness-cascade-once-switch-harness-mid-way-through.md) or [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md) with several runs per setup that shows the accuracy gap is real.

# Gaps

- The benchmarks differ (MLE-bench, Terminal-Bench, DeepSWE, professional benchmarks), and most setups ran once, so confidence intervals are wide. The Cascade authors say their accuracy gains deserve more caution than the cost savings.
- Cost figures come from the authors' pricing and from list prices, not from my bills.
- Nothing here has been run on my own tasks yet.

[^apple]: Abstract of arXiv 2609.40303, submitted 2026-09-30.
[^cascade]: Blog by Kwon, Srivastava, Zhu, Hasan and Zou, 2026-10-17; figures checked against the blog text on 2026-10-24.
[^jah]: Abstract of arXiv 2610.21412 for the 69.5% and 19.0-point findings; cost figures from the project README as recorded in [#40](../issues/40-run-jah-strong-vs-jah-auto-through-the-jevagentharness-p.md).
[^sub]: arXiv 2610.10263, 354 tasks and 2,124 executions; the 1.41 to 3.31x range is as recorded in [#34](../issues/34-deep-read-the-sub-agent-concurrency-paper-short-tasks-sl.md).
[^harness2]: Abstract of arXiv 2610.14224, submitted 2026-10-09.
[^doc2harness]: Abstract of arXiv 2610.20344, submitted 2026-10-14.
