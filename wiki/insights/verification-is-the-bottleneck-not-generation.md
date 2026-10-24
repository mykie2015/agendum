---
type: Insight
title: "Verification, not generation, is now the bottleneck, and vendors answer by moving the review"
description: "Agents write faster than people can review. Evidence from Anthropic, a Harvard paper and PostgreSQL shows review time rising, and three different answers: verify intent, prove properties, or hand unreviewed reports to the receiver."
tags: [review, verification, agents, coding]
status: draft
confidence: medium
issues: [2, 15, 20, 25, 41, 54, 56]
generated: { by: reference_agent/claude-sonnet-5-5, at: 2026-10-24T08:40:57+08:00 }
sources:
  - { id: jellyfish, resource: https://fion.ac/jellyfish.pdf, title: "Artificial Intelligence in the Firm: Bottlenecks in Software Production", author: "Fiona Chen, James Stratton" }
  - { id: employment, resource: https://www.anthropic.com/research/employment-at-anthropic, title: "How employment is changing at Anthropic", author: "team:anthropic" }
  - { id: scanner, resource: https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source, title: "Launching an opt-in vulnerability-finding service", author: "team:anthropic-frontier-red-team" }
  - { id: formal, resource: https://www.anthropic.com/research/formal-verification, title: "LLMs are making formal software verification feasible at a much larger scale", author: "team:anthropic-frontier-red-team" }
---

# Claim

Once agents write and find things faster than people can read them, the scarce resource is human review and judgment. The sources here agree on the problem and split on the fix.

# Evidence of the bottleneck

- Anthropic's internal report: agents worked six hours for every human hour by August, and reading a Claude agent's output took half a work week, even for non-technical staff.[^employment] [#15](../issues/15-anthropic-s-internal-employment-report-designing-judgmen.md)
- Harvard job-market paper over 718 companies: after agent adoption, PR review time rose about 49%, and the share of PRs needing changes nearly doubled.[^jellyfish] [#20](../issues/20-deep-read-harvard-jellyfish-ai-agents-push-the-bottlenec.md)
- PostgreSQL 19 slipped to about 19 November because LLM-assisted review found about forty defects the team had to fix by hand. That is one committer's account, not a measurement. [#20](../issues/20-deep-read-harvard-jellyfish-ai-agents-push-the-bottlenec.md)
- Anthropic's scanner found over 29,000 candidate vulnerabilities and could human-review only about 6,000.[^scanner] [#41](../issues/41-deep-read-anthropic-oss-scanner-29k-candidate-vulnerabil.md)

# Three answers, and who pays

| Answer | Example | Who carries the review |
| --- | --- | --- |
| Verify intent before generation, not diffs after | A Tessl team stopped reading line-by-line diffs and turns review comments into enforced invariants. [#20](../issues/20-deep-read-harvard-jellyfish-ai-agents-push-the-bottlenec.md) [#54](../issues/54-deep-read-code-is-clay-now-where-judgment-goes-once-chan.md) | The author, up front |
| Prove properties by machine | Claude wrote Rocq proofs for 123 OSS libraries, checked by the proof kernel.[^formal] [#56](../issues/56-deep-read-anthropic-frontier-red-team-on-formal-verifica.md) | The proof checker; humans trust only the assumptions |
| Send unreviewed output to the receiver | Maintainers can opt in to receive model reports with no human review; about 5,000 were sent at maintainers' request. [#41](../issues/41-deep-read-anthropic-oss-scanner-29k-candidate-vulnerabil.md) | The maintainer |

The third answer does not remove the bottleneck. It moves it to the person with the least context, which is the tension with the first two.

# So what for me

- Define "done" with a review-cost line, not only "code written". The Jellyfish numbers are the reason. [#20](../issues/20-deep-read-harvard-jellyfish-ai-agents-push-the-bottlenec.md)
- Prefer a verifier or invariant I can run over a longer review. Start by turning repeated review comments into rules. [#20](../issues/20-deep-read-harvard-jellyfish-ai-agents-push-the-bottlenec.md)
- Keep human judgment for the choices that cannot be specified: taste and product shape. [#25](../issues/25-deep-read-linear-s-karri-on-someone-behind-the-software.md) [#54](../issues/54-deep-read-code-is-clay-now-where-judgment-goes-once-chan.md)
- Anthropic's code-review post is the first-hand reference for how a team splits work between model and human. [#2](../issues/02-anthropic-code-review-methodology-post-ga-boundaries.md)

# What would change my mind

- External data showing review time falling once teams adopt intent-first or proof-based checks.
- Evidence that the 49% is driven by one kind of change or by early adopters.

# Gaps

- Anthropic numbers are self-reported. The Jellyfish data is proprietary and was aggregated by the platform.
- The 49% and "nearly doubled" figures were quoted by a newsletter and not checked against the PDF tables in this tracker. [#20](../issues/20-deep-read-harvard-jellyfish-ai-agents-push-the-bottlenec.md)
- Whether formal proof scales beyond fuzz-covered C libraries is unknown. [#56](../issues/56-deep-read-anthropic-frontier-red-team-on-formal-verifica.md)

[^employment]: Anthropic, 2026-10-16, company self-report.
[^jellyfish]: Chen and Stratton, current version 2026-08-04; figures quoted via Wisereads and not rechecked in the PDF.
[^scanner]: Anthropic Frontier Red Team, 2026-10-08.
[^formal]: Anthropic Frontier Red Team, 2026-10-22.
