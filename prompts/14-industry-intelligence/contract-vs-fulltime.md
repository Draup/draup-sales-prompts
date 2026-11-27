[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Check if a skill market buys contractors

> **What share of hiring for a skill is contract versus full-time, how much staffing firms drive it, what it means for staff-aug or SI demand, and a named end-employer contact.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell staffing, staff augmentation or SI services and want to know whether a skill's market buys contractors. | Services, SI & Staffing Seller, Partnerships & Alliances, Sales Leader & RevOps | Services sellers | 1–2 min | Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Technology]` | SAP S/4HANA |
| `[Territory (optional)]` | United States of America |
| `[What I sell]` | SAP staff augmentation |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my talent market analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Technology: [skill or product, e.g. SAP S/4HANA]
- Territory (optional): [country in full; default: my territory from setup, or "global"; e.g. United States of America]
- What I sell: [one line, e.g. SAP staff augmentation — skip if you ran the start-here prompt]

STEPS
1. Resolve the technology to Draup's skill name (e.g. "CrowdStrike Falcon", not "CrowdStrike") and [Territory] to Draup's name; show them. If postings come back 0, retry once with the product name.
2. Pull the work-type breakdown of postings for [Technology] over the last 12 months: full-time, contract, part-time, other and no type stated.
3. Work out each type's share of all postings and of postings that state a type.
4. Pull the top 15 companies posting for [Technology] in the same window and territory, merge subsidiaries into parents, and classify each as end employer, staffing firm or IT services/SI.
5. For the top end employer: its top 3 executives in the function that owns [Technology] and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — whether this market buys contractors and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Split": Work type | Postings | Share of all % | Share of stated-type %. Verdict: "contract-heavy" over 40% of stated, "balanced" at 20–40%, else "full-time-led" (editable).
- "Who's hiring" (top 10): Company | Postings | Type.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: header with technology, territory (or "global") and exact window; ranks 11–15; 3 bullets on what it means for [What I sell].

RULES
- Never count no-type postings as full-time, and always show the no-type share.
- Use the same window and territory for every number; city breakdowns are out of scope.
- Many staffing or SI firms in the top 15 is another sign of contract-led demand.
- Postings are openings, not hires.

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
Bottom line and next step first: for [Technology] postings in 12 months, the contract vs full-time split (stated types), the no-type share, how many top-15 hirers are staffing or IT-services firms, and who to call.
```

</details>

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
- If staffing firms dominate the hirer list, demand is often met through contractors: a staff-aug opening.

## Related prompts

- [Who's hiring for a tech or role](../../prompts/06-prospecting-and-lists/hiring-led-list.md): The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.
- [Roles the client can't hire: staffing pitch](../../prompts/17-talent-cost-and-location/hard-to-hire.md): Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.
- [Compare countries for a delivery centre](../../prompts/14-industry-intelligence/country-compare.md): A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways, client questions and, if you name the client, who to talk to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_visualize_work_type_v3`, `talent_demand_top_companies_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-contract-vs-fulltime`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
