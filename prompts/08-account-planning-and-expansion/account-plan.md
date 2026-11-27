[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Draft an account plan

> **An account plan in eight parts: snapshot, their strategy in their own words, buying committee, incumbents, ranked expansion plays, risks and a 90-day plan, plus an optional short SWOT.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Annual or half-year account planning, or when you inherit a strategic account. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps | Everyone | 6–10 min | Company & financials, Priorities & opportunities, Executives & movement, Tech stack, Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | bmw.com |
| `[What I sell]` | supply-chain planning software |
| `[Business function]` | Supply Chain |
| `[Already buy from us (optional)]` | demand planning for two regions |
| `[Our goal (optional)]` | double ARR in 12 months |
| `[Competitor (optional)]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my strategic account planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. bmw.com]
- What I sell: [One line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Business function: [The function that buys from us, e.g. Supply Chain]
- Already buy from us: [Optional, e.g. demand planning for two regions]
- Our goal: [Optional, e.g. double ARR in 12 months]
- Competitor: [Optional, up to 3, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Snapshot: profile, latest revenue (USD at Draup's rate), Draup-estimated IT spend, Opportunity Index.
3. Strategy: top 5 [Business function] priorities, sorted by date yourself, with source, quarter and workloads.
4. Buying committee: top 8 executives in [Business function] by full title and budget control; if none, list 5 titles to target.
5. Incumbents: products on those workloads (last seen, strength; skip Generic rows), top providers, and any [Competitor] product anywhere in the stack.
6. Risks: senior exits in 6 months (by workload, latest move date), layoffs in 90 days, [Competitor] products newly detected in 12 months.

OUTPUT
- Bottom line: 2 sentences — prize and first play.
- Seven sections, each ending "Source: … (date)": Snapshot; "Their strategy in their own words" (Priority | Quarter | Source | Workloads); Buying committee (Name | Full title | Budget control | Why); Incumbents (Workload | Products | Providers | [Competitor]?); "Expansion plays" (top 3 by evidence, building on what they buy; High-usage [Competitor] on the core workload = displacement, not greenfield); Risks (3 dated); 90-day plan toward [Our goal] (two actions per 30 days, owner role each).
- Optional "SWOT" if I ask: 2 cited bullets per quadrant.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- In banking and consulting, VP/SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.
- Professional information only; no personal contact details.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Keep to about 600 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Draft an account plan for [Company] from Draup: snapshot, [Business function] priorities in their own words, buying committee, incumbents, ranked expansion plays for [What I sell], risks and a 90-day plan. Cite source and date per section.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Add the short SWOT section.
```

```text
Turn the 90-day plan into a mutual action plan I can share with my champion.
```

```text
Run a renewal risk check on this account.
```

```text
Write a 120-word executive summary of this plan for my VP.
```

## Tips for better results

- Paste what they already buy and your goal. The expansion plays and 90-day plan get much sharper.
- When executive data is thin, the plan lists target titles instead, so you know who to find.

## Related prompts

- [Renewal risk check (RAG)](../../prompts/08-account-planning-and-expansion/risk-check.md): A Red/Amber/Green risk table for one customer, including your sponsor's status, with dated evidence, an overall rating and two actions.
- [Entry points and whitespace](../../prompts/08-account-planning-and-expansion/entry-points.md): The five best ways into the account for what you sell, each with dated evidence, incumbents and the likely owner.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_deals_service_provider_v3`, `get_account_executive_movement`, `get_top_signals`, `get_tech_stack_trend_v3`

Status: **tested live**. Prompt id: `plan-account-plan`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
