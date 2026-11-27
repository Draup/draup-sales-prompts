[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find uncovered functions worth selling to

> **Every business function at an existing customer scored on priorities, hiring and outsourced work against where you already sell, with the top 3 uncovered functions, the named leaders who own them and a bridge from your current footprint.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before an account plan or QBR, when you want to grow beyond the function you sell into today. Use this to rank functions across the account; use "Entry points" (plan-entry-points) instead to pick initiatives inside one function. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 4–6 min | Priorities & opportunities, Hiring & job postings, Outsourcing deals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | roche.com |
| `[Current footprint]` | IT – data engineering and BI (or my saved account notes) |
| `[What I sell]` | data and analytics services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-expansion strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. roche.com]
- Current footprint: [where we sell today, by function or workload, e.g. IT – data engineering and BI — or my saved account notes]
- What I sell: [one line, e.g. data and analytics services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
A function worth pursuing shows three signals: leaders talking about it, hiring behind it and work already bought from outside.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Pull the grouped key priorities (up to 3 per function, with quarter), not the full list, which is too large.
3. Pull 12-month hiring by function (top 15), last 5 full months vs the 5 before.
4. Pull outsourced workloads (types of work, e.g. Data Engineering) by deal count (top 20), mapped to functions, plus active engagements per function; if a function returns zero, retry Draup's other name (R&D for ER&D).
5. Score each function 0–3 (editable default): +1 for an earnings-call priority in the last two fiscal quarters, +1 for Rising hiring or postings in the top third of functions, +1 for 20+ deals in its workloads. Mark Covered if it matches [Current footprint].
6. Keep only uncovered functions that fit [What I sell]. For the top 2, pull senior leaders filtered by the function and the workloads matching [What I sell] (one page of 10 each).
7. Pull the most important 90-day news item touching a top function.

OUTPUT
- Bottom line: 2 sentences — the best uncovered function and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the top function, the action this week and the dated why-now; if none, say so.
- Table "Top 3 whitespace functions": Function | Score | Why now (dated priority or hiring fact) | Leader (name, title).
- Table "Function heat map" (up to 10): Function | Latest priority (quarter) | Postings and trend | Engagements | Score (Covered?).
- "Bridge": per top function, how [Current footprint] gets us in the room (shared data, leader or programme).
- Detail: who owns each top function (Name | Full title | Location | Years in title, up to 5) and incumbent providers.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Catch-all workloads (Account Management, Project/Programs Management) never score a function.
- Don't recommend a function whose only signal is outsourcing to agencies or staffing firms.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- If the company sells technology itself, ignore its own products and priorities about them.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Score every business function at [Company] on priorities, 12-month hiring and outsourced work. Lead with the top 3 uncovered functions for [What I sell] and the named leader to approach, with a dated why-now.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [Function], map the full buying committee.
```

```text
Which providers already work in [Function] and how deep are they?
```

```text
Draft a 100-word email from our current sponsor introducing us to the [Function] leader.
```

## Tips for better results

- Be precise in Current footprint (function and workload); vague footprints produce vague whitespace.
- The Bridge line is what turns a cold function into a warm introduction.

## Related prompts

- [Best entry points: expand or new](../../prompts/11-account-planning/entry-points.md): The five best ways in for what you sell, each marked Expand (we already serve it) or New, with dated evidence, incumbents, any installed competitor and the likely owner.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.
- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_key_account_priorities`, `accounts_hiring_demand_category_v3`, `get_deals_workloads_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `expand-function-whitespace`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
