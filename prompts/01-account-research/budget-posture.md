[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is their budget growing or shrinking?

> **A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you set deal size or pick a value story, or when a champion says 'budgets are tight'. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 2–4 min | Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | unilever.com |
| `[What I sell]` | managed data engineering and analytics services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales finance analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- What I sell: [one line, e.g. managed data engineering and analytics services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue, EBITDA, IT and R&D spend for the last 3 fiscal years, plus Draup's next-year forecast.
3. Pull the IT spend split for the latest and prior year.
4. Pull acquisitions (3 years), and divestments, layoffs and cost programmes from news (12 months; say so).
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Verdict: Growing, Holding or Shrinking, with 3 dated evidence bullets.
- "3-year trend": Fiscal year | Revenue | YoY | EBITDA margin | IT spend (Draup estimate). Forecast year last.
- "Deal-size implication": one line on how big a first deal to propose.
- "What to pitch": 3 bullets fitting the verdict, naming the IT spend category most addressable by [What I sell] and its likely owner.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "IT spend split (Draup estimate)": Category | Latest FY | Prior FY | YoY | % of total; R&D spend by year.

RULES
- Verdict (editable default): Growing = revenue and EBITDA up over 3% a year; Shrinking = either down over 5% after the divestment check; else Holding.
- For any drop over 5%, name the divestment, demerger or restatement behind it, or say none falls in that year.
- If every IT split category moves with the total, call the split proportional.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- If a forecast is more than 15% from the latest actual, or contradicts the latest year-on-year change, show both and call it a model estimate.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Is [Company]'s budget growing, holding or shrinking? Bottom line and who to pitch first, then 3-year revenue, EBITDA margin and IT spend, a verdict with evidence, deal-size implication and the pitch for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Convert everything to USD and compare with [Company 2].
```

```text
Which business units are growing fastest?
```

```text
Draft a cost-takeout talk track for the CFO based on this.
```

## Tips for better results

- A falling number is not always a cut. Spin-offs and restatements often explain big drops; the prompt checks for them.
- The IT spend split is Draup's estimate. Use it to size the conversation, not as a reported figure.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.
- [Business units worth targeting first](../../prompts/01-account-research/business-units.md): The two business units to target first, ranked by growth, with the priority behind each and a named leader to approach.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and the named person to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_revenue_rnd_timelines_v3`, `accounts_financials_forecast_v3`, `accounts_financials_revenue_by_it_spend_v3`, `accounts_partnerships_mergers_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-budget-posture`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
