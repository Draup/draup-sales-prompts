[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Where a rival makes its money

> **A competitor's revenue by business unit and region with growth, plus what it sells most, read as where it will defend price and where it is exposed, with the dated move and person to act on.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a pricing or positioning discussion, or when building a competitive account strategy. | Sales Leader & RevOps, Account Executive, Services, SI & Staffing Seller, Marketing & ABM, Presales & Solutions | Everyone | 2–4 min | Company & financials, Outsourcing deals, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | accenture.com |
| `[What I sell]` | data and AI services |
| `[Region I sell in]` | EMEA (optional) |
| `[Account to defend or win]` | boeing.com (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive analyst for pricing and positioning. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. accenture.com]
- What I sell: [one line, e.g. data and AI services — skip if you ran the start-here prompt]
- Region I sell in (optional): [e.g. EMEA]
- Account to defend or win (optional): [website of a live deal or key customer, e.g. visa.com]

CONTEXT (why this matters)
A rival protects its big, growing lines and discounts where revenue is small or shrinking; mix and install base are proxies.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull the latest fiscal-year revenue, EBITDA and R&D spend with growth, and the next-year forecast.
3. Pull revenue by business unit (share, growth); if none, say so and rely on step 5.
4. Pull revenue by region, latest year; compute growth from amounts.
5. Mix proxy. Software: top 10 products by companies using them. Services: customer summary and top 12 workloads by engagements, marking those closest to [What I sell].
6. Classify each row: Core (large, growing), Cash (large, flat or falling), Bet (small, fast growing), Exposed (small, shrinking). Large = 15%+ share; growing = above company growth (editable defaults).
7. Dated trigger: [Competitor]'s most important news item from the last 90 days.
8. If I gave [Account to defend or win], find it by website and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — where they'll defend and where they're exposed, and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at [Account to defend or win], the action this week, and [Competitor]'s dated move as the why-now; with no account given, name the role to brief.
- Table "Where they make money" (up to 10): Unit, region, product or workload | Share or size | Growth | Class. Highlight [Region I sell in].
- Table "Headline numbers": Metric | Latest FY | Growth | Forecast.
- "Defend vs exposed": 3 bullets each, tied to rows above; then a 2-sentence pricing read labelled inference.
- Detail: full unit, region and mix tables.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Product counts are install base, not revenue. Never state the rival's prices, discounts or margins.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Use USD millions at Draup's rate. A forecast over 15% off the latest actual is a model estimate.
- Check for divestments before calling a regional drop a cut.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Where does [Competitor] make its money? Lead with where it will defend price and where it's exposed, and the named person to act with. Show revenue, growth and forecast, revenue by unit and region, and its biggest products or workloads.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Compare this mix with my second competitor's.
```

```text
Which accounts in my territory run [Competitor]'s Exposed products?
```

```text
Write 3 pricing objections we'll hear in their Core area and a reply to each.
```

## Tips for better results

- Large technology vendors often have no business-unit split in Draup; the product install-base list is the better proxy.
- Regions growing below the company average are often where their field teams are being cut back.

## Related prompts

- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.
- [Business units worth targeting first](../../prompts/01-account-research/business-units.md): The two business units to target first, ranked by growth, with the priority behind each and a named leader to approach.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_forecast_v3`, `get_revenue_by_business_v3`, `accounts_financials_revenue_by_region_post_v3`, `get_account_key_solution_offerings_v3`, `accounts_customers_summary_v3`, `get_deals_workloads_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `compete-revenue-mix`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
