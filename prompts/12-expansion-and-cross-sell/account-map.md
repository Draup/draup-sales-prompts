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
- Where we are today (optional): [units or regions we serve, e.g. Safety & Industrial, North America — or my saved account notes]

CONTEXT (why this matters)
Large customers buy in pieces: units, regions, brands and service centres each have their own leaders and budgets.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Pull the profile (HQ, workforce, industries) and revenue by business unit (share, growth), or say none.
3. Pull revenue by region for the latest year; compute growth from the two years' amounts.
4. Pull key locations across all functions, 40 rows. Group by metro: functions present, postings (12 months), site tags (HQ, capability centre). Keep the top 10 metros by postings plus every capability centre.
5. Pull the top 10 senior leaders (one page) and one page of 10 in the function closest to [What I sell]; note each one's unit or brand from the employer on their profile.
6. Pull acquisitions in the last 3 years, and the most important news item from the last 90 days where [Company] is the actor.
7. Mark each unit, region and site Ours (from [Where we are today]), Adjacent (same unit or region) or Open.

OUTPUT
- Bottom line: 2 sentences — where the room to grow is and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who leads the biggest open area, the action this week and the dated why-now; if none, say so.
- Table "White space" (top 3): Area | Fact behind it | Who leads it | Status.
- Table "Where to sell" (up to 10): Unit, region or site | Share or postings | Growth | Status (Ours, Adjacent, Open).
- "Units and brands in the leadership": up to 5 bullets; flag subsidiaries and brands that may have been sold or spun off.
- Detail: shape of the account (HQ, workforce, revenue, industries), all units, regions and key sites, acquisitions (Date | Company | Why bought).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- A unit or brand seen only in leaders' profiles is "seen in leadership", not a confirmed business unit.
- If unit or region revenue is empty, don't infer it from news.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- Use the latest year's regional split; compute growth from amounts and check for divestments before calling a drop a cut.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- Site headcount is indicative only; lean on postings.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
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
