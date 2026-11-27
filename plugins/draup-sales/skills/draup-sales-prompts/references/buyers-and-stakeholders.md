# Buyers and stakeholders

Find the people who own the problem and the budget, and a warm way in.

## Map the buying committee

- **id:** `people-buying-committee`
- **What you get:** Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- **Use it when:** Before multi-threading an account, or when you only know one contact. Use this when you need everyone who decides today; use "New leaders and warm intro paths" instead when you want people who just arrived or who came from your customers.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager, Presales & Solutions
- **Time:** 2–4 min
- **Inputs:** Company (e.g. costco.com); Business function or workload (e.g. IT, or Artificial Intelligence & Data Science); Region (optional) (e.g. United States of America); What I sell (e.g. application modernisation and cloud migration services)

### Detailed prompt

```text
Act as my sales stakeholder analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. costco.com]
- Business function or workload: [e.g. IT, or Artificial Intelligence & Data Science]
- Region (optional): [e.g. United States of America]
- What I sell: [one line, e.g. application modernisation and cloud migration services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
One contact is a single point of failure. A committee map tells you who to open with, who signs, and who might block, so you can multi-thread before the first proposal.

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull key executives for the function or workload, 10 per page, up to 3 pages, with region only if I gave one.
3. If a workload returns fewer than 5 people, add the 2 closest workloads and say which. Drop clear title–function mismatches and flag people at subsidiaries or acquired brands.
4. If no economic buyer (C-level, EVP, "Head of") appears, search once more without the function filter for C-level titles (Chief, EVP, CIO), keep those whose titles fit, and say what you found.
5. Pull priorities for the same function or workload to match leaders to initiatives.
6. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step in two parts, each with one dated fact: "Entry point" (the likely champion by name and title, and how to open) and "Sponsor to reach later" (the likely economic buyer by name and title, and what you need first). If either is missing, say so.
- One line: people found, pages checked, people kept, subsidiaries flagged, and whether the step-4 widening ran.
- "Buying committee": Rank | Name | Full title and unit (flag subsidiaries) | Likely role | Linked priority + quarter. Up to 10, ranked by role, then budget control, then title.
- Likely roles: Economic buyer, Technical buyer, Champion candidate, Influencer, Potential blocker (e.g. incumbent-tool owner, security, procurement).
- "Roles with no clear person": the titles to look for.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: Name | Location | Budget control | Time in role | LinkedIn; anyone beyond the top 10.

RULES
- Economic buyer and champion are candidates, never confirmed.
- Rank the parent company's own leaders above subsidiary leaders unless the subsidiary is where [What I sell] lands.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Buying committee at [Company] for [Business function or workload]: entry point and sponsor by name first, then up to 10 people with full title, unit (flag subsidiaries), likely role and linked priority. No economic buyer? Widen once to C-level.
```

### Follow-ups

- Profile the entry-point contact and give me 2 openers.
- Which of these people joined in the last 6 months?
- Do any of them have past companies that are our customers?

### Tips

- Use a workload (e.g. Cybersecurity) when your offer is narrow; use a function (e.g. IT) for a broad map.
- Many top leaders carry no function tag in Draup, which is why the prompt widens once to C-level titles before saying there's no economic buyer.
- Opening cold with the economic buyer often fails. Start with the entry point and earn the sponsor meeting.

## New leaders and warm intro paths

- **id:** `people-new-leaders-warm-paths`
- **What you get:** Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- **Use it when:** Monthly, or when an account goes quiet: new leaders often review vendors in their first 90 days. Use this for people who just arrived or came from your customers; use "Map the buying committee" instead when you need everyone who decides today.
- **Best for:** SDR / BDR, Account Executive, Account & Customer Success Manager
- **Time:** 2–4 min
- **Inputs:** Company (e.g. 3m.com); Workload (e.g. Inventory Management, Demand Management — a type of work, not a function like Supply Chain; a function gets mapped for you); Our customers (optional) (e.g. Contoso Retail, Fabrikam Foods); What I sell (e.g. supply-chain planning software)

### Detailed prompt

```text
Act as my sales stakeholder analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Workload: [1–3 Draup workloads, e.g. Inventory Management, Demand Management — not a function like Supply Chain; if I give a function, map it to workloads first]
- Our customers (optional): [e.g. Contoso Retail, Fabrikam Foods]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Leaders in their first 90 days set plans and review vendors. The warmest door is often someone who used to work at one of your customers, whether they arrived last month or years ago.

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. If I gave a business function, map it to the 1–3 closest Draup workloads and say which.
3. Pull executive hires and promotions, one workload at a time; keep rows where [Company] is the current employer.
4. Keep moves from the last 6 months. Leadership data can lag about 3 months: if none fall inside, show the latest moves from the 3 months before, labelled "just outside the window".
5. Compare each new hire's past companies (whole history, not just the last one) with [Our customers], allowing name variants ("Contoso" = "Contoso Retail Inc.").
6. If fewer than 3 warm paths, also check current senior leaders in the matching business function (10 per page, up to 3 pages) whose past companies include [Our customers]. Flag any with under 6 months in their title as new.
7. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title, what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- One line per workload: rows checked, rows kept, latest move date in the data.
- "New leaders": Date | Name | New title | Came from (company, or "promoted") | Warm path? Newest first, up to 10.
- "Warm paths": Name | Current title | Customer in their past | Found as (new leader or current leader) | Who on our side to ask.
- "First-90-days plays": the top 3 people to approach, each with a one-line angle tied to [What I sell].
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out exits; the customer-alumni prompt covers them.
- Drop rows that clearly aren't about [Company], such as look-alike company names.
- If a workload has no moves even in the wider window, say "none found"; don't widen further silently.
- A warm path means they worked at our customer, not that they bought from us.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- If I give a business function where a workload is needed, map it to the 1–3 closest Draup workloads, say which, then continue.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Leadership-move data can lag about 3 months; give the latest move date you saw.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
New leaders at [Company] in [Workload]: bottom line and who to contact first, then hires and promotions in the last 6 months (date, name, title, came from) and any current leaders who worked at [Our customers].
```

### Follow-ups

- Profile the top new leader and draft a congratulations note with a relevant angle.
- Check pages 4–6 of current leaders for more warm paths.
- Show exits in the same workloads: where did they go?
- Draft the intro request to our account team at the matched customer.

### Tips

- Type a workload if you know it; if you type a function such as Supply Chain, the prompt maps it to workloads and says which.
- Leadership-move data can lag about 3 months, so the prompt shows moves just outside the window rather than an empty table.
- A leader who came from one of your customers is often the warmest intro you can get.

## Warm paths among current leaders

- **id:** `people-warm-paths-current-leaders`
- **What you get:** Senior leaders at the account who used to work at your customers, partners or your own company, who on your side to ask for the intro, and why now.
- **Use it when:** Before cold outreach to a senior buyer, or when building an intro plan for a strategic account. Use "New leaders and warm intro paths" instead when recent arrivals matter most.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); Business function (e.g. IT); Our customers (e.g. Contoso Retail, Fabrikam Foods); My company (optional) (e.g. Northwind Data Services — to find alumni); Partners (optional) (e.g. Tailspin Partners); What I sell (e.g. cloud data-platform modernisation services)

### Detailed prompt

```text
Act as my relationship-mapping analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Business function: [e.g. IT]
- Our customers: [comma-separated, e.g. Contoso Retail, Fabrikam Foods]
- My company (optional): [to find alumni, e.g. Northwind Data Services]
- Partners (optional): [e.g. Tailspin Partners]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull key executives in [Business function], 10 per page, up to 3 pages.
3. Compare each person's past companies with [Our customers], [My company] and [Partners], allowing name variants ("Contoso" = "Contoso Retail Inc.").
4. If fewer than 3 match, check 3 more pages or widen to all functions, and say which.
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (a matched leader), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- One line: profiles checked, matches found, functions covered.
- "Warm paths": Name | Full title | Matched past company | Match type (Customer, Our alumni, Partner) | Budget control. Customers first, then alumni, then partners; by seniority within each.
- "Intro plan": for the top 3, who on our side to ask and a one-line ask.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: years at [Company], their title at the matched company (only if it was their most recent previous role), LinkedIn.

RULES
- Past companies come without dates unless it was the most recent previous employer: say "previously worked at", not when.
- Don't infer they used or bought our product there.
- If nothing matches, write "No matches in N profiles checked"; don't stretch to near-miss names.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Which senior [Business function] leaders at [Company] previously worked at [Our customers], [My company] or [Partners]? Bottom line and the intro to ask for first, then name, title, matched company, match type and budget control.
```

### Follow-ups

- Draft the intro request to our account manager at the matched customer.
- Profile the top match and give 2 openers referencing their past company.
- Run the same check on new leaders from the last 6 months.

### Tips

- List customers where you have a strong, referenceable relationship; a weak one makes a poor intro.
- Add your own company to find alumni. Former colleagues are often the fastest door-openers.

## Executive profile and openers

- **id:** `people-executive-profile`
- **What you get:** A one-screen profile of a named executive, two openers tied to the account's current priorities, and a dated reason to reach out now.
- **Use it when:** Before an email, call or meeting with a specific senior person.
- **Best for:** Account Executive, SDR / BDR, Account & Customer Success Manager
- **Time:** 2–4 min
- **Inputs:** Executive name (e.g. Jane Doe); Company (e.g. target.com); Business function (e.g. IT); What I sell (e.g. AI platform engineering services)

### Detailed prompt

```text
Act as my sales research assistant. Use Draup for Sales for every fact.

INPUTS (edit these)
- Executive name: [e.g. Jane Doe]
- Company: [website, e.g. target.com]
- Business function: [their likely function, e.g. IT]
- What I sell: [one line, e.g. AI platform engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. There is no name search: page through key executives in [Business function], 10 per page, up to 50, and stop when you find the name (allow initials and short forms).
3. If not found, show the top 5 in that function (name, full title) and ask which I mean. Don't guess.
4. Pull up to 5 recent priorities for their workloads; if none come back, use their business function.
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (usually this executive), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: name, full title from the profile, location, LinkedIn.
- "Profile": Time at company | Time in current title | Budget control | Workloads | Previous employer and title | Past companies.
- "What they likely own": 2 priorities from their area, each with source and quarter.
- "Openers": 2 openers (35 words or fewer), each tied to a named priority and [What I sell]; one may mention their previous employer.
- "One question to ask": open-ended, citing a priority.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Under 12 months in the current title is a timing signal; mention it.
- Say if the person belongs to a subsidiary or acquired brand.
- If not found and likely in Europe or the UK, say the profile may be restricted.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Profile [Executive name] at [Company] ([Business function]): bottom line and why reach out now, then full title, time in role, past companies, budget control, 2 openers tied to current priorities and one question.
```

### Follow-ups

- Write a 90-word email using opener 1.
- Who does this person likely work with? Map the buying committee around them.
- What does their previous employer run in my category?

### Tips

- Give the function you think they're in. Large companies have thousands of profiles, so the right function makes the search much faster.
- Openers tied to a named priority often land better than ones tied to the person's career.

## Who uses [Technology] there

- **id:** `people-personas-by-tool`
- **What you get:** Which roles at the account use a given tool, grouped into three buyer personas with the message for each, and the senior person to target first.
- **Use it when:** Planning persona-based outreach or ABM around a product you integrate with or replace.
- **Best for:** Presales & Solutions, Marketing & ABM, Account Executive
- **Time:** 2–4 min
- **Inputs:** Company (e.g. jpmorganchase.com); Technology (e.g. salesforce); What I sell (e.g. CRM data quality and automation)

### Detailed prompt

```text
Act as my persona research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Technology: [tool name, e.g. salesforce]
- What I sell: [one line, e.g. CRM data quality and automation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the company's roles that list [Technology] as a skill or tool. Names match exactly and in lower case; if nothing returns, try up to 3 variants (e.g. "salesforce crm", "salesforce sales cloud") and say which worked.
3. Take the top 10 roles by count, with job family and other tools.
4. Pull the number of job postings in the last 12 months that mention [Technology], as an activity check.
5. Group the 10 roles into 3 buyer personas (e.g. builders, operators, business owners).
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to name the senior owner to target.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "3 personas": name, roles in it, what they likely care about, adjacent tools that signal integration or displacement, a one-line message angle for [What I sell], and the likely senior owner.
- "Roles using [Technology]": Role | Job family | Other top tools (up to 5). Top 10.
- One line: postings mentioning [Technology] in the last 12 months.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If no roles use the tool, say so and show the 5 closest tools that do appear.
- Adjacent tools made by competitors I've named are displacement angles; say so.
- If a company's posting count is larger than its workforce, the company match is wrong; say so and leave it out.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Which roles at [Company] use [Technology]? Bottom line and who to target first, then top 10 roles with other tools, grouped into 3 buyer personas with a message angle for [What I sell].
```

### Follow-ups

- Find senior executives who manage these personas.
- Write one 80-word email per persona.
- Which of the adjacent tools compete with ours?

### Tips

- Type the tool in lower case and in its common short form first ("salesforce", "sap", "jira").
- Adjacent tools tell you what to integrate with, or what you might replace.

## Discovery questions built on their data

- **id:** `people-discovery-questions`
- **What you get:** An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- **Use it when:** Before a discovery call, so you lead with insight instead of 'tell me about your priorities'.
- **Best for:** Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. supply-chain and fulfilment modernisation services); Meeting with (optional) (e.g. SVP Technology, or a name)

### Detailed prompt

```text
Act as my discovery coach. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. supply-chain and fulfilment modernisation services — skip if you ran the start-here prompt]
- Meeting with (optional): [name or title, e.g. SVP Technology]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the 8 most recent stated priorities in the meeting person's function, or else the function closest to [What I sell].
3. Pull technology added in the last 12 months (High and Medium usage) in that function; if none, use the function's current High and Medium stack and say so.
4. Pull hiring workloads trending up over 12 months in that function (ignore partial first and last months).
5. Pull hires and promotions for the most relevant workload; if only exits come back, note the count and use news instead.
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Opening insight": 2 sentences to open with, built on the strongest fact.
- "Discovery questions": # | Question | Hypothesis | Evidence (dated fact) | What a good answer tells me. Exactly 8: 3 priorities, 2 technology, 2 hiring, 1 leadership or news. Order: strategy, specifics, then timing and budget.
- "If you only ask two": the two that best qualify [What I sell].
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Open questions only, no pitches.
- Phrase evidence as a well-read seller would ("I saw you've been building out AI engineering"), never as surveillance.
- Each question cites a different fact; if a source has no data, use another and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Leadership-move data can lag about 3 months; give the latest move date you saw.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

### Quick version

```text
Discovery prep for [Company]: bottom line and who else to invite, a 2-sentence opening insight, then 8 questions, each tied to a dated Draup fact, with the hypothesis and what a good answer tells me.
```

### Follow-ups

- Write the answers I'd hope to hear and how I'd respond to each.
- Turn the top 2 questions into a meeting agenda email.
- Pre-fill MEDDPICC for this deal from the same evidence.

### Tips

- Questions grounded in their own priorities often earn more airtime than generic discovery.
- Say who you're meeting; the prompt shifts priorities, technology and hiring to their function.

## Pre-fill MEDDPICC from outside-in data

- **id:** `people-meddpicc-prefill`
- **What you get:** A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.
- **Use it when:** After the first meeting, or before a deal review, to see what you know and what you still have to find out.
- **Best for:** Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Presales & Solutions
- **Time:** 4–6 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. cloud data-platform modernisation services); Business function (e.g. IT); Competitor (optional) (e.g. Accenture or Snowflake (company or product))

### Detailed prompt

```text
Act as my deal-qualification analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. cloud data-platform services — skip if you ran the start-here prompt]
- Business function: [e.g. IT]
- Competitor (optional): [e.g. Snowflake or Accenture]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Metrics: latest revenue and growth, and targets or guidance in relevant priorities.
3. Economic buyer: [Business function] executives, up to 3 pages of 10; keep senior titles with high budget control. If none is C-level, EVP or "Head of", widen once to C-level titles without the function filter.
4. Pain: the 5 most recent priorities in [Business function], with workloads.
5. Competition: if [Competitor] sells software, check the whole tech stack for any product it makes, in any area; if a services firm, pull its active engagements here. Then the top incumbents on the pain workloads.
6. Champion: start with executives under a year in their title from the people already pulled. Only if there are none, check hires and promotions (last 6 months) for the main workload, keeping only people whose current employer is [Company]; say so.
7. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from steps 3 or 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "MEDDPICC": Letter | What Draup suggests | Evidence + date | Status (Evidence, Hypothesis, Must discover) | Question to confirm. Rows: Metrics, Economic buyer, Decision criteria, Decision process, Paper process, Identify pain, Champion, Competition (with its Red, Amber or Green rating).
- Decision criteria: hypotheses from stack and priorities. Decision and Paper process: "Must discover" (fiscal year end hints timing).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: incumbent providers on the pain workloads with active engagements.

RULES
- Economic buyer and champion are candidates, never confirmed.
- Rank providers by engagements yourself; drop recruiters, staffing, agency and research firms; flag subsidiaries.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Leadership-move data can lag about 3 months; give the latest move date you saw.
- Competitor rating: a [Competitor] product with High usage in the workloads I sell is Red; Medium is Amber; newly detected in the last 12 months is a separate Amber signal.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Pre-fill MEDDPICC for [What I sell] at [Company] in [Business function]: bottom line and who to see next, then metrics, economic buyer candidates, pain, and [Competitor] rated Red/Amber/Green. Mark the rest must-discover.
```

### Follow-ups

- Write the 5 questions that would close the biggest unknowns.
- Profile the top economic-buyer candidate.
- Show [Competitor]'s footprint at this account in detail.

### Tips

- Outside-in data can suggest Metrics, Pain and Competition well. Decision process, Paper process and Champion usually need a conversation.
- Re-run after each meeting and overwrite the Must-discover rows with what you learned.
