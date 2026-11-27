# Deal strategy and qualification

Win live opportunities: re-engage stalled deals, answer RFPs, build business cases, handle objections and beat a named competitor.

## Re-open a stalled deal

- **id:** `deals-stalled-reentry`
- **What you get:** A reopen, wait or walk-away verdict on a stalled deal, tested against why it stalled, with the named person to call, the dated change that justifies it and a 90-word re-entry email.
- **Use it when:** A live opportunity has gone quiet for 60+ days, or a prospect said "not now". Use this to restart a stalled or lost deal; use "What changed since [Date]" instead for a routine check on a current customer.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. starbucks.com); Stalled since (e.g. 2026-05-15); Why it stalled (e.g. budget freeze (or: champion left, priority shifted, lost to competitor, no decision)); Last contact (e.g. Jane Doe, VP Supply Chain Systems (optional)); Competitor (e.g. Blue Yonder (optional)); What I sell (e.g. supply-chain planning software)

### Detailed prompt

```text
Act as my deal-rescue strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- Stalled since: [e.g. 2026-05-15]
- Why it stalled: [budget freeze, champion left, priority shifted, lost to competitor or no decision]
- Last contact (optional): [e.g. Jane Doe, VP Supply Chain Systems]
- Competitor (optional): [e.g. Blue Yonder]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Re-enter only on a dated buyer-side change that moved the blocker; otherwise wait.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell]; say which.
3. Test the stall reason. Budget freeze: latest revenue and EBITDA growth. Champion left: look for [Last contact] in 2 pages of the function's executives. Priority shifted: up to 10 function priorities, noting those after [Stalled since]. Lost to competitor: check the whole stack for [Competitor] products (engagements, for a services firm). No decision: run all four lightly.
4. People: the 3 most senior function executives by title, plus anyone under 1 year in title.
5. News since [Stalled since] (up to 12 months; say if it's older): investments, executive moves, vendor selections, layoffs; 20+ items, marking the most important from the last 90 days.
6. Hiring: average monthly function postings, 5 full months before [Stalled since] vs the 5 latest.
7. Pick the re-entry angle: a dated change tied to a priority.

OUTPUT
- Bottom line: 2 sentences — Reopen now, Wait until [event or date] or Walk away, with the deciding fact.
- Recommended next step: a named person (name, full title), the action this week and the dated why-now (or say none).
- Table "Stall reason test": Reason | Still true? (Yes, Weaker, Gone, Not in Draup) | Evidence + date.
- Table "What changed" (up to 6, newest first): Date | Type | What changed | Why it matters.
- "Re-entry email": 90 words max: the dated change, one line of history, one low-friction ask.
- Detail: who to re-engage (Name | Full title | In role since) and hiring.
- Gaps: what Draup lacked; ask in discovery.

RULES
- A reason is "Gone" only with a dated fact after [Stalled since].
- Rate [Competitor]: Red if a product has High usage in my workloads or a services rival holds 30%+ of active engagements there (reopen only on a new trigger); Amber if Medium, new or 10–29%; else Green.
- Falling hiring plus rising investment usually means automation or outsourcing, not a freeze.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
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
- RFP scope: [one line, e.g. payments-analytics data-platform modernisation]
- Area in scope: [1–3 workloads or a function, e.g. Data Engineering, Cloud Computing — or IT]
- Known bidders (optional): [e.g. Accenture, Infosys]
- What I sell: [one line, e.g. data-platform modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
An incumbent-heavy RFP with no matching stated priority is usually column fodder.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Area in scope] to 1–3 workloads; say which.
3. Evaluation priorities: up to 10 in those workloads (if fewer than 3, widen to the function), with quarter and outcome lines.
4. Incumbents: engagements, partners and top 10 providers in those workloads, minus staffing and agencies.
5. Installed tools: top 10 products in those workloads, High then Medium, with vendor.
6. Known bidders: engagements in scope (services) or whole-stack check (software).
7. Panel: one page of 10 executives in those workloads.
8. News, 12 months: vendor selections, partnerships, technology budgets, leadership changes. Review 20+ items; mark the most important from the last 90 days.
9. Money: revenue and growth.

OUTPUT
- Bottom line: 2 sentences — Bid, Bid-to-learn or Qualify-out, and the deciding fact. Bid if 2+ High-weight priorities match and no provider is Red (editable default).
- Recommended next step: a named person (name, full title) from the panel, the action this week and the dated why-now (or say none).
- Table "Likely evaluation priorities" (up to 6): Priority | Source + quarter | Weight | How to answer it. High weight = from the 2 latest quarters (publication month for news priorities) and on scope.
- Table "Who is already there" (up to 8): Provider or vendor | Engagements or products | Share in scope | Rating (Red, Amber, Green).
- "Win themes": 3: theme, their words (dated), our proof, ghosting line.
- "Q&A questions": 5 that expose gaps or hidden incumbent advantages.
- Detail: panel (Name | Full title | Linked priority, up to 6), known-bidder footprint, money.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Ghosting lines describe a weakness, never a named rival.
- Quote any technology budget figure from news.
- Rating: Red if a firm holds 30%+ of in-scope active engagements or a product has High usage in scope; Amber if 10–29% or Medium; else Green.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 500 words above Detail, tables included.
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
- **Use it when:** You need to quantify value for a proposal or CFO conversation. Use this for a new deal's value model; use "Expansion business case from growth units" instead to grow an existing customer.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. medtronic.com); Area affected (e.g. Data Engineering (or a function like IT)); Value levers (e.g. cost per pipeline, time to data, vendor consolidation); Our assumptions (e.g. 20% productivity gain; loaded cost $120K per FTE (optional)); What I sell (e.g. managed data engineering services)

### Detailed prompt

```text
Act as my value engineer. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- Area affected: [workload or function, e.g. Data Engineering, or IT]
- Value levers: [2–3, e.g. cost per pipeline, time to data, vendor consolidation]
- Our assumptions (optional): [e.g. 20% productivity gain; loaded cost $120K per FTE]
- What I sell: [one line, e.g. managed data engineering services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
A case built on the buyer's own numbers, every assumption labelled, survives finance review.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Area affected] to 1–3 workloads and its function; say which.
3. Money: 3-year revenue, EBITDA, IT and R&D spend, growth and next-year forecast.
4. IT spend split, latest two years: software on premise, internal staffing, IT outsourcing, hardware.
5. Workforce: IT and R&D headcount and number of sites.
6. Outsourcing in the workloads: active engagements and partners.
7. Hiring in the workloads: 12-month postings and metros; in the 10 latest postings, note published pay, contract vs full-time, and partner, cost or speed lines.
8. Stated targets: up to 5 priorities in the workloads (else the function) with cost, speed, capacity or risk outcomes.
9. Owner and trigger: the top 3 executives in the function (one page of 10) and the most important 90-day news item.
10. Worked example: per lever, the formula, inputs from above, [Our assumptions], and a low–high result.

OUTPUT
- Bottom line: 2 sentences — the size of the prize as a range and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the biggest lever, the action this week and the dated why-now (or say none).
- Table "Worked example": Lever | Formula | Low | High (USD millions).
- Table "Their numbers" (top 8): Metric | Value | Year | Label.
- "What they said they want": up to 3 bullets: priority, quarter, lever.
- "Assumptions to validate": each of our inputs and who can confirm it (title).
- Detail: full numbers (IT split, headcount, engagements, postings) and up to 3 risks to the case.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Every number carries one label: Reported, Draup estimate, Model forecast or Our assumption.
- No assumptions given? Use a marked placeholder ("[X]% gain — your number").
- Margin % = EBITDA / revenue, same year. If Draup has no IT split, say so.
- A priority about building in-house or cutting vendors goes under risks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- IT spend is Draup-estimated (often modelled from revenue); its growth isn't a signal. Use USD millions at Draup's rate; a forecast over 15% off the latest actual is a model estimate.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 480 words above Detail, tables included.
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
- **Use it when:** You're setting a close date or a champion says "let's revisit next quarter". Use this to set or test the date; use "Mutual action plan on their calendar" instead once the date is agreed.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. 3m.com); Target close date (e.g. 2027-03-31); Business function (e.g. IT (optional)); What I sell (e.g. industrial data-platform software)

### Detailed prompt

```text
Act as my deal-timing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Target close date: [e.g. 2027-03-31]
- Business function (optional): [budget holder's, e.g. IT]
- What I sell: [one line, e.g. industrial data-platform software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Close dates must fit the buyer's calendar.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Fiscal calendar: the latest fiscal year and end date in Draup's financials; the last 5 earnings calls (fiscal label, release date). Infer each quarter's months, the next call and year-end.
4. Budget posture: latest revenue and EBITDA with growth, and next-year forecast. If news or a newer call reports a fiscal year Draup's table lacks, use it, labelled "from news".
5. Money-moving events, last 6 months (20+ items): guidance, cost programmes, layoffs, reorganisations, spin-offs, divestments, big investments, function leadership changes.
6. Hiring in the function: average monthly postings, last 5 full months vs the 5 before.
7. Up to 5 recent priorities in the function, fiscal labels translated to calendar months.
8. People: the top 3 function executives (one page of 10).
9. Judge [Target close date] against fiscal year-end, reorganisations and earnings dates.

OUTPUT
- Bottom line: 2 sentences — the best signature window and whether [Target close date] is Realistic, At risk or Unrealistic.
- Recommended next step: a named person (name, full title) to confirm the budget release date with, the action this week and the dated why-now (or say none).
- Table "Buyer calendar" (up to 8, by date): Date | Event | Effect (Accelerates, Delays, Neutral) | Source.
- "Budget posture": Growing, Holding or Tightening, with 3 dated facts.
- "Signature window": the 4–8 week window and why, plus a fallback.
- "Questions for the buyer": 3 (budget release date, approval thresholds, freeze periods).
- Detail: fiscal mapping (Fiscal period | Calendar months | Evidence), hiring, priorities.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Never assume a calendar fiscal year; derive it from period end and call dates, and show both if they disagree.
- Quote garbled news numbers as written and flag them.
- A reorganisation or spin-off effective inside the window is a Delay unless news ties it to new spending. Label future call dates "inferred".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- IT spend is Draup-estimated (often modelled from revenue); its growth isn't a signal. A forecast over 15% off the latest actual is a model estimate.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
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
- Objections: [not a priority, have a vendor, no budget, build in-house, bad timing, or "all"]
- Area (optional): [workload or function, e.g. Cloud Computing or IT]
- Incumbent (optional): [e.g. Infosys, or Snowflake]
- What I sell: [one line, e.g. managed cloud and data modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Most objections are partly true.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use [Area], or the function closest to [What I sell], as 1–3 workloads; say which.
3. Pull per objection. Not a priority: up to 6 function priorities. Already have a vendor: if I sell software, check the whole stack for the incumbent's products and any second product in the same sub-category (overlap is the opening); if services, active engagements and top providers in the workloads. No budget: revenue, EBITDA, IT spend and split. Build in-house: 12-month postings and in-house priorities. Bad timing: 90-day news on reorganisations, layoffs, leaders, big programmes.
4. Owner and trigger: top 3 function executives and the most important 90-day news item.
5. Judge each (Supports, Partly, Undercuts) and reply: acknowledge, one fact from the last 12 months (no industry trends), reframe, one question.

OUTPUT
- Bottom line: 2 sentences — which are real, which are cover, and what that means for me.
- Recommended next step: a named person (name, full title), the action this week and the dated why-now (or say none).
- Table "Objection scorecard": Objection | Verdict | Key fact (dated) | Source.
- Per objection: "Reply" (under 60 words) and "Question back".
- "If it's real": a re-qualification move (narrower scope, a workload where the incumbent has 3 or fewer engagements, later date).
- Detail: vendors (Provider or product | Engagements or usage | Where thin), money, hiring.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Rate the incumbent: Red (objection real: complement or narrow scope) if a product has High usage in my workloads or a services firm holds 30%+ of engagements there; Amber if Medium or 10–29%; else Green.
- Falling postings undercut "build in-house" and favour consolidation for "have a vendor"; rising ones support building.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Active engagements (Draup-derived) are estimates, not contracts; never quote outsourced headcount.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
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
- **Use it when:** A specific rival is in a live deal with you, as incumbent or the other finalist. Use this for one live deal; use "Is a competitor installed?" instead for a quick check before you pitch.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. medtronic.com); Competitor (e.g. Databricks (product or services firm)); Area in the deal (e.g. Data Engineering (or a function like IT; optional)); Deal stage (e.g. shortlist of two (optional)); What I sell (e.g. cloud data-platform software)

### Detailed prompt

```text
Act as my competitive deal strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- Competitor: [software or services rival, e.g. Databricks or Accenture]
- Area in the deal (optional): [workload or function, e.g. Data Engineering or IT]
- Deal stage (optional): [e.g. shortlist of two]
- What I sell: [one line, e.g. cloud data-platform software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
One deal, not a battlecard.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Area in the deal], or the function closest to [What I sell], to 1–3 workloads; say which.
3. Footprint. Software rival: whole-stack check for its products (strength, last seen, countries). Services rival: active engagements (Draup-derived; never outsourced headcount), tier, workloads, delivery locations.
4. Skills pull (hiring by skill): 12-month count and monthly trend of postings naming [Competitor]'s main product as a skill, in its skill spelling (e.g. CrowdStrike Falcon, not CrowdStrike); if 0, read 3 recent postings in the workload for the spelling and retry once. Note metros.
5. Who else is in the room: High and Medium products in the workloads, or a services rival's top 10 providers.
6. Priorities: up to 5 in the workloads, else the function, else say none (never borrow).
7. People: one page of 10 executives in the workloads; flag skills or past employers tied to [Competitor].
8. News, 12 months: partnerships, vendor selections, hiring plans, any [Company]–[Competitor] announcement; mark the top 90-day item.

OUTPUT
- Bottom line: 2 sentences — the rating and our best path.
- Recommended next step: a named person (name, full title) to align with, the action this week and the dated why-now.
- Table "Rival footprint" (up to 8): Product or engagement | Usage or tier | Last seen | Where.
- Table "Landmines" (3): Question or proof point | What it exposes | When to use it.
- "Their likely pitch": 3 bullets tied to account facts.
- "Our wedge": 2–3 areas where evidence favours us.
- Detail: skills pull, who else is there, priorities, people (Name | Full title | Leaning, likely).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Rating: Red if a [Competitor] product has High usage in the deal's workloads or a services rival holds 30%+ of active engagements there; Amber if Medium, newly detected or 10–29%; else Green.
- Landmines are fair questions grounded in a dated fact; never claim the rival's pricing, roadmap or unshown weaknesses.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
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

- For job-ad counts use the product's skill name (CrowdStrike Falcon, not CrowdStrike); for the stack, use the maker as Draup spells it (e.g. Salesforce.com).
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
Fragmented providers under a cost programme mean consolidation; a concentrated base means an incumbent to dislodge.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Work in scope] to 1–3 workloads (types of work) and say which.
3. Whole account: active engagements and partners.
4. In scope: active engagements and partners in those workloads, then the top 10 providers; compute the top-3 share.
5. Software deals: the top 10 technology vendors in the workloads, with main products.
6. Up to 5 Procurement priorities, with outcome lines and linked tools and providers.
7. Pressure, last 12 months of news: savings programmes, restructuring, layoffs, divestments, vendor consolidation, outsourcing deals. Review at least 20 items; mark the most important from the last 90 days.
8. Procurement executives, one page of 10: look for IT, indirect, digital or technology procurement titles; flag subsidiaries. If none, take the top 3 executives in the function that owns the work.

OUTPUT
- Bottom line: 2 sentences — the stance to expect (Consolidate, Cost-down, Competitive re-bid or Strategic partner) and what it means for [What I sell].
- Recommended next step: a named person (name, full title) in procurement, or the business owner if none, the action this week and the dated why-now (or say none).
- Table "Provider landscape" (top 10 in scope): Rank | Provider | Active engagements | Share. Then the top-3 share and a label: Concentrated over 50%, Fragmented under 30% (editable defaults), else Mixed.
- Table "Pressure on procurement" (up to 5): Date | Programme or event | Figure | Source.
- "What they'll ask for" (rate card, outcome pricing, transition plan, savings commitment) and "How to prepare": 3 moves.
- Detail: whole-account context, procurement tools, software vendors, "Procurement contacts" (Name | Full title | Unit | IT/indirect or direct materials).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Exclude advertising, media, PR, staffing and market-research firms when the deal is IT or services work, and say so.
- A savings programme counts only if news names a target, date or scope.
- If no IT, indirect or technology procurement lead appears, say so rather than naming a direct-materials buyer.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
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
- Decision maker (optional): [e.g. SVP Global Supply Chain]
- Status quo (optional): [e.g. SAP IBP, or spreadsheets]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
The pack must read as the champion's own argument, short enough to forward.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the champion's function; say which.
3. Their words: up to 6 function priorities with quarter and outcome; mark earnings-call ones.
4. Money: revenue and EBITDA growth.
5. Momentum: 12-month monthly function postings (rising, flat or falling).
6. Recent events, last 90 days (15+ items): investments, orders, cost actions, leadership moves.
7. Peer moves: 6 months of industry news where a named peer adopted what I sell.
8. Check the whole stack for any named status-quo tool's maker.
9. Decision maker: if I gave none, pick the likely economic buyer from the top 3 function executives (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the case the champion can make and what it means for [What I sell].
- Recommended next step: a named person (name, full title) the champion should route the pack to, the action this week and the dated why-now (or say none).
- "Why now": 3 bullets, each a dated fact plus implication; lead with an earnings-call priority if any.
- Table "If they ask…": Who (CFO, CIO, Procurement) | Answer | Fact behind it (dated).
- "Internal email": 150 words max, champion to decision maker, no vendor name in the first two sentences, a specific ask.
- "Cost of waiting": 2 bullets tied to stated outcomes.
- Detail: peer moves (or "No peer proof in Draup"), status-quo usage, "Don't say" (2 claims).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Write Why now and the email in the buyer's voice ("we", "our"); no superlatives about us.
- Priority outcome lines are Draup summaries, not verbatim quotes.
- A status-quo tool at High usage in my workloads is Red: frame us as an addition or phased swap; Medium is Amber; else Green.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low. Say "fading", never "dropped".
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 480 words above Detail, tables included.
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
- Deal summary: [e.g. AI support services, $2M, close 2026-12-31]
- Stated pain: [e.g. support costs rising with volume]
- Forecast category: [Commit, Best case or Pipeline]
- Competitor (optional): [e.g. Concentrix]
- What I sell: [one line, e.g. AI-enabled customer-support services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
This shows where the rep's story and the evidence disagree.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell] and its 1–3 workloads; say which.
3. Pain: up to 6 priorities in the function that match [Stated pain].
4. Money: revenue and EBITDA growth.
5. Activity: postings in the function (last 5 full months vs the 5 before) and active engagements.
6. People: one page of 10 function executives: top 3 and anyone under 1 year in title.
7. Events, last 90 days (20+ items): layoffs, restructuring, leadership changes, cost programmes, acquisitions, guidance.
8. Competition: [Competitor] in the stack (software) or engagements (services).
9. Score each dimension 0–2 against [Forecast category] and the close date.

OUTPUT
- Bottom line: 2 sentences — whether the forecast category holds and the recommended category.
- Recommended next step: a named person (name, full title) at the account to verify the deal with, the action this week and the dated why-now (or say none).
- Table "Scorecard": Dimension | Score | Evidence + date | Contradicts the rep? Then Total out of 10 and category: Commit 8–10, Best case 6–7, Pipeline 4–5, Omit 0–3 (editable defaults).
- "Questions for the rep": 4, tied to weak scores.
- "Red flags": up to 3.
- Detail: the numbers behind each score.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Pain 2 = a matching priority in the 2 latest quarters. Money 2 = growth and no cost action touching the function. Timing 2 = no blocking event before close. People 2 = stable, or a new leader with a mandate. Competition: 0 if [Competitor] is Red (a product at High usage, or 30%+ of active engagements in my workloads), 1 if Amber (Medium, newly detected or 10–29%), 2 if Green (Low-only, under 10% or absent). Activity informs Money and Timing; it isn't scored.
- Layoffs hurt Money only if they hit the function or signal a freeze. Never score to match the rep.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
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
- **Use it when:** You've agreed a target close date and want a plan both sides sign up to. Use this once the date is agreed; use "Pick a realistic signature window" instead to test the date first.
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
Plans that ignore the buyer's calendar slip; give every step a buyer owner.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell]; say which.
3. Fiscal calendar: the latest fiscal year and end date from Draup's financials; the last 5 earnings calls (label, release date). Infer year-end, the next call and quarter-ends in the window.
4. Stakeholders: function executives (one page of 10) and Procurement executives (5): technology or indirect procurement, and anyone under 1 year in title.
5. Events, last 90 days and announced for the window (15+ items): leadership changes with effective dates, reorganisations, divestments, spin-offs, investor events.
6. Up to 3 recent priorities in the function to anchor the objective.
7. Build backwards from [Target close date] using [Steps still needed], or the default: business case, security review, procurement, legal, executive approval, signature, kickoff.

OUTPUT
- Bottom line: 2 sentences — Achievable, Tight or Unrealistic, with an alternative date if needed.
- Recommended next step: a named person (name, full title) to send the draft plan to, the action this week and the dated why-now (or say none).
- Table "Mutual action plan" (up to 8): Step | Target date | Buyer owner and ours | Exit criteria | Calendar note.
- Table "Buyer calendar" (up to 6): Date | Event (fiscal year-end, quarter-end, earnings call, leadership start) | Effect on the plan.
- "Objective": one sentence in the buyer's words, tied to a dated priority.
- "Timeline risks": up to 3, each with the step it threatens and a mitigation.
- Detail: "Stakeholders" (Name | Full title | Role: approver, reviewer, signer, user | In title since), up to 8.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Never assume a calendar fiscal year; derive it from financials and call dates and say how.
- A senior leader starting or leaving inside the window is a timeline risk; name the effective date.
- Default durations (editable): security review 3 weeks, procurement 3, legal 2, executive approval 1.
- Don't name subsidiary executives as approvers unless the deal is with that unit. Label future call dates "inferred".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
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
