[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find the fastest revenue growers

> **The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside, a shortlist growing both revenue and headcount, and who to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want accounts with money and momentum, or a growth angle for a campaign. | Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM | Everyone | 2–4 min | Company directory, Company & financials |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Retail |
| `[Country]` | United States of America |
| `[Minimum revenue ($M)]` | 1,000 |
| `[Minimum employees (optional)]` | 5,000 |
| `[What I sell]` | e-commerce replatforming services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Retail]
- Country: [HQ country in full, e.g. United States of America]
- Minimum revenue ($M): [e.g. 1,000]
- Minimum employees (optional): [e.g. 5,000]
- What I sell: [one line, e.g. e-commerce replatforming services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical and country to Draup's names and show them.
2. List companies with primary vertical [Vertical], HQ in [Country], revenue of at least [Minimum revenue] (and the employee minimum if given). Count them all, then sort by revenue growth and take the top 30.
3. Mark "M&A-driven?" when growth tops 20% (check acquisitions and M&A news for up to 5), "check vertical" when the description doesn't fit, "stale year" when the fiscal year lags by over a year.
4. Set those aside; keep the top 10. Add workforce, workforce growth % and postings (90 days).
5. For the top 3 "growing and hiring": the most important news item from the last 90 days where the company is the actor. For the #1: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — who is growing fastest and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Fastest growers" (top 10): Rank | Company | Revenue growth % (FY) | Workforce growth % | Flag.
- "Growing and hiring": revenue growth over 10% and workforce growth over 0% (editable), one-line angle each.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: revenue ($M, FY), postings (90 days) and Opportunity Index for the top 10; "Set aside" rows and reasons; how many companies had no growth figure.

RULES
- Growth over 20% is "likely M&A until checked"; say what you found.
- Before calling a revenue drop of more than 5% a cut, check for a divestment, demerger or restatement.
- Size filters drop companies with no workforce figure; say how many.
- Show USD millions using Draup's conversion rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: the 10 fastest-growing [Vertical] companies by revenue, HQ in [Country], $[Minimum revenue]M+, with likely M&A jumps set aside, a shortlist also growing headcount, and who to call at the best one.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5, what are their stated priorities this year?
```

```text
Which of these grew revenue with flat headcount, and what does that suggest?
```

```text
Draft a growth-themed opener for the Growing and hiring companies.
```

## Tips for better results

- Very high growth often means an acquisition. The prompt sets these aside until checked.
- Companies report on different fiscal years. Compare growth rates, not raw totals.

## Related prompts

- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Spot scale-up and cost-out buyers](../../prompts/06-prospecting-and-lists/growth-and-cost-out.md): Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and a named person to call first.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_universe_companies_v3`, `accounts_partnerships_mergers_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-revenue-growth-screen`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
