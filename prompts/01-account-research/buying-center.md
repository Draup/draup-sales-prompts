[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which region should own this account

> **Which region should own the pursuit, where to hold the first meeting and with whom, backed by revenue by region, top metros and where your function's leaders sit.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning territory ownership for a global account, or deciding where to run the first meetings. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 2–4 min | Company & financials, Industry ecosystem, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | unilever.com |
| `[Business function]` | IT |
| `[What I sell]` | data and analytics managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my territory planning analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- Business function: [e.g. IT]
- What I sell: [one line, e.g. data and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue by region for the latest fiscal year: share and year-on-year change.
3. Pull key locations (up to 100 rows) for [Business function] and combine them into one row per metro.
4. Pull senior executives in [Business function], 10 per page, up to 3 pages, and count them by country and metro.
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 4), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Recommended owning region": 3 bullets weighing revenue, people and decision makers, separating where budget sits from where delivery happens.
- "Where to hold the first meeting": one metro and why.
- "Revenue by region": Region | Share % | YoY | Fiscal year.
- "Top 8 metros": Metro | Country | 12-month postings | Top function | HQ or GCC (global capability centre: a company-owned offshore site). Sort by postings.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Where [Business function] leaders sit": Country or metro | # senior leaders | Most senior title; indicative headcount per metro.

RULES
- Site headcount is approximate and varies between lookups: call it indicative and back it with postings. GCC tags can include plants; drop mainly-manufacturing sites.
- A "new" site can only be inferred from postings; say so. The HQ metro may be undercounted; don't conclude the HQ is small.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which region should own [Company] for [Business function]? Bottom line, who to meet first and where, then revenue by region, the top 8 metros with postings and capability-centre flags, and where senior leaders sit.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
What is each GCC hiring for? Top functions and skills by metro.
```

```text
Name the top 5 leaders in the recommended region.
```

```text
Which service providers deliver from these metros?
```

## Tips for better results

- Budget is often decided at HQ but spent where the delivery centre is. The output separates the two.
- European executive profiles can be restricted, so Europe may look thinner on leaders than it is.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_financials_revenue_by_region_post_v3`, `accounts_location_insights_key_locations_map_v3`, `get_globalization_summary`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-buying-center`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
