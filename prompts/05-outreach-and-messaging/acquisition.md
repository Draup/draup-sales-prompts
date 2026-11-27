[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email after an acquisition

> **The account's recent deals sorted by type and status and fact-checked, the integration work it has described in its own words, and a 100-word email to a named reader aimed at that integration problem.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account has just closed or announced an acquisition and you want to reach the people who now have to merge systems, suppliers or teams. | Account Executive, SDR / BDR, Services, SI & Staffing Seller | Everyone | 2–4 min | News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | novartis.com |
| `[Persona]` | Head of R&D IT |
| `[What I sell]` | clinical data integration services |
| `[Acquired company (optional)]` | a deal you already know about |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for post-merger integration. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. novartis.com]
- Persona: [who reads it, e.g. Head of R&D IT]
- What I sell: [one line, e.g. clinical data integration services — skip if you ran the start-here prompt]
- Acquired company (optional): [a deal you already know about]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull acquisitions from the last 12 months and remove duplicates.
3. Pull 6 months of M&A news, newest first, 10 items. Keep deals where [Company] or a labelled subsidiary is the buyer; separate company acquisitions from licence or trademark purchases; mark each announced or closed; check the target name matches the text. Fact-check size and close date.
4. Pull up to 5 priorities whose names mention integration (if fewer than 2, also try "acqui"), with function, source, quarter and linked tools and providers.
5. Choose the newest closed acquisition with an integration priority near [Persona]'s area (or the one I named, if it qualifies).
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (100 words max): the deal and close date; the integration task as a question; one concrete offer (a day-100 checklist, a teardown of similar integrations); one ask.
- Variant (60 words max) for a leader on the acquired side, only if that company is in Draup.
- Table "Deals" (newest first): Date | Target | Type | Status | Fact check.
- Table "Integration work they've described": Priority (Draup's words) | Function | Quarter | Likely owner.
- Detail: size, buyer (group or subsidiary) and source per deal; linked tools or providers; Gaps (what Draup lacked, to ask in discovery).

RULES
- Never mention write-downs, impairments, failed trials, job cuts or share price in the copy.
- A licence, asset or trademark purchase is not a company integration; use it only if it creates the work I sell.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- The acquisitions table can miss deals; if news or priorities name one it lacks, check 12 months of M&A news. Say tools are "linked" to a priority, never "used for".
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named reader, a dated deal). List [Company]'s acquisitions from 12 months, fact-check size and close date, find priorities that mention integration, and write a 100-word email to a [Persona] about the integration work.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Find the leaders on the acquired side who are still in Draup, with titles.
```

```text
Write a second touch for day 7 on the supplier or data side of the same integration.
```

```text
Which service providers are linked to the integration priority? Who should I partner with or displace?
```

```text
Find a second source for the deal size so I can quote it.
```

## Tips for better results

- Deals between 3 and 12 months past close are often the sweet spot: the plan exists, the work is still open.
- Large acquirers also buy rights and trademarks; those rarely create systems integration work.
- If the acquisitions table looks thin, the news step usually finds the missing deal.

## Related prompts

- [Openings from their recent acquisitions](../../prompts/01-account-research/acquisitions.md): The top 3 integration openings from the account's acquisitions in the last 3 years, who likely owns each, and an optional read of its strategic investments.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Emails to three buyers at one account](../../prompts/05-outreach-and-messaging/multithread.md): A thread map for one account (economic buyer, technical buyer and champion), each named from Draup and tied to a different stated priority, with two fact-checked emails per person and a staggered send plan.
- [Peers' outsourcing deals for social proof](../../prompts/10-outsourcing-and-services/peer-deals.md): Recent outsourcing engagements at the prospect's peers in the work you sell, ready-to-use proof lines, and who to send them to and why now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_partnerships_mergers_v3`, `get_news_feed_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-acquisition`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
