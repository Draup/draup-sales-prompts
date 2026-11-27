[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Reality-check a forecasted deal

> **An outside-in score of a forecasted deal on pain, money, timing, people and competition, a recommended forecast category, the questions to ask the rep and the named buyer to verify with.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a forecast call or deal review, or when a deal looks too good to be true. | Sales Leader & RevOps, Account Executive, Account & Customer Success Manager | Everyone | 4–6 min | Priorities & opportunities, Company & financials, Hiring & job postings, Outsourcing deals, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | fedex.com |
| `[Deal summary]` | AI-enabled customer-support services, $2M, close 2026-12-31 |
| `[Stated pain]` | support costs rising with shipment volume |
| `[Forecast category]` | Commit |
| `[Competitor]` | Concentrix (optional) |
| `[What I sell]` | AI-enabled customer-support services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales manager running a deal review. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. fedex.com]
- Deal summary: [e.g. AI support services, $2M, close 2026-12-31]
- Stated pain: [e.g. support costs rising with volume]
- Forecast category: [Commit, Best case or Pipeline]
- Competitor (optional): [e.g. Concentrix]
- What I sell: [one line, e.g. AI-enabled customer-support services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
This shows where the rep's story and the evidence disagree.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell] and its 1–3 workloads; say which.
3. Pain: up to 6 priorities in the function that match [Stated pain].
4. Money: revenue and EBITDA growth.
5. Activity: postings in the function (last 5 full months vs the 5 before) and active engagements.
6. People: one page of 10 function executives: top 3 and anyone under 1 year in title.
7. Events, last 90 days (20+ items): layoffs, restructuring, leadership changes, cost programmes, acquisitions, guidance.
8. Competition: [Competitor] in the stack (software) or engagements (services).
9. Score each dimension 0–2 against [Forecast category] and the close date.

OUTPUT
- Bottom line: 2 sentences — whether the forecast category holds and the recommended category.
- Recommended next step: a named person (name, full title) at the account to verify the deal with, the action this week and the dated why-now (or say none).
- Table "Scorecard": Dimension | Score | Evidence + date | Contradicts the rep? Then Total out of 10 and category: Commit 8–10, Best case 6–7, Pipeline 4–5, Omit 0–3 (editable defaults).
- "Questions for the rep": 4, tied to weak scores.
- "Red flags": up to 3.
- Detail: the numbers behind each score.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Pain 2 = a matching priority in the 2 latest quarters. Money 2 = growth and no cost action touching the function. Timing 2 = no blocking event before close. People 2 = stable, or a new leader with a mandate. Competition: 0 if [Competitor] is Red (a product at High usage, or 30%+ of active engagements in my workloads), 1 if Amber (Medium, newly detected or 10–29%), 2 if Green (Low-only, under 10% or absent). Activity informs Money and Timing; it isn't scored.
- Layoffs hurt Money only if they hit the function or signal a freeze. Never score to match the rep.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Reality-check my [Forecast category] deal at [Company]: [Deal summary]. Lead with whether the category holds and the named buyer to verify with. Score Pain, Money, Timing, People and Competition 0–2 from dated evidence and give 4 questions for the rep.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run this check on my other 5 Commit deals: [Accounts, deal summaries].
```

```text
Write the coaching note for the rep in under 120 words.
```

```text
Build the plan that gets the weakest dimension to 2 before close.
```

## Tips for better results

- Use it as a conversation starter in deal reviews, not a verdict on the rep.
- Low Pain plus high Money often means the buyer can afford it but hasn't decided they need it; coach to the business case.
- Re-run after each big event at the account; one news item can flip Timing.

## Related prompts

- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [Pick a realistic signature window](../../prompts/08-deal-strategy/budget-timing.md): Whether your close date fits the buyer's fiscal calendar and budget posture, the events that move money in the next two quarters, the best 4–8 week signature window and the named person to confirm it with.
- [Re-open a stalled deal](../../prompts/08-deal-strategy/stalled-reentry.md): A reopen, wait or walk-away verdict on a stalled deal, tested against why it stalled, with the named person to call, the dated change that justifies it and a 90-word re-entry email.
- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_account_financials_v3`, `accounts_hiring_timeline_v3`, `get_outsourcing_summary_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`, `get_account_tech_stack_products_v3`, `get_deals_workloads_v3`

Status: **tested live**. Prompt id: `deals-forecast-check`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
