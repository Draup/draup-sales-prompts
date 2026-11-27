[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Fastest revenue growers in my ICP

> **The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside and a shortlist growing both revenue and headcount.**

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
- Vertical: [Industry, e.g. Retail]
- Country: [HQ country in full, e.g. United States of America]
- Minimum revenue ($M): [e.g. 1,000]
- Minimum employees (optional): [e.g. 5,000]
- What I sell: [one line, e.g. e-commerce replatforming services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical and country to Draup's names and show them.
2. List companies with primary vertical [Vertical], HQ in [Country], revenue of at least [Minimum revenue] (and the employee minimum if given). Sort by revenue growth; take the top 40.
3. Mark "M&A-driven?" when growth tops 100% (editable default; check acquisitions for up to 5), "check vertical" when the description doesn't fit, "stale year" when its fiscal year lags by over a year.
4. Set aside M&A-driven and misclassified rows; keep the top 25. Look them up by website in one list for workforce, workforce growth %, postings (90 days), IT spend and Opportunity Index.

OUTPUT
- Bottom line: 2 sentences — who is growing fastest and what it means for [What I sell].
- Table (top 25, fastest first): Rank | Company | Revenue ($M, FY) | Revenue growth % | Workforce | Workforce growth % | Postings (90 days) | IT spend ($M) | Opportunity Index | Who to call (title) | Flag.
- "Growing and hiring": revenue growth over 10% and workforce growth over 0% (editable defaults), one-line angle each.
- "Set aside": rows and reasons.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Count companies with no growth figure, but don't rank them.
- IT spend is a Draup estimate, often modelled from revenue: label it "Draup-estimated"; its growth is not a separate signal.
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Show USD millions using Draup's conversion rate; if Draup gives none, name the rate and date and mark it as outside Draup.
- Size filters drop companies with no workforce figure; say how many and offer to include them.
- Before calling a revenue drop of more than 5% a cut, check for a divestment, demerger or restatement.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Show the 25 fastest-growing [Vertical] companies by revenue, HQ in [Country], with $[Minimum revenue]M+ revenue. Set aside likely M&A jumps, add who to call, and shortlist those also growing headcount.
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
Draft a growth-themed opener for the 'Growing and hiring' companies.
```

## Tips for better results

- Very high growth often means an acquisition. The prompt sets these aside for you.
- Companies report on different fiscal years. Compare growth rates, not raw totals.

## Related prompts

- [Build and size an ICP list](../../prompts/05-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.
- [Growing and shrinking companies: scale vs cost-out buyers](../../prompts/05-prospecting-and-lists/growth-and-cost-out.md): Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and who to call.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `get_universe_companies_v3`, `accounts_partnerships_mergers_v3`

Status: **tested live**. Prompt id: `prospect-revenue-growth-screen`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
