---
type: Agendum Action
title: "Add a verified-scope table for Claude Duet to the wiki"
description: "Worth 30 minutes to turn the fact check into a short corrected Duet note in the wiki, so later notes stop repeating the overstated wording (\"desktop\", \"continuously monitors\", \"enterprise\")."
resource: https://github.com/mykie2015/agendum/issues/62
tags: [write, p2, ai, agent]
status: stable
issue: 62
action_type: write
priority: p2
state: closed
created: 2026-10-24
generated: { by: process:agendum-wiki/1, at: 2026-10-24T08:47:18+08:00 }
sources:
  - { id: s1, resource: https://claude.com/blog/claude-duet }
  - { id: s2, resource: https://www.reddit.com/r/ClaudeAI/comments/1xc6beb/claude_duet_research_preview_what_you_get_what_it/ }
---

# Decision

Worth 30 minutes to turn the fact check into a short corrected Duet note in the wiki, so later notes stop repeating the overstated wording ("desktop", "continuously monitors", "enterprise").

# Summary

Add the verified facts to `02.wiki/research/claude-duet-launch-pulse.md` and mark what is unverified, so the wiki has one correct source for Duet's scope.

# Used in insights

* [Scope words and multipliers inflate between a vendor's text and its retellings](../insights/launch-claims-inflate-between-source-and-retelling.md)
* [A proactive agent is defined by where its approval boundary sits and what happens when it fails](../insights/proactive-agents-are-defined-by-their-approval-boundary.md)

# Limits

The VentureBeat article was not found. Whether Duet "schedules jobs" is not confirmed. The Anthropic post itself was read through second-hand coverage in places.

# Next steps

- [x] Add a "Verified scope" table to `claude-duet-launch-pulse.md` with the four breakdown items
- [x] Mark "schedules jobs" and the VentureBeat claim as unverified on the page
- [x] Link #49 and this issue from the page under `## Actions`

# Result

The wiki page now has a table with five verified items (platforms, cadence, access, model, approval) and the wrong wordings next to them. "Schedules jobs" and the VentureBeat claim are listed as unverified. Learned: a fact check is cheaper when the first-hand post and one search are read before the summary is copied.

Follow-up: KEEP · continue

# Updates

- Done: table added to the wiki page, unverified items marked, issues linked.

# Sources

- https://claude.com/blog/claude-duet
- https://www.reddit.com/r/ClaudeAI/comments/1xc6beb/claude_duet_research_preview_what_you_get_what_it/

# Tracking

[Issue #62](https://github.com/mykie2015/agendum/issues/62) · WRITE · P2 · XS · 30 minutes · closed

Topics: [ai](../topics/ai.md), [agent](../topics/agent.md)
