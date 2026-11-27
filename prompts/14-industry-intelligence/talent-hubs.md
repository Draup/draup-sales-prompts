[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find where a vertical's teams sit

> **The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are choosing where to hold events, recruit or place delivery capacity for an industry. | Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller | Services sellers | 1–2 min | Industry ecosystem |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Banking & Financial Services |
| `[Country (optional)]` | India |
| `[What I sell]` | data-engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market and location analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Banking & Financial Services]
- Country (optional): [in full, e.g. India]
- What I sell: [one line, e.g. data-engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical, and the country if given, to Draup's names and show them.
2. Pull the metros where the vertical's IT teams are concentrated, ranked by Draup's workforce-strength index. The data is global, so if I gave a country, keep only its metros.
3. Do the same for the vertical's R&D teams, and mark metros on both lists.
4. For the #1 hub: the biggest [Vertical] employer there, its top 3 executives located in that metro in the function closest to What I sell, and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — where the vertical's technical work sits and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 4), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "IT hubs" (top 10): Rank | Metro | Country | Index | Also an R&D hub?
- "Where to focus": 3 metros, one reason each (delivery, events or recruiting).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "R&D hubs" (top 10): Rank | Metro | Country | Index.

RULES
- The index is relative strength, not headcount. Never call it employees, and only compare values within one list.
- These hubs show where delivery and engineering sit, not where budget holders are; say so once.
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
Bottom line and next step first: the top 10 metros for [Vertical] IT teams and for R&D teams by Draup's workforce-strength index, metros on both lists, 3 places to focus, and who to meet in the #1 hub.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who are the 10 biggest [Vertical] employers in the #1 metro?
```

```text
Which companies have GCCs in the top 3 IT hubs?
```

```text
Compare the top 2 countries on labour force, cost of living and tax.
```

## Tips for better results

- Use the index to rank places, not to size teams.
- Add a country to get a territory-level view.

## Related prompts

- [Find the biggest logos in your city](../../prompts/06-prospecting-and-lists/territory-logos.md): The largest employers in a vertical in one metro, by Draup-estimated local headcount, with global capability centres (GCCs) called out and a named person to call first.
- [Compare countries for a delivery centre](../../prompts/14-industry-intelligence/country-compare.md): A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways, client questions and, if you name the client, who to talk to.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_vertical_map_data_it`, `ecosystem_vertical_map_data_r_and_d`, `get_ecosystem_employers_data`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-talent-hubs`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
