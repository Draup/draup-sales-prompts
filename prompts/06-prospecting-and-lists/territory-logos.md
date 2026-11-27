[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find the biggest logos in your city

> **The largest employers in a vertical in one metro, by Draup-estimated local headcount, with global capability centres (GCCs) called out and a named person to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You own a city or metro and want the big local employers to prioritise. | Account Executive, SDR / BDR, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 1–2 min | Industry ecosystem, Company directory |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[City]` | Bengaluru |
| `[Vertical]` | Banking & Financial Services |
| `[What I sell]` | GCC talent and operations services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my territory planning analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- City: [e.g. Bengaluru]
- Vertical: [industry, e.g. Banking & Financial Services]
- What I sell: [one line, e.g. GCC talent and operations services — skip if you ran the start-here prompt]

STEPS
1. Resolve the city to Draup's metro name (e.g. "Bengaluru Area, India") and the vertical to Draup's name; show both. If the metro returns nothing, try the nearest Draup metro and say which worked.
2. Pull the top employers in [Vertical] in that metro, ranked by local headcount; take the top 25.
3. Merge subsidiaries into parents, look them up in one company list and keep only the exact companies: global workforce, HQ country, and whether the metro is one of their GCC locations (a global capability centre is a company-owned offshore or captive site).
4. Work out local share = local headcount ÷ global workforce. Move IT-services or staffing firms to a separate list unless [Vertical] is IT services.
5. For the best fit for [What I sell]: its top 3 executives located in [City] in the function closest to What I sell, and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — who the big local logos are and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 10" (largest local headcount first): Company | Local headcount (approx.) | Local share % | Site type (HQ / GCC / Other).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: rows 11–25; global workforce and HQ country for all; "GCCs in [City]"; service firms in the list.

RULES
- Local headcount is a Draup estimate and can vary between lookups; present it as approximate.
- A GCC tag can include plants or operations sites; if a site looks like a plant, say so.
- Look up named companies by website or exact name; "contains" matches pull in look-alikes.

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
Bottom line and next step first: the 10 biggest [Vertical] employers in [City] by Draup-estimated local headcount, with local share, HQ or GCC site type, and who to call at the best one.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5 GCCs, which functions are they hiring for in [City]?
```

```text
Who leads the [City] centre at the top 3 companies?
```

```text
Compare [City] with [another city] for the same vertical.
```

## Tips for better results

- A high local share means the site matters to the company, which often means local decision makers.
- Use local headcount to rank companies, not to size teams.

## Related prompts

- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_ecosystem_employers_data`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `prospect-territory-logos`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
