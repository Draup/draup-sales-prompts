[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find who hires hardest in a vertical

> **The real end employers hiring hardest in an industry, ranked on postings per 1,000 staff with recruiters and outliers removed, plus hot spots and a named person to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want the most active companies in a vertical this year; active hiring often means active budgets. | SDR / BDR, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 2–4 min | Industry ecosystem, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Life Sciences |
| `[Territory (optional)]` | United States of America |
| `[What I sell]` | talent-acquisition software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Life Sciences]
- Territory (optional): [country in full; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. talent-acquisition software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. With a Territory, rank the top 50 employers posting in [Territory] with primary vertical [Vertical], last 12 months, staffing firms and job boards excluded; merge brands and subsidiaries into parents and drop foreign companies' local teams. With none, pull Draup's top hiring companies for the vertical (a fixed top 50) and note its window.
3. Remove staffing and recruiting firms and job boards; record each.
4. Look the rest up in one company list by exact name: workforce, primary vertical and postings (90 days). Work out postings per 1,000 employees.
5. Remove outliers: a posting count above the company's workforce, or an unfamiliar firm posting far more than household names. Rank companies with 1,000+ staff (editable) by postings per 1,000.
6. For the #1: its top 3 executives in the function closest to What I sell and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — who is hiring hardest for their size and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Hiring hardest" (top 10): Rank | Company | Postings | Per 1,000 staff | Workforce.
- "Hot spots for [What I sell]": 5 companies, one reason each.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: vertical and window ("window not stated" if none); companies under 1,000 staff; the raw-count ranking; "Removed" with reasons.

RULES
- Flag "check vertical" when a company's primary vertical isn't [Vertical].
- No workforce figure: write "n/a" for intensity and list it in Detail rather than dropping it.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- If an industry returns zeros, say so, retry with its parent and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: the top 10 [Vertical] companies in [Territory] by postings per 1,000 staff (1,000+ employees), staffing firms and outliers removed, 5 hot spots for [What I sell], and who to call at the #1.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5, which functions and skills are they hiring for most?
```

```text
Which of these are hiring most in [Country]?
```

```text
Draft a hiring-themed opener for the #1 hot spot.
```

## Tips for better results

- Ranking on postings per 1,000 staff shows who is hiring hard for their size, not just who is biggest.
- Check the Removed list if a name you expected is missing.

## Related prompts

- [Who's hiring for a tech or role](../../prompts/06-prospecting-and-lists/hiring-led-list.md): The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_organization_top_top_hiring_accounts`, `talent_demand_top_companies_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-hiring-leaders`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
