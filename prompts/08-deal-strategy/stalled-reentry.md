[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Re-open a stalled deal

> **A reopen, wait or walk-away verdict on a stalled deal, tested against why it stalled, with the named person to call, the dated change that justifies it and a 90-word re-entry email.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A live opportunity has gone quiet for 60+ days, or a prospect said "not now". Use this to restart a stalled or lost deal; use "What changed since [Date]" instead for a routine check on a current customer. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 4–6 min | Priorities & opportunities, Executives & movement, News signals, Hiring & job postings, Company & financials, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | starbucks.com |
| `[Stalled since]` | 2026-05-15 |
| `[Why it stalled]` | budget freeze (or: champion left, priority shifted, lost to competitor, no decision) |
| `[Last contact]` | Jane Doe, VP Supply Chain Systems (optional) |
| `[Competitor]` | Blue Yonder (optional) |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal-rescue strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- Stalled since: [e.g. 2026-05-15]
- Why it stalled: [budget freeze, champion left, priority shifted, lost to competitor or no decision]
- Last contact (optional): [e.g. Jane Doe, VP Supply Chain Systems]
- Competitor (optional): [e.g. Blue Yonder]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Re-enter only on a dated buyer-side change that moved the blocker; otherwise wait.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell]; say which.
3. Test the stall reason. Budget freeze: latest revenue and EBITDA growth. Champion left: look for [Last contact] in 2 pages of the function's executives. Priority shifted: up to 10 function priorities, noting those after [Stalled since]. Lost to competitor: check the whole stack for [Competitor] products (engagements, for a services firm). No decision: run all four lightly.
4. People: the 3 most senior function executives by title, plus anyone under 1 year in title.
5. News since [Stalled since] (up to 12 months; say if it's older): investments, executive moves, vendor selections, layoffs; 20+ items, marking the most important from the last 90 days.
6. Hiring: average monthly function postings, 5 full months before [Stalled since] vs the 5 latest.
7. Pick the re-entry angle: a dated change tied to a priority.

OUTPUT
- Bottom line: 2 sentences — Reopen now, Wait until [event or date] or Walk away, with the deciding fact.
- Recommended next step: a named person (name, full title), the action this week and the dated why-now (or say none).
- Table "Stall reason test": Reason | Still true? (Yes, Weaker, Gone, Not in Draup) | Evidence + date.
- Table "What changed" (up to 6, newest first): Date | Type | What changed | Why it matters.
- "Re-entry email": 90 words max: the dated change, one line of history, one low-friction ask.
- Detail: who to re-engage (Name | Full title | In role since) and hiring.
- Gaps: what Draup lacked; ask in discovery.

RULES
- A reason is "Gone" only with a dated fact after [Stalled since].
- Rate [Competitor]: Red if a product has High usage in my workloads or a services rival holds 30%+ of active engagements there (reopen only on a new trigger); Amber if Medium, new or 10–29%; else Green.
- Falling hiring plus rising investment usually means automation or outsourcing, not a freeze.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
My deal at [Company] stalled on [Stalled since] because [Why it stalled]. Lead with reopen, wait or walk away, then the named person to call and the dated change since. Add the stall-reason test and a 90-word re-entry email.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 3-touch re-engagement sequence (email, call script, LinkedIn note) around the re-entry angle.
```

```text
Profile the newest leader in that function and suggest two openers.
```

```text
Run the renewal-style risk check on this account before I commit time to it.
```

## Tips for better results

- Be honest about why it stalled. The prompt tests that reason first, which is what makes the re-entry credible.
- A new leader in the buying function is often the best re-entry: they have no history with the old "no".
- If the verdict is Wait, put the named event in your calendar and re-run the prompt then.

## Related prompts

- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.
- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [Pick a realistic signature window](../../prompts/08-deal-strategy/budget-timing.md): Whether your close date fits the buyer's fiscal calendar and budget posture, the events that move money in the next two quarters, the best 4–8 week signature window and the named person to confirm it with.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `get_signal_news_v3`, `accounts_hiring_timeline_v3`

Status: **tested live**. Prompt id: `deals-stalled-reentry`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
