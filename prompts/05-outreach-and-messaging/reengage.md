[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Re-engage a stalled or ghosted account

> **A dated, fact-checked list of what changed since your last contact, a reopen-or-wait call, a re-engagement email built on the change, a polite break-up email, and a version for a new person if one appeared.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A deal or conversation went quiet weeks or months ago and you want a reason to re-open that isn't "just checking in". For a fuller account review, use "What changed since [Date]". | Account Executive, Account & Customer Success Manager, SDR / BDR | Everyone | 2–4 min | News signals, Priorities & opportunities, Hiring & job postings, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Last contact date]` | 2026-06-01 |
| `[What we discussed]` | an AI pilot for R&D data |
| `[Contact title]` | Head of R&D Data |
| `[What I sell]` | AI data platform services |
| `[Workload or function (optional)]` | Artificial Intelligence & Data Science |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal re-engagement strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. pfizer.com]
- Last contact date: [e.g. 2026-06-01]
- What we discussed: [one line, e.g. an AI pilot for R&D data]
- Contact title: [the person who went quiet, e.g. Head of R&D Data]
- What I sell: [one line, e.g. AI data platform services — skip if you ran the start-here prompt]
- Workload or function (optional): [e.g. Artificial Intelligence & Data Science; blank uses the one closest to what I sell]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull news since [Last contact date], newest first, 10 items: executive moves, M&A, partnerships, expansion, layoffs. Flag leadership changes in or above [Contact title]'s area. Fact-check each.
3. Pull up to 3 priorities in [Workload or function]; mark those sourced after [Last contact date].
4. Compare average monthly postings in [Workload or function], full months before vs after [Last contact date].
5. Pull the top 3 executives in the function now and check whether [Contact title] is still there.
6. Pick the one or two changes most relevant to [What we discussed] and decide: Reopen now (a change touches the topic), Reopen via new person (a new leader owns it), or Wait (nothing material; set a date).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Start with the verdict and one dated reason.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Re-engagement email: subject (6 words max) and body (90 words max): the change; one clause recalling [What we discussed]; a question on whether it changes their thinking; one small ask.
- Break-up email (60 words max): a polite close that asks permission ("shall I close this out for now?").
- New-person version (70 words max), only if a new leader appeared.
- Table "What changed" (newest first): Date | Change | Type | Relevance | Fact check.
- Detail: sources; hiring before and after; Gaps (what Draup lacked, to ask in discovery).

RULES
- No guilt or pressure: never "I've tried several times", "just checking in" or "did you get my email".
- Pose hiring shifts as a question, never a claim, and without counts.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Hiring, new-technology and news data cover the last 12 months; if my date is older, cover the last 12 months and say so.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line first (reopen now, reopen via a new person, or wait) and the next step with a named person. List confirmed changes at [Company] since [Last contact date], then write a 90-word re-engagement email and a 60-word break-up email.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a LinkedIn message for the new leader instead of an email.
```

```text
If they reply "not now", draft a 2-line response and a reminder for 90 days.
```

```text
Run the same check for my other stalled accounts: [websites].
```

```text
Find a second source for the top change so I can name it in the email.
```

## Tips for better results

- The break-up email works best after one re-engagement attempt; send it about a week later.
- A new leader in the buyer's chain is often the strongest reason to reopen, and a reason to write to both people.

## Related prompts

- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.
- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [Email during cost cuts or restructuring](../../prompts/05-outreach-and-messaging/restructuring.md): A private read of the account's cost pressure and restructuring news, a sensitivity rating, and a careful 90-word email built on the company's own stated savings goal, with a softer alternative and a named reader.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `get_account_priorities_v3`, `accounts_hiring_timeline_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-reengage`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
