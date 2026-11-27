[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Business-case inputs from their numbers

> **The size of the prize as a range, built on the account's own revenue, margin, spend, outsourcing and hiring, with every number labelled, a worked example you can edit and the named owner to validate it with.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need to quantify value for a proposal or CFO conversation. Use this for a new deal's value model; use "Expansion business case from growth units" instead to grow an existing customer. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Outsourcing deals, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | medtronic.com |
| `[Area affected]` | Data Engineering (or a function like IT) |
| `[Value levers]` | cost per pipeline, time to data, vendor consolidation |
| `[Our assumptions]` | 20% productivity gain; loaded cost $120K per FTE (optional) |
| `[What I sell]` | managed data engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my value engineer. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- Area affected: [workload or function, e.g. Data Engineering, or IT]
- Value levers: [2–3, e.g. cost per pipeline, time to data, vendor consolidation]
- Our assumptions (optional): [e.g. 20% productivity gain; loaded cost $120K per FTE]
- What I sell: [one line, e.g. managed data engineering services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
A case built on the buyer's own numbers, every assumption labelled, survives finance review.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Area affected] to 1–3 workloads and its function; say which.
3. Money: 3-year revenue, EBITDA, IT and R&D spend, growth and next-year forecast.
4. IT spend split, latest two years: software on premise, internal staffing, IT outsourcing, hardware.
5. Workforce: IT and R&D headcount and number of sites.
6. Outsourcing in the workloads: active engagements and partners.
7. Hiring in the workloads: 12-month postings and metros; in the 10 latest postings, note published pay, contract vs full-time, and partner, cost or speed lines.
8. Stated targets: up to 5 priorities in the workloads (else the function) with cost, speed, capacity or risk outcomes.
9. Owner and trigger: the top 3 executives in the function (one page of 10) and the most important 90-day news item.
10. Worked example: per lever, the formula, inputs from above, [Our assumptions], and a low–high result.

OUTPUT
- Bottom line: 2 sentences — the size of the prize as a range and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the biggest lever, the action this week and the dated why-now (or say none).
- Table "Worked example": Lever | Formula | Low | High (USD millions).
- Table "Their numbers" (top 8): Metric | Value | Year | Label.
- "What they said they want": up to 3 bullets: priority, quarter, lever.
- "Assumptions to validate": each of our inputs and who can confirm it (title).
- Detail: full numbers (IT split, headcount, engagements, postings) and up to 3 risks to the case.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Every number carries one label: Reported, Draup estimate, Model forecast or Our assumption.
- No assumptions given? Use a marked placeholder ("[X]% gain — your number").
- Margin % = EBITDA / revenue, same year. If Draup has no IT split, say so.
- A priority about building in-house or cutting vendors goes under risks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- IT spend is Draup-estimated (often modelled from revenue); its growth isn't a signal. Use USD millions at Draup's rate; a forecast over 15% off the latest actual is a model estimate.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 480 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Business-case inputs for [What I sell] at [Company]. Lead with the prize as a range and the named person to validate it. Show their numbers, each labelled Reported, Draup estimate or Our assumption, and a worked example per lever.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the worked example into a one-slide value summary for the CFO.
```

```text
Rebuild the case with conservative assumptions and show payback at our price of [Price].
```

```text
Which executive owns each lever? Map them to the buying committee.
```

## Tips for better results

- Give your own assumptions where you have proof; the prompt keeps them visibly separate from the buyer's numbers.
- Show ranges, not single numbers. Finance teams trust a range they can tighten in the meeting.
- Postings rarely publish pay; if none do, bring your own loaded-cost figure and label it.

## Related prompts

- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Numbers from the latest earnings call](../../prompts/01-account-research/numbers-from-the-call.md): The three numbers from the latest earnings call that matter for your deal, the question each opens and who to raise them with, plus every stated number in a reference table.
- [Offshore saving case from market pay](../../prompts/17-talent-cost-and-location/offshoring-cost-case.md): A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.
- [Arm your champion to sell internally](../../prompts/08-deal-strategy/champion-pack.md): A forwardable brief your champion can use to sell the deal inside: why now in their company's words, cost of waiting, answers for the CFO, CIO and procurement, a 150-word internal email, and who to route it to.
- [Answer objections with their own facts](../../prompts/08-deal-strategy/objection-handler.md): Which objections are real and which are cover, with a short reply and a question back for each, built on dated facts about the account, and the named person to take the answer to.
- [Expansion business case from growth units](../../prompts/12-expansion-and-cross-sell/business-case.md): A short, evidence-led case for expanding into a customer's fastest-growing unit or region: where growth is, the priorities funding it, a Draup-estimated spend pool, a 150-word executive summary and the named owner to send it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_revenue_rnd_timelines_v3`, `accounts_financials_forecast_v3`, `accounts_financials_revenue_by_it_spend_v3`, `get_globalization_summary`, `get_outsourcing_summary_v3`, `accounts_hiring_summary_v3`, `accounts_hiring_job_postings_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `deals-business-case-inputs`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
