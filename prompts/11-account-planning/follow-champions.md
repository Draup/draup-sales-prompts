[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Customer alumni now at your targets

> **Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want warm paths into new logos through people who may know your product. Use "New leaders and warm intro paths" instead for warm paths into the new leaders at one account. | Account Executive, Account & Customer Success Manager, SDR / BDR | Everyone | 2–4 min | Executives & movement, Talent flow & locations, News signals |

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
Act as my relationship-mapping analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [Our customer's website, e.g. walmart.com]
- Accounts: [Our target list, e.g. Target, Kroger, Costco]
- Function or workload: [e.g. Supply Chain — a function is fine, I'll map it to workloads]
- Champion names (optional): [Paste names from your CRM]

STEPS
1. Find the company by website (no result: try its name once and show the match score). Confirm it's the parent, not a subsidiary or sister company; if several match, ask me. Use Draup's exact name from then on.
2. Map [Function or workload] to its 1–3 main workloads and say which. Pull leadership exits for the last 12 months, one workload at a time. Keep director-plus by full title and rows whose previous company is [Company]. State rows checked and the latest move date.
3. For each: name, old title, new employer, new title, month.
4. Match names against [Champion names] and new employers against [Accounts], allowing for spelling differences.
5. Pull talent-flow counts from [Company] to each target; write "not in the top flows" if absent.
6. Timing: for the best warm path, pull the new employer's most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how many warm paths and the best one.
- Recommended next step: the best warm path (name and new title), the opening line, and why now (their move month or the step-6 news). If there's no warm path, say so and name the closest alumnus.
- "Alumni on the move": Name | Old title | New employer and title | Month | Match (champion, my list or none).
- "Warm paths": named champions first, then my list, each with one opening line about their new role.
- Gaps: what Draup didn't have — worth checking in my CRM.
- Detail: "Flow to my targets" (Target | People moved, window).

RULES
- Never claim a past buying relationship. Mention our work with [Company] only if my CRM confirms they were involved.
- Names come only from leadership moves; talent flow gives counts, never names.
- If no exits come back, try a neighbouring workload.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Talent-flow data ends about 3 months ago; state the months.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 380 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named alumnus, dated move) first. Which director-plus people left [Company] recently in [Function or workload], per Draup? Name, old title, new employer, new title, month. Flag employers on my list ([Accounts]) and names I paste.
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
- Leadership data lags about 3 months, so "recent" means up to the latest move date the answer states.

## Related prompts

- [Who they lose talent to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.
- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_executive_movement`, `accounts_talent_flow_insights_companies_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-follow-champions`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
