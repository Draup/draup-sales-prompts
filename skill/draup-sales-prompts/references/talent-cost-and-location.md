# Talent cost and location

Cost-arbitrage, location and hiring-difficulty cases for services pursuits. Uses the Draup for Talent connector.

## Offshore saving case from market pay

- **id:** `talent-offshoring-cost-case`
- **What you get:** A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. You're pitching offshore or nearshore delivery and the buyer wants a cost case grounded in market pay, not your rate card.
- **Best for:** Services, SI & Staffing Seller, Presales & Solutions, Account Executive
- **Time:** 4–6 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Role (e.g. Data Engineer); Years of experience (e.g. 3–6); Onshore location (e.g. Greater New York City Area, United States); Offshore locations (e.g. Bengaluru Area, India; Kraków, Poland; Mexico City, Mexico); Team size (e.g. 25); What I sell (e.g. offshore data-engineering delivery); Client (optional) (e.g. pepsico.com); Exchange rate (optional) (e.g. the rate your finance team uses this quarter)

### Detailed prompt

```text
Act as my deal-shaping analyst for services pursuits. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company facts. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Role: [e.g. Data Engineer]
- Years of experience: [band, e.g. 3–6]
- Onshore location: [metro or country, e.g. Greater New York City Area, United States]
- Offshore locations: [up to 3, e.g. Bengaluru Area, India; Kraków, Poland; Mexico City, Mexico]
- Team size: [FTEs in scope, e.g. 25]
- What I sell: [one line, e.g. offshore data-engineering delivery; skip if saved in setup]
- Client (optional): [website of the buyer, e.g. pepsico.com]
- Exchange rate (optional): [your rate to USD per currency, e.g. your finance team's quarterly rate]

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use.
2. Match each place to Draup's name (metros look like "Bengaluru Area, India"). If one doesn't match, show the closest and ask.
3. Per location, pull annual base pay at [Years of experience]: median, P10, P90, salaries reported, confidence (empty band: use all levels, say so).
4. With my rates, work out saving per FTE, saving % and team saving in USD against onshore; without rates, show local pay and ask.
5. For each offshore location, pull talent supply, 3-year growth and hiring difficulty for the role.
6. If I named a client, find it by website (parent; name lookup with its score if the website fails) and pull its top 3 executives in the function that owns this work and its top 90-day news item.

OUTPUT
- Bottom line: 2 sentences — annual base-pay saving for [Team size] FTEs at the best location (or "rates needed"), and whether supply can staff it; say it's base pay, not loaded cost.
- Recommended next step: who to take it to (step 6, or the title to find), what to do, and one dated why-now. If none, say so.
- "Pay": Location | Median USD (or local) | Salaries reported | Saving per FTE | Saving %. Onshore first, then by saving.
- "Can it scale?": Location | Talent supply | Hiring difficulty | Team as % of supply.
- Detail: P10–P90 (local), confidence, 3-year supply growth; 3 bullets on what this means for [What I sell].
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- The saving excludes transition, attrition and knowledge-transfer cost. Add overhead only with my multiplier.
- Don't build the bottom line on a location with low confidence or under 50 reported salaries (editable default); flag it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Show pay in local currency with its code; convert to USD only with my [Exchange rate], and say which rate.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: the base-pay saving for [Team size] [Role]s ([Years of experience] years) moving from [Onshore location] to [Offshore locations], at my exchange rates, and whether offshore supply can staff it.
```

### Follow-ups

- Apply my loaded-cost multipliers ([onshore]x and [offshore]x) and redo the saving.
- Add two nearshore options in Latin America and re-rank.
- Turn this into a one-slide cost case with three bullets for the CFO, noting what the base-pay gap leaves out.

### Tips

- Use Draup's metro names (e.g. "Bengaluru Area, India"). If a city doesn't match, Claude shows the closest options.
- Treat the result as a base-pay gap. Your commercial model adds overhead, margin and transition cost on top.

## Best city for a delivery team

- **id:** `talent-delivery-location`
- **What you get:** A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. A client asks where you'd staff their team, or you're shaping a captive-centre, centre-of-excellence or build-operate-transfer proposal.
- **Best for:** Services, SI & Staffing Seller, Presales & Solutions, Sales Leader & RevOps
- **Time:** 4–6 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Company (e.g. medtronic.com); Role (e.g. Cloud Engineer); Country (e.g. India); Team size (e.g. 60); What I sell (e.g. cloud engineering managed services); Weights (optional) (e.g. supply 35%, cost 30%, hiring difficulty 20%, location risk 15%)

### Detailed prompt

```text
Act as my location-strategy analyst for services pursuits. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company facts and the client's existing sites. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [the client's website, e.g. medtronic.com]
- Role: [e.g. Cloud Engineer]
- Country: [in full, e.g. India]
- Team size: [e.g. 60]
- What I sell: [one line, e.g. cloud engineering managed services; skip if saved in setup]
- Weights (optional): [default supply 35%, cost 30%, hiring difficulty 20%, location risk 15% (editable default)]

CONTEXT (optional)
Clients pick delivery cities on more than pay: a cheap city with thin supply turns into attrition and missed service levels, and a city next to the client's own centre is easier to sell. Show the trade-off, not just the winner.

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use. Then confirm Draup's name for [Country].
2. Pull the 10 metros in [Country] with the most talent supply for the role, with 3-year growth, median annual base pay, open postings and hiring difficulty.
3. Score each 1–10 on supply, cost (cheaper scores higher) and difficulty (easier scores higher).
4. For the top 3, pull Draup's location profile (cost of living, political stability, rule of law, corporate tax), score risk 1–10, and combine all four scores with the weights.
5. Find [Company] by website, confirm the parent (if the website returns nothing, look it up by name once and show the match and its score), and list its sites or capability centres in [Country].
6. Pull [Company]'s top 3 executives in the function that owns this work and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the lead metro and backup, and whether a [Team size]-person team is realistic there.
- Recommended next step: who to take it to (name and title from step 6), what to do, and why now (one dated fact). If none is found, say so.
- Table: Metro | Talent supply | Median pay (local) | Hiring difficulty | Score. Top 5, by score.
- "Client footprint": [Company]'s sites in [Country] with indicative headcount, or "Not in Draup".
- Detail: top 3 compared on every metric with periods; 3-year growth and open postings; weights used.
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Warn on capacity where [Team size] exceeds 2% of a metro's talent supply (editable default) or open postings are high against supply.
- Site headcount is approximate: call it indicative.
- Rank metros on local pay; no conversion is needed within one country.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: the best metro in [Country] for a [Team size]-person [Role] team for [Company], scored on supply, pay, hiring difficulty and location risk, with the client's sites and who to take it to.
```

### Follow-ups

- Re-run with cost weighted highest, then supply, then hiring difficulty.
- Compare the top metro with the best metro in [Second country].
- Which large employers in the top metro compete hardest for this role?

### Tips

- Change the weights to match the buyer's real worry: cost-led and scale-led buyers often pick different cities.
- Take the capacity warning seriously: a cheap city with thin supply can turn into attrition and missed service levels.

## Roles the client can't hire: staffing pitch

- **id:** `talent-hard-to-hire`
- **What you get:** Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. You sell staffing, staff augmentation or managed delivery and want evidence the client can't easily hire these roles itself.
- **Best for:** Services, SI & Staffing Seller, Account Executive, SDR / BDR
- **Time:** 4–6 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Company (optional) (e.g. fedex.com); Roles (e.g. Salesforce Developer, Data Engineer, SAP FICO Consultant); Location (e.g. Memphis, Tennessee Area, United States); What I sell (e.g. Salesforce and data staff augmentation); Exchange rate (optional) (e.g. the rate your finance team uses this quarter)

### Detailed prompt

```text
Act as my staffing and managed-services strategist. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company facts and the account's job postings. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company (optional): [the account's website, e.g. fedex.com]
- Roles: [up to 5, e.g. Salesforce Developer, Data Engineer, SAP FICO Consultant]
- Location: [metro or country, e.g. Memphis, Tennessee Area, United States]
- What I sell: [one line, e.g. Salesforce and data staff augmentation; skip if saved in setup]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

STEPS
1. Find Draup's standard name for each role. If there's no exact match, show the 3 closest and ask which to use.
2. Match the place to Draup's name (metros look like "Bengaluru Area, India"). If it doesn't match, show the closest and ask.
3. For each role in [Location], pull hiring difficulty (higher means harder to hire), talent supply, 3-year supply growth, open postings and median annual base pay.
4. Classify each: Hard (difficulty in the top third of roles checked, or postings outpacing supply; editable default), Moderate or Easy.
5. If [Company] is given, find it by website (parent, not a subsidiary; if the website returns nothing, look it up by name once and show the score) and count its postings per role in the last 6 months, noting repeats or long-open ones. Then pull its top 3 executives in the function that owns these roles (often IT or HR talent acquisition) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — which role is hardest to hire and what that means for [What I sell].
- Recommended next step: who to take it to (name and title from step 5, or the title to find), what to do, and why now (one dated fact). If none is found, say so.
- Table: Role | Hiring difficulty | Talent supply | Open postings | Verdict. Hardest first.
- "The pitch": one line per Hard role on how [What I sell] removes the hiring problem.
- Detail: median pay (local) and 3-year growth per role; "Account demand" (role, postings in 6 months, repeats or long-open).
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Explain the hiring-difficulty score in one plain line the first time it appears.
- Don't pitch Easy roles; say they're usually better hired in-house.
- Postings are openings, not hires.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Show pay in local currency with its code; convert to USD only with my [Exchange rate], and say which rate.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: which of [Roles] is hardest to hire in [Location] — difficulty, supply, open postings, median pay — and which makes the best staffing pitch for [What I sell], and to whom.
```

### Follow-ups

- Which nearby metros have more supply for the Hard roles? Show the top 3.
- Write a 90-word email to [Company]'s head of talent acquisition built on the hardest role.
- Which employers in [Location] hire the most people in the Hard roles?

### Tips

- Pair the difficulty score with the account's own postings: a hard role the client keeps re-posting is often your strongest opening.
- Easy-to-hire roles are a weak staffing pitch. Lead with the scarce ones and expand from there.

## Do layoffs open an outsourcing deal?

- **id:** `talent-layoff-pool`
- **What you get:** Where and in which roles a company has cut jobs in the last 12 months, read as a possible outsourcing trigger, plus which skills are now more available in the market.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. A target announces cuts, or you want to know whether a restructuring creates an outsourcing or managed-services opening.
- **Best for:** Services, SI & Staffing Seller, SDR / BDR, Account Executive
- **Time:** 2–4 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Company (e.g. 3m.com); Location (optional) (e.g. United States of America); Roles of interest (optional) (e.g. software engineer, QA); What I sell (e.g. managed engineering services)

### Detailed prompt

```text
Act as my services-pursuit analyst. Use the Draup for Talent connector for layoff data, and the Draup for Sales connector for company facts, executives and news. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Location (optional): [country or metro, e.g. United States of America]
- Roles of interest (optional): [e.g. software engineer, QA]
- What I sell: [one line, e.g. managed engineering services; skip if saved in setup]

CONTEXT (optional)
Cuts in one function plus hiring in another often mean work is moving, not disappearing; that's the services opening. Buyers react badly to outreach that leads with job losses, so the message must be about the business problem.

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary or a similarly named firm. If the website returns nothing, look it up by name once and show the match and its score. If unclear, ask me.
2. Pull the layoffs Draup records at [Company] in the last 12 months, in [Location] if given, grouped by month.
3. Break the same records down by job title (top 10) and location (top 10). Show any roles of interest separately.
4. Map the top titles to business functions (IT, engineering, customer service, finance) and name the functions with the deepest cuts.
5. Pull layoff, restructuring and site news on [Company] from the last 90 days to explain the cuts.
6. Pull the top 3 executives in the function with the deepest cuts (or the function closest to What I sell).

OUTPUT
- Bottom line: 2 sentences — the scale and focus of the cuts, and whether they point to an opening for [What I sell].
- Recommended next step: who to take it to (name and title from step 6), what to do, and why now (one dated fact from step 5). If none is found, say so.
- "Roles affected": Job title | Count | Function. Top 10.
- "Possible outsourcing trigger": 3 bullets on whether work looks outsourced, consolidated or automated, and what [What I sell] could take on. Mark each "likely".
- Detail: by month; by location (top 10); skills now more available in the market, for your delivery hiring plans; news used.
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Counts come from profiles Draup holds with a layoff date: a sample that shows the pattern, not the official total. Say so.
- Report counts only. Never name or list individuals, describe people as a pool or bench, or suggest contacting them about the company.
- Keep any outreach about the business problem, not the layoffs.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: does [Company]'s last 12 months of layoffs (by month, top titles, top locations; counts only, no names) point to an outsourcing opening for [What I sell], and who to take it to?
```

### Follow-ups

- Which of these functions does [Company] already outsource, and to whom?
- Draft a value-led note to the executive named above that doesn't mention the layoffs.
- Compare with [Peer company]'s layoffs over the same 12 months.

### Tips

- Cuts in one function plus hiring in another often mean work is moving, not disappearing. That's the services opening.
- Keep outreach about the business problem, not the cuts. Buyers often react badly to messages that lead with job losses.

## Size a skill pool and its employers

- **id:** `talent-role-sizing`
- **What you get:** How many people hold a role in up to 3 countries, how fast supply is growing, and which companies employ the most, split into prospects and services competitors.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. You're sizing a services practice, a staffing market or a target list built around one skill set.
- **Best for:** Services, SI & Staffing Seller, Sales Leader & RevOps, Partnerships & Alliances
- **Time:** 2–4 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Role (e.g. SAP FICO Consultant); Countries (e.g. India, Poland, Philippines); Vertical (optional) (e.g. Retail); What I sell (e.g. SAP finance managed services)

### Detailed prompt

```text
Act as my market-sizing analyst for a services practice. Use the Draup for Talent connector for talent-supply facts, and the Draup for Sales connector for company facts. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Role: [e.g. SAP FICO Consultant]
- Countries: [up to 3, in full, e.g. India, Poland, Philippines]
- Vertical (optional): [limit to people at companies in this industry, e.g. Retail]
- What I sell: [one line, e.g. SAP finance managed services; skip if saved in setup]

CONTEXT (optional)
A skill pool tells you two things at once: where you can hire to deliver, and which end clients carry big in-house teams that could move to managed services. Services firms holding the same skill are the competitors you'll meet in both deals and hiring.

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use. Then confirm Draup's name for each country.
2. For each country, pull the talent supply for the role, its likely range, 3-year growth and how reliable the estimate is, limited to [Vertical] if given.
3. For the largest country, pull the top 25 current employers of people in this role.
4. Sort those employers into end clients (use the skill in-house) and services firms (IT services, consulting, staffing). Keep the top 15 overall.
5. For the largest end client, pull its top 3 executives in the function that owns this skill and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how big and fast-growing the supply is, and what it means for [What I sell].
- Recommended next step: who to take it to (name and title from step 5), what to do, and why now (one dated fact). If none is found, say so.
- "Supply": Country | Talent supply | Likely range | 3-yr growth | Reliability. Largest first.
- "Who employs them": Employer | Type (End client or Services firm) | People in role. Top 10.
- Detail: employers 11–15; prospects (end clients with the largest in-house teams); competitors (services firms holding most of this skill); 3 bullets on what this means for [What I sell].
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Show the likely range beside every supply figure; if reliability is poor, say so beside the number.
- Employer counts come from profiles Draup has matched: use them to rank, not as exact headcount.
- If the role returns nothing in a country, write "Not in Draup" for that row; never borrow another country's figure.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: how many [Role]s are in [Countries] (with likely range and 3-year growth), and the top 15 employers in the largest country, split into end-client prospects and services competitors.
```

### Follow-ups

- Show the same supply figures for two adjacent roles so I can see the wider practice.
- For the top 5 prospects, show their recent hiring for this role.
- Which metros in the largest country hold most of this skill?

### Tips

- Large in-house teams at end clients are often expensive and hard to retain: a good managed-services conversation.
- Use the likely range, not just the point estimate, when you put the number in a business case.

## Is our rate defensible against market pay?

- **id:** `talent-pay-benchmark`
- **What you get:** Market pay for a role by employer, including named competitors, the markup a proposed or quoted rate implies, and the rate you'd need at your target markup.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. You're pricing a staffing or managed-services bid, or a client pushes back that your rates are too high.
- **Best for:** Services, SI & Staffing Seller, Presales & Solutions, Account Executive, Sales Leader & RevOps
- **Time:** 2–4 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Role (e.g. Java Developer); Location (e.g. Pune Area, India); Years of experience (e.g. 5–8); Rate to check (e.g. USD 32 per hour); Competitor (optional) (e.g. Infosys, Cognizant, Capgemini); Target markup range (optional) (e.g. 1.8–2.4x); Hours per year (optional) (e.g. 1,880); Exchange rate (optional) (e.g. the rate your finance team uses this quarter)

### Detailed prompt

```text
Act as my pricing analyst for services bids. Use the Draup for Talent connector for pay facts, and the Draup for Sales connector for company facts. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Role: [e.g. Java Developer]
- Location: [metro or country, e.g. Pune Area, India]
- Years of experience: [band, e.g. 5–8]
- Rate to check: [ours or a competitor's, with unit and currency, e.g. USD 32 per hour]
- Competitor (optional): [e.g. Infosys, Cognizant, Capgemini]
- Target markup range (optional): [e.g. 1.8–2.4x]
- Hours per year (optional): [default 1,880 (editable default)]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

CONTEXT (optional)
"You're expensive" is easier to answer with market pay than with a discount. The markup over what the market pays its people shows how much room you have and what a competitor must be absorbing to undercut you.

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use.
2. Match the place to Draup's name (metros look like "Bengaluru Area, India"). If it doesn't match, show the closest and ask.
3. Pull market annual base pay at [Years of experience]: median, P10, P90, salaries reported, confidence.
4. Pull median base pay by employer. Keep the top 15 among employers with 20+ salaries reported (editable default), plus any [Competitor].
5. Convert to hourly with [Hours per year]. If [Rate to check] is in another currency, use my [Exchange rate] or ask for one.
6. Divide [Rate to check] by the hourly median, P10 and P90 for the implied markup. With a target range, work out the rate needed at each end.

OUTPUT
- Bottom line: 2 sentences — where the rate sits against market pay and what that means for the bid.
- Recommended next step: who to take it to (the bid owner or the client's procurement lead, by title), what to say, and the one number to lead with. If you can't name a person, say so.
- "Rate check": Rate | Markup on median | on P10 | on P90 | Verdict against [Target markup range].
- "Rate needed at target markup": Low end | High end, per hour.
- Detail: market pay annual and hourly with salaries reported and confidence; by employer (rank, employer, median pay, salaries reported) with [Competitor] highlighted; 3 bullets — room on price, competitor pay, and a reply to "you're expensive".
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Base pay excludes benefits, bench, overhead and margin. Never present it as a competitor's bill rate.
- Flag thin salary counts and low-confidence figures.
- Without [Target markup range], show the multiples only; don't call a markup high or low.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Show pay in local currency with its code; convert to USD only with my [Exchange rate], and say which rate.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: where [Rate to check] sits against [Role] market pay in [Location] — median and P10–P90, the markup it implies, the rate needed at my target markup, and how named competitors pay.
```

### Follow-ups

- Redo the rate check for a junior band to see a blended rate.
- Compare the same role in [Second location] and show the rate I'd need there for the same markup.
- Write a 3-sentence reply to a client who says our rate is [X]% above competitors.

### Tips

- Give your own markup range; without it Claude shows only the multiples, which is safer than guessing what's normal.
- Change hours per year to suit the country: working hours differ a lot between markets.
- Employer pay is what firms pay their people, not what they charge. Use it to explain cost, not to quote a competitor's price.

## Employer-brand gaps for an RPO pitch

- **id:** `talent-employer-brand`
- **What you get:** How a company scores as an employer against its hiring rivals, its three weakest areas from employee reviews, and RPO or employer-branding angles.
- **Use it when:** Preview: needs the Draup for Talent connector; not yet live-tested. You sell RPO, recruitment marketing or employer-branding services and need a data-led reason to start the conversation.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Marketing & ABM
- **Time:** 2–4 min
- **Note:** needs the separate Draup for Talent connector; not live-tested.
- **Inputs:** Company (e.g. costco.com); Hiring rivals (e.g. target.com, walmart.com); Location (optional) (e.g. United States of America); What I sell (e.g. RPO and employer-branding services)

### Detailed prompt

```text
Act as my talent-acquisition services strategist. Use the Draup for Talent connector for employer-value scores, and the Draup for Sales connector for company facts, executives and news. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [website, e.g. costco.com]
- Hiring rivals: [up to 3 companies it competes with for hires, e.g. target.com, walmart.com]
- Location (optional): [country or metro for location-level scores, e.g. United States of America]
- What I sell: [one line, e.g. RPO and employer-branding services; skip if saved in setup]

CONTEXT (optional)
A gap against a named hiring rival opens more doors than an absolute score. Frame it constructively: this analysis may reach the client, and talent leaders respond to opportunities, not criticism.

STEPS
1. Find [Company] and each rival by website and confirm the parent company. If a website returns nothing, look it up by name once and show the match and its score; if it still fails, tell me and carry on.
2. For each, pull the employer-value scores: overall index, employee reviews analysed, and every pillar and sub-pillar score. Use [Location] scores if given; otherwise company-wide.
3. Find [Company]'s 3 weakest pillars: the lowest scores and the biggest gaps behind the rival average.
4. For each weak pillar, summarise the review themes in your own words (2–3 themes each).
5. Pull [Company]'s top 3 executives in Human Resources (prefer talent acquisition or the CHRO) and its most important news item from the last 90 days (hiring drives, new sites, layoffs).

OUTPUT
- Bottom line: 2 sentences — where [Company] trails its hiring rivals and the RPO angle that follows.
- Recommended next step: an opening line for the person named from step 5 (name and title), framed on one gap against a named rival, with the dated why-now. If none is found, say so.
- Table: Pillar | [Company] | Rival average | Gap. Worst gap first, top 6.
- "Weakest 3": Pillar | Gap | What employees say (themes) | The RPO angle for [What I sell].
- Detail: scores per rival and sub-pillar; reviews analysed and scope (company-wide or [Location]).
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Mark any company with fewer than 200 reviews analysed as low confidence (editable default), and don't build the opening line on it.
- Paraphrase review themes. Never quote or identify individual reviewers.
- Keep the tone constructive: frame gaps as opportunities.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step first: where [Company] trails [Hiring rivals] as an employer — overall index, reviews analysed, the 3 weakest pillars with review themes — and the RPO angle and person to open with for [What I sell].
```

### Follow-ups

- Show how hard it is for [Company] to hire its top 3 roles in [Location].
- Turn this into a 5-slide outline for an RPO discovery meeting.
- Which pillar is [Company] strongest on, so we can acknowledge it first?

### Tips

- Compare against named hiring rivals. A gap against a known rival usually opens more doors than an absolute score.
- Pair this with hiring difficulty: a weak employer brand plus hard-to-hire roles makes the strongest RPO case.
