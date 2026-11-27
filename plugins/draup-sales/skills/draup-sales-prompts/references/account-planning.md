# Account planning and expansion

Account plans, entry points, risk checks, QBR prep and territory tiering.

## Draft an account plan

- **id:** `plan-account-plan`
- **What you get:** An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- **Use it when:** Annual or half-year account planning, or when you inherit a strategic account.
- **Best for:** Account & Customer Success Manager, Account Executive, Sales Leader & RevOps
- **Time:** 6–10 min
- **Inputs:** Company (e.g. bmw.com); What I sell (e.g. supply-chain planning software); Business function (e.g. Supply Chain); Already buy from us (optional) (e.g. demand planning for two regions); Our goal (optional) (e.g. double ARR in 12 months); Competitor (optional) (e.g. Kinaxis, o9 Solutions)

### Detailed prompt

```text
Act as my strategic account planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. bmw.com]
- What I sell: [One line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Business function: [The function that buys from us, e.g. Supply Chain]
- Already buy from us (optional): [e.g. demand planning for two regions]
- Our goal (optional): [e.g. double ARR in 12 months]
- Competitor (optional): [Up to 3, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Snapshot: profile, latest revenue (USD at Draup's rate), Opportunity Index.
3. Strategy: top 5 [Business function] priorities, newest first, with source, quarter and workloads.
4. Buying committee: top 8 leaders in [Business function] by title and budget control (up to 3 pages of 10). If no economic buyer (C-level, EVP, "Head of") appears, search once more for Chief, EVP or CIO titles.
5. Incumbents: products on those workloads (strength, last seen), top providers in the function, and any [Competitor] product anywhere in the stack. Rate [Competitor]: Red for High usage in the workloads I sell into; Amber for Medium usage there or anything newly detected in 12 months; otherwise Green, still listed.
6. Risks: senior exits in 6 months (by workload; state the latest move date), layoffs in 90 days, [Competitor] products newly detected in 12 months.
7. Timing: the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the prize and the first play.
- Recommended next step: one person from step 4 (name and title), what to do, and why now (the dated item from step 7 or another dated fact). If none turned up, say so.
- "Expansion plays" (top 3, building on what they buy): Play | Evidence and date | Builds on | Likely owner. A High-usage [Competitor] product in the play's workload makes it a displacement; say so.
- "Buying committee" (top 5): Name | Full title | Budget control | Why they matter.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail, each part with its source and date: Snapshot; "Their strategy in their own words" (Priority | Quarter | Workloads); Incumbents (Workload | Products | Providers | [Competitor] rating); Risks (3 dated); 90-day plan toward [Our goal] (two actions per 30 days, owner role each); SWOT only if I ask.

RULES
- In banking and consulting, VP and SVP are mid-level.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell. Where a workload is needed and I gave a function, map it to its 1–3 main Draup workloads and say which.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 500 words including tables.
```

### Quick version

```text
Bottom line, first play and a named contact with a dated why-now first. Then an account plan for [Company]: [Business function] priorities, buying committee, incumbents and installed [Competitor] products, ranked plays for [What I sell], risks, 90-day plan.
```

### Follow-ups

- Add the short SWOT section.
- Turn the 90-day plan into a mutual action plan I can share with my champion.
- Run a renewal risk check on this account.
- Write a 120-word executive summary of this plan for my VP.

### Tips

- Paste what they already buy and your goal. The expansion plays and 90-day plan get much sharper.
- Name the competitors you meet. A rival installed with High usage in your workload turns an expansion play into a displacement.

## Best entry points: expand or new

- **id:** `plan-entry-points`
- **What you get:** The five best ways in for what you sell, each marked Expand (we already serve it) or New, with dated evidence, incumbents, any installed competitor and the likely owner.
- **Use it when:** You know the account (often an existing customer) and need a concrete next deal to work on. Use plan-account-plan instead for a full plan.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. bmw.com); Business function or Workload (e.g. Supply Chain); What I sell (e.g. supply-chain planning software); Already deployed (optional) (e.g. demand planning in Europe); Competitor (optional) (e.g. Kinaxis, o9 Solutions)

### Detailed prompt

```text
Act as my pursuit strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. bmw.com]
- Business function or Workload: [e.g. Supply Chain or Demand Management]
- What I sell: [One line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Already deployed (optional): [What we already run there, e.g. demand planning in Europe; blank for a prospect]
- Competitor (optional): [e.g. Kinaxis, o9 Solutions]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Map [Business function or Workload] to the 1–2 workloads closest to [What I sell] and say which. Pull Draup's potential initiatives for the account, always narrowed to those workloads (if nothing comes back, to the function; never unlimited).
3. Drop initiatives unrelated to [What I sell], templates that don't fit the account's industry and, if it sells technology, initiatives about its own products. Mark any initiative we already serve (from Already deployed) "Expand", the rest "New". Rank by fit, then by how recent the evidence is.
4. For the top 5, note the initiative, its evidence (source and date), incumbent tech, and only providers that plausibly deliver this work.
5. Check the whole tech stack for [Competitor] products in the same workloads. Rate [Competitor]: Red for High usage in the workloads I sell into; Amber for Medium usage there or anything newly detected in 12 months; otherwise Green, still listed.
6. Pull leaders in the same function (10 per page, up to 3 pages) and match up to 2 per entry point by workload or title.
7. Timing: the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the best way in and why now.
- Recommended next step: one person from step 6 (name and title), what to do, and why now (the step-7 item or another dated fact). If none turned up, say so.
- "Entry points": # | Initiative (Expand or New) | Evidence and date | Incumbents (tech; providers) | Likely owner.
- "Competitor in these workloads": Product | Maker | Usage | Last seen | Rating. Write "none found" if empty.
- "Lead with": the single best entry point and why, in two sentences.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Dropped as unrelated" in one line, so I can bring any back.

RULES
- Owners are matched by function and workload, not confirmed; label them "likely".
- Providers here are linked to the initiative, not confirmed: say "linked" and leave out firms that clearly don't do this work (publishers, architects, recyclers).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- If [Company] sells technology, drop priorities and tools about its own products.
- Label inferences (buyer role, intent, fit) "likely".
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 430 words including tables.
```

### Quick version

```text
Bottom line and next step (named owner, dated why-now) first. Find the top 5 entry points at [Company] for [What I sell] in [Business function]: initiative, Expand or New (we run [Already deployed]), dated evidence, incumbents, [Competitor] installed, likely owner.
```

### Follow-ups

- Write a discovery question for each entry point, citing its evidence.
- Which providers would we compete with on entry point 1, and how strong are they here?
- Turn 'Lead with' into a 100-word email to the person in the next step.

### Tips

- For a customer, say what you already run there. The answer then separates expansion from new business.
- Name the competitors you meet. An installed rival in the same workload changes the play from land to displace.
- If you save your solution offering in the Draup platform, Draup can also surface entry points from leadership moves and intent signals.

## Where they're building teams

- **id:** `plan-expansion-footprint`
- **What you get:** The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.
- **Use it when:** You're planning where to expand inside a customer, or which regional team should own it.
- **Best for:** Account & Customer Success Manager, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. walmart.com); Business function (e.g. Supply Chain); What I sell (e.g. warehouse automation software)

### Detailed prompt

```text
Act as my account-expansion analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [e.g. Supply Chain, IT, ER&D]
- What I sell: [One line, e.g. warehouse automation software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull key locations for [Business function]: metro, country, indicative workforce, 12-month postings, growth index and site tags (HQ, capability centre). Keep the top 10 by postings, plus every capability-centre row.
3. Infer likely new sites: metros with real postings but little or no workforce. Say they're inferred.
4. Pull net hiring by metro from talent flow (hires minus exits) and state the months covered.
5. People and timing: pull the top 3 leaders in [Business function], preferring those based in the fastest-growing metro, and the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — where they're building and where [What I sell] should land.
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Top metros": Metro | Tag | Postings (12 mo) | Growth index | Net hiring (window).
- "Why this matters for [What I sell]": 3 bullets on where to land or expand and which regional team should own it.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Capability centres and likely new sites" (Metro | Country | Tag or "inferred new" | Postings) and "Fastest growing" (3 metros with the highest growth index among those with 100+ workforce; editable default).

RULES
- Always run with one business function.
- Site workforce is approximate and varies between pulls; treat it as indicative and lean on postings.
- The growth index is postings divided by workforce, so it runs high for small sites; say so when one tops the list.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Label inferences (buyer role, intent, fit) "likely".
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 400 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Where is [Company] building [Business function] teams? Top 10 metros by 12-month postings with growth index, HQ or capability-centre tags, net hiring (state the window) and likely new sites.
```

### Follow-ups

- Run the same for [another Business function] and compare.
- Who are the leaders based in the fastest-growing metro?
- What roles are they hiring at the likely new site?

### Tips

- A metro with fresh postings but little workforce is often the earliest sign of a team being built.
- Talent-flow numbers lag by a few months. Use job postings for the most recent picture.

## Renewal risk check (red, amber, green)

- **id:** `plan-risk-check`
- **What you get:** A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- **Use it when:** About 90 days before a renewal, or when a deal goes quiet. Use plan-qbr-prep instead the week before a business review, and signals-change-log for a monthly what-changed log.
- **Best for:** Account & Customer Success Manager, Account Executive, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. walmart.com); Business function (e.g. Supply Chain); Sponsor name and title (e.g. Jane Doe, VP Supply Chain Systems); Competitor (e.g. Blue Yonder, Manhattan Associates); What I sell (e.g. warehouse automation software)

### Detailed prompt

```text
Act as my customer-success risk analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [Our sponsor's function, e.g. Supply Chain]
- Sponsor name and title: [e.g. Jane Doe, VP Supply Chain Systems — a title alone may match several people]
- Competitor: [Products or firms we lose to, e.g. Blue Yonder, Manhattan Associates]
- What I sell: [One line, e.g. warehouse automation software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Sponsor: look for [Sponsor name] among leaders in [Business function] (up to 3 pages of 10) and in recent exits. Red: left. Amber: title or unit changed. If not found, say "not found in Draup", not "left".
3. Senior exits in [Business function], 6 months, narrowed by its main workloads. Red: the sponsor's level or above. Amber: other director-plus. State rows checked and the latest move date.
4. Layoffs, 90 days. Red: touching [Business function] or over 5% of staff. Amber: other. Workforce growth (talent-flow window; state the months): Red below −3%, Amber −3% to 0%. Revenue growth, latest fiscal year: Red below −5% without a divestment, Amber −5% to +2%.
5. Competitor tools: check the whole tech stack for any product made by [Competitor], whatever area it's filed under. Red: a [Competitor] product with High usage in the same workloads as What I sell. Amber: Medium usage in those workloads, or newly detected in the last 12 months. Low usage or other workloads: list it, rate Green.
6. Negative news, 90 days, where [Company] is the actor. Red: a merger, divestment or restructuring touching [Business function]. Amber: other restructuring or cost-cutting, or a new vendor in our category.

OUTPUT
- Bottom line: 2 sentences — overall rating and the risk to act on.
- Recommended next step: the sponsor or another leader from step 2 (name and title), what to do, and why now (the most important dated news item from step 6 or 4); if none turned up, say so.
- Table: Risk | Rating | Evidence | Date | Source. One row each: Sponsor, Senior exits, Layoffs, Workforce growth, Revenue growth, Competitor tools, Negative news.
- "Overall": Red if 2+ Reds, or Red on Sponsor or Competitor tools; Amber if any Red or 2+ Ambers; else Green.
- "Two actions this month", each tied to a row.
- Gaps: what Draup didn't have — worth asking your sponsor.

RULES
- Cut-offs are editable defaults. No rows = Green (unverified). Data unavailable or sponsor not found = Not in Draup, left out of Overall.
- In the Competitor tools row, name each product with its usage and workload.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 400 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Renewal risk on [Company]: Red/Amber/Green for our sponsor [Sponsor name], [Business function] exits, layoffs, growth, [Competitor] tools installed or new in our workloads, negative news; overall rating, 2 actions.
```

### Follow-ups

- Who replaced the leader who left, and do we know them?
- Draft a check-in email to our sponsor that addresses the top risk without alarming them.
- Run the same check on my other top 5 customers: [Accounts].

### Tips

- Give your sponsor's name, not just a title. Big accounts often have several people with the same title.
- "Green (unverified)" means Draup found nothing, not that the risk is zero. Confirm with your sponsor.
- Name the competitor products you actually lose to. An installed rival with High usage in your workload is rated Red, even if it's been there for years.

## Who they lose talent to

- **id:** `plan-talent-competitors`
- **What you get:** The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.
- **Use it when:** You want peers the buyer watches for talent, or a benchmark set that isn't just the annual-report competitor list.
- **Best for:** Account & Customer Success Manager, Account Executive, Marketing & ABM
- **Time:** 1–2 min
- **Inputs:** Company (e.g. walmart.com); Business function (optional) (e.g. IT); What I sell (e.g. developer productivity software)

### Detailed prompt

```text
Act as my account intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function (optional): [e.g. IT; blank uses the function closest to What I sell]
- What I sell: [One line, e.g. developer productivity software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull talent flow by company for [Business function] (or the function closest to [What I sell]): companies it loses people to and companies it hires from.
3. Remove the account's own subsidiaries and sister companies, "Self Employed", and blank or unknown employers. Mark staffing and IT services firms.
4. Join the two lists and work out net flow per company (hired from minus lost to).
5. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — who it competes with for talent and what that means for [What I sell].
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Window line: "Talent flow for [months], [function]".
- "Loses talent to" (top 10): Company | People lost | People hired from them | Net.
- "Hires talent from" (top 10): Company | People hired | People lost to them | Net.
- "Talent rivals": companies in both top 10s — they compete for the same skills, which makes them good benchmark peers. They aren't necessarily business rivals.
- "Why this matters for [What I sell]": 2–3 bullets (e.g. losing engineers to a tech employer: show what that employer's teams use; staffing firms high in the list: likely contractor dependence).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Counts are people moves Draup observed in the window, not total headcount.
- Staffing and IT services firms usually mean contractors moving, not competition; keep them out of Talent rivals.
- If the function returns nothing, rerun for the whole company and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Label inferences (buyer role, intent, fit) "likely".
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 380 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Which companies does [Company] lose the most people to, and hire the most from? Top 10 each way with net flow, excluding its subsidiaries and staffing firms. State the window.
```

### Follow-ups

- Benchmark [Company] against its top 3 talent rivals on hiring and growth.
- Which senior leaders left [Company] for these rivals recently?
- Which skills are they losing most to [rival]?

### Tips

- Talent rivals are often better benchmark peers than the competitors named in an annual report.
- The data lags by a few months, so it describes the recent past, not this month.

## Customer alumni now at your targets

- **id:** `plan-follow-champions`
- **What you get:** Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.
- **Use it when:** You want warm paths into new logos through people who may know your product. Use people-new-leaders-warm-paths instead for warm paths into the new leaders at one account.
- **Best for:** Account Executive, Account & Customer Success Manager, SDR / BDR
- **Time:** 2–4 min
- **Inputs:** Company (e.g. walmart.com); Accounts (e.g. Target, Kroger, Costco, Home Depot); Function or workload (e.g. Supply Chain); Champion names (optional) (e.g. paste names from your CRM)

### Detailed prompt

```text
Act as my relationship-mapping analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Our customer's website, e.g. walmart.com]
- Accounts: [Our target list, e.g. Target, Kroger, Costco]
- Function or workload: [e.g. Supply Chain — a function is fine, I'll map it to workloads]
- Champion names (optional): [Paste names from your CRM]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Map [Function or workload] to its 1–3 main workloads and say which. Pull leadership exits for the last 12 months, one workload at a time. Keep director-plus by full title and rows whose previous company is [Company]. State rows checked and the latest move date.
3. For each: name, old title, new employer, new title, month.
4. Match names against [Champion names] and new employers against [Accounts], allowing for spelling differences.
5. Pull talent-flow counts from [Company] to each target; write "not in the top flows" if absent.
6. Timing: for the best warm path, pull the new employer's most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how many warm paths and the best one.
- Recommended next step: the best warm path (name and new title), the opening line, and why now (their move month or the step-6 news). If there's no warm path, say so and name the closest alumnus.
- "Alumni on the move": Name | Old title | New employer and title | Month | Match (champion, my list or none).
- "Warm paths": named champions first, then my list, each with one opening line about their new role.
- Gaps: what Draup didn't have — worth checking in my CRM.
- Detail: "Flow to my targets" (Target | People moved, window).

RULES
- Never claim a past buying relationship. Mention our work with [Company] only if my CRM confirms they were involved.
- Names come only from leadership moves; talent flow gives counts, never names.
- If no exits come back, try a neighbouring workload.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 380 words including tables.
```

### Quick version

```text
Bottom line and next step (named alumnus, dated move) first. Which director-plus people left [Company] recently in [Function or workload], per Draup? Name, old title, new employer, new title, month. Flag employers on my list ([Accounts]) and names I paste.
```

### Follow-ups

- For each warm path, find the new employer's priorities in their function.
- Draft a 70-word congratulations note on the first person's new role.
- Who replaced each of them at [Company]?

### Tips

- Paste your real champions' names. Draup doesn't know who used your product, so a confirmed match is worth far more than a title match.
- Leadership data lags about 3 months, so "recent" means up to the latest move date the answer states.

## QBR prep: talking points and asks

- **id:** `plan-qbr-prep`
- **What you get:** Three talking points and three asks for your business review, built on what changed at the customer in your sponsor's function, set against the outcomes you delivered.
- **Use it when:** The week before a quarterly or executive business review. Use plan-risk-check instead about 90 days before renewal, and signals-change-log for a monthly what-changed log.
- **Best for:** Account & Customer Success Manager, Account Executive, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. walmart.com); Review period (optional) (e.g. 1 Aug 2026 – 31 Oct 2026); Business function (e.g. Supply Chain); What I sell (e.g. warehouse automation software, live in 40 distribution centres); Outcomes we delivered (e.g. uptime 99.9%, picking time down 12%); Competitor (optional) (e.g. Blue Yonder)

### Detailed prompt

```text
Act as my customer-success and QBR analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Review period (optional): [e.g. 1 Aug 2026 – 31 Oct 2026; blank = last full calendar quarter]
- Business function: [Our sponsor's function, e.g. Supply Chain]
- What I sell: [One line, e.g. warehouse automation software, live in 40 distribution centres — skip if you ran the start-here prompt]
- Outcomes we delivered: [Paste this period's results, e.g. uptime 99.9%, picking time down 12%]
- Competitor (optional): [e.g. Blue Yonder]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Priorities in [Business function] dated in [Review period] (10 at a time), with workloads; if none, the 3 most recent, marked as earlier.
3. Leadership: director-plus moves in [Review period], one step-2 workload per pull; keep only people whose current or previous employer is [Company]. If nothing falls in the period, say so and give the latest move date.
4. Hiring: monthly postings in [Business function] in [Review period] versus the same-length period before; top 3 [Business function] workloads trending up.
5. News in [Review period] where [Company] is the actor: deals, expansion, M&A, layoffs, restructuring.
6. Competitor check: any [Competitor] product in the stack in our workloads, with usage and last seen; flag anything newly detected in the period.
7. People: the top 3 leaders in [Business function] (full profile titles).
8. Financials: latest fiscal-year revenue and growth (USD at Draup's rate).

OUTPUT
- Bottom line: 2 sentences — the biggest change and what it means for renewal or expansion.
- Recommended next step: one person from step 7 or the sponsor (name and title), what to do before the meeting, and why now (a dated item from steps 2–5). If none turned up, say so.
- "3 talking points": each links a dated change to [Outcomes we delivered].
- "3 asks": expansion (tied to a priority), reference or case study, executive sponsor.
- "What changed" (up to 8 rows): Date | Type | What changed | Why it matters.
- Gaps: what Draup didn't have — worth asking in the meeting.
- Detail: leadership moves (Name | Move | Full title | Month), hiring numbers, competitor check, financials.

RULES
- Hiring, technology and news cover 12 months at most; if [Review period] is older, say what was covered.
- Check for a divestment before calling a revenue drop a cut.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

### Quick version

```text
Lead with 3 talking points, 3 asks and a next step naming a person. QBR for [Company], [Review period]: what changed in [Business function] (priorities, leaders, hiring, news, installed [Competitor] tools), set against [Outcomes we delivered].
```

### Follow-ups

- Turn the talking points and asks into 3 QBR slides: headline, evidence, ask.
- Run a renewal risk check before the meeting.
- Which new priority is the best expansion opportunity, and who owns it?

### Tips

- Lead with the outcomes you delivered; Draup's outside-in view works best as the bridge to your asks.
- Leadership data can lag about 3 months, so a quiet leadership section may just mean the data hasn't caught up. The answer states the latest move date.

## Tier my accounts by fit and timing

- **id:** `plan-propensity-tiering`
- **What you get:** Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.
- **Use it when:** Planning a quarter or a territory, or deciding where to spend limited time. Use plan-territories instead to split a whole market between reps.
- **Best for:** Account Executive, Sales Leader & RevOps, Account & Customer Success Manager, SDR / BDR
- **Time:** 4–6 min
- **Inputs:** Accounts (e.g. target.com, walmart.com, siemens.com, zebra.com, bmwgroup.com); What I sell (e.g. supply-chain planning software); Target revenue band (optional) (e.g. $5B–$150B); Competitor (optional) (e.g. Kinaxis, o9 Solutions)

### Detailed prompt

```text
Act as my territory planning analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [Up to 25 websites, e.g. target.com, walmart.com, siemens.com]
- What I sell: [One line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Target revenue band (optional): [e.g. $5B–$150B]
- Competitor (optional): [e.g. Kinaxis, o9 Solutions]

STEPS
1. Look up the accounts by website (exact match), 10 per lookup. Resolve misses one by one; if a website returns a subsidiary, ask. Never match by name.
2. Take revenue, revenue growth, Opportunity Index (Draup's 0–10 fit score), hiring %, workforce growth and primary industry.
3. Map [What I sell] to 1–3 Draup workloads and say which. For each account, pull 12-month postings in those workloads (one small lookup each) and rank them within the list.
4. If I named competitors, check in one list lookup which accounts have their products; for the top 10 by Fit, check usage strength in my workloads.
5. For the top 10 by Fit, count distinct dated news events from the last 90 days where the company is the actor; an event tied to [What I sell] counts double. Others: "not checked", 8 points.
6. Score, add up and tier, then apply the re-tier rule.
7. People and timing: at the top account, pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the A accounts and what they share.
- Recommended next step: a person from step 7 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Table: Tier | Account | Total (Fit + Timing) | Strongest driver | Weakest driver. By total.
- One-line reason per A account.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: per-account values (postings in my workloads, competitor usage, news count), "Rubric used", "Data flags" (missing values, websites that resolved to a subsidiary, possibly inactive).

RULES
- Rubric (editable defaults). FIT 50: relevance 20 (postings in my workloads: list's top third 20, middle 10, else 0); competitor installed 5 (High or Medium in my workloads 5, elsewhere 2, none 0: a displacement play); Opportunity Index 10 (score); revenue in band 10 (in 10, within 2x 5, else 2; 10 if no band); revenue growth 5 (over 5% 5, 0–5% 3). TIMING 50: news 20 (0, 1–2 = 8, 3–5 = 14, 6+ = 20); hiring % 15 (over 10% 15, 5–10% 10, 2–5% 5); workforce growth 15 (over 3% 15, 0–3% 10, −3–0% 5).
- Leave IT spend out: it's modelled from revenue and doesn't separate accounts.
- Tiers: A 70+, B 50–69, C under 50. If more than half the list lands in one tier, re-tier by rank (top 30% A, next 40% B, rest C) and say so.
- Missing value = half that item's points, flagged.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Tier [Accounts] for [What I sell]: fit (postings in my workloads, installed [Competitor]) and timing (news, hiring, growth), A/B/C relative to the list, one-line reason each.
```

### Follow-ups

- Change the rubric: relevance 30, Opportunity Index 0, and rerun.
- For my A accounts, give one why-now signal each from the last 60 days.
- Count news events for the accounts marked "not checked".
- Build a one-page account brief for the top-scoring account.

### Tips

- The rubric is in the prompt on purpose. Change the weights to match how your team actually wins.
- Use websites, not names. Some parents use unusual domains (home.barclays, group.bnpparibas); if a website returns a subsidiary, the assistant will ask.
- If every account looks like an A, the re-tier rule spreads them by rank so the list is still usable.

## Carve balanced territories by geography

- **id:** `plan-territories`
- **What you get:** An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.
- **Use it when:** Advanced: annual territory planning or when a new rep joins; best run by RevOps or a sales leader. Use plan-propensity-tiering instead to rank a list you already own.
- **Best for:** Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Insurance); Country (e.g. United States of America); Minimum employees (e.g. 10000); Number of territories (e.g. 3); Balance on (optional) (e.g. revenue); Accounts already owned (optional) (e.g. metlife.com, allstate.com)

### Detailed prompt

```text
Act as my RevOps territory planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Country: [HQ country in full, e.g. United States of America]
- Minimum employees: [e.g. 10000]
- Number of territories: [e.g. 3]
- Balance on (optional): [Draup-estimated IT spend (default), revenue or account count]
- Accounts already owned (optional): [Websites to exclude, e.g. metlife.com]

STEPS
1. Confirm Draup's names for the industry and country.
2. Count first: companies whose primary industry is [Vertical], HQ in [Country], with [Minimum employees]+ staff. If more than 100, stop and ask me to raise the threshold.
3. Pull them 10 at a time, largest first by the balance measure: HQ metro, employees, revenue, Draup-estimated IT spend.
4. Remove accounts already owned (match by website). Remove non-operating holding companies, conglomerates and private-equity or investment firms, and list them. Flag misfiled companies (HQ or description doesn't fit) and possibly inactive ones.
5. Group accounts by HQ region (e.g. Northeast, Southeast, Central, West; or metros if there are more than 4 territories). Assign whole regions to territories, then move single accounts only if a territory is more than 10% off balance; list every move.
6. Count companies of the same size and country that have [Vertical] only as a secondary industry; list up to 5 that genuinely operate in it as "Consider adding". Don't assign them.

OUTPUT
- Bottom line: 2 sentences — universe size and how even the split is.
- Recommended next step: who on my team does what, by when (e.g. "RevOps lead reviews the moves with the three regional managers this week"). No account why-now needed.
- "Territory summary": Territory | Regions and main metros | Accounts | Total (USD M, fiscal year) | Share.
- "Moves for balance": each single account moved, from and to, and why.
- Gaps: what Draup didn't have — worth checking in our CRM.
- Detail: one table per territory (Account | HQ metro | Employees | Revenue | IT spend); "Removed" (holding, private-equity, owned); "Consider adding"; "Data flags" (misfiled, possibly inactive, no IT spend so placed by revenue, how many matches lack size data).

RULES
- Size limits drop companies with no workforce figure (often large private firms or mutuals); report how many and offer to include them.
- IT spend is a Draup estimate, often modelled from revenue, so balancing on it is close to balancing on revenue; say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

### Quick version

```text
Bottom line and next step first. Count [Vertical] companies (primary industry) headquartered in [Country] with [Minimum employees]+ staff, drop owned, holding and private-equity firms, and split the rest into [Number of territories] territories by HQ region, balanced within 10%.
```

### Follow-ups

- Rebalance on account count instead.
- Add Draup's Opportunity Index score and show the top 5 per territory.
- Tier each territory's accounts by fit to what we sell.
- Export the assignments as a table I can paste into a spreadsheet.

### Tips

- Geography comes first so each rep gets a coherent patch; balance is then fixed with a few named moves you can argue about.
- Large suppliers whose main industry is different won't appear in the main list. Check "Consider adding".
- Balancing on spend favours fairness of opportunity; balancing on count favours fairness of workload. Pick one.

## Brief for a C-level pursuit meeting

- **id:** `plan-cxo-pursuit-brief`
- **What you get:** A one-page pursuit brief for a C-level meeting: the 3 workloads to lead with, the buyers, incumbents, a Go or Not-yet evidence check, what to learn in meeting 1 and a 90-day plan.
- **Use it when:** You have, or want, a meeting with a CIO, CTO, COO or other C-level buyer on a large pursuit.
- **Best for:** Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps, Presales & Solutions
- **Time:** 4–6 min
- **Inputs:** Company (e.g. pfizer.com); Business function (e.g. IT); What I sell (e.g. AI-led application modernisation services)

### Detailed prompt

```text
Act as my pursuit lead. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Business function: [The executive's function, e.g. IT for a CIO]
- What I sell: [One line, e.g. AI-led application modernisation services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Money: latest fiscal-year revenue (USD at Draup's rate) and growth.
3. Priorities in [Business function] from the 4 most recent quarter labels in the data; count how many involve each workload.
4. For the top 6 workloads, pull engagements, leading providers and the top provider's tier.
5. Pick 3 lead workloads: most evidence, best fit to [What I sell], no strategic incumbent. Skip catch-alls.
6. Buyers: up to 6 senior leaders in [Business function] (10 per page, up to 3 pages), plus director-plus moves in 6 months narrowed by those workloads. If no C-level, EVP or "Head of" appears, search once more for Chief, EVP or CIO titles and say what you found.
7. Timing: the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the case and the opening angle.
- Recommended next step: one buyer from step 6 (name and title), what to do, and why now (the step-7 item or another dated fact). If none turned up, say so.
- "Lead with": Workload | Priority evidence (quarter) | Incumbent and tier | Our angle.
- "Buyers": Name | Full title | Why they matter | Recent move.
- "Evidence check: Go / Not yet": Go if 2+ matching priorities sit in the 2 latest quarter labels, a reachable senior buyer exists, and a lead workload has no strategic incumbent (editable default); else Not yet and what would change it.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: money context; "What we must learn in meeting 1" (3 questions); "90-day plan" (two actions per 30 days).

RULES
- In banking and consulting, VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Rank providers by engagements yourself.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

### Quick version

```text
Bottom line and next step (named buyer, dated why-now) first. Build a C-level pursuit brief for [Company]'s [Business function] leader: 3 workloads to lead with (priorities plus incumbents), buyers, a Go or Not-yet check, meeting-1 questions and a 90-day plan.
```

### Follow-ups

- Write 5 hypothesis-led questions for the executive, each citing a fact from the brief.
- Pick a co-sell partner for the first lead workload.
- Turn the brief into a 3-slide executive summary.

### Tips

- The evidence check is in the prompt. Tighten or loosen it to match how your team qualifies large pursuits.
- Check each buyer's full title yourself. Seniority tags can overstate.

## AI readiness against close peers

- **id:** `plan-ai-readiness`
- **What you get:** A read on the account's AI hiring, priorities, new tools and outsourced AI work, its AI hiring compared with up to 4 close peers, and who to raise it with.
- **Use it when:** You sell AI, data or automation and need a maturity read or a peer comparison.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Company (e.g. pfizer.com); What I sell (e.g. enterprise generative AI platform); Peers (optional) (e.g. lilly.com, abbvie.com, novartis.com, bms.com)

### Detailed prompt

```text
Act as my AI market analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. enterprise generative AI platform — skip if you ran the start-here prompt]
- Peers (optional): [Up to 4 websites, e.g. lilly.com, abbvie.com; blank = Draup's closest competitors]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Peers, in one company-list lookup: my websites, or the account's top competitors in its primary industry, keeping the 4 closest in revenue (0.3–3x, editable default), with workforce.
3. Account deep-dive: "Artificial Intelligence & Data Science" postings (12 months, monthly); AI, Generative AI or Machine Learning priorities (count, latest two with quarter); AI tools newly detected in 12 months (up to 5, no generic tools such as chat assistants or office add-ons); outsourced AI engagements and top 3 providers.
4. For each peer, pull only AI & Data Science postings with the monthly trend.
5. Compare AI postings per 1,000 employees; under 10% apart is level (editable default).
6. People and timing: at [Company], pull the top 3 leaders in the function that owns AI and data (often IT) and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — where the account stands and the opening for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Peers": Company | AI postings (12 mo) | Per 1,000 employees | Trend | Read (Ahead, Level or Behind). Account first.
- "Account deep-dive": 4 dated bullets — AI postings and trend, AI priorities, new AI tools, outsourced AI work.
- "Questions to raise": 3, each naming a peer and a number.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: peer workforce figures and "Why this matters for [What I sell]" (2 bullets and one peer-evidence sentence).

RULES
- Compare peers on AI hiring only. Tool additions are newly detected, not confirmed rollouts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 420 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Read [Company]'s AI readiness: AI postings and trend, AI priorities, new AI tools and outsourced AI work. Then compare AI hiring per 1,000 employees with up to 4 peers.
```

### Follow-ups

- Show the 10 most recent AI postings at [Company], with title, date and location.
- Which leaders at [Company] own the AI priorities?
- Write a 120-word peer-comparison email to the person in the next step.

### Tips

- A low AI hiring rate alongside several AI priorities often means the work is outsourced or not yet staffed. Both are openings.
- Pick peers the buyer actually watches. Paste their websites if Draup's competitors don't fit.
