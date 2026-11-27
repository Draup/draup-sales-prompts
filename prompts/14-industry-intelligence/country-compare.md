[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Compare countries for delivery

> **A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways and questions for the client.**

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
| `[What I sell]` | nearshore delivery centre services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my location strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Country A: [In full, e.g. India]
- Country B: [In full, e.g. Poland]
- Country C (optional): [e.g. Mexico]
- What I sell: [one line, e.g. nearshore delivery centre services — skip if you ran the start-here prompt]

STEPS
1. Use full country names as Draup knows them (e.g. "United States of America", not "USA").
2. Pull Draup's country data for all of them in one go: labour force, unemployment rate, median age, cost-of-living index, inflation, corporate tax rate, political stability, and any other workforce metric Draup returns.

OUTPUT
- Bottom line: 2 sentences — how the locations compare and which fits [What I sell] best for this client.
- Table: Metric | [Country A] | [Country B] | ([Country C]) | Period or year.
- "Takeaways": 3 bullets on talent-pool scale, cost position, and tax and risk.
- "What it means for [What I sell]": 2 bullets on how to position each location.
- "Questions to ask the client": 3 questions this comparison raises (e.g. language needs, time-zone overlap, scale over 3 years).
- Recommended next step: who to contact at the client (title, e.g. head of global delivery), what to share, and why now.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Cost of living is an index (higher = more expensive), not a currency amount. Say so.
- This view has no salary data. For pay by role and city, say the Draup for Talent connector is needed.
- Use no outside sources for missing metrics; mark them "Not in Draup".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 250 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Country A] and [Country B] on labour force, unemployment, median age, cost of living, inflation, corporate tax and political stability, with the period for each, 3 takeaways and 3 client questions.
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

- This answers in a single lookup, so it is quick to run several pairs.
- Use full country names, such as 'United States of America' or 'United Kingdom'.

## Related prompts

- [Where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, with hubs that host both: where its delivery and engineering work happens.
- [Where to put a delivery team](../../prompts/17-talent-cost-and-location/delivery-location.md): A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.
- [Global capability centres (GCCs) and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`demographics_data`

Status: **tested live**. Prompt id: `market-country-compare`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
