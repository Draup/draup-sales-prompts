[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which region gets the next rep

> **A ranked comparison of 2–5 regions for one industry — how many sizeable accounts each holds, how many are active in the work you sell, where your rivals already sit, and the revenue at stake — with the region to staff next and the first account to open there.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Annual or half-year planning, when you must decide which country or region gets the next rep, partner or campaign budget. Use this to compare regions; use "Which cities to base reps and events" to pick cities inside one country, and the territory-carving prompt to split a region between reps. | Sales Leader & RevOps, Marketing & ABM | Everyone | 4–6 min | Company directory, Company & financials, Outsourcing deals, Hiring & job postings, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Aerospace & Defense |
| `[Regions]` | France, Germany, United Kingdom |
| `[Minimum employees]` | 2,000 |
| `[What I sell]` | OT and device security software |
| `[My competitors (optional)]` | CrowdStrike, Palo Alto Networks |
| `[Current coverage (optional)]` | 1 rep in the UK, none in France or Germany |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales strategy and RevOps analyst sizing territories. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Aerospace & Defense]
- Regions: [2–5 HQ countries in full, e.g. France, Germany, United Kingdom]
- Minimum employees: [e.g. 2,000]
- What I sell: [one line, e.g. OT and device security software — skip if you ran the start-here prompt]
- My competitors (optional): [rival products or firms, e.g. CrowdStrike, Palo Alto Networks — skip if you ran the start-here prompt]
- Current coverage (optional): [reps per region, e.g. 1 rep in the UK, none in France]

STEPS
1. Use Draup's exact industry and region names; map What I sell to its 1–3 main workloads (types of work, e.g. Cybersecurity) and say which.
2. Per region, list companies with primary industry [Vertical], HQ there and [Minimum employees]+ staff (names only, up to 100, by revenue). Over 100? Ask me to raise the threshold.
3. Per region, repeat step 2 adding "active in my workloads". That count is the relevance measure.
4. Per region, pull the top 10 by revenue in full, showing only my competitors' products: revenue and year, rivals present (stack, or provider list for services rivals), description.
5. Flag misfiled, distributor, holding or private-equity, possibly inactive, subsidiary, and companies that sell what I sell. Count them; leave them out of totals.
6. Score each region (editable): share of workload-active accounts 35%, top-10 revenue 25%, rival-present accounts 20% (displacement pool), accounts 20%. With coverage, divide by reps plus one.
7. For the winning region's top clean account, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the region to staff next and what it means for [What I sell].
- Recommended next step: the decision, its owner on my team and a date to decide by; then the first account to open, with a named person (name and title from step 7) and one dated fact. If none is found, say so.
- "Regions compared": Region | Accounts (all / in my workloads) | Rival present (of top 10) | Top-10 revenue (USD B, FY) | Score.
- "Where to add capacity": top region and runner-up, 2 number-backed reasons each, plus any coverage gap.
- Detail: top 5 logos per region; what's missing (removed rows; big names with no workforce figure or HQ elsewhere); rubric.
- Gaps: what Draup didn't have — worth asking in discovery.
- Slide version (only if I ask): 5 bullets, each with one dated number, plus 1 table.

RULES
- Totals cover the top 10 per region only, never the whole market.
- A rival present at over 70% of accounts no longer separates regions; say so and lean on the workload count.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- Counts and totals must apply every condition I set; never report one from a check that dropped a condition.
- Rivals: High usage in my workloads is Red, Medium Amber, newly detected Amber; unchecked is "present (usage not checked)". Ignore "Generic" rows.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: which of [Regions] gets the next rep for [What I sell] in [Vertical] ([Minimum employees]+ staff), scored on accounts active in my workloads, rivals and revenue, plus the first account and person.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Rerun with Minimum employees at 1,000 for the two smallest regions.
```

```text
Change the weights: workload activity 50%, revenue 30%, rival presence 20%.
```

```text
For the top region, carve the accounts into 2 balanced territories, whole metros first.
```

```text
List well-known companies missing from [Region] (no workforce figure or HQ elsewhere) so I can add them by hand.
```

## Tips for better results

- Compare regions with the same size cut; a lower threshold in one region makes it look bigger than it is.
- If your rival shows up almost everywhere, the "active in my workloads" count is the better guide to where demand is.
- Big groups registered in one country but run from another can drop out of the list; check "What's missing" before you commit headcount.

## Related prompts

- [Carve balanced territories by geography](../../prompts/11-account-planning/territories.md): An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Which cities to base reps and events](../../prompts/15-sales-leadership-and-revops/metro-heatmap.md): A ranked map of the metros in one country where an industry's people, big local employers and the employers active in your workloads concentrate, telling you where to base reps, run events, or assign a named-account owner instead.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry, optionally scoped to your region: size and growth, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `leaders-territory-potential`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
