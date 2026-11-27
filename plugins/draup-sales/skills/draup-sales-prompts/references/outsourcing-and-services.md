# Outsourcing and services deals

For IT services, consulting and staffing sellers: incumbents, share of wallet, GCCs and wedges.

## Outsourcing footprint and consolidation wedge

- **id:** `services-outsourcing-footprint`
- **What you get:** How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- **Use it when:** Before any services pursuit, to size the account and see who you're up against. Use this when you don't yet know which rival matters; use "A rival's footprint and your wedge" instead when you do.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); What I sell (e.g. data engineering and analytics managed services)

### Detailed prompt

```text
Act as my outsourcing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. data engineering and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the account's active service providers and active engagements, once for the whole account and once for the business function closest to [What I sell] (e.g. IT).
3. Pull the top 25 providers. Set aside agencies, staffing, market-research and merchandising firms, software vendors, look-alikes and the account's subsidiaries (one combined line). Keep the top 10, with each one's engagements in that function.
4. Pull the top 15 outsourced workloads.
5. For up to 5 non-catch-all workloads, matching [What I sell] first, pull their providers: how many, and the largest one's share.
6. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — concentrated or long tail, and the best opening for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and the dated why-now (or say none).
- Verdict line: "Concentrated" if the top 3 providers hold more than 50% of active engagements (editable default), otherwise "Long tail". Every % is a share of the account's total active engagements from step 2; state that total.
- "Consolidation wedge" (up to 3): Workload | Engagements | Providers | Largest provider (share, rating) | One-line pitch. Only workloads matching [What I sell] with 5+ providers and none Red (editable defaults).
- "Top providers": Rank | Provider | Engagements | % of total | In [function].
- Gaps: what Draup lacked; ask in discovery.
- Detail: the 15 workloads (Workload | Engagements | Providers checked?) and the set-aside line.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- If no workload matches [What I sell], say so instead of forcing a wedge.
- $10B+ revenue but under 20 IT-services engagements? Warn the work may be in-house or the data thin.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the business function closest to What I sell; map a function I give to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Rate a services rival by its share of the account's active engagements in the relevant workloads: Red 30%+ (entrenched), Amber 10–29%, Green under 10% (light; room to wedge in).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

### Quick version

```text
Bottom line and a next step (named person, dated why-now) first. Then size [Company]'s outsourcing: active engagements, top 10 IT and services providers by share, concentrated or long tail, and up to 3 consolidation wedges for [What I sell].
```

### Follow-ups

- Show [Competitor]'s footprint at [Company] and where it's thinnest.
- Who owns the wedge workloads? List up to 5 leaders with full titles.
- Is any of this work moving in-house? Check in-house hiring in the wedge workloads.
- Draft a 120-word vendor-consolidation point of view for the person in the next step.

### Tips

- A long tail of small providers often means no one owns the workload end to end. That's the opening for a consolidation pitch.
- Engagement counts are Draup-derived. Use them to compare providers inside one account, not as contract values to quote to the client.

## A rival's footprint and your wedge

- **id:** `services-competitor-at-account`
- **What you get:** How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- **Use it when:** You're planning a displacement or second-vendor play at an account a rival already serves. Use "Outsourcing footprint and consolidation wedge" instead when you don't know who's there yet.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); Competitor (e.g. Cognizant); What I sell (e.g. application modernisation and managed cloud services)

### Detailed prompt

```text
Act as my services competitive analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Competitor: [Services firm, e.g. Cognizant]
- What I sell: [One line, e.g. application modernisation and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull active engagements and top 10 providers for the whole account and the function closest to [What I sell], without agencies and staffing firms. Confirm the competitor's Draup spelling.
3. Pull the competitor's engagement detail: engagements, tier, workloads, client and delivery locations.
4. If it has 2 engagements or fewer here (editable default), say so and run steps 3 and 5 on the largest provider instead. Under 20 IT-services engagements or an own capability centre? Flag the work may be in-house.
5. Pull the account's and the analysed provider's workload counts; check who holds up to 5 non-catch-all workloads: wedges matching [What I sell] plus the provider's top 2.
6. People and timing: the top 3 leaders in the function closest to [What I sell] and the most important 90-day news item where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the rating of [Competitor] (or the largest provider, if absent) and where I get in.
- Recommended next step: a person from step 6 (name and title), what to do, and the dated why-now (or say none).
- Verdict line: "[Provider] is #N at [Company] with X active engagements (Y in [function]); tier: …; rating: Red, Amber or Green" (by share of active engagements in my workloads).
- "Wedge workloads" (up to 3): Workload | Its engagements | Who else holds it | Why it's a wedge. Workloads matching [What I sell] where the provider has 3 or fewer engagements (editable default) or an operational or limited tier.
- "Top providers": Rank | Provider | Engagements | % of account | In [function]; highlight the analysed provider.
- Gaps: what Draup lacked; ask in discovery.
- Detail: the provider's footprint by workload and its onshore/nearshore/offshore share.

RULES
- Tiers: strategic (broad, long-standing), operational (defined services), specialist (niche), limited (a few small engagements); operational and limited are easiest to unseat.
- Never recommend catch-all workloads (Project/Programs Management, Account Management).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the business function closest to What I sell; map a function I give to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Rate a services rival by its share of the account's active engagements in the relevant workloads: Red 30%+ (entrenched), Amber 10–29%, Green under 10% (light; room to wedge in).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. How big is [Competitor] at [Company] in Draup: rank, engagements, tier, delivery locations, and 3 thin workloads matching [What I sell]? If it's absent, analyse the largest provider.
```

### Follow-ups

- Show the 10 most recent engagements between [Company] and [Competitor], with month, workload and delivery location.
- Which leaders at [Company] own the wedge workloads?
- Draft a 3-bullet 'why a second vendor' point of view for the person in the next step.

### Tips

- Spell provider names as Draup does. If a name returns nothing, try the short brand name.
- If your rival isn't there, the prompt switches to the largest provider, so an empty result still gives you a plan.
- A thin footprint in a workload you lead is usually a better wedge than attacking the rival's core.

## A rival's customers you can win

- **id:** `services-competitor-customers`
- **What you get:** A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.
- **Use it when:** You're building a displacement campaign against one services rival in one industry. Use "A rival's footprint and your wedge" instead for a single account.
- **Best for:** Services, SI & Staffing Seller, Account Executive, SDR / BDR, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Competitor (e.g. Capgemini); Vertical (e.g. Life Sciences); Country (e.g. United States of America (default: my territory)); Workload (optional) (e.g. Data Engineering); What I sell (e.g. clinical data and analytics managed services)

### Detailed prompt

```text
Act as my displacement-campaign analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [Services firm, e.g. Capgemini]
- Vertical: [Draup industry, e.g. Life Sciences]
- Country: [Customer HQ country in full, e.g. United States of America; default: my territory from setup]
- Workload (optional): [e.g. Data Engineering, or a business function I'll map; blank for all]
- What I sell: [One line, e.g. clinical data and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Confirm Draup's spelling of the competitor, industry and country. Use each customer's primary industry so loosely tagged companies don't slip in.
2. Pull the competitor's customers in that primary industry with HQ in that country (and workload, if given), by engagements. Merge subsidiaries into parents; keep the top 20.
3. For the top 8, pull each account's provider ranking (the competitor's rank and the provider just above or below it), and get all 8 accounts' total engagements in one customer lookup; share = competitor engagements ÷ total.
4. Pull the competitor's top 5 workloads in this industry and country.
5. People and timing: pick the Best 3 (see OUTPUT). For the first one, pull its top 3 leaders in the business function closest to [What I sell] (full profile titles) and its most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — how big [Competitor] is here and which accounts to attack first.
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Headline line: "[Competitor] has N customers and X active engagements in [Vertical], [Country]", plus its top 5 workloads.
- "Targets" (top 10): Rank | Customer | Engagements with rival | Share of account | Read.
- Read: Red (entrenched: #1 or 30%+), Amber (contestable: #2–3, or 10–29%), Green (foothold: outside the top 3 and under 10%; a light presence) — editable defaults. Rows 9–20: "not assessed".
- "Best 3 to target": assessed Amber or Green accounts with the most engagements, one line each with the provider next to the rival.
- Gaps: what Draup lacked; ask in discovery.
- Detail: rows 11–20 and each top-8 account's total engagements and rank.

RULES
- Flag customers that look misclassified, are the competitor's own subsidiaries or are investors; leave them out of Best 3.
- If fewer than 5 customers come back, drop the workload, then widen the country to its region, and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the business function closest to What I sell; map a function I give to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

### Quick version

```text
Bottom line and next step (named buyer, dated why-now) first. Which [Vertical] companies headquartered in [Country] use [Competitor] most in Draup? Top 20 by engagements, its share and rank at the top 8, and the 3 most contestable.
```

### Follow-ups

- Show [Competitor]'s footprint and wedge workloads at the first Best-3 account.
- Assess rows 9–16 the same way.
- Write a 3-email displacement sequence for the person in the next step.

### Tips

- Use the full country name, e.g. United States of America.
- An Amber account (the rival is #2–3) is often easier to win than a Red one where it is the main partner.

## Peers' outsourcing deals for social proof

- **id:** `services-peer-deals`
- **What you get:** Recent outsourcing engagements at the prospect's peers in the work you sell, ready-to-use proof lines, and who to send them to and why now.
- **Use it when:** You need "companies like you are already doing this" evidence for an email, a deck or a first call.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Marketing & ABM
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); Workload (e.g. Software Testing); My company (optional) (e.g. Northwind Data Services); What I sell (e.g. testing and QA managed services)

### Detailed prompt

```text
Act as my sales researcher building social proof for a services pitch. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Workload: [Draup workload, e.g. Software Testing; a business function like Quality is fine, I'll map it]
- My company (optional): [Our services firm as Draup spells it, e.g. Northwind Data Services]
- What I sell: [One line, e.g. testing and QA managed services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary industry and HQ country.
2. If I gave a business function, map it to its 1–2 main workloads and say which. Pull engagements in those workloads at other companies with the same primary industry and HQ country. Keep the 10 most recent: month, customer, provider, delivery location, one-line description. If fewer than 5, widen to the industry worldwide and say so.
3. Merge near-duplicates (same customer, provider and work within a quarter). Drop agencies, staffing firms and investors listed as customers.
4. If My company is given, pull our engagements in those workloads in the same industry, newest first, as reference candidates.
5. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — how common this work is among peers and the strongest proof angle.
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Peer engagements": Month | Customer | Provider | What the work was. Newest first.
- "Proof lines": 3 sentences of 25 words or fewer. Name companies only where I say it's allowed; otherwise describe them by size and industry.
- Gaps: what Draup lacked; ask in discovery.
- Detail: "Who peers use" (providers with counts) and "Our references" (Month | Customer | What the work was), if My company is given.

RULES
- These are Draup-derived records, paraphrased, with month-level dates. Never present them as quotes, press releases or signed contracts.
- If I ask for public references only, keep engagements Draup marks as publicly reported.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the business function closest to What I sell; map a function I give to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 400 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Find the 10 most recent [Workload] engagements at [Company]'s peers (same industry and HQ country) in Draup: month, customer, provider, the work. Then write 3 proof lines.
```

### Follow-ups

- Turn the proof lines into a 90-word email to the person in the next step.
- Which of these peers are also our customers? Here is our list: [Our customers].
- Show the same for [another Workload].

### Tips

- Engagement records have month-level dates. Use them to show a pattern, not to quote a specific contract.
- Describing peers by size and industry is often safer than naming them.

## Find the biggest buyers of my service

- **id:** `services-offering-to-buyers`
- **What you get:** Your offering mapped to Draup workloads you approve, then the 20 companies in your territory that outsource them most, their incumbents, where the provider mix is fragmented, and who to call first.
- **Use it when:** You have a new service line or practice, or want the biggest buyers of one type of work in an industry or country.
- **Best for:** Services, SI & Staffing Seller, Marketing & ABM, Sales Leader & RevOps, SDR / BDR, Partnerships & Alliances
- **Time:** 4–6 min
- **Inputs:** What I sell (e.g. We modernise legacy mainframe and .NET applications to cloud-native, then run them as a managed service.); Country or Vertical (e.g. Germany); Workload (optional) (e.g. Application Development & Maintenance)

### Detailed prompt

```text
Act as my go-to-market analyst for a services practice. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- What I sell: [One paragraph, e.g. We modernise legacy mainframe and .NET applications to cloud-native, then run them as a managed service.]
- Country or Vertical: [Required. HQ country in full, e.g. Germany (default: my territory from setup), or a Draup industry, e.g. Banking & Financial Services]
- Workload (optional): [If you know the Draup name, e.g. Application Development & Maintenance; skips the mapping]

STEPS
1. If Workload is given, confirm it and go to step 3. Otherwise map [What I sell] to up to 8 Draup workloads (types of work), each Strong, Partial or Doubtful with a 5-word reason. Automatic mapping can be loose; judge each.
2. Stop for me to confirm or prune (if I said "don't wait", use Strong only).
3. Pull the top 20 companies outsourcing the confirmed workloads in [Country or Vertical] (primary industry; HQ country). Remove IT services firms, consultancies, staffing firms, agencies and investors; merge subsidiaries into parents.
4. Pull the top 10 providers in the same segment, with share.
5. For the top 10 buyers, pull their top 3 providers in those workloads. Rows 11–20: "not checked".
6. People and timing: at the top buyer in "Where to play", pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- "Workload mapping" (shown first, before the list): Workload | Fit | Reason.
- Bottom line: 2 sentences — segment size and where to start.
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Target list" (top 10): Rank | Company | Engagements | Main incumbent (share, rating) | Fragmented?
- Fragmented = no provider Red in these workloads (editable default).
- "Where to play": 3–5 fragmented or broadest buyers, one line each.
- Gaps: what Draup lacked; ask in discovery.
- Detail: rows 11–20 and "Segment providers" (Rank | Provider | Engagements | % of segment).

RULES
- Never run the list without a country or industry; unlimited, it returns only global megacaps.
- Never map to catch-all workloads such as Account Management.
- Flag companies that look misclassified; leave them out of Where to play.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Rate a services rival by its share of the account's active engagements in the relevant workloads: Red 30%+ (entrenched), Amber 10–29%, Green under 10% (light; room to wedge in).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 450 words including tables.
```

### Quick version

```text
Map [What I sell] to Draup workloads for me to approve. Then give the bottom line, a named first call, and the 20 companies in [Country or Vertical] outsourcing that work most, with main incumbent and fragmentation.
```

### Follow-ups

- Add Draup's Opportunity Index score for each company and re-rank.
- For the top 5, who owns these workloads?
- Show peer engagements in the confirmed workloads I can use as social proof.
- Format this as a target list I can paste into my CRM (company, website, reason).

### Tips

- Check the workload mapping before the list is built. One wrong workload can fill the list with the wrong companies.
- A country or industry keeps the list from leaning toward global megacaps.

## Profile a services firm, rival or partner

- **id:** `services-competitor-profile`
- **What you get:** A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- **Use it when:** Before a competitive bid, when a new rival keeps showing up, or before approaching a firm as a partner.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Marketing & ABM
- **Time:** 2–4 min
- **Inputs:** Firm (e.g. Cognizant); Rival or partner (e.g. Rival); Vertical or Country (e.g. Life Sciences); What I sell (e.g. clinical data management and testing services)

### Detailed prompt

```text
Act as my competitive and alliances analyst for services deals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Firm: [Services firm, e.g. Cognizant]
- Rival or partner: [e.g. Rival]
- Vertical or Country: [Required. Draup industry, e.g. Life Sciences, or customer HQ country in full (default: my territory from setup)]
- What I sell: [One line, e.g. clinical data management and testing services — skip if you ran the start-here prompt]

STEPS
1. Find the firm by website or name (show the match and score); confirm Draup's spelling and that it's the parent. If a sister brand also matches, list it separately.
2. Pull its customer summary: active customers, engagements, main industries.
3. Pull its top 10 customers and top 10 workloads by engagements, overall and within [Vertical or Country].
4. Pull its delivery locations, always limited to [Vertical or Country]. Keep the top 10 metros and group them onshore (customers' country), nearshore (same region) or offshore.
5. People and timing: pull the most important news from the last 90 days where [Firm] is the actor (client wins, acquisitions, alliances). Partner: pull [Firm]'s top 3 leaders for [Vertical or Country] or alliances. Rival: pull the top 3 leaders, in the function closest to [What I sell], at its largest in-segment customer, where a displacement play would start.

OUTPUT
- Bottom line: 2 sentences — how strong [Firm] is in this segment and what that means for [What I sell].
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Header line: [Firm] | active customers | engagements | top 3 industries.
- "Top customers": Rank | Customer | Engagements overall | In segment.
- Rival: "How to out-position [Firm]" — 3 angles tied to facts (thin where we lead, offshore-heavy, few big logos). Partner: "Where to team" — 3 angles tied to facts (workloads it lacks that we cover, shared customers, complementary hubs).
- Gaps: what Draup lacked; ask in discovery.
- Detail: "Workloads" (Workload | Overall | In segment) and "Delivery hubs" (Metro | Country | Engagements | Onshore/Nearshore/Offshore, plus the % split).

RULES
- Never pull delivery locations without the industry or country limit; the full list is too large.
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- Analyst rankings and awards are context, never a why-now.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 430 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Profile [Firm] from Draup: customers and engagements, top customers and workloads overall and in [Vertical or Country], delivery hubs with onshore share, then 3 out-position (rival) or teaming (partner) angles.
```

### Follow-ups

- Which [Vertical] companies in [Country] use [Firm] most and look contestable?
- Show [Firm]'s footprint at [Company].
- Turn the three angles into a one-page battlecard, or a partner intro note.

### Tips

- Compare the overall and in-segment columns: a firm that is huge overall can be thin in your industry.
- For partners, overlap in customers matters more than size. Shared accounts are where a joint pitch lands.

## Which providers to partner with or replace

- **id:** `services-partner-map`
- **What you get:** For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.
- **Use it when:** You're deciding who to partner with and who you'd be replacing at one account. Use this when you want the play for every priority; use "Pick the SI to co-sell with" instead when you sell software and need one SI to co-sell with, and "Who's already working each priority" when you only need who's working each priority.
- **Best for:** Partnerships & Alliances, Services, SI & Staffing Seller, Account Executive
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); Business function (e.g. IT); I sell (e.g. software); What I sell (e.g. AI and automation platform); Partners to evaluate (optional) (e.g. Tailspin Partners, Accenture)

### Detailed prompt

```text
Act as my alliances and pursuit strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Business function: [e.g. IT or Supply Chain]
- I sell: [software, services or both — skip if you ran the start-here prompt]
- What I sell: [One line, e.g. AI and automation platform — skip if you ran the start-here prompt]
- Partners to evaluate (optional): [e.g. Tailspin Partners, Accenture]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull priorities in [Business function]; keep up to 8 most relevant to [What I sell], newest first, with source and quarter.
3. For each priority, list up to 4 linked providers and 4 linked products, skipping subsidiaries, agencies and staffing firms.
4. Pull the provider ranking limited to [Business function] (or its main workloads) and for the whole account: "in function / total".
5. Tag each Partner (complements what I sell), Displace (does what I sell) or Neutral; for software sellers, services firms and our platforms are never Displace.
6. Compare any partners I named: engagements in [Business function] at the account, in total there, and in [Business function] across its industry.
7. People and timing: the top 3 leaders in [Business function] and the most important 90-day news item where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — who to team with and who you'd replace.
- Recommended next step: a person from step 7 (name and title), what to do (often via the best partner's account lead), and the dated why-now (or say none).
- "Priority map": Priority (source, quarter) | Linked providers (in function / total) | Linked tech | Play | Likely owner.
- Play: Partner-led, Displacement, or Open (nothing linked, or only providers with 2 or fewer in-function engagements; editable default).
- "Best partners to call": up to 3, named partners first, with in-function engagements and why.
- Gaps: what Draup lacked; ask in discovery.
- Detail: "Who we'd displace" (up to 3, with engagements and rating) and the head-to-head table from step 6.

RULES
- Links are by workload, not confirmed: say "linked", never "used for".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Rate a services rival by its share of the account's active engagements in the relevant workloads: Red 30%+ (entrenched), Amber 10–29%, Green under 10% (light; room to wedge in).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 450 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. For [Company]'s top priorities in [Business function], which providers and tech vendors are linked to each, with engagements in that function? Tag Partner, Displace or Open for [What I sell].
```

### Follow-ups

- Pick the best co-sell partner for the top Open priority.
- Show the buying committee for [Business function].
- Draft a note to the best partner's account lead proposing a joint session with the person in the next step.

### Tips

- A provider linked to a priority works in the same workloads; it hasn't necessarily won that initiative. Check its in-function engagements before pitching a partnership.
- Name the partners you're weighing. The head-to-head comparison is often the most useful part of the answer.
- Open priorities with no strong incumbent are often the quickest entry.

## Is outsourced work coming back in-house?

- **id:** `services-reinsourcing-risk`
- **What you get:** For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- **Use it when:** Before a renewal, an expansion pitch or a new pursuit, to decode what the account really intends.
- **Best for:** Services, SI & Staffing Seller, Account & Customer Success Manager, Account Executive
- **Time:** 4–6 min
- **Inputs:** Company (e.g. pfizer.com); What I sell (e.g. managed analytics and BI services)

### Detailed prompt

```text
Act as my services account strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. managed analytics and BI services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the top 10 outsourced workloads with engagements, narrowed to the business function closest to [What I sell] (say which); if fewer than 5 remain, add the next largest and mark them "outside my function".
3. Pull in-house postings by workload in one pass (up to 60, monthly; narrowing to one workload mixes in co-tagged roles). Compare the last 5 full months with the 5 before.
4. Also list workloads outside that top 10 with postings up over 50% and 50+ in 12 months.
5. Pull capability-centre sites (company-owned offshore sites, all functions) and 12-month centre setup or expansion news; ignore branches, HQ moves and plants.
6. Classify each workload in order: No signal (under 20 postings in 12 months); Re-insourcing risk (up over 20% with a capability centre hiring in that function); Capability gap (up over 20%, no centre); Cost takeout (up 20% or less).
7. People and timing: one page of 10 leaders in the function closest to [What I sell]; for IT keep IT, applications, infrastructure, data, CIO or CTO titles; if none fit, widen per the people rule, then to a leader named in news. Add the most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — biggest risk and biggest opening for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and the dated why-now (or say none).
- "Workload read": Workload | Engagements | In-house postings (12 mo) | Last 5 vs prior 5 | Read.
- "Biggest risk" and "Biggest opening": one workload each, with what to pitch.
- "Growing in-house in my workloads": up to 3 step-4 rows in the workloads closest to [What I sell], shown here, not under Detail.
- Gaps: what Draup lacked; ask in discovery.
- Detail: other step-4 rows (Workload | Postings | Change | Centre link | Likely meaning) and the centre sites.

RULES
- Thresholds are editable defaults. Catch-alls (Project/Programs Management, Account Management): "not assessed".
- Site headcount is indicative; count each site once.
- Each Read is a hypothesis, not a fact.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Postings are openings, not hires; skip partial first and last months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Label inferences "likely".
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. For [Company]'s top 10 outsourced workloads in my function, compare in-house postings over time, check capability centres, and label each: re-insourcing risk, capability gap, cost takeout or no signal.
```

### Follow-ups

- Who leads the capability centre behind the biggest risk?
- Show the 10 most recent in-house postings for the risk workload, with title, date and location.
- Draft a renewal-defence talking point for the risk workload.

### Tips

- Hiring and outsourcing in the same workload isn't always bad news. Without a captive centre behind it, it often means demand is outgrowing both.
- The fastest in-house growth is often outside the outsourced top 10; that list is where new captive teams show up first.

## Their capability centres and the services play

- **id:** `services-gcc-opportunity`
- **What you get:** The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- **Use it when:** You sell capability-centre set-up, build-operate-transfer, staff augmentation or managed services to companies with captive centres.
- **Best for:** Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Company (e.g. pfizer.com); What I sell (e.g. GCC build-operate-transfer and talent services in India)

### Detailed prompt

```text
Act as my capability-centre and location-strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. GCC build-operate-transfer and talent services in India — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull sites Draup tags as global capability centres (GCCs), all functions: metro, country, indicative size, functions hiring, 12-month postings, growth index. Count each site once; drop sites hiring mainly in manufacturing (likely plants).
3. Pull IT and R&D footprint summaries. Take likely new sites only from news naming a new centre or office; Draup's "New Site" tag can also mark established sites.
4. Pull centre setup and expansion news (12 months) where [Company] is the actor.
5. In one company-list lookup, pull the account's top competitors in its primary industry with centre counts. Drop suppliers, dealers, its own subsidiaries and firms under one-fifth of its revenue.
6. People and timing: pull the top 3 leaders in the function closest to [What I sell], preferring those based in the largest centre's country, and the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — centre maturity and the play for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Centres": Metro | Country | Functions hiring | Postings (12 mo) | Indicative size. By postings.
- "Maturity" (editable defaults): Nascent = 1–2 centre metros, one main function; Scaling = 3–5 metros or several fast-growing functions; Mature = 6+ metros, several functions, average or slower growth.
- "Recommended play": build-operate-transfer or centre-as-a-service (nascent or new site), centre-of-excellence expansion (scaling), managed services (mature), or not a centre account, and why.
- Gaps: what Draup lacked; ask in discovery.
- Detail: "Likely new sites (from news)" (Metro | Date | What opened), IT and R&D footprint, and "Peers" (Company | Centre locations).

RULES
- Site headcount is approximate and varies between pulls; never quote it as exact.
- If no centres come back, say so; don't infer one.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Label inferences (buyer role, intent, fit) "likely".
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 430 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Map [Company]'s capability centres in Draup: metro, functions hiring, 12-month postings, indicative size, likely new sites and peers' centre counts. Give a maturity read and the services play.
```

### Follow-ups

- Who runs the largest centre? Find leaders based in that metro.
- Which IT and services providers deliver from [centre country] for this account?
- Which outsourced workloads is the centre likely to take back in-house?
- What roles are they hiring at the likely new site?

### Tips

- A site with fresh postings but little workforce is often the best moment for build-operate-transfer or staffing support.
- Peers with many more centres make a strong "your competitors are already doing this" argument.

## How their vendor mix compares with peers

- **id:** `services-vendor-mix-benchmark`
- **What you get:** Where the account outsources more or less than its industry, which leading industry providers it doesn't use yet, and who to raise it with.
- **Use it when:** You need a peer-based argument for a new service line, or to find consolidation targets. For internal planning.
- **Best for:** Services, SI & Staffing Seller, Partnerships & Alliances, Account Executive, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); What I sell (e.g. cloud infrastructure managed services)

### Detailed prompt

```text
Act as my services benchmarking analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. cloud infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary industry.
2. Pull the account's top 50 outsourced workloads with engagements, and each one's share of that total.
3. Pull the industry's top 50 outsourced workloads and shares the same way. If it returns zeros, try the parent industry and name it.
4. For the industry's top 20, compute an index: account share ÷ industry share. Under 0.5 = under-indexed; over 2.0 = over-indexed (editable defaults).
5. Pull the account's top 10 providers and the industry's top 10, leaving out agencies, staffing, market-research and merchandising firms. Find leaders missing at the account.
6. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the clearest gap or excess and what it means for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Workload mix" (top 10 by industry share): Workload | Account share | Industry share | Index | Read.
- "Under-indexed": up to 3 matching [What I sell], each as a question ("peers outsource this more; is it in-house?"). "Over-indexed": up to 3 that may suit consolidation or rate pressure.
- Gaps: what Draup lacked; ask in discovery.
- Detail: rows 11–20 of the mix and "Providers" (Industry rank | Provider | At the account? engagements or No).

RULES
- Shares are of each top-50 total, not all work; say so. The index is fragile: internal use only, never in front of the client.
- Exclude catch-all workloads (Project/Programs Management, Account Management, Talent Acquisition) from Under and Over picks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Compare [Company]'s outsourced workload mix and top providers with its industry's in Draup. Show where it's under- or over-indexed and which leading industry providers it doesn't use.
```

### Follow-ups

- Is [Company] hiring in-house for the under-indexed workloads?
- Which industry peers outsource the under-indexed workload most? Give me 5 names as proof.
- Draft a 100-word peer-benchmark email to the person in the next step, without the index numbers.

### Tips

- An under-indexed workload is either greenfield or done in-house. A quick look at job postings tells you which.
- Use the index to plan, not to pitch. In front of the client, talk about what peers do, not the multiplier.

## Pick the SI to co-sell with

- **id:** `services-cosell-partner`
- **What you get:** A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- **Use it when:** You sell software and want a systems integrator (SI) already inside the account to open or speed up a deal. Use "Which providers to partner with or replace" instead when you want the partner-or-displace play for every priority, and "Joint account plan with a partner" once you've picked the partner.
- **Best for:** Partnerships & Alliances, Account Executive, Presales & Solutions
- **Time:** 2–4 min
- **Inputs:** Company (e.g. pfizer.com); Workload or business function (e.g. Data Engineering); Technology (e.g. Snowflake); What I sell (e.g. Snowflake-native data observability software); Our current partners (optional) (e.g. Tailspin Partners)

### Detailed prompt

```text
Act as my partner and alliances manager. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Workload or business function: [e.g. Data Engineering, or IT — I'll map a function to its main workloads]
- Technology: [Our product or platform as Draup names it, e.g. Snowflake]
- What I sell: [One line, e.g. Snowflake-native data observability software — skip if you ran the start-here prompt]
- Our current partners (optional): [e.g. Tailspin Partners]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary industry.
2. If I gave a business function, map it to the 1–3 workloads closest to [What I sell] and say which.
3. Pull the top 10 providers in those workloads at the account, leaving out agencies and staffing firms, and each one's total engagements at the account. Show "in workload / total".
4. For the top 5 (plus current partners in the top 10), pull relationship tier and delivery locations.
5. Pull the top 10 providers whose engagements involve [Technology] in the account's primary industry, worldwide.
6. Check the account's whole tech stack for [Technology] and other products by its maker: usage strength and last seen.
7. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the partner to call first and why.
- Recommended next step: a person from step 7 (name and title), what to do (with or through the partner), and the dated why-now (or say none).
- "Shortlist": Partner (current partners marked) | In workload / total | Tier | [Technology] engagements in industry | Verdict.
- Verdict: Lead co-sell (here in the workload and [Technology]-skilled), Access partner (here, little [Technology]), Skills partner ([Technology]-skilled, not here) or Skip. Current partners first.
- "Call first": one partner, three reasons tied to numbers.
- "Is [Technology] already there?": installed (strength, last seen) or not seen — expand or land.
- Gaps: what Draup lacked; ask in discovery.

RULES
- If [Technology] returns nothing, retry with the vendor or product family name and say which worked.
- A strategic tier means access and possibly loyalty to a rival product; note it, don't assume it.
- Never rank partners on whole-account counts; a firm big elsewhere in the account may do none of this work.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

### Quick version

```text
Bottom line and next step (named person, dated why-now) first. Which providers deliver [Workload] at [Company] (engagements in that work vs total), which have [Technology] experience in its industry, and which one do I call first?
```

### Follow-ups

- Draft a short note to [Partner]'s account lead proposing a joint approach to the person in the next step.
- Which other accounts in [Vertical] does [Partner] serve in [Workload]?
- Build a joint account plan for [Company] with [Partner].

### Tips

- The best co-sell partner is usually already inside the account in your workload, even if it isn't the biggest provider overall.
- Ask for the partner's other accounts in the industry to build a joint pipeline, not just one deal.
