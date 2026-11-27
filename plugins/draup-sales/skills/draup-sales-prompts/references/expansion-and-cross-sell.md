# Expansion and cross-sell

Grow existing customers: global account maps, whitespace, cross-sell, new budget holders and sponsor coverage.

## Map a customer's units, sites and leaders

- **id:** `expand-account-map`
- **What you get:** A one-page map of a customer: business units and regions with growth, key sites, the units and brands its leaders sit in and recent acquisitions, marked Ours, Adjacent or Open, with the top white space and who leads it.
- **Use it when:** At the start of an account plan, or when you inherit a large customer.
- **Best for:** Account & Customer Success Manager, Account Executive, Sales Leader & RevOps, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. 3m.com); What I sell (e.g. supply-chain analytics software); Where we are today (e.g. Safety & Industrial, North America (optional))

### Detailed prompt

```text
Act as my strategic account planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- What I sell: [one line, e.g. supply-chain analytics software — skip if you ran the start-here prompt]
- Where we are today (optional): [units or regions we serve, e.g. Safety & Industrial, North America]

CONTEXT (why this matters)
Large customers buy in pieces, each with its own budget.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull the profile (HQ, workforce, industries) and revenue by business unit (share, growth).
3. Pull revenue by region, latest year; compute growth from amounts.
4. Locations: key locations for the function closest to [What I sell] (one row per metro, 15 rows), plus all-function rows limited to HQ Location and to GCC Locations. Group by metro (functions, 12-month postings, tags); keep the HQ, top metros and every capability centre.
5. Pull one page of top leaders and one page of 10 in the function closest to [What I sell]; note each one's unit or brand from their profile employer.
6. Pull 3-year acquisitions and the most important 90-day news item where [Company] is the actor.
7. Mark each unit, region and site Ours ([Where we are today]), Adjacent (same unit or region) or Open.

OUTPUT
- Bottom line: 2 sentences — where the room to grow is and what it means for me.
- Recommended next step: a named person (name, full title) who leads the biggest open area, the action this week and the dated why-now (or say none).
- Table "White space" (top 3): Area | Fact behind it | Who leads it | Status.
- Table "Where to sell" (up to 10): Unit, region or site | Share or postings | Growth | Status.
- "Units and brands in the leadership": up to 5 bullets; flag subsidiaries and possibly sold or spun-off brands.
- Detail: account shape (HQ, workforce, revenue, industries), all units, regions and sites, acquisitions (Date | Company | Why bought).
- Gaps: what Draup lacked; ask in discovery.

RULES
- A unit seen only in leaders' profiles is "seen in leadership", not confirmed.
- Empty unit or region revenue: say so; don't infer from news. Two or fewer units: say so and use units and brands seen in leadership as the unit list.
- Flag acquisition rows whose fields look shifted.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Check for divestments before calling a regional drop a cut.
- The acquisitions table can miss deals; check M&A news too.
- Site headcount is indicative; lean on postings.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

### Quick version

```text
Map [Company] on one page. Lead with the 3 biggest open areas for [What I sell] and a named leader to approach. Show units, regions and top sites with growth, marked Ours, Adjacent or Open, and recent acquisitions.
```

### Follow-ups

- For the biggest Open unit, map the buying committee.
- Where are they hiring fastest in the function closest to what I sell?
- Turn the white space into 3 expansion plays with a first email each.

### Tips

- Fill in Where we are today (or save account notes in the start-here prompt); the Ours, Adjacent and Open labels are what make the map useful.
- Leaders' profile employers often reveal brands and units the revenue split hides.

## Find uncovered functions worth selling to

- **id:** `expand-function-whitespace`
- **What you get:** Every business function at an existing customer scored on priorities, hiring and outsourced work against where you already sell, with the top 3 uncovered functions, the named leaders who own them and a bridge from your current footprint.
- **Use it when:** Before an account plan or QBR, when you want to grow beyond the function you sell into today. Use this to rank functions across the account; use "Best entry points: expand or new" instead to pick initiatives inside one function.
- **Best for:** Account & Customer Success Manager, Account Executive, Sales Leader & RevOps, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. roche.com); Current footprint (e.g. IT – data engineering and BI (or my saved account notes)); What I sell (e.g. data and analytics services)

### Detailed prompt

```text
Act as my account-expansion strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. roche.com]
- Current footprint: [where we sell today, by function or workload, e.g. IT – data engineering and BI — or my saved account notes]
- What I sell: [one line, e.g. data and analytics services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Worth pursuing: leaders talk about it, hire for it and buy it outside.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull the grouped key priorities (up to 3 per function, with quarter), not the full list, which is too large.
3. Pull 12-month hiring by function (top 15), last 5 full months vs the 5 before.
4. Pull outsourced workloads (types of work, e.g. Data Engineering) by deal count (top 20), mapped to functions, plus active engagements per function; if a function returns zero, retry Draup's other name (R&D for ER&D).
5. Score each function 0–3 (editable default): +1 for an earnings-call priority in the last two fiscal quarters, +1 for Rising hiring or postings in the top third of functions, +1 for 20+ deals in its workloads. Mark Covered if it matches [Current footprint].
6. Keep uncovered functions that fit [What I sell]; for the top 2, pull leaders filtered by function and matching workloads (one page of 10 each).
7. Pull the most important 90-day news item touching a top function.

OUTPUT
- Bottom line: 2 sentences — the best uncovered function and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the top function, the action this week and the dated why-now (or say none).
- Table "Top 3 whitespace functions": Function | Score | Why now (dated priority or hiring fact) | Leader (name, title).
- Table "Function heat map" (up to 10): Function | Latest priority (quarter) | Postings and trend | Engagements | Score (Covered?).
- "Bridge": per top function, how [Current footprint] gets us in the room (shared data, leader or programme).
- Detail: who owns each top function (Name | Full title | Location | Years in title, up to 5) and incumbent providers.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Catch-all workloads (Account Management, Project/Programs Management) never score a function.
- Don't recommend a function whose only signal is outsourcing to agencies or staffing firms.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

### Quick version

```text
Score every business function at [Company] on priorities, 12-month hiring and outsourced work. Lead with the top 3 uncovered functions for [What I sell] and the named leader to approach, with a dated why-now.
```

### Follow-ups

- For [Function], map the full buying committee.
- Which providers already work in [Function] and how deep are they?
- Draft a 100-word email from our current sponsor introducing us to the [Function] leader.

### Tips

- Be precise in Current footprint (function and workload); vague footprints produce vague whitespace.
- The Bridge line is what turns a cold function into a warm introduction.

## Cross-sell from their adjacent stack

- **id:** `expand-adjacent-tech`
- **What you get:** The tools a customer runs next to what you already sell them, graded Active, Thin or Fading and rated for incumbent strength, with the priorities and job ads that justify a cross-sell, up to 3 plays and the named owner to pitch.
- **Use it when:** You have a product installed and want to sell the next one, or attach a service to it.
- **Best for:** Account & Customer Success Manager, Account Executive, Presales & Solutions
- **Time:** 4–6 min
- **Inputs:** Company (e.g. visa.com); What we already sell them (e.g. our data integration platform (or my saved account notes)); Adjacent areas (e.g. Data Governance Software, Data Quality Software (optional)); What I sell (e.g. data governance and quality platform)

### Detailed prompt

```text
Act as my cross-sell strategist for a software account team. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. visa.com]
- What we already sell them: [e.g. our data integration platform]
- Adjacent areas (optional): [1–3 software categories, e.g. Data Governance Software; blank = the 2–3 next to what we sell]
- What I sell: [one line, e.g. data governance and quality platform — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Expand next door to a working install, where no strong incumbent locks the area.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Confirm our install: check the stack for that product or maker (strength, last seen); if not detected, say so.
3. Pull the stack in [Adjacent areas], up to 40 rows each; if one returns nothing, retry the closest Draup category and say which.
4. Rate each tool: Red (High) or Amber (Medium) if seen in 90 days; Green if Low, or "fading" (no strength, or last seen over 90 days ago). Drop obvious misfilings.
5. Pull up to 5 priorities in the adjacent workloads; keep those about the area.
6. Pull the top 15 job-ad skills for the matching workload (12 months).
7. Owner and trigger: from one page of 10 executives in the matching workload or function, the 3 best-fitting titles; and the most important 90-day news item.
8. Build up to 3 plays: Replace (Green incumbent), Consolidate (3+ overlapping tools) or Complement (Red incumbent).

OUTPUT
- Bottom line: 2 sentences — open or locked, and the best play for us.
- Recommended next step: a named person (name, full title) who owns the adjacent area, the action this week and the dated why-now (or say none).
- Table "Cross-sell plays" (up to 3): Play | Target tools | Evidence (dated) | Opening line (25 words max).
- Table "Adjacent landscape" (top 10): Product | Maker | Strength, last seen | Rating.
- One line on our install; "Incumbents to respect": coexist or compete.
- Detail: the full landscape and why-now evidence (priorities, skills).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Red means locked: complement it. Low-only tools don't count as an incumbent; say so.
- A product first seen in 12 months and already Medium or High is a fresh choice: complement it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low. Say "fading", never "dropped".
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
At [Company], confirm our installed product, then grade every tool in [Adjacent areas]. Lead with the best cross-sell play and the named owner to pitch, with a dated why-now. Show incumbent strength, matching priorities and job-ad skills.
```

### Follow-ups

- Map the buying committee for [Adjacent area].
- Draft a consolidation business case for the Consolidate play.
- Which peers of [Company] already run our adjacent product?

### Tips

- Name exact Draup categories in Adjacent areas; if unsure, leave it blank and Claude will pick the ones next to what you sell.
- Fragmented areas with several Low tools often signal no clear owner; find one.

## New budget holders outside our footprint

- **id:** `expand-new-budget-holders`
- **What you get:** Senior leaders new in role (about 18 months or less) in the functions you don't yet sell to, plus announced leadership changes, each with the priority they likely own, a first-90-days angle and the one to contact first.
- **Use it when:** Quarterly in your top accounts, or when you need a reason to reach a new part of a customer. Use this to widen into functions you don't cover; use "New leaders and warm intro paths" instead for warm intros in the function you already sell to.
- **Best for:** Account & Customer Success Manager, Account Executive, SDR / BDR, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. boeing.com); Functions we don't cover (e.g. Finance & Accounting, Human Resources, Procurement); What I sell (e.g. finance and HR process automation)

### Detailed prompt

```text
Act as my account-expansion researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. boeing.com]
- Functions we don't cover: [1–3 business functions, e.g. Finance & Accounting, Human Resources, Procurement]
- What I sell: [one line, e.g. finance and HR process automation — skip if you ran the start-here prompt]

CONTEXT (why this matters)
New leaders review vendors and set priorities in their first year; in a customer, one in an uncovered function is the cleanest way in.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull senior leaders in [Functions we don't cover], 10 per page, up to 3 pages. Keep Director and above by full title with 18 months or less in their current title (editable default).
3. Search Draup's news for executive appointments, departures and interim roles at [Company] in the last 6 months; keep only items where [Company] is the employer, and mark the most important from the last 90 days.
4. Pull up to 3 priorities per uncovered function (latest fiscal quarters first) and match each new leader to the closest by function and title.
5. Rank: C-level or "Head of" first, then budget control, then shortest time in title.

OUTPUT
- Bottom line: 2 sentences — the best new budget holder and what it means for [What I sell]. Add: people checked, pages, people kept.
- Recommended next step: a named person (name, full title), the top new leader, the action this week and the dated why-now (or say none).
- Table "New budget holders" (up to 10): Name | Full title | Function | Months in title | Linked priority (quarter).
- "First-90-days angles": top 3 leaders, 2 lines each, tied to [What I sell] and to proof from the part of [Company] we serve.
- "Announced changes" (6 months): Date | Change (appointment, exit, interim) | Role | Source.
- Detail: each leader's unit (flag subsidiaries), location and budget control; functions with no new leader.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Interim leaders and announced searches mean decisions may wait; say so next to the person.
- If a function returns fewer than 3 people, say profiles may be thin rather than concluding there's no leader.
- Board appointments are not budget holders.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Leadership data can lag about 3 months; give the latest move date seen.
- If European executives return none, say profiles there may be restricted.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 400 words above Detail, tables included.
```

### Quick version

```text
At [Company], find senior leaders in [Functions we don't cover] 18 months or less in title. Lead with the one to contact first and the dated why-now, then announced changes, linked priorities and first-90-days angles.
```

### Follow-ups

- Write a 90-word intro email from our current sponsor to [Leader].
- Where did [Leader] work before, and was it one of our customers?
- Map the rest of the buying committee under [Leader].

### Tips

- Months in title comes from the profile and can lag about 3 months; confirm before you open with "congratulations".
- Announced departures are as useful as hires: the successor will review vendors.

## Subsidiaries and acquisitions to expand into

- **id:** `expand-subsidiaries`
- **What you get:** A customer's acquired companies and subsidiaries, each checked for whether it still runs on its own (own hiring, size, people moving to the parent), ranked as expansion targets, with the named person to approach at the top one.
- **Use it when:** After a customer buys companies, or when the main account is saturated and you want the next logo inside the group.
- **Best for:** Account & Customer Success Manager, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. medtronic.com); What I sell (e.g. ERP integration and managed services); Window (e.g. last 3 years (optional))

### Detailed prompt

```text
Act as my account-expansion analyst for corporate groups. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- What I sell: [one line, e.g. ERP integration and managed services — skip if you ran the start-here prompt]
- Window (optional): [default last 3 years]

CONTEXT (why this matters)
An integrating acquisition is bought for centrally by the parent; a standalone subsidiary has its own leaders and budget and sells like a new logo.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull acquisitions in [Window]: date, company, intent, size, and whether Draup holds it as a company.
3. Search Draup's M&A news for [Company], last 12 months, for deals the table misses and any divestments; mark the most important item from the last 90 days.
4. Pull talent flow by company (20 rows, largest movement first). Rows marked as its own subsidiaries are subsidiaries; large one-way flows from an acquired company into [Company] suggest staff moving onto the parent.
5. For the 3 largest acquired companies or subsidiaries Draup holds: profile (workforce, parent shown) and 12-month hiring summary.
6. Rate each: Integrating (few or no own postings, or staff moving to parent), Standalone (own postings continuing), Unclear.
7. For the top target: if Standalone, pull its own top 3 executives; if Integrating, pull the parent's top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the best target and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the target or the parent's integration lead, the action this week and the dated why-now (or say none).
- Table "Target check" (top 3): Company | Workforce | Own postings (12 mo) | Rating | Who to approach.
- Table "Acquisitions" (up to 10, newest first): Date | Company | Size or "undisclosed" | In Draup?
- "Expansion plays": per target, the angle for [What I sell] and the timing. "Leave alone": divested or spun-off units, dated.
- Detail: deals from news missing from the table; subsidiaries in talent flow (Company | Moving to parent | Moving back | Read).
- Gaps: what Draup lacked; ask in discovery.

RULES
- A subsidiary with zero own postings is likely folded into the parent's hiring; don't call it inactive.
- Don't treat internal division names (e.g. "[Company] MedTech") as separate companies unless Draup holds them as one.
- Keep deal sizes as reported; if table and news disagree, show both.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- Talent flow ends about 3 months ago and the last month undercounts exits; state the months.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Label anything you infer as "likely".
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

### Quick version

```text
List [Company]'s acquisitions in [Window] and subsidiaries. Lead with the best target and a named person to approach. For the top 3, check size, own hiring and staff moving to the parent; rate Integrating or Standalone.
```

### Follow-ups

- For [Target], who are the senior leaders and which came from the parent?
- What does [Target] run in its tech stack compared with the parent?
- Draft an email to the parent's integration lead offering help with [Target].

### Tips

- Deals closed 6–18 months ago are often mid-integration: the busiest window for systems work.
- The acquisitions table can miss big deals; the news step is not optional.

## Land at one site, expand to others

- **id:** `expand-site-to-site`
- **What you get:** From the site or capability centre you already serve, the sister sites doing the same work, ranked by workload overlap and growth, with each one's local leader and the next site to approach.
- **Use it when:** You've landed at one site or global capability centre and want to replicate it across the group.
- **Best for:** Account & Customer Success Manager, Services, SI & Staffing Seller, Account Executive, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. 3m.com); Site we serve (e.g. Bengaluru, India); Business function (e.g. IT (optional)); What I sell (e.g. infrastructure managed services)

### Detailed prompt

```text
Act as my land-and-expand strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Site we serve: [metro, e.g. Bengaluru, India]
- Business function (optional): [e.g. IT, ER&D, Finance & Accounting; default is the one closest to What I sell]
- What I sell: [one line, e.g. infrastructure managed services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
The best next site does similar work, is growing and has a reachable leader.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Pull key locations for the function limited to capability-centre sites, 15 rows: metro, indicative workforce, 12-month postings, growth index.
4. Pull key locations for the function across all site types, 15 rows, to add the HQ and other large sites. Merge by metro.
5. Pull the top workloads in job ads for the function at [Site we serve] and the 2 most promising other sites (one lookup per site, 8 rows).
6. For the top 3 candidate sites, pull senior leaders in the function based there (one page of 5 each). Drop anyone whose headline names another employer.
7. Score each: workload overlap with [Site we serve] (High, Medium, Low), growth index vs the median of listed sites, and whether a named local leader exists.
8. Pull the most important news item from the last 90 days where [Company] is the actor (site openings and expansions first).

OUTPUT
- Bottom line: 2 sentences — the next site and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the next site, the action this week and the dated why-now (or say none).
- Table "Next 3 sites": Metro | Overlap | Growth vs median | Local leader (name, title) | Why now (dated).
- Table "Sites with the function" (up to 10): Metro | Tag | Workforce (indicative) | Postings (12 mo) | Growth index. Highlight [Site we serve].
- "Reference story": 2 lines on what we deliver at [Site we serve] that maps to the next site's hiring. "Intro path": who at our site could introduce us, and to whom.
- Detail: what each site is hiring for (Workload | our site | Site 2 | Site 3).
- Gaps: what Draup lacked; ask in discovery.

RULES
- If rows come back for every function, say the limit didn't apply and keep only that function's rows.
- A site with zero postings in 12 months is stable, not growing; don't rank it first.
- The growth index is postings divided by workforce, so it runs high for small sites; say so when one tops the list.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Site headcount is indicative only; lean on postings.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
Starting from [Site we serve] at [Company], rank the sister sites for [Business function]. Lead with the next site to approach and its named local leader with a dated why-now. Compare size, postings and what each site is hiring for.
```

### Follow-ups

- What are they hiring for at [Next site]? Show 5 recent postings.
- Draft an intro request from our sponsor at [Site we serve] to the leader at [Next site].
- Which providers already deliver at [Next site]?

### Tips

- Workload overlap matters more than size: the same work means your reference lands.
- Capability-centre tags can include plants; check the functions before you plan the pitch.

## Check sponsor risk and relationship gaps

- **id:** `expand-sponsor-coverage`
- **What you get:** A risk read on your executive sponsor (tenure, new bosses, announced changes), a coverage grid of who you know versus who matters, likely successors and the 3 named relationships to build next.
- **Use it when:** Before a renewal or expansion, after a reorganisation, or when one sponsor carries the account. Use this for relationship coverage; use "Renewal risk check (red, amber, green)" for the whole account's risk, including competitors.
- **Best for:** Account & Customer Success Manager, Sales Leader & RevOps, Account Executive, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. mastercard.com); Our sponsor (e.g. Jane Doe, SVP Data Platforms (or my saved account notes)); Who we know (e.g. Director Data Engineering; Head of IT Procurement (optional)); Business function (e.g. IT (optional)); What I sell (e.g. data platform services)

### Detailed prompt

```text
Act as my account relationship strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. mastercard.com]
- Our sponsor: [name and title, e.g. Jane Doe, SVP Data Platforms — a title alone may match several people]
- Who we know (optional): [titles of other contacts, names optional]
- Business function (optional): [default is the one closest to What I sell, e.g. IT]
- What I sell: [one line, e.g. data platform services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Accounts are lost when one sponsor leaves or is overruled. Good coverage spans three levels in more than one unit; never guess at people's plans.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Pull senior leaders in the function, 10 per page, up to 3 pages. If fewer than 15 come back, add the top 20 leaders across the company (2 pages) to cover the C-suite.
4. Match [Our sponsor] and [Who we know] to profiles by name and title; unmatched contacts are "not found in Draup".
5. Search Draup's news for executive appointments, departures, interim roles and reorganisations at [Company] in the last 6 months; mark the most important from the last 90 days.
6. Rate sponsor risk: High (new leader above them in 12 months, unit reorganised, or under 6 months in title), Medium (over 6 years in title, or their function lead is interim), Low otherwise. Editable defaults.
7. Build the coverage grid: three levels by unit or region, each Known or Gap.

OUTPUT
- Bottom line: 2 sentences — sponsor risk and the biggest coverage gap. Add: people checked, pages, contacts matched.
- Recommended next step: a named person (name, full title) to build a relationship with next, the action this week and the dated why-now (or say none).
- "Sponsor read": one line: title, months in title, risk (High, Medium, Low) and the dated signals behind it.
- Table "Coverage grid": Level | up to 4 units or regions, each cell Known (who) or Gap (most senior person there).
- Table "Build next" (3): Person (name, title) | Why (dated fact) | Intro path through someone we know.
- Detail: likely successors or backups (up to 3, months in title) and leadership changes (Date | Change | Source).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Sponsor risk is internal planning; never put it in customer-facing copy.
- Function tags can be loose (legal or scientific leaders under IT); drop clear mismatches and say how many.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Leadership data can lag about 3 months; give the latest move date seen.
- If European executives return none, say profiles there may be restricted.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
Rate [Our sponsor]'s risk at [Company] (tenure, new leaders above, announced changes). Lead with the risk and the named person to build a relationship with next, then a coverage grid and likely successors.
```

### Follow-ups

- Draft a note from [Our sponsor] introducing us to [Gap leader].
- Prepare a 1-page executive-sponsor brief for our CEO to meet [Economic buyer].
- Run this again after the next earnings call and compare.

### Tips

- Give your sponsor's name and title; several people often share a title.
- A brand-new CFO or CPO above your sponsor often triggers a vendor review within two quarters.

## Expansion business case from growth units

- **id:** `expand-business-case`
- **What you get:** A short, evidence-led case for expanding into a customer's fastest-growing unit or region: where growth is, the priorities funding it, a Draup-estimated spend pool, a 150-word executive summary and the named owner to send it to.
- **Use it when:** Before proposing an expansion to an existing customer's sponsor or your own deal desk. Use this to grow an existing customer; use "Business-case inputs from their numbers" instead for a new deal's value model.
- **Best for:** Account & Customer Success Manager, Account Executive, Sales Leader & RevOps, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. boeing.com); Current footprint (e.g. Commercial Airplanes, North America; $400K a year (or my saved account notes)); Expansion idea (e.g. extend predictive maintenance analytics to Global Services); What I sell (e.g. industrial IoT analytics software and services)

### Detailed prompt

```text
Act as my value consultant writing an expansion business case. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. boeing.com]
- Current footprint: [where we are and roughly what it's worth, e.g. Commercial Airplanes, North America; $400K a year]
- Expansion idea: [one line, e.g. extend predictive maintenance analytics to Global Services]
- What I sell: [one line, e.g. industrial IoT analytics software and services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Expansion cases ride the customer's own growth story.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull latest revenue, EBITDA, R&D and IT spend with growth, and forecasts.
3. Pull revenue by business unit and by region; name the fastest-growing unit and region (or say Draup has no unit split).
4. Pull key priorities grouped by function; keep those supporting [Expansion idea] or the growth unit, with quarter and stated targets.
5. Pull the Draup-estimated IT spend split (software, internal staffing, IT outsourcing, hardware) for the latest two years.
6. Pull workloads (types of work) trending up in hiring (12 months) linked to [Expansion idea].
7. Owner and trigger: the top 3 executives in the function closest to [Expansion idea] (one page of 10) and the most important news item from the last 90 days.
8. Size a range: the relevant IT-spend category scaled by the growth unit's revenue share, vs [Current footprint].

OUTPUT
- Bottom line: 2 sentences — the size of the opportunity and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the expansion area, the action this week and the dated why-now (or say none).
- Table "Growth story" (up to 8): Unit, region or metric | Share or value | Growth | Year.
- Table "Spend pool": Category | Latest | Prior year | Note; then the sized range with the maths shown.
- "What leadership committed to" (priority, quarter, fit), "Why us" (3 bullets) and "Risks" (up to 3, dated).
- "Executive summary": 150 words max, for our sponsor to forward.
- Detail: hiring behind it and full financials.
- Gaps: what Draup lacked; ask in discovery.

RULES
- The sized range is not their budget; show the formula.
- Thin hiring for its size? Say so; lean on priorities.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- IT spend is Draup-estimated (often modelled from revenue); its growth isn't a signal. A forecast over 15% off the latest actual is a model estimate.
- Compute regional growth from amounts; check for divestments before calling a drop a cut.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 500 words above Detail, tables included.
```

### Quick version

```text
Build an expansion case for [Expansion idea] at [Company]. Lead with the size of the opportunity and the named owner to send it to. Show growth units, supporting priorities, a Draup-estimated spend pool and a 150-word summary.
```

### Follow-ups

- Turn the executive summary into a 5-slide outline.
- Which leaders own the priorities in the case?
- Stress-test the case: what would make the sponsor say no?

### Tips

- Quote management's own words from the priorities; sponsors reuse them in budget requests.
- Fill in what the current footprint is worth; the comparison makes the ask feel proportionate.
