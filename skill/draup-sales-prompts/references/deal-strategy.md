# Deal strategy and qualification

Win live opportunities: re-engage stalled deals, answer RFPs, build business cases, handle objections and beat a named competitor.

## Re-open a stalled deal

- **id:** `deals-stalled-reentry`
- **What you get:** A reopen, wait or walk-away verdict on a stalled deal, tested against why it stalled, with the named person to call, the dated change that justifies it and a 90-word re-entry email.
- **Use it when:** A live opportunity has gone quiet for 60+ days, or a prospect said "not now". Use this to restart a stalled or lost deal; use "What changed since [Date]" (signals-change-log) instead for a routine check on a current customer.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. starbucks.com); Stalled since (e.g. 2026-05-15); Why it stalled (e.g. budget freeze (or: champion left, priority shifted, lost to competitor, no decision)); Last contact (e.g. Jane Doe, VP Supply Chain Systems (optional)); Competitor (e.g. Blue Yonder (optional)); What I sell (e.g. supply-chain planning software)

### Detailed prompt

```text
Act as my deal-rescue strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- Stalled since: [date it went quiet, e.g. 2026-05-15]
- Why it stalled: [budget freeze, champion left, priority shifted, lost to competitor, no decision — or your words]
- Last contact (optional): [name and title, e.g. Jane Doe, VP Supply Chain Systems]
- Competitor (optional): [e.g. Blue Yonder]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
A credible re-entry names a dated change on the buyer's side and shows the blocker has moved; if it still holds, recommend waiting.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell]; say which.
3. Test the stall reason. Budget freeze: latest revenue and EBITDA growth. Champion left: look for [Last contact] in 2 pages (10 per page) of that function's executives. Priority shifted: up to 10 priorities in the function, noting those sourced after [Stalled since]. Lost to competitor: check the whole stack for [Competitor] products. No decision: run all four lightly.
4. People: the 3 most senior executives in the function by title, plus anyone under 1 year in title.
5. News since [Stalled since] (up to 12 months): investments, executive moves, vendor selections, layoffs. Review 20+ items; mark the most important from the last 90 days.
6. Hiring: average monthly postings in the function, 5 full months before [Stalled since] vs the 5 latest.
7. Pick the re-entry angle: a dated change tied to a priority.

OUTPUT
- Bottom line: 2 sentences — Reopen now, Wait until [event or date] or Walk away, with the deciding fact.
- Recommended next step: a named person (name, full title), the action this week and the dated why-now; if none, say so.
- Table "Stall reason test": Reason | Still true? (Yes, Weaker, Gone, Not in Draup) | Evidence + date.
- Table "What changed" (up to 6, newest first): Date | Type | What changed | Why it matters.
- "Re-entry email": 90 words max: open with the dated change, at most one line on history, one low-friction ask.
- Detail: who to re-engage (Name | Full title | In role since) and hiring.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- A reason is "Gone" only with a dated fact after [Stalled since].
- A [Competitor] product with High usage in the workloads I sell into is Red: reopen only on a new trigger. Medium or newly detected is Amber.
- Falling hiring with rising investment usually means automation or outsourcing, not a freeze.
- News and hiring reach back 12 months; if [Stalled since] is older, say so.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
My deal at [Company] stalled on [Stalled since] because [Why it stalled]. Lead with reopen, wait or walk away, then the named person to call and the dated change since. Add the stall-reason test and a 90-word re-entry email.
```

### Follow-ups

- Write a 3-touch re-engagement sequence (email, call script, LinkedIn note) around the re-entry angle.
- Profile the newest leader in that function and suggest two openers.
- Run the renewal-style risk check on this account before I commit time to it.

### Tips

- Be honest about why it stalled. The prompt tests that reason first, which is what makes the re-entry credible.
- A new leader in the buying function is often the best re-entry: they have no history with the old "no".
- If the verdict is Wait, put the named event in your calendar and re-run the prompt then.

## RFP research and bid/no-bid call

- **id:** `deals-rfp-research`
- **What you get:** A bid, bid-to-learn or qualify-out call on an RFP, with the likely evaluation priorities, who is already there, the named panel member to reach, three win themes and the questions to submit in the Q&A window.
- **Use it when:** An RFP, RFI or tender has landed and you have days, not weeks, to decide whether to bid and how to position.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 6–10 min
- **Inputs:** Company (e.g. mastercard.com); RFP scope (e.g. managed data-platform modernisation for payments analytics); Area in scope (e.g. Data Engineering, Cloud Computing (or a function like IT)); Known bidders (e.g. Accenture, Infosys (optional)); What I sell (e.g. data-platform modernisation services)

### Detailed prompt

```text
Act as my bid manager. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. mastercard.com]
- RFP scope: [one line from the RFP, e.g. managed data-platform modernisation for payments analytics]
- Area in scope: [1–3 workloads or a function, e.g. Data Engineering, Cloud Computing — or IT]
- Known bidders (optional): [e.g. Accenture, Infosys]
- What I sell: [one line, e.g. data-platform modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
RFPs mirror priorities the buyer already stated, often shaped by an incumbent. An incumbent-heavy RFP with no matching priority is usually column fodder.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Turn [Area in scope] into 1–3 workloads (types of work, e.g. Data Engineering); if I gave a function, map it and say which.
3. Evaluation priorities: up to 10 in those workloads (if fewer than 3, widen to the function), with quarter and outcome lines.
4. Incumbents: engagements and partners in those workloads, then the top 10 providers, minus staffing and agency firms.
5. Installed tools: the top 10 products in those workloads by usage (High, then Medium), with vendor.
6. Known bidders: engagements in scope (services) or whole-stack check (software).
7. Panel: executives in those workloads, up to 2 pages of 10.
8. News, 12 months: vendor selections, partnerships, technology budgets, leadership changes. Review 20+ items; mark the most important from the last 90 days.
9. Money: revenue and growth.

OUTPUT
- Bottom line: 2 sentences — Bid, Bid-to-learn or Qualify-out, and the deciding fact. Bid if 2+ High-weight priorities match and no provider holds over 40% of in-scope engagements (editable default).
- Recommended next step: a named person (name, full title) from the panel, the action this week and the dated why-now; if none, say so.
- Table "Likely evaluation priorities" (up to 6): Priority | Source + quarter | Weight | How to answer it. High weight = from the 2 latest quarters (publication month for news priorities) and on scope.
- Table "Who is already there" (up to 8): Provider or vendor | Engagements or products | Share in scope | Threat (Incumbent, Contender, Minor).
- "Win themes": 3: theme, their words (dated), our proof, ghosting line.
- "Q&A questions": 5 that expose gaps or hidden incumbent advantages.
- Detail: panel (Name | Full title | Linked priority, up to 6), known-bidder footprint, money.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Ghosting lines describe a weakness, never a named rival.
- Quote any technology budget figure from news.
- A known bidder's product with High usage in scope is Red (incumbent advantage); Medium is Amber.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 500 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
RFP at [Company], scope [RFP scope]. Lead with bid, bid-to-learn or qualify-out, and the named panel member to reach with a dated why-now. Then likely evaluation priorities, incumbents in [Area in scope], 3 win themes and 5 Q&A questions.
```

### Follow-ups

- Draft the executive summary of our response (250 words) using the win themes.
- Turn the evaluation priorities into a compliance matrix with our response approach per row.
- Profile the top panel member and suggest how to address them in the orals.
- Show the 10 most recent engagements of the top incumbent in these workloads.

### Tips

- Paste the RFP's own scope sentence; the closer it matches the buyer's language, the better the priority match.
- Use the Q&A questions to make the buyer state things the incumbent already knows.
- If the call is Qualify-out, spending the bid budget elsewhere is often the better decision.

## Business-case inputs from their numbers

- **id:** `deals-business-case-inputs`
- **What you get:** The size of the prize as a range, built on the account's own revenue, margin, spend, outsourcing and hiring, with every number labelled, a worked example you can edit and the named owner to validate it with.
- **Use it when:** You need to quantify value for a proposal or CFO conversation. Use this for a new deal's value model; use "Expansion business case from growth units" (expand-business-case) instead to grow an existing customer.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. medtronic.com); Area affected (e.g. Data Engineering (or a function like IT)); Value levers (e.g. cost per pipeline, time to data, vendor consolidation); Our assumptions (e.g. 20% productivity gain; loaded cost $120K per FTE (optional)); What I sell (e.g. managed data engineering services)

### Detailed prompt

```text
Act as my value engineer. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- Area affected: [workload or function your offer changes, e.g. Data Engineering, or IT]
- Value levers: [2–3, e.g. cost per pipeline, time to data, vendor consolidation]
- Our assumptions (optional): [e.g. 20% productivity gain; loaded cost $120K per FTE]
- What I sell: [one line, e.g. managed data engineering services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
CFOs discount industry averages; a case built on the buyer's own numbers, with every assumption labelled and editable, survives finance review.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Map [Area affected] to 1–3 workloads (types of work) and its business function; say which.
3. Money: 3-year revenue, EBITDA, Draup-estimated IT and R&D spend, latest growth and next-year forecast.
4. IT spend split, latest two years: software on premise, internal staffing, IT outsourcing, hardware.
5. Workforce: IT and R&D headcount and number of sites.
6. Outsourcing in the workloads: active engagements and partners.
7. Hiring in the workloads: 12-month postings and metros; then the 10 latest postings, noting published pay, contract versus full-time, and lines naming partners, cost or speed targets.
8. Stated targets: up to 5 priorities in the workloads (if none, the function) with outcome lines naming a cost, speed, capacity or risk goal.
9. Owner and trigger: the top 3 executives in the function (one page of 10) and the most important news item from the last 90 days.
10. Worked example: per lever, the formula, inputs from above, [Our assumptions], and a low–high result.

OUTPUT
- Bottom line: 2 sentences — the size of the prize as a range and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the biggest lever, the action this week and the dated why-now; if none, say so.
- Table "Worked example": Lever | Formula | Low | High (USD millions).
- Table "Their numbers" (top 8): Metric | Value | Year | Label (Reported, Draup estimate, Model forecast, Our assumption).
- "What they said they want": up to 3 bullets: priority, quarter, lever.
- "Assumptions to validate": each of our inputs and who can confirm it (title).
- Detail: full numbers (IT split, headcount, engagements, postings) and up to 3 risks to the case.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Every number carries one label: Reported, Draup estimate, Model forecast or Our assumption.
- With no assumptions given, use a marked placeholder ("[X]% gain — your number"); never invent one.
- Margin % = EBITDA / revenue, same year. If Draup has no IT split, say so.
- A priority about building in-house or cutting vendors goes under risks.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- IT spend is Draup-estimated, often modelled from revenue; don't treat its growth as a signal. Use USD millions at Draup's rate. A forecast over 15% off the latest actual is a model estimate.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 480 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Business-case inputs for [What I sell] at [Company]. Lead with the prize as a range and the named person to validate it. Show their numbers, each labelled Reported, Draup estimate or Our assumption, and a worked example per lever.
```

### Follow-ups

- Turn the worked example into a one-slide value summary for the CFO.
- Rebuild the case with conservative assumptions and show payback at our price of [Price].
- Which executive owns each lever? Map them to the buying committee.

### Tips

- Give your own assumptions where you have proof; the prompt keeps them visibly separate from the buyer's numbers.
- Show ranges, not single numbers. Finance teams trust a range they can tighten in the meeting.
- Postings rarely publish pay; if none do, bring your own loaded-cost figure and label it.

## Pick a realistic signature window

- **id:** `deals-budget-timing`
- **What you get:** Whether your close date fits the buyer's fiscal calendar and budget posture, the events that move money in the next two quarters, the best 4–8 week signature window and the named person to confirm it with.
- **Use it when:** You're setting a close date or a champion says "let's revisit next quarter". Use this to set or test the date; use "Mutual action plan on their calendar" (deals-mutual-action-plan) instead once the date is agreed.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. 3m.com); Target close date (e.g. 2027-03-31); Business function (e.g. IT (optional)); What I sell (e.g. industrial data-platform software)

### Detailed prompt

```text
Act as my deal-timing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Target close date: [e.g. 2027-03-31]
- Business function (optional): [the budget holder's function, e.g. IT]
- What I sell: [one line, e.g. industrial data-platform software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Deals slip when the close date ignores the buyer's calendar: fiscal year-end, budget release, earnings, reorganisations and spin-offs.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Fiscal calendar: the latest fiscal year in Draup's financials and its end date; the last 5 earnings calls with fiscal label and release date. Infer each fiscal quarter's months, the next call and the fiscal year-end.
4. Budget posture: latest revenue and EBITDA with growth, and next-year forecast. If news or a newer call reports a fiscal year Draup's table lacks, use it, labelled "from news".
5. Money-moving events, last 6 months: guidance, cost programmes, layoffs, reorganisations, spin-offs, divestments, big investments, leadership changes in the function. Review at least 20 items.
6. Hiring in the function: average monthly postings, last 5 full months versus the 5 before.
7. Up to 5 recent priorities in the function, fiscal labels translated to calendar months.
8. People: the top 3 executives in the function (one page of 10).
9. Judge [Target close date] against fiscal year-end, reorganisations and earnings dates.

OUTPUT
- Bottom line: 2 sentences — the best signature window and whether [Target close date] is Realistic, At risk or Unrealistic.
- Recommended next step: a named person (name, full title) to confirm the budget release date with, the action this week and the dated why-now; if none, say so.
- Table "Buyer calendar" (up to 8, by date): Date | Event | Effect (Accelerates, Delays, Neutral) | Source.
- "Budget posture": Growing, Holding or Tightening, with 3 dated facts.
- "Signature window": the 4–8 week window and why, plus a fallback.
- "Questions for the buyer": 3 (budget release date, approval thresholds, freeze periods).
- Detail: fiscal mapping (Fiscal period | Calendar months | Evidence), hiring, priorities.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Never assume a calendar fiscal year; derive it from period end and call dates, and show both if they disagree.
- Quote garbled news numbers as written and flag them.
- A reorganisation or spin-off effective inside the window is a Delay unless news ties it to new spending. Label future call dates "inferred".

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- IT spend is Draup-estimated, often modelled from revenue; don't treat its growth as a signal. Use USD millions at Draup's rate. A forecast over 15% off the latest actual is a model estimate.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Is [Target close date] realistic at [Company]? Lead with the best signature window and the named person to confirm it with, then fiscal quarters as calendar months, budget posture and events in the next 6 months that move money.
```

### Follow-ups

- Build a mutual action plan backwards from the recommended signature window.
- Draft a short note to my champion asking the 3 calendar questions.
- Is their budget growing or shrinking? Show the 3-year trend and IT spend split.

### Tips

- Ask your champion when the next budget is released; it is the single most useful date in the deal.
- Spin-offs and reorganisations often freeze new vendor decisions for a quarter or more. Plan around them.
- Re-run this before each forecast call; events change the window.

## Answer objections with their own facts

- **id:** `deals-objection-handler`
- **What you get:** Which objections are real and which are cover, with a short reply and a question back for each, built on dated facts about the account, and the named person to take the answer to.
- **Use it when:** A buyer has pushed back (not a priority, already have a vendor, no budget, we'll build in-house, bad timing), or before a meeting where you expect pushback.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. adobe.com); Objections (e.g. already have a vendor; bad timing (or: all)); Area (e.g. Cloud Computing, Data Engineering (or a function like IT; optional)); Incumbent or competitor (e.g. Infosys (optional)); What I sell (e.g. managed cloud and data modernisation services)

### Detailed prompt

```text
Act as my objection-handling coach. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. adobe.com]
- Objections: [not a priority; have a vendor; no budget; build in-house; bad timing — or "all"]
- Area (optional): [workloads or a function, e.g. Cloud Computing — or IT]
- Incumbent or competitor (optional): [e.g. Infosys, or Snowflake]
- What I sell: [one line, e.g. managed cloud and data modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Objections are usually partly true: acknowledge it, add one hard fact from their company, ask a question; if the evidence agrees, re-qualify.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use [Area], or the function closest to [What I sell], as 1–3 workloads; say which.
3. Pull only what the objections need. Not a priority: up to 6 priorities in the function. Already have a vendor: active engagements and top providers in the workloads; for software, check the whole stack for the incumbent's products. No budget: revenue, EBITDA, Draup-estimated IT spend and split. Build in-house: 12 months of postings in the workloads and any in-house priority. Bad timing: 90 days of news on reorganisations, layoffs, leadership changes and big programmes.
4. Owner and trigger: the top 3 executives in the function and the most important 90-day news item.
5. Judge each: Supports, Partly or Undercuts.
6. Reply: acknowledge, one dated fact, reframe, one question.

OUTPUT
- Bottom line: 2 sentences — which objections are real, which are cover, and what it means for [What I sell].
- Recommended next step: a named person (name, full title), the action this week and the dated why-now; if none, say so.
- Table "Objection scorecard": Objection | Verdict | Key fact (dated) | Source.
- Per objection: "Reply" (under 60 words) and "Question back".
- "If it's real": a re-qualification move (narrower scope, another workload, later date).
- Detail: vendor table (Provider or product | Engagements or usage | Where thin), money, hiring.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Each reply uses a fact from the last 12 months, never industry trends.
- A large incumbent isn't a reason to quit: find workloads where it has 3 or fewer engagements. Ignore the company's own products.
- An incumbent product with High usage in my workloads is Red (the objection is real: position as complement or narrower scope); Medium is Amber.
- Falling postings undercut "we'll build in-house"; rising ones support it.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- Trust usage strength and last-seen date; ignore confidence scores and "Generic" rows. A last-seen date shared by many rows is a data refresh. Say "fading", never "dropped".
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Answer these objections at [Company] with dated Draup facts: [Objections]. Lead with which are real, which are cover, and the named person to take it to. For each: verdict, the key fact, a 60-word reply and a question back.
```

### Follow-ups

- Role-play the buyer: raise these objections one by one and score my replies.
- Turn the 'already have a vendor' answer into a one-page second-vendor point of view.
- Write a follow-up email that answers the objection I heard today in under 120 words.

### Tips

- Ask for "all" before a big meeting; pick one or two right after a call so the answers stay sharp.
- A Supports verdict is useful: it tells you to change scope or timing rather than push harder.

## Win plan against a rival

- **id:** `deals-competitive-strategy`
- **What you get:** How entrenched a named rival is at the account (rated Red, Amber or Green), the pitch they'll likely make, your wedge, three landmine questions and the named person to align with first.
- **Use it when:** A specific rival is in a live deal with you, as incumbent or the other finalist. Use this for one live deal; use "Is a competitor installed?" (tech-competitor-installed) instead for a quick check before you pitch.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. medtronic.com); Competitor (e.g. Databricks (product or services firm)); Area in the deal (e.g. Data Engineering (or a function like IT; optional)); Deal stage (e.g. shortlist of two (optional)); What I sell (e.g. cloud data-platform software)

### Detailed prompt

```text
Act as my competitive deal strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- Competitor: [the rival, software or services, e.g. Databricks or Accenture]
- Area in the deal (optional): [workload or function, e.g. Data Engineering — or IT]
- Deal stage (optional): [e.g. shortlist of two]
- What I sell: [one line, e.g. cloud data-platform software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
This is one deal, not a battlecard: how embedded the rival is here and where the evidence favours us. Never claim unshown weaknesses.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use [Area in the deal], or the function closest to [What I sell], mapped to 1–3 workloads; say which.
3. Footprint. Software rival: whole-stack check for its products (strength, last seen, countries, workloads). Services rival: its engagements, tier, workloads and delivery locations.
4. Skills pull: the 12-month count and trend of postings naming [Competitor]'s main product as a skill (from hiring by skill, not full postings), plus metros from up to 10 postings.
5. Who else is in the room: High and Medium products in the workloads (software rival) or the top 10 providers (services rival).
6. Priorities: up to 5 in the workloads, else the function, else say none.
7. People: one page of 10 executives in the workloads; flag skills or past employers pointing to [Competitor].
8. News, last 12 months: partnerships, vendor selections, hiring plans in the area, any [Company]–[Competitor] announcements; mark the most important from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the entrenchment rating and our best path.
- Recommended next step: a named person (name, full title) to align with, the action this week and the dated why-now; if none, say so.
- Table "Rival footprint" (up to 8): Product or engagement | Usage or tier | Last seen | Where.
- Table "Landmines" (3): Question or proof point | What it exposes | When to use it.
- "Their likely pitch": 3 bullets tied to account facts.
- "Our wedge": 2–3 areas where the evidence favours [What I sell].
- Detail: skills pull, who else is there, priorities, people to align (Name | Full title | Leaning, likely).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Rating: Red if a [Competitor] product has High usage in the deal's workloads, or a services rival holds the most engagements there; Amber if Medium usage, newly detected or a top-3 provider; Green otherwise.
- Landmines are fair questions grounded in a dated fact; no claims about the rival's pricing or roadmap.
- Never borrow priorities from other functions.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- Trust usage strength and last-seen date; ignore confidence scores and "Generic" rows. A last-seen date shared by many rows is a data refresh. Say "fading", never "dropped".
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
[Competitor] is in my deal at [Company]. Lead with how entrenched they are (Red, Amber, Green) and the named person to align with. Then their footprint, likely pitch, our wedge and 3 landmine questions.
```

### Follow-ups

- Write the discovery script that works the 3 landmines in naturally.
- Draft a reference-call brief: which of our customers should talk to them and what they should cover.
- Build the one-page battlecard for [Competitor] in my industry.
- Which of their leaders came from companies where [Competitor] is big?

### Tips

- Name the rival as Draup would spell it (product or company); if nothing comes back, try the maker's name.
- Skills in job ads often show a rival's real depth better than the installed-stack view alone.
- Software rival in a services deal (or the reverse)? Run it twice, once for each, and compare.

## Prepare for their procurement team

- **id:** `deals-procurement-landscape`
- **What you get:** The procurement stance to expect (consolidate, cost-down, re-bid or strategic), who already supplies the work in scope and how concentrated they are, the pressure procurement is under and the named procurement lead to reach.
- **Use it when:** A deal is heading to procurement or a vendor-selection process, or the buyer mentions consolidation or a preferred-supplier list.
- **Best for:** Account Executive, Services, SI & Staffing Seller, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. roche.com); Work in scope (e.g. Application Development & Maintenance (or a function like IT)); Deal type (e.g. services (or software)); What I sell (e.g. application management services)

### Detailed prompt

```text
Act as my procurement strategy advisor for sellers. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. roche.com]
- Work in scope: [workload or function being bought, e.g. Application Development & Maintenance — or IT]
- Deal type: [services or software]
- What I sell: [one line, e.g. application management services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Fragmented providers under a cost programme mean consolidation and rate pressure; a concentrated base means an incumbent to dislodge. Find the technology procurement lead, not direct materials.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Map [Work in scope] to 1–3 workloads (types of work) and say which.
3. Whole account: active engagements and partners.
4. In scope: active engagements and partners in those workloads, then the top 10 providers; compute the top-3 share.
5. Software deals: the top 10 technology vendors in the workloads, with main products.
6. Up to 5 Procurement priorities, with outcome lines and linked tools and providers.
7. Pressure, last 12 months of news: savings programmes, restructuring, layoffs, divestments, vendor consolidation, outsourcing deals. Review at least 20 items; mark the most important from the last 90 days.
8. Procurement executives, one page of 10: look for IT, indirect, digital or technology procurement titles; flag subsidiaries. If none, take the top 3 executives in the function that owns the work.

OUTPUT
- Bottom line: 2 sentences — the stance to expect (Consolidate, Cost-down, Competitive re-bid or Strategic partner) and what it means for [What I sell].
- Recommended next step: a named person (name, full title) in procurement, or the business owner if none, the action this week and the dated why-now; if none, say so.
- Table "Provider landscape" (top 10 in scope): Rank | Provider | Active engagements | Share. Then the top-3 share and a label: Concentrated over 50%, Fragmented under 30% (editable defaults), else Mixed.
- Table "Pressure on procurement" (up to 5): Date | Programme or event | Figure | Source.
- "What they'll ask for" (rate card, outcome pricing, transition plan, savings commitment) and "How to prepare": 3 moves.
- Detail: whole-account context, procurement tools, software vendors, "Procurement contacts" (Name | Full title | Unit | IT/indirect or direct materials).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Exclude advertising, media, PR, staffing and market-research firms when the deal is IT or services work, and say so.
- A savings programme counts only if news names a target, date or scope.
- If no IT, indirect or technology procurement lead appears, say so rather than naming a direct-materials buyer.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Procurement read for [Company] on [Work in scope]. Lead with the stance to expect and the named procurement lead to reach. Then incumbents and their share, cost programmes with figures, and 3 moves to prepare.
```

### Follow-ups

- Draft a consolidation proposal outline that reduces their provider count in [Work in scope].
- Which of the incumbents are thinnest here? Show their engagements and tiers.
- Write a 100-word note to the procurement lead framing our offer against their savings programme.

### Tips

- Ask your champion who in procurement covers technology services; Draup's procurement pages often skew to direct materials.
- Fragmented plus a savings target usually means a consolidation play beats a pure price play.

## Arm your champion to sell internally

- **id:** `deals-champion-pack`
- **What you get:** A forwardable brief your champion can use to sell the deal inside: why now in their company's words, cost of waiting, answers for the CFO, CIO and procurement, a 150-word internal email, and who to route it to.
- **Use it when:** You have a champion who supports the deal but needs ammunition to win budget or reach the economic buyer.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. 3m.com); Champion (e.g. Jane Doe, Director Supply Chain Analytics); Decision maker (e.g. SVP Global Supply Chain (optional)); Competitor or status quo (e.g. SAP IBP, or spreadsheets (optional)); What I sell (e.g. supply-chain planning software)

### Detailed prompt

```text
Act as my deal coach who writes for champions. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Champion: [name and title, e.g. Jane Doe, Director Supply Chain Analytics]
- Decision maker (optional): [title or name, e.g. SVP Global Supply Chain]
- Competitor or status quo (optional): [e.g. SAP IBP, or spreadsheets]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Champions lose deals because they can't make the case in their company's language. The pack must read as their argument, short enough to forward.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use the champion's function; say which.
3. Their words: up to 6 priorities in the function with quarter and outcome lines; mark earnings-call ones.
4. Money: revenue and EBITDA growth.
5. Momentum: 12 months of monthly postings in the function (rising, flat or falling).
6. Recent events, last 90 days: investments, orders, cost actions, leadership moves. Review at least 15 items.
7. Peer moves: 6 months of industry news where a named peer adopted what [What I sell] provides.
8. Check the whole stack for any named status-quo tool's maker.
9. Decision maker: if I gave none, take the top 3 executives in the function (one page of 10) and pick the likely economic buyer.

OUTPUT
- Bottom line: 2 sentences — the case the champion can make and what it means for [What I sell].
- Recommended next step: a named person (name, full title) the champion should route the pack to, the action this week and the dated why-now; if none, say so.
- "Why now": 3 bullets in the champion's voice, each a dated fact plus implication; lead with an earnings-call priority if one exists.
- Table "If they ask…": Who (CFO, CIO, Procurement) | Answer | Fact behind it (dated).
- "Internal email": 150 words max, champion to decision maker, no vendor name in the first two sentences, a specific ask.
- "Cost of waiting": 2 bullets tied to stated outcomes.
- Detail: peer moves (or "No peer proof in Draup"), status-quo usage, "Don't say" (2 unsupported claims).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Write Why now and the email as "we" and "our", in the buyer's voice. No superlatives about [What I sell].
- Priority outcome lines are Draup summaries, not verbatim quotes.
- A status-quo tool with High usage in the workloads I sell into is a strong incumbent: frame us as an addition or phased swap, not a rip-out.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- Trust usage strength and last-seen date; ignore confidence scores and "Generic" rows. A last-seen date shared by many rows is a data refresh. Say "fading", never "dropped".
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 480 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Champion pack for [Champion] at [Company]. Lead with the case and the named decision maker to route it to before a dated event, then 3 dated why-now facts, CFO/CIO/procurement answers and a 150-word internal email.
```

### Follow-ups

- Turn the pack into a 3-slide internal deck the champion can present.
- Write the champion's talk track for a 5-minute slot in the staff meeting.
- What would the CFO's objections be? Answer each with a dated fact.

### Tips

- Send the email draft to your champion as a suggestion, not a script; they'll edit it into their own voice.
- Earnings-call priorities carry the most weight internally because leadership said them in public.
- If peer proof comes back empty, swap in your own customer reference rather than stretching the evidence.

## Reality-check a forecasted deal

- **id:** `deals-forecast-check`
- **What you get:** An outside-in score of a forecasted deal on pain, money, timing, people and competition, a recommended forecast category, the questions to ask the rep and the named buyer to verify with.
- **Use it when:** Before a forecast call or deal review, or when a deal looks too good to be true.
- **Best for:** Sales Leader & RevOps, Account Executive, Account & Customer Success Manager
- **Time:** 4–6 min
- **Inputs:** Company (e.g. fedex.com); Deal summary (e.g. AI-enabled customer-support services, $2M, close 2026-12-31); Stated pain (e.g. support costs rising with shipment volume); Forecast category (e.g. Commit); Competitor (e.g. Concentrix (optional)); What I sell (e.g. AI-enabled customer-support services)

### Detailed prompt

```text
Act as my sales manager running a deal review. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. fedex.com]
- Deal summary: [offer, amount, close date, e.g. AI support services, $2M, close 2026-12-31]
- Stated pain: [e.g. support costs rising with shipment volume]
- Forecast category: [the rep's call: Commit, Best case, Pipeline]
- Competitor (optional): [e.g. Concentrix]
- What I sell: [one line, e.g. AI-enabled customer-support services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
When the rep's story and the account's evidence disagree, this shows the manager which questions to ask.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell] (e.g. Customer Support & Service) and its 1–3 workloads; say which.
3. Pain: up to 6 priorities in the function that match [Stated pain].
4. Money: revenue and EBITDA growth.
5. Activity: postings in the function (last 5 full months vs the 5 before) and active engagements.
6. People: one page of 10 function executives: the top 3 and anyone under 1 year in title.
7. Events, last 90 days: layoffs, restructuring, leadership changes, cost programmes, acquisitions, guidance. Review at least 20 items.
8. Competition: [Competitor] in the whole stack (software) or engagements (services).
9. Score each dimension 0–2 against [Forecast category] and the close date.

OUTPUT
- Bottom line: 2 sentences — whether the forecast category holds and the recommended category.
- Recommended next step: a named person (name, full title) at the account to verify the deal with, the action this week and the dated why-now; if none, say so.
- Table "Scorecard": Dimension | Score | Evidence + date | Contradicts the rep? Then Total out of 10 and category: Commit 8–10, Best case 6–7, Pipeline 4–5, Omit 0–3 (editable defaults).
- "Questions for the rep": 4, tied to weak scores.
- "Red flags": up to 3.
- Detail: the numbers behind each score.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Pain 2 = matching priority in the 2 latest quarter labels. Money 2 = growth and no cost action touching the function. Timing 2 = no blocking event before close. People 2 = stable, or a new leader with a mandate. Competition 2 = no strong incumbent; 0 if a [Competitor] product has High usage, or [Competitor] is a top-3 provider by engagements, in my workloads; 1 if Medium, fewer engagements or newly detected. Activity is evidence for Money and Timing, not scored alone.
- Priorities about products [Company] sells aren't internal pain.
- Layoffs hurt Money only if they hit the function or signal a freeze. Never raise a score to match the rep.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Reality-check my [Forecast category] deal at [Company]: [Deal summary]. Lead with whether the category holds and the named buyer to verify with. Score Pain, Money, Timing, People and Competition 0–2 from dated evidence and give 4 questions for the rep.
```

### Follow-ups

- Run this check on my other 5 Commit deals: [Accounts, deal summaries].
- Write the coaching note for the rep in under 120 words.
- Build the plan that gets the weakest dimension to 2 before close.

### Tips

- Use it as a conversation starter in deal reviews, not a verdict on the rep.
- Low Pain plus high Money often means the buyer can afford it but hasn't decided they need it; coach to the business case.
- Re-run after each big event at the account; one news item can flip Timing.

## Mutual action plan on their calendar

- **id:** `deals-mutual-action-plan`
- **What you get:** A mutual action plan built backwards from your close date that respects the buyer's fiscal calendar, names buyer owners at each step, flags events that could move dates and says who to send the draft to.
- **Use it when:** You've agreed a target close date and want a plan both sides sign up to. Use this once the date is agreed; use "Pick a realistic signature window" (deals-budget-timing) instead to test the date first.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Company (e.g. starbucks.com); Deal stage (e.g. technical evaluation complete); Target close date (e.g. 2027-01-29); Steps still needed (e.g. security review, business case sign-off, procurement, legal (optional)); What I sell (e.g. data-platform modernisation services)

### Detailed prompt

```text
Act as my deal desk lead. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- Deal stage: [e.g. technical evaluation complete]
- Target close date: [e.g. 2027-01-29]
- Steps still needed (optional): [e.g. security review, business case sign-off, procurement, legal]
- What I sell: [one line, e.g. data-platform modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Plans that ignore fiscal year-end, freezes, earnings or a new executive mid-plan slip quietly; give every step a buyer owner.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use the business function closest to [What I sell] (e.g. IT) and say which.
3. Fiscal calendar: the latest fiscal year and its end date from Draup's financials; the last 5 earnings calls with fiscal label and release date. Infer fiscal year-end, the next call and quarter-ends in the plan window.
4. Stakeholders: function executives (one page of 10) and Procurement executives (5); look for technology or indirect procurement and anyone under 1 year in title. Flag subsidiaries.
5. Events, last 90 days and announced for the window: leadership changes with effective dates, reorganisations, divestments, IPOs or spin-offs, investor events. Review at least 15 items.
6. Up to 3 recent priorities in the function to anchor the objective.
7. Build backwards from [Target close date] using [Steps still needed], or: business case sign-off, security and architecture review, procurement, legal, executive approval, signature, kickoff.

OUTPUT
- Bottom line: 2 sentences — Achievable, Tight or Unrealistic, with an alternative date if needed.
- Recommended next step: a named person (name, full title) to send the draft plan to, the action this week and the dated why-now; if none, say so.
- Table "Mutual action plan" (up to 8): Step | Target date | Buyer owner and ours | Exit criteria | Calendar note.
- Table "Buyer calendar" (up to 6): Date | Event (fiscal year-end, quarter-end, earnings call, leadership start) | Effect on the plan.
- "Objective": one sentence in the buyer's words, tied to a dated priority.
- "Timeline risks": up to 3, each with the step it threatens and a mitigation.
- Detail: "Stakeholders" (Name | Full title | Role: approver, reviewer, signer, user | In title since), up to 8.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Never assume a calendar fiscal year; derive it from financials and call dates and say how.
- A senior leader starting or leaving inside the window is a timeline risk; name the effective date.
- Default durations (editable): security review 3 weeks, procurement 3, legal 2, executive approval 1.
- Don't name subsidiary executives as approvers unless the deal is with that unit. Label future call dates "inferred".

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

### Quick version

```text
Mutual action plan for [Company] from [Deal stage] to [Target close date]. Lead with Achievable, Tight or Unrealistic and who to send the draft to, then milestones with buyer owners and calendar events that could shift dates.
```

### Follow-ups

- Turn the plan into a one-page document I can share with the buyer (no internal notes).
- Draft the email proposing this plan to my champion.
- Which steps can run in parallel to pull the close date in by two weeks?

### Tips

- Share the plan as a draft and ask the buyer to correct dates; their edits are the best signal of real intent.
- Name buyer owners by function first; confirm names with your champion before sharing.
- Earnings dates are inferred from past calls; check the investor-relations calendar before you commit.
