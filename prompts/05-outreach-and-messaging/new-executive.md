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
- Function or area: [e.g. Sales & Marketing]
- What I sell: [one line, e.g. loyalty personalisation software — skip if you ran the start-here prompt]
- Executive (optional): [name or role, e.g. the new head of loyalty]
- Proof point (optional): [e.g. lifted repeat bookings for Contoso Retail]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Pull 6 months of executive-movement news, newest first, 15 items. Keep corporate VP-and-above appointments in or near [Function]; drop single-site appointments (one hotel, store or plant) and board seats. Fact-check each name, title and start date. If I named an executive, find them first.
3. Pull key executives in [Function], 10 per page, up to 2 pages; flag anyone under 12 months in title as "new in role". If an appointee has no profile, say "profile not found" and rely on the announcement.
4. Rank up to 5 candidates by recency, seniority, fit and fact check; pick one.
5. Pull up to 8 [Function] priorities, newest quarter first, and choose the one closest to the new remit.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): single-source or disputed facts the copy leans on and any "verify" profile, with what to check; or "none".
- Email: subject (6 words max), body (90 words max): the announced remit, no congratulation clichés; the priority as a question about their first 90 days; one concrete offer; a 20-minute ask. [Proof point] only if given.
- Follow-up (day 5): 50 words max, a second fact, same ask.
- Table "New leaders" (up to 5, newest first): Date | Name | New title | Fact check | Source.
- Detail: the angle (person and priority in Draup's words, source, quarter); Gaps (to ask in discovery).

RULES
- Reference only what was announced (role, remit, start date); never time in role or career history.
- No qualifying appointment in 6 months: say so in the Bottom line's first sentence, then write to the best "new in role" profile on a priority, labelled "Built on a priority, not an announcement". Never imply newness or stretch older moves.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources, never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: [Company] must be the actor; drop look-alikes, sister companies, passing mentions and re-dated stories. Give source and headline.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first. Find the newest VP-and-above appointment in [Function] at [Company] in 6 months, fact-check it, match a priority, and write a 90-word email and follow-up. None? Say so, then write on a priority.
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
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A short profile of one senior person, found by name or just by title, with time in role, past companies, what they likely own, a competitor check and two openers. If Draup has no one with that title, you're told so up front and given the 3 closest people.
- [LinkedIn note and InMail to an executive](../../prompts/05-outreach-and-messaging/linkedin-exec.md): A confirmed profile for one named executive, a 300-character connection note with no pitch, a 110-word InMail tied to a stated priority in their remit, and a short message for after they accept.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `outreach-new-executive`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
