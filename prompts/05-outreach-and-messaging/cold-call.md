[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Cold-call opener, talk track, objections

> **A 10-second opener, a 60-second talk track and three objection replies for one named person, each built on a fact-checked public fact or stated priority, plus three discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're about to cold-call a named prospect and want a reason to call that is specific to this account, not a generic pitch. | SDR / BDR, Account Executive | Everyone | 2–4 min | News signals, Priorities & opportunities, Tech stack, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | lowes.com |
| `[Persona]` | VP Supply Chain Planning |
| `[What I sell]` | supply-chain planning software |
| `[Business function (optional)]` | Supply Chain |
| `[Competitor (optional)]` | Blue Yonder |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my cold-calling coach. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. lowes.com]
- Persona: [who you're calling, e.g. VP Supply Chain Planning]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Business function (optional): [the persona's function, e.g. Supply Chain; blank uses the one closest to what I sell]
- Competitor (optional): [company or product, e.g. Blue Yonder]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the account's top-ranked news from the last 90 days and keep the 2 items most relevant to [Business function] where [Company] is the actor. Fact-check each.
3. Pull up to 4 [Business function] priorities with source, quarter and linked tools.
4. If I named a competitor, check the whole stack for products by its maker, whatever area they're filed under: usage strength, last seen and rating.
5. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact. That person is who I call.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Opener (25 words max): who you are, the specific public reason for the call, and a permission question.
- Talk track (150 words max, about 60 seconds): the reason for calling; the problem it creates for someone in [Persona]'s seat, as a question; how [What I sell] helps, in one line; the ask (20 minutes, two time options).
- Objection replies (40 words max each) to "We already have [tool]", "Not a priority right now" and "Just send me an email": acknowledge, use one account fact, end with a question.
- Discovery questions: 3, each tied to a priority.
- Table "Reasons to call" (2 or 3, newest first): Date | Fact | Source | Fact check.
- Detail (prep, not to say): linked tools and competitor products with rating; Gaps (what Draup lacked, to ask in discovery).

RULES
- Never name an installed tool unless it appears in public job ads or announcements, claim to know internal plans, or invent peer statistics.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Rating: an installed competitor product with High usage in the workloads of What I sell is Red, Medium is Amber, else Green. Newly detected (first seen within 12 months) is a separate Amber signal.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (who to call, named, and why today). From 2 confirmed public facts and [Company]'s priorities, write a 25-word opener, a 150-word talk track, three objection replies and three discovery questions for a [Persona].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write the voicemail I leave if they don't pick up, and a matching follow-up email.
```

```text
Give me two more objection replies: "We're mid-contract" and "Talk to procurement".
```

```text
Rewrite the talk track for a services seller offering a managed service.
```

```text
Who should I call second if this person doesn't pick up?
```

## Tips for better results

- Lead with the newest confirmed fact; anything older than a quarter sounds like research, not a reason to call.
- If the company reports on a fiscal year that runs ahead of the calendar, say "on your latest earnings call" rather than naming a quarter.

## Related prompts

- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Voicemail script plus follow-up email](../../prompts/05-outreach-and-messaging/voicemail.md): A 25-second voicemail for a named person built on one confirmed public fact, the matching same-day follow-up email, and a shorter second voicemail for day 4.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_top_signals`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-cold-call`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
