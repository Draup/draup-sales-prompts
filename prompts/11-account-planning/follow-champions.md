[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Customer alumni on the move

> **Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want warm paths into new logos through people who may know your product. | Account Executive, Account & Customer Success Manager, SDR / BDR | Everyone | 2–4 min | Executives & movement, Talent flow & locations |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Accounts]` | Target, Kroger, Costco, Home Depot |
| `[Function or workload]` | Supply Chain |
| `[Champion names (optional)]` | paste names from your CRM |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my relationship-mapping analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Our customer's website, e.g. walmart.com]
- Accounts: [Our target list, e.g. Target, Kroger, Costco]
- Function or workload: [Required, e.g. Supply Chain]
- Champion names: [Optional, paste names from your CRM]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull executive exits, last 12 months, narrowed to the workloads behind [Function or workload]. Keep director-plus by full title and rows whose previous company is [Company].
3. For each: name, old title, new employer, new title, month.
4. Match names against [Champion names] and new employers against [Accounts], allowing for spelling differences.
5. Pull talent-flow counts from [Company] to each target; write "not in the top flows" if absent.

OUTPUT
- Bottom line: 2 sentences — how many warm paths and the best one.
- "Alumni on the move": Name | Old title | New employer | New title | Month | Named champion? | On my list?
- "Warm paths": named champions first, then my list, each with one opening line about their new role.
- "Flow to my targets": Target | People moved (window).
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never claim a past buying relationship. Mention our work with [Company] only if my CRM confirms they were involved.
- Names come only from executive movement; talent flow gives counts, never names.
- If no exits come back, try a neighbouring workload.

STANDARD RULES (leave as is)
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Use professional information only (name, title, employer, Draup profile link). No personal contact details; don't infer personal details or past buying relationships.
- Draup shows only the latest 10 or so moves per type and can't filter by function: narrow by workload, state the latest move date and rows checked, and keep rows where [Company] is the current (for exits, previous) employer.
- Talent-flow data ends about 3 months ago; state the months covered.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which director-level and above people left [Company] recently in [Function or workload], per Draup? Name, old title, new employer, new title, month. Flag new employers on my list ([Accounts]) and any names I paste.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For each warm path, find the new employer's priorities in their function.
```

```text
Draft a 70-word congratulations note on the first person's new role.
```

```text
Who replaced each of them at [Company]?
```

## Tips for better results

- Paste your real champions' names. Draup doesn't know who used your product, so a confirmed match is worth far more than a title match.
- Narrow by function or workload. Draup lists only the most recent moves, so a narrow search surfaces more of the people you care about.

## Related prompts

- [Talent rivals: who they lose people to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, and credible peers to benchmark against.
- [New leaders in the last 6 months](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted in the last 6 months in your area, where they came from, and which ones arrive from your customers.
- [Renewal risk check (RAG)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer, including your sponsor's status, with dated evidence, an overall rating and two actions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_executive_movement`, `accounts_talent_flow_insights_companies_v3`

Status: **tested live**. Prompt id: `plan-follow-champions`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
