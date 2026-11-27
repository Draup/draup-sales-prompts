[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email after a new site or centre

> **The account's newest centres, leases and expansions, fact-checked and matched against its location footprint and local hiring, plus a 100-word email and a LinkedIn note aimed at what the site is being staffed for.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account has announced a new office, capability centre (an in-house delivery or tech centre, often called a GCC), hub or expansion, and the vendors for that site are about to be chosen. | Account Executive, SDR / BDR, Services, SI & Staffing Seller, Partnerships & Alliances | Everyone | 4–6 min | News signals, Hiring & job postings, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | hsbc.com |
| `[Persona]` | Head of the India technology centre |
| `[What I sell]` | managed workplace and IT services for new delivery centres |
| `[Business function (optional)]` | IT (default) |
| `[Location (optional)]` | Bengaluru |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for expansion and new-site triggers. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. hsbc.com]
- Persona: [who reads it, e.g. Head of the India technology centre]
- What I sell: [one line, e.g. managed workplace and IT services for new delivery centres — skip if you ran the start-here prompt]
- Business function (optional): [default IT, e.g. IT or ER&D (engineering and R&D)]
- Location (optional): [metro to focus on, e.g. Bengaluru]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull 6 months of centre-setup and expansion news, newest first, 10 items (only [Location] if given). Keep new centres, leases, hubs and capacity growth; drop store openings and partner facilities. Fact-check stated scale. If nothing qualifies, widen to 12 months.
3. Pull the top 8 locations for [Business function]: approximate headcount, 12-month postings, growth index, tags.
4. For the chosen location, pull the top 5 workloads in its postings over 12 months, with trend, and up to 3 [Business function] priorities they support (or say none fits).
5. Pick the announced site with rising postings.
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (100 words max): the announcement and its date; what the site will do (from postings) as a question; one offer tied to standing it up; one ask.
- LinkedIn note: under 300 characters.
- Table "Site signals" (newest first): Date | Location | What was announced | Scale stated | Fact check.
- Table "What they're staffing it for" (top 5): Workload | Postings | Trend | Likely owner.
- Detail: footprint check (Metro | Approx. headcount | Postings | Growth index | Tag); sources; linked priority; Gaps (what Draup lacked, to ask in discovery).

RULES
- Quote announced scale only if Confirmed, as the source states it; never quote Draup headcount in copy.
- A headquarters move is a relocation, not new demand, unless the source says capacity grows. If the site shows no postings, say so and lower confidence.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Site headcount is approximate and centre tags can include plants; lean on postings. A "New Site" tag is inferred from postings.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named reader, a dated announcement). Find [Company]'s new-site news from 6 months, fact-check the scale, check local postings, and write a 100-word email to a [Persona] on what it's staffed for.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who leads [Business function] in [Location]? Show up to 5 people with full titles.
```

```text
Which service providers already deliver from [Location] for this account?
```

```text
Write a version for a facilities or workplace leader instead of [Persona].
```

```text
Find a second source for the stated scale so I can quote it.
```

## Tips for better results

- A lease or opening plus rising local postings is a much stronger trigger than either alone.
- Selling services to capability centres? Run the capability-centre services prompt next for build-operate-transfer and centre-of-excellence angles.

## Related prompts

- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.
- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.
- [Email after a funding or investment](../../prompts/05-outreach-and-messaging/funding.md): A dated, fact-checked read of the account's latest raise or announced investment, where the money is going by function, and a 100-word email plus a LinkedIn note that ties it to one priority.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `accounts_location_insights_key_locations_map_v3`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-new-site`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
