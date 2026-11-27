[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email during cost cuts or restructuring

> **A private read of the account's cost pressure and restructuring news, a sensitivity rating, and a careful 90-word email built on the company's own stated savings goal, with a softer alternative and a named reader.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account is cutting costs, closing sites or restructuring, and you sell something that pays back fast but need to approach without seeming to profit from people's bad news. | Account Executive, SDR / BDR, Account & Customer Success Manager, Services, SI & Staffing Seller | Everyone | 2–4 min | Company & financials, News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | nestle.com |
| `[Persona]` | VP Procurement |
| `[What I sell]` | spend analytics software |
| `[Region (optional)]` | Europe |
| `[Proof point (optional)]` | found savings in indirect spend for Fabrikam Foods |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for accounts under cost pressure. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. nestle.com]
- Persona: [who reads it, e.g. VP Procurement]
- What I sell: [one line, e.g. spend analytics software — skip if you ran the start-here prompt]
- Region (optional): [e.g. Europe]
- Proof point (optional): [a result I may quote, e.g. found savings in indirect spend for Fabrikam Foods]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the latest financial snapshot: revenue and EBITDA, year-on-year growth, fiscal year.
3. Pull 6 months of layoff and restructuring news, newest first, 10 items (in [Region] if given): date, event, location, function affected; label subsidiaries.
4. Pull up to 4 priorities whose names mention cost (if under 2, try "efficien" and "productivity"), with function, source and quarter.
5. Rate sensitivity: High if cuts hit [Persona]'s own function or region in the last 90 days, Medium if another function in the same region, otherwise Low.
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for. For High sensitivity, suggest waiting 2 to 4 weeks.
- Sensitivity: High, Medium or Low, with a one-line reason.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max, no "cost-cutting" or "tough times") and body (90 words max): their goal in their words; a question on where the next savings must come from; a low-risk offer framed around payback (a two-week diagnostic, a fixed-scope pilot); one ask.
- Softer alternative (50 words max): no meeting ask, one resource.
- Table "Their stated savings goals": Priority (Draup's words) | Function | Quarter | Likely owner.
- Detail (for me, never for the copy): Metric | Fiscal year | Value | Year-on-year; what's happening (Date | Event | Location | Function | Source); Gaps (what Draup lacked, to ask in discovery).

RULES
- Never mention job cuts, closures, sites, union talks, people affected, "turnaround" or falling results in the copy. Claim no savings figure beyond [Proof point]. If the cuts hit [Persona]'s own team, also draft for an adjacent function.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Financials come in the reporting currency, in millions, with Draup's conversion rate; convert to US dollars only when comparing or when I ask.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named reader). For [Company], show revenue growth, 6 months of restructuring news and stated cost priorities; rate sensitivity; write a 90-word [Persona] email on their own savings goal, never mentioning cuts.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Rewrite the email for the CFO, tied to the cash or margin priority.
```

```text
Which functions are still hiring despite the cuts? Show the top 5 with trends.
```

```text
Draft a 3-touch sequence over 3 weeks that never mentions the restructuring.
```

```text
Is anyone new leading [Persona]'s function since the restructuring began?
```

## Tips for better results

- The company's own words (from an earnings call) are the safest hook: you're echoing their goal, not their pain.
- If the persona's team was just cut, a short resource with no meeting ask often lands better than a pitch.

## Related prompts

- [Spot scale-up and cost-out buyers](../../prompts/06-prospecting-and-lists/growth-and-cost-out.md): Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and a named person to call first.
- [Do layoffs open an outsourcing deal?](../../prompts/17-talent-cost-and-location/layoff-pool.md): Where and in which roles a company has cut jobs in the last 12 months, read as a possible outsourcing trigger, plus which skills are now more available in the market.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Re-engage a stalled or ghosted account](../../prompts/05-outreach-and-messaging/reengage.md): A dated, fact-checked list of what changed since your last contact, a reopen-or-wait call, a re-engagement email built on the change, a polite break-up email, and a version for a new person if one appeared.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_news_feed_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-restructuring`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
