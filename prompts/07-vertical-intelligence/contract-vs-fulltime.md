# Contract vs full-time demand

**What share of hiring for a skill is contract versus full-time, and how much staffing firms drive it: a read on staff-aug and SI demand.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell staffing, staff augmentation or SI services and want to know whether a skill's market buys contractors. | Services, SI & Staffing Seller, Partnerships & Alliances, Sales Leader & RevOps | Services sellers | 1–2 min | Hiring & job postings |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Technology]` | SAP S/4HANA |
| `[Country (optional)]` | United States of America |
| `[What I sell]` | SAP staff augmentation |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my talent market analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Technology: [Skill or product, e.g. SAP S/4HANA]
- Country (optional): [In full, e.g. United States of America]
- What I sell: [one line, e.g. SAP staff augmentation — skip if you ran the start-here prompt]

STEPS
1. Resolve the technology, and the country if given, to Draup's names and show them.
2. Pull the work-type breakdown of postings for [Technology] over the last 12 months: full-time, contract, part-time, other and no type stated.
3. Work out each type's share of all postings and of postings that state a type.
4. Pull the top 15 companies posting for [Technology] in the same window and country, and classify each as end employer, staffing firm or IT services/SI.

OUTPUT
- Bottom line: 2 sentences — whether this market buys contractors and what it means for [What I sell].
- Header: technology, country (or "global") and the exact window.
- Table: Work type | Postings | Share of all % | Share of stated-type %.
- Verdict: "contract-heavy" if contract is over 40% of stated postings, "balanced" at 20–40%, otherwise "full-time-led" (editable defaults).
- "Who's hiring": Company | Postings | Type | Who to call (title, end employers only).
- "What it means for [What I sell]": 3 bullets.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never count no-type postings as full-time, and always show the no-type share.
- Use the same window and country for every number. City breakdowns are out of scope here.
- Many staffing or SI firms in the top 15 is another sign of contract-led demand.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Label anything you infer (buyer title, intent, fit) as "likely".
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
For [Technology] postings in the last 12 months, show the contract vs full-time split among postings stating a type, the no-type share, and how many top-15 hirers are staffing or IT-services firms.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run the same check for [another technology] and compare the two.
```

```text
Which end employers post the most contract roles for [Technology]?
```

```text
What job titles dominate [Technology] postings?
```

## Tips for better results

- A large no-type share is normal. Judge the split on postings that state a type.
- If staffing firms dominate the hirer list, demand is often being met through contractors: a staff-aug opening.

## Related prompts

- [Who's hiring for a tech or role](../../prompts/05-prospecting-and-lists/hiring-led-list.md): The end employers posting the most jobs for a technology or buyer role, cleaned of job boards and staffing firms, with who to call and the industries driving demand.
- [Hard-to-hire roles: staffing pitch](../../prompts/10-talent-cost-and-location/hard-to-hire.md): Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.
- [Compare countries for delivery](../../prompts/07-vertical-intelligence/country-compare.md): A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways and questions for the client.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_visualize_work_type_v3`, `talent_demand_top_companies_v3`

Status: **tested live**. Prompt id: `market-contract-vs-fulltime`.

</details>

[Back to Industry and market intelligence](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
