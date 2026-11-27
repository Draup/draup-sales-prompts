[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Accounts a partner can open for you

> **A sized list of companies in your industry and country where a named partner already delivers work and your product (or a rival's) isn't in the stack, with how deep the partner is at the top 5 and a named buyer at the best one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a joint pipeline review, a partner business plan or a co-marketing campaign, when you need accounts the partner can open for you. | Partnerships & Alliances, Account Executive, Sales Leader & RevOps, Marketing & ABM | Software sellers | 4–6 min | Company directory, Outsourcing deals, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Partner]` | Accenture |
| `[Vertical]` | Retail |
| `[Country]` | United States of America |
| `[Not installed]` | Databricks |
| `[What I sell]` | lakehouse analytics platform for retailers |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner pipeline analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Partner: [Services firm as Draup spells it, e.g. Accenture]
- Vertical: [Draup industry, e.g. Retail]
- Country: [HQ country in full, e.g. United States of America; default: my territory from setup]
- Not installed: [Maker whose products must be absent: ours, or a rival's, e.g. Databricks]
- What I sell: [One line, e.g. lakehouse analytics platform for retailers; skip if saved in setup]

STEPS
1. Use Draup's exact names for all inputs; say which.
2. Size the list: companies with primary industry [Vertical], HQ in [Country], [Partner] among their engaged providers, and no product made by [Not installed] anywhere in the stack. Band the total: request single rows at positions 10, 50, 100 and 250; the last that returns a company sets the band.
3. Band again without the [Not installed] condition, labelled, to show how much of [Partner]'s base already runs [Not installed].
4. Pull the top 10 matches in full, by revenue (if most rows lack revenue, sort by total workforce and say so): workforce, revenue, Opportunity Index, other providers, parent.
5. Flag: Subsidiary (name the parent), Misfiled, Possibly inactive. If more than 3 of the top 10 are flagged, move them to Detail and backfill the table with the next unflagged rows. List private companies without revenue but larger than row 5 as "Large private companies".
6. For the top 5 unflagged rows, pull [Partner]'s engagement detail: workloads, engagements (how many in workloads matching [What I sell]), tier and locations.
7. At the top unflagged account, pull the top 3 leaders in the function closest to [What I sell] and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — how much pipeline exists and which account to raise with [Partner] first.
- Recommended next step: a person from step 7 (name and title), what to raise with [Partner]'s client lead, and the dated why-now; if none, say so.
- Header line: "[Band] companies match; without the [Not installed] condition, [band]." One line on what the difference implies.
- "Pipeline" (top 10): Rank | Company | Revenue (USD M, FY) | Other providers (3) | Flag.
- "Partner depth" (top 5): Company | [Partner] engagements (in my workloads / total) | Tier | Depth | Joint angle for [What I sell].
- Depth: Deep (5+ engagements, or any matching [What I sell]), Light (1–4); editable.
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: workforce, Opportunity Index, parent; flagged rows moved out of the table, with the reason; "Large private companies".

RULES
- "No [Not installed] products" means no public evidence: a hypothesis to confirm with the partner.
- Judge depth on engagements, not the tier label.
- Under 10 matches? Widen to the region and say so.
- If the provider list and [Partner]'s engagement detail disagree, say so; trust the detail.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Trust usage strength and last-seen date, not confidence or first-seen; ignore "Generic" rows; a rival counts only at High or Medium usage.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named buyer, dated why-now) first. Which [Vertical] companies in [Country] use [Partner] and show no [Not installed] products? Band the total, top 10 unflagged by revenue, the partner's depth at the top 5.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show rows 11–20 the same way.
```

```text
For the top 3, what stated priorities in data and analytics could justify a joint pitch?
```

```text
Draft a one-page joint account list I can send to [Partner]'s alliance team (check our Draup licence first).
```

## Tips for better results

- If the list is small or full of mid-size names, the big accounts probably already run the excluded maker. That's useful for the partner conversation too.
- Lead the partner review with accounts where the partner works in a workload next to yours; that's where an introduction is credible.

## Related prompts

- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.
- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Joint account plan with a partner](../../prompts/13-partners-and-alliances/joint-account-plan.md): A one-page plan you and a partner can both sign up to for one account: where the partner already works in your function, the priorities there, your technology's and a rival's position, who to meet and a 90-day plan with owners on both sides.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_universe_companies_v3`, `get_outsourcing_engagement_details`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `partners-sourced-pipeline`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
