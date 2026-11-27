# Where a vertical's teams sit

**The metros where an industry's IT and R&D teams are concentrated, with hubs that host both: where its delivery and engineering work happens.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are choosing where to hold events, recruit or place delivery capacity for an industry. | Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller | Services sellers | 1–2 min | Industry ecosystem |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Banking & Financial Services |
| `[Country (optional)]` | India |
| `[What I sell]` | data-engineering services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my market and location analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Banking & Financial Services]
- Country (optional): [In full, e.g. India]
- What I sell: [one line, e.g. data-engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical, and the country if given, to Draup's names and show them.
2. Pull the metros where the vertical's IT teams are concentrated, ranked by Draup's workforce-strength index. The data is global, so if I gave a country, keep only its metros.
3. Do the same for the vertical's R&D teams.
4. Mark metros that appear on both lists.

OUTPUT
- Bottom line: 2 sentences — where the vertical's technical work sits and what it means for [What I sell].
- "IT hubs" (top 10, highest index first): Rank | Metro | Country | Workforce-strength index.
- "R&D hubs" (top 10): Rank | Metro | Country | Workforce-strength index.
- "Dual hubs": metros on both lists, with one line on why that matters for delivery or events.
- "Where to focus for [What I sell]": 3 metros, one reason each.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- The index is relative strength, not headcount. Never call it employees, and only compare values within one list.
- These hubs show where delivery and engineering sit, not where buyers or budget holders are. Say so once.
- Recommended next step names an action such as an event, a recruiting push or a site visit, with the likely owner (title).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 250 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Rank the top 10 metros for [Vertical] IT teams and the top 10 for R&D teams by Draup's workforce-strength index, flag metros on both lists, and say where to focus for [What I sell].
```

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

- [Biggest logos in my territory](../../prompts/05-prospecting-and-lists/territory-logos.md): The largest employers in a vertical in one metro, by Draup-estimated local headcount, with global capability centres (GCCs) called out and who to call.
- [Compare countries for delivery](../../prompts/07-vertical-intelligence/country-compare.md): A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways and questions for the client.
- [Global capability centres (GCCs) and the services play](../../prompts/06-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_vertical_map_data_it`, `ecosystem_vertical_map_data_r_and_d`

Status: **tested live**. Prompt id: `market-talent-hubs`.

</details>

[Back to Industry and market intelligence](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
