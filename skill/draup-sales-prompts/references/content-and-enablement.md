# Content and enablement

Turn Draup data into battlecards, ABM messages and email sequences.

## Battlecard: beat a rival services firm

- **id:** `content-battlecard-services`
- **What you get:** A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.
- **Use it when:** A services rival keeps showing up in your pursuits, or you're preparing a team for a competitive bid or renewal. Selling software? Use "Battlecard: beat a rival software vendor" instead.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Presales & Solutions, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Competitor (e.g. infosys.com); What I sell (e.g. SAP S/4HANA migration and managed services); Vertical (optional) (e.g. Automotive); Where we lose to them (optional) (e.g. lost the Contoso Retail bid on offshore price); Proof we can cite (optional) (e.g. halved SAP ticket backlog at Fabrikam Foods)

### Detailed prompt

```text
Act as my competitive analyst for services pursuits. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [rival services firm's website, e.g. infosys.com]
- What I sell: [one line, e.g. SAP S/4HANA migration and managed services — skip if you ran the start-here prompt]
- Vertical (optional): [e.g. Automotive]
- Territory (optional): [HQ country in full, e.g. Germany; blank uses my saved territory]
- Where we lose to them (optional): [paste win/loss notes, e.g. lost on offshore price]
- Proof we can cite (optional): [e.g. halved SAP ticket backlog at Fabrikam Foods]

CONTEXT (optional)
Whole-firm totals flatter a big rival; what matters is my workloads (e.g. ERP Implementation).

STEPS
1. Find [Competitor] by website and confirm the parent, not a subsidiary or brand; if unclear, ask me. Map What I sell to its 1–3 main workloads and say which.
2. Pull HQ, workforce, and latest fiscal-year revenue and growth (USD).
3. Pull its top 10 parent-company customers by active engagements in my workloads (primary industry [Vertical], HQ in [Territory], if given). Then, in one customer lookup without the provider filter, get those 10 accounts' total engagements in my workloads; share = rival ÷ total: Red 30%+ (entrenched), Amber 10–29%, Green under 10%.
4. Pull its top 8 workloads and top 3 delivery locations from the firm's summary.
5. Search 180 days of news on them (deals, acquisitions, leadership); review 30+ items.
6. Pick the first account: the top-10 customer with the most engagements in my workloads where they rate Green or Amber. Pull its top 3 executives in the function closest to What I sell and its top 90-day news item.

OUTPUT
- Bottom line: 2 sentences — their strength in my workloads and where [What I sell] can win.
- Recommended next step: the first account, who to contact (name and title from step 6), what to do, and the dated fact. If none, say so.
- "Where they deliver my work" (top 10): Customer | Industry | Rival / all engagements in my workloads | Share | Rating. Green = under 10%.
- "How we win": 3 angles tied to facts above and [Proof we can cite]; one landmine where they're strongest.
- "Trap questions": 3 questions that expose their weak spots without naming them.
- "Objection to expect": their likely claim and a one-line, data-backed reply.
- Detail: what they win (workload, engagements); delivery hubs; recent moves (up to 6, dated, sourced, why it matters); "Where we lose" counters.
- Gaps: what Draup lacked, to ask in discovery.

RULES
- Never build an angle on catch-all workloads (Project/Programs Management, Account Management).
- Mark the card "Internal use" (customer lists are for targeting, not quoting); claim no results beyond [Proof we can cite].

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)": activity estimates, not contracts or headcount.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alikes and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. Flag conflicting or single-source figures as unverified.
- Never return a blank table: say what came back empty and use the fallback.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

### Quick version

```text
Bottom line and next step first: internal battlecard on [Competitor] for [What I sell]: top customers in my workloads rated Red/Amber/Green by its share, 180 days of moves, three ways we win, trap questions, first account.
```

### Follow-ups

- Which of my target accounts already use [Competitor]? Check [Accounts], 5 at a time.
- Turn 'How we win' and the trap questions into a 90-second talk track for a discovery call.
- Build the same card for the services rival we meet second most, and compare the two side by side.
- Show [Competitor]'s engagement trend in my workloads at [Account].

### Tips

- Paste your win/loss notes. The 'Where we lose' section is often the part reps use most.
- Read the Share column: a rival with hundreds of engagements firm-wide can hold under 10% of an account's work in your area (Green).

## Battlecard: beat a rival software vendor

- **id:** `content-battlecard-product`
- **What you get:** A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.
- **Use it when:** A software rival keeps showing up in your deals, or you're preparing a team for a competitive pursuit. Selling services? Use "Battlecard: beat a rival services firm" instead.
- **Best for:** Account Executive, Presales & Solutions, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Competitor (e.g. datadoghq.com or Datadog); What I sell (e.g. observability and IT operations software); Vertical (optional) (e.g. Retail); Where we lose to them (optional) (e.g. lost Contoso Retail on bundled pricing); Proof we can cite (optional) (e.g. Fabrikam Foods cut alert noise by half in one quarter)

### Detailed prompt

```text
Act as my competitive analyst for software deals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [rival vendor's website or product, e.g. datadoghq.com or Datadog]
- What I sell: [one line, e.g. observability and IT operations software — skip if you ran the start-here prompt]
- Vertical (optional): [e.g. Retail]
- Territory (optional): [HQ country in full, e.g. United States of America; blank uses my saved territory, or ask]
- Where we lose to them (optional): [paste win/loss notes, e.g. lost on bundled pricing]
- Proof we can cite (optional): [e.g. Fabrikam Foods halved alert noise]

CONTEXT (optional)
Implementers and resellers look like big users; they're partners, not targets.

STEPS
1. Find [Competitor] by website and confirm the parent. If I named a product, use its maker. If unclear, ask me.
2. Pull HQ, workforce, revenue and growth (USD), and top 5 products by installs.
3. In one short company list (default view, sorted by total_workforce, never employee_count), pull the 10 largest parent companies running [Competitor] products, in primary industry [Vertical] and HQ in [Territory]. Exclude IT services, consulting and outsourcing firms and say how many. Merge subsidiaries into parents; flag holding companies.
4. For the top 5, check the whole stack for any [Competitor] product in any area (usage, last seen). Count installs only at High or Medium on a named product; Low but seen in the last 6 months is "light"; not seen for 6 months is "fading"; if only the Generic row is High, say "present, product not identified".
5. Search 180 days of their news (launches, acquisitions, partnerships, leadership); review 30+ items.
6. First account: the largest Amber or fading install in [Territory] whose top executives sit at the parent, not a branch or subsidiary. Pull its top 3 executives in the function closest to What I sell and its top 90-day news item.

OUTPUT
- Bottom line: 2 sentences — how entrenched they are and where [What I sell] can win.
- Recommended next step: the first account, who to contact (name and title from step 6), what to do, and the dated fact. If none, say so.
- "Where they're installed": Company | Industry | Workforce | Main product | Usage rating. Rows 6–10: "usage not checked".
- "How we win": 3 angles tied to facts above and [Proof we can cite]; one landmine.
- "Trap questions": 3 questions that expose their weak spots without naming them.
- "Objection to expect": their likely claim and a reply.
- Detail: top products by install count; excluded implementers; recent moves (up to 6, dated, sourced); "Where we lose" counters.
- Gaps: what Draup lacked, to ask in discovery.

RULES
- Mark the card "Internal use". Claim no results beyond [Proof we can cite].
- No install in [Vertical] or [Territory]? Say so and show neighbouring industries or regions.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage, not first-seen dates; say "fading", never "dropped".
- Rivals: High usage in my workloads is Red, Medium Amber, newly detected Amber; unchecked is "present (usage not checked)"; ignore "Generic" rows.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alikes and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. Flag conflicting or single-source figures as unverified.
- Never return a blank table: say what came back empty and use the fallback.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

### Quick version

```text
Bottom line and next step first: battlecard on [Competitor] for [What I sell]: the 10 largest parent end users in my territory running it (no IT services firms), usage, 180 days of moves, how we win, first account.
```

### Follow-ups

- Check rows 6–10 product by product and add usage strength and last-seen dates.
- Which of my target accounts run [Competitor]? Check [Accounts], 5 at a time.
- Turn 'How we win' into a one-page objection-handling sheet for SDRs.
- List the IT services firms you excluded: they may be partners worth recruiting.

### Tips

- If your rival is a product inside a bigger company (a cloud database, say), name the product. Claude records the maker and checks every product it makes.
- Usage strength and last-seen date matter more than the install count: Medium or fading installs are where switching conversations start.
- Set a Territory (or save one in setup). Without it the list ranks the world's largest companies, so the first account can be one you can't sell to.

## ABM openers for 10 accounts at once

- **id:** `content-abm-messages`
- **What you get:** A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.
- **Use it when:** You're launching an ABM play, an SDR sprint or a joint campaign on a named list of 10–30 accounts. Use this for lists; use the signal-to-email prompt instead when you want one or a few carefully timed emails with a subject line and the full signal story.
- **Best for:** Marketing & ABM, SDR / BDR, Account Executive, Partnerships & Alliances
- **Time:** 6–10 min
- **Inputs:** Accounts (e.g. pepsico.com, medtronic.com, 3m.com, fedex.com, starbucks.com); Business function (e.g. Supply Chain); Persona (e.g. VP Supply Chain Planning); What I sell (e.g. supply-chain planning software); Proof point (optional) (e.g. cut planning cycle time at Fabrikam Foods); Co-sell partner (optional) (e.g. Tailspin Partners)

### Detailed prompt

```text
Act as my ABM copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [websites, up to 10 per pass, e.g. pepsico.com, medtronic.com, fedex.com]
- Business function: [e.g. Supply Chain]
- Persona: [title, e.g. VP Supply Chain Planning]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut planning cycle time at Fabrikam Foods]
- Co-sell partner (optional): [e.g. Tailspin Partners]

CONTEXT (optional)
A CFO hears cost and risk; a planning VP hears forecast accuracy and inventory. One dated, relevant signal beats three generic ones.

STEPS
1. Take the first 10 accounts and resolve them by website in one company lookup, confirming each parent (not a subsidiary or brand). Retry any that don't resolve with one name lookup using the group or legal name (e.g. "Expedia Group", not "Expedia"), showing the match and score; list any that still fail and carry on, never dropping one silently.
2. For each, pull its top 3 [Business function] priorities (newest first, with source and quarter) and keep the best fit for [What I sell].
3. Pull one news feed for all 10, last 60 days, money-or-change categories (deals, new sites, leadership moves, acquisitions, investments, layoffs). If one account fills over a third of items, pull again without it. For accounts with nothing, check top-ranked signals in the window.
4. Keep one item per account where the account is the actor, preferring one linked to the priority. Orders placed with the account are context only.
5. Write 2 sentences to [Persona], in their language: the signal and date; then the priority link and the problem [What I sell] solves for them, ending in a soft question. [Proof point] in at most two messages; with [Co-sell partner], add ONE joint note for the strongest row.
6. For the first account, pull its top 3 executives in [Business function] and pick the closest match to [Persona].

OUTPUT
- Bottom line: 2 sentences — how many accounts have a strong hook and which to send first.
- Recommended next step: who to send first (name and title from step 6), and the dated signal; if none, say so.
- Table: Account | Signal (date) | Priority (quarter) | Strength | Message. Strong first. Strong = signal links to priority; OK = both, unlinked; Weak = priority only.
- Detail: sources for each row; the joint partner note; "Skipped" (not found or no [Business function] priority).
- Gaps: what Draup lacked, to ask in discovery.

RULES
- 45 words or fewer per message. No flattery or claims about the reader's own work.
- No qualifying signal: write from the priority alone, mark Weak. Never invent or re-date a signal.
- Quote priorities in Draup's words. After 10 accounts, show the table and continue unless I say stop.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alikes and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. Flag conflicting or single-source figures as unverified.
- If an account sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

### Quick version

```text
Bottom line and next step first: for up to 10 of [Accounts], a 2-sentence opener to a [Persona], in their words, tied to one [Business function] priority and one 60-day signal. Strong first (signal ties to the priority).
```

### Follow-ups

- Do the next 10 accounts on my list.
- Rewrite each Strong message as a LinkedIn connection request under 300 characters.
- Rewrite the Strong rows for a CFO persona instead.
- Write a 3-touch follow-up for the Strong rows: email on day 3, LinkedIn on day 6, a short close-the-loop email on day 10.

### Tips

- Narrow to one business function. Priorities across every function bury the one that matters to your persona.
- Weak rows aren't wasted: they often point to accounts that need a call or a different angle rather than an email.
- Change the persona and rerun: the same signal reads very differently to a CFO and a planning lead.

## 3-email sequence for one industry persona

- **id:** `content-email-sequence`
- **What you get:** A ready-to-load 3-email sequence for one persona in one industry, each email built on a priority in the persona's function and a dated move by a real company, plus the first account to load with a named contact.
- **Use it when:** You're starting outbound into an industry and need a sequence grounded in what that industry is working on. Use the ABM openers prompt instead when you already have a named account list.
- **Best for:** Marketing & ABM, SDR / BDR, Account Executive
- **Time:** 2–4 min
- **Inputs:** Vertical (e.g. Automotive); Persona (e.g. Head of Supply Chain Planning); Business function (e.g. Supply Chain); What I sell (e.g. supply-chain planning software); Proof point (optional) (e.g. cut forecast error at Fabrikam Foods)

### Detailed prompt

```text
Act as my outbound copywriter for [Vertical]. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [industry, e.g. Automotive]
- Persona: [title, e.g. Head of Supply Chain Planning]
- Business function: [the persona's function, e.g. Supply Chain]
- Territory (optional): [HQ country or region, e.g. Germany; blank uses my saved territory]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut forecast error at Fabrikam Foods]

CONTEXT (optional)
A sequence lands when every email is about the persona's own problem and carries proof that a peer is acting on it. Industry priorities give themes but no dates; proof must come from named, dated companies.

STEPS
1. Match [Vertical] to Draup's industry name and map [Business function] to its 1–3 main workloads; say which. If the industry returns zeros, say so and try the parent industry, naming it.
2. Pull the industry's priorities and judge fit from each priority's text.
3. Pick the 3 closest to [Business function] and [What I sell]. If no priority sits in the function, use the nearest (for Supply Chain: Manufacturing, Procurement, Management & Strategy) and say so.
4. For each, find one named company in [Vertical] acting on it in the last 180 days: first the priority's own examples; if they carry no date, pull the dated [Business function] priorities of 2–3 of the industry's largest parent employers in [Territory] (company list sorted by total workforce), then industry news (search, then the feed for links). The company must be the actor.
5. Name the first account to load: the company behind the strongest dated example (or the largest in [Territory] if none). Pull its top 3 executives in [Business function] and pick the closest match to [Persona].

OUTPUT
- Bottom line: 2 sentences — the persona's top industry pressure and the angle the sequence takes.
- Recommended next step: the first account to load, who to send it to (name and title from step 5), and the dated example. If none, say so.
- Email 1 (day 1): subject (7 words max) and body on priority 1.
- Email 2 (day 4): priority 2, using [Proof point] if given.
- Email 3 (day 9): priority 3, a short close-the-loop note.
- Each body: company example, the problem, one sentence on how [What I sell] helps, one low-effort call to action.
- Detail: "Priorities used": Priority | Why it fits the persona | Company example (month, year, source).
- Gaps: what Draup lacked, to ask in discovery.

RULES
- 120 words or fewer per body. Plain language, no hype, no emoji.
- Present examples as public industry moves, never as our customers.
- No example found: write on the priority alone and flag it. Claim no results beyond [Proof point].

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alikes and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. Flag conflicting or single-source figures as unverified.
- Never return a blank table: say what came back empty and use the fallback.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 500 words including tables; then offer to continue.
```

### Quick version

```text
Bottom line and next step first: a 3-email sequence (120 words each, with subjects) for a [Persona] in [Vertical], on 3 [Business function] priorities, each with a dated company example, plus the first account to load.
```

### Follow-ups

- Write a version of email 1 for a CFO in the same industry.
- Give me two subject-line options for each email to A/B test.
- List 10 more accounts in [Vertical] to load, each active in [Business function] hiring.
- Turn priority 1 and its example into a short LinkedIn post for our company page. Check your Draup licence before publishing Draup data externally.

### Tips

- Name the persona's function. Industry priorities span every department, and the sequence works best when they're the persona's own problems.
- Re-run it each quarter: industry priorities and the examples behind them change.

## Explain where a Draup number comes from

- **id:** `content-how-draup-knows`
- **What you get:** A plain-English, shareable answer on how Draup builds a number (IT spend, outsourcing activity, talent flow and so on) and how far to trust it, written for the person who asked, with the help-centre link.
- **Use it when:** A prospect or your own exec asks where a Draup number comes from and how much to trust it, or before you put a Draup figure on a slide.
- **Best for:** Presales & Solutions, Account Executive, Account & Customer Success Manager, Marketing & ABM
- **Time:** 1–2 min
- **Inputs:** Metric or question (e.g. How does Draup estimate a company's IT spend?); Audience (e.g. a CFO at a prospect)

### Detailed prompt

```text
Act as my presales engineer. Answer only from Draup's own help-centre content, through the Draup for Sales connector. Don't use outside knowledge or guess at methodology, and label anything that isn't from the help centre.

INPUTS (edit these)
- Metric or question: [what you were asked, e.g. How does Draup estimate a company's IT spend?]
- Audience: [who will read it, e.g. a CFO at a prospect]

CONTEXT (optional)
Trust in a number grows when you say plainly what it is: a reported figure, a modelled estimate, or a count built from public signals such as job postings and news. Overstating precision loses a CFO faster than admitting a range. Known traps worth checking: IT spend is modelled from revenue for many companies; industry totals are global; leadership data can lag about 3 months, while news and hiring are near real-time.

STEPS
1. Ask Draup's help centre the question as written. If it's vague (e.g. "Is the data accurate?"), break it into the specific metric being questioned and ask about that.
2. If the first answer doesn't cover how the number is built, ask once more with a narrower question (e.g. "Where does Draup's IT spend data come from?" or "How often is it refreshed?").
3. Keep the help-centre article titles and links that come back.
4. Decide which kind of number it is: reported, modelled estimate, or signal-based count. If the help centre doesn't say, write "not stated".

OUTPUT
- Bottom line: 2 sentences — what the number is (reported figure or Draup estimate) and how to present it to [Audience].
- Recommended next step: who to send it to and how (e.g. reply to the CFO's email with the link), and the follow-up question to expect.
- "How it's built": 3–4 plain sentences on where the data comes from, how the number is built and how often it's refreshed (if the help centre says).
- "How to present it": one sentence, e.g. "a modelled estimate for sizing, not an audited figure".
- "Source": help-centre article title(s) and link(s).
- Gaps: what the help centre didn't cover — worth raising with Draup support.

RULES
- Use only what the help centre returned. If it has no relevant article, write "The Draup help centre doesn't cover this" and suggest asking Draup support.
- Write for [Audience]: no internal jargon or field names.
- Don't overstate precision. If the help centre says modelled or estimated, keep that word.
- One metric at a time; offer the next.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Phone-first: open with Bottom line and Recommended next step. Keep to about 200 words plus the links.
```

### Quick version

```text
Bottom line first: in 4–5 plain sentences, explain how Draup works out [Metric or question] for [Audience], whether it's reported or estimated, using only Draup's help centre, with the article link and one line on how to present it.
```

### Follow-ups

- Turn this into a two-line footnote I can put under a slide.
- Now answer the follow-up they're likely to ask: how current is this data?
- Explain the same thing for an outsourcing-activity number instead.
- Write a 'Before you trust a number' box for my team covering IT spend, industry totals and leadership data.

### Tips

- Ask about one metric at a time. "How is IT spend estimated?" usually gets a far better answer than "How accurate is Draup?".
- Send the link with the answer, so the buyer can read the method in Draup's own words.
