[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Renewal risk check (RAG)

> **A Red/Amber/Green risk table for one customer, including your sponsor's status, with dated evidence, an overall rating and two actions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a renewal, a QBR, or when a deal goes quiet. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps | Everyone | 2–4 min | News signals, Executives & movement, Talent flow & locations, Company & financials, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Business function]` | Supply Chain |
| `[Sponsor name and title (optional)]` | VP Supply Chain Systems |
| `[Competitor]` | Blue Yonder, Manhattan Associates |
| `[What I sell]` | warehouse automation software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my customer-success risk analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [Our sponsor's function, e.g. Supply Chain]
- Sponsor name and title: [Optional, e.g. VP Supply Chain Systems]
- Competitor: [Products or firms we lose to, e.g. Blue Yonder]
- What I sell: [One line, e.g. warehouse automation software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Sponsor: look in key executives and recent exits. Red: left. Amber: title changed.
3. Senior exits in [Business function], 6 months, narrowed by workload. Red: sponsor's level or above. Amber: other director-plus.
4. Layoffs, 90 days. Red: touching [Business function] or over 5% of staff. Amber: other. Workforce growth (talent-flow window; state the months). Red: below −3%. Amber: −3% to 0%. Revenue growth, latest fiscal year. Red: below −5% without a divestment. Amber: −5% to +2%.
5. Competitor tools: check the whole tech stack for any product made by [Competitor], whatever area it's filed under. Amber: newly detected in 12 months.
6. Negative news, 90 days (restructuring, cost-cutting, merger, new vendor in our category). Anything not Red or Amber is Green.

OUTPUT
- Bottom line: 2 sentences — overall rating and the risk to act on.
- Table: Risk | Rating | Evidence | Date | Source.
- "Overall": Red if 2+ Reds or Red on Sponsor; Amber if any Red or 2+ Ambers; else Green.
- "Two actions this month", each tied to a row.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Cut-offs are editable defaults. No rows = Green (unverified). Data unavailable or sponsor not found = Not in Draup, left out of Overall.
- A newly detected competitor tool is Amber, never an automatic Red.
- Draup shows only recent moves; state the latest move date. Professional information only; no personal contact details.

STANDARD RULES (leave as is)
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Renewal risk check on [Company] from Draup: Red/Amber/Green for our sponsor, senior exits in [Business function], layoffs, workforce and revenue growth, newly detected [Competitor] tools and negative news. Overall rating plus 2 actions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who replaced the executive who left, and do we know them?
```

```text
Draft a check-in email to our sponsor that addresses the top risk without alarming them.
```

```text
Run the same check on my other top 5 customers: [Accounts].
```

## Tips for better results

- "Green (unverified)" means Draup found nothing, not that the risk is zero. Confirm with your sponsor.
- Name the competitor products you actually lose to. The check looks for those across the whole stack.

## Related prompts

- [QBR prep](../../prompts/11-account-planning/qbr-prep.md): What changed at the customer during the review period, set against the outcomes you delivered, with three talking points and three asks.
- [Customer alumni on the move](../../prompts/11-account-planning/follow-champions.md): Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.
- [Is work coming back in-house? (re-insourcing risk)](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_executive_movement`, `get_signal_news_v3`, `get_top_signals`, `accounts_talent_flow_top_metrics_v3`, `get_account_financials_v3`, `get_account_tech_stack_products_v3`, `get_tech_stack_trend_v3`

Status: **tested live**. Prompt id: `plan-risk-check`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
