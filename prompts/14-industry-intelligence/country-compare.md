[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Compare countries for a delivery centre

> **A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways, client questions and, if you name the client, who to talk to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A client is weighing delivery or GCC locations, or you are positioning a nearshore or offshore option. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Sales Leader & RevOps | Services sellers | 1–2 min | Industry ecosystem |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Country A]` | India |
| `[Country B]` | Poland |
| `[Country C (optional)]` | Mexico |
| `[Client (optional)]` | the client's website, e.g. fabrikam.com (illustrative) |
| `[What I sell]` | nearshore delivery centre services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my location strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Country A: [in full, e.g. India]
- Country B: [in full, e.g. Poland]
- Country C (optional): [e.g. Mexico]
- Client (optional): [the client's website, e.g. fabrikam.com (illustrative)]
- What I sell: [one line, e.g. nearshore delivery centre services — skip if you ran the start-here prompt]

STEPS
1. Use full country names as Draup knows them (e.g. "United States of America", not "USA").
2. Pull Draup's country data for all of them in one go: labour force, unemployment rate, median age, cost-of-living index, inflation, corporate tax rate, political stability, and any other workforce metric Draup returns.
3. If I named a client: find it by website (confirm the parent; no match: retry once by name and show the match score), then pull its top 3 executives in IT or global delivery and its most important news item from the last 90 days (centre openings, expansions or cost programmes first).

OUTPUT
- Bottom line: 2 sentences — how the locations compare and which fits [What I sell] best for this client.
- Recommended next step: a named person (name and full title from step 3), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Comparison": Metric | [Country A] | [Country B] | ([Country C]) | Period.
- "Takeaways": 3 bullets on talent-pool scale, cost position, and tax and risk.
- "Questions to ask the client": 3 (e.g. language needs, time-zone overlap, scale over 3 years).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: 2 bullets on how to position each location for [What I sell].

RULES
- Cost of living is an index (higher = more expensive), not a currency amount; say so.
- This view has no salary data. For pay by role and city, say the Draup for Talent connector is needed.
- Use no outside sources for missing metrics; mark them "Not in Draup".

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
Bottom line and next step first: compare [Country A] and [Country B] on labour force, unemployment, median age, cost of living, inflation, corporate tax and stability, with periods, 3 takeaways and 3 client questions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which metros in [Country B] have the strongest IT teams in [Vertical]?
```

```text
Who are the biggest [Vertical] employers in [City]?
```

```text
Turn this into a one-slide location comparison.
```

## Tips for better results

- The comparison answers in a single lookup, so it is quick to run several pairs.
- Name the client to get a named contact and a dated reason to call.

## Related prompts

- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.
- [Best city for a delivery team](../../prompts/17-talent-cost-and-location/delivery-location.md): A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`demographics_data`, `get_account_id`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-country-compare`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
