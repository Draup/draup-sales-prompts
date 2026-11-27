[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Biggest logos in my territory

> **The largest employers in a vertical in one metro, by Draup-estimated local headcount, with global capability centres (GCCs) called out and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You own a city or metro and want to know the big local employers to prioritise. | Account Executive, SDR / BDR, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 1–2 min | Industry ecosystem, Company directory |

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
- Vertical: [Industry, e.g. Banking & Financial Services]
- What I sell: [one line, e.g. GCC talent and operations services — skip if you ran the start-here prompt]

STEPS
1. Resolve the city to Draup's metro name (e.g. "Bengaluru Area, India") and the vertical to Draup's name. Show both. If the metro returns nothing, try the nearest Draup metro and say which worked.
2. Pull the top employers in [Vertical] in that metro, ranked by local headcount. Take the top 25.
3. Look the 25 up in one company list and keep only the exact companies: global workforce, HQ country, and whether the metro is one of their GCC locations (a global capability centre is a company-owned offshore or captive site).
4. Work out local share = local headcount ÷ global workforce.
5. If IT-services or staffing firms appear and [Vertical] isn't IT services, move them to a separate list.

OUTPUT
- Bottom line: 2 sentences — who the big local logos are and what it means for [What I sell].
- Table (top 25, largest local headcount first): Rank | Company | Local headcount (approx.) | Global workforce | Local share % | Site type (HQ / GCC / Other) | HQ country | Who to call (title).
- "GCCs in [City]": the GCC rows, largest first.
- "Service firms in the list" (if any).
- Recommended next step: 5 accounts to prioritise, each with the likely buyer title, what to do and one dated fact.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Local headcount is a Draup estimate and can vary between lookups. Present it as approximate, never as exact.
- A GCC tag can include plants or operations sites. If a site looks like a plant, say so.
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Look up named companies by website (exact) and check each came back. Name searches match on "contains" and pull in look-alikes, so keep only companies you resolved.
- IT spend, R&D spend and local headcount are Draup estimates; say so once.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Who are the 25 biggest [Vertical] employers in [City] by Draup-estimated local headcount? Add global workforce, local share, whether the site is HQ or a GCC, and who to call.
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

- [Where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, with hubs that host both: where its delivery and engineering work happens.
- [Global capability centres (GCCs) and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with GCCs and likely new sites called out and net hiring over a stated window.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_ecosystem_employers_data`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `prospect-territory-logos`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
