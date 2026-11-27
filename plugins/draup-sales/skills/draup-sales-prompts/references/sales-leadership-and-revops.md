# Sales leadership and RevOps

Size territories, segment books, plan pipeline and enable reps on new verticals.

## Which region gets the next rep

- **id:** `leaders-territory-potential`
- **What you get:** A ranked comparison of 2–5 countries for one industry, or 2–4 industries in one country: how many sizeable accounts each holds, how many are active in the work you sell, where your rivals are really in use, and the revenue at stake, with where to add the next rep and the first account to open.
- **Use it when:** Annual or half-year planning, when you must decide which country, or which industry in your country, gets the next rep, partner or campaign budget. Use "Which cities to base reps and events" to pick cities inside one country, and "Carve balanced territories by geography" to split a market between reps.
- **Best for:** Sales Leader & RevOps, Marketing & ABM
- **Time:** 6–8 min
- **Inputs:** Vertical (e.g. Aerospace & Defense (or 2–4 industries, e.g. Retail; Food, Beverages & Consumer Goods)); Compare (e.g. France, Germany, United Kingdom (or one country, e.g. United States of America)); Minimum employees (e.g. 2,000); What I sell (e.g. OT and device security software); My competitors (optional) (e.g. CrowdStrike, Palo Alto Networks); Current coverage (optional) (e.g. 1 rep in the UK, none in France or Germany)

### Detailed prompt

```text
Act as my RevOps analyst sizing territories. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Aerospace & Defense; or 2–4 to compare, e.g. Retail; Food, Beverages & Consumer Goods]
- Compare: [2–5 HQ countries, e.g. France, Germany, United Kingdom; or one country when comparing verticals]
- Minimum employees: [e.g. 2,000]
- What I sell: [one line, e.g. OT and device security software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. CrowdStrike, Palo Alto Networks; skip if saved in setup]
- Current coverage (optional): [reps per segment, e.g. 1 rep in the UK, none in France]

STEPS
1. Use Draup's exact names. Say the mode: countries (one vertical) or verticals (one country); each country or industry is a "segment". Map What I sell to its 1–3 main workloads (types of work, e.g. Cybersecurity).
2. Per segment, count companies with that primary industry, HQ there and [Minimum employees]+ staff (names only). Over 100? Check single rows at positions 250 and 500 and report the band.
3. Repeat step 2 adding "active in my workloads": the relevance measure.
4. Per segment, pull the top 10 by revenue in full, showing only my competitors' products (names, not usage): revenue and year, description.
5. For the top 3 accounts per segment (top 5 when comparing 2), check my competitors' products with usage strength. Only High or Medium counts as in use; say how many were Low only.
6. Flag misfiled, distributor, holding or private-equity, possibly inactive and subsidiary rows, and companies that sell what I sell; leave them out of totals.
7. Score (editable): workload-active share 35%, top-10 revenue 25%, rival-in-use share of those checked 20%, accounts 20%. With coverage, divide by reps plus one and say if the winner changes.
8. For the winner's top clean account, pull its top 3 executives in the function closest to What I sell and its top 90-day news item; if it's a mega-cap, also name the best mid-size account.

OUTPUT
- Bottom line: 2 sentences — the segment to staff next and what it means for [What I sell].
- Recommended next step: the decision, its owner and a date; then the first account to open, with a named person (step 8) and one dated fact. If none, say so.
- "Segments compared": Segment | Accounts (all / in my workloads) | Rival in use (of checked) | Top-10 revenue (USD B, FY) | Score (per rep).
- "Where to add capacity": winner and runner-up, 2 number-backed reasons each.
- Detail: top 5 logos per segment; Low-only rival detections; what's missing (removed rows, no workforce figure, HQ elsewhere); rubric.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Totals cover each segment's top 10, never the whole market.
- A rival in use at over 70% of accounts checked no longer separates segments; lean on the workload count.
- Same size cut in every segment; label fiscal years.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: which of [Compare] (2–5 countries for [Vertical], or 2–4 industries in one country) gets the next rep for [What I sell], scored on workload-active accounts, rivals at High or Medium usage, revenue and coverage.
```

### Follow-ups

- Rerun with Minimum employees at 1,000 for the two smallest segments.
- Change the weights: workload activity 50%, revenue 30%, rival presence 20%.
- Check rival usage for accounts 4–10 in the winning segment.
- List well-known companies missing from [Segment] (no workforce figure or HQ elsewhere) so I can add them by hand.

### Tips

- Compare segments with the same size cut; a lower threshold in one makes it look bigger than it is.
- Draup lists many rival products at low usage almost everywhere. Only High or Medium usage counts as a rival in place, so the rival column stays meaningful.
- Use verticals mode when the real question is "which industry in my country", not "which country"; add current coverage so the per-rep score can change the answer.

## Which cities to base reps and events

- **id:** `leaders-metro-heatmap`
- **What you get:** A ranked map of the metros in one country where an industry's people, big local employers and the employers active in your workloads concentrate, telling you where to base reps, run events, or assign a named-account owner instead.
- **Use it when:** Deciding where to hire the next field rep, where to hold a roadshow or dinner series, or which city a new office should cover. Use "Which region gets the next rep" first if you're still choosing the country.
- **Best for:** Sales Leader & RevOps, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Insurance); Country (e.g. United States of America); Metros to compare (optional) (e.g. Hartford, Dallas, Chicago); What I sell (e.g. claims-automation software)

### Detailed prompt

```text
Act as my field-sales and events strategist. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Country: [in full, e.g. United States of America]
- Metros to compare (optional): [up to 5, e.g. Hartford, Dallas, Chicago; default the top 5]
- What I sell: [one line, e.g. claims-automation software; skip if saved in setup]

STEPS
1. Use Draup's exact industry, country and metro names; map What I sell to its workloads. If the industry returns zeros, try its parent and name it.
2. Pull Draup's metro map for the industry (a fixed top 50 worldwide, ranked by a relative strength index); keep metros in [Country], plus mine.
3. For the top 5 metros (or up to 5 of mine), pull the industry's top local employers there (up to 50 each) with approximate local headcount.
4. For the same metros, list companies in the industry with a presence there, 1,000+ staff and activity in my workloads (names only, up to 50). That count is the relevance measure.
5. Per metro: local headcount of the top 50, employers with 1,000+ local staff (editable default), top-2 share, 3 biggest employers. Flag employers from another primary industry; don't let them drive the verdict.
6. Classify: Anchor cluster (top 2 hold over 50%; say whether they are HQs or plants), Broad territory (8+ employers with 1,000+ local staff), Mixed. A metro whose anchors are plants of companies run from elsewhere is a site-visit city, not a rep base.
7. For the lead metro's biggest relevant employer, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — where to base people and what it means for [What I sell].
- Recommended next step: the decision, its owner and a date; then the first account, with a named person (step 7) and one dated fact. If none, say so.
- "Heatmap": Metro | Local headcount (approx.) | Employers 1,000+ / in my workloads | Type | 3 biggest employers. By relevance, then strength.
- "Where to put people and events": up to 3 rep bases (5 accounts each) and 2 event cities (6 accounts to invite).
- Detail: named-account metros with the 2 accounts that justify a named owner; flagged employers; strength index.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- The strength index is relative; never call it headcount. Write "approx." beside every local headcount.
- These are people, not budget holders: where the HQ is elsewhere, say where decisions are likely made.
- "Who to invite" means the account, not a named person.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Every count and total applies all my conditions.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Parent companies only; merge subsidiaries and alternate names of one company.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: rank the top 5 metros in [Country] for [Vertical], with big local employers, employers active in my workloads and whether each is a broad territory or a few HQ accounts, for [What I sell].
```

### Follow-ups

- For [Metro], which of these employers run a capability centre or HQ there?
- Add two more metros: [Metro], [Metro].
- Who leads [Business function] at the 5 accounts in my top rep-base metro?
- Turn the events section into a 3-city roadshow plan with invite lists.

### Tips

- A metro full of 1,000–3,000-person regional sites often makes a better volume territory than one with two giant headquarters.
- Run it for two industries you sell into and overlay the results to find cities that serve both.
- Check where the HQ sits before you staff for a big local employer; the buyer may be in another city.

## Sort my book into coverage tiers

- **id:** `leaders-book-segmentation`
- **What you get:** Up to 20 accounts sorted into Strategic, Growth, Maintain and Deprioritise on an editable potential-versus-momentum rubric that scores your own workloads and rivals, with the coverage model for each tier and the flags behind every placement.
- **Use it when:** Setting coverage for a new fiscal year, rebalancing books between reps, or deciding which accounts get a named AE, a pooled team or a digital motion. Use "Tier my accounts by fit and timing" instead when the question is who might buy this quarter.
- **Best for:** Sales Leader & RevOps, Account & Customer Success Manager, Account Executive
- **Time:** 4–6 min
- **Inputs:** Accounts (e.g. boeing.com, airbus.com, rtx.com, northropgrumman.com, l3harris.com); What I sell (e.g. OT and device security software); My competitors (optional) (e.g. CrowdStrike, Palo Alto Networks); Current customers (optional) (e.g. l3harris.com); Reps available (optional) (e.g. 3)

### Detailed prompt

```text
Act as my sales operations lead designing account coverage. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Accounts: [up to 20 websites, 10 per pass, e.g. boeing.com, airbus.com, rtx.com, l3harris.com]
- What I sell: [one line, e.g. OT and device security software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. CrowdStrike, Palo Alto Networks; skip if saved in setup]
- Current customers (optional): [websites, e.g. l3harris.com]
- Reps available (optional): [e.g. 3]

STEPS
1. Map What I sell to its 1–3 main workloads. Look up the accounts by website, 10 per lookup, showing only my competitors' products. If a website returns nothing, look it up by name once and show the match and its score; ask if only suggestions return. Never drop an account silently.
2. Take revenue and year, revenue growth, hiring %, workforce growth, workforce and rival products listed (names only, usage unchecked).
3. Per account, pull 12-month postings in my workloads (keep only those) and work out postings per 1,000 employees.
4. POTENTIAL 0–50 (editable): workload postings per 1,000 — top third 20, middle 12, else 4; revenue — over $20B 15, $5–20B 10, $1–5B 6, else 2; rival at High or Medium 10, listed but unchecked 5 (check usage for the top 5 by Potential; current customers: risk flag); Opportunity Index 5.
5. MOMENTUM 0–50 (editable): revenue growth — over 8% 20, 3–8% 14, 0–3% 8, else 3; hiring % — over 10% 15, 6–10% 10, 3–6% 5, else 1; workforce growth — over 3% 15, 0–3% 10, else 3. Missing value = half points, flagged; revenue moving over 25% in a year = possible merger or spin-off, score 8.
6. Segment (editable): Strategic = Potential 30+ and Momentum 25+; Maintain = Potential 30+ only; Growth = Momentum 25+ only; else Deprioritise. Customers stay at Maintain or above. Over half in one segment? Re-segment by rank (top 30%, next 40%, rest) and say so.
7. For the top Strategic account, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the shape of the book and what it means for [What I sell].
- Recommended next step: the coverage decision, its owner and a date; then the first account, with a named person (step 7) and one dated fact. If none, say so.
- "Segments": Account | Segment | Potential | Momentum | Strongest driver. Strategic first.
- "Coverage model": Strategic = named AE and account plan; Growth = pooled AEs; Maintain = AM-led; Deprioritise = digital or partner-led. Counts per tier; flag over 5 Strategic per rep.
- Detail: postings and rivals per account; flags; rubric.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Opportunity Index is Draup's own rating; never quote it as a company fact.
- Flagged accounts reach Strategic only as "Strategic (confirm)".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: sort [Accounts] into Strategic, Growth, Maintain or Deprioritise for [What I sell], scoring revenue, postings in my workloads, rivals installed and growth, with a coverage model per tier.
```

### Follow-ups

- Check usage strength (High, Medium, Low) of my rivals at the 5 Strategic and Maintain accounts.
- Change the rubric: workload postings 30, revenue 10, and rerun.
- Split the Strategic and Growth accounts across [Reps available] reps, balanced on Potential.
- Give one dated why-now signal from the last 60 days for each Strategic account.

### Tips

- Run it after propensity tiering: tiering says who might buy now, segmentation says who deserves a named owner all year.
- When a rival shows up at nearly every account, the workload-postings score is what separates them; ask for usage strength before calling an account contested.
- Private companies often lack revenue in Draup; score them by hand rather than letting them fall to Deprioritise.

## Board slides: where we hunt next quarter

- **id:** `leaders-where-to-hunt-slide`
- **What you get:** Three board-ready slides for one industry — the market in numbers, the 8 accounts to hunt next quarter chosen on fit with what you sell, and what the team needs — with speaker notes and every number dated and sourced.
- **Use it when:** Preparing a quarterly business review, a board update or a sales kick-off section on where the team will hunt next quarter. Use "Next quarter's target accounts" when you need a working list for reps rather than slides.
- **Best for:** Sales Leader & RevOps, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Insurance); Territory (optional) (e.g. United States of America); What I sell (e.g. claims and underwriting data services); My competitors (optional) (e.g. Guidewire, Duck Creek); Our position (optional) (e.g. 4 customers in the vertical, 1 partner)

### Detailed prompt

```text
Act as my chief of staff to the sales leader, building board slides. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Territory (optional): [e.g. United States of America; default: my territory from setup; narrows the account picks — industry totals stay global]
- What I sell: [one line, e.g. claims and underwriting data services; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Guidewire, Duck Creek; skip if saved in setup]
- Our position (optional): [e.g. 4 customers in the vertical, 1 partner]

STEPS
1. Use Draup's exact industry and territory names; map What I sell to its workloads. If the industry returns zeros, try its parent and name it.
2. Pull the industry's revenue and growth (Draup may give no year; say so).
3. Pull industry priorities; keep the 3 most relevant to [What I sell] (examples are undated; say so).
4. Pull the top outsourcing buyers and fastest-growing companies by workforce (fixed top 50s, worldwide); keep growers with 1,000+ staff, in [Territory].
5. Run one 90-day news search in the industry and territory (acquisitions, expansions, partnerships, investments, leadership changes); review up to 20 items.
6. Shortlist 12 candidates (two-list companies first) and check them in one company list by exact name, showing only my competitors' products and whether each is active in my workloads. Pick 8: workload-active first, then two-list, then the strongest single reason. For the top 3 picks, check rival usage (only High or Medium counts); for the rest write "rival listed, usage not checked".
7. For the top pick, pull its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where we hunt and what it means for [What I sell].
- Recommended next step: the first board ask and its owner; then the first account, with a named person (step 7) and one dated fact. If none, say so.
- Slide 1 "[Vertical]: the market": one-sentence headline, revenue and growth, 3 priorities with what each means for us.
- Slide 2 "Where we hunt next quarter": Account | Why it fits (workloads, rival) | Why now (dated) | Likely owner (title). 8 rows.
- Slide 3 "What we need": 3 asks, each tied to a slide-2 fact and Our position.
- Detail: speaker notes (60 words per slide); sources and caveats.
- Gaps: what Draup didn't have, to ask in discovery.
- One-slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Use growth-list companies only from the core business; mark brokers, health groups and agencies.
- If an industry total is driven by one company (over a third), name it.
- Why-now counts only if dated in the last 90 days with the company as actor.
- Industry totals are global estimates; never add them to company figures.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 500 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: 3 board slides on [Vertical] for [What I sell] — market numbers, 8 accounts to hunt next quarter (each active in my workloads, with a dated why-now) and the asks.
```

### Follow-ups

- Turn slide 2 into a one-page brief per account for the team.
- Redo the slides for [Second vertical] so I can compare.
- Add a fourth slide: which services rivals lead in this industry and where we rank.
- Shorten everything to one slide for the board pack.

### Tips

- Accounts that appear on two lists and are active in your workloads usually make a stronger board story than the biggest logo.
- Keep the speaker notes; they hold the caveats the slide can't.
- If you share these slides outside the company, check your Draup licence before publishing Draup data externally.

## Next quarter's target accounts, ranked by triggers

- **id:** `leaders-pipeline-targets`
- **What you get:** A territory-wide list of accounts ranked by distinct triggers in the last 90 days, activity in the work you sell and rival presence, with one dated why-now each, the person to call at the top account, and the off-list companies acting in your territory.
- **Use it when:** Setting next quarter's pipeline-generation targets for SDRs and AEs in one territory, or planning a campaign wave. Use "Board slides: where we hunt next quarter" to present the plan, and "Which accounts each rep works this week" for named books.
- **Best for:** Sales Leader & RevOps, SDR / BDR, Account Executive, Marketing & ABM
- **Time:** 8–12 min
- **Inputs:** Vertical (e.g. Automotive); Territory (optional) (e.g. Germany); Minimum employees (e.g. 5,000); What I sell (e.g. software-defined-vehicle engineering services); My competitors (optional) (e.g. Capgemini Engineering, Bertrandt); Accounts to exclude (optional) (e.g. bmwgroup.com)

### Detailed prompt

```text
Act as my pipeline strategist for a territory. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Automotive]
- Territory (optional): [HQ country in full, e.g. Germany; default: my territory from setup]
- Minimum employees: [e.g. 5,000]
- What I sell: [one line, e.g. software-defined-vehicle engineering services; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Capgemini Engineering, Bertrandt; skip if saved in setup]
- Accounts to exclude (optional): [websites in active deals, e.g. bmwgroup.com]

STEPS
1. Use Draup's exact names; map What I sell to its workloads.
2. List the territory: primary industry [Vertical], HQ in [Territory], [Minimum employees]+ staff (names only, up to 50, by revenue), then again adding "active in my workloads"; mark those and remove exclusions.
3. For the top 20 workload-active accounts by revenue, run one 90-day news search per account, filtered to its Draup name, with a broad question ("[Account] leadership changes, expansions, partnerships, acquisitions"); do 10, then offer the next 10. Then one search across [Vertical] and [Territory] for off-list actors; if one company fills over half, rerun without it.
4. Keep items where the account is the actor and the event concerns [Territory]; drop look-alike tags (e.g. "target company" in someone else's deal); merge repeats; off-list actors go to "Acting in the territory".
5. For the 10 accounts with most trigger types, pull full rows by exact name with only my competitors' products: hiring %, 90-day postings. For the top 5, check rival usage (only High or Medium counts; say how many were Low).
6. Score (editable): each trigger type 20 (max 60); workload-active 20; rival at High or Medium 10, listed but unchecked 5; hiring % over 8% adds 10. Act this month 60+, Next quarter 30–59, Watch under 30. If over half share a tag, re-tag by rank (top 30%, next 40%, rest) and say so.
7. For the top account, pull its top 3 executives in the function closest to What I sell. If it's a mega-cap, also name the best mid-size account.

OUTPUT
- Bottom line: 2 sentences — accounts per tag and what it means for [What I sell].
- Recommended next step: who to contact first (step 7), what to do, and the dated trigger. If none, say so.
- "Target list" (top 10): Account | Triggers (type, date) | In my workloads / rival | Tag | Why now.
- Detail: acting in the territory; searched accounts with no triggers (beyond the top 20 write "not searched"); dropped items; likely owner title; a split by rep if I give team size.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Job cuts, restructuring or site sales trigger only cost-out, transformation or services offers.
- Board and regional sales appointments count only in my buying area.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Size limits drop companies with no workforce figure; say so.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: for the top 20 workload-active [Vertical] accounts in [Territory] ([Minimum employees]+ staff), search 90-day news per account, rank by distinct triggers and rival usage, with a dated why-now each for [What I sell].
```

### Follow-ups

- Write a 70-word opener for each Act-this-month account, tied to its trigger.
- Add the 11th to 20th accounts and score them the same way.
- Who leads [Business function] at my top 5 accounts?
- Rerun with only partnership and vendor-selection news.

### Tips

- Accounts with two different trigger types are usually worth more than one account with five articles on the same story.
- Territories over 100 accounts: rank by workload activity first, then check news for the top 20; one territory-wide search lets one big name crowd out everyone else.
- The "Acting in the territory" list often holds the best surprises: foreign companies building local sites and private groups your size limit missed.

## Brief reps on a new industry

- **id:** `leaders-vertical-enablement`
- **What you get:** A rep-ready brief on an industry you're entering: the words to use, what it funds in your function, who buys and how the function is organised at a lead account, where your rivals already sit, the services firms you'll meet and 5 discovery questions.
- **Use it when:** Onboarding reps to a new industry, launching a vertical team, or preparing a sales kick-off session. Use "Build an industry point of view" when you need a narrative for customers rather than a brief for your team.
- **Best for:** Sales Leader & RevOps, Account Executive, SDR / BDR, Presales & Solutions
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Energy & Utilities); Reference account (e.g. nationalgrid.com); Business function (e.g. IT); What I sell (e.g. asset-data and field-service modernisation services); My competitors (optional) (e.g. IBM Maximo, Accenture)

### Detailed prompt

```text
Act as my sales enablement lead. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Energy & Utilities]
- Reference account: [website of a typical target, e.g. nationalgrid.com]
- Business function: [where we sell, e.g. IT]
- What I sell: [one line, e.g. asset-data and field-service modernisation services; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. IBM Maximo, Accenture; skip if saved in setup]

STEPS
1. Use Draup's exact names; map What I sell to its workloads. Find the reference account by website (parent; if nothing returns, try its name once and show the match score). A sub-industry returning zeros: try its parent.
2. Pull industry priorities; keep the 6 most relevant to [What I sell] in [Business function], plus 2 budget-shaping ones from other functions. If they come back empty, say so first, then build "What they're funding" from the 3 newest dated [Business function] priorities at [Reference account] and at the industry's 2 largest employers, labelled "company proof, not industry-wide".
3. Pick 10 industry terms from the priority text and define each in one line.
4. Pull growing technologies (a fixed top 50); drop generic tools (office suites, chat assistants, browsers); keep 8, marking my competitors'.
5. Pull the top outsourcing vendors (a fixed top 50); drop agencies, staffing and inspection firms; keep 8, marking my competitors.
6. At the reference account: read full titles of executives in [Business function] (up to 2 pages of 10) to see how the function is organised; check its stack for my competitors' products with usage; pull its top 90-day news item.

OUTPUT
- Bottom line: 2 sentences — what this industry buys and what it means for [What I sell].
- Recommended next step: the enablement action, owner and date; then a first call at [Reference account] with a named person (step 6) and the dated news fact. If none, say so.
- "What they're funding": Priority | What it means for [What I sell] | Company example (dated if company proof). Top 6.
- "Who buys": Title pattern | Likely role | Example title at [Reference account], plus one line on how the function is organised.
- Detail: 10 words to know; technology in play with rival ratings; services firms we'll meet; 5 discovery questions with good answers; a 60-word opener.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Use title patterns in the brief; name people only in the next step.
- Industry priorities are undated themes; company proof carries its quarter.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Rivals count only at High or Medium usage (say how many were Low). Software: High in my workloads Red, Medium or newly detected Amber, else Green. Services, by share of active engagements in my workloads: 30%+ Red, 10–29% Amber, under 10% Green. No "Generic" rows.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 500 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: brief my reps on [Vertical] for [What I sell] — 10 terms, the top priorities in [Business function], buyer titles at [Reference account], rivals in play and 5 discovery questions.
```

### Follow-ups

- Turn this into a 10-question quiz for the reps.
- Redo "Who buys" with [Second reference account] to check the pattern holds.
- Write a 3-email sequence for the economic-buyer title in this brief.
- Which of the services firms listed are partners we could recruit?

### Tips

- Pick a reference account that looks like your typical target, not the largest company in the industry; if Draup has no industry priorities, it also becomes your main proof.
- Read the full titles: in many regulated industries IT is organised by business line, which changes who your rep should call.
- Refresh the brief each half-year; priorities shift faster than reps expect.

## Rewrite our ICP from best customers

- **id:** `leaders-icp-refinement`
- **What you get:** The traits your 5–10 best customers share in Draup — industry, HQ, size, providers, activity in the work you sell — turned into a tested look-alike definition with the number of new companies it returns, the trade-off of each loosening, and the first look-alike to approach.
- **Use it when:** Rewriting the ideal customer profile before planning, a new campaign or a territory carve. Use "Find look-alikes of your best customer" when you start from one account.
- **Best for:** Sales Leader & RevOps, Marketing & ABM, Account Executive
- **Time:** 4–6 min
- **Inputs:** Best customers (e.g. progressive.com, allstate.com, travelers.com, thehartford.com, chubb.com); What I sell (e.g. claims-automation software); My competitors (optional) (e.g. Guidewire, Duck Creek); Territory (optional) (e.g. United States of America)

### Detailed prompt

```text
Act as my go-to-market strategist refining an ideal customer profile. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Best customers: [5–10 websites, e.g. progressive.com, allstate.com, travelers.com, thehartford.com, chubb.com]
- What I sell: [one line, e.g. claims-automation software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Guidewire, Duck Creek; skip if saved in setup]
- Territory (optional): [HQ country or region for look-alikes, e.g. United States of America; default: my territory from setup]

STEPS
1. Map What I sell to its 1–3 main workloads and say which. Look up all customers by website (exact) in one company list. If a row shows a parent, fund, venture arm or unit, look up the parent and ask me which to use. If a website returns nothing, look it up by name once and show the match and its score.
2. For each: primary industry, sub-industries, HQ country, workforce, revenue, growth, service providers, hiring %, and whether it's active in my workloads.
3. Find shared traits: an industry or sub-industry held by 80%+ (editable), HQ countries, workforce and revenue range (rounded), providers at 60%+, workload activity.
4. Write the look-alike definition, including "active in my workloads" if 80%+ share it. Count matches in [Territory] if given (names only, up to 100) minus the customers.
5. Test up to 2 loosenings one at a time (drop the provider, widen the size band, add a neighbouring sub-industry), counted the same way. If I named competitors, test once adding "runs a rival product" (presence only; usage not checked, say so).
6. Recommend the tightest definition returning 15–100 new companies (editable). Pull its top 10 by revenue in one detail page.
7. For the first look-alike, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the recommended ICP and what it means for [What I sell].
- Recommended next step: who owns the ICP update and by when; then the first account to open, with a named person (name and title from step 7) and one dated fact. If none is found, say so.
- "Definitions tested": Version | Conditions | New companies | What it adds or loses.
- "Recommended ICP": the conditions in plain words for a planning doc, plus 2 traits to qualify by hand.
- Detail: shared traits (n of N; Strong 80%+, Moderate 60–79%); customer data check; first 10 look-alikes with why each matches.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Never count the customers, their subsidiaries or sister companies as look-alikes.
- Name well-known companies missing for lack of a workforce figure (e.g. large mutuals) and offer to add them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Every count and total applies all my conditions.
- Size limits drop companies with no workforce figure (often private firms or mutuals); say so.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Parent companies only; merge subsidiaries and alternate names of one company.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: find what [Best customers] share in Draup, including activity in my workloads, turn it into a look-alike definition for [What I sell], count the new companies it returns and name the first to approach.
```

### Follow-ups

- Run a full ICP list with the recommended definition, 10 rows at a time.
- Tier the first 10 look-alikes by fit and timing for what I sell.
- Repeat with my 5 most recent losses to see which traits they lack.
- Write the ICP as a one-paragraph brief for SDRs.

### Tips

- Feed it customers that renewed or expanded, not just the biggest logos; the traits are sharper.
- Some websites resolve to a venture arm or regional unit; the customer check catches it, so read that table first.
- If the tight version only finds a handful of new companies, the market for that profile is small — that's a finding, not a failure.

## Which accounts each rep works this week

- **id:** `leaders-coverage-check`
- **What you get:** Your pasted accounts and owners checked against real triggers in the window, tied to what you sell, grouped by owner, with the 5 actions for this week, the named person behind the top action, and which reps' books have gone quiet.
- **Use it when:** Before a weekly or monthly team call, when you need to point reps at the accounts that just changed. Use "Weekly trigger sweep for my book" for your own accounts without owners or coaching notes.
- **Best for:** Sales Leader & RevOps, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Accounts and owners (e.g. costco.com – Rep A; starbucks.com – Rep A; fedex.com – Rep B; att.com – Rep B; visa.com – Rep C; mastercard.com – Rep C); What I sell (e.g. observability and IT operations software); My competitors (optional) (e.g. Datadog, Dynatrace); Window (optional) (e.g. last 30 days)

### Detailed prompt

```text
Act as my sales manager running a pipeline and coverage review. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Accounts and owners: [up to 15 lines of website – owner, e.g. costco.com – Rep A; fedex.com – Rep B]
- What I sell: [one line, e.g. observability and IT operations software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Datadog, Dynatrace; skip if saved in setup]
- Window (optional): [default last 30 days; up to 90]

STEPS
1. Resolve all accounts by website (exact) in one short lookup; if a website returns nothing, look it up by name once and show the match and its score; ask if only suggestions return. Never drop an account silently. Keep each owner beside the account.
2. Pull one news feed for all accounts in the window, material categories only (leadership, acquisitions, partnerships and vendor deals, expansions and new centres, investments, layoffs), 2 pages. If one account fills over a third of items, pull again without it.
3. For accounts still under 2 items, pull their top-ranked signals and keep items dated inside the window.
4. Drop noise and items where the account isn't the actor (it advised on, supplied or was merely named in someone else's deal). Merge repeats.
5. Tag each trigger: Strong (opens a project or budget), Useful (a reason to call), Context.
6. Rank by strength, then recency; group by owner. If I named competitors, check the stacks of the top 3 action accounts and rate them.
7. For action 1, pull the account's top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where the team should spend this week and what it means for [What I sell].
- Recommended next step: action 1 — who to contact (name and title from step 7), what to do, and the dated trigger. If none is found, say so.
- "This week's 5 actions": Account | Owner | Trigger (what, date) | Strength | Action.
- "By owner": Owner | Strong | Useful | Quiet accounts | Coaching note.
- Detail: quiet accounts with their latest item's date; not resolved; rival ratings; coverage flags (3+ Strong for one owner, or a whole book quiet); sources.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Every trigger needs a date inside the window; drop anything you can't date.
- A trigger counts once per account, however many outlets covered it.
- Don't pull leadership-move histories for every account.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Rivals count only at High or Medium usage (say how many were Low). Software: High in my workloads Red, Medium or newly detected Amber, else Green. Services, by share of active engagements in my workloads: 30%+ Red, 10–29% Amber, under 10% Green. No "Generic" rows.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: for [Accounts and owners], find triggers in [Window] that matter to [What I sell], group them by owner, rank this week's 5 actions with a named contact for action 1, and list quiet books.
```

### Follow-ups

- Draft a 60-word note to each owner with their top action.
- Write the opener for action 1, tied to the trigger.
- Extend the window to 90 days for the quiet accounts.
- Rebalance: suggest moving 2 quiet accounts from the busiest owner to the quietest.

### Tips

- Paste the owner next to each website; the by-owner view is what makes this a management tool rather than a news digest.
- A big brand can dominate a combined news feed; the per-account check stops quieter accounts being missed.
- Use the coaching notes in one-to-ones rather than reading the full table in the team call.
