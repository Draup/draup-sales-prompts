# Industry and market intelligence

Industry-level numbers, priorities and vendor landscapes for pitches and planning.

## One-page vertical market snapshot

- **id:** `market-vertical-snapshot`
- **What you get:** A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.
- **Use it when:** You are entering a vertical, building a territory plan, or need industry context for a pitch or a leadership review.
- **Best for:** Sales Leader & RevOps, Marketing & ABM, Account Executive, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Aerospace & Defense); Region (optional) (e.g. Europe, or North America); What I sell (e.g. PLM software)

### Detailed prompt

```text
Act as my industry analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Aerospace & Defense]
- Region (optional): [default: my territory from setup; e.g. Europe, or North America]
- What I sell: [one line, e.g. PLM software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical (a sub-industry with zeros: use its parent) and [Region] to Draup's names. If the region doesn't resolve, use Draup's nearest values (e.g. "Northern America" = US and Canada) and list their countries.
2. The vertical's revenue, IT spend and R&D spend, latest year, with growth (global totals).
3. The vertical's key priorities: pick the 5 that fit [What I sell], with dated proof from the 2 largest employers in [Region] in that function. If there are none, say so first and use those 2 employers' dated priorities, labelled "company proof, not industry-wide".
4. Top buyers: the 10 largest parents by workforce, primary vertical [Vertical], HQ in [Region], with revenue; count subsidiaries once. Total their revenue as the regional size. Flag any that sell what I sell. Rivals I named: note who runs them at High or Medium usage (ignore Low; say so).
5. Growing technologies: up to 5 relevant to [What I sell], or "none relevant in Draup".
6. Services sellers only: top outsourcing vendors (no agencies, staffing or research firms) and top 5 workloads, with active engagements (Draup-derived).
7. For the best-fit top buyer: its top 3 executives in that function and top 90-day news item. If it is a top-3 giant, also pick the best-fit mid-size buyer.

OUTPUT
- Bottom line: 2 sentences — the state of [Vertical] in [Region] and what it means for [What I sell].
- Recommended next step: a named person (name, full title), the action and a dated why-now; if missing, the title to find. Add the mid-size buyer if picked.
- "The numbers": Metric | Value ($B) | Growth % | Year: revenue, IT and R&D spend (global; "year not given" if omitted), then the top-10 buyers' revenue in [Region].
- "Top priorities": Priority | Dated proof (company, quarter) | Likely owner | Fit.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: top buyers (rivals present); growing technologies; outsourcing (services sellers); exclusions.

RULES
- Name any company that makes up over a third of a total.
- "Fit" is judgement (Draup ties no priority to a seller). Vertical lists are a fixed top 50; say so once.
- Flag off-vertical, sanctioned or state-owned buyers. IT spend tracks revenue, so its growth is no trend.
- No generic tools (office suites, chat assistants) in technology lists. If I ask for a slide: 5 bullets + 1 table.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: a one-page snapshot of [Vertical] in [Region]: global size and growth plus the top-10 buyers' regional revenue, the 5 priorities that fit [What I sell] with dated company proof, and who to call first.
```

### Follow-ups

- Turn the top 3 priorities into a 5-slide point of view for [What I sell].
- Which 10 companies in [Vertical] in [Region] hire most per 1,000 staff right now?
- Show the outsourcing league table for this vertical in [Region] (services sellers).

### Tips

- Region defaults to your territory; the industry totals stay global, so read the top-10 buyers' revenue as the regional size.
- If one giant dominates a total (one retailer's R&D, say), the snapshot names it; discount the growth figure accordingly.
- The Fit column is the assistant's judgement, not a Draup score. Challenge it.

## Build an industry point of view

- **id:** `market-industry-pov`
- **What you get:** The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.
- **Use it when:** You need a 'why this, why now' story for an industry keynote, campaign or first meeting.
- **Best for:** Marketing & ABM, Account Executive, Presales & Solutions, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Vertical (e.g. Automotive); Audience (e.g. VP Supply Chain); Territory (optional) (e.g. United States of America); What I sell (e.g. supply-chain planning software)

### Detailed prompt

```text
Act as my industry marketing strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Automotive]
- Audience: [the persona, e.g. VP Supply Chain]
- Territory (optional): [HQ country or region; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull the vertical's key priorities. If none come back, say so in the first line and use the dated priorities of its 2 largest parent employers in [Territory], labelled "company proof, not industry-wide".
3. Choose the 5 priorities that best fit [What I sell] and [Audience]'s function. Judge by what each describes, not its function label, and explain each choice in one line.
4. Vertical priorities carry no dates: for each, keep the named company examples and pull the dated priorities of 2–3 of the vertical's largest parent employers in [Territory] in that function and use those as proof (company, quarter or month).
5. Market context: the vertical's revenue and R&D growth, and the 3 fastest-growing technologies relevant to [What I sell] (none: "Not in Draup", never generic tools).
6. For the company behind the strongest proof: its top 3 executives in [Audience]'s function and its most important news item from the last 90 days. If it is one of the vertical's 3 largest employers, also name the best-fit mid-size company in one line.

OUTPUT
- Bottom line: 2 sentences — the industry story and why [What I sell] fits it now.
- Recommended next step: a named person (name, full title), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 5 priorities": # | Priority | Dated proof | Likely owner (title) | Why it matters to [Audience].
- "5-slide narrative": per slide a title, 3 short bullets and one dated proof point. Slide 1: the market shift. Slides 2–4: the three strongest priorities. Slide 5: why [What I sell] now.
- "One-line POV": 35 words or fewer.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: why each priority was chosen; growth figures with year (or "year not given").

RULES
- Use only Draup facts and company examples. Never invent statistics or quotes.
- Company examples are real public companies; present them as industry evidence, never as our customers.
- IT spend tracks revenue in Draup; don't use its growth as a trend.
- If an industry returns zeros, say so, retry with its parent and name it.
- Name any company driving over a third of a growth figure.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: pick the 5 [Vertical] priorities that fit [What I sell] for a [Audience], each with dated proof from named companies, then a 5-slide narrative and a 35-word POV.
```

### Follow-ups

- Turn this into a 3-email sequence for [Audience], 120 words or fewer each, each with one dated example.
- Which 10 [Vertical] companies are most active on priority #1?
- Make a version for a CFO audience.

### Tips

- Name a specific persona in Audience. 'VP Supply Chain' gives sharper picks than 'executives'.
- Check your Draup licence before publishing Draup data externally, for example in a keynote or blog.

## Who wins services work in a vertical

- **id:** `market-vendor-league`
- **What you get:** Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.
- **Use it when:** You sell IT or business services and need to know who you are up against in an industry.
- **Best for:** Services, SI & Staffing Seller, Partnerships & Alliances, Sales Leader & RevOps, Marketing & ABM
- **Time:** 2–4 min
- **Inputs:** Vertical (e.g. Life Sciences); Workload (optional) (e.g. Application Development & Maintenance); Territory (optional) (e.g. United States of America); My company (e.g. Northwind Data Services (illustrative)); What I sell (e.g. clinical-data platform services)

### Detailed prompt

```text
Act as my services market analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Life Sciences]
- Workload (optional): [a type of work, e.g. Application Development & Maintenance]
- Territory (optional): [client HQ country or region; default: my territory from setup, e.g. United States of America]
- My company: [as Draup spells it, e.g. Northwind Data Services (illustrative)]
- What I sell: [one line, e.g. clinical-data platform services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. With a Territory, rank providers by active engagements at [Vertical] companies HQ'd in [Territory] (top 50; say it is a regional ranking). With none, pull the vertical's fixed global top 50 vendors. Remove advertising and media agencies, staffing, market-research, merchandising and field-marketing firms; list what you removed. Keep the top 15.
3. Pull the top 10 outsourced workloads and the top 10 outsourcing buyers (in [Territory] if set), merging subsidiaries into parents.
4. If I gave a workload, pull the top 10 providers for it among companies whose primary vertical is [Vertical] (HQ in [Territory] if set).
5. Find [My company]'s rank and active engagements, or say "not in the top 50"; if nothing returns, try the short brand name.
6. For the top buyer where [My company] is absent: its top 3 executives in the function closest to What I sell and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how the market is split and where [My company] stands.
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "League table" (top 10): Rank | Provider | Active engagements (Draup-derived) | Share of top 15 % | Type (global systems integrator, consulting, niche specialist, business-process outsourcer).
- "Where [My company] stands": rank, gap to #1 and #5, and the 2 workloads with the most room.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: ranks 11–15; concentration (top-3 share; "concentrated" over 50%, editable); top workloads; top buyers with likely owner; "[Workload] leaders"; excluded firms.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them as the opening.
- Flag buyers whose business doesn't fit [Vertical].
- Engagements are Draup-derived estimates, not public contracts; never call them signed deals.
- If an industry returns zeros, say so, retry with its parent and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank the top 10 outsourcing providers in [Vertical] (clients in [Territory]) by active engagements, agencies and staffing removed; show where [My company] ranks, the top buyers, and who to call.
```

### Follow-ups

- Show where [Competitor] wins [Workload] work in [Vertical]: top 10 customers.
- For the top 5 buyers, who are their top 3 providers?
- Which buyers have no top-5 provider in [Workload]?

### Tips

- Engagement counts measure breadth of relationship, not revenue.
- Agencies and staffing firms rank high on raw counts; the prompt removes them so the table shows real services rivals.
- Set Territory to see who wins work from clients in your region; the global list can rank a different leader first.

## Find where a vertical's teams sit

- **id:** `market-talent-hubs`
- **What you get:** The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.
- **Use it when:** You are choosing where to hold events, recruit or place delivery capacity for an industry.
- **Best for:** Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 1–2 min
- **Inputs:** Vertical (e.g. Banking & Financial Services); Country (optional) (e.g. India); What I sell (e.g. data-engineering services)

### Detailed prompt

```text
Act as my market and location analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Banking & Financial Services]
- Country (optional): [in full, e.g. India]
- What I sell: [one line, e.g. data-engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical, and the country if given, to Draup's names and show them.
2. Pull the metros where the vertical's IT teams are concentrated, ranked by Draup's workforce-strength index. The data is global, so if I gave a country, keep only its metros.
3. Do the same for the vertical's R&D teams, and mark metros on both lists.
4. For the #1 hub: the biggest [Vertical] employer there, its top 3 executives located in that metro in the function closest to What I sell, and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — where the vertical's technical work sits and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 4), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "IT hubs" (top 10): Rank | Metro | Country | Index | Also an R&D hub?
- "Where to focus": 3 metros, one reason each (delivery, events or recruiting).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "R&D hubs" (top 10): Rank | Metro | Country | Index.

RULES
- The index is relative strength, not headcount. Never call it employees, and only compare values within one list.
- These hubs show where delivery and engineering sit, not where budget holders are; say so once.
- If an industry returns zeros, say so, retry with its parent and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: the top 10 metros for [Vertical] IT teams and for R&D teams by Draup's workforce-strength index, metros on both lists, 3 places to focus, and who to meet in the #1 hub.
```

### Follow-ups

- Who are the 10 biggest [Vertical] employers in the #1 metro?
- Which companies have GCCs in the top 3 IT hubs?
- Compare the top 2 countries on labour force, cost of living and tax.

### Tips

- Use the index to rank places, not to size teams.
- Add a country to get a territory-level view.

## Find who hires hardest in a vertical

- **id:** `market-hiring-leaders`
- **What you get:** The real end employers hiring hardest in an industry, ranked on postings per 1,000 staff with recruiters and outliers removed, plus hot spots and a named person to call first.
- **Use it when:** You want the most active companies in a vertical this year; active hiring often means active budgets.
- **Best for:** SDR / BDR, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Vertical (e.g. Life Sciences); Territory (optional) (e.g. United States of America); What I sell (e.g. talent-acquisition software)

### Detailed prompt

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Life Sciences]
- Territory (optional): [country in full; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. talent-acquisition software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. With a Territory, rank the top 50 employers posting in [Territory] with primary vertical [Vertical], last 12 months, staffing firms and job boards excluded; merge brands and subsidiaries into parents and drop foreign companies' local teams. With none, pull Draup's top hiring companies for the vertical (a fixed top 50) and note its window.
3. Remove staffing and recruiting firms and job boards; record each.
4. Look the rest up in one company list by exact name: workforce, primary vertical and postings (90 days). Work out postings per 1,000 employees.
5. Remove outliers: a posting count above the company's workforce, or an unfamiliar firm posting far more than household names. Rank companies with 1,000+ staff (editable) by postings per 1,000.
6. For the #1: its top 3 executives in the function closest to What I sell and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — who is hiring hardest for their size and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Hiring hardest" (top 10): Rank | Company | Postings | Per 1,000 staff | Workforce.
- "Hot spots for [What I sell]": 5 companies, one reason each.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: vertical and window ("window not stated" if none); companies under 1,000 staff; the raw-count ranking; "Removed" with reasons.

RULES
- Flag "check vertical" when a company's primary vertical isn't [Vertical].
- No workforce figure: write "n/a" for intensity and list it in Detail rather than dropping it.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- If an industry returns zeros, say so, retry with its parent and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: the top 10 [Vertical] companies in [Territory] by postings per 1,000 staff (1,000+ employees), staffing firms and outliers removed, 5 hot spots for [What I sell], and who to call at the #1.
```

### Follow-ups

- For the top 5, which functions and skills are they hiring for most?
- Which of these are hiring most in [Country]?
- Draft a hiring-themed opener for the #1 hot spot.

### Tips

- Ranking on postings per 1,000 staff shows who is hiring hard for their size, not just who is biggest.
- Check the Removed list if a name you expected is missing.

## Check if a skill market buys contractors

- **id:** `market-contract-vs-fulltime`
- **What you get:** What share of hiring for a skill is contract versus full-time, how much staffing firms drive it, what it means for staff-aug or SI demand, and a named end-employer contact.
- **Use it when:** You sell staffing, staff augmentation or SI services and want to know whether a skill's market buys contractors.
- **Best for:** Services, SI & Staffing Seller, Partnerships & Alliances, Sales Leader & RevOps
- **Time:** 1–2 min
- **Inputs:** Technology (e.g. SAP S/4HANA); Territory (optional) (e.g. United States of America); What I sell (e.g. SAP staff augmentation)

### Detailed prompt

```text
Act as my talent market analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Technology: [skill or product, e.g. SAP S/4HANA]
- Territory (optional): [country in full; default: my territory from setup, or "global"; e.g. United States of America]
- What I sell: [one line, e.g. SAP staff augmentation — skip if you ran the start-here prompt]

STEPS
1. Resolve the technology to Draup's skill name (e.g. "CrowdStrike Falcon", not "CrowdStrike") and [Territory] to Draup's name; show them. If postings come back 0, retry once with the product name.
2. Pull the work-type breakdown of postings for [Technology] over the last 12 months: full-time, contract, part-time, other and no type stated.
3. Work out each type's share of all postings and of postings that state a type.
4. Pull the top 15 companies posting for [Technology] in the same window and territory, merge subsidiaries into parents, and classify each as end employer, staffing firm or IT services/SI.
5. For the top end employer: its top 3 executives in the function that owns [Technology] and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — whether this market buys contractors and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Split": Work type | Postings | Share of all % | Share of stated-type %. Verdict: "contract-heavy" over 40% of stated, "balanced" at 20–40%, else "full-time-led" (editable).
- "Who's hiring" (top 10): Company | Postings | Type.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: header with technology, territory (or "global") and exact window; ranks 11–15; 3 bullets on what it means for [What I sell].

RULES
- Never count no-type postings as full-time, and always show the no-type share.
- Use the same window and territory for every number; city breakdowns are out of scope.
- Many staffing or SI firms in the top 15 is another sign of contract-led demand.
- Postings are openings, not hires.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: for [Technology] postings in 12 months, the contract vs full-time split (stated types), the no-type share, how many top-15 hirers are staffing or IT-services firms, and who to call.
```

### Follow-ups

- Run the same check for [another technology] and compare the two.
- Which end employers post the most contract roles for [Technology]?
- What job titles dominate [Technology] postings?

### Tips

- A large no-type share is normal. Judge the split on postings that state a type.
- If staffing firms dominate the hirer list, demand is often met through contractors: a staff-aug opening.

## Compare countries for a delivery centre

- **id:** `market-country-compare`
- **What you get:** A side-by-side country comparison on labour force, unemployment, cost of living, inflation, tax and stability, with takeaways, client questions and, if you name the client, who to talk to.
- **Use it when:** A client is weighing delivery or GCC locations, or you are positioning a nearshore or offshore option.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Sales Leader & RevOps
- **Time:** 1–2 min
- **Inputs:** Country A (e.g. India); Country B (e.g. Poland); Country C (optional) (e.g. Mexico); Client (optional) (e.g. the client's website, e.g. fabrikam.com (illustrative)); What I sell (e.g. nearshore delivery centre services)

### Detailed prompt

```text
Act as my location strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Country A: [in full, e.g. India]
- Country B: [in full, e.g. Poland]
- Country C (optional): [e.g. Mexico]
- Client (optional): [the client's website, e.g. fabrikam.com (illustrative)]
- What I sell: [one line, e.g. nearshore delivery centre services — skip if you ran the start-here prompt]

STEPS
1. Use full country names as Draup knows them (e.g. "United States of America", not "USA").
2. Pull Draup's country data for all of them in one go: labour force, unemployment rate, median age, cost-of-living index, inflation, corporate tax rate, political stability, and any other workforce metric Draup returns.
3. If I named a client: find it by website (confirm the parent; no match: retry once by name and show the match score), then pull its top 3 executives in IT or global delivery and its most important news item from the last 90 days (centre openings, expansions or cost programmes first).

OUTPUT
- Bottom line: 2 sentences — how the locations compare and which fits [What I sell] best for this client.
- Recommended next step: a named person (name and full title from step 3), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Comparison": Metric | [Country A] | [Country B] | ([Country C]) | Period.
- "Takeaways": 3 bullets on talent-pool scale, cost position, and tax and risk.
- "Questions to ask the client": 3 (e.g. language needs, time-zone overlap, scale over 3 years).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: 2 bullets on how to position each location for [What I sell].

RULES
- Cost of living is an index (higher = more expensive), not a currency amount; say so.
- This view has no salary data. For pay by role and city, say the Draup for Talent connector is needed.
- Use no outside sources for missing metrics; mark them "Not in Draup".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: compare [Country A] and [Country B] on labour force, unemployment, median age, cost of living, inflation, corporate tax and stability, with periods, 3 takeaways and 3 client questions.
```

### Follow-ups

- Which metros in [Country B] have the strongest IT teams in [Vertical]?
- Who are the biggest [Vertical] employers in [City]?
- Turn this into a one-slide location comparison.

### Tips

- The comparison answers in a single lookup, so it is quick to run several pairs.
- Name the client to get a named contact and a dated reason to call.
