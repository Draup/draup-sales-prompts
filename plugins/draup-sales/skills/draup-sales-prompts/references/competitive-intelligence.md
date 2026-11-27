# Competitive intelligence

Track what rivals are winning, building and losing, and where you can take share.

## What a rival did this quarter

- **id:** `compete-recent-moves`
- **What you get:** The few moves a competitor made in the last 90 days that change your deals (customer wins, partnerships, launches, deals and leadership), the accounts to defend or attack, and the named person to call at the top one.
- **Use it when:** Before a pipeline review or competitive deal, or when the field asks "what is [Competitor] up to?" Use this for one rival; use "Quarterly competitor watch for the team" for up to 3 side by side, or "How a rival's strategy is shifting" after an earnings call.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps, Marketing & ABM, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Competitor (e.g. adobe.com); What I sell (e.g. digital experience platform); Territory (e.g. North America (optional)); Our customers (e.g. Contoso Retail, Fabrikam Foods (optional)); Our differentiators (e.g. open architecture, faster time to value (optional))

### Detailed prompt

```text
Act as my competitive-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. adobe.com]
- What I sell: [one line, e.g. digital experience platform — skip if you ran the start-here prompt]
- Territory (optional): [e.g. North America; default: my territory from setup]
- Our customers (optional): [names or a saved Draup list, e.g. Contoso Retail, Fabrikam Foods]
- Our differentiators (optional): [e.g. open architecture, faster time to value]

CONTEXT (why this matters)
What matters: named customer wins, bundling partnerships, gap-closing launches, leaders leaving.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Search news for [Competitor], last 90 days (20+ items): wins, partnerships, launches, deals, investments, leadership, layoffs.
3. Pull the feed for the same window, limited to [Competitor] (15 items), to catch misses.
4. Pull 12-month acquisitions and reconcile each with the news (date, target, price).
5. Classify each item: Customer win (a named company adopting or expanding [Competitor]), Partnership, Product launch, M&A or investment, Leadership or layoff, Expansion. Merge repeats; prefer [Territory].
6. Write three signals on where [Competitor] is pushing next, each with two dated items.
7. Pick the account to watch: one of [Our customers] named in a move, or else running [Competitor] at High or Medium (check up to 3 stacks; maker as Draup spells it, e.g. Salesforce.com): Defend. Otherwise the newest Customer win in [Territory]: Attack later. Confirm it's the right company and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the move that matters most and what it means for me.
- Recommended next step: a named person (name, full title) at the top account, the action this week and the dated why-now (or say none).
- Table "Moves that matter" (up to 8, newest first): Date | Type | What happened | Named company | Source.
- Table "Accounts to watch" (up to 8): Company | Move | Defend, Avoid for now or Attack later | Why (likely).
- "Three signals": Signal, dated evidence, what it means for me.
- "Counter-message": 3 bullets, tied to [Our differentiators] if given (60 words max).
- Detail: the rest of the log (up to 15) and the acquisitions check.
- Gaps: what Draup lacked; ask in discovery.

RULES
- A partner release that only mentions [Competitor] is a Partnership; a marketplace listing is not a win.
- Keep only items whose event date falls in the window.
- A rival's outage, breach, price rise or layoff is a counter-message trigger for me; keep it. Never pick an "Avoid for now" account for the next step.
- If the acquisitions table and news disagree, show both; a price from news alone is single-source.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
What did [Competitor] do in the last 90 days that matters to [What I sell]? Lead with the bottom line and a named person at the top account to defend, then dated moves, accounts to watch and a counter-message.
```

### Follow-ups

- Turn the counter-message into a 120-word email to the named executive at the top Defend account.
- For [Named company], check whether [Competitor] products show up in their tech stack and how strong they are.
- Run the same log for my second competitor and compare the two.

### Tips

- Run it monthly for your top two rivals; Accounts to watch is usually the most useful output.
- Partner announcements tell you which services firms are now steering deals toward the rival.
- Add your territory and Our customers: Defend then means your own accounts, and the next step lands in your patch.

## What a rival is building next

- **id:** `compete-hiring-signals`
- **What you get:** What a competitor is likely building or selling next, read from its own job ads (rising workloads, skills and new roles in the last 5 months), with proof postings, a talk track and the named person to brief.
- **Use it when:** Before a roadmap or positioning review, or when you suspect a rival is entering your space.
- **Best for:** Presales & Solutions, Sales Leader & RevOps, Marketing & ABM, Partnerships & Alliances, Account Executive
- **Time:** 4–6 min
- **Inputs:** Competitor (e.g. databricks.com); What I sell (e.g. AI agents for sales teams); Focus area (e.g. Artificial Intelligence & Data Science (optional)); Account to defend or win (e.g. visa.com (optional))

### Detailed prompt

```text
Act as my competitive-intelligence analyst who reads job ads for strategy. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. databricks.com]
- What I sell: [one line, e.g. AI agents for sales teams — skip if you ran the start-here prompt]
- Focus area (optional): [a workload, i.e. a type of work, e.g. Artificial Intelligence & Data Science]
- Account to defend or win (optional): [website of a live deal or key customer, e.g. visa.com]

CONTEXT (why this matters)
Companies hire 6–12 months ahead of launches; the signal is change, not volume.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull hiring by workload (12 months, global, top 15) with monthly trends. Compare the last 5 full months with the 5 before: Rising (+25% or more, editable default), Steady or Falling. Draw no conclusions from catch-all workloads (Account Management, Project/Programs Management).
3. Pull the top 20 skills within [Focus area], or else the workloads closest to [What I sell], with trends; flag Rising skills.
4. Pull job titles trending up (12 months); if fewer than 3, use the rising workloads.
5. For the 2 most surprising rising skills or titles, pull 4 recent postings each and read the responsibilities. Drop a skill as an artefact if it appears in unrelated roles (HR, finance) or rises in lockstep with an unrelated skill.
6. Turn what survives into build signals: the offer or segment the hiring points to.
7. Dated trigger: [Competitor]'s most important news item from the last 90 days that bears on the build signals.
8. If I gave [Account to defend or win], find it by website and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — what they're likely building and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at [Account to defend or win], the action this week, and [Competitor]'s dated move as the why-now; with no account given, name the role to brief.
- Table "Build signals" (up to 3): Likely building or selling | Evidence | Threat or opening | Likely timing.
- Table "Where hiring is moving" (top 10): Workload | Postings (12 mo) | Last 5 vs prior 5 | Read.
- "Talk track": 2 bullets for my team (50 words max).
- Detail: rising skills and titles (kept or dropped as artefact) and proof postings (Date | Title | Location | quote).
- Gaps: what Draup lacked; ask in discovery.

RULES
- A signal needs two kinds of evidence (e.g. a rising skill plus a posting naming the offer); otherwise label it "weak".
- Never infer revenue or customers from postings.
- Under 300 postings in 12 months is a small sample; keep conclusions tentative.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

### Quick version

```text
What is [Competitor] building next, judged from its job ads? Lead with the bottom line and who to brief, then rising workloads and roles (last 5 full months vs prior 5), proof postings and up to 3 build signals.
```

### Follow-ups

- Show where those rising roles are based: which metros and countries.
- Compare this with what [Competitor] said on its latest earnings call.
- Write a one-page internal brief for product marketing on the top build signal.

### Tips

- New job titles (e.g. forward-deployed roles for a new segment) are usually stronger signals than skill counts.
- Read 3–4 actual postings before acting on any skill spike.
- Add a live deal as the account and the next step names the person to brief there.

## Where a rival's people are going

- **id:** `compete-talent-drain`
- **What you get:** Who a competitor loses people to and hires from, its workforce trend, the clients absorbing its staff (a sign of insourcing or delivery strain) and the named person to talk to at the most exposed client.
- **Use it when:** Before a displacement pitch, or when a rival's delivery quality or stability is your angle.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Sales Leader & RevOps, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Competitor (e.g. cognizant.com); What I sell (e.g. application modernisation and managed services); Region (e.g. United States (optional))

### Detailed prompt

```text
Act as my competitive-intelligence analyst for workforce signals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. cognizant.com]
- What I sell: [one line, e.g. application modernisation and managed services — skip if you ran the start-here prompt]
- Region (optional): [country or metro, e.g. United States]

CONTEXT (why this matters)
A rival losing people faster than it hires, or to its clients, is under delivery pressure.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull talent flow by company, by people lost, 25 rows ([Region] if given). Remove its subsidiaries, "Self Employed" and blanks.
3. If the region result looks almost the same as global, say the region may not have applied and show global; if its top row is under 25 people, say the region is too thin and show global.
4. Split rows into Rival vendors (services firms, software vendors, consultancies) and End clients (companies that buy from [Competitor]). Net flow = hired from minus lost to.
5. Pull the monthly workforce trend (hires, exits, net, total) for the same window.
6. Search news for [Competitor] leadership moves and layoffs (6 months); mark the most important from the last 90 days.
7. For the top end client absorbing staff (or else the top end client in the list), find it by name and pull its top 3 executives in the function closest to [What I sell] (one page of 10) and its most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the pressure on [Competitor] and what it means for [What I sell]. Add the window: "Talent flow for [months], [region or global]".
- Recommended next step: a named person (name, full title) at the most exposed end client, the action this week and the dated why-now (or say none).
- Table "Loses people to" (top 10): Company | Type (rival vendor, end client) | Lost | Hired from | Net.
- Table "Monthly trend" (last 6 full months): Month | Hires | Exits | Net; then one line on direction.
- "Clients absorbing their staff": end clients with 50+ people lost to and few hired back (editable default), each with a likely read (insourcing, rebadging, new captive).
- "Leadership changes" (6 months, up to 5) and "How to use this": 3 bullets.
- Detail: net winners against them (top 3) and the full monthly trend with workforce.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Counts are people moves Draup observed in the window, not total headcount or attrition rates.
- Never tell a client that [Competitor] is losing staff on their account; use it to shape questions. Label inferences "likely".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Talent flow ends about 3 months ago and the last month undercounts exits; state the months.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
Where are [Competitor]'s people going? Lead with the bottom line and a named person at the client most likely absorbing its staff, then who it loses talent to and hires from, and monthly hires vs exits.
```

### Follow-ups

- For [End client], show its outsourcing providers and [Competitor]'s engagements there.
- Which job families is [Competitor] losing most in [Region]?
- Write 3 discovery questions on delivery continuity I can ask the named executive.

### Tips

- End clients high in the lose-to list are often your best displacement targets.
- Pair this with "A rival's footprint and your wedge" for the client it flags.

## Rival head-to-head in one industry

- **id:** `compete-vertical-head-to-head`
- **What you get:** Two services firms compared in one industry and country by active engagements, shared and exclusive customers and workload mix, with the shared accounts to attack, the workloads where you lead and a named person at the top target.
- **Use it when:** Planning an industry campaign against a rival services firm, or deciding where your firm should focus versus a competitor.
- **Best for:** Services, SI & Staffing Seller, Sales Leader & RevOps, Account Executive, Partnerships & Alliances, Marketing & ABM
- **Time:** 2–4 min
- **Inputs:** Our firm (e.g. Wipro (or "not in Draup")); Competitor (e.g. Cognizant); Industry (e.g. Banking & Financial Services); Country (e.g. United States of America (default: my territory)); Our accounts and strengths (e.g. paste accounts and workloads we lead in (optional)); What I sell (e.g. data engineering and cloud managed services)

### Detailed prompt

```text
Act as my services competitive strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Our firm: [Draup name, e.g. Wipro; or "not in Draup: Infosys" to compare two rivals]
- Competitor: [services firm, e.g. Cognizant]
- Industry: [e.g. Banking & Financial Services]
- Country: [customer HQ country in full, e.g. United States of America; default: my territory]
- Our accounts and strengths (optional): [if our firm isn't in Draup: accounts and workloads we lead in]
- What I sell: [one line, e.g. data engineering and cloud managed services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Buyers already compare both firms at shared accounts.

STEPS
1. Confirm Draup's names for both firms, industry and country.
2. Pull the provider ranking for [Industry] customers headquartered in [Country] (primary industry): both firms' engagements and rank, plus the top 10. Drop agencies, staffing and real-estate firms.
3. Pull each firm's top 20 customers (same industry and country) and match by exact name: Shared, Ours only, Theirs only; note each shared account's leader and gap. Pasted Our accounts are our side; if Our firm is "not in Draup" and I pasted none, compare the two named rivals. Merge subsidiaries into parents.
4. Pull each firm's top 12 workloads, same industry and country, with each one's share of the firm's total; mark mine.
5. For the top attack account, find it by website (else by name, showing match and score), pull its top 3 executives in the function closest to [What I sell] (one page of 10) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — "[Our firm]: N engagements (#rank); [Competitor]: N (#rank)" and what it means for me.
- Recommended next step: a named person (name, full title) at the top attack account, the action this week and the dated why-now (or say none).
- Table "Where to attack" (5): Customer | Ours | Theirs | Workload to lead with: shared accounts where [Competitor] leads by 3x or less (editable default).
- Table "Workload mix" (top 10): Workload | Ours (share) | Theirs (share) | Edge (none on catch-alls).
- "Where we lead": up to 3 workloads where our share is 5+ points higher (editable default), mine first; say if none.
- Our firm not in Draup: label columns by firm name, never "Ours"; retitle "Where to attack" "Where a challenger fits" (shared accounts where the two are close, plus thin workloads); "Where we lead" only from my pasted accounts and strengths, else skip.
- Detail: top 10 providers, shared accounts with gaps, 5 fortresses each side.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Every count uses both industry and country.
- Leave misclassified customers and either firm's subsidiaries out of Where to attack; under 5 customers for a firm? Widen to the region.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

### Quick version

```text
Compare [Our firm] and [Competitor] in [Industry], [Country]. Lead with who's ahead and a named person at the top shared account to attack. Then 5 attack accounts, workload mix and where we lead, all on active engagements.
```

### Follow-ups

- For [Shared account], show both firms' engagements by workload.
- Which executives at the top 3 attack accounts own [Workload]?
- Turn Where we lead into a one-page industry point of view.

### Tips

- Shared accounts where the rival leads narrowly are usually the fastest share-of-wallet wins.
- If your firm isn't in Draup, write "not in Draup" and paste your accounts and strengths; the answer compares the two rivals and shows where a challenger fits.

## How a rival's strategy is shifting

- **id:** `compete-strategy-shift`
- **What you get:** How a competitor's stated priorities moved across its last three earnings calls, the acquisitions, leaders and cuts behind each shift, what changes in your deals and who to brief.
- **Use it when:** After a rival's earnings call, a big acquisition or a leadership change. Use this for the strategic read; use "What a rival did this quarter" for a dated list of moves.
- **Best for:** Sales Leader & RevOps, Presales & Solutions, Marketing & ABM, Account Executive, Partnerships & Alliances
- **Time:** 4–6 min
- **Inputs:** Competitor (e.g. salesforce.com); What I sell (e.g. customer service platform); Area to watch (e.g. customer service and AI agents (optional)); Account to defend or win (e.g. att.com (optional))

### Detailed prompt

```text
Act as my competitive strategist who reads earnings calls. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. salesforce.com]
- What I sell: [one line, e.g. customer service platform — skip if you ran the start-here prompt]
- Area to watch (optional): [e.g. customer service and AI agents]
- Account to defend or win (optional): [website of a live deal or key customer, e.g. visa.com]

CONTEXT (why this matters)
A real shift shows on the call, in money and in people. Read a tech vendor's priorities as product moves.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. List its earnings-call transcripts; note the latest three with fiscal quarter and release date.
3. Pull its key priorities grouped by function (up to 3 each, with fiscal quarter). Sort into New in the latest quarter, Repeated, and Older only. Focus on [Area to watch], or else on areas closest to [What I sell].
4. Search news for [Competitor], last 6 months (20+ items): executive moves, acquisitions, divestments, layoffs; mark the most important from the last 90 days.
5. Pull acquisitions in the last 12 months and reconcile with news. Flag announced-but-not-closed deals.
6. For each theme, link the priority, the money and the people.
7. If I gave [Account to defend or win], find it by website and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the shift that matters most and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at [Account to defend or win], the action this week, and [Competitor]'s dated move as the why-now; with no account given, name the role to brief.
- Table "Strategy read" (3): Shift | Strength (Strong = call + money + people; Moderate = two; Talk only) | Dated evidence | What changes in deals.
- Table "Money and people behind it" (up to 8): Date | Move | Size if given | Theme.
- "Trap question": one discovery question that exposes the rival's integration or execution risk.
- Detail: calls covered (Fiscal quarter | Release date) and priority shifts (Theme | New, Repeated or Fading | Latest quarter | Example priority).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Keep only acquisitions and leadership items where [Competitor] is the actor and the event is in the window.
- Never estimate layoff numbers.
- Say where they'll bundle or discount, what new objection to expect, and where they're distracted.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

### Quick version

```text
How has [Competitor]'s strategy shifted across its last 3 earnings calls? Lead with the bottom line and who to brief. Rate each shift Strong, Moderate or Talk only, and say what changes in my deals.
```

### Follow-ups

- Pull the latest call and quote the two passages that support the strongest shift.
- Which of my accounts run the products [Competitor] just acquired?
- Update my battlecard for [Competitor] with these shifts.

### Tips

- "Talk only" themes are often marketing; Strong themes are what their reps will push next quarter.
- Acquisitions mid-integration are a classic opening: ask customers about roadmap certainty.

## Where a rival makes its money

- **id:** `compete-revenue-mix`
- **What you get:** A competitor's revenue by business unit and region with growth, plus what it sells most, read as where it will defend price and where it is exposed, with the dated move and person to act on.
- **Use it when:** Before a pricing or positioning discussion, or when building a competitive account strategy.
- **Best for:** Sales Leader & RevOps, Account Executive, Services, SI & Staffing Seller, Marketing & ABM, Presales & Solutions
- **Time:** 2–4 min
- **Inputs:** Competitor (e.g. accenture.com); What I sell (e.g. data and AI services); Region I sell in (e.g. EMEA (optional)); Account to defend or win (e.g. boeing.com (optional))

### Detailed prompt

```text
Act as my competitive analyst for pricing and positioning. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. accenture.com]
- What I sell: [one line, e.g. data and AI services — skip if you ran the start-here prompt]
- Region I sell in (optional): [e.g. EMEA]
- Account to defend or win (optional): [website of a live deal or key customer, e.g. visa.com]

CONTEXT (why this matters)
A rival protects its big, growing lines and discounts where revenue is small or shrinking; mix and install base are proxies.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull the latest fiscal-year revenue, EBITDA and R&D spend with growth, and the next-year forecast.
3. Pull revenue by business unit (share, growth); if none, say so and rely on step 5.
4. Pull revenue by region, latest year; compute growth from amounts.
5. Mix proxy. Software: top 10 products by companies using them. Services: customer summary and top 12 workloads by engagements, marking those closest to [What I sell].
6. Classify each row: Core (large, growing), Cash (large, flat or falling), Bet (small, fast growing), Exposed (small, shrinking). Large = 15%+ share; growing = above company growth (editable defaults).
7. Dated trigger: [Competitor]'s most important news item from the last 90 days.
8. If I gave [Account to defend or win], find it by website and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — where they'll defend and where they're exposed, and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at [Account to defend or win], the action this week, and [Competitor]'s dated move as the why-now; with no account given, name the role to brief.
- Table "Where they make money" (up to 10): Unit, region, product or workload | Share or size | Growth | Class. Highlight [Region I sell in].
- Table "Headline numbers": Metric | Latest FY | Growth | Forecast.
- "Defend vs exposed": 3 bullets each, tied to rows above; then a 2-sentence pricing read labelled inference.
- Detail: full unit, region and mix tables.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Product counts are install base, not revenue. Never state the rival's prices, discounts or margins.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Use USD millions at Draup's rate. A forecast over 15% off the latest actual is a model estimate.
- Check for divestments before calling a regional drop a cut.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
Where does [Competitor] make its money? Lead with where it will defend price and where it's exposed, and the named person to act with. Show revenue, growth and forecast, revenue by unit and region, and its biggest products or workloads.
```

### Follow-ups

- Compare this mix with my second competitor's.
- Which accounts in my territory run [Competitor]'s Exposed products?
- Write 3 pricing objections we'll hear in their Core area and a reply to each.

### Tips

- Large technology vendors often have no business-unit split in Draup; the product install-base list is the better proxy.
- Regions growing below the company average are often where their field teams are being cut back.

## Accounts where a rival is fading

- **id:** `compete-fading-installs`
- **What you get:** Your target accounts rated by how strong a rival's installed products are (Entrenched, Present, Thin or Fading), the successor already in place, and the best 3 takeout targets with a named person at the top one.
- **Use it when:** Planning a takeout campaign against a software rival across a named account list.
- **Best for:** Account Executive, SDR / BDR, Presales & Solutions, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Competitor (e.g. Teradata); Accounts (e.g. visa.com, fedex.com, att.com, boeing.com); What I sell (e.g. cloud data warehouse)

### Detailed prompt

```text
Act as my competitive displacement analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [software vendor or product, e.g. Teradata]
- Accounts: [up to 8 websites, e.g. visa.com, fedex.com, att.com, boeing.com]
- What I sell: [one line, e.g. cloud data warehouse — skip if you ran the start-here prompt]

CONTEXT (why this matters)
A rival's weakest installs are the cheapest wins: thin usage, stale evidence, a successor in place.

STEPS
1. Find each account by website and confirm the parent (retry an unresolved site once by name, show the match and score; never drop one silently); ask only if none or several match. If I gave more than 8, do the first 8 and offer to continue.
2. For each account, check the whole stack for [Competitor] products (one lookup, up to 50 rows), whatever area they're filed under. If [Competitor] is a product, check its maker as Draup spells it.
3. Record strength and last seen; a date shared by 3+ of an account's rows, or across accounts, is a refresh date.
4. Rate each account by its strongest [Competitor] product seen in the last 90 days (not on a refresh date): High = Red (entrenched), Medium = Amber, Low only = Green (thin), none = Green (fading). Flag any product first seen within 12 months (the one use of first-seen dates). Editable defaults.
5. For the 3 weakest accounts, pull the sub-category matching [What I sell] (e.g. Data Warehouse Software, 30 rows) and name other vendors' High or Medium products: the likely successor.
6. Rank targets: Green (fading), then Green (thin), then fewest [Competitor] products first (an easier swap).
7. For the #1 target, pull its top 3 executives in the matching workload (e.g. Data Engineering) or IT, and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the best target and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the #1 target, the action this week and the dated why-now (or say none).
- Table "Install health" (up to 8): Account | Strongest product (strength, last seen) | Products found | Rating.
- Table "Best 3 takeout targets": Account | Successor in place | Why now (dated) | Opening for [What I sell].
- "Leave for later": Red and Amber accounts, one line each.
- Detail: successor reads (Replacing, Parallel, Unclear), countries, unresolved accounts.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Low-only installs don't count as present (Green); a newly detected install is a fresh choice, so don't attack it.
- A successor already at High means a likely mid-migration: the play is speed.
- Say "not detected", never "not used". Label inferences "likely".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low. Say "fading", never "dropped".
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

### Quick version

```text
For up to 8 [Accounts], check every [Competitor] product in the stack. Lead with the best takeout target and a named person there. Rate each account Red, Amber or Green (thin or fading) and name the successor already in place.
```

### Follow-ups

- For [Account], map the buying committee in the function that owns the product.
- Check job ads at the best 3 targets for skills naming [Competitor]'s product (product spelling, not the maker; retry once if 0).
- Write a 90-word email to the named executive at the top target.

### Tips

- Keep the list to accounts you can work this quarter; 8 is one pass.
- A rival product still listed but Low across the board is often a renewal you can shape.

## Quarterly competitor watch for the team

- **id:** `compete-quarterly-watch`
- **What you get:** A one-page quarterly report on up to 3 rivals: a side-by-side scorecard including hiring in your space, each one's top moves and leadership changes, three team actions and a named account contact for the biggest threat.
- **Use it when:** At the start of each quarter, for a team meeting or sales kick-off. Use this for up to 3 rivals side by side; use "What a rival did this quarter" to go deep on one.
- **Best for:** Sales Leader & RevOps, Marketing & ABM, Presales & Solutions, Partnerships & Alliances
- **Time:** 6–10 min
- **Inputs:** Competitors (e.g. capgemini.com, cognizant.com, accenture.com); What I sell (e.g. cloud and data managed services); Quarter (e.g. last 90 days (optional)); Last report (e.g. paste last quarter's scorecard (optional))

### Detailed prompt

```text
Act as my competitive-intelligence lead writing the quarterly team briefing. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitors: [up to 3 websites, e.g. capgemini.com, cognizant.com, accenture.com]
- What I sell: [one line, e.g. cloud and data managed services — skip if you ran the start-here prompt]
- Quarter (optional): [default last 90 days]
- Last report (optional): [paste last quarter's scorecard to compare]

CONTEXT (why this matters)
Same lenses per rival; a rival adding roles in my space is coming for my deals.

STEPS
1. Find each competitor by website and confirm name, HQ and website (if one doesn't resolve, retry once by name and show the match and score). If I gave more than 3, do the first 3 and offer to continue.
2. For each, pull the quarter's news plus one targeted customer-wins search. Review 20+ items per rival; keep the top 5 by importance to [What I sell].
3. For each, pull the 12-month hiring timeline: last 5 full months vs the 5 before, Growing (+10% or more), Flat or Cutting (−10% or more), editable defaults. A month that jumps over 2x and stays may be a data-coverage change; flag it.
4. For each, pull 12-month postings in the 1–3 workloads closest to [What I sell], with trend.
5. Note dated leadership changes; if I pasted last quarter's scorecard, mark what changed.
6. Pick three team actions tied to dated moves.
7. From the named win most relevant to [What I sell], find the account by website and confirm its HQ and industry (if its executives look like look-alikes, use the next win and say so); pull its top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the biggest threat this quarter and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the account in the strongest rival win, the action this week and the dated why-now (or say none).
- Table "Scorecard": Rival | Top move (dated) | Hiring overall (% change) | Hiring in my space | Change vs last report.
- Table "Team actions next quarter" (3): Action | Owner role | Trigger move (dated).
- Per rival: "So what for us", one line, plus its top 3 moves.
- "Patterns" (2 bullets) and "Watch list" (3: unclosed deals, leaders in transition).
- Detail: each rival's top 5 moves (Date | Move | Source) and counts of deals, M&A and leadership changes.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Scorecard counts come only from items that survived the noise rule; say how many were reviewed per rival.
- Label unclosed acquisitions "announced".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 500 words above Detail, tables included.
```

### Quick version

```text
Quarterly watch on up to 3 [Competitors]. Lead with the biggest threat and a named person at the account it touches. Then a scorecard (top move, hiring overall and in my space), top moves per rival and 3 team actions.
```

### Follow-ups

- Turn the scorecard into a slide-ready table and 3 speaker notes.
- Deep-dive the strongest move with "How a rival's strategy is shifting".
- Draft a 150-word note to the sales team with the 3 actions. (Check your Draup licence before sharing Draup data outside your company.)

### Tips

- Save the scorecard each quarter and paste it next time; the change column is what leaders read.
- Three rivals per run keeps it fast; split bigger lists across runs.
