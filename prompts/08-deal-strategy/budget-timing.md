[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Pick a realistic signature window

> **Whether your close date fits the buyer's fiscal calendar and budget posture, the events that move money in the next two quarters, the best 4–8 week signature window and the named person to confirm it with.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're setting a close date or a champion says "let's revisit next quarter". Use this to set or test the date; use "Mutual action plan on their calendar" (deals-mutual-action-plan) instead once the date is agreed. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 2–4 min | Company & financials, Earnings calls & filings, News signals, Hiring & job postings, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | 3m.com |
| `[Target close date]` | 2027-03-31 |
| `[Business function]` | IT (optional) |
| `[What I sell]` | industrial data-platform software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal-timing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Target close date: [e.g. 2027-03-31]
- Business function (optional): [the budget holder's function, e.g. IT]
- What I sell: [one line, e.g. industrial data-platform software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Deals slip when the close date ignores the buyer's calendar: fiscal year-end, budget release, earnings, reorganisations and spin-offs.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Fiscal calendar: the latest fiscal year in Draup's financials and its end date; the last 5 earnings calls with fiscal label and release date. Infer each fiscal quarter's months, the next call and the fiscal year-end.
4. Budget posture: latest revenue and EBITDA with growth, and next-year forecast. If news or a newer call reports a fiscal year Draup's table lacks, use it, labelled "from news".
5. Money-moving events, last 6 months: guidance, cost programmes, layoffs, reorganisations, spin-offs, divestments, big investments, leadership changes in the function. Review at least 20 items.
6. Hiring in the function: average monthly postings, last 5 full months versus the 5 before.
7. Up to 5 recent priorities in the function, fiscal labels translated to calendar months.
8. People: the top 3 executives in the function (one page of 10).
9. Judge [Target close date] against fiscal year-end, reorganisations and earnings dates.

OUTPUT
- Bottom line: 2 sentences — the best signature window and whether [Target close date] is Realistic, At risk or Unrealistic.
- Recommended next step: a named person (name, full title) to confirm the budget release date with, the action this week and the dated why-now; if none, say so.
- Table "Buyer calendar" (up to 8, by date): Date | Event | Effect (Accelerates, Delays, Neutral) | Source.
- "Budget posture": Growing, Holding or Tightening, with 3 dated facts.
- "Signature window": the 4–8 week window and why, plus a fallback.
- "Questions for the buyer": 3 (budget release date, approval thresholds, freeze periods).
- Detail: fiscal mapping (Fiscal period | Calendar months | Evidence), hiring, priorities.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Never assume a calendar fiscal year; derive it from period end and call dates, and show both if they disagree.
- Quote garbled news numbers as written and flag them.
- A reorganisation or spin-off effective inside the window is a Delay unless news ties it to new spending. Label future call dates "inferred".

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- IT spend is Draup-estimated, often modelled from revenue; don't treat its growth as a signal. Use USD millions at Draup's rate. A forecast over 15% off the latest actual is a model estimate.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Is [Target close date] realistic at [Company]? Lead with the best signature window and the named person to confirm it with, then fiscal quarters as calendar months, budget posture and events in the next 6 months that move money.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Build a mutual action plan backwards from the recommended signature window.
```

```text
Draft a short note to my champion asking the 3 calendar questions.
```

```text
Is their budget growing or shrinking? Show the 3-year trend and IT spend split.
```

## Tips for better results

- Ask your champion when the next budget is released; it is the single most useful date in the deal.
- Spin-offs and reorganisations often freeze new vendor decisions for a quarter or more. Plan around them.
- Re-run this before each forecast call; events change the window.

## Related prompts

- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Mutual action plan on their calendar](../../prompts/08-deal-strategy/mutual-action-plan.md): A mutual action plan built backwards from your close date that respects the buyer's fiscal calendar, names buyer owners at each step, flags events that could move dates and says who to send the draft to.
- [Reality-check a forecasted deal](../../prompts/08-deal-strategy/forecast-check.md): An outside-in score of a forecasted deal on pain, money, timing, people and competition, a recommended forecast category, the questions to ask the rep and the named buyer to verify with.
- [Numbers from the latest earnings call](../../prompts/01-account-research/numbers-from-the-call.md): The three numbers from the latest earnings call that matter for your deal, the question each opens and who to raise them with, plus every stated number in a reference table.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_forecast_v3`, `get_account_transcripts`, `get_signal_news_v3`, `accounts_hiring_timeline_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `deals-budget-timing`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
