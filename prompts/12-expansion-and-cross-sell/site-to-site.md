[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Land at one site, expand to others

> **From the site or capability centre you already serve, the sister sites doing the same work, ranked by workload overlap and growth, with each one's local leader and the next site to approach.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You've landed at one site or global capability centre and want to replicate it across the group. | Account & Customer Success Manager, Services, SI & Staffing Seller, Account Executive, Sales Leader & RevOps | Everyone | 4–6 min | Hiring & job postings, Executives & movement, Talent flow & locations |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | 3m.com |
| `[Site we serve]` | Bengaluru, India |
| `[Business function]` | IT (optional) |
| `[What I sell]` | infrastructure managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my land-and-expand strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Site we serve: [metro, e.g. Bengaluru, India]
- Business function (optional): [e.g. IT, ER&D, Finance & Accounting; default is the one closest to What I sell]
- What I sell: [one line, e.g. infrastructure managed services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
The best next site does similar work, is growing and has a reachable leader.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Pull key locations for the function limited to capability-centre sites, 15 rows: metro, indicative workforce, 12-month postings, growth index.
4. Pull key locations for the function across all site types, 15 rows, to add the HQ and other large sites. Merge by metro.
5. Pull the top workloads in job ads for the function at [Site we serve] and the 2 most promising other sites (one lookup per site, 8 rows).
6. For the top 3 candidate sites, pull senior leaders in the function based there (one page of 5 each). Drop anyone whose headline names another employer.
7. Score each: workload overlap with [Site we serve] (High, Medium, Low), growth index vs the median of listed sites, and whether a named local leader exists.
8. Pull the most important news item from the last 90 days where [Company] is the actor (site openings and expansions first).

OUTPUT
- Bottom line: 2 sentences — the next site and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the next site, the action this week and the dated why-now (or say none).
- Table "Next 3 sites": Metro | Overlap | Growth vs median | Local leader (name, title) | Why now (dated).
- Table "Sites with the function" (up to 10): Metro | Tag | Workforce (indicative) | Postings (12 mo) | Growth index. Highlight [Site we serve].
- "Reference story": 2 lines on what we deliver at [Site we serve] that maps to the next site's hiring. "Intro path": who at our site could introduce us, and to whom.
- Detail: what each site is hiring for (Workload | our site | Site 2 | Site 3).
- Gaps: what Draup lacked; ask in discovery.

RULES
- If rows come back for every function, say the limit didn't apply and keep only that function's rows.
- A site with zero postings in 12 months is stable, not growing; don't rank it first.
- The growth index is postings divided by workforce, so it runs high for small sites; say so when one tops the list.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Site headcount is indicative only; lean on postings.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Starting from [Site we serve] at [Company], rank the sister sites for [Business function]. Lead with the next site to approach and its named local leader with a dated why-now. Compare size, postings and what each site is hiring for.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
What are they hiring for at [Next site]? Show 5 recent postings.
```

```text
Draft an intro request from our sponsor at [Site we serve] to the leader at [Next site].
```

```text
Which providers already deliver at [Next site]?
```

## Tips for better results

- Workload overlap matters more than size: the same work means your reference lands.
- Capability-centre tags can include plants; check the functions before you plan the pitch.

## Related prompts

- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Which region should own this account](../../prompts/01-account-research/buying-center.md): Which region should own the pursuit, where to hold the first meeting and with whom, backed by revenue by region, top metros and where your function's leaders sit.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_location_insights_key_locations_map_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `expand-site-to-site`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
