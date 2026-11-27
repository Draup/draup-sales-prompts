[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who's hiring for a tech or role

> **The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell around a technology or to a persona and want accounts actively building in that area. Use this when hiring is the filter; use "Size your ideal-customer list" instead when industry and size define the list. | SDR / BDR, Account Executive, Services, SI & Staffing Seller, Marketing & ABM | Everyone | 2–4 min | Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Technology or Role]` | Snowflake (or: Head of Data Platform) |
| `[Country]` | United States of America |
| `[Vendor to exclude (optional)]` | Snowflake Inc. |
| `[What I sell]` | data-platform migration services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pipeline research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Technology or Role: [a product, e.g. Snowflake, or a job title, e.g. Head of Data Platform]
- Country: [in full, e.g. United States of America]
- Vendor to exclude (optional): [the maker, or my own company, e.g. Snowflake Inc.]
- What I sell: [one line, e.g. data-platform migration services — skip if you ran the start-here prompt]

STEPS
1. Resolve the technology (or role) and country to Draup's names; show them.
2. Technology: filter postings by that product. If the top company has under 30 postings (editable), also run a keyword search and say which you used. Role: list the title variants Draup sees and keep only the same seat (drop recruiter and junior variants).
3. Pull the top 40 companies by postings in [Country], last 12 months, excluding staffing firms and job boards.
4. Remove [Vendor to exclude] and its subsidiaries and unnamed rows; record each. Move IT-services and consulting firms to a separate "Partners hiring" list.
5. Look up the top 10 end employers in one company list by exact name: workforce and primary industry. Work out postings per 1,000 employees.
6. For the top 3 by postings per 1,000: the most important news item from the last 90 days where the company is the actor. For the #1: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where demand is and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "End employers hiring" (top 10): Rank | Company | Postings (12 months) | Per 1,000 staff | Why now (dated).
- "Partners hiring" (top 5): Company | Postings — co-sell partner or competitor.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: industries driving demand (Industry | Postings | Share %); the "Removed" list with reasons.

RULES
- Label tables with country, window and filter (product or keyword).
- Raw postings reward size: show per-1,000 beside every count; write "n/a" when workforce is missing.
- A posting count above the company's workforce means a failed match; say so and drop it.
- Postings are openings, not hires. Professional information only.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: which end employers posted most [Technology or Role] jobs in [Country] in 12 months? Top 10 after removing job boards, staffing firms and the vendor, with postings per 1,000 staff and who to call.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5 employers, show 3 recent postings each with title, date, location and key responsibilities.
```

```text
Which of these employers show [Technology] in their tech stack, with usage strength and last-seen date?
```

```text
Draft a 70-word opener for the #1 employer that cites its hiring.
```

## Tips for better results

- Postings per 1,000 staff often reorders the list: a mid-size company hiring hard beats a giant's routine backfill.
- IT-services firms hiring for a technology are building a practice. Treat them as partner or competitor leads, not end customers.

## Related prompts

- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Check if a skill market buys contractors](../../prompts/14-industry-intelligence/contract-vs-fulltime.md): What share of hiring for a skill is contract versus full-time, how much staffing firms drive it, what it means for staff-aug or SI demand, and a named end-employer contact.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_top_companies_v3`, `talent_demand_visualize_job_title_v3`, `get_universe_companies_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-hiring-led-list`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
