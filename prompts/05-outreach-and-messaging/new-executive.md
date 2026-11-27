[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email a newly appointed executive

> **The newest senior appointments in your area at one account, checked against a second source, the stated priority that fits the new remit, and a 90-word first-90-days email plus a short follow-up.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A leader has just been appointed or promoted at a target account and you want to be the useful email in a crowded inbox, not another congratulations note. | Account Executive, SDR / BDR, Account & Customer Success Manager | Everyone | 2–4 min | Executives & movement, News signals, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | marriott.com |
| `[Function or area]` | Sales & Marketing |
| `[What I sell]` | loyalty personalisation software |
| `[Executive (optional)]` | the new head of loyalty |
| `[Proof point (optional)]` | lifted repeat bookings for Contoso Retail |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for executive transitions. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. marriott.com]
- Function or area: [where the new leader sits, e.g. Sales & Marketing]
- What I sell: [one line, e.g. loyalty personalisation software — skip if you ran the start-here prompt]
- Executive (optional): [name or role if known, e.g. the new head of loyalty]
- Proof point (optional): [a result I may quote, e.g. lifted repeat bookings for Contoso Retail]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull executive-movement news about [Company] for the last 6 months, newest first, 15 items. Keep corporate appointments at VP or above in or near [Function]; drop single-site appointments (one hotel, store or plant) and board seats. If I named an executive, find them first.
3. Fact-check each appointment's name, title and start date.
4. Pull key executives in [Function], 10 per page, up to 2 pages. Flag anyone under 12 months in their current title as "new in role". Use the full profile title; if the person isn't there, write "profile not found" and rely on the announcement.
5. Rank up to 5 candidates by recency, seniority, fit and fact check; pick one.
6. Pull up to 8 [Function] priorities, newest quarter first, and choose the one closest to the new remit.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (90 words max): the announced remit, no congratulation clichés; the priority as a question about their first 90 days; one concrete offer; one ask for 20 minutes. Use [Proof point] only if given.
- Follow-up (day 5): 50 words max, a second fact, same ask.
- Table "New leaders" (up to 5, newest first): Date | Name | New title | Fact check | Source.
- Detail: the angle (person and priority in Draup's words, source, quarter); Gaps (what Draup lacked, to ask in discovery).

RULES
- Reference only what was announced: role, remit, start date. Never mention time in role or career history the announcement didn't state.
- No qualifying appointment in 6 months: say so and offer the "new in role" profiles instead; don't stretch older moves.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (the named new leader, dated). Find the newest VP-and-above appointment in [Function] at [Company] in 6 months, confirm it with a second source, match a priority, and write a 90-word email and 50-word follow-up.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a version for the new leader's own boss, tied to a different priority.
```

```text
Draft a LinkedIn connection note under 300 characters for the same person.
```

```text
Who else joined [Company] in [Function] in the last 6 months? Show the next 5.
```

```text
Find a second source for the appointment so I can name the start date.
```

## Tips for better results

- Big brands announce many site-level appointments (hotel or store managers). Naming a corporate function such as Sales & Marketing keeps those out.
- If the new leader isn't in Draup's executive list yet, the announcement alone is enough; leadership data can lag about 3 months.
- If two outlets disagree on a title or start date, the email leaves it out and the check line tells you what to confirm.

## Related prompts

- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive, two openers tied to the account's current priorities, and a dated reason to reach out now.
- [LinkedIn note and InMail to an executive](../../prompts/05-outreach-and-messaging/linkedin-exec.md): A confirmed profile for one named executive, a 300-character connection note with no pitch, a 110-word InMail tied to a stated priority in their remit, and a short message for after they accept.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `outreach-new-executive`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
