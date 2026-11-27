[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# QBR prep

> **What changed at the customer during the review period, set against the outcomes you delivered, with three talking points and three asks.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| The week before a quarterly or executive business review. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Executives & movement, Hiring & job postings, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Review period]` | 1 Aug 2026 – 31 Oct 2026 |
| `[What I sell]` | warehouse automation software, live in 40 distribution centres |
| `[Outcomes we delivered]` | paste results from this period |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my customer-success and QBR analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Review period: [e.g. 1 Aug 2026 – 31 Oct 2026]
- What I sell: [One line, e.g. warehouse automation software, live in 40 distribution centres — skip if you ran the start-here prompt]
- Outcomes we delivered: [Paste this period's results, e.g. uptime, savings]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Financials: latest fiscal-year revenue and Draup-estimated IT spend with growth (USD at Draup's rate), plus Draup's forecast.
3. Priorities dated in [Review period] (10 at a time), with function and workloads; if none, the 3 most recent, marked as earlier.
4. Leadership: director-plus moves in [Review period], one step-3 workload per pull; keep only people whose current or previous employer is [Company]; state the latest move date.
5. Hiring: monthly postings in [Review period] versus the same-length period before; top 5 workloads trending up.
6. News in [Review period] where [Company] is the actor: deals, expansion, M&A, layoffs, launches; skip stock chatter and look-alikes.

OUTPUT
- Bottom line: 2 sentences — the biggest change and what it means for renewal or expansion.
- "What changed": Financials, Priorities, Leadership (Name | Move | Full title | Month), Hiring, News (Date | Headline | Why it matters).
- "3 talking points": each links a change to [Outcomes we delivered].
- "3 asks": expansion (tied to a priority), reference or case study, executive sponsor.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Hiring, technology and news cover 12 months at most; if [Review period] is older, say what was covered.
- If a forecast moves over 15% from the latest actual, call it a model estimate.
- Fiscal labels can run ahead of the calendar. Check for a divestment before calling a drop a cut.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Use professional information only (name, title, employer, Draup profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Prep my QBR with [Company] for [Review period]: annual financials, new priorities, leadership changes, hiring trend and key news, set against [Outcomes we delivered]. End with 3 talking points and 3 asks.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the talking points and asks into 3 QBR slides: headline, evidence, ask.
```

```text
Run a renewal risk check before the meeting.
```

```text
Which new priority is the best expansion opportunity, and who owns it?
```

## Tips for better results

- Lead with the outcomes you delivered; Draup's outside-in view works best as the bridge to your asks.
- Financials in Draup are annual. Use priorities, leadership, hiring and news for what changed in the quarter.

## Related prompts

- [Renewal risk check (RAG)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer, including your sponsor's status, with dated evidence, an overall rating and two actions.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan in eight parts: snapshot, their strategy in their own words, buying committee, incumbents, ranked expansion plays, risks and a 90-day plan, plus an optional short SWOT.
- [Entry points and whitespace](../../prompts/11-account-planning/entry-points.md): The five best ways into the account for what you sell, each with dated evidence, incumbents and the likely owner.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_forecast_v3`, `get_account_priorities_v3`, `get_account_executive_movement`, `accounts_hiring_timeline_v3`, `accounts_hiring_demand_category_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plan-qbr-prep`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
