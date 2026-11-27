[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who wins services work in a vertical

> **Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell IT or business services and need to know who you are up against in an industry. | Services, SI & Staffing Seller, Partnerships & Alliances, Sales Leader & RevOps, Marketing & ABM | Services sellers | 2–4 min | Industry ecosystem, Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Life Sciences |
| `[Workload (optional)]` | Application Development & Maintenance |
| `[My company]` | Northwind Data Services (illustrative) |
| `[What I sell]` | clinical-data platform services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my services market analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Life Sciences]
- Workload (optional): [a type of work, e.g. Application Development & Maintenance]
- My company: [as Draup spells it, e.g. Northwind Data Services (illustrative)]
- What I sell: [one line, e.g. clinical-data platform services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull the vertical's top outsourcing vendors (a fixed top 50). Remove advertising and media agencies, staffing, market-research, merchandising and field-marketing firms; list what you removed. Keep the top 15.
3. Pull the top 10 outsourced workloads and the top 10 outsourcing buyers.
4. If I gave a workload, pull the top 10 providers for it among companies whose primary vertical is [Vertical].
5. Find [My company]'s rank and active engagements, or say "not in the top 50"; if nothing returns, try the short brand name.
6. For the top buyer where [My company] is absent: its top 3 executives in the function closest to What I sell and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how the market is split and where [My company] stands.
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "League table" (top 10): Rank | Provider | Active engagements (Draup-derived) | Share of top 15 % | Type (global systems integrator, consulting, niche specialist, business-process outsourcer).
- "Where [My company] stands": rank, gap to #1 and #5, and the 2 workloads with the most room.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: ranks 11–15; concentration (top-3 share; "concentrated" over 50%, editable); top workloads; top buyers with likely owner; "[Workload] leaders"; excluded firms.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them as the opening.
- Flag buyers whose business doesn't fit [Vertical].
- Engagements are Draup-derived estimates, not public contracts; never call them signed deals.
- If an industry returns zeros, say so, retry with its parent and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: rank the top 10 outsourcing providers in [Vertical] by active engagements, agencies and staffing removed; show where [My company] ranks, the top buyers, and who to call at the best opening.
```

</details>

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

- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry, optionally scoped to your region: size and growth, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.
- [A rival's customers you can win](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.
- [How their vendor mix compares with peers](../../prompts/10-outsourcing-and-services/vendor-mix-benchmark.md): Where the account outsources more or less than its industry, which leading industry providers it doesn't use yet, and who to raise it with.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_outsourcing_vendors`, `ecosystem_get_vertical_outsourcing_workloads`, `ecosystem_get_vertical_outsourcing_customers`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-vendor-league`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
