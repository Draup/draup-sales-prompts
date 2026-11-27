# What changed since [Date]

**A dated log of everything material that changed at an account since a date you choose, ranked by impact on your deal.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Revisiting a closed-lost deal, prepping a renewal or QBR, or picking up an account from a colleague. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 4–6 min | Executives & movement, Tech stack, Hiring & job postings, Priorities & opportunities, News signals, Company & financials |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Date]` | 2026-03-01 |
| `[Business function]` | Supply Chain |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my account-intelligence analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. walmart.com]
- Date: [starting point, e.g. 2026-03-01, when we lost the deal or held the last QBR]
- Business function: [e.g. Supply Chain, IT]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Priorities: stated priorities in [Business function] sourced after [Date], with fiscal quarter; note the 2–3 workloads behind them.
3. Leadership: hires, exits and promotions since [Date], one workload at a time, narrowest first. If a workload returns too much to read, say so and use executive-movement news instead. Use full titles, not seniority labels; say how many rows you checked.
4. Technology: products first detected since [Date] that touch the function or [What I sell], and any product by a competitor I named in setup, anywhere in the stack.
5. Hiring: average monthly postings in [Business function] before versus after [Date], full months only (postings are openings, not hires).
6. News since [Date]: executive moves, M&A, partnerships, expansion, layoffs, investment plans.
7. Financials: any new fiscal year: revenue and Draup-estimated IT spend, with growth. Before calling a drop over 5% a cut, check for a divestment or restatement.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Top 5 changes that matter": one line each, ranked by impact, with date.
- Table "Change log" (newest first): Date | Type (Leadership, Technology, Hiring, Priority, News, Financials) | What changed | Source | Impact (High, Medium, Low) | Likely owner.
- The next step also says reopen, wait or watch.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Technology, hiring and news reach back 12 months at most; if [Date] is older, cover the last 12 months and say so.
- "First detected" means Draup first saw evidence, not a contract date.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Draup shows about the 10 most recent moves per type, so narrow by workload, and state the latest move date in the data. Keep only rows where [Company] is the current employer (for exits, the previous one).
- Use professional information only: name, title, employer and the profile link Draup gives. No personal contact details.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 380 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
What changed at [Company] since [Date] that matters for [What I sell] in [Business function]? Leadership moves, new tools, hiring shifts, new priorities, news and new financials, in one dated table ranked by impact.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a re-engagement email to the new leader in [Business function], tied to the top change.
```

```text
Has any competitor product been first detected since [Date]?
```

```text
Turn this into a 5-bullet update for my manager.
```

## Tips for better results

- For a closed-lost revisit, use the date you lost. For renewals, use the date of the last QBR.
- A new leader in the function plus a new priority is a classic reopen signal.

## Related prompts

- [QBR prep](../../prompts/08-account-planning-and-expansion/qbr-prep.md): What changed at the customer during the review period, set against the outcomes you delivered, with three talking points and three asks.
- [Renewal risk check (RAG)](../../prompts/08-account-planning-and-expansion/risk-check.md): A Red/Amber/Green risk table for one customer, including your sponsor's status, with dated evidence, an overall rating and two actions.
- [Weekly trigger sweep for my book](../../prompts/04-signals-and-timing/weekly-book-sweep.md): One table of the week's real triggers across up to 10 accounts, each with a so-what and an action, plus a clean list of accounts with nothing new.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_account_executive_movement`, `get_tech_stack_trend_v3`, `accounts_hiring_timeline_v3`, `get_news_feed_v3`, `get_account_financials_v3`

Status: **tested live**. Prompt id: `signals-change-log`.

</details>

[Back to Signals and timing](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
