# Signals and timing

Reach out when something just changed: hiring spikes, leadership moves, news, new tools.

## What's worth acting on now

- **id:** `signals-whats-actionable`
- **What you get:** An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- **Use it when:** Before outreach, at the start of an account cycle, or when an account has gone quiet. Use this for one account; use "Weekly trigger sweep for my book" for up to 10 accounts at once.
- **Best for:** SDR / BDR, Account Executive, Account & Customer Success Manager
- **Time:** 2–4 min
- **Inputs:** Company (e.g. jpmorganchase.com); What I sell (e.g. AI governance software); Territory (optional) (e.g. North America)

### Detailed prompt

```text
Act as my sales-trigger analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- What I sell: [one line, e.g. AI governance software — skip if you ran the start-here prompt]
- Territory (optional): [region I cover, e.g. North America — skip if saved in setup]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull its top-ranked news signals and news feed for the last 90 days; review at least 30 items, or say how many there were.
3. Apply the noise rule (it depends on what I sell); also drop store closures counted as layoffs. The company must be the actor.
4. Keep executive moves (VP and above), M&A, partnerships, expansion, investment plans, restructuring, regulatory inquiries or fines, and incidents or launches that touch my space. Merge repeat coverage; count independent sources.
5. Link each trigger to a stated priority in the function closest to [What I sell] only if the text supports it (source, fiscal quarter); else "no direct link".
6. Rank by relevance to [What I sell], then events in my territory, then recency.
7. Pull the top 3 executives in the function closest to [What I sell] and match each trigger to its likeliest owner, checking titles in the profile bio.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Start with Act, Watch or Skip.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for. Add an opening sentence built on a Confirmed trigger.
- Table "Triggers" (up to 5; if fewer than 3 survive, say so and don't pad): Date | Trigger (with any number) | Why it matters to us | Likely owner (name, title) | Sources (1 = unverified).
- Detail: per trigger, source and headline (link), linked priority (quarter) and action; "Dropped as noise" count by type, naming any incident and whether it was kept; Gaps (what Draup lacked, to ask in discovery).

RULES
- If event and capture dates differ by over 30 days, use the event date and flag it.
- Never build the opening sentence on a single-source or conflicting fact.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line first (Act, Watch or Skip) and next step: a named owner and one dated trigger. Then up to 5 real 90-day triggers at [Company] that bear on [What I sell], incidents included, with source counts.
```

### Follow-ups

- Turn the top trigger into a 70-word email to the person in the next step.
- Who is the new executive in trigger [N]? Pull their professional profile.
- Run the same check for the last 30 days only.
- Which of these triggers has a second source I can quote?

### Tips

- Outages, incidents and regulatory inquiries are kept when they bear on what you sell (security, reliability, observability, IT operations, compliance). Put your offer in the start-here prompt so the filter knows.
- A trigger marked "1 = unverified" is fine for prioritising but not for quoting; the email follow-up will warn you before you send it.
- Fewer than 3 real triggers is a useful answer: lead with a priority, not a news hook.

## Signal-led emails for up to 10 accounts

- **id:** `signals-signal-to-email`
- **What you get:** For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.
- **Use it when:** Use this when you have one to 10 named accounts and want each email anchored on that account's own recent event. Use "ABM messages for a target list" instead for a longer campaign list, a fixed theme or a joint partner note.
- **Best for:** SDR / BDR, Account Executive, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Accounts (e.g. bmw.com, target.com); What I sell (e.g. supply-chain planning software); Persona (e.g. VP Supply Chain); Territory (optional) (e.g. North America); Contact name (optional) (e.g. Jane Doe); Proof point (optional) (e.g. cut forecast error for Contoso Retail)

### Detailed prompt

```text
Act as my outbound copywriter and researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [one website, or up to 10, e.g. bmw.com, target.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Persona: [who reads it, e.g. VP Supply Chain]
- Territory (optional): [region I cover, e.g. North America]
- Contact name (optional): [e.g. Jane Doe]
- Proof point (optional): [a result I may quote, e.g. cut forecast error for Contoso Retail]

STEPS
1. Find each account by website (exact match, parent company); ask if none or several match. Do up to 10 per pass: after each 5, show the table and continue unless I say stop.
2. Pull 60 days of news for all accounts in one feed pull: deals, expansion, executive moves, M&A, investment plans, and incidents that bear on what I sell. If one account fills over half the results, pull the quiet ones separately. The account must be the actor.
3. Per account, pick the signal most relevant to [What I sell], the persona and my territory; prefer events in my territory and say if there are none.
4. Fact-check it (Confirmed, Single source or Conflicting) and pick the persona's stated priority that best fits, with source and fiscal quarter.
5. For one account, or a list's strongest row, pull the top 3 executives in the persona's function and name the best match.
6. Write each message in [Persona]'s language and goals.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Check before sending": each message leaning on a single-source or conflicting fact, and what to verify (or "none").
- One account: signal (date, source, fact check), priority, Subject (7 words max) and opener (70 words max): the signal, the priority as a question, one easy ask. Use contact name and proof point only if given.
- Several accounts: Account | Signal (date; in territory?) | Fact check | Message (2 sentences, 45 words max, ending in the ask).
- Detail: source and headline per account; priority used; priority-only openers where no signal qualified; "Not found" accounts; Gaps (what Draup lacked, to ask in discovery).

RULES
- Quote only Confirmed numbers, exactly as the source states them. Keep fiscal quarters out of the copy.
- Pose the signal–priority link as a question; no flattery, "I noticed", hype or exclamation marks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- Fact check before copy: tag each fact used Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting. Keep single-source numbers and disputed names or dates out of the copy; if a message still leans on one, put "Check before sending: [fact], [why]" directly above it.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first. For each of [Accounts] (up to 10), pick the 60-day signal most relevant to [What I sell] and my [Territory], fact-check it, and write a 45-word [Persona] opener ending in one ask.
```

### Follow-ups

- Write a second-touch email for each account using a different priority.
- Rewrite the openers for a CIO instead of [Persona].
- Run the next 10 accounts in the same way.
- For the rows marked Single source, find a second source or swap in another signal.

### Tips

- Give the assistant a real proof point you're allowed to quote. A specific, permitted result often beats a generic value statement.
- Add your territory once in the start-here prompt; signals in your region rank first and the table says when an account has none.
- If most accounts come back with no qualifying signal, widen the window to 90 days in a follow-up.

## Are they hiring more than usual?

- **id:** `signals-hiring-spike`
- **What you get:** A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.
- **Use it when:** Timing outreach, or checking a hunch that an account is gearing up (or slowing down).
- **Best for:** SDR / BDR, Account Executive, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. data and AI staff augmentation); Workload (optional) (e.g. Artificial Intelligence & Data Science)

### Detailed prompt

```text
Act as my hiring-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. data and AI staff augmentation — skip if you ran the start-here prompt]
- Workload (optional): [a type of work, e.g. Artificial Intelligence & Data Science; blank uses the function closest to what I sell]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull monthly job postings for the last 12 months, company-wide and for the function closest to [What I sell] (or [Workload]); full months only, and say which months you used.
3. Work out the monthly average and standard deviation, and the last 5 full months against the 5 before.
4. Verdict on the last 3 full months (editable defaults): Spiking = any month over 2 standard deviations above average; Above normal = their average over 1 above; Slowing = over 1 below; Normal = anything else.
5. Label a flagged month seasonal if it's an industry peak (e.g. retail holidays), or company-wide if many unrelated workloads rose together.
6. For each flagged month, list the top 5 workloads against their usual month.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: one plain-English line (e.g. "Above normal in IT, not seasonal") with the 5-vs-5 change in %, for the function and company-wide.
- Table (last 6 full months, function view): Month | Postings | Gap from average (standard deviations) | Flag.
- Table "What drove it" (top 5): Workload | Postings in flagged month | Usual month | Likely owner.
- Detail: the full 12-month series; the company-wide view; "Why this matters for [What I sell]" (2–3 bullets); Gaps (what Draup lacked, to ask in discovery).

RULES
- Standard deviations go in the table; the verdict uses plain words.
- State the exact window, e.g. "Dec 2025 – Oct 2026".
- A seasonal frontline spike is rarely a buying signal; say so when it's the driver.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). Is [Company] hiring more than usual in the function closest to [What I sell]? Last 5 full months vs the 5 before, flagged months, drivers, and whether it's seasonal.
```

### Follow-ups

- Show 3 recent postings from the flagged month in [Workload], with title, location and date.
- Which cities did the extra postings come from?
- Is this backed by a stated priority? Check their priorities in the same workloads.
- Write a 70-word email to the person in the next step about the capability being built, with no posting counts.

### Tips

- The function view is the one that matters: store or warehouse hiring can swamp a retailer's company-wide total.
- Slowing is a signal too: it can mean a freeze, a reorganisation or a shift to outsourcing worth asking about.

## Are they really investing in X?

- **id:** `signals-investing-in-x`
- **What you get:** A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.
- **Use it when:** Before you claim an account is "investing in GenAI" (or SAP, or cloud) in a pitch or email.
- **Best for:** Account Executive, Presales & Solutions, SDR / BDR
- **Time:** 2–4 min
- **Inputs:** Company (e.g. jpmorganchase.com); Technology (e.g. generative AI for software development); What I sell (e.g. AI developer-productivity platform)

### Detailed prompt

```text
Act as my investment-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Technology: [theme in plain words, e.g. generative AI for software development]
- What I sell: [one line, e.g. AI developer-productivity platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the skills and workloads in the company's job postings over the last 12 months, trending up first, and pick those related to my theme using Draup's exact names. Broad labels ("Generative AI") may match nothing; specific ones ("AI-Assisted Development") usually do.
3. For each: 12-month postings and average per month in the last 5 full months against the 5 before. Flag one-off spikes (one month over half the total). Read declining skills' monthly numbers before trusting the label.
4. Pull 3 recent postings for the strongest skill: title, date, location, key responsibilities.
5. Pull the headcount trend for the matching job family (e.g. software developers): a year before the latest month against the latest month.
6. Pull stated priorities that mention the theme, with source and fiscal quarter.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Start with the verdict: Yes (rising hiring, growing headcount and a stated priority), Early (rising hiring only) or No.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 8): Skill | 12-month postings | Avg/month, prior 5 | Avg/month, last 5 | Note.
- "Talking points": 3, each with a number and its date.
- Detail: proof postings (Title | Date | Location | What the role does); headcount (job family, then and now, % change, months covered); stated priorities (name, source, quarter, likely owner); Gaps (what Draup lacked, to ask in discovery).

RULES
- "Rising" = the last 5 full months beat the 5 before by more than 20% (editable default).
- Salaries are often missing from postings; don't estimate them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Talent-flow data ends about 3 months ago; state the months covered.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line (Yes, Early or No) and next step first, with a named owner. Is [Company] really investing in [Technology]? Related job-ad skills, last 5 full months vs the 5 before, 3 proof postings, headcount trend and stated priorities.
```

### Follow-ups

- Which tools did they start hiring for from near zero this year?
- Who leads this area? Find executives tagged to the matching workload.
- Turn the talking points into a 3-sentence opener for the person in the next step.
- Compare the same theme at [a peer] so I can say whether they're ahead or behind.

### Tips

- Use Draup's own skill names. The assistant reads them off the trending list first, so broad labels don't come back empty.
- Early is often a good verdict for a seller: hiring is rising but the work isn't fully staffed yet.

## Which tools their job ads are building

- **id:** `signals-practice-shift`
- **What you get:** The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press, with a named person to call.
- **Use it when:** Validating a technology priority, or looking for an early, non-obvious why-now in engineering, data and AI.
- **Best for:** Account Executive, Presales & Solutions, SDR / BDR, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. servicenow.com); What I sell (e.g. AI code-review and governance tooling); Business function (optional) (e.g. IT)

### Detailed prompt

```text
Act as my hiring and stack-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. servicenow.com]
- What I sell: [one line, e.g. AI code-review and governance tooling — skip if you ran the start-here prompt]
- Business function (optional): [e.g. IT or ER&D (engineering and R&D); blank uses the function closest to what I sell]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the skills in the company's job postings over the last 12 months in the function: the top 50 plus those trending up. Keep named software tools only.
3. For each tool, compare average postings per month in the last 5 full months with the 5 before. Set aside one-off spikes (one month over half the total).
4. Pull the installed stack for the makers of the top 15 tools: usage strength, last seen, and whether first detected in the last 12 months. For very broad makers (Google, Microsoft, Amazon), also narrow by category. Say which tools you couldn't find.
5. Group each tool (editable defaults): New = 5 or fewer a month before, 20+ (or 5x) after; Building = rising in job ads but Low, absent or new in the stack; Core = in job ads and High or Medium in the stack; Coasting = High in the stack, under 5 postings in 12 months.
6. For the top 3 New or Building tools, pull 2 recent postings each: title, date, location.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10, by recent volume): Tool | Avg/month, prior 5 | Avg/month, last 5 | In stack (strength) | Group.
- "What it signals": 3 bullets on the practice change, and the opening for [What I sell] with its likely owner.
- Detail: makers, first-detected flags and sample titles; rows 11–20; Gaps (what Draup lacked, to ask in discovery).

RULES
- Job-ad mentions measure hiring demand, not licences or spend; say so once.
- If nothing is New, say so and lead with Building.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Trust last-seen date and usage strength. Ignore the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). Which software tools appear in [Company]'s job ads this year, and how do they match its stack? Sort into New, Building, Core and Coasting.
```

### Follow-ups

- Show 3 full job descriptions for the top New tool so I can quote the responsibilities.
- Has anyone senior been hired into this area recently? Check executive moves in the matching workload.
- Write a 70-word email to the person in the next step that opens on this practice shift.
- Which of these tools are made by my competitors?

### Tips

- A tool that shows up in job ads before it shows up in the stack is often a project in its first months: a good time to engage.
- Big employers' company-wide results can be swamped by frontline hiring, so the prompt reads the function closest to what you sell unless you name another.

## Priorities with no hiring behind them

- **id:** `signals-priorities-vs-hiring`
- **What you get:** Which stated priorities in your function have hiring behind them and which don't: the gaps where the account may need to buy rather than build, with a named person to call.
- **Use it when:** Shaping a services or software pitch, or deciding which priority to lead with.
- **Best for:** Account Executive, Services, SI & Staffing Seller, Presales & Solutions
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. intelligent automation and RPA services); Business function (optional) (e.g. Supply Chain)

### Detailed prompt

```text
Act as my account strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. intelligent automation and RPA services — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Supply Chain, IT; blank uses the function closest to what I sell]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the workloads in the stated priorities for the function, ranked by how many priorities involve each. Keep the top 15. If the function has none, say so and don't borrow from others.
3. Pull hiring by workload for the last 12 months, up to 5 pages: postings and trend. Set frontline workloads (store operations, food and beverage, warehousing) aside unless they relate to what I sell.
4. Match each priority workload to its hiring; where names differ, use the closest and say so.
5. Mark each (editable defaults): Backed = top 20 hiring workload or trending up; Partial = 50+ postings but not Backed; Thin = under 50; Silent = none; Not comparable = strategy or governance work that rarely appears in job ads.
6. For the 3 biggest gaps (most priorities, least hiring), pull the priority names with source and fiscal quarter.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- "Build-or-buy gaps" (top 3): priority, source and quarter, hiring numbers, and why [What I sell] could fill it.
- Table (top 10): Workload | Priorities involving it | Postings (12 months) | Trend | Read.
- Detail: the remaining workloads; "Already backed" (2–3 workloads they're building in-house, with likely owners); Gaps (what Draup lacked, to ask in discovery).

RULES
- Little hiring doesn't prove they will buy; they may already outsource the work. Say so, and suggest checking their outsourcing for those workloads.
- State the hiring window.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). Compare [Company]'s priority workloads in my function with 12 months of hiring; mark each Backed, Partial, Thin or Silent, and name the 3 biggest build-or-buy gaps for [What I sell].
```

### Follow-ups

- For the top gap, which service providers already work that workload at [Company]?
- Who owns the top gap? List executives tagged to that workload.
- Write a one-paragraph point of view on the top gap for the person in the next step.
- Run the same check for [another function].

### Tips

- Silent or Thin workloads with several priorities are worth testing as buy signals, after you check who already does the work for them.
- Backed workloads still matter. They show where the account has in-house teams you'd work alongside.

## Who in my market just [did X]?

- **id:** `signals-news-question-templates`
- **What you get:** A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.
- **Use it when:** Building a themed list, prepping an industry call, or finding companies that just changed.
- **Best for:** SDR / BDR, Marketing & ABM, Account Executive, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Event type (e.g. expansion or new centres); Vertical (e.g. Banking & Financial Services); Country (e.g. India); What I sell (e.g. cloud migration services); Window (optional) (e.g. 6 months (default 90 days)); Theme (optional) (e.g. cloud migration (partnerships only))

### Detailed prompt

```text
Act as my market-news researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Event type: [one of M&A; layoffs; leadership change; expansion or new centres; funding; partnership — e.g. expansion or new centres]
- Vertical: [industry, e.g. Banking & Financial Services]
- Country: [in full, e.g. India]
- What I sell: [one line, e.g. cloud migration services — skip if you ran the start-here prompt]
- Window (optional): [default 90 days; up to 12 months]
- Theme (optional): [for partnerships, e.g. cloud migration]

STEPS
1. Use Draup's exact industry and country names; say which you used.
2. Search Draup news first with "Which [Vertical] companies in [Country] [Event type] in the last [Window]?" (main source; up to 20 results, often without links). Then page the news feed for the same filters to add links and catch misses. Review at least 30 items in total.
3. Apply the noise rule. Keep only items where the named company is the actor, the event happened in [Country], and the company really is in [Vertical].
4. By type: M&A: Acquisition, Merger or Divestiture, and Announced or Completed. Layoffs: store and branch closures listed separately; headcount only if stated. Leadership: C-level and VP, at the new employer. Expansion: add Type (capability centre, tech centre, office); leave out factories, stores, branches and wealth centres. Funding: no donations or grants. Partnerships: no sponsorships or marketing tie-ins.
5. Merge repeat coverage, keeping the earliest date and counting sources.
6. For the most relevant company, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10, newest first): Date | Company | What happened (with any number) | Sources (count).
- "Pattern": 3 bullets, and why it matters for [What I sell]; name the 3 companies to approach first.
- Detail: rows 11–20; source and headline (link if available) and type for every row; "Excluded" count by reason; Gaps (what Draup lacked, to ask in discovery).

RULES
- Search results come back by relevance, not date; sort by date yourself.
- One event type per run.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Hiring, new-technology and news data cover the last 12 months; if my window is longer, say what was covered.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 420 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (a named person, a dated why-now). Which [Vertical] companies in [Country] did [Event type] in the last [Window]? Top 10: date, company, what happened and how many sources report it.
```

### Follow-ups

- For the top 5 companies, pull a one-line profile: workforce, revenue and HQ.
- Run the same event type for [another country].
- Write a 2-sentence opener for each of the top 5, using only items with 2+ sources.
- Which of these companies already run my competitors' products?

### Tips

- The news search finds more but often without links; the feed adds links. The assistant uses both and gives source and headline either way.
- Phrase the theme the way a press release would ("core banking", "cloud migration").
- A single-source item is worth a look but not a quote; the Sources column shows which ones to double-check.

## Who just picked a vendor

- **id:** `signals-vendor-selection-news`
- **What you get:** A dated list of companies in your industry that just selected, deployed or replaced a vendor in your category: competitor wins to watch, peer proof, and the implementation partners involved, with a named person at the best account.
- **Use it when:** Weekly or monthly competitive watch, or before a campaign in a new industry.
- **Best for:** Account Executive, Marketing & ABM, Partnerships & Alliances, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Technology (e.g. demand forecasting software); Vertical (e.g. Retail); Competitor (e.g. RELEX, Blue Yonder); What I sell (e.g. supply-chain planning software); My company (optional) (e.g. Northwind Data Services; Tailspin Partners); Window (optional) (e.g. 90 days (default))

### Detailed prompt

```text
Act as my competitive-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Technology: [your category in plain words, e.g. demand forecasting software]
- Vertical: [industry, e.g. Retail, Insurance]
- Competitor: [one or more rival vendors, e.g. RELEX, Blue Yonder]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- My company (optional): [our firm and partners, e.g. Northwind Data Services; Tailspin Partners]
- Window (optional): [default 90 days; up to 12 months]

STEPS
1. Turn my industry into Draup's exact name; say which you used.
2. Search Draup news for the window with 3 phrasings: "[Vertical] company selects or partners with a [Technology] vendor", "... deploys, goes live on or migrates to new [Technology]" and "... replaces its legacy [Technology] system", then one search per competitor. Add links from the news feed where you can. Review at least 30 items.
3. Keep only stories where a named buyer chose a named vendor: buyer, vendor, implementation partner, scope (sites, regions, modules), what it replaced, and stage (Selected, Implementing, Live, Expanded).
4. Drop vendor roundups, rankings, "editorial picks", product launches and single stores named as the buyer. Merge repeat coverage and count sources; a win reported only by the vendor's own release is single-source.
5. Look up the 10 most relevant buyers in one company-list lookup for HQ and workforce; mark the rest "not checked".
6. For the best buyer to approach, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10, newest first): Date | Buyer (HQ) | Vendor | Stage | Sources (count).
- "Competitor wins": with later phases still open.
- Detail: implementation partner, scope and what it replaced per row; "Peer proof" (rows where [My company] or a partner won, or "none found"); "Implementation partners seen" (Partner | Wins | Vendors); source and headline per row; Gaps (what Draup lacked, to ask in discovery).

RULES
- A selection isn't a go-live; always show the stage.
- Search results come back by relevance, not date; sort by date yourself.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Hiring, new-technology and news data cover the last 12 months; if my window is longer, say what was covered.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 420 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (a named person, a dated why-now). Which [Vertical] companies selected, deployed or replaced a [Technology] vendor in [Window]? Top 10 with buyer, vendor, stage and source count; flag [Competitor] wins.
```

### Follow-ups

- For each competitor win, which phases or regions are still open?
- Which implementation partner appears most often? Profile them as a co-sell target.
- Write a 3-sentence peer-proof email using our most recent win for 5 lookalike accounts.
- Check the stack at the top 3 competitor wins: is the product already showing as active?

### Tips

- Phrase your category the way a press release would ("demand forecasting", "replenishment", "core banking"). Search works on meaning, not exact words.
- Multi-year rollouts often start with one module. A competitor win today can still leave later modules open.

## What changed since [Date]

- **id:** `signals-change-log`
- **What you get:** A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.
- **Use it when:** Revisiting a closed-lost deal, prepping a renewal or QBR, or picking up an account from a colleague.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. walmart.com); Date (e.g. 2026-03-01); Relationship (e.g. current customer (or lost deal)); What I sell (e.g. supply-chain planning software); Business function (optional) (e.g. Supply Chain)

### Detailed prompt

```text
Act as my account-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. walmart.com]
- Date: [e.g. 2026-03-01: when we lost the deal or held the last QBR]
- Relationship: [current customer or lost deal]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Supply Chain, IT; blank uses the function closest to what I sell]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Priorities: stated priorities in the function sourced after [Date], with fiscal quarter and workloads.
3. Leadership: hires, exits and promotions since [Date], one workload at a time, with full titles, rows checked and latest move date; then the top 3 executives in the function now.
4. Technology: products first detected since [Date] in the function, and any competitor product anywhere in the stack; rate each (see rules).
5. Hiring: average monthly postings in the function before vs after [Date], full months only.
6. News since [Date]: executive moves, M&A, partnerships, expansion, layoffs, investment plans, and incidents that bear on what I sell.
7. Financials: any new fiscal year's revenue growth; check for a divestment before calling a drop a cut.

OUTPUT
- Bottom line: 2 sentences, starting with the call (lost deal: reopen, wait or watch; current customer: defend, expand or monitor) and the top change.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table "Change log" (highest impact first, at most 10 rows, then offer more): Date | Type | What changed | Impact | Likely owner.
- Detail: sources; competitor ratings; hiring before and after; Gaps (what Draup lacked, to ask in discovery).

RULES
- Technology, hiring and news reach back 12 months; if [Date] is older, say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Leadership data shows about the 10 latest moves per type and can lag about 3 months. Keep only rows where [Company] is the current employer (for exits, the previous one).
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Rating: an installed competitor product with High usage in the workloads of What I sell is Red, Medium is Amber, else Green. Newly detected (first seen within 12 months) is a separate Amber signal.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line first (customer: defend, expand or monitor; lost deal: reopen, wait or watch) and next step with a named person. Then up to 10 dated changes at [Company] since [Date] that matter for [What I sell].
```

### Follow-ups

- Draft a re-engagement email to the new leader in the function, tied to the top change.
- Has any competitor product been first detected since [Date]? Show usage strength and countries.
- Turn this into a 5-bullet update for my manager.
- Compare this with the risk check for the same account.

### Tips

- For a closed-lost revisit, use the date you lost. For renewals, use the date of the last QBR.
- A competitor tool rated Red in your workloads is the first thing to raise at a renewal; Amber means ask about it in discovery.
- Leadership data can lag about 3 months; the latest move date tells you how fresh it is.

## Weekly trigger sweep for my book

- **id:** `signals-weekly-book-sweep`
- **What you get:** One phone-sized table of the week's real triggers across up to 10 accounts, including any CEO or leadership change that takes effect in the window, plus the nearest item just outside the window for every quiet account.
- **Use it when:** Monday morning, or before a pipeline review. Use this for your whole book; use "What's worth acting on now" to go deep on one account.
- **Best for:** Account Executive, Account & Customer Success Manager, SDR / BDR
- **Time:** 4–6 min
- **Inputs:** Accounts (e.g. walmart.com, target.com, bmw.com, pfizer.com); What I sell (e.g. supply-chain planning software); Window (optional) (e.g. last 7 days (default; up to 30))

### Detailed prompt

```text
Act as my weekly account-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [up to 10 websites, e.g. walmart.com, target.com, bmw.com — or "my saved list"]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Window (optional): [default last 7 days; up to 30 days]

STEPS
1. Reuse the Draup names saved in my setup. Resolve others by website (exact match, parent company); ask only if none or several match. If I gave more than 10, do the first 10 and offer to continue.
2. Pull news for all accounts in one feed pull for the window: executive moves (CEO and other C-level changes first), M&A, layoffs, partnerships and vendor deals, expansion, funding and investment, plus incidents or regulatory items that bear on what I sell. If one account fills more than half the results, pull the other accounts separately.
3. Apply the noise rule; also drop court dockets, stock-analysis pieces and store-property sales tagged as M&A.
4. After step 3, for every account with nothing left, check its top-ranked signals and keep items whose event or effective date falls inside the window, even if the story was captured before or after it (e.g. a new CEO who takes over on a date inside the window).
5. Leadership check: before calling any account quiet, confirm steps 2–4 found no CEO or other C-level change announced or effective in the window.
6. Label subsidiary news "[Subsidiary] ([Account])". Merge repeat coverage and count sources.
7. Write one "so what" per item for [What I sell] and tag it Act now (this week), Plan (next touch) or Watch.
8. For the top Act-now account, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (Act now first, then newest; up to 10): Account | Date | Trigger (with any number) | So what | Action.
- "Just outside the window": for each quiet account, the nearest material item (date, one line), or "nothing in 90 days".
- "No material signals" and "Not resolved": account names only.
- Detail: source and headline, type, source count and likely owner per item; "Dropped" count by reason; Gaps (what Draup lacked, to ask in discovery).

RULES
- Every item needs an event or effective date inside the window; drop anything you can't date.
- Don't pull leadership-move histories for every account; if I ask about one, narrow to the workloads I name.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named person, dated why-now). For [Accounts], list [Window]'s real triggers, including leadership changes effective in the window, each with a so-what for [What I sell]; give quiet accounts their nearest item outside it.
```

### Follow-ups

- Write a short email for each Act now item, with a fact check on each.
- For [Account], show leadership moves in [workload] in the last 30 days.
- Run the same sweep for the last 14 days and compare it with this week.
- Turn the "Just outside the window" items into priority-led touches for the quiet accounts.

### Tips

- Save your account list in a Claude Project or the start-here prompt so you can rerun this every Monday with one line.
- Use a 14-day window after a holiday week; the "Just outside the window" line still shows what you'd otherwise miss.
- One big name can flood a shared news pull; the prompt re-pulls the quiet accounts so they aren't missed.

## Weekly industry signal digest

- **id:** `signals-vertical-digest`
- **What you get:** A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.
- **Use it when:** A weekly routine for vertical sellers and marketers, or before an industry call or event.
- **Best for:** Marketing & ABM, Account Executive, Sales Leader & RevOps, SDR / BDR
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Insurance); What I sell (e.g. claims automation software); Country (optional) (e.g. United Kingdom); Window (optional) (e.g. last 7 days (default; up to 30))

### Detailed prompt

```text
Act as my industry news editor. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [industry, e.g. Insurance, Life Sciences]
- What I sell: [one line, e.g. claims automation software — skip if you ran the start-here prompt]
- Country (optional): [in full, e.g. United Kingdom]
- Window (optional): [default last 7 days; up to 30 days]

STEPS
1. Use Draup's exact industry and country names. If the industry returns nothing, try its parent and name it.
2. Pull the most-covered industry news in the window: M&A, executive moves, partnerships, expansion, layoffs, funding, plus incidents or regulatory actions that bear on what I sell. Review at least 30 items.
3. Check each company really belongs to the industry; tags can leak to similar names or unrelated events.
4. Apply the noise rule; also drop board-nominee filings and minor marketing deals. The named company must be the actor, and if I gave a country, the event must happen there.
5. Keep regional-unit news (e.g. a country CEO change at a global insurer) but name the unit. Merge repeat coverage and count sources.
6. Rank by relevance to [What I sell], then company size; keep the top 10. For the top 3 companies, attach one fitting stated priority with fiscal quarter.
7. For the best account to touch, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (up to 10): Date | Company (unit) | What happened (with any number) | Why it matters for [What I sell] | Sources (count).
- "Accounts to touch": 3–5, each with reason, linked priority and likely owner.
- Detail: "Themes" (2–3 patterns citing the rows behind each); region, type and source and headline per row; "Dropped" count by reason; Gaps (what Draup lacked, to ask in discovery).

RULES
- Keep amounts in the reported currency; convert to USD in brackets only if I ask, using Draup's rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 420 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (a named person, a dated why-now). This week's [Vertical] digest: the 10 most material moves with date, source count and why each matters for [What I sell], plus 3–5 accounts to touch.
```

### Follow-ups

- Turn this digest into a 150-word LinkedIn post for our industry page, using only items with 2+ sources. Check your Draup licence before publishing Draup data externally.
- For the accounts to touch, write a 2-sentence opener each.
- Run the same digest for the last 30 days and show which themes are growing.
- Which of this week's companies run my competitors' products?

### Tips

- Industry tags can catch companies with similar names. The "Dropped" count shows how much the assistant filtered out.
- Run it every Monday with the same inputs so you can compare themes week to week.
