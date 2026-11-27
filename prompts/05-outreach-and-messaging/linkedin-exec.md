[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# LinkedIn note and InMail to an executive

> **A confirmed profile for one named executive, a 300-character connection note with no pitch, a 110-word InMail tied to a stated priority in their remit, and a short message for after they accept.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have one senior person to reach on LinkedIn and want a note that gets accepted and an InMail that gets read. | SDR / BDR, Account Executive, Account & Customer Success Manager, Partnerships & Alliances | Everyone | 2–4 min | Executives & movement, Priorities & opportunities, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | cisco.com |
| `[Executive]` | Global Head of Enterprise Applications, IT |
| `[What I sell]` | AI-assisted quoting software |
| `[Business function (optional)]` | IT |
| `[Shared ground (optional)]` | we both spoke at the same industry event |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my social-selling copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. cisco.com]
- Executive: [name and/or title, e.g. Global Head of Enterprise Applications, IT]
- What I sell: [one line, e.g. AI-assisted quoting software — skip if you ran the start-here prompt]
- Business function (optional): [e.g. IT; blank uses the one closest to what I sell]
- Shared ground (optional): [a real, permitted connection, e.g. we both spoke at the same industry event]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Find the executive: pull key executives in [Business function], 10 per page, up to 3 pages, and match by name or full profile title. If not found, say so first, show the 5 closest titles and ask which to use. Record full title, location, function and workloads.
3. Pull up to 6 [Business function] priorities, newest quarter first, and keep the one closest to the executive's remit.
4. Pull the account's top-ranked news from the last 90 days where [Company] is the actor and keep one item that touches the remit, if any. Fact-check it.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): single-source or disputed facts the copy leans on and any "verify" profile, with what to check; or "none".
- Connection note: 300 characters max including spaces, no pitch, no link; mention [Shared ground] only if I gave it.
- InMail: subject (6 words max), body (110 words max): the priority or news as context; a question about their remit; one line on [What I sell]; one ask.
- After they accept (60 words max): thanks in a few words, one useful resource, no meeting ask.
- Table "Who": Name | Full title | Location | Workloads | Pages checked.
- Detail: the hook (priority in Draup's words, source, quarter; news item, date, source); Gaps (to ask in discovery).

RULES
- Never mention tenure, schools, past employers, skills or anything else from the profile unless it is [Shared ground].
- If the person can't be found, don't write to a guessed person; ask me.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources, never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function (in banking and consulting, VP and SVP are mid-level); flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 380 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first. Find [Executive] at [Company], confirm the full title, match a stated priority and a confirmed 90-day news item, then write a 300-character note, a 110-word InMail and a 60-word post-accept message.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a second InMail for day 7 on a different priority.
```

```text
Draft a comment I could leave on a company post about this priority.
```

```text
Find two peers of [Executive] in the same function for a parallel thread.
```

```text
Turn the InMail into a 70-word email for the same person.
```

## Tips for better results

- Draup has no name search for executives, so give the full title as well as the name; it makes the match much faster.
- Notes with no pitch are often accepted more readily; save the ask for the InMail or the post-accept message.

## Related prompts

- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A short profile of one senior person, found by name or just by title, with time in role, past companies, what they likely own, a competitor check and two openers. If Draup has no one with that title, you're told so up front and given the 3 closest people.
- [Email a newly appointed executive](../../prompts/05-outreach-and-messaging/new-executive.md): The newest senior appointments in your area at one account, checked against a second source, the stated priority that fits the new remit, and a 90-word first-90-days email plus a short follow-up.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [ABM openers for 10 accounts at once](../../prompts/16-content-and-enablement/abm-messages.md): A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `outreach-linkedin-exec`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
