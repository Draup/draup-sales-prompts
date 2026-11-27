[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Size your ideal-customer list

> **The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are planning a territory, a campaign or next quarter's target list. Use this when industry and size define your list; use "Who's hiring for a tech or role" instead when hiring is the filter. | SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller | Everyone | 4–6 min | Company directory, Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Retail |
| `[Territory (optional)]` | United States of America |
| `[Minimum employees]` | 5,000 |
| `[Technology (optional)]` | Snowflake |
| `[Rank by (optional)]` | Opportunity Index (default; Draup's 0–10 attractiveness score), revenue or workforce |
| `[What I sell]` | data observability software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales operations analyst building a target account list. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Retail]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- Minimum employees: [e.g. 5,000]
- Technology (optional): [a product they must run, e.g. Snowflake]
- Rank by (optional): [Opportunity Index (default; Draup's 0–10 attractiveness score), revenue or workforce]
- What I sell: [one line, e.g. data observability software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical, territory and technology to Draup's names and show them.
2. Count companies with primary vertical [Vertical], HQ in [Territory], at least [Minimum employees] staff and, if given, [Technology] in their stack, using the short company view (up to 100 rows a page) so every match counts: that is the true total. Then count once with a size floor of 1 and once with none; the difference lacks a workforce figure.
3. Set aside intermediaries by default and say how many: distributors, wholesalers and resellers (sub-vertical Wholesale Distribution & B2B Supply, or so described), insurance brokers, and holding or private-equity firms.
4. Merge subsidiaries into parents, rank the rest by [Rank by] and pull full rows for the top 10: workforce, revenue, postings (90 days), service providers.
5. For the 5 best fits: confirm [Technology] with its usage strength and last-seen date, and its top 90-day news item where it is the actor.
6. For the #1 account: the top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — the true count with every filter applied, and what it means for [What I sell].
- Recommended next step: a named person (name, full title), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Where to start" (5 rows): Company | Why it fits | Why now (dated, or "none in 90 days") | [Technology] usage.
- "Top 10": Rank | Company | Workforce | Postings (90 days) | Flag.
- Count line: "N companies match every filter; X intermediaries set aside; Y more lack a workforce figure. Include them?"
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: revenue ($M, FY), Draup-estimated IT spend and 3 providers for the top 10; the intermediaries list.

RULES
- If the count runs past 300, report "300+" rather than guessing.
- Low [Technology] usage means present, not standard; say so.
- Flag "check revenue" above $5M revenue per employee and "check vertical" when a description doesn't fit.
- Never rank on IT spend (modelled from revenue). Professional information only.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line first: how many [Vertical] companies HQ'd in [Territory] with [Minimum employees]+ staff (running [Technology]) match every filter, distributors set aside. Then the 5 to start with, each with a dated why-now, and who to call first.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the companies with no workforce figure, largest revenue first.
```

```text
Put the distributors back and re-rank by revenue.
```

```text
Tier the top 10 by propensity to buy [What I sell].
```

```text
Write a 70-word opener for the #1 account built on its why-now.
```

## Tips for better results

- The default ranking (Opportunity Index, distributors set aside) surfaces mid-size accounts your AEs may not own yet. Rank by revenue when you want the biggest logos.
- Low usage of the required technology often means a pocket, not the main platform. Ask about it in discovery.
- Size filters drop companies with no workforce figure, often big private firms. The count line tells you how many.

## Related prompts

- [Find look-alikes of your best customer](../../prompts/06-prospecting-and-lists/lookalikes.md): Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches, plus who to call first and why now.
- [Find the fastest revenue growers](../../prompts/06-prospecting-and-lists/revenue-growth-screen.md): The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside, a shortlist growing both revenue and headcount, and who to call first.
- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_universe_companies_v3`, `get_account_tech_stack_products_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-icp-list`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
