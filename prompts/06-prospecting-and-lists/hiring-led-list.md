[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who's hiring for a tech or role

> **The end employers posting the most jobs for a technology or buyer role, cleaned of job boards and staffing firms, with who to call and the industries driving demand.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell around a technology or to a persona and want accounts that are actively building in that area. | SDR / BDR, Account Executive, Services, SI & Staffing Seller, Marketing & ABM | Everyone | 2–4 min | Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Technology or Role]` | Snowflake (or: Head of Data Platform) |
| `[Vendor to exclude]` | Snowflake Inc. |
| `[Country]` | United States of America |
| `[Window]` | last 12 months |
| `[What I sell]` | data-platform migration services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pipeline research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Technology or Role: [A product, e.g. Snowflake, or a job title, e.g. Head of Data Platform]
- Vendor to exclude: [The maker, or my own company, e.g. Snowflake Inc.]
- Country: [In full, e.g. United States of America]
- Window: [default last 12 months]
- What I sell: [one line, e.g. data-platform migration services — skip if you ran the start-here prompt]

STEPS
1. Resolve the technology (or role) and country to Draup's names; show them.
2. Technology: filter postings by that product. If the top company has under 30 postings (editable default), also run a keyword search and say which you used.
3. Role: list the 10 title variants Draup sees with counts; keep only the same seat (drop recruiter and clearly junior variants).
4. Pull the top 60 companies by postings in [Country] over [Window], so 25 survive cleaning.
5. Remove job boards, staffing firms, [Vendor to exclude] and its subsidiaries, and unnamed rows; record each. Move IT-services and SI firms to a separate list.
6. Rank industries by postings, footnoting IT Services, Professional Services, staffing and unassigned. Give top 5 titles for the top 3 others.

OUTPUT
- Bottom line: 2 sentences — where the demand is and what it means for [What I sell].
- "End employers hiring" (top 25, most first): Rank | Company | Postings | Industry | Share of top 25 % | Who to call (title).
- "Partners hiring" (top 10): Company | Postings — co-sell partner or competitor.
- "Industries": Industry | Postings | Share %, plus top titles.
- "Removed": name and why.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Label tables with country, window and filter (product or keyword).
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- A posting count in the millions or above the company's workforce means a failed match; say so and drop it.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which end employers posted the most [Technology or Role] jobs in [Country] in the last 12 months? Top 25 after removing job boards, staffing firms and the vendor, with who to call; list IT-services firms separately; add the top industries.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5 employers, show 3 recent postings each with title, date, location and key responsibilities.
```

```text
Which of these employers already show [Technology] in their tech stack, and when was it last seen?
```

```text
Draft a 90-word opener for the #1 employer that cites their hiring.
```

## Tips for better results

- Scan the 'Removed' list in case a real employer was cut.
- IT-services firms hiring for a technology are building a practice. Treat them as partner or competitor leads, not end customers.

## Related prompts

- [Build and size an ICP list](../../prompts/06-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.
- [Contract vs full-time demand](../../prompts/14-industry-intelligence/contract-vs-fulltime.md): What share of hiring for a skill is contract versus full-time, and how much staffing firms drive it: a read on staff-aug and SI demand.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings are running above or below normal, which workloads drive it, and whether it's seasonal.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_top_companies_v3`, `talent_demand_visualize_job_title_v3`, `talent_demand_visualize_verticals_v3`

Status: **tested live**. Prompt id: `prospect-hiring-led-list`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
