[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What changed since [Date]

> **A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Revisiting a closed-lost deal, prepping a renewal or QBR, or picking up an account from a colleague. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 4–6 min | Executives & movement, Tech stack, Hiring & job postings, Priorities & opportunities, News signals, Company & financials |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Date]` | 2026-03-01 |
| `[Relationship]` | current customer (or lost deal) |
| `[What I sell]` | supply-chain planning software |
| `[Business function (optional)]` | Supply Chain |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. walmart.com]
- Date: [e.g. 2026-03-01: when we lost the deal or held the last QBR]
- Relationship: [current customer or lost deal]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Supply Chain, IT; blank uses the function closest to what I sell]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Priorities: function priorities sourced after [Date], with fiscal quarter and workloads.
3. Leadership: hires, exits and promotions since [Date], one workload at a time, with full titles, rows checked and latest move date; then the top 3 executives in the function now.
4. Technology: products first detected since [Date] in the function, and any competitor product anywhere in the stack; rate each (see rules).
5. Hiring: average monthly postings in the function before vs after [Date], full months only.
6. News since [Date]: executive moves, M&A, partnerships, expansion, layoffs, investment plans, and incidents bearing on what I sell.
7. Financials: any new fiscal year's revenue growth; check for a divestment before calling a drop a cut.

OUTPUT
- Bottom line: 2 sentences, starting with the call (lost deal: reopen, wait or watch; current customer: defend, expand or monitor) and the top change.
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- Table "Change log" (highest impact first, up to 10 rows, then offer more): Date | Type | What changed | Impact | Likely owner.
- Detail: sources; competitor ratings; hiring before and after; Gaps (to ask in discovery).

RULES
- Technology, hiring and news cover 12 months; if [Date] is older, say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the function closest to What I sell (e.g. IT) and say which; map any function I give to its main workloads and name them.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Leadership moves show about the 10 latest per type and lag about 3 months; keep rows where [Company] is the current employer (previous, for exits).
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and re-dated old stories (use the event date). Outages, incidents, breaches and regulatory inquiries count for security, reliability, IT operations or compliance sellers; keep any item that bears directly on What I sell. Give source, headline and link (if any) per item.
- If sources conflict on a name, date or number, say so and repeat neither as fact; single-source figures are unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Rating: count a rival only at High or Medium usage (ignore Low or very-low-confidence detections; say so). High in my workloads is Red, Medium Amber, none Green; newly detected (first seen in 12 months) is a separate Amber signal.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line first (customer: defend, expand or monitor; lost deal: reopen, wait or watch) and next step with a named person. Then up to 10 dated changes at [Company] since [Date] that matter for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a re-engagement email to the new leader in the function, tied to the top change.
```

```text
Has any competitor product been first detected since [Date]? Show usage strength and countries.
```

```text
Turn this into a 5-bullet update for my manager.
```

```text
Compare this with the risk check for the same account.
```

## Tips for better results

- For a closed-lost revisit, use the date you lost. For renewals, use the date of the last QBR.
- A competitor tool rated Red in your workloads is the first thing to raise at a renewal; Amber means ask about it in discovery.
- Leadership data can lag about 3 months; the latest move date tells you how fresh it is.

## Related prompts

- [QBR prep: talking points and asks](../../prompts/11-account-planning/qbr-prep.md): Three talking points and three asks for your business review, built on what changed at the customer in your sponsor's function, set against the outcomes you delivered.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [Weekly trigger sweep for my book](../../prompts/04-signals-and-timing/weekly-book-sweep.md): One phone-sized table of the week's real triggers across up to 10 accounts, including any CEO or leadership change that takes effect in the window, plus the nearest item just outside the window for every quiet account.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_account_executive_movement`, `accounts_executives_key_executives_v3`, `get_tech_stack_trend_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_timeline_v3`, `get_news_feed_v3`, `get_account_financials_v3`

Status: **tested live**. Prompt id: `signals-change-log`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
