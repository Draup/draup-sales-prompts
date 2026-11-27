[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Private company funding and who signs

> **How much a private company has raised, its last round and valuation, whether it is in growth mode, and who signs, by name.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Selling to a startup or scale-up, or checking a private competitor's runway. | Account Executive, SDR / BDR, Sales Leader & RevOps, Partnerships & Alliances | Everyone | 1–2 min | Company & financials, Hiring & job postings, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | databricks.com |
| `[What I sell]` | security compliance automation |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my venture research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. databricks.com]
- What I sell: [one line, e.g. security compliance automation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull private funding: total raised and each round's date, type, amount, valuation and lead investors.
3. Pull the profile (workforce, year founded) and the monthly hiring trend for the last 12 months.
4. From the first executives page, pick the founder or CEO, the CFO and the leader closest to [What I sell].
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 4), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Headline: total raised, last round (date, type, amount, valuation, leads).
- "Last 5 equity rounds": Date | Type | Amount ($M) | Valuation ($M) | Lead investors. Newest first.
- "Growth mode": workforce, average monthly postings, and the last 5 full months against the 5 before.
- "Who signs": usually the founder, CEO or CFO at this stage; name them with title and time in role.
- "What this means for [What I sell]": 2 bullets.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Debt and secondary": same columns as the equity table.

RULES
- Debt and secondary sales are not equity rounds; keep them out of the equity table and the round count.
- Amounts in $M; write "undisclosed" for missing valuations.
- No funding returned: say it may be bootstrapped, public or untracked; if public, suggest the account brief.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 380 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
[Company] funding: bottom line and who signs, then total raised, last round (date, amount, valuation, leads), last 5 equity rounds in $M with debt separate, and the hiring trend.
```

</details>

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

- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.
- [Openings from their recent acquisitions](../../prompts/01-account-research/acquisitions.md): The top 3 integration openings from the account's acquisitions in the last 3 years, who likely owns each, and an optional read of its strategic investments.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_private_financials_v3`, `get_account_details_v3`, `accounts_hiring_timeline_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-private-funding`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
