# Solution plays: by what you sell

Find the accounts most ready for what you sell, and check any account's readiness: cloud, data & AI, ERP, security, GenAI, CX, supply chain, HR tech, managed services, engineering, testing.

## Find accounts ripe for cloud migration

- **id:** `plays-cloud-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy cloud migration, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a cloud or infrastructure-modernisation campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Aerospace & Defense); Country (e.g. United States of America); What I sell (e.g. cloud migration and managed cloud services)

### Detailed prompt

```text
Act as my cloud-migration target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Aerospace & Defense]
- Country: [HQ country in full, e.g. United States of America]
- What I sell: [one line, e.g. cloud migration and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and country to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in the Cloud Computing and Infrastructure Management System workloads, 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in Cloud Computing, Infrastructure Management System, Legacy Modernization and Data Centre Management; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop cloud providers, IT resellers and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only cloud and infrastructure tools; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 priorities each in those four workloads, newest first.
7. One news search across the top 5 on modernisation, cloud, data-centre or infrastructure partnerships, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Cloud Computing or Infrastructure Management System; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (thirds by postings per 1,000); Priority 0–3 (3 = modernisation priority in the last 4 fiscal quarters; 2 = older or news-sourced); Stack 0–2 (2 = migration tooling, or public cloud beside on-premise virtualisation); Outsourcing 0–1 (5+ engagements); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Count a priority only if its text mentions infrastructure, cloud, data centre, platform or core-system modernisation; these workloads also catch payments and store projects.
- Government IT contractors that serve defence or public-sector primes are providers, not buyers.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for cloud migration on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A migration tool showing in the stack is often a sign a programme is already under way.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for cloud migration?

- **id:** `plays-cloud-readiness`
- **What you get:** A 0–20 readiness score for cloud migration at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a cloud or infrastructure-modernisation deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. thekrogerco.com); Competitor or incumbent (optional) (e.g. Infosys); What I sell (e.g. cloud migration and managed cloud services)

### Detailed prompt

```text
Act as my cloud-migration account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. thekrogerco.com]
- Competitor or incumbent (optional): [e.g. Infosys]
- What I sell: [one line, e.g. cloud migration and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure). If it sells cloud services itself, drop its own products throughout.
2. Money: latest revenue and growth, Draup-estimated IT spend and its split (direction only).
3. Intent: up to 6 priorities in Cloud Computing, Infrastructure Management System, Legacy Modernization, Data Centre Management and DevOps, newest first, with linked tools and providers.
4. Current state: vendors ranked by products in the cloud, infrastructure and data-centre workloads, with top products; sort into public cloud and on-premise (virtualisation, mainframe, Unix, servers, storage).
5. Capability: IT postings by workload, then the top 15 skills in cloud, infrastructure and DevOps postings; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by active engagements at [Company] in the step-3 workloads, top 10, no agencies or staffing firms. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Cloud Computing or Infrastructure Management System; keep cloud, infrastructure, platform, CTO or CIO titles; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on modernisation, cloud, data centres, acquisitions, separations or cost programmes; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Intent (dated modernisation priority), On-premise gap, Capacity gap (4 = thin cloud hiring beside a modernisation push), Buying pattern (active infrastructure outsourcing), Timing (dated trigger).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Area | Vendors | Read); IT split (direction only).

RULES
- Count a priority only if its text mentions infrastructure, cloud, data centre, platform or core-system modernisation.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for cloud migration (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Map the buying committee for Infrastructure Management System.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- A big hardware and on-premise software share in the IT split, next to few cloud postings, often signals a buy-not-build migration.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for data platforms

- **id:** `plays-data-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy data-platform modernisation, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a data-platform, lakehouse or analytics campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Banking & Financial Services); Country (e.g. United States of America); What I sell (e.g. lakehouse modernisation and analytics services)

### Detailed prompt

```text
Act as my data-platform target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Banking & Financial Services]
- Country: [HQ country in full, e.g. United States of America]
- What I sell: [one line, e.g. lakehouse modernisation and analytics services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and country to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in the Data Engineering and Business Intelligence & Analytics workloads, 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in Data Engineering and Business Intelligence & Analytics; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop technology and data vendors and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only data tools, sorted legacy (Hadoop, Teradata, Informatica PowerCenter, on-premise warehouses) or modern; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 priorities each in those two workloads plus Artificial Intelligence & Data Science, newest first.
7. One news search across the top 5 on data, analytics or data-platform partnerships, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Data Engineering or Business Intelligence & Analytics; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (thirds by postings per 1,000); Priority 0–3 (3 = data priority tied to an outcome in the last 4 fiscal quarters; 2 = older); Stack 0–2 (2 = legacy tools visible; 1 = modern only); Outsourcing 0–1 (20+ engagements); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Count a priority only if it names data, analytics, a data platform or a measurable data outcome; drop priorities about products the company sells (many banks sell data services).
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for data-platform modernisation on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Legacy and modern tools side by side usually means a migration is under way: ask what is left to move.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for data platforms?

- **id:** `plays-data-readiness`
- **What you get:** A 0–20 readiness score for data-platform modernisation at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a data-platform, lakehouse or analytics deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. target.com); Competitor or incumbent (optional) (e.g. Databricks); What I sell (e.g. lakehouse modernisation and analytics services)

### Detailed prompt

```text
Act as my data-platform account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Competitor or incumbent (optional): [e.g. Databricks]
- What I sell: [one line, e.g. lakehouse modernisation and analytics services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in Data Engineering, Business Intelligence & Analytics and Artificial Intelligence & Data Science that name data, analytics or a measurable data outcome, newest first, with linked tools and providers.
4. Current state: vendors ranked by products in Data Engineering and Business Intelligence & Analytics, sorted into legacy (Hadoop, Teradata, Netezza, Informatica PowerCenter, older BI) and modern.
5. Capability: the top 15 data skills in postings, noting legacy skills and rising ones; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by active engagements at [Company] in the step-3 workloads, top 10, no agencies, research or merchandising firms. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Data Engineering or Business Intelligence & Analytics; keep data, analytics, insights, platform, CDO or CTO titles; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on data platforms, analytics, AI, leadership changes, acquisitions or capex; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Intent, Legacy gap (legacy platforms still in use), Capability gap (4 = legacy skills still hired and governance or platform skills trending up), Buying pattern, Timing.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Layer | Legacy | Modern | Read).

RULES
- Legacy skills in current job ads mean the old platform is far from retired; check usage before calling a vendor the standard.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for data-platform modernisation (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Show the 10 most recent data-engineering postings with title, date and the tools named.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Legacy skills still in job ads (for example Hadoop) often mean the old platform is far from retired.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for ERP modernisation

- **id:** `plays-erp-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy ERP modernisation, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a S/4HANA, Oracle Cloud ERP or other ERP campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Industrial); Country (e.g. Germany); Target platform (e.g. SAP S/4HANA); Legacy platform (optional) (e.g. SAP ERP (ECC)); What I sell (e.g. SAP S/4HANA migration and AMS services)

### Detailed prompt

```text
Act as my ERP-modernisation target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Industrial]
- Country: [HQ country in full, e.g. Germany]
- Target platform: [e.g. SAP S/4HANA]
- Legacy platform (optional): [e.g. SAP ERP (ECC)]
- What I sell: [one line, e.g. SAP S/4HANA migration and AMS services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and platforms to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most postings naming [Target platform], 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in engagements involving [Target platform] or [Legacy platform]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop ERP vendors, consultancies and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only ERP products from the main makers, labelling each company Not started (legacy only), Mid-migration, Moved or Other ERP; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 6 Finance & Accounting and IT priorities each, marked direct (ERP named) or indirect.
7. One news search across the top 5 on ERP programmes, carve-outs, acquisitions, divestments or finance transformation, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in IT, then Finance & Accounting (ERP, applications, CIO or CFO titles); no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (thirds by [Target platform] postings per 1,000); ERP status 0–2 (Not started or Mid-migration 2, Other ERP 1); Trigger 0–3 (3 = carve-out, acquisition or finance transformation within 12 months; 2 = indirect priority); Outsourcing 0–1 (3+ ERP engagements); Named programme 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Never present an indirect trigger as a confirmed ERP project; label it direct or indirect.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for ERP modernisation on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Carve-outs and divestments are among the strongest ERP triggers: the separated business needs its own system, fast.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for ERP modernisation?

- **id:** `plays-erp-readiness`
- **What you get:** A 0–20 readiness score for ERP modernisation at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a S/4HANA, Oracle Cloud ERP or other ERP deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. caterpillar.com); Target platform (e.g. SAP S/4HANA); Competitor or incumbent (optional) (e.g. Cognizant); What I sell (e.g. SAP S/4HANA migration and AMS services)

### Detailed prompt

```text
Act as my ERP-modernisation account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. caterpillar.com]
- Target platform: [e.g. SAP S/4HANA]
- Competitor or incumbent (optional): [e.g. Cognizant]
- What I sell: [one line, e.g. SAP S/4HANA migration and AMS services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in Finance & Accounting and IT, each marked direct (ERP named) or indirect (carve-out, integration, shared services, productivity programme), newest first, with linked tools and providers.
4. Current state: ERP products from the main ERP makers (SAP, Oracle, Infor, Microsoft, Epicor) and [Target platform]'s maker, 30 per page and at most 2 pages, with usage and last seen; group by vendor.
5. Capability: postings naming [Target platform] versus postings naming the main legacy ERP, 12 months: say which one hiring points to; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by engagements at [Company] involving ERP or [Target platform], top 10, no agencies or facilities firms. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in IT, then Finance & Accounting; keep ERP, applications, finance-systems, CIO or CFO titles; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on ERP, acquisitions, divestments, separations, productivity programmes or finance transformation; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Platform intent, Legacy exposure, Trigger (direct or indirect), Partner pattern, Owner clarity.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: ERP landscape (Vendor | Products, usage, last seen | Read).

RULES
- High legacy usage with legacy hiring far above [Target platform] hiring is "maintaining", not "migrating": score Platform intent low.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for ERP modernisation (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Show the 10 most recent ERP postings with title, date, location and platform named.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Hiring often points to a different ERP than the one you expect; follow the postings, not the logo.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for cybersecurity

- **id:** `plays-cyber-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy cybersecurity, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a security platform, managed security or security consolidation campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Hospitals & Healthcare Services); Country (e.g. United States of America); What I sell (e.g. managed detection and response and identity security)

### Detailed prompt

```text
Act as my cybersecurity target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Hospitals & Healthcare Services]
- Country: [HQ country in full, e.g. United States of America]
- What I sell: [one line, e.g. managed detection and response and identity security — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and country to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in the Cybersecurity workload, 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in Cybersecurity; top 15.
4. Incidents: one news search for breaches or ransomware at [Industry] companies in [Country], last 90 days; add up to 3 named companies.
5. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop security vendors, managed-security providers and IT-services firms, investors, off-industry rows and foreign companies' local teams.
6. One company-list lookup for the 10 by website: workforce, revenue, providers, and only security tools; note legacy on-premise tools and 3+ overlapping tools in one job (firewall, endpoint, SIEM, identity); work out postings per 1,000 employees.
7. Top 5 by provisional score: up to 5 priorities each in the Cybersecurity workload; if none, try the Cybersecurity technology area once.
8. One news search across the top 5 on breaches, regulatory actions, security leadership changes or acquisitions, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
9. Top 3: 3 executives each in Cybersecurity; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 9), the action and the dated why-now (step 8); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Incident 0–3 (3 = own incident in 90 days; 1 = earlier in 12 months); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (legacy on-premise or 3+ overlapping tools); Outsourcing 0–1 (3+ engagements); Priority 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Use incident facts as published; never speculate on cause, attacker or impact. Openers lead with help or a peer pattern, never the breach.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for cybersecurity on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A breach at a close peer is often as useful as one at the account: boards ask 'could that be us?'.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for security investment?

- **id:** `plays-cyber-readiness`
- **What you get:** A 0–20 readiness score for cybersecurity at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a security platform, managed security or security consolidation deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. unitedhealthgroup.com); Competitor or incumbent (optional) (e.g. Palo Alto Networks); What I sell (e.g. managed detection and response and identity security)

### Detailed prompt

```text
Act as my cybersecurity account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unitedhealthgroup.com]
- Competitor or incumbent (optional): [e.g. Palo Alto Networks]
- What I sell: [one line, e.g. managed detection and response and identity security — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in the Cybersecurity workload (if none, the Cybersecurity technology area once); keep security, identity, resilience or privacy priorities, newest first, with linked tools and providers.
4. Current state: security vendors ranked by products in the Cybersecurity workload, with top products; flag legacy on-premise tools and categories where 3+ vendors overlap (firewall, endpoint, SIEM, identity).
5. Capability: the top 15 skills in Cybersecurity postings; note incident-response and cloud-security skills; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by Cybersecurity engagements at [Company], top 10. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Cybersecurity; find the CISO or equivalent and anyone under a year in title; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on incidents, breaches, litigation, regulation, acquisitions or security leadership (check main subsidiaries too); if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Pressure (incident, litigation or regulation), Change (acquisition or new leader), Tool sprawl, Capacity gap, Stated intent.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Category | Vendors | Overlap or legacy flag).

RULES
- Use incident and litigation facts as published; never speculate on cause or impact, and never open outreach with them. Drop investor law-firm notices.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for cybersecurity (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Show every security tool with usage strength and last seen, by category.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Acquisitions are an underused security trigger: every integration brings identities, endpoints and networks to bring under control.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for generative AI

- **id:** `plays-genai-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy generative AI, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a generative AI platform, AI-agent or AI services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Insurance); Country (e.g. United Kingdom); What I sell (e.g. generative AI implementation and AI agent services)

### Detailed prompt

```text
Act as my generative-AI target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Insurance]
- Country: [HQ country in full, e.g. United Kingdom]
- What I sell: [one line, e.g. generative AI implementation and AI agent services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and country to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most naming Generative AI, Large Language Models, Prompt Engineering or Retrieval Augmented Generation, 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in Artificial Intelligence & Data Science; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop AI vendors and IT-services firms (flag subsidiaries with their parent), investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only AI and machine-learning tools, marking GenAI platforms (hosted model services, copilots, agent frameworks, retrieval tools); work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Generative AI priorities each (if none, Artificial Intelligence & Data Science, and say so).
7. One news search across the top 5 on GenAI launches, AI agents or AI partnerships, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Artificial Intelligence & Data Science; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = GenAI or agentic priority in the last 4 fiscal quarters; 2 = AI without GenAI); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (2 = two or more GenAI platforms); News 0–1 (dated launch); Outsourcing 0–1. Stage in Detail: Scaling, Piloting or Exploring.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Classic analytics or machine-learning tools alone are not GenAI evidence; drop generic chat widgets.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for generative AI on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Tools without a priority often mean pilots stuck short of production, which is a strong services opening.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for generative AI?

- **id:** `plays-genai-readiness`
- **What you get:** A 0–20 readiness score for generative AI at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a generative AI platform, AI-agent or AI services deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. allianz.com); Competitor or incumbent (optional) (e.g. Accenture); What I sell (e.g. generative AI implementation and AI agent services)

### Detailed prompt

```text
Act as my generative-AI account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. allianz.com]
- Competitor or incumbent (optional): [e.g. Accenture]
- What I sell: [one line, e.g. generative AI implementation and AI agent services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure). If it sells AI products, drop its own products throughout.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in the Generative AI technology area (if fewer than 3, add Artificial Intelligence & Data Science and say so), newest first, with linked tools and providers.
4. Current state: AI and machine-learning products with usage and last seen; mark GenAI platforms, copilots, agent frameworks and retrieval tools, and the 1–2 platforms they build on.
5. Capability: the top 15 skills in AI and data-science postings; call out GenAI, model-provider and governance skills; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by Artificial Intelligence & Data Science engagements at [Company], top 10. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Artificial Intelligence & Data Science; keep AI, data, digital, CTO or CDO titles; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on GenAI, AI agents, AI investments and partnerships; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Stated intent, Platform maturity, Skills and governance, Money committed, Delivery gap (4 = intent and platform ahead of hiring or partners).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: GenAI stack (Product | Type | Usage | Last seen).

RULES
- Classic analytics or ML tools alone are not GenAI evidence. A model-provider skill shows intent to use it, not a contract.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for generative AI (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Show the 10 most recent GenAI postings with title, date and tools named.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Model-provider names appearing as skills in job ads are often the clearest sign of which platform a company has picked.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for CX change

- **id:** `plays-cx-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy CX and contact-centre change, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a CX and contact-centre campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Insurance); Country (e.g. United States of America); Workloads (optional) (e.g. a type of work, default Customer Service & Support, Customer Success); Products that signal fit (optional) (e.g. Genesys Cloud CX, Amazon Connect); What I sell (e.g. contact-centre modernisation and CX managed services)

### Detailed prompt

```text
Act as my CX and contact-centre target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Insurance]
- Country: [HQ country in full, e.g. United States of America]
- Workloads (optional): [a type of work, default Customer Service & Support, Customer Success]
- Products that signal fit (optional): [e.g. Genesys Cloud CX, Amazon Connect]
- What I sell: [one line, e.g. contact-centre modernisation and CX managed services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop contact-centre operators, IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only contact-centre and CRM tools; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Customer Support & Service priorities each (add Sales & Marketing if I sell CRM).
7. One news search across the top 5 on contact centres, customer service, CRM, CX outsourcing, reshoring or vendor choices, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Customer Service & Support (customer care, contact-centre or chief customer titles); no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = service-cost, churn or self-service priority in the last 2 fiscal quarters); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (2 = old and new contact-centre products both active, or a platform first seen in 12 months); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Heavy outsourcing with no stated priority = "renewal watch", not ripe.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for CX and contact-centre change on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for CX change?

- **id:** `plays-cx-readiness`
- **What you get:** A 0–20 readiness score for CX and contact-centre change at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a CX and contact-centre deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. verizon.com); Workloads (optional) (e.g. a type of work, default Customer Service & Support, Customer Success); Competitor or incumbent (optional) (e.g. Genesys, or Concentrix); What I sell (e.g. contact-centre modernisation and CX managed services)

### Detailed prompt

```text
Act as my CX and contact-centre account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. verizon.com]
- Workloads (optional): [a type of work, default Customer Service & Support, Customer Success]
- Competitor or incumbent (optional): [e.g. Genesys, or Concentrix]
- What I sell: [one line, e.g. contact-centre modernisation and CX managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, Draup-estimated IT spend (direction only) and its split.
3. Intent: up to 6 priorities in Customer Support & Service, plus up to 3 whose name contains "contact", newest first, with linked tools and providers.
4. Current state: the stack in category Customer Service Software (if empty, [Workloads]), up to 30 rows; High or Medium usage in 6 months is core.
5. Capability: Customer Support & Service postings by workload (one big month is a batch, not a trend); last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; contact-centre operators count. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Customer Service & Support (customer care, contact-centre or chief customer titles); check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on contact centres, customer service, CRM, CX outsourcing, reshoring or vendor choices; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (service-cost or churn priority), Momentum, Change window (old and new contact-centre products both active), Budget (outsourcing share or savings target), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Low in-house hiring plus large outsourcing reads "buys, doesn't build". Layoffs or reshoring beside AI service programmes are triggers, not disqualifiers.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for CX and contact-centre change (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Which incumbent is weakest in the workloads I lead? Show its footprint.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Reshoring customer care or a big AI service programme changes which providers win; check who is in before you pitch.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for supply chain tech

- **id:** `plays-scm-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy supply chain planning and logistics tech, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a supply chain planning and logistics campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Food, Beverages & Consumer Goods); Country (e.g. United States of America); Workloads (optional) (e.g. a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution); Products that signal fit (optional) (e.g. SAP IBP, Kinaxis); What I sell (e.g. supply chain planning implementation and logistics technology services)

### Detailed prompt

```text
Act as my supply-chain technology target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Food, Beverages & Consumer Goods]
- Country: [HQ country in full, e.g. United States of America]
- Workloads (optional): [a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution]
- Products that signal fit (optional): [e.g. SAP IBP, Kinaxis]
- What I sell: [one line, e.g. supply chain planning implementation and logistics technology services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop logistics providers and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only tools in category Supply Chain & Logistics Software; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Supply Chain priorities each, with linked tools and providers.
7. One news search across the top 5 on network redesigns, distribution centres, planning platforms or separations, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Supply Chain; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = network, productivity or separation priority in the last 2 fiscal quarters); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (2 = an older planning tool beside a newer one, or a platform first seen in 12 months); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Cost or separation news counts only when it names supply chain or logistics.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for supply chain planning and logistics tech on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for SCM tech?

- **id:** `plays-scm-readiness`
- **What you get:** A 0–20 readiness score for supply chain planning and logistics tech at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a supply chain planning and logistics deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. unilever.com); Workloads (optional) (e.g. a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution, Warehousing); Competitor or incumbent (optional) (e.g. Kinaxis, or Capgemini); What I sell (e.g. supply chain planning implementation and logistics technology services)

### Detailed prompt

```text
Act as my supply-chain technology account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- Workloads (optional): [a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution, Warehousing]
- Competitor or incumbent (optional): [e.g. Kinaxis, or Capgemini]
- What I sell: [one line, e.g. supply chain planning implementation and logistics technology services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in Supply Chain, plus up to 3 whose name contains "cost", newest first, with linked tools and providers.
4. Current state: the stack in category Supply Chain & Logistics Software (if empty, [Workloads]), up to 30 rows; High or Medium usage in 6 months is core.
5. Capability: Supply Chain postings by workload; name the top 3 workloads; last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; split planning from execution where workloads show it. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Supply Chain; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on supply chain redesign, distribution centres, planning platforms, separations and logistics partners; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum, Change window (old and new planning tools both active, or a separation in 12 months), Budget (productivity programme naming supply chain), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Separations, mergers and divestments that move brands or plants are triggers.
- Drop linked tools that clearly belong elsewhere, and e-commerce or label tools.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for supply chain planning and logistics tech (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Which incumbent is weakest in the workloads I lead? Show its footprint.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Separations and divestments that move brands or plants force planning and logistics decisions fast.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for HR tech

- **id:** `plays-hcm-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy HR technology and HCM, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a HR technology and HCM campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Banking & Financial Services); Country (e.g. United Kingdom); Workloads (optional) (e.g. a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition); Products that signal fit (optional) (e.g. Workday HCM, SAP SuccessFactors, Oracle PeopleSoft); What I sell (e.g. HCM implementation, payroll consolidation and HR operations services)

### Detailed prompt

```text
Act as my HR-technology target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Banking & Financial Services]
- Country: [HQ country in full, e.g. United Kingdom]
- Workloads (optional): [a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition]
- Products that signal fit (optional): [e.g. Workday HCM, SAP SuccessFactors, Oracle PeopleSoft]
- What I sell: [one line, e.g. HCM implementation, payroll consolidation and HR operations services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop staffing firms, HR outsourcers and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only HR and payroll tools (category Human Capital Management Software (HCM)); work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Human Resources priorities each, with linked tools and providers.
7. One news search across the top 5 on HR systems, payroll, restructuring, mergers or HR leadership changes, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Human Resources; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = people, restructuring or HR-systems priority in the last 2 fiscal quarters); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (2 = two core HR or payroll systems at once, or an HCM platform first seen in 12 months); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Staffing suppliers are recruiting vendors, not HR-technology incumbents.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for HR technology and HCM on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for HR tech?

- **id:** `plays-hcm-readiness`
- **What you get:** A 0–20 readiness score for HR technology and HCM at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a HR technology and HCM deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. homedepot.com); Workloads (optional) (e.g. a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition); Competitor or incumbent (optional) (e.g. Workday, or Accenture); What I sell (e.g. HCM implementation, payroll consolidation and HR operations services)

### Detailed prompt

```text
Act as my HR-technology account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. homedepot.com]
- Workloads (optional): [a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition]
- Competitor or incumbent (optional): [e.g. Workday, or Accenture]
- What I sell: [one line, e.g. HCM implementation, payroll consolidation and HR operations services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in Human Resources, plus up to 3 whose name contains "workforce", newest first, with linked tools and providers.
4. Current state: the stack in category Human Capital Management Software (HCM) (if empty, [Workloads]), up to 30 rows; High or Medium usage in 6 months is core.
5. Capability: Human Resources postings by workload, focusing on HR systems and HR operations roles; last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; if most are staffing firms with one engagement each, say "HR services are open ground". If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Human Resources; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on HR systems, payroll, restructuring and HR leadership changes; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum, Change window (two systems doing one job, or a platform added in 12 months), Budget (restructuring or workforce programme), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Drop education, childcare and other misfiled HR tools. Staffing firms are recruiting suppliers, not HCM incumbents.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for HR technology and HCM (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Which incumbent is weakest in the workloads I lead? Show its footprint.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- A new HR leader in their first year often reviews systems and partners.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for AMS deals

- **id:** `plays-ams-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy AMS and IT managed services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a AMS and IT managed-services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Life Sciences); Country (e.g. United States of America); Workloads (optional) (e.g. a type of work, default Application Development & Maintenance, Infrastructure Management System); What I sell (e.g. application management and IT infrastructure managed services)

### Detailed prompt

```text
Act as my AMS and IT managed-services target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Life Sciences]
- Country: [HQ country in full, e.g. United States of America]
- Workloads (optional): [a type of work, default Application Development & Maintenance, Infrastructure Management System]
- What I sell: [one line, e.g. application management and IT infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in the IT function, 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop IT-services firms and captives, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers; work out postings per 1,000 employees.
6. Top 5 by provisional score: each one's providers in [Workloads] (up to 50) for count, top-3 share and long tail; top 3: IT priorities containing "cost".
7. One news search across the top 5 on separations, divestments, IT outsourcing, vendor consolidation, cost programmes or IT layoffs, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in IT (Application Development & Maintenance or Infrastructure Management System); keep applications, infrastructure, CIO or CTO titles; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Fragmentation 0–3 (3 = 15+ long-tail providers or top 3 under 50%; 2 = top 3 at 50–75%); Hiring 0–3 (thirds by IT postings per 1,000); Priority 0–2 (2 = cost programme naming technology; 1 = other savings); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Drop agencies, staffing firms, "Self" and captives (names containing the company's name) from provider counts; never recommend catch-all workloads such as Account Management.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for AMS and IT managed services on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A long tail of small providers is the clearest consolidation signal; one entrenched incumbent is a displacement play.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for AMS consolidation?

- **id:** `plays-ams-readiness`
- **What you get:** A 0–20 readiness score for AMS and IT managed services at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a AMS and IT managed-services deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. pfizer.com); Workloads (optional) (e.g. a type of work, default Application Development & Maintenance, Infrastructure Management System); Competitor or incumbent (optional) (e.g. Accenture); What I sell (e.g. application management and IT infrastructure managed services)

### Detailed prompt

```text
Act as my AMS and IT managed-services account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. pfizer.com]
- Workloads (optional): [a type of work, default Application Development & Maintenance, Infrastructure Management System]
- Competitor or incumbent (optional): [e.g. Accenture]
- What I sell: [one line, e.g. application management and IT infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, Draup-estimated IT spend (direction only) and its split.
3. Intent: up to 6 priorities in IT, plus up to 3 IT priorities whose name contains "cost", newest first, with linked tools and providers.
4. Current state: providers ranked by active engagements in [Workloads], up to 50: count, top-3 share and long tail (1–2 engagements).
5. Capability: IT postings by workload; rising in-house hiring in an outsourced workload is a re-insourcing flag; last 5 full months vs the 5 before.
6. Incumbents: the top 10 providers from step 4 with their share. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in IT, in Application Development & Maintenance or Infrastructure Management System; keep applications, infrastructure, platforms, CIO or CTO titles; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on separations, divestments, IT outsourcing, vendor consolidation, cost programmes and IT layoffs; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (savings programme naming technology), Momentum (rising in-house IT hiring = re-insourcing risk), Fragmentation, Budget, Trigger (separation or cost programme).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: provider landscape (Provider | Engagements | Share); captives separately.

RULES
- Drop agencies, staffing firms, "Self" and captives from provider counts; list captives separately. Never recommend catch-all workloads (Project/Programs Management, Account Management).
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for AMS and IT managed services (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Which incumbent is weakest in the workloads I lead? Show its footprint.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- A spin-off or business sale usually creates transition and application-split work for 12 to 24 months.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for ER&D services

- **id:** `plays-erd-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy engineering and R&D services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a engineering and R&D services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Automotive); Country (e.g. Germany); Workloads (optional) (e.g. a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development); Engineering service rivals (optional) (e.g. LTTS, Capgemini, Cyient); What I sell (e.g. embedded software and product engineering services)

### Detailed prompt

```text
Act as my engineering and R&D services target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Automotive]
- Country: [HQ country in full, e.g. Germany]
- Workloads (optional): [a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development]
- Engineering service rivals (optional): [e.g. LTTS, Capgemini, Cyient]
- What I sell: [one line, e.g. embedded software and product engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in the ER&D function (broader and more reliable than niche engineering workloads), 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop engineering-services firms and captives, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers; work out postings per 1,000 employees.
6. Top 5 by provisional score: rank each one's engineering providers in [Workloads] (one pull each), marking captives. For the top 3, up to 3 ER&D priorities.
7. One news search across the top 5 on R&D programmes, engineering centres, new platforms or engineering partnerships, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in ER&D; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Provider mix 0–3 (3 = top 3 under 60% excluding captives, or a new engineering centre in 12 months); Hiring 0–3 (thirds by ER&D postings per 1,000); Priority 0–2 (2 = R&D programme shift in the last 4 fiscal quarters); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Captives (names containing the company's name) are in-house, not rivals; show them separately.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for engineering and R&D services on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Hiring by the ER&D function is broader and more reliable than niche engineering workloads.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for ER&D services?

- **id:** `plays-erd-readiness`
- **What you get:** A 0–20 readiness score for engineering and R&D services at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a engineering and R&D services deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. bosch.com); Workloads (optional) (e.g. a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development); Competitor or incumbent (optional) (e.g. LTTS); What I sell (e.g. embedded software and product engineering services)

### Detailed prompt

```text
Act as my engineering and R&D services account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. bosch.com]
- Workloads (optional): [a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development]
- Competitor or incumbent (optional): [e.g. LTTS]
- What I sell: [one line, e.g. embedded software and product engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated R&D spend and growth.
3. Intent: up to 6 priorities in ER&D, plus up to 3 whose name contains "engineering", newest first, with linked tools and providers.
4. Current state: engineering providers ranked by active engagements in [Workloads], marking captives (names containing the company's name) as in-house.
5. Capability: ER&D postings by workload; flag [Workloads] that slow while priorities grow; last 5 full months vs the 5 before.
6. Incumbents: the top 10 providers from step 4, captives left out of share. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in ER&D; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on R&D programmes, engineering centres, new platforms and engineering partnerships; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (R&D programme shift), Momentum, Provider mix (4 = top 3 under 60% excluding captives), Budget (R&D spend growing), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: provider landscape with captives marked; R&D spend (Draup-estimated).

RULES
- Captives are in-house: show them, never count them as rivals.
- Private with no revenue or R&D spend: write "Not in Draup" and score Budget 2. If [Workloads] return little, use the top ER&D workloads from step 5 and say so.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for engineering and R&D services (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Which incumbent is weakest in the workloads I lead? Show its footprint.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Captive engineering centres take new work first; find out what they can't absorb.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for testing services

- **id:** `plays-qe-targets`
- **What you get:** A ranked list of companies in your industry and country most ready to buy quality engineering and testing, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a quality engineering and testing campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Banking & Financial Services); Country (e.g. India); Workloads (optional) (e.g. a type of work, default Software Testing, Quality Assurance); Testing tools that signal fit (optional) (e.g. Tricentis Tosca, Selenium, Micro Focus UFT); What I sell (e.g. test automation and quality engineering services)

### Detailed prompt

```text
Act as my quality-engineering target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Banking & Financial Services]
- Country: [HQ country in full, e.g. India]
- Workloads (optional): [a type of work, default Software Testing, Quality Assurance]
- Testing tools that signal fit (optional): [e.g. Tricentis Tosca, Selenium, Micro Focus UFT]
- What I sell: [one line, e.g. test automation and quality engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, country and workloads to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in [Workloads], 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop testing and IT-services firms, investors, off-industry rows and foreign companies' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, and only testing tools (makers of [Testing tools that signal fit]), leaving out manufacturing quality-management tools; work out postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 IT priorities each, with linked tools and providers.
7. One news search across the top 5 on software quality, release failures, outages tied to releases, core-system changes or regulatory deadlines, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
8. Top 3: 3 executives each in [Workloads], falling back to IT; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 8), the action and the dated why-now (step 7); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = core-system change, digital launch or regulatory deadline in the last 2 fiscal quarters); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (2 = a fading commercial test tool, or an automation tool first seen in 12 months); Outsourcing 0–1 (top third); News 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Outages count only when tied to a release or code change.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Country] for quality engineering and testing on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run the readiness check on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these run a competitor I name? Rate each Red, Amber or Green.

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Foreign banks' local testing centres often out-hire local banks; they're a centre-of-excellence motion, not the ranked list.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for QE services?

- **id:** `plays-qe-readiness`
- **What you get:** A 0–20 readiness score for quality engineering and testing at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a quality engineering and testing deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. ford.com); Workloads (optional) (e.g. a type of work, default Software Testing, Quality Assurance); Competitor or incumbent (optional) (e.g. Wipro, or Tricentis); What I sell (e.g. test automation and quality engineering services)

### Detailed prompt

```text
Act as my quality-engineering account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. ford.com]
- Workloads (optional): [a type of work, default Software Testing, Quality Assurance]
- Competitor or incumbent (optional): [e.g. Wipro, or Tricentis]
- What I sell: [one line, e.g. test automation and quality engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in IT and ER&D, plus up to 3 whose name contains "quality"; only software-quality priorities count, newest first, with linked tools and providers.
4. Current state: the testing stack for [Workloads], up to 30 rows, dropping manufacturing quality-management tools; High or Medium usage seen in 6 months is core.
5. Capability: testing postings in IT and ER&D; under 60 a year (editable) means in-house testing is small; last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; flag joint ventures or captives as in-house. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in [Workloads], falling back to IT, then ER&D; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on software quality, recalls or outages tied to software, release failures and core-system changes; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum, Change window (a fading commercial tool listed, or a software recall in 6 months), Budget (warranty, quality or cost programme), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Recalls or outages count only when tied to software or updates; plant quality goes in Entry angle.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: score [Company]'s readiness for quality engineering and testing (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

### Follow-ups

- Map the buying committee around the owner you found.
- Turn the entry angle into a 100-word email to the person in the next step.
- Which incumbent is weakest in the workloads I lead? Show its footprint.
- Re-score after I tell you what I learned in discovery.

### Tips

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- A software recall or failed over-the-air update is the strongest testing trigger; lead with help, not the incident.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.
