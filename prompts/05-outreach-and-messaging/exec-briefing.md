[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# One-page brief before a C-level meeting

> **A one-page, send-ahead briefing note for a C-level meeting (what you understand they're working on, what you'll bring, a 30-minute agenda and two questions), built only on confirmed facts, with a cover email and a private prep sheet of sensitivities.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a meeting booked with a C-level executive and want to send a short note 24 to 48 hours ahead that shows you've done the work. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 2–4 min | Company & financials, News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | unilever.com |
| `[Executive title]` | Chief Digital and Marketing Officer |
| `[Meeting purpose]` | first meeting on creator-marketing measurement |
| `[What I sell]` | marketing mix and attribution analytics |
| `[Business function (optional)]` | Sales & Marketing |
| `[Proof point (optional)]` | improved media ROI for Contoso Retail |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my executive-briefing writer. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- Executive title: [e.g. Chief Digital and Marketing Officer]
- Meeting purpose: [one line, e.g. first meeting on creator-marketing measurement]
- What I sell: [one line, e.g. marketing mix and attribution analytics — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Sales & Marketing; blank uses the executive's function]
- Proof point (optional): [a result I may quote, e.g. improved media ROI for Contoso Retail]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the latest financial snapshot: revenue and EBITDA with year-on-year growth and fiscal year.
3. Pull news about [Company] for the last 90 days, newest first, 8 items: deals, executive moves, M&A, investment, expansion, layoffs. Check each item's content matches its category; set aside divestments, cuts and disputes as sensitivities. Fact-check the rest.
4. Pull up to 4 [Business function] priorities, newest quarter first.
5. Pull the top 3 executives in the function and confirm who holds [Executive title] (full profile title).
6. Choose the 3 Confirmed points most relevant to [Meeting purpose] and build the note.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Briefing note (350 words max), ready to send: title line; "Why we're meeting" (1 sentence); "What we understand you're working on" (3 bullets, each with a public source and date); "What we'll bring" (3 bullets, no claims beyond [Proof point]); "Proposed agenda" (30 minutes, 3 items with minutes); "Two questions we'd value your view on".
- Cover email: 60 words max, one ask (confirm the agenda or add to it).
- Detail (prep sheet, not to send): Metric | Fiscal year | Value | Year-on-year; recent news with dates and sources; "Don't raise unless they do" (sensitive items) and why; Gaps (what Draup lacked, to ask in discovery).

RULES
- Use financials only as private context; never describe results as weak or declining in the note.
- Quote priorities in the company's own words where possible; don't present Draup's summaries as their quotes.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Financials come in the reporting currency, in millions, with Draup's conversion rate; convert to US dollars only when comparing or when I ask.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 500 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first. Build a send-ahead one-page note for a [Executive title] at [Company]: 3 confirmed, dated things they're working on, what we'll bring, a 30-minute agenda, two questions, a 60-word cover email and private sensitivities.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the note into a 3-slide opening deck for the meeting.
```

```text
Write the follow-up email I'll send after the meeting, leaving blanks for what they said.
```

```text
Add a short section on what two peers are doing on the same priority.
```

```text
Who else from their team should I invite, by name and title?
```

## Tips for better results

- Send the note 24 to 48 hours ahead; it often gets forwarded to the people the executive wants in the room.
- Keep the sensitivities list handy: a divestment or reorganisation is often on the executive's mind even if it's not on your agenda.

## Related prompts

- [Brief for a C-level pursuit meeting](../../prompts/11-account-planning/cxo-pursuit-brief.md): A one-page pursuit brief for a C-level meeting: the 3 workloads to lead with, the buyers, incumbents, a Go or Not-yet evidence check, what to learn in meeting 1 and a 90-day plan.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.
- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_news_feed_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-exec-briefing`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
