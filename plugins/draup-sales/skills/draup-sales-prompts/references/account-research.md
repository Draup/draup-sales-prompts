# Account research

Know the account before you call: size, money, priorities, filings and earnings calls.

## One-page account brief

- **id:** `research-account-brief`
- **What you get:** Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.
- **Use it when:** An account just landed on your list, or you're prepping a call or meeting (tomorrow or later) with someone there, including when you only know their title. Use "10-minute pre-call snapshot" instead when you only have a few minutes.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, SDR / BDR
- **Time:** 2–4 min
- **Inputs:** Company (e.g. starbucks.com); What I sell (e.g. store technology and data platform services); Meeting with (optional) (e.g. a name or a title, e.g. CISO); Competitor (optional) (e.g. Snowflake or Accenture (company or product); defaults to your saved competitors)

### Detailed prompt

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- What I sell: [one line, e.g. store technology and data platform services — skip if you ran the start-here prompt]
- Meeting with (optional): [name or title, e.g. CISO]
- Competitor (optional): [company or product, e.g. Snowflake; default: my saved competitors]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile and latest fiscal-year revenue, EBITDA and IT spend with growth (if private, funding instead), plus revenue by business unit and region, kept only if more than one holds 10% or more.
3. Pull stated priorities for the function closest to [What I sell]: the 8 most relevant, newest first (none: say so and use the company-wide list). Pull acquisitions from the last 3 years.
4. Pull the top 3 executives in that function and the 2 most important news items from the last 90 days where [Company] is the actor.
5. If I named who I'm meeting, find them: the workload closest to their title, then the function's next page once, matching full profile titles. Not found: say so and list the 3 closest people.
6. Check the whole stack for [Competitor]'s products, in any area; for a services firm, its share of active engagements in my workloads.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]; say here if the person I'm meeting isn't in Draup.
- Recommended next step: one person by name and title (the person I'm meeting if found, else from step 4), what to do and why now (a dated fact from the last 90 days); say if either is missing.
- "What they're focused on": Priority | Source + quarter | Likely owner (name, else title) | Why it matters. Up to 8.
- "Who to talk to": Name | Full title | Time in role | Linked priority. Up to 3, the person I'm meeting first; if they're not in Draup, the 3 closest.
- "Competitor in the stack": one line each: product or engagement share, usage strength, last seen, Red/Amber/Green.
- "Why this matters for [What I sell]": 3 bullets: fact → implication → action.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "The numbers" (Metric | Latest FY | YoY); business units and regions if kept; "Recent deals" (Date | Company acquired | Size | Why), flagging divestments and duplicates.

RULES
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- The acquisitions table can be incomplete; if news names a deal it lacks, say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Money: annual, millions of reporting currency. IT and R&D spend are modelled and move with revenue, so their growth isn't a signal. Check for a divestment before calling a drop over 5% a cut.
- Competitor rating: a [Competitor] product at High usage in the workloads I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber. Services rival, by share of the account's active engagements in those workloads: 30%+ Red, 10–29% Amber, under 10% Green.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
One-page Draup brief on [Company], meeting [Meeting with]: bottom line, who to call and why now; that person (or the 3 closest if not in Draup); 8 priorities in my function; revenue growth; [Competitor] rated Red/Amber/Green.
```

### Follow-ups

- Now run "Map the buying committee" for [Business function].
- Which of these priorities have the most hiring behind them?
- Is their budget growing or shrinking? Show the 3-year trend.
- Turn the 'Why this matters' section into a 90-word email to the person in the next step.

### Tips

- Add your main competitor, or save it with "Tell your AI about you": finding it, or its absence, in the stack is often the most useful line in the brief.
- Use the company website rather than the name; it is the most reliable way to land on the right company.
- Business-unit and region tables only appear when the company is genuinely split; a single-market retailer skips them.
- Prepping a meeting? Put the title in Meeting with ("CISO"). If Draup has no one with that title, the brief says so up front and gives the 3 closest people.

## 10-minute pre-call snapshot

- **id:** `research-precall-snapshot`
- **What you get:** Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.
- **Use it when:** You have a call in 10 minutes, including when you only know who you're meeting by title. Use "One-page account brief" instead when you have 30 minutes or need the numbers and a competitor check.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager, Presales & Solutions
- **Time:** 1–2 min
- **Inputs:** Company (e.g. medtronic.com); What I sell (e.g. application modernisation and cloud migration services); Meeting with (optional) (e.g. a name or a title, e.g. CISO or VP Global IT)

### Detailed prompt

```text
Act as my pre-call research assistant. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- What I sell: [one line, e.g. application modernisation and cloud migration services — skip if you ran the start-here prompt]
- Meeting with (optional): [name or title, e.g. CISO or VP Global IT]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile: what they do, workforce, latest revenue and its fiscal year.
3. Pull the top news from the last 90 days where [Company] is the actor.
4. Pull the top 3 workloads (types of work) trending up in 12-month hiring in the business function closest to [What I sell] (e.g. IT); if none is rising, show that function's top 3 by postings with their trend.
5. Pull stated priorities for that function and pick the one closest to [What I sell], preferring the function of the person I'm meeting.
6. Pull the top 3 executives in that function (full title, time in role). If I named who I'm meeting, find them: the workload closest to their title, then the function's next page once, matching full profile titles. Not found: say so in the Bottom line and list the 3 closest.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- If I named who I'm meeting: a priority they likely own and their time in role, or "Not in Draup" and the 3 closest (name, full title).
- Then exactly 5 bullets, 25 words or fewer each:
  1. What they do and their size (workforce, revenue, fiscal year).
  2. The 2 most important events from the last 90 days, each dated.
  3. Hiring in [function]: the top 3 workloads with posting counts and trend (rising, flat or falling).
  4. The priority closest to [What I sell], with source and quarter.
  5. One open question that cites a fact from bullets 1–4.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If fewer than 2 real events exist, say so; don't pad.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Call with [Company] in 10 minutes. Bottom line and who to contact first, then five 25-word bullets: size; 2 events from 90 days; hiring in the function closest to [What I sell]; its closest priority; one question.
```

### Follow-ups

- Give me 3 more questions like bullet 5, each tied to a different fact.
- Who else from [Company] should be in the next meeting?
- Expand bullet 2: what changed and why it matters for [What I sell].
- Show company-wide hiring too, so I can see where the overall headcount is going.

### Tips

- Name who you're meeting, even just the title ("CISO"). Claude picks the priority in their function, checks their time in role, and says plainly if Draup has no one with that title.
- If you have 30 minutes rather than 10, run "One-page account brief" instead.

## Is their budget growing or shrinking?

- **id:** `research-budget-posture`
- **What you get:** A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- **Use it when:** Before you set deal size or pick a value story, or when a champion says 'budgets are tight'.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. unilever.com); What I sell (e.g. managed data engineering and analytics services)

### Detailed prompt

```text
Act as my sales finance analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- What I sell: [one line, e.g. managed data engineering and analytics services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue, EBITDA, IT and R&D spend for the last 3 fiscal years, plus Draup's next-year forecast.
3. Pull the IT spend split for the latest and prior year.
4. Pull acquisitions (3 years), and divestments, layoffs and cost programmes from news (12 months; say so).
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Verdict: Growing, Holding or Shrinking, with 3 dated evidence bullets.
- "3-year trend": Fiscal year | Revenue | YoY | EBITDA margin | IT spend (Draup estimate). Forecast year last.
- "Deal-size implication": one line on how big a first deal to propose.
- "What to pitch": 3 bullets fitting the verdict, naming the IT spend category most addressable by [What I sell] and its likely owner.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "IT spend split (Draup estimate)": Category | Latest FY | Prior FY | YoY | % of total; R&D spend by year.

RULES
- Verdict (editable default): Growing = revenue and EBITDA up over 3% a year; Shrinking = either down over 5% after the divestment check; else Holding.
- For any drop over 5%, name the divestment, demerger or restatement behind it, or say none falls in that year.
- If every IT split category moves with the total, call the split proportional.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- If a forecast is more than 15% from the latest actual, or contradicts the latest year-on-year change, show both and call it a model estimate.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Is [Company]'s budget growing, holding or shrinking? Bottom line and who to pitch first, then 3-year revenue, EBITDA margin and IT spend, a verdict with evidence, deal-size implication and the pitch for [What I sell].
```

### Follow-ups

- Convert everything to USD and compare with [Company 2].
- Which business units are growing fastest?
- Draft a cost-takeout talk track for the CFO based on this.

### Tips

- A falling number is not always a cut. Spin-offs and restatements often explain big drops; the prompt checks for them.
- The IT spend split is Draup's estimate. Use it to size the conversation, not as a reported figure.

## Which priority to anchor your pitch on

- **id:** `research-priorities-by-function`
- **What you get:** The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.
- **Use it when:** You need to know which initiative to anchor a pitch on.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. siemens.com); What I sell (e.g. cloud data-platform modernisation services); Business function (optional) (e.g. IT — leave blank and Claude picks the best fit)

### Detailed prompt

```text
Act as my sales strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]
- Business function (optional): [e.g. IT; leave blank and Claude picks]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull how many priorities mention each workload (a type of work, e.g. Data Engineering). Mark each Strong, Partial or No fit to [What I sell] and keep the top 5 by fit, then count.
3. If I gave no business function, choose the one holding most Strong-fit workloads and say why.
4. Pull up to 8 priorities for that function and sort them by date yourself, newest first.
5. Pull the top 3 executives in that function (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to name the anchor's likely owner.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Best anchor for [What I sell]": the one priority to lead with, its likely owner by name, and 2 bullets on why.
- "Top priorities in [Business function]": Priority | Source + quarter | Workloads | Up to 3 linked providers. Up to 8.
- "Where priorities cluster": Rank | Workload | # priorities | Fit (Strong, Partial, No). Top 5.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: a one-line summary of each priority.

RULES
- Leave out linked technology or use cases that clearly don't fit the industry.
- If the function has no priorities, say so and show the 3 nearest functions by priority count.
- Source matters: earnings-call priorities usually outweigh news-derived ones; say which each is.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Tools and providers linked to a priority are "linked", not confirmed. Leave out recruiters, staffing firms, agencies and research firms.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Which [Company] priority should I anchor [What I sell] on? Bottom line, the anchor and its likely owner by name, then top 5 workloads by fit and the top 8 priorities in the best-fit function.
```

### Follow-ups

- For the anchor priority, which technology and incumbent vendors are linked?
- Who else owns the anchor priority? Find executives tagged to its workloads.
- Is there hiring behind these priorities, or are they just talk?

### Tips

- Leaving the function blank lets Claude choose where your offer fits best.
- Priorities from earnings calls often carry more weight than ones inferred from news.

## Their leaders' own words on [Topic]

- **id:** `research-proof-points`
- **What you get:** Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.
- **Use it when:** You want to open with the customer's own words rather than your claims. Use "Numbers from the latest earnings call" instead when you need figures for a business case.
- **Best for:** Account Executive, Presales & Solutions, Marketing & ABM, Account & Customer Success Manager
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); Topic (e.g. AI, supply chain, technology investment); What I sell (e.g. AI-driven demand forecasting software)

### Detailed prompt

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Topic: [e.g. AI, supply chain, technology investment]
- What I sell: [one line, e.g. AI-driven demand forecasting software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first, and open the most recent. Note each speaker's title from the introductions, and whether it is an analyst or a press call.
3. Find every passage where an executive talks about [Topic], preferring the CEO and CFO. If [Topic] isn't there, say so and repeat on the previous call.
4. Fallback: if there are no transcripts, or neither call mentions [Topic], pull the annual filings Draup holds for the last 5 years (US SEC filers only).
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to choose who to take the quotes to.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: call date, the company's own name for the period with Draup's label in brackets, call type.
- "Quotes": # | Speaker and title | Verbatim quote (40 words or fewer) | What it signals. Up to 6, strongest first.
- "How to use this with [What I sell]": 2 bullets, each pairing a quote with a talking point.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail, fallback only: "Filings to read": Fiscal year | Type | Filed date | Link; then up to 4 sections to read (e.g. Risk Factors, Business), one line each on what to look for.

RULES
- Quote word for word; trim with an ellipsis, never paraphrase inside quotation marks. Executives only, not analysts.
- Don't summarise or quote a filing you haven't opened. Non-US companies usually have none; that's expected.
- Read only what you need; reproduce nothing beyond the quotes.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Quote [Company]'s leaders on [Topic] from the latest earnings call: bottom line and who to take it to first, then up to 6 verbatim quotes with speaker, title and fiscal quarter. No call? List filings to read.
```

### Follow-ups

- Do the same for the previous call. Has the tone on [Topic] changed?
- Pull every number they stated in this call into a table.
- Write a 3-line email opener using the strongest quote.

### Tips

- Quarters follow the company's fiscal year, which can run a year ahead of the calendar. The prompt shows both labels.
- For US-listed companies, the filing fallback points you to risk-factor language you can cite.

## Numbers from the latest earnings call

- **id:** `research-numbers-from-the-call`
- **What you get:** The three numbers from the latest earnings call that matter for your deal, the question each opens and who to raise them with, plus every stated number in a reference table.
- **Use it when:** Building a business case, a QBR, or an executive email that should use their numbers, not yours. Use "Their leaders' own words on [Topic]" instead when you want quotes on a theme.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. store and supply-chain technology modernisation)

### Detailed prompt

```text
Act as my financial analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. store and supply-chain technology modernisation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first, and open the most recent analyst call. If the newest is a press call, use the latest analyst call and say so.
3. Note each executive's title from the introductions.
4. Extract every number an executive states: results, guidance, targets, capital spending, technology investment, site counts, headcount, AI or digital metrics, savings programmes.
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: call date, the company's own name for the period, Draup's quarter label in brackets.
- "Numbers that matter for [What I sell]": Number | Period it refers to | Speaker | Question it opens. Exactly 3.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Everything they said", grouped as Guidance / Investment and capex / Operating KPIs / Technology, AI and digital: Metric | Value | Period | Actual, guidance or target | Speaker. Up to 15 rows, then offer the rest.

RULES
- Executives only; skip numbers that appear only in analysts' questions.
- Keep units and currency as stated ("$5 billion to $6 billion", "about 6%"). Don't round or convert unless I ask.
- Separate the period a number refers to from the call's quarter. Mark raised or lowered only if the speaker compares with earlier guidance.
- No transcript: say so and suggest the filing fallback in "Their leaders' own words on [Topic]".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
From [Company]'s latest earnings call: bottom line and who to raise it with, then the 3 numbers that matter for [What I sell], each with period, speaker and a question to ask.
```

### Follow-ups

- Compare these with the previous call's numbers. What moved?
- Build a one-slide business case using the three numbers that matter.
- Which of these numbers ties to a stated priority in Draup?

### Tips

- Their own guidance is the strongest anchor for a business case. Quote it rather than analyst estimates.
- Press calls usually carry less guidance; the prompt switches to the analyst call.

## What changed between two earnings calls

- **id:** `research-call-over-call`
- **What you get:** Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, who owns them, and a 2-line talk track for your next QBR.
- **Use it when:** Advanced: quarterly, for strategic accounts. Before a strategic meeting, QBR or renewal, to show you know where their story is moving.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. siemens.com); What I sell (e.g. industrial AI platform services)

### Detailed prompt

```text
Act as my sales strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. industrial AI platform services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first. Pick the two most recent analyst calls for consecutive quarters. If one is a press call or a quarter is missing, say so and use the nearest pair.
3. Open the latest call in full and list its 6–10 main themes (strategy, investment, cost, technology, markets, risks).
4. Open the previous call. If it fails to load or comes back truncated, compare against the priorities Draup sourced in the previous quarter instead, and say so.
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to name who owns the New themes.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: both calls with dates, the company's own period names and Draup's quarter labels.
- "Theme shifts": Theme | Status (New, Stronger, Weaker, Dropped, Continued) | Quote from the latest call (25 words or fewer, speaker) | Likely owner. Up to 8, New first.
- "What this means for [What I sell]": 3 implications, each tied to a row.
- "QBR talk track": 2 lines: "Last quarter you emphasised X; now you're talking about Y. Here's how we help with Y."
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: for each theme, one line on how it was framed in the previous call.

RULES
- Quote executives only, word for word.
- Call a theme Dropped only if it got real airtime before and none now.
- Read for themes; reproduce nothing beyond the quotes.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Label anything you infer (buyer role, intent, fit) as "likely".
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Compare [Company]'s two latest earnings calls: bottom line and who to raise it with, then themes marked New, Stronger, Weaker, Dropped or Continued, each with a short quote, and a 2-line QBR talk track.
```

### Follow-ups

- Go deeper on the top New theme: every quote about it from the latest call.
- Which executives own the New themes?
- Turn the implications into 3 talking points for my QBR.

### Tips

- This reads two long transcripts, so it takes longer than most prompts. Run it once a quarter per key account.
- New and Stronger themes are often where fresh budget goes; test that in the meeting.

## Which region should own this account

- **id:** `research-buying-center`
- **What you get:** Which region should own the pursuit, where to hold the first meeting and with whom, backed by revenue by region, top metros and where your function's leaders sit.
- **Use it when:** Planning territory ownership for a global account, or deciding where to run the first meetings.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. unilever.com); Business function (e.g. IT); What I sell (e.g. data and analytics managed services)

### Detailed prompt

```text
Act as my territory planning analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- Business function: [e.g. IT]
- What I sell: [one line, e.g. data and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue by region for the latest fiscal year: share and year-on-year change.
3. Pull key locations (up to 100 rows) for [Business function] and combine them into one row per metro.
4. Pull senior executives in [Business function], 10 per page, up to 3 pages (there is no title search), and count them by country and metro.
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 4), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Recommended owning region": 3 bullets weighing revenue, people and decision makers, separating where budget sits from where delivery happens.
- "Where to hold the first meeting": one metro and why.
- "Revenue by region": Region | Share % | YoY | Fiscal year.
- "Top 8 metros": Metro | Country | 12-month postings | Top function | HQ or GCC (global capability centre: a company-owned offshore site). Sort by postings.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Where [Business function] leaders sit": Country or metro | # senior leaders | Most senior title; indicative headcount per metro.

RULES
- Site headcount is approximate and varies between lookups: call it indicative and back it with postings. GCC tags can include plants; drop mainly-manufacturing sites.
- A "new" site can only be inferred from postings; say so. The HQ metro may be undercounted; don't conclude the HQ is small.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. Professional information only.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Which region should own [Company] for [Business function]? Bottom line, who to meet first and where, then revenue by region, the top 8 metros with postings and capability-centre flags, and where senior leaders sit.
```

### Follow-ups

- What is each GCC hiring for? Top functions and skills by metro.
- Name the top 5 leaders in the recommended region.
- Which service providers deliver from these metros?

### Tips

- Budget is often decided at HQ but spent where the delivery centre is. The output separates the two.
- European executive profiles can be restricted, so Europe may look thinner on leaders than it is.

## Business units worth targeting first

- **id:** `research-business-units`
- **What you get:** The two business units to target first, ranked by growth, with the priority behind each and a named leader to approach.
- **Use it when:** Choosing which division to enter first at a conglomerate or multi-segment company.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. siemens.com); What I sell (e.g. rail and infrastructure digital-twin software)

### Detailed prompt

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. rail and infrastructure digital-twin software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue by business unit for the latest year Draup holds, and the latest reported fiscal year.
3. Pull stated priorities for the function closest to [What I sell] and match each unit to the priorities that mention its products, markets or workloads.
4. For the top 2 units, find the most senior leader on the first executives page for the function closest to [What I sell].
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 4), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Target these 2": for each, why (growth, size), one linked priority with source and quarter, and the unit leader by name and title (or "title to find").
- "Business units" (fiscal year in the heading): Rank | Unit | Revenue (millions, currency) | Share % | YoY. Sort by YoY, highest first.
- "Watch": units shrinking more than 5% (editable default), with a reason if Draup shows one.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out eliminations, reconciliation, corporate and internal financing lines.
- If segment data is a year older than the latest fiscal year, say so plainly.
- If segment data is empty, say so and fall back to priorities grouped by business function, labelled as a fallback.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Which [Company] business units should I target for [What I sell]? Bottom line and who to approach, then units ranked by revenue growth (revenue, share, YoY) and the top 2, each with a linked priority.
```

### Follow-ups

- Who leads the top unit? Map its buying committee.
- What is the top unit hiring for?
- Compare the top unit's priorities with what [Competitor] offers.

### Tips

- Fast-growing units often have new budget, which makes them a good first entry point.
- Segment data can lag the latest annual report by a year; the prompt flags it.

## Openings from their recent acquisitions

- **id:** `research-acquisitions`
- **What you get:** The top 3 integration openings from the account's acquisitions in the last 3 years, who likely owns each, and an optional read of its strategic investments.
- **Use it when:** An account has been buying or investing in companies and you sell integration, data, migration, change or platform work.
- **Best for:** Account Executive, Services, SI & Staffing Seller, Presales & Solutions, Account & Customer Success Manager, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. siemens.com); What I sell (e.g. ERP and data integration services); Strategic bets (optional) (e.g. yes — adds investments from the last 12 months)

### Detailed prompt

```text
Act as my M&A analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. ERP and data integration services — skip if you ran the start-here prompt]
- Strategic bets (optional): [yes or no, e.g. yes — adds 12 months of investments]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull acquisitions from the last 3 years.
3. Search 12 months of M&A news with [Company]'s name in the question, not just news tagged to [Company] (the acquired firm is often the one tagged). Add deals where [Company] is the buyer that the table lacks; list divestments separately.
4. Infer each deal's integration work: systems, data, security, process, people.
5. If Strategic bets is yes, pull investments (12 months), drop debt financing, merge repeat rounds and compare themes with stated priorities.
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role; widen as in the executives rule) and the most important news item from the last 90 days where [Company] is the actor, to name who owns the top opening.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Top 3 integration openings for [What I sell]": deal, months since close, likely owner.
- "Acquisitions": Date | Target | Theme | Likely integration work | Source (table or news). Newest first, up to 10.
- Optional "Strategic bets": up to 3, each with a matching priority or "none yet".
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: what each target does and its size; "Divestments (news)": Date | Business sold | Buyer; investments table (Company | Rounds | Total $M | Latest date).

RULES
- Flag rows whose date, target and size don't fit together, and duplicates; count each deal once.
- Deals closed 3–18 months ago (editable default) are usually the best openings. Investment amounts are whole rounds, not [Company]'s cheque.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
[Company]'s acquisitions from the last 3 years, cross-checked with M&A news: bottom line and who to contact, then date, target, theme and likely integration work, and the top 3 openings for [What I sell].
```

### Follow-ups

- Which executives joined [Company] from the acquired companies?
- What tech stack did the top acquisition bring in?
- Show strategic investments over the last 3 years to see whether the bets are new.
- Draft a 100-word note to the owner of the top opening.

### Tips

- Most deal sizes are undisclosed. That's normal; the date and theme matter more for timing.
- If the deals table looks empty for a company you know has been buying, the news cross-check usually finds the missing deals.

## Private company funding and who signs

- **id:** `research-private-funding`
- **What you get:** How much a private company has raised, its last round and valuation, whether it is in growth mode, and who signs, by name.
- **Use it when:** Selling to a startup or scale-up, or checking a private competitor's runway.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Partnerships & Alliances
- **Time:** 1–2 min
- **Inputs:** Company (e.g. databricks.com); What I sell (e.g. security compliance automation)

### Detailed prompt

```text
Act as my venture research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. databricks.com]
- What I sell: [one line, e.g. security compliance automation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull private funding: total raised and each round's date, type, amount, valuation and lead investors.
3. Pull the profile (workforce, year founded) and the monthly hiring trend for the last 12 months.
4. From the first executives page, pick the founder or CEO, the CFO and the leader closest to [What I sell].
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 4), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Headline: total raised, last round (date, type, amount, valuation, leads).
- "Last 5 equity rounds": Date | Type | Amount ($M) | Valuation ($M) | Lead investors. Newest first.
- "Growth mode": workforce, average monthly postings, and the last 5 full months against the 5 before.
- "Who signs": usually the founder, CEO or CFO at this stage; name them with title and time in role.
- "What this means for [What I sell]": 2 bullets.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Debt and secondary": same columns as the equity table.

RULES
- Debt and secondary sales are not equity rounds; keep them out of the equity table and the round count.
- Amounts in $M; write "undisclosed" for missing valuations.
- No funding returned: say it may be bootstrapped, public or untracked; if public, suggest "One-page account brief".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
[Company] funding: bottom line and who signs, then total raised, last round (date, amount, valuation, leads), last 5 equity rounds in $M with debt separate, and the hiring trend.
```

### Follow-ups

- Who are the lead investors' other portfolio companies in my ideal customer profile?
- Which leaders joined in the last 6 months?
- Compare its hiring with [Competitor]'s.

### Tips

- Public companies return nothing here. Use "One-page account brief" for them.
- A recent large round is often one of the strongest why-now signals for a scale-up.

## Account SWOT, outside-in

- **id:** `research-swot`
- **What you get:** A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and the named person to take it to.
- **Use it when:** Preparing an executive briefing or a point of view for a strategic pursuit. A shorter SWOT is also an optional section in "Draft an account plan".
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. retail supply-chain AI and data services)

### Detailed prompt

```text
Act as my strategy analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. retail supply-chain AI and data services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue and EBITDA margin for the last 3 fiscal years, and revenue growth by business unit.
3. Pull the 10 most recent stated priorities, preferring the function closest to [What I sell].
4. Pull hiring workloads trending up and declining over the last 12 months in the function closest to [What I sell]; add the company-wide top 3 for context.
5. Pull workforce growth and the top 5 companies they lose people to.
6. Pull technology added in the last 12 months (High and Medium usage only), the top 3 executives in the function closest to [What I sell] and the top news from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Strengths (growth, margin, capabilities being built), Weaknesses (shrinking units or margins, attrition, priorities without hiring), Opportunities (priorities with hiring and technology behind them), Threats (layoffs, talent loss, cost pressure): 3–4 bullets each, the point then dated evidence in brackets.
- "Where [What I sell] fits": 3 bullets, each tied to a Weakness or Opportunity, with the likely owner by name where step 6 found one.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Drop any bullet without Draup evidence.
- Phrase weaknesses as questions for the buyer, not judgements.
- Talent-flow data ends about 3 months ago; state the months covered.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Evidence-based SWOT of [Company] from Draup: bottom line and who to take it to, then 3–4 dated bullets each for strengths, weaknesses, opportunities and threats, and where [What I sell] fits.
```

### Follow-ups

- Turn the Opportunities into a 3-slide point of view for the CIO.
- Which executives own the Weaknesses you listed?
- Run the same SWOT for [Company 2] and compare.

### Tips

- Every bullet cites Draup evidence, so you can defend it in front of the customer.
- Building a full account plan? "Draft an account plan" has a shorter SWOT section; use this one when the SWOT itself is the deliverable.
