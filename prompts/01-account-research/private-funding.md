# Private company funding

**How much a private company has raised, its last round and valuation, equity history, whether it is in growth mode, and who signs.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Selling to a startup or scale-up, or checking a private competitor's runway. | Account Executive, SDR / BDR, Sales Leader & RevOps, Partnerships & Alliances | Everyone | 1–2 min | Company & financials, Hiring & job postings, Executives & movement |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | databricks.com |
| `[What I sell]` | security compliance automation |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my venture research analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. databricks.com]
- What I sell: [one line, e.g. security compliance automation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull private funding: total raised and each round's date, type, amount, valuation and lead investors.
3. Pull the profile (workforce, year founded) and the monthly hiring trend for the last 12 months.
4. From the first executives page, pick the founder or CEO, the CFO and the leader closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Headline: total raised, last round (date, type, amount, valuation, leads).
- "Last 5 equity rounds": Date | Type | Amount ($M) | Valuation ($M) | Lead investors. Newest first.
- "Debt and secondary": same columns, listed separately.
- "Growth mode": workforce, average monthly postings, and the last 5 full months against the 5 before.
- "Who signs": usually the founder, CEO or CFO at this stage; name them if Draup has them, with title and time in role.
- "What this means for [What I sell]": 2 bullets (fresh capital often funds hiring and tooling; a long gap may mean cost discipline).
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Debt and secondary sales are not equity rounds; keep them out of the equity table and the round count.
- Amounts in $M; write "undisclosed" for missing valuations.
- No funding returned: say it may be bootstrapped, public or untracked; if public, suggest the account brief.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 250 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
[Company] funding: total raised, last round (date, amount, valuation, leads), last 5 equity rounds in $M with debt separate, headcount and hiring trend, and who likely signs.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who are the lead investors' other portfolio companies in my ideal customer profile?
```

```text
Which leaders joined in the last 6 months?
```

```text
Compare its hiring with [Competitor]'s.
```

## Tips for better results

- Public companies return nothing here. Use the one-page account brief for them.
- A recent large round is often one of the strongest why-now signals for a scale-up.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Acquisitions, strategic bets and the openings they create](../../prompts/01-account-research/acquisitions.md): The account's acquisitions in the last 3 years, grouped by theme, the integration work each creates and the top 3 openings for you, plus an optional read of its strategic investments.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_private_financials_v3`, `get_account_details_v3`, `accounts_hiring_timeline_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `research-private-funding`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
