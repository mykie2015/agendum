# Intake with /last30days

`/last30days <topic>` is the first step of the Agendum loop. It collects what people said about a topic in the last 30 days. It does not decide anything. Agendum decides.

```text
/last30days <topic>   →   triage   →   issue (docs/issue-body-skeleton.md)   →   work
   radar                  judge          action queue                            outcome
```

## 1. Run the radar

Run `/last30days <topic>` in Claude Code. Use a named topic: a product, a paper, a repo, a person, or a claim. Do not use a vague phrase.

The run gives you:

- a short synthesis with the top patterns
- ranked evidence clusters (saved in the raw file)
- an engine footer with counts per source
- a raw file at `~/Documents/Last30Days/<slug>-raw-v3.md`

Keep the raw file. It is the evidence file for the issue.

## 2. Triage the result

Ask four questions in this order. Stop at the first "no".

1. Is there a primary source with a link and a date? (Official post, docs, repo, paper, maintainer post.)
2. Do two or more independent sources agree? A single-source cluster is a signal, not evidence.
3. Can you state the decision in one sentence?
4. Is the next step concrete?

If the answer to question 1, 3, or 4 is "no", set the type to WATCH or do not create an issue. A quiet result is valid: write `Today: No Action`.

Popularity is not value. High likes, stars, or views do not replace a primary source.

## 3. Map the output to the issue form

| Issue field | Take it from |
| --- | --- |
| Event type, Priority, Effort | Your triage decision. |
| Core judgment | Your one-sentence decision. Do not copy the synthesis. |
| Evidence chain → Primary source | The first-party URL in the evidence clusters. |
| Evidence chain → Published | The date on that item. State the time zone. |
| Evidence chain → Independent verification | A second source that does not repeat the first. |
| Evidence chain → Related discussion | The Reddit, HN, X, or YouTube items with real engagement. |
| Evidence chain → Limits | Clusters tagged single-source or thin-evidence, the "Partial Coverage" note, and any number you did not verify. Write "unverified". |
| Discovery channel | The sources in the footer that found it. Write `last30days` plus the platforms. |
| Interpretation and breakdown | Your reading of the top patterns and the community comments. |

Quote a community comment only when it adds evidence. Wrap X handles in backticks.

## 4. Create the issue

Follow `docs/issue-body-skeleton.md`. Keep the `###` headings exactly as written. Then:

```bash
gh issue create -R mykie2015/agendum \
  --title "[READ] YYYY-MM-DD · one-line decision / action" \
  --body-file body.md \
  --label action,read,p1,ai
```

For WATCH, pass only `action,watch`. The repository is public. Redact private data before you create the issue.

## 5. Close the loop

When the work is done, fill in `Progress log`, `Result / review`, and `Follow-up decision`. Then close the issue.

The `vault-gardener-agendum` skill does steps 2 to 5 for the Vault_2 wiki. It also links the issue back into the wiki page.
