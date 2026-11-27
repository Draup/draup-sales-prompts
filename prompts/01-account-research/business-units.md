# Fastest-growing business units

**Business units ranked by revenue growth, with the two worth targeting, the priority behind each and the unit leader's title.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Choosing which division to enter first at a conglomerate or multi-segment company. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 2–4 min | Company & financials, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | rail and infrastructure digital-twin software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my sales research analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. rail and infrastructure digital-twin software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue by business unit for the latest year Draup holds, and the latest reported fiscal year.
3. Pull stated priorities and match each unit to the priorities that mention its products, markets or workloads.
4. For the top 2 units, find the most senior leader on the first executives page for the closest function.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Business units": Rank | Unit | Revenue (millions, currency) | Share % | YoY | Fiscal year. Sort by YoY, highest first.
- "Target these 2": for each, why (growth, size), one linked priority with source and quarter, and the unit leader's title (or "title to find").
- "Watch": units shrinking more than 5% (editable default), with a reason if Draup shows one.
- "Why this matters for [What I sell]": 2 bullets.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out eliminations, reconciliation, corporate and internal financing lines.
- If segment data is a year older than the latest fiscal year, say so plainly.
- If segment data is empty, say so and fall back to priorities grouped by business function, labelled as a fallback.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Financials are annual, in millions of reporting currency, by fiscal year (which can run ahead of the calendar). Use the latest year's regional split only. Check for a divestment, demerger or restatement before calling a drop over 5% a cut.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level (if none appears, say so in Gaps).
- Keep to about 250 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Rank [Company]'s business units by revenue growth (revenue, share, YoY, fiscal year), skip reconciliation lines, and name the top 2 to target for [What I sell], each with a linked priority and the leader's title.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who leads the top unit? Map its buying committee.
```

```text
What is the top unit hiring for?
```

```text
Compare the top unit's priorities with what [Competitor] offers.
```

## Tips for better results

- Fast-growing units often have new budget, which makes them a good first entry point.
- Segment data can lag the latest annual report by a year; the prompt flags it.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.
- [Which region should own this account](../../prompts/01-account-research/buying-center.md): Which region and metros hold the revenue, people and decision makers for your function, which region should own the pursuit, and where to hold the first meeting.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_revenue_by_business_v3`, `get_account_financials_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `research-business-units`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
