# Vertical vendor league table

**Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers and where your firm ranks.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell IT or business services and need to know who you are up against in an industry. | Services, SI & Staffing Seller, Partnerships & Alliances, Sales Leader & RevOps, Marketing & ABM | Services sellers | 2–4 min | Industry ecosystem, Outsourcing deals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Life Sciences |
| `[Workload (optional)]` | Application Development & Maintenance |
| `[My company]` | Northwind Data Services |
| `[What I sell]` | clinical-data platform services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my services market analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Life Sciences]
- Workload (optional): [e.g. Application Development & Maintenance]
- My company: [As Draup spells it, e.g. Northwind Data Services]
- What I sell: [one line, e.g. clinical-data platform services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull the vertical's top outsourcing vendors (a fixed top 50). Remove advertising and media agencies, staffing, market-research, merchandising and field-marketing firms, and list what you removed. Keep the top 15.
3. Pull the top 10 outsourced workloads and the top 10 outsourcing buyers.
4. If I gave a workload, pull the top 10 providers for it among companies whose primary vertical is [Vertical].
5. Find [My company]'s rank and engagements, or say "not in the top 50".

OUTPUT
- Bottom line: 2 sentences — how the market is split and where [My company] stands.
- League table: Rank | Provider | Engagements | Share of top 15 % | Type. Types: GSI (global systems integrator), consulting, niche specialist, BPO (business-process outsourcing).
- "Concentration": top-3 share of the top 15; "concentrated" if over 50% (editable default), otherwise "long tail".
- "Top workloads": Workload | Engagements. "Top buyers": Company | Engagements | Likely owner (title).
- "[Workload] leaders" (if given): Rank | Provider | Engagements.
- "Where [My company] stands": rank, gap to #1 and #5, and the 2 workloads with the most room.
- "Excluded".
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them as the opening.
- Flag buyers whose business doesn't fit [Vertical].
- If [My company] returns nothing, try the short brand name.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Rank the top 15 outsourcing providers in [Vertical] by engagements, excluding agencies and staffing firms, with share and type. Add top workloads, top buyers, the leaders in [Workload], and where [My company] ranks.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show where [Competitor] wins [Workload] work in [Vertical]: top 10 customers.
```

```text
For the top 5 buyers, who are their top 3 providers?
```

```text
Which buyers have no top-5 provider in [Workload]?
```

## Tips for better results

- Engagement counts measure breadth of relationship, not revenue.
- Agencies and staffing firms rank high on raw counts; the prompt removes them so the table shows real services rivals.

## Related prompts

- [One-page vertical market snapshot](../../prompts/07-vertical-intelligence/vertical-snapshot.md): A one-page view of an industry: revenue and spend, top priorities with likely owners, technologies gaining ground, and who outsources what to whom.
- [Competitor's customers in my vertical](../../prompts/06-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your vertical and country, with how entrenched it is at each: your displacement targets.
- [Vendor mix vs the vertical](../../prompts/06-outsourcing-and-services/vendor-mix-benchmark.md): Where the account outsources more or less than its industry, and which leading industry providers it doesn't use yet.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_outsourcing_vendors`, `ecosystem_get_vertical_outsourcing_workloads`, `ecosystem_get_vertical_outsourcing_customers`, `get_deals_service_provider_v3`

Status: **tested live**. Prompt id: `market-vendor-league`.

</details>

[Back to Industry and market intelligence](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
