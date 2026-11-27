[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find accounts ripe for supply chain tech

> **A ranked list of companies in your industry and country most ready to buy supply chain planning and logistics tech, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a supply chain planning and logistics campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account. | Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller | Everyone | 6–10 min | Outsourcing deals, Hiring & job postings, Tech stack, Priorities & opportunities, News signals, Company directory, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Industry]` | Food, Beverages & Consumer Goods |
| `[Country]` | United States of America |
| `[Workloads (optional)]` | a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution |
| `[Products that signal fit (optional)]` | SAP IBP, Kinaxis |
| `[What I sell]` | supply chain planning implementation and logistics technology services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my supply-chain technology target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Food, Beverages & Consumer Goods]
- Country: [HQ country in full, e.g. United States of America]
- Workloads (optional): [a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution]
- Products that signal fit (optional): [e.g. SAP IBP, Kinaxis]
- What I sell: [one line, e.g. supply chain planning implementation and logistics technology services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop logistics providers and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only tools in category Supply Chain & Logistics Software; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Supply Chain priorities each, with linked tools and providers.
7. One news search across the top 5 on network redesigns, distribution centres, planning platforms or separations, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Supply Chain; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = network, productivity or separation priority in the last 2 fiscal quarters); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (2 = an older planning tool beside a newer one, or a platform first seen in 12 months); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Cost or separation news counts only when it names supply chain or logistics.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: rank [Industry] companies in [Country] for supply chain planning and logistics tech on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run the readiness check on the #1 account.
```

```text
Show the next 10 companies with the same scoring.
```

```text
Write a 70-word opener for each of the top 3, each tied to its why-now.
```

```text
Which of these run a competitor I name? Rate each Red, Amber or Green.
```

## Tips for better results

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Related prompts

- [Is this account ready for SCM tech?](../../prompts/07-solution-plays/scm-readiness.md): A 0–20 readiness score for supply chain planning and logistics tech at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- [Who's hiring for a tech or role](../../prompts/06-prospecting-and-lists/hiring-led-list.md): The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.
- [Who just picked a vendor](../../prompts/04-signals-and-timing/vendor-selection-news.md): A dated list of companies in your industry that just selected, deployed or replaced a vendor in your category: competitor wins to watch, peer proof, and the implementation partners involved, with a named person at the best account.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_top_companies_v3`, `get_deals_customer_v3`, `get_universe_companies_v3`, `get_account_priorities_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `plays-scm-targets`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
