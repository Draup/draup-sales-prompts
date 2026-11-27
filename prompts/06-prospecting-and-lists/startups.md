[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find startups with real momentum

> **The startups in a vertical that Draup scores for momentum, with what they do, funding, hiring, why they'd buy and a named person to contact first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell to high-growth companies, or want early-stage logos before competitors find them. | SDR / BDR, Account Executive, Partnerships & Alliances | Everyone | 4–6 min | Industry ecosystem, Company & financials |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[City (optional)]` | London |
| `[Territory (optional)]` | HQ country; default: my territory from setup, or "global" |
| `[What I sell]` | cloud cost-management software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my startup prospecting analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Insurance]
- City (optional): [e.g. London]
- Territory (optional): [HQ country; default: my territory from setup, or "global"]
- What I sell: [one line, e.g. cloud cost-management software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical and, if given, the city to Draup's metro name (e.g. "Greater London Area, United Kingdom"); show both.
2. Pull Draup's top startups for the vertical (fixed top 50), limited to that metro if given, else to HQs in [Territory]. Keep only startups with a momentum score, highest first.
3. Look up the top 10 in one company list, keeping only the same Draup companies: what they do, HQ, workforce growth %, total funding, investors, postings (90 days).
4. For those 10, pull the last funding round (type, date, amount, lead investor).
5. For the best fit: its founders or first functional leaders (up to 3) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how many momentum startups there are and the best fit for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 10" (highest momentum first): Startup | What they do | Last round (type, date, $M) | Postings (90 days) | Flag.
- "Why they'd buy": one line each for the top 5, tied to funding, hiring or stage.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: HQ, workforce growth %, total funding, lead investor and momentum score for all 10; "X startups scored".

RULES
- Leave out units of large corporations; they aren't startups.
- Flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- If an industry returns zeros, say so, retry with its parent and name it.
- Stop at 10 and offer the next 10.

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
Bottom line and next step first: the top 10 [Vertical] startups by Draup's momentum score, with what they do, funding, last round, 90-day postings, why each might buy [What I sell], and who to contact at the best one.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Continue with startups 11 to 20.
```

```text
Which of these raised money in the last 12 months? Show round, amount and date.
```

```text
Draft a 70-word opener for the best fit tied to its last round.
```

## Tips for better results

- Add a city to focus on your territory.
- A recent round plus rising job postings is often the best timing signal at a startup.

## Related prompts

- [Spot scale-up and cost-out buyers](../../prompts/06-prospecting-and-lists/growth-and-cost-out.md): Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and a named person to call first.
- [Private company funding and who signs](../../prompts/01-account-research/private-funding.md): How much a private company has raised, its last round and valuation, whether it is in growth mode, and who signs, by name.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_organization_top_startups`, `get_universe_companies_v3`, `accounts_private_financials_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `prospect-startups`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
