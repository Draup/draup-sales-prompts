# Outreach and messaging

Research-backed emails, call scripts, LinkedIn notes and briefing notes, each grounded in dated Draup facts.

## Email a newly appointed executive

- **id:** `outreach-new-executive`
- **What you get:** The newest senior appointments in your area at one account, checked against a second source, the stated priority that fits the new remit, and a 90-word first-90-days email plus a short follow-up.
- **Use it when:** A leader has just been appointed or promoted at a target account and you want to be the useful email in a crowded inbox, not another congratulations note.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager
- **Time:** 2–4 min
- **Inputs:** Company (e.g. marriott.com); Function or area (e.g. Sales & Marketing); What I sell (e.g. loyalty personalisation software); Executive (optional) (e.g. the new head of loyalty); Proof point (optional) (e.g. lifted repeat bookings for Contoso Retail)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first (the named new leader, dated). Find the newest VP-and-above appointment in [Function] at [Company] in 6 months, confirm it with a second source, match a priority, and write a 90-word email and 50-word follow-up.
```

### Follow-ups

- Write a version for the new leader's own boss, tied to a different priority.
- Draft a LinkedIn connection note under 300 characters for the same person.
- Who else joined [Company] in [Function] in the last 6 months? Show the next 5.
- Find a second source for the appointment so I can name the start date.

### Tips

- Big brands announce many site-level appointments (hotel or store managers). Naming a corporate function such as Sales & Marketing keeps those out.
- If the new leader isn't in Draup's executive list yet, the announcement alone is enough; leadership data can lag about 3 months.
- If two outlets disagree on a title or start date, the email leaves it out and the check line tells you what to confirm.

## Email after a funding or investment

- **id:** `outreach-funding`
- **What you get:** A dated, fact-checked read of the account's latest raise or announced investment, where the money is going by function, and a 100-word email plus a LinkedIn note that ties it to one priority.
- **Use it when:** An account has just raised money or announced a big investment plan (new region, plant, capital programme) and budgets are being set.
- **Best for:** Account Executive, SDR / BDR, Marketing & ABM
- **Time:** 2–4 min
- **Inputs:** Company (e.g. databricks.com); Persona (e.g. VP Engineering); What I sell (e.g. cloud cost management software); Proof point (optional) (e.g. cut cloud spend for Fabrikam Foods)

### Detailed prompt

```text
Act as my outbound copywriter for growth-stage and investing accounts. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. databricks.com]
- Persona: [who reads it, e.g. VP Engineering]
- What I sell: [one line, e.g. cloud cost management software — skip if you ran the start-here prompt]
- Proof point (optional): [a result I may quote, e.g. cut cloud spend for Fabrikam Foods]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on. Note whether it is public or private.
2. Pull funding history: the last 3 rounds (date, USD millions, type, lead investors), or say it has none.
3. Pull 6 months of fundraise-and-investment news, newest first, 10 items. Sort each: Raised, Committed (announced spending), Reported (talks) or Invested in others. Fact-check each amount.
4. Pull 12 months of job postings by function: top 6 with trend, last 5 full months vs the 5 before.
5. Pull up to 6 priorities in [Persona]'s function, newest quarter first, and link the newest Raised or Committed event to the hiring and best-fit priority.
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (100 words max): the event and its date in one clause; the stated use; a question linking it to [Persona]'s priority; one concrete offer; one ask. Use [Proof point] only if given.
- LinkedIn note: 280 characters max.
- Table "Money events" (newest first): Date | Type | Amount | Stated use | Fact check.
- Table "Where it is going" (top 6): Function | Postings (12 months) | Last 5 vs prior 5 | Trend.
- Detail: sources and lead investors; invested-in-others items, one line each; linked priority (source, quarter); Gaps (what Draup lacked, to ask in discovery).

RULES
- Never congratulate or mention valuation; quote an amount only if Confirmed, as the source states it.
- Reported or in-talks items are not closed: never write them as done, and prefer a closed event for the hook. If the only events are investments in other companies, write from hiring and priority instead.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News: [Company] must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated old stories; keep incidents or regulatory items that bear on What I sell. Give source and headline per item.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

### Quick version

```text
Bottom line and next step first (a named reader, a dated event). List [Company]'s funding and investment news from 6 months, fact-check the amounts, show where hiring is rising, and write a 100-word email to a [Persona].
```

### Follow-ups

- Write the same email for the CFO, focused on spending the new money with control.
- Which metros are getting the new hiring? Show the top 5 with postings.
- Draft a second touch for day 6 that uses the hiring trend instead of the funding.
- Find a second source for the amount so I can quote it.

### Tips

- The strongest hook is often the stated use of funds (a new region or team), not the amount.
- Corporate venture arms make many investments in other companies; those rarely mean the account itself has new budget.
- Amounts reported by one outlet, or reported differently by two, stay out of the email until you confirm them.

## Email after an acquisition

- **id:** `outreach-acquisition`
- **What you get:** The account's recent deals sorted by type and status and fact-checked, the integration work it has described in its own words, and a 100-word email to a named reader aimed at that integration problem.
- **Use it when:** An account has just closed or announced an acquisition and you want to reach the people who now have to merge systems, suppliers or teams.
- **Best for:** Account Executive, SDR / BDR, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. novartis.com); Persona (e.g. Head of R&D IT); What I sell (e.g. clinical data integration services); Acquired company (optional) (e.g. a deal you already know about)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first (a named reader, a dated deal). List [Company]'s acquisitions from 12 months, fact-check size and close date, find priorities that mention integration, and write a 100-word email to a [Persona] about the integration work.
```

### Follow-ups

- Find the leaders on the acquired side who are still in Draup, with titles.
- Write a second touch for day 7 on the supplier or data side of the same integration.
- Which service providers are linked to the integration priority? Who should I partner with or displace?
- Find a second source for the deal size so I can quote it.

### Tips

- Deals between 3 and 12 months past close are often the sweet spot: the plan exists, the work is still open.
- Large acquirers also buy rights and trademarks; those rarely create systems integration work.
- If the acquisitions table looks thin, the news step usually finds the missing deal.

## Email during cost cuts or restructuring

- **id:** `outreach-restructuring`
- **What you get:** A private read of the account's cost pressure and restructuring news, a sensitivity rating, and a careful 90-word email built on the company's own stated savings goal, with a softer alternative and a named reader.
- **Use it when:** An account is cutting costs, closing sites or restructuring, and you sell something that pays back fast but need to approach without seeming to profit from people's bad news.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. nestle.com); Persona (e.g. VP Procurement); What I sell (e.g. spend analytics software); Region (optional) (e.g. Europe); Proof point (optional) (e.g. found savings in indirect spend for Fabrikam Foods)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first (a named reader). For [Company], show revenue growth, 6 months of restructuring news and stated cost priorities; rate sensitivity; write a 90-word [Persona] email on their own savings goal, never mentioning cuts.
```

### Follow-ups

- Rewrite the email for the CFO, tied to the cash or margin priority.
- Which functions are still hiring despite the cuts? Show the top 5 with trends.
- Draft a 3-touch sequence over 3 weeks that never mentions the restructuring.
- Is anyone new leading [Persona]'s function since the restructuring began?

### Tips

- The company's own words (from an earnings call) are the safest hook: you're echoing their goal, not their pain.
- If the persona's team was just cut, a short resource with no meeting ask often lands better than a pitch.

## Email after a new site or centre

- **id:** `outreach-new-site`
- **What you get:** The account's newest centres, leases and expansions, fact-checked and matched against its location footprint and local hiring, plus a 100-word email and a LinkedIn note aimed at what the site is being staffed for.
- **Use it when:** An account has announced a new office, capability centre (an in-house delivery or tech centre, often called a GCC), hub or expansion, and the vendors for that site are about to be chosen.
- **Best for:** Account Executive, SDR / BDR, Services, SI & Staffing Seller, Partnerships & Alliances
- **Time:** 4–6 min
- **Inputs:** Company (e.g. hsbc.com); Persona (e.g. Head of the India technology centre); What I sell (e.g. managed workplace and IT services for new delivery centres); Business function (optional) (e.g. IT (default)); Location (optional) (e.g. Bengaluru)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first (a named reader, a dated announcement). Find [Company]'s new-site news from 6 months, fact-check the scale, check local postings, and write a 100-word email to a [Persona] on what it's staffed for.
```

### Follow-ups

- Who leads [Business function] in [Location]? Show up to 5 people with full titles.
- Which service providers already deliver from [Location] for this account?
- Write a version for a facilities or workplace leader instead of [Persona].
- Find a second source for the stated scale so I can quote it.

### Tips

- A lease or opening plus rising local postings is a much stronger trigger than either alone.
- Selling services to capability centres? Run the capability-centre services prompt next for build-operate-transfer and centre-of-excellence angles.

## Email on a hiring surge

- **id:** `outreach-hiring-surge`
- **What you get:** Which function is hiring above its own normal, the workloads and roles driving it, a named reader, and a 100-word email on the capability the surge is building, with no counting of their job ads in the copy.
- **Use it when:** An account is posting more jobs than usual in a function you sell into and you want to reach out while the team and its budget are taking shape.
- **Best for:** SDR / BDR, Account Executive, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. delta.com); Persona (e.g. VP Commercial Strategy); What I sell (e.g. sales enablement and CRM services); Business function (optional) (e.g. Sales & Marketing)

### Detailed prompt

```text
Act as my outbound copywriter for hiring-led triggers. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. delta.com]
- Persona: [who reads it, e.g. VP Commercial Strategy]
- What I sell: [one line, e.g. sales enablement and CRM services — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Sales & Marketing]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull 12 months of job postings by function: top 6, each with last 5 full months vs the 5 before and any "Trending Up" label. Use [Business function], else the function closest to [What I sell], else the biggest riser that fits.
3. In that function, pull the top 5 workloads with trend and the 4 newest postings: title, date, location, work type and a responsibility hinting at a new team or programme.
4. Pull up to 4 priorities in that function and pick the one the hiring most plausibly supports.
5. Label it Surge (over 25% up, editable default), Rising (10 to 25%), Flat, or Seasonal (a one-month spike); write copy only for Surge or Rising.
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact. Also pull the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (100 words max): the capability being built, in general terms from public job ads ("building out a media sales team"); a question on ramping it; one offer; one ask.
- Table "Functions" (top 6): Function | Postings (12 months) | Last 5 vs prior 5 (%) | Label.
- Table "What's driving it" (top 5): Workload | Postings | Recent months.
- Detail: newest roles (Date | Title | Location | Work type | Hint); linked priority (Draup's words, source, quarter); Gaps (what Draup lacked, to ask in discovery).

RULES
- Never quote posting counts or percentages in the copy; describe the team being built.
- If over half the newest roles are contract, say it may signal staff augmentation. If no function is Surge or Rising, say so and suggest a priority-led message instead.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables.
```

### Quick version

```text
Bottom line and next step first (a named reader, a dated why-now). Find where [Company]'s postings near [What I sell] rose most (last 5 full months vs 5 before), show what drives it, and write a 100-word [Persona] email.
```

### Follow-ups

- Show the metros where this function's postings are rising fastest.
- Who leads this function at [Company]? List up to 5 with full titles.
- Write a version for a services firm offering to staff part of the build-out.
- Is there a news item or priority that explains the surge?

### Tips

- Read the newest postings' responsibilities: they often name the new programme the surge is for.
- Partial first and last months distort the trend; the 5-versus-5 full-month comparison avoids that.

## Email on a new or rival tool

- **id:** `outreach-new-technology`
- **What you get:** Whether a technology or rival product is really in use at the account, how central it is (rated Red, Amber or Green if it's a competitor), where it shows up in public job ads, the priority it links to, and a 100-word email that never reveals stack tracking.
- **Use it when:** You've heard an account adopted a technology, or a competitor's product turned up there, and you want a timely, credible message: a complement, displace or integrate play.
- **Best for:** Account Executive, SDR / BDR, Presales & Solutions, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. intel.com); Technology or competitor (e.g. Databricks); Play (e.g. complement (or displace, or integrate)); Persona (e.g. Director of Data Engineering); What I sell (e.g. data observability software)

### Detailed prompt

```text
Act as my technical outbound copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. intel.com]
- Technology or competitor: [product or vendor, e.g. Databricks]
- Play: [complement, displace or integrate]
- Persona: [who reads it, e.g. Director of Data Engineering]
- What I sell: [one line, e.g. data observability software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Check the whole stack for products by [Technology or competitor]: category, usage strength, first and last evidence. Mark each Active (seen in 6 months) or Fading, and New if first seen in 12 months; rate competitors.
3. If [Company] makes or owns a product in the same category, say a displace play is unlikely.
4. Pull the 3 newest job postings naming the tool (title, date, what the team does with it) and the 12-month count.
5. Pull up to 3 priorities in the tool's workload and judge the [Play] opening: complement (Active, central), displace (Low or Fading), integrate (New, and priorities mention connecting systems).
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact. Also pull the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: the [Play] opening as Strong, Moderate or Weak, with one reason.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (100 words max): the team or programme from the job ads; a question tied to the priority; one offer for [Play]; one ask. Name the tool only if it appears in their public job ads.
- Table "In the stack": Product | Usage strength | Last seen | Status | Rating.
- Detail: job ads with the 12-month count; linked priority (Draup's words, source, quarter); Gaps (what Draup lacked, to ask in discovery).

RULES
- "First seen" is Draup's first public evidence, not a contract date; never write "you just bought".
- Never disparage the tool or its maker. If it isn't in the stack or job ads, say so and stop before writing.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Search by maker, whatever area products are filed under; for very broad makers (Microsoft, Google, Amazon), also name the category.
- Rating: an installed competitor product with High usage in the workloads of What I sell is Red, Medium is Amber, else Green. Newly detected (first seen within 12 months) is a separate Amber signal.
- If [Company] sells technology itself, skip priorities about products it sells.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables.
```

### Quick version

```text
Bottom line and next step first (a named reader, a dated why-now). Check [Company]'s stack for [Technology or competitor] with usage strength and rating; count job ads naming it; link a priority; write a 100-word [Play] email to a [Persona].
```

### Follow-ups

- Which other tools appear next to [Technology or competitor] in the same job ads?
- Who owns this area at [Company]? Show up to 5 people with full titles.
- Rewrite the email for the integrate play, aimed at an enterprise architect.
- Run the competitor check for a second vendor in the same category.

### Tips

- Job ads are public, so they're the safest way to mention a tool in an email.
- A tool with High usage and recent evidence is usually central: lead with a complement or integration angle rather than a rip-and-replace.
- If the account makes its own tool in the same category, the verdict will say so; a displace pitch rarely lands there.

## Cold-call opener, talk track, objections

- **id:** `outreach-cold-call`
- **What you get:** A 10-second opener, a 60-second talk track and three objection replies for one named person, each built on a fact-checked public fact or stated priority, plus three discovery questions.
- **Use it when:** You're about to cold-call a named prospect and want a reason to call that is specific to this account, not a generic pitch.
- **Best for:** SDR / BDR, Account Executive
- **Time:** 2–4 min
- **Inputs:** Company (e.g. lowes.com); Persona (e.g. VP Supply Chain Planning); What I sell (e.g. supply-chain planning software); Business function (optional) (e.g. Supply Chain); Competitor (optional) (e.g. Blue Yonder)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first (who to call, named, and why today). From 2 confirmed public facts and [Company]'s priorities, write a 25-word opener, a 150-word talk track, three objection replies and three discovery questions for a [Persona].
```

### Follow-ups

- Write the voicemail I leave if they don't pick up, and a matching follow-up email.
- Give me two more objection replies: "We're mid-contract" and "Talk to procurement".
- Rewrite the talk track for a services seller offering a managed service.
- Who should I call second if this person doesn't pick up?

### Tips

- Lead with the newest confirmed fact; anything older than a quarter sounds like research, not a reason to call.
- If the company reports on a fiscal year that runs ahead of the calendar, say "on your latest earnings call" rather than naming a quarter.

## LinkedIn note and InMail to an executive

- **id:** `outreach-linkedin-exec`
- **What you get:** A confirmed profile for one named executive, a 300-character connection note with no pitch, a 110-word InMail tied to a stated priority in their remit, and a short message for after they accept.
- **Use it when:** You have one senior person to reach on LinkedIn and want a note that gets accepted and an InMail that gets read.
- **Best for:** SDR / BDR, Account Executive, Account & Customer Success Manager, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. cisco.com); Executive (e.g. Global Head of Enterprise Applications, IT); What I sell (e.g. AI-assisted quoting software); Business function (optional) (e.g. IT); Shared ground (optional) (e.g. we both spoke at the same industry event)

### Detailed prompt

```text
Act as my social-selling copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. cisco.com]
- Executive: [name and/or title, e.g. Global Head of Enterprise Applications, IT]
- What I sell: [one line, e.g. AI-assisted quoting software — skip if you ran the start-here prompt]
- Business function (optional): [e.g. IT; blank uses the one closest to what I sell]
- Shared ground (optional): [a real, permitted connection, e.g. we both spoke at the same industry event]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Find the executive: pull key executives in [Business function], 10 per page, up to 3 pages, and match by name or full profile title. If not found, show the 5 closest titles and ask which to use. Record full title, location, function and workloads.
3. Pull up to 6 [Business function] priorities, newest quarter first, and keep the one closest to the executive's remit.
4. Pull the account's top-ranked news from the last 90 days where [Company] is the actor and keep one item that touches the remit, if any. Fact-check it.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Connection note: 300 characters max including spaces, no pitch, no link; mention [Shared ground] only if I gave it.
- InMail: subject (6 words max) and body (110 words max): the priority or news as context; a question about their remit; one line on [What I sell]; one ask.
- After they accept (60 words max): thanks in a few words, one useful resource, no meeting ask.
- Table "Who": Name | Full title | Location | Workloads | Pages checked.
- Detail: the hook (priority in Draup's words, source, quarter; news item, date, source); Gaps (what Draup lacked, to ask in discovery).

RULES
- Never mention tenure, schools, past employers, skills or anything else from the profile unless it is [Shared ground].
- If the person can't be found, don't write to a guessed person; ask me.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 380 words including tables.
```

### Quick version

```text
Bottom line and next step first. Find [Executive] at [Company], confirm the full title, match a stated priority and a confirmed 90-day news item, then write a 300-character note, a 110-word InMail and a 60-word post-accept message.
```

### Follow-ups

- Write a second InMail for day 7 on a different priority.
- Draft a comment I could leave on a company post about this priority.
- Find two peers of [Executive] in the same function for a parallel thread.
- Turn the InMail into a 70-word email for the same person.

### Tips

- Draup has no name search for executives, so give the full title as well as the name; it makes the match much faster.
- Notes with no pitch are often accepted more readily; save the ask for the InMail or the post-accept message.

## Voicemail script plus follow-up email

- **id:** `outreach-voicemail`
- **What you get:** A 25-second voicemail for a named person built on one confirmed public fact, the matching same-day follow-up email, and a shorter second voicemail for day 4.
- **Use it when:** You call senior buyers who rarely pick up and want the voicemail and email to work as one touch.
- **Best for:** SDR / BDR, Account Executive
- **Time:** 1–2 min
- **Inputs:** Company (e.g. target.com); Persona (e.g. VP Store Operations); What I sell (e.g. workforce scheduling software); Me (e.g. [Your name], Northwind Data Services); Priority theme (optional) (e.g. store teams)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first (who to call, named, and why now). From one confirmed 60-day fact and one [Company] priority, write a 60-word voicemail, an 80-word follow-up email and a 40-word day-4 voicemail for a [Persona].
```

### Follow-ups

- Write a 3-touch call-email-call cadence for the next 10 days.
- Rewrite voicemail 1 for the persona's boss.
- Give me a 15-second version for a mobile number.
- Swap in a different confirmed fact for voicemail 2.

### Tips

- Read the script aloud once; if it runs past 30 seconds, cut the value line, not the fact.
- Common words in company names can pull in unrelated news; the actor check in step 2 catches most of it.

## Emails to three buyers at one account

- **id:** `outreach-multithread`
- **What you get:** A thread map for one account (economic buyer, technical buyer and champion), each named from Draup and tied to a different stated priority, with two fact-checked emails per person and a staggered send plan.
- **Use it when:** A deal depends on more than one person and you want to open three conversations at once without sending the same email three times.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. siemens.com); What I sell (e.g. supply-chain planning software); Personas (optional) (e.g. CFO, Head of Supply Chain IT, SVP Supply Chain Planning); Proof point (optional) (e.g. cut planning cycle time at Fabrikam Foods)

### Detailed prompt

```text
Act as my account-based sequencing strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Personas (optional): [three titles, e.g. CFO, Head of Supply Chain IT, SVP Supply Chain Planning; blank and I'll suggest them]
- Proof point (optional): [a result I may quote, e.g. cut planning cycle time at Fabrikam Foods]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the account's key priorities grouped by function in one pass (up to 3 per function).
3. Give each persona a distinct priority: Economic buyer (Finance or Management & Strategy), Technical buyer (IT or the function's systems), Champion (the operating function closest to [What I sell]). Use my titles if given.
4. For each persona's function, pull 5 key executives and pick the likeliest by full profile title; drop titles that don't fit and flag subsidiaries. If no economic buyer appears, search once more for Chief, EVP or CIO titles.
5. Pull top-ranked news from the last 90 days; keep one Confirmed item all three threads can use (the account must be the actor).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for. Start with the champion.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Per persona: Email 1 (subject 6 words max, body 90 words max) on that persona's priority; Email 2 (day 4, 50 words max) on the shared news item or a second fact; same single ask in both.
- Table "Thread map": Persona | Name | Full title | Priority (quarter) | Angle in one line.
- Send plan: champion day 1, technical buyer day 3, economic buyer day 6, and what to do if one replies.
- Detail: priorities in Draup's words with source; "Roles with no clear person" (titles to look for); Gaps (what Draup lacked, to ask in discovery).

RULES
- Never reuse a paragraph across threads. Never write "I've also contacted your colleagues" or CC anyone. Buyer roles are candidates, labelled "likely".
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 500 words including tables.
```

### Quick version

```text
Bottom line and next step first (who to email first, named). Give [Company]'s economic buyer, technical buyer and champion each a different priority, name a person for each, and write two emails each with a staggered send plan.
```

### Follow-ups

- Add a fourth thread for procurement, tied to a sourcing priority.
- Write a LinkedIn connection note for each of the three people.
- One of them replied positively; draft the internal-champion brief I should send them.
- Swap the economic buyer for the CIO and rewrite that thread.

### Tips

- The grouped-priorities view covers every function in one pass, so you can see at a glance which leaders share an agenda.
- In conglomerates, executive lists often include business-unit heads under a shared function tag; check the full title before you pick.

## Re-engage a stalled or ghosted account

- **id:** `outreach-reengage`
- **What you get:** A dated, fact-checked list of what changed since your last contact, a reopen-or-wait call, a re-engagement email built on the change, a polite break-up email, and a version for a new person if one appeared.
- **Use it when:** A deal or conversation went quiet weeks or months ago and you want a reason to re-open that isn't "just checking in". For a fuller account review, use "What changed since [Date]".
- **Best for:** Account Executive, Account & Customer Success Manager, SDR / BDR
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); Last contact date (e.g. 2026-06-01); What we discussed (e.g. an AI pilot for R&D data); Contact title (e.g. Head of R&D Data); What I sell (e.g. AI data platform services); Workload or function (optional) (e.g. Artificial Intelligence & Data Science)

### Detailed prompt

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

### Quick version

```text
Bottom line first (reopen now, reopen via a new person, or wait) and the next step with a named person. List confirmed changes at [Company] since [Last contact date], then write a 90-word re-engagement email and a 60-word break-up email.
```

### Follow-ups

- Write a LinkedIn message for the new leader instead of an email.
- If they reply "not now", draft a 2-line response and a reminder for 90 days.
- Run the same check for my other stalled accounts: [websites].
- Find a second source for the top change so I can name it in the email.

### Tips

- The break-up email works best after one re-engagement attempt; send it about a week later.
- A new leader in the buyer's chain is often the strongest reason to reopen, and a reason to write to both people.

## One-page brief before a C-level meeting

- **id:** `outreach-exec-briefing`
- **What you get:** A one-page, send-ahead briefing note for a C-level meeting (what you understand they're working on, what you'll bring, a 30-minute agenda and two questions), built only on confirmed facts, with a cover email and a private prep sheet of sensitivities.
- **Use it when:** You have a meeting booked with a C-level executive and want to send a short note 24 to 48 hours ahead that shows you've done the work.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. unilever.com); Executive title (e.g. Chief Digital and Marketing Officer); Meeting purpose (e.g. first meeting on creator-marketing measurement); What I sell (e.g. marketing mix and attribution analytics); Business function (optional) (e.g. Sales & Marketing); Proof point (optional) (e.g. improved media ROI for Contoso Retail)

### Detailed prompt

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

### Quick version

```text
Bottom line and next step first. Build a send-ahead one-page note for a [Executive title] at [Company]: 3 confirmed, dated things they're working on, what we'll bring, a 30-minute agenda, two questions, a 60-word cover email and private sensitivities.
```

### Follow-ups

- Turn the note into a 3-slide opening deck for the meeting.
- Write the follow-up email I'll send after the meeting, leaving blanks for what they said.
- Add a short section on what two peers are doing on the same priority.
- Who else from their team should I invite, by name and title?

### Tips

- Send the note 24 to 48 hours ahead; it often gets forwarded to the people the executive wants in the room.
- Keep the sensitivities list handy: a divestment or reorganisation is often on the executive's mind even if it's not on your agenda.
