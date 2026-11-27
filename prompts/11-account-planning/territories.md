[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Carve balanced territories

> **An industry-and-country account universe split into N territories balanced on Draup-estimated IT spend (or revenue or count), with HQ clusters kept together and owned accounts excluded.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Advanced: annual territory planning or when a new rep joins; best run by RevOps or a sales leader. | Sales Leader & RevOps | Everyone | 4–6 min | Company directory |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Automotive |
| `[Country]` | Germany |
| `[Minimum employees]` | 5000 |
| `[Number of territories]` | 3 |
| `[Accounts already owned (exclude)]` | bmwgroup.com, porsche.com |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my RevOps territory planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Automotive]
- Country: [HQ country in full, e.g. Germany]
- Minimum employees: [e.g. 5000]
- Number of territories: [e.g. 3]
- Balance on: [Optional: Draup-estimated IT spend (default), revenue or account count]
- Accounts already owned: [Optional websites to exclude, e.g. bmwgroup.com]

STEPS
1. Confirm Draup's names for the vertical and country.
2. Pull companies whose primary vertical is [Vertical], HQ in [Country], with [Minimum employees]+ staff, with HQ metro, revenue and IT spend, sorted by IT spend. Page 50 at a time, up to 5 pages; if more remain, stop and ask me to raise the threshold.
3. Remove accounts already owned (match by website).
4. Separately pull companies with [Vertical] as a secondary vertical, same size and country. List them as "Consider adding"; don't assign them.
5. Assign accounts in balance order, each to the territory with the lowest running total, keeping same-metro companies together where it costs under 10% balance (editable default).

OUTPUT
- Bottom line: 2 sentences — universe size and how even the split is.
- "Universe": accounts and total of the balance measure (USD millions, fiscal year).
- "Territory summary": Territory | Accounts | Total | Share | Main HQ metros.
- One table per territory: Account | HQ metro | Employees | Revenue | IT spend.
- "Consider adding": Company | Primary vertical | Employees | IT spend.
- "Data flags": possibly inactive companies, accounts without IT spend (placed by revenue), and how many matches lack size data.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Size filters drop companies with no workforce figure (often large private firms); report how many and offer to include them.
- IT spend is a Draup estimate, often modelled from revenue; say so.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Use primary vertical only, sort largest first, and flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
List [Vertical] companies (primary vertical) headquartered in [Country] with [Minimum employees]+ staff from Draup, drop accounts already owned, and split the rest into [Number of territories] territories balanced on IT spend, keeping HQ metros together.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Rebalance on account count instead.
```

```text
Add Draup's Opportunity Index score and show the top 5 per territory.
```

```text
Export the assignments as a table I can paste into a spreadsheet.
```

## Tips for better results

- Large suppliers whose main industry is different won't appear in the main list. Check the "Consider adding" section.
- Balancing on spend favours fairness of opportunity; balancing on count favours fairness of workload. Pick one.

## Related prompts

- [Tier my accounts by propensity to buy](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on an editable Fit (0–50) and Timing (0–50) rubric, tiered A, B or C and placed on a fit-versus-timing grid, with the driver behind each score.
- [Build and size an ICP list](../../prompts/06-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`build_company_filters_v3`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `plan-territories`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
