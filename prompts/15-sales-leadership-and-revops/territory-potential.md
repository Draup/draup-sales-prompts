[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which region gets the next rep

> **A ranked comparison of 2–5 countries for one industry, or 2–4 industries in one country: how many sizeable accounts each holds, how many are active in the work you sell, where your rivals are really in use, and the revenue at stake, with where to add the next rep and the first account to open.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Annual or half-year planning, when you must decide which country, or which industry in your country, gets the next rep, partner or campaign budget. Use "Which cities to base reps and events" to pick cities inside one country, and "Carve balanced territories by geography" to split a market between reps. | Sales Leader & RevOps, Marketing & ABM | Everyone | 6–8 min | Company directory, Company & financials, Outsourcing deals, Hiring & job postings, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Aerospace & Defense (or 2–4 industries, e.g. Retail; Food, Beverages & Consumer Goods) |
| `[Compare]` | France, Germany, United Kingdom (or one country, e.g. United States of America) |
| `[Minimum employees]` | 2,000 |
| `[What I sell]` | OT and device security software |
| `[My competitors (optional)]` | CrowdStrike, Palo Alto Networks |
| `[Current coverage (optional)]` | 1 rep in the UK, none in France or Germany |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my RevOps analyst sizing territories. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Aerospace & Defense; or 2–4 to compare, e.g. Retail; Food, Beverages & Consumer Goods]
- Compare: [2–5 HQ countries, e.g. France, Germany, United Kingdom; or one country when comparing verticals]
- Minimum employees: [e.g. 2,000]
- What I sell: [one line, e.g. OT and device security software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. CrowdStrike, Palo Alto Networks; skip if saved in setup]
- Current coverage (optional): [reps per segment, e.g. 1 rep in the UK, none in France]

STEPS
1. Use Draup's exact names. Say the mode: countries (one vertical) or verticals (one country); each country or industry is a "segment". Map What I sell to its 1–3 main workloads (types of work, e.g. Cybersecurity).
2. Per segment, count companies with that primary industry, HQ there and [Minimum employees]+ staff (names only). Over 100? Check single rows at positions 250 and 500 and report the band.
3. Repeat step 2 adding "active in my workloads": the relevance measure.
4. Per segment, pull the top 10 by revenue in full, showing only my competitors' products (names, not usage): revenue and year, description.
5. For the top 3 accounts per segment (top 5 when comparing 2), check my competitors' products with usage strength. Only High or Medium counts as in use; say how many were Low only.
6. Flag misfiled, distributor, holding or private-equity, possibly inactive and subsidiary rows, and companies that sell what I sell; leave them out of totals.
7. Score (editable): workload-active share 35%, top-10 revenue 25%, rival-in-use share of those checked 20%, accounts 20%. With coverage, divide by reps plus one and say if the winner changes.
8. For the winner's top clean account, pull its top 3 executives in the function closest to What I sell and its top 90-day news item; if it's a mega-cap, also name the best mid-size account.

OUTPUT
- Bottom line: 2 sentences — the segment to staff next and what it means for [What I sell].
- Recommended next step: the decision, its owner and a date; then the first account to open, with a named person (step 8) and one dated fact. If none, say so.
- "Segments compared": Segment | Accounts (all / in my workloads) | Rival in use (of checked) | Top-10 revenue (USD B, FY) | Score (per rep).
- "Where to add capacity": winner and runner-up, 2 number-backed reasons each.
- Detail: top 5 logos per segment; Low-only rival detections; what's missing (removed rows, no workforce figure, HQ elsewhere); rubric.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Totals cover each segment's top 10, never the whole market.
- A rival in use at over 70% of accounts checked no longer separates segments; lean on the workload count.
- Same size cut in every segment; label fiscal years.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: which of [Compare] (2–5 countries for [Vertical], or 2–4 industries in one country) gets the next rep for [What I sell], scored on workload-active accounts, rivals at High or Medium usage, revenue and coverage.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Rerun with Minimum employees at 1,000 for the two smallest segments.
```

```text
Change the weights: workload activity 50%, revenue 30%, rival presence 20%.
```

```text
Check rival usage for accounts 4–10 in the winning segment.
```

```text
List well-known companies missing from [Segment] (no workforce figure or HQ elsewhere) so I can add them by hand.
```

## Tips for better results

- Compare segments with the same size cut; a lower threshold in one makes it look bigger than it is.
- Draup lists many rival products at low usage almost everywhere. Only High or Medium usage counts as a rival in place, so the rival column stays meaningful.
- Use verticals mode when the real question is "which industry in my country", not "which country"; add current coverage so the per-rep score can change the answer.

## Related prompts

- [Carve balanced territories by geography](../../prompts/11-account-planning/territories.md): An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Which cities to base reps and events](../../prompts/15-sales-leadership-and-revops/metro-heatmap.md): A ranked map of the metros in one country where an industry's people, big local employers and the employers active in your workloads concentrate, telling you where to base reps, run events, or assign a named-account owner instead.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `get_universe_companies_v3`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `leaders-territory-potential`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
