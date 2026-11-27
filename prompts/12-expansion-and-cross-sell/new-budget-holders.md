[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# New budget holders outside our footprint

> **Senior leaders new in role (about 18 months or less) in the functions you don't yet sell to, plus announced leadership changes, each with the priority they likely own, a first-90-days angle and the one to contact first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Quarterly in your top accounts, or when you need a reason to reach a new part of a customer. Use this to widen into functions you don't cover; use "New leaders and warm paths" (people-new-leaders-warm-paths) instead for warm intros in the function you already sell to. | Account & Customer Success Manager, Account Executive, SDR / BDR, Sales Leader & RevOps | Everyone | 2–4 min | Executives & movement, News signals, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | boeing.com |
| `[Functions we don't cover]` | Finance & Accounting, Human Resources, Procurement |
| `[What I sell]` | finance and HR process automation |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-expansion researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. boeing.com]
- Functions we don't cover: [1–3 business functions, e.g. Finance & Accounting, Human Resources, Procurement]
- What I sell: [one line, e.g. finance and HR process automation — skip if you ran the start-here prompt]

CONTEXT (why this matters)
New leaders review vendors and set priorities in their first year; in a customer, one in an uncovered function is the cleanest way in.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Pull senior leaders in [Functions we don't cover], 10 per page, up to 3 pages. Keep Director and above by full title with 18 months or less in their current title (editable default).
3. Search Draup's news for executive appointments, departures and interim roles at [Company] in the last 6 months; keep only items where [Company] is the employer, and mark the most important from the last 90 days.
4. Pull up to 3 priorities per uncovered function (latest fiscal quarters first) and match each new leader to the closest by function and title.
5. Rank: C-level or "Head of" first, then budget control, then shortest time in title.

OUTPUT
- Bottom line: 2 sentences — the best new budget holder and what it means for [What I sell]. Add: people checked, pages, people kept.
- Recommended next step: a named person (name, full title), the top new leader, the action this week and the dated why-now; if none, say so.
- Table "New budget holders" (up to 10): Name | Full title | Function | Months in title | Linked priority (quarter).
- "First-90-days angles": top 3 leaders, 2 lines each, tied to [What I sell] and to proof from the part of [Company] we serve.
- "Announced changes" (6 months): Date | Change (appointment, exit, interim) | Role | Source.
- Detail: each leader's unit (flag subsidiaries), location and budget control; functions with no new leader.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Interim leaders and announced searches mean decisions may wait; say so next to the person.
- If a function returns fewer than 3 people, say profiles may be thin rather than concluding there's no leader.
- Board appointments are not budget holders.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Leadership data can lag about 3 months; give the latest move date seen.
- If European executives return none, say profiles there may be restricted.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 400 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
At [Company], find senior leaders in [Functions we don't cover] 18 months or less in title. Lead with the one to contact first and the dated why-now, then announced changes, linked priorities and first-90-days angles.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 90-word intro email from our current sponsor to [Leader].
```

```text
Where did [Leader] work before, and was it one of our customers?
```

```text
Map the rest of the buying committee under [Leader].
```

## Tips for better results

- Months in title comes from the profile and can lag about 3 months; confirm before you open with "congratulations".
- Announced departures are as useful as hires: the successor will review vendors.

## Related prompts

- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Check sponsor risk and relationship gaps](../../prompts/12-expansion-and-cross-sell/sponsor-coverage.md): A risk read on your executive sponsor (tenure, new bosses, announced changes), a coverage grid of who you know versus who matters, likely successors and the 3 named relationships to build next.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `get_key_account_priorities`

Status: **tested live**. Prompt id: `expand-new-budget-holders`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
