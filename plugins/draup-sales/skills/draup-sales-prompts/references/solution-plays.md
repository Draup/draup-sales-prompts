# Solution plays: by what you sell

Find the accounts most ready for what you sell, and check any account's readiness: cloud, data & AI, ERP, security, GenAI, CX, supply chain, HR tech, managed services, engineering, testing.

## Find accounts ripe for cloud migration

- **id:** `plays-cloud-targets`
- **What you get:** A ranked list of companies in your industry and territory most ready to buy cloud migration, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a cloud or infrastructure-modernisation campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for cloud migration?" instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Aerospace & Defense); Territory (optional) (e.g. United States of America); What I sell (e.g. cloud migration and managed cloud services)

### Detailed prompt

```text
Act as my cloud-migration target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Aerospace & Defense]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. cloud migration and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in Cloud Computing and Infrastructure Management System, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in those workloads plus Legacy Modernization and Data Centre Management; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop cloud providers, IT resellers and services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, cloud and infrastructure tools only; postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 priorities each in those four workloads, newest first; count only those naming infrastructure, cloud, data centre, platform or core-system modernisation.
7. One news search across the top 5 on modernisation, cloud, data-centre or infrastructure deals, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Cloud Computing or Infrastructure Management System.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Priority 0–3 (3 = modernisation priority in the last 4 fiscal quarters, 2 = older or news-sourced, 1 = related IT priority, 0 = none); Stack 0–2 (2 = migration tooling, or public cloud beside on-premise virtualisation; 1 = public cloud only); Outsourcing 0–1 (5+ engagements); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (e.g. data-centre or automation vendors, SaaS platforms); list them under Dropped. Government IT contractors are providers, not buyers.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for cloud migration on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for cloud migration?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A migration tool showing in the stack is often a sign a programme is already under way.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for cloud migration?

- **id:** `plays-cloud-readiness`
- **What you get:** A 0–20 readiness score for cloud migration at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a cloud or infrastructure-modernisation deal, or ahead of a first meeting. Use "Find accounts ripe for cloud migration" instead to find accounts.
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
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, Draup-estimated IT spend and its split (direction only).
3. Intent: up to 6 priorities in Cloud Computing, Infrastructure Management System, Legacy Modernization, Data Centre Management and DevOps, newest first, with linked tools and providers; count only those naming infrastructure, cloud, data centre, platform or core-system modernisation.
4. Current state: vendors ranked by products in the cloud, infrastructure and data-centre workloads, split public cloud vs on-premise (virtualisation, mainframe, Unix, servers, storage).
5. Capability: IT postings by workload, then the top 15 skills in cloud, infrastructure and DevOps postings; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by active engagements at [Company] in the step-3 workloads, top 10, no agencies or staffing firms. Check any rival I named across the whole stack.
7. Owner: executives in Cloud Computing or Infrastructure Management System; keep cloud, infrastructure, platform, CTO or CIO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on modernisation, cloud, data centres, acquisitions, separations or cost programmes; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Intent (dated modernisation priority), On-premise gap, Capacity gap (4 = thin cloud hiring beside a modernisation push), Buying pattern (active infrastructure outsourcing), Timing (dated trigger).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Area | Vendors | Read); IT split (direction only).

RULES
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy data-platform modernisation, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a data-platform, lakehouse or analytics campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for data platforms?" instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Banking & Financial Services); Territory (optional) (e.g. United States of America); What I sell (e.g. lakehouse modernisation and analytics services)

### Detailed prompt

```text
Act as my data-platform target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Banking & Financial Services]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. lakehouse modernisation and analytics services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in Data Engineering and Business Intelligence & Analytics, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in those two workloads; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents and the same company under different names (e.g. Cigna / The Cigna Group); drop technology and data vendors, IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, data tools only, legacy (Hadoop, Teradata, Informatica PowerCenter, on-premise warehouses) or modern; postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 priorities each in those workloads plus Artificial Intelligence & Data Science, newest first; count only those naming data, analytics or a data outcome.
7. One news search across the top 5 on data, analytics or data-platform deals, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Data Engineering or Business Intelligence & Analytics.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Priority 0–3 (3 = data priority tied to an outcome in the last 4 fiscal quarters, 2 = older, 1 = data named without an outcome, 0 = none); Stack 0–2 (2 = legacy tools visible, 1 = modern only); Outsourcing 0–1 (20+ engagements); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (data vendors, banks selling data services); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for data-platform modernisation on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for data platforms?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Legacy and modern tools side by side usually means a migration is under way: ask what is left to move.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for data platforms?

- **id:** `plays-data-readiness`
- **What you get:** A 0–20 readiness score for data-platform modernisation at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a data-platform, lakehouse or analytics deal, or ahead of a first meeting. Use "Find accounts ripe for data platforms" instead to find accounts.
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
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in Data Engineering, Business Intelligence & Analytics and Artificial Intelligence & Data Science naming data, analytics or a data outcome, newest first.
4. Current state: vendors ranked by products in Data Engineering and Business Intelligence & Analytics, sorted into legacy (Hadoop, Teradata, Informatica PowerCenter, older BI) and modern.
5. Capability: the top 15 data skills in postings, noting legacy and rising skills; last 5 full months vs the 5 before.
6. Incumbents: providers by active engagements at [Company] in the step-3 workloads, top 10, no agencies or research firms. Check any rival I named across the whole stack.
7. Owner: executives in Data Engineering or Business Intelligence & Analytics; keep data, analytics, CDO or CTO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on data platforms, AI, leadership changes or acquisitions; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Intent, Legacy gap (legacy platforms still in use), Capability gap (4 = legacy skills still hired, platform skills rising), Buying pattern, Timing.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Layer | Legacy | Modern | Read).

RULES
- Legacy skills in current job ads mean the old platform isn't retired; check usage before calling a vendor the standard.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy ERP modernisation, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building an S/4HANA, Oracle Cloud ERP or other ERP campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for ERP modernisation?" instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Industrial); Territory (optional) (e.g. Germany); Target platform (e.g. SAP S/4HANA); Legacy platform (optional) (e.g. SAP ERP (ECC)); What I sell (e.g. SAP S/4HANA migration and AMS services)

### Detailed prompt

```text
Act as my ERP-modernisation target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Industrial]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. Germany]
- Target platform: [e.g. SAP S/4HANA]
- Legacy platform (optional): [e.g. SAP ERP (ECC)]
- What I sell: [one line, e.g. SAP S/4HANA migration and AMS services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, platforms and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings for [Target platform] (Draup's skill name; if 0, retry with the product name), 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Target platform] or [Legacy platform] work; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop ERP vendors and IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, main-maker ERP products only, each labelled Not started (legacy only), Mid-migration, Moved or Other ERP; postings per 1,000 employees.
6. Top 5 by provisional score: up to 6 Finance & Accounting and IT priorities each, direct (ERP named) or indirect.
7. One news search across the top 5 on ERP, carve-outs or acquisitions, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in IT, then Finance & Accounting (ERP or CIO titles).

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); ERP status 0–2 (Not started or Mid-migration 2, Other ERP 1, Moved 0); Trigger 0–3 (3 = carve-out, acquisition or finance change in 12 months, 2 = indirect priority, 1 = older, 0 = none); Outsourcing 0–1 (3+ engagements); Named programme 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Never call an indirect trigger a confirmed ERP project.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (ERP software or services); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for ERP modernisation on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for ERP modernisation?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Carve-outs and divestments are among the strongest ERP triggers: the separated business needs its own system, fast.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for ERP modernisation?

- **id:** `plays-erp-readiness`
- **What you get:** A 0–20 readiness score for ERP modernisation at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for an S/4HANA, Oracle Cloud ERP or other ERP deal, or ahead of a first meeting. Use "Find accounts ripe for ERP modernisation" instead to find accounts.
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
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 Finance & Accounting and IT priorities, marked direct (ERP named) or indirect (carve-out, integration, shared services), newest first.
4. Current state: ERP products from the main makers (SAP, Oracle, Infor, Microsoft, Epicor) and [Target platform]'s maker, up to 60 rows, with usage and last seen, by vendor.
5. Capability: postings for [Target platform] (Draup's skill name; if 0, retry with the product name) vs the main legacy ERP, 12 months: which way hiring points; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by engagements at [Company] involving ERP or [Target platform], top 10, no agencies. Check any rival I named across the whole stack.
7. Owner: executives in IT, then Finance & Accounting; keep ERP, CIO or CFO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on ERP, acquisitions, divestments, separations or finance transformation; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Platform intent, Legacy exposure, Trigger (direct or indirect), Partner pattern, Owner clarity.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: ERP landscape (Vendor | Products, usage, last seen | Read).

RULES
- High legacy usage with legacy hiring far above [Target platform] hiring is "maintaining", not "migrating": score Platform intent low.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy cybersecurity, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a security platform, managed security or security consolidation campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for security investment?" instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Hospitals & Healthcare Services); Territory (optional) (e.g. United States of America); What I sell (e.g. managed detection and response)

### Detailed prompt

```text
Act as my cybersecurity target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Hospitals & Healthcare Services]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. managed detection and response — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in the Cybersecurity workload, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in Cybersecurity; top 15.
4. Incidents: one 90-day news search for breaches or ransomware at [Industry] companies in [Territory]; add up to 3 named.
5. Long list of 10, both lists first: merge subsidiaries into parents; drop security vendors and service firms, investors, off-industry rows and foreign firms' local teams.
6. One company-list lookup for the 10 by website: workforce, revenue, providers, security tools only, noting legacy on-premise and 3+ overlapping tools in one job; postings per 1,000 employees.
7. Top 5 by provisional score: up to 5 Cybersecurity priorities each (none: the Cybersecurity technology area).
8. One news search across the top 5 on breaches, regulation, security leaders or acquisitions, last 90 days; else each one's most material dated event, labelled indirect.
9. Top 3: 3 executives each in Cybersecurity.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Incident 0–3 (3 = own incident in 90 days, 2 = subsidiary incident or regulatory action in 90 days, 1 = earlier in 12 months, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = legacy on-premise and 3+ overlapping tools, 1 = either); Outsourcing 0–1 (3+ engagements); Priority 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Quote incidents as published, no speculation on cause or impact; openers lead with help or a peer pattern, never the breach.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (security software or managed security); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for cybersecurity on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for security investment?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A breach at a close peer is often as useful as one at the account: boards ask 'could that be us?'.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for security investment?

- **id:** `plays-cyber-readiness`
- **What you get:** A 0–20 readiness score for cybersecurity at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a security platform, managed security or security consolidation deal, or ahead of a first meeting. Use "Find accounts ripe for cybersecurity" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. unitedhealthgroup.com); Competitor or incumbent (optional) (e.g. Palo Alto Networks); What I sell (e.g. managed detection and response)

### Detailed prompt

```text
Act as my cybersecurity account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unitedhealthgroup.com]
- Competitor or incumbent (optional): [e.g. Palo Alto Networks]
- What I sell: [one line, e.g. managed detection and response — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in the Cybersecurity workload (if none, the Cybersecurity technology area once); keep security, identity, resilience or privacy priorities, newest first.
4. Current state: security vendors ranked by products in the Cybersecurity workload, with top products; flag legacy on-premise tools and categories where 3+ vendors overlap (firewall, endpoint, SIEM, identity).
5. Capability: the top 15 skills in Cybersecurity postings; note incident-response and cloud-security skills; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by Cybersecurity engagements at [Company], top 10. Check any rival I named across the whole stack.
7. Owner: executives in Cybersecurity; find the CISO or equivalent and anyone under a year in title. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on incidents, breaches, litigation, regulation, acquisitions or security leadership (check main subsidiaries too); if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Pressure (incident, litigation or regulation), Change (acquisition or new leader), Tool sprawl, Capacity gap, Stated intent.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Category | Vendors | Overlap or legacy flag).

RULES
- Use incident and litigation facts as published; never speculate on cause or impact, and never open outreach with them. Drop investor law-firm notices.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy generative AI, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a generative AI platform, AI-agent or AI services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for generative AI?" instead when you already have one account.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Insurance); Territory (optional) (e.g. United Kingdom); What I sell (e.g. generative AI implementation and AI agent services)

### Detailed prompt

```text
Act as my generative-AI target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Insurance]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United Kingdom]
- What I sell: [one line, e.g. generative AI implementation and AI agent services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in postings naming Generative AI, Large Language Models, Prompt Engineering or Retrieval Augmented Generation, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in Artificial Intelligence & Data Science; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop AI vendors and IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, AI and machine-learning tools only, marking GenAI platforms (hosted models, copilots, agents, retrieval); postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Generative AI priorities each (if none, Artificial Intelligence & Data Science; say so).
7. One news search across the top 5 on GenAI launches, AI agents or AI partnerships, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Artificial Intelligence & Data Science.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = GenAI or agentic priority in the last 4 fiscal quarters, 2 = AI without GenAI, 1 = older AI priority, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = two or more GenAI platforms, 1 = one); News 0–1 (dated launch); Outsourcing 0–1. Stage in Detail: Scaling, Piloting or Exploring.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Classic analytics or machine-learning tools alone are not GenAI evidence; drop generic chat widgets.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (AI software or platforms); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for generative AI on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for generative AI?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Tools without a priority often mean pilots stuck short of production, which is a strong services opening.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for generative AI?

- **id:** `plays-genai-readiness`
- **What you get:** A 0–20 readiness score for generative AI at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a generative AI platform, AI-agent or AI services deal, or ahead of a first meeting. Use "Find accounts ripe for generative AI" instead to find accounts.
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
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in the Generative AI technology area (if fewer than 3, add Artificial Intelligence & Data Science and say so), newest first.
4. Current state: AI and machine-learning products with usage and last seen; mark GenAI platforms, copilots, agent frameworks and retrieval tools, and the 1–2 platforms they build on.
5. Capability: the top 15 skills in AI and data-science postings; call out GenAI, model-provider and governance skills; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by Artificial Intelligence & Data Science engagements at [Company], top 10. Check any rival I named across the whole stack.
7. Owner: executives in Artificial Intelligence & Data Science; keep AI, data, digital, CTO or CDO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on GenAI, AI agents, AI investments and partnerships; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Stated intent, Platform maturity, Skills and governance, Money committed, Delivery gap (4 = intent and platform ahead of hiring or partners).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: GenAI stack (Product | Type | Usage | Last seen).

RULES
- Classic analytics or ML tools alone are not GenAI evidence. A model-provider skill shows intent to use it, not a contract.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy CX and contact-centre change, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a CX and contact-centre campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for CX change?" instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Insurance); Territory (optional) (e.g. United States of America); Workloads (optional) (e.g. a type of work, default Customer Service & Support, Customer Success); Products that signal fit (optional) (e.g. Genesys Cloud CX); What I sell (e.g. contact-centre modernisation services)

### Detailed prompt

```text
Act as my CX and contact-centre target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Insurance]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- Workloads (optional): [a type of work, default Customer Service & Support, Customer Success]
- Products that signal fit (optional): [e.g. Genesys Cloud CX]
- What I sell: [one line, e.g. contact-centre modernisation services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop contact-centre and IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, contact-centre and CRM tools only; postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Customer Support & Service priorities each (plus Sales & Marketing for CRM).
7. One news search across the top 5 on contact centres, CRM, CX outsourcing or reshoring, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Customer Service & Support.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = service-cost, churn or self-service priority in the last 2 fiscal quarters, 2 = older, 1 = other service priority, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = old and new contact-centre products both active, or one new in 12 months; 1 = one platform); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Heavy outsourcing, no stated priority = "renewal watch".
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (CX software or services); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for CX and contact-centre change on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for CX change?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for CX change?

- **id:** `plays-cx-readiness`
- **What you get:** A 0–20 readiness score for CX and contact-centre change at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a CX and contact-centre deal, or ahead of a first meeting. Use "Find accounts ripe for CX change" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. verizon.com); Workloads (optional) (e.g. a type of work, default Customer Service & Support, Customer Success); Competitor or incumbent (optional) (e.g. Genesys, or Concentrix); What I sell (e.g. contact-centre modernisation services)

### Detailed prompt

```text
Act as my CX and contact-centre account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. verizon.com]
- Workloads (optional): [a type of work, default Customer Service & Support, Customer Success]
- Competitor or incumbent (optional): [e.g. Genesys, or Concentrix]
- What I sell: [one line, e.g. contact-centre modernisation services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth; Draup-estimated IT spend and split (direction only).
3. Intent: up to 6 Customer Support & Service priorities plus up to 3 named "contact", newest first.
4. Current state: the stack in category Customer Service Software (if empty, [Workloads]), up to 30 rows; High or Medium usage in 6 months = core.
5. Capability: Customer Support & Service postings by workload; last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; contact-centre operators count. Check any rival I named across the whole stack.
7. Owner: executives in Customer Service & Support; keep customer care or contact-centre titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on contact centres, CRM, CX outsourcing or reshoring; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (service-cost or churn priority), Momentum (4 = service postings or programmes rising; 0 = falling), Change window (old and new contact-centre products both active), Budget (savings target), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Low in-house hiring plus large outsourcing reads "buys, doesn't build". Layoffs or reshoring beside AI service programmes are triggers.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy supply chain planning and logistics tech, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a supply chain planning and logistics campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for supply-chain tech?" instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Food, Beverages & Consumer Goods); Territory (optional) (e.g. United States of America); Workloads (optional) (e.g. a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution); Products that signal fit (optional) (e.g. Kinaxis); What I sell (e.g. supply-chain planning services)

### Detailed prompt

```text
Act as my supply-chain technology target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Food, Beverages & Consumer Goods]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- Workloads (optional): [a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution]
- Products that signal fit (optional): [e.g. Kinaxis]
- What I sell: [one line, e.g. supply-chain planning services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop logistics and IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, tools in category Supply Chain & Logistics Software only; postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Supply Chain priorities each.
7. One news search across the top 5 on network redesigns, distribution centres or planning platforms, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Supply Chain.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = network, productivity or separation priority in the last 2 fiscal quarters, 2 = older, 1 = other, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = old and new planning tools side by side, or one new in 12 months; 1 = one tool); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Cost or separation news counts only if it names supply chain.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (supply-chain software or logistics); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for supply chain planning and logistics tech on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for supply-chain tech?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for supply-chain tech?

- **id:** `plays-scm-readiness`
- **What you get:** A 0–20 readiness score for supply chain planning and logistics tech at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a supply chain planning and logistics deal, or ahead of a first meeting. Use "Find accounts ripe for supply chain tech" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. unilever.com); Workloads (optional) (e.g. a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution, Warehousing); Competitor or incumbent (optional) (e.g. Kinaxis, or Capgemini); What I sell (e.g. supply-chain planning services)

### Detailed prompt

```text
Act as my supply-chain technology account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- Workloads (optional): [a type of work, default Demand Management, Supply Chain Analytics, Logistics & Distribution, Warehousing]
- Competitor or incumbent (optional): [e.g. Kinaxis, or Capgemini]
- What I sell: [one line, e.g. supply-chain planning services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 Supply Chain priorities plus up to 3 named "cost", newest first.
4. Current state: the stack in category Supply Chain & Logistics Software (if empty, [Workloads]), up to 30 rows; High or Medium usage in 6 months = core.
5. Capability: Supply Chain postings by workload; last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; split planning from execution. Check any rival I named across the whole stack.
7. Owner: executives in Supply Chain; keep supply chain, planning or logistics titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on network redesign, distribution centres, planning platforms or separations; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum (4 = supply chain postings or programmes rising; 0 = falling), Change window (old and new planning tools both active, or a separation in 12 months), Budget (productivity programme), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Separations and divestments that move brands or plants are triggers. Drop e-commerce, label and misfiled linked tools.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy HR technology and HCM, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building an HR technology and HCM campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for HR tech?" instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Banking & Financial Services); Territory (optional) (e.g. United Kingdom); Workloads (optional) (e.g. a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition); Products that signal fit (optional) (e.g. Workday HCM, Oracle PeopleSoft); What I sell (e.g. HCM implementation and payroll services)

### Detailed prompt

```text
Act as my HR-technology target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Banking & Financial Services]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United Kingdom]
- Workloads (optional): [a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition]
- Products that signal fit (optional): [e.g. Workday HCM, Oracle PeopleSoft]
- What I sell: [one line, e.g. HCM implementation and payroll services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in [Workloads] or naming [Products that signal fit], 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop staffing firms, HR outsourcers, IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, tools in category Human Capital Management Software (HCM) only; postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Human Resources priorities each.
7. One news search across the top 5 on HR systems, payroll, restructuring or HR leadership, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Human Resources.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = people, restructuring or HR-systems priority in the last 2 fiscal quarters, 2 = older, 1 = other, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = two core HR or payroll systems at once, or one new in 12 months; 1 = one system); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Staffing suppliers are recruiting vendors, not HR-technology incumbents.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (HR software or outsourcing); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for HR technology and HCM on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for HR tech?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Edit the workloads to match exactly what you deliver; the hiring and outsourcing rankings follow them.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for HR tech?

- **id:** `plays-hcm-readiness`
- **What you get:** A 0–20 readiness score for HR technology and HCM at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for an HR technology and HCM deal, or ahead of a first meeting. Use "Find accounts ripe for HR tech" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. homedepot.com); Workloads (optional) (e.g. a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition); Competitor or incumbent (optional) (e.g. Workday, or Accenture); What I sell (e.g. HCM implementation and payroll services)

### Detailed prompt

```text
Act as my HR-technology account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. homedepot.com]
- Workloads (optional): [a type of work, default HRIS & Analytics, Workforce Administration & Management, Payroll, Talent Acquisition]
- Competitor or incumbent (optional): [e.g. Workday, or Accenture]
- What I sell: [one line, e.g. HCM implementation and payroll services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 Human Resources priorities plus up to 3 named "workforce", newest first.
4. Current state: the stack in category Human Capital Management Software (HCM) (if empty, [Workloads]), up to 30 rows; High or Medium usage in 6 months = core.
5. Capability: Human Resources postings by workload; last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10 (mostly one-engagement staffing firms: "HR services are open ground"). Check any rival I named across the whole stack.
7. Owner: executives in Human Resources; keep HR, HR-systems or payroll titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on HR systems, payroll, restructuring or HR leaders; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum (4 = HR-systems postings or programmes rising; 0 = falling), Change window (two systems doing one job, or one added in 12 months), Budget (restructuring programme), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Drop misfiled HR tools (education, childcare). Staffing firms are recruiting suppliers, not HCM incumbents.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
- **What you get:** A ranked list of companies in your industry and territory most ready to buy AMS and IT managed services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building an AMS and IT managed-services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for AMS consolidation?" instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Life Sciences); Territory (optional) (e.g. United States of America); Workloads (optional) (e.g. a type of work, default Application Development & Maintenance, Infrastructure Management System); What I sell (e.g. application and infrastructure managed services)

### Detailed prompt

```text
Act as my AMS and IT managed-services target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Life Sciences]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- Workloads (optional): [a type of work, default Application Development & Maintenance, Infrastructure Management System]
- What I sell: [one line, e.g. application and infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in the IT function, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop IT-services firms and captives, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers; postings per 1,000 employees.
6. Top 5 by provisional score: each one's providers in [Workloads] (up to 50): count, top-3 share, long tail; for the top 3, IT priorities named "cost".
7. One news search across the top 5 on separations, IT outsourcing, vendor consolidation, cost programmes or IT layoffs, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 IT executives each (applications, infrastructure, CIO or CTO titles).

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Hiring 0–3 (IT postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Fragmentation 0–3 (3 = 15+ long-tail providers or top 3 under 50%, 2 = 50–75%, 1 = 75–90%, 0 = one provider over 90%); Priority 0–2 (2 = cost programme naming technology, 1 = other savings, 0 = none); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Drop agencies, staffing firms, "Self" and captives (names containing the company's name) from provider counts; never recommend catch-all workloads.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (IT services or enterprise software); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for AMS and IT managed services on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for AMS consolidation?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A long tail of small providers is the clearest consolidation signal; one entrenched incumbent is a displacement play.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for AMS consolidation?

- **id:** `plays-ams-readiness`
- **What you get:** A 0–20 readiness score for AMS and IT managed services at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for an AMS and IT managed-services deal, or ahead of a first meeting. Use "Find accounts ripe for AMS deals" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. pfizer.com); Workloads (optional) (e.g. a type of work, default Application Development & Maintenance, Infrastructure Management System); Competitor or incumbent (optional) (e.g. Accenture); What I sell (e.g. application and infrastructure managed services)

### Detailed prompt

```text
Act as my AMS and IT managed-services account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. pfizer.com]
- Workloads (optional): [a type of work, default Application Development & Maintenance, Infrastructure Management System]
- Competitor or incumbent (optional): [e.g. Accenture]
- What I sell: [one line, e.g. application and infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth; Draup-estimated IT spend and split (direction only).
3. Intent: up to 6 IT priorities plus up to 3 named "cost", newest first.
4. Current state: providers ranked by active engagements in [Workloads], up to 50: count, top-3 share and long tail (1–2 engagements).
5. Capability: IT postings by workload (rising in-house hiring in an outsourced workload = re-insourcing flag); last 5 full months vs the 5 before.
6. Incumbents: the top 10 providers from step 4 with their share. Check any rival I named across the whole stack.
7. Owner: IT executives in [Workloads]; keep applications, infrastructure, CIO or CTO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on separations, IT outsourcing, vendor consolidation, cost programmes or IT layoffs; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (savings programme naming technology), Momentum (4 = no rising in-house hiring in outsourced workloads; 0 = strong re-insourcing), Fragmentation, Budget, Trigger (separation or cost programme).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: provider landscape (Provider | Engagements | Share); captives separately.

RULES
- Drop agencies, staffing firms, "Self" and captives from provider counts (list captives separately). Never recommend catch-all workloads (Account Management).
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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

- Add your rival or the incumbent you replace: a services firm with 30% or more of the engagements is entrenched (Red), so plan a second-vendor entry, not a swap.
- A spin-off or business sale usually creates transition and application-split work for 12 to 24 months.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Find accounts ripe for ER&D services

- **id:** `plays-erd-targets`
- **What you get:** A ranked list of companies in your industry and territory most ready to buy engineering and R&D services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building an engineering and R&D services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for ER&D services?" instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Automotive); Territory (optional) (e.g. Germany); Workloads (optional) (e.g. a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development); What I sell (e.g. embedded and product engineering services)

### Detailed prompt

```text
Act as my engineering and R&D services target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Automotive]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. Germany]
- Workloads (optional): [a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development]
- What I sell: [one line, e.g. embedded and product engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in the ER&D function, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop engineering-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers; postings per 1,000 employees.
6. Top 5 by provisional score: each one's providers in [Workloads], captives marked; top 3: up to 3 ER&D priorities.
7. One news search across the top 5 on R&D programmes, engineering centres or new platforms, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in ER&D.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Provider mix 0–3 (3 = top 3 under 60% excluding captives, or a new centre in 12 months; 2 = 60–80%; 1 = over 80%; 0 = captives only); Hiring 0–3 (ER&D postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Priority 0–2 (2 = R&D programme shift in the last 4 fiscal quarters, 1 = older, 0 = none); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Captives (names containing the company's name) are in-house. Rate services rivals from my setup at the top 3 by share of engagements in [Workloads]: 30%+ Red, 10–29% Amber, under 10% Green.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (engineering services); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for engineering and R&D services on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for ER&D services?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Hiring by the ER&D function is broader and more reliable than niche engineering workloads.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for ER&D services?

- **id:** `plays-erd-readiness`
- **What you get:** A 0–20 readiness score for engineering and R&D services at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for an engineering and R&D services deal, or ahead of a first meeting. Use "Find accounts ripe for ER&D services" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. bosch.com); Workloads (optional) (e.g. a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development); Competitor or incumbent (optional) (e.g. LTTS); What I sell (e.g. embedded and product engineering services)

### Detailed prompt

```text
Act as my engineering and R&D services account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. bosch.com]
- Workloads (optional): [a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development]
- Competitor or incumbent (optional): [e.g. LTTS]
- What I sell: [one line, e.g. embedded and product engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated R&D spend and growth.
3. Intent: up to 6 ER&D priorities plus up to 3 named "engineering", newest first.
4. Current state: engineering providers ranked by active engagements in [Workloads]; captives (names containing the company's name) are in-house.
5. Capability: ER&D postings by workload, flagging [Workloads] that slow while priorities grow; last 5 full months vs the 5 before.
6. Incumbents: the top 10 providers from step 4, captives left out of share. Check any rival I named across the whole stack.
7. Owner: executives in ER&D; keep engineering, R&D or CTO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on R&D programmes, engineering centres or new platforms; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (R&D programme shift), Momentum (4 = ER&D postings rising; 0 = falling), Provider mix (4 = top 3 under 60% excluding captives), Budget (R&D spend growing), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: provider landscape with captives marked; R&D spend (Draup-estimated).

RULES
- Captives are never rivals. Private with no revenue or R&D spend: "Not in Draup", Budget 2. If [Workloads] return little, use step 5's top ER&D workloads and say so.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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

## Find accounts ripe for QE services

- **id:** `plays-qe-targets`
- **What you get:** A ranked list of companies in your industry and territory most ready to buy quality engineering and testing, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- **Use it when:** Building a quality engineering and testing campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for QE services?" instead when you already have one account.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 6–10 min
- **Inputs:** Industry (e.g. Banking & Financial Services); Territory (optional) (e.g. India); Workloads (optional) (e.g. a type of work, default Software Testing, Quality Assurance); Testing tools that signal fit (optional) (e.g. Tricentis Tosca, Micro Focus UFT); What I sell (e.g. test automation services)

### Detailed prompt

```text
Act as my quality-engineering target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Banking & Financial Services]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. India]
- Workloads (optional): [a type of work, default Software Testing, Quality Assurance]
- Testing tools that signal fit (optional): [e.g. Tricentis Tosca, Micro Focus UFT]
- What I sell: [one line, e.g. test automation services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in [Workloads], 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop testing and IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, testing tools only (makers of [Testing tools that signal fit]), no manufacturing quality tools; postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 IT priorities each, with linked tools.
7. One news search across the top 5 on release failures or outages, core-system changes or regulatory deadlines, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in [Workloads], falling back to IT.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = core-system change, digital launch or regulatory deadline in the last 2 fiscal quarters, 2 = older, 1 = other, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = a fading commercial test tool, or an automation tool new in 12 months; 1 = steady tools); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Outages count only when tied to a release or code change.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (testing tools or services); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for quality engineering and testing on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

### Follow-ups

- Run "Is this account ready for QE services?" on the #1 account.
- Show the next 10 companies with the same scoring.
- Write a 70-word opener for each of the top 3, each tied to its why-now.
- Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).

### Tips

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Foreign banks' local testing centres often out-hire local banks; they're a centre-of-excellence motion, not the ranked list.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Is this account ready for QE services?

- **id:** `plays-qe-readiness`
- **What you get:** A 0–20 readiness score for quality engineering and testing at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- **Use it when:** Before investing pursuit time in one account for a quality engineering and testing deal, or ahead of a first meeting. Use "Find accounts ripe for QE services" instead to find accounts.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. ford.com); Workloads (optional) (e.g. a type of work, default Software Testing, Quality Assurance); Competitor or incumbent (optional) (e.g. Wipro, or Tricentis); What I sell (e.g. test automation services)

### Detailed prompt

```text
Act as my quality-engineering account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. ford.com]
- Workloads (optional): [a type of work, default Software Testing, Quality Assurance]
- Competitor or incumbent (optional): [e.g. Wipro, or Tricentis]
- What I sell: [one line, e.g. test automation services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 IT and ER&D priorities plus up to 3 named "quality", software quality only, newest first.
4. Current state: the testing stack for [Workloads], up to 30 rows, no manufacturing quality tools; High or Medium usage in 6 months = core.
5. Capability: testing postings in IT and ER&D (under 60 a year = small in-house team); last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; joint ventures and captives are in-house. Check any rival I named across the whole stack.
7. Owner: executives in [Workloads], then IT; keep testing or quality titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on software recalls or outages, release failures or core-system changes; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum (4 = testing postings or releases rising; 0 = falling), Change window (a fading commercial tool or a recent software recall), Budget (cost programme), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Recalls or outages count only when tied to software; plant quality goes in Entry angle.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
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
