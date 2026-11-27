[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Map a customer's units, sites and leaders

> **A one-page map of a customer: business units and regions with growth, key sites, the units and brands its leaders sit in and recent acquisitions, marked Ours, Adjacent or Open, with the top white space and who leads it.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| At the start of an account plan, or when you inherit a large customer. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 4–6 min | Company & financials, Executives & movement, Hiring & job postings, Talent flow & locations |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | 3m.com |
| `[What I sell]` | supply-chain analytics software |
| `[Where we are today]` | Safety & Industrial, North America (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my strategic account planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- What I sell: [one line, e.g. supply-chain analytics software — skip if you ran the start-here prompt]
- Where we are today (optional): [units or regions we serve, e.g. Safety & Industrial, North America]

CONTEXT (why this matters)
Large customers buy in pieces, each with its own budget.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull the profile (HQ, workforce, industries) and revenue by business unit (share, growth).
3. Pull revenue by region, latest year; compute growth from amounts.
4. Locations: key locations for the function closest to [What I sell] (one row per metro, 15 rows), plus all-function rows limited to HQ Location and to GCC Locations. Group by metro (functions, 12-month postings, tags); keep the HQ, top metros and every capability centre.
5. Pull one page of top leaders and one page of 10 in the function closest to [What I sell]; note each one's unit or brand from their profile employer.
6. Pull 3-year acquisitions and the most important 90-day news item where [Company] is the actor.
7. Mark each unit, region and site Ours ([Where we are today]), Adjacent (same unit or region) or Open.

OUTPUT
- Bottom line: 2 sentences — where the room to grow is and what it means for me.
- Recommended next step: a named person (name, full title) who leads the biggest open area, the action this week and the dated why-now (or say none).
- Table "White space" (top 3): Area | Fact behind it | Who leads it | Status.
- Table "Where to sell" (up to 10): Unit, region or site | Share or postings | Growth | Status.
- "Units and brands in the leadership": up to 5 bullets; flag subsidiaries and possibly sold or spun-off brands.
- Detail: account shape (HQ, workforce, revenue, industries), all units, regions and sites, acquisitions (Date | Company | Why bought).
- Gaps: what Draup lacked; ask in discovery.

RULES
- A unit seen only in leaders' profiles is "seen in leadership", not confirmed.
- Empty unit or region revenue: say so; don't infer from news. Two or fewer units: say so and use units and brands seen in leadership as the unit list.
- Flag acquisition rows whose fields look shifted.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Check for divestments before calling a regional drop a cut.
- The acquisitions table can miss deals; check M&A news too.
- Site headcount is indicative; lean on postings.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Map [Company] on one page. Lead with the 3 biggest open areas for [What I sell] and a named leader to approach. Show units, regions and top sites with growth, marked Ours, Adjacent or Open, and recent acquisitions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the biggest Open unit, map the buying committee.
```

```text
Where are they hiring fastest in the function closest to what I sell?
```

```text
Turn the white space into 3 expansion plays with a first email each.
```

## Tips for better results

- Fill in Where we are today (or save account notes in the start-here prompt); the Ours, Adjacent and Open labels are what make the map useful.
- Leaders' profile employers often reveal brands and units the revenue split hides.

## Related prompts

- [Which region should own this account](../../prompts/01-account-research/buying-center.md): Which region should own the pursuit, where to hold the first meeting and with whom, backed by revenue by region, top metros and where your function's leaders sit.
- [Business units worth targeting first](../../prompts/01-account-research/business-units.md): The two business units to target first, ranked by growth, with the priority behind each and a named leader to approach.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_revenue_by_business_v3`, `accounts_financials_revenue_by_region_post_v3`, `accounts_location_insights_key_locations_map_v3`, `accounts_executives_key_executives_v3`, `accounts_partnerships_mergers_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `expand-account-map`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
