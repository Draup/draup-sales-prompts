[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Size a role and who employs it

> **How many people hold a role in up to 3 countries, how fast supply is growing, and which companies employ the most, split into prospects and services competitors.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You're sizing a services practice, a staffing market or a target list built around one skill set. | Services, SI & Staffing Seller, Sales Leader & RevOps, Partnerships & Alliances | Services sellers | 2–4 min | Talent cost & supply |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Role]` | SAP FICO Consultant |
| `[Countries]` | India, Poland, Philippines |
| `[Vertical (optional)]` | Retail |
| `[What I sell]` | SAP finance managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market-sizing analyst for a services practice. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company lookups. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Role: [e.g. SAP FICO Consultant]
- Countries: [up to 3, in full, e.g. India, Poland, Philippines]
- Vertical (optional): [limit to people at companies in this industry, e.g. Retail]
- What I sell: [one line, e.g. SAP finance managed services — skip if you ran the start-here prompt]

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use. Then confirm Draup's name for each country.
2. For each country, pull the talent supply for the role, its likely range, 3-year growth and how reliable the estimate is, limited to [Vertical] if given.
3. For the largest country, pull the top 25 current employers of people in this role.
4. Sort those employers into end clients (use the skill in-house) and services firms (IT services, consulting, staffing). Keep the top 15 overall.

OUTPUT
- Bottom line: 2 sentences — how big and fast-growing the supply is, and what it means for [What I sell].
- "Supply": Country | Talent supply | Likely range | 3-yr growth | Reliability. Largest first.
- "Who employs them": Rank | Employer | Type (End client or Services firm) | People in role | Likely owner (for end clients). Top 15.
- "Prospects": end clients with the largest in-house teams (managed-services or augmentation candidates).
- "Competitors": services firms holding most of this skill, met in both deals and hiring.
- "Why this matters for [What I sell]": 3 bullets, each fact → implication → action.
- Recommended next step: who to take it to (title), what to do, and why now (one dated figure).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Show the likely range beside every supply figure; if reliability is poor, say so beside the number.
- Employer counts come from profiles Draup has matched: use them to rank, not as exact headcount.
- If the role returns nothing in a country, write "Not in Draup" for that row; never borrow another country's figure.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
How many [Role]s are there in [Countries] per Draup, with likely range and 3-year growth? Then list the top 15 employers in the largest country, split into end clients (prospects) and services firms (competitors).
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the same supply figures for two adjacent roles so I can see the wider practice.
```

```text
For the top 5 prospects, show their recent hiring for this role.
```

```text
Which metros in the largest country hold most of this skill?
```

## Tips for better results

- Large in-house teams at end clients are often expensive and hard to retain: a good managed-services conversation.
- Use the likely range, not just the point estimate, when you put the number in a business case.

## Related prompts

- [Hard-to-hire roles: staffing pitch](../../prompts/10-talent-cost-and-location/hard-to-hire.md): Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.
- [Who's hiring for a tech or role](../../prompts/05-prospecting-and-lists/hiring-led-list.md): The end employers posting the most jobs for a technology or buyer role, cleaned of job boards and staffing firms, with who to call and the industries driving demand.
- [Where a vertical's teams sit](../../prompts/07-vertical-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, with hubs that host both: where its delivery and engineering work happens.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_talent_size_compare_roles_v3`, `talent_size_compare_locations`, `visualize_account`

Status: **documented, not live-tested**. Prompt id: `talent-role-sizing`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
