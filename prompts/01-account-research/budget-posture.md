[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is their budget growing or shrinking?

> **A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.**

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
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue, EBITDA, IT and R&D spend for the last 3 fiscal years, plus Draup's next-year forecast.
3. Pull the IT spend split for the latest and prior year.
4. Pull acquisitions (3 years), and divestments, layoffs and cost programmes from news (12 months; say so).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "3-year trend": Fiscal year | Revenue | YoY | EBITDA margin | IT spend | YoY | R&D | YoY, forecast year last.
- Verdict: Growing, Holding or Shrinking, with 3 dated evidence bullets.
- "IT spend split (Draup estimate)": Category | Latest FY | Prior FY | YoY | % of total.
- "Deal-size implication": one line on how big a first deal to propose.
- "What to pitch": 3 bullets fitting the verdict, naming the IT spend category most addressable by [What I sell] and its likely owner (title).
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Verdict (editable default): Growing = revenue and EBITDA up over 3% a year; Shrinking = either down over 5% after the divestment check; else Holding.
- For any drop over 5%, name the divestment, demerger or restatement behind it, or say none falls in that year.
- If every IT split category moves with the total, call the split proportional.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- IT and R&D spend are Draup estimates, and IT spend often moves with revenue; don't treat IT-spend growth as a separate signal.
- If a forecast is more than 15% from the latest actual, or contradicts the latest year-on-year change, show both and call it a model estimate.
- Financials are annual, in millions of reporting currency, by fiscal year (which can run ahead of the calendar).
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Is [Company]'s budget growing, holding or shrinking? 3-year revenue, EBITDA, IT and R&D spend plus forecast, the IT spend split, a verdict with evidence, deal-size implication and pitch for [What I sell].
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

- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Fastest-growing business units](../../prompts/01-account-research/business-units.md): Business units ranked by revenue growth, with the two worth targeting, the priority behind each and the unit leader's title.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_revenue_rnd_timelines_v3`, `accounts_financials_forecast_v3`, `accounts_financials_revenue_by_it_spend_v3`, `accounts_partnerships_mergers_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `research-budget-posture`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
