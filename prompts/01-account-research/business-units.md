[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Business units worth targeting first

> **The two business units to target first, ranked by growth, with the priority behind each and a named leader to approach.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Choosing which division to enter first at a conglomerate or multi-segment company. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 2–4 min | Company & financials, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | rail and infrastructure digital-twin software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. rail and infrastructure digital-twin software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue by business unit for the latest year Draup holds, and the latest reported fiscal year.
3. Pull stated priorities for the function closest to [What I sell] and match each unit to the priorities that mention its products, markets or workloads.
4. For the top 2 units, find the most senior leader on the first executives page for the function closest to [What I sell].
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 4), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Target these 2": for each, why (growth, size), one linked priority with source and quarter, and the unit leader by name and title (or "title to find").
- "Business units" (fiscal year in the heading): Rank | Unit | Revenue (millions, currency) | Share % | YoY. Sort by YoY, highest first.
- "Watch": units shrinking more than 5% (editable default), with a reason if Draup shows one.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out eliminations, reconciliation, corporate and internal financing lines.
- If segment data is a year older than the latest fiscal year, say so plainly.
- If segment data is empty, say so and fall back to priorities grouped by business function, labelled as a fallback.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 380 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which [Company] business units should I target for [What I sell]? Bottom line and who to approach, then units ranked by revenue growth (revenue, share, YoY) and the top 2, each with a linked priority.
```

</details>

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

- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Which region should own this account](../../prompts/01-account-research/buying-center.md): Which region should own the pursuit, where to hold the first meeting and with whom, backed by revenue by region, top metros and where your function's leaders sit.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_revenue_by_business_v3`, `get_account_financials_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-business-units`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
