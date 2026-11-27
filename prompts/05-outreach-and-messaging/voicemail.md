[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Voicemail script plus follow-up email

> **A 25-second voicemail for a named person built on one confirmed public fact, the matching same-day follow-up email, and a shorter second voicemail for day 4.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You call senior buyers who rarely pick up and want the voicemail and email to work as one touch. | SDR / BDR, Account Executive | Everyone | 1–2 min | News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Persona]` | VP Store Operations |
| `[What I sell]` | workforce scheduling software |
| `[Me]` | [Your name], Northwind Data Services |
| `[Priority theme (optional)]` | store teams |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my phone-outreach copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Persona: [who you're calling, e.g. VP Store Operations]
- What I sell: [one line, e.g. workforce scheduling software — skip if you ran the start-here prompt]
- Me: [your name and firm, e.g. [Your name], Northwind Data Services]
- Priority theme (optional): [a word or two to find the right priority, e.g. store teams]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull news about [Company] for the last 60 days, newest first, 8 items: deals and partnerships, executive moves, expansion, M&A, investment plans and layoffs. Keep items where [Company] is the actor; drop items where its name is an ordinary word or belongs to another firm. Fact-check each.
3. Pull up to 3 priorities whose names match [Priority theme]; if none (or no theme), take the 3 newest in the persona's function.
4. Pick one Confirmed fact and one priority that connect.
5. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Voicemail 1 (60 words max, about 25 seconds): name and firm; the fact; one question tied to the priority; callback ask; "I'll send a short note too"; name and number said slowly at the end as [phone].
- Follow-up email (same day): subject (6 words max) and body (80 words max): one line referencing the voicemail; the same fact; the question; one ask with a yes-or-no reply option.
- Voicemail 2 (day 4, 40 words max): a different fact or priority, same callback ask.
- Table "Facts used": Date | Fact | Source | Fact check.
- Detail: priority used (Draup's words, source, quarter); Gaps (what Draup lacked, to ask in discovery).

RULES
- Spell out numbers the way you'd say them ("five to six billion") in the scripts.
- Never leave pricing, competitor names or anything confidential on a voicemail.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 380 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (who to call, named, and why now). From one confirmed 60-day fact and one [Company] priority, write a 60-word voicemail, an 80-word follow-up email and a 40-word day-4 voicemail for a [Persona].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 3-touch call-email-call cadence for the next 10 days.
```

```text
Rewrite voicemail 1 for the persona's boss.
```

```text
Give me a 15-second version for a mobile number.
```

```text
Swap in a different confirmed fact for voicemail 2.
```

## Tips for better results

- Read the script aloud once; if it runs past 30 seconds, cut the value line, not the fact.
- Common words in company names can pull in unrelated news; the actor check in step 2 catches most of it.

## Related prompts

- [Cold-call opener, talk track, objections](../../prompts/05-outreach-and-messaging/cold-call.md): A 10-second opener, a 60-second talk track and three objection replies for one named person, each built on a fact-checked public fact or stated priority, plus three discovery questions.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-voicemail`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
