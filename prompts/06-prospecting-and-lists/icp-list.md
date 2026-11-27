[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Build and size an ICP list

> **The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are planning a territory, a campaign or next quarter's target list. | SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM | Everyone | 4–6 min | Company directory, Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Banking & Financial Services |
| `[Country]` | India |
| `[Minimum employees]` | 5,000 |
| `[Technology (optional)]` | SAP S/4HANA |
| `[Rank by]` | revenue |
| `[What I sell]` | core-banking modernisation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales operations analyst building a target account list. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Banking & Financial Services]
- Country: [HQ country in full, e.g. India]
- Minimum employees: [e.g. 5,000]
- Technology (optional): [Product they must run, e.g. SAP S/4HANA]
- Rank by: [revenue, workforce or Opportunity Index; default revenue]
- What I sell: [one line, e.g. core-banking modernisation services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical, country and technology to Draup's names.
2. List companies with primary vertical [Vertical], HQ in [Country] and, if given, [Technology] in their tech stack (that filter is the evidence). Leave the size minimum off; sort by [Rank by].
3. Apply [Minimum employees] yourself: count matches, companies lacking a workforce figure, and matches by band: [Minimum]–9,999 (skip if empty), 10,000–49,999, 50,000+.
4. For the 5 best fits only, pull 90-day top news and confirm [Technology] with its last-seen date.

OUTPUT
- Bottom line: 2 sentences — how big the list is and what it means for [What I sell].
- Header: "N companies match" (or "250+"), band counts, and "M more lack a workforce figure; include them?"
- Top 25 (by [Rank by]): Rank | Company | Workforce | Revenue ($M, FY) | IT spend ($M, FY) | Opportunity Index | Service providers (3, unranked) | Postings (90 days) | Who to call (likely title) | Flag.
- "Where to start" (5 rows): Company | Why it fits | Why now (freshest material dated event, or "none in 90 days") | [Technology] last seen.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Flag "check vertical" if a description doesn't fit.
- IT spend is a Draup estimate, often modelled from revenue: label it "Draup-estimated"; its growth is not a separate signal.

- Flag "check revenue" when revenue per employee is above $5M (often gross trading revenue). (editable default)
STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Use primary vertical only, sort largest first, and flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- Pull 10 companies per page (each row is large), at most 3 pages. For the total, check whether a 250th match exists and report "250+" if it does; size-band and missing-workforce counts then cover the rows pulled.
- Show USD millions using Draup's conversion rate; if Draup gives none, name the rate and date and mark it as outside Draup.
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Count every company with primary vertical [Vertical], HQ in [Country], [Minimum employees]+ staff (running [Technology] if given). Show the top 25 by revenue with providers, 90-day postings and who to call, plus a why-now for the best 5.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Tier these 25 by propensity to buy [What I sell].
```

```text
Include the companies with no workforce figure and show the 10 largest by revenue.
```

```text
For the top 5, who owns [Business function]? Names, titles and level.
```

## Tips for better results

- Primary vertical keeps the list clean, but a company filed under another industry won't appear. Add those by hand.
- If the count looks small, ask how many companies dropped out for missing workforce data.

## Related prompts

- [Look-alikes of a best customer](../../prompts/06-prospecting-and-lists/lookalikes.md): Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches and who to call.
- [Fastest revenue growers in my ICP](../../prompts/06-prospecting-and-lists/revenue-growth-screen.md): The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside and a shortlist growing both revenue and headcount.
- [Tier my accounts by propensity to buy](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on an editable Fit (0–50) and Timing (0–50) rubric, tiered A, B or C and placed on a fit-versus-timing grid, with the driver behind each score.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `get_universe_companies_v3`, `get_top_signals`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `prospect-icp-list`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
