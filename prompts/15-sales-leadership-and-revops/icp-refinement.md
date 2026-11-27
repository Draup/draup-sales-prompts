[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Rewrite our ICP from best customers

> **The traits your 5–10 best customers share in Draup — industry, HQ, size, providers, activity in the work you sell — turned into a tested look-alike definition with the number of new companies it returns, the trade-off of each loosening, and the first look-alike to approach.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Rewriting the ideal customer profile before planning, a new campaign or a territory carve. Use "Find look-alikes of your best customer" when you start from one account. | Sales Leader & RevOps, Marketing & ABM, Account Executive | Everyone | 4–6 min | Company directory, Company & financials, Outsourcing deals, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Best customers]` | progressive.com, allstate.com, travelers.com, thehartford.com, chubb.com |
| `[What I sell]` | claims-automation software |
| `[My competitors (optional)]` | Guidewire, Duck Creek |
| `[Territory (optional)]` | United States of America |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my go-to-market strategist refining an ideal customer profile. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Best customers: [5–10 websites, e.g. progressive.com, allstate.com, travelers.com, thehartford.com, chubb.com]
- What I sell: [one line, e.g. claims-automation software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Guidewire, Duck Creek; skip if saved in setup]
- Territory (optional): [HQ country or region for look-alikes, e.g. United States of America; default: my territory from setup]

STEPS
1. Map What I sell to its 1–3 main workloads and say which. Look up all customers by website (exact) in one company list. If a row shows a parent, fund, venture arm or unit, look up the parent and ask me which to use. If a website returns nothing, look it up by name once and show the match and its score.
2. For each: primary industry, sub-industries, HQ country, workforce, revenue, growth, service providers, hiring %, and whether it's active in my workloads.
3. Find shared traits: an industry or sub-industry held by 80%+ (editable), HQ countries, workforce and revenue range (rounded), providers at 60%+, workload activity.
4. Write the look-alike definition, including "active in my workloads" if 80%+ share it. Count matches in [Territory] if given (names only, up to 100) minus the customers.
5. Test up to 2 loosenings one at a time (drop the provider, widen the size band, add a neighbouring sub-industry), counted the same way. If I named competitors, test once adding "runs a rival product" (presence only; usage not checked, say so).
6. Recommend the tightest definition returning 15–100 new companies (editable). Pull its top 10 by revenue in one detail page.
7. For the first look-alike, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the recommended ICP and what it means for [What I sell].
- Recommended next step: who owns the ICP update and by when; then the first account to open, with a named person (name and title from step 7) and one dated fact. If none is found, say so.
- "Definitions tested": Version | Conditions | New companies | What it adds or loses.
- "Recommended ICP": the conditions in plain words for a planning doc, plus 2 traits to qualify by hand.
- Detail: shared traits (n of N; Strong 80%+, Moderate 60–79%); customer data check; first 10 look-alikes with why each matches.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Never count the customers, their subsidiaries or sister companies as look-alikes.
- Name well-known companies missing for lack of a workforce figure (e.g. large mutuals) and offer to add them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Every count and total applies all my conditions.
- Size limits drop companies with no workforce figure (often private firms or mutuals); say so.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Parent companies only; merge subsidiaries and alternate names of one company.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: find what [Best customers] share in Draup, including activity in my workloads, turn it into a look-alike definition for [What I sell], count the new companies it returns and name the first to approach.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run a full ICP list with the recommended definition, 10 rows at a time.
```

```text
Tier the first 10 look-alikes by fit and timing for what I sell.
```

```text
Repeat with my 5 most recent losses to see which traits they lack.
```

```text
Write the ICP as a one-paragraph brief for SDRs.
```

## Tips for better results

- Feed it customers that renewed or expanded, not just the biggest logos; the traits are sharper.
- Some websites resolve to a venture arm or regional unit; the customer check catches it, so read that table first.
- If the tight version only finds a handful of new companies, the market for that profile is small — that's a finding, not a failure.

## Related prompts

- [Find look-alikes of your best customer](../../prompts/06-prospecting-and-lists/lookalikes.md): Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches, plus who to call first and why now.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.
- [Which region gets the next rep](../../prompts/15-sales-leadership-and-revops/territory-potential.md): A ranked comparison of 2–5 countries for one industry, or 2–4 industries in one country: how many sizeable accounts each holds, how many are active in the work you sell, where your rivals are really in use, and the revenue at stake, with where to add the next rep and the first account to open.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_universe_companies_v3`, `get_account_id`, `build_company_filters_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `leaders-icp-refinement`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
