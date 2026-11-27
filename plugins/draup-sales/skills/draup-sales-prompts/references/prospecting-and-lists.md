# Prospecting and target lists

Build, size and qualify target lists from firmographics, tech, hiring and growth.

## Size your ideal-customer list

- **id:** `prospect-icp-list`
- **What you get:** The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- **Use it when:** You are planning a territory, a campaign or next quarter's target list. Use this when industry and size define your list; use "Who's hiring for a tech or role" instead when hiring is the filter.
- **Best for:** SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Retail); Territory (optional) (e.g. United States of America); Minimum employees (e.g. 5,000); Technology (optional) (e.g. Snowflake); Rank by (optional) (e.g. Opportunity Index (default; Draup's 0–10 attractiveness score), revenue or workforce); What I sell (e.g. data observability software)

### Detailed prompt

```text
Act as my sales operations analyst building a target account list. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Retail]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- Minimum employees: [e.g. 5,000]
- Technology (optional): [a product they must run, e.g. Snowflake]
- Rank by (optional): [Opportunity Index (default; Draup's 0–10 attractiveness score), revenue or workforce]
- What I sell: [one line, e.g. data observability software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical, territory and technology to Draup's names and show them.
2. Count companies with primary vertical [Vertical], HQ in [Territory], at least [Minimum employees] staff and, if given, [Technology] in their stack, using the short company view (up to 100 rows a page) so every match counts: that is the true total. Then count once with a size floor of 1 and once with none; the difference lacks a workforce figure.
3. Set aside intermediaries by default and say how many: distributors, wholesalers and resellers (sub-vertical Wholesale Distribution & B2B Supply, or so described), insurance brokers, and holding or private-equity firms.
4. Merge subsidiaries into parents, rank the rest by [Rank by] and pull full rows for the top 10: workforce, revenue, postings (90 days), service providers.
5. For the 5 best fits: confirm [Technology] with its usage strength and last-seen date, and its top 90-day news item where it is the actor.
6. For the #1 account: the top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — the true count with every filter applied, and what it means for [What I sell].
- Recommended next step: a named person (name, full title), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Where to start" (5 rows): Company | Why it fits | Why now (dated, or "none in 90 days") | [Technology] usage.
- "Top 10": Rank | Company | Workforce | Postings (90 days) | Flag.
- Count line: "N companies match every filter; X intermediaries set aside; Y more lack a workforce figure. Include them?"
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: revenue ($M, FY), Draup-estimated IT spend and 3 providers for the top 10; the intermediaries list.

RULES
- If the count runs past 300, report "300+" rather than guessing.
- Low [Technology] usage means present, not standard; say so.
- Flag "check revenue" above $5M revenue per employee and "check vertical" when a description doesn't fit.
- Never rank on IT spend (modelled from revenue). Professional information only.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line first: how many [Vertical] companies HQ'd in [Territory] with [Minimum employees]+ staff (running [Technology]) match every filter, distributors set aside. Then the 5 to start with, each with a dated why-now, and who to call first.
```

### Follow-ups

- Show the companies with no workforce figure, largest revenue first.
- Put the distributors back and re-rank by revenue.
- Tier the top 10 by propensity to buy [What I sell].
- Write a 70-word opener for the #1 account built on its why-now.

### Tips

- The default ranking (Opportunity Index, distributors set aside) surfaces mid-size accounts your AEs may not own yet. Rank by revenue when you want the biggest logos.
- Low usage of the required technology often means a pocket, not the main platform. Ask about it in discovery.
- Size filters drop companies with no workforce figure, often big private firms. The count line tells you how many.

## Who's hiring for a tech or role

- **id:** `prospect-hiring-led-list`
- **What you get:** The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.
- **Use it when:** You sell around a technology or to a persona and want accounts actively building in that area. Use this when hiring is the filter; use "Size your ideal-customer list" instead when industry and size define the list.
- **Best for:** SDR / BDR, Account Executive, Services, SI & Staffing Seller, Marketing & ABM
- **Time:** 2–4 min
- **Inputs:** Technology or Role (e.g. Snowflake (or: Head of Data Platform)); Territory (optional) (e.g. United States of America); Vendor to exclude (optional) (e.g. Snowflake Inc.); What I sell (e.g. data-platform migration services)

### Detailed prompt

```text
Act as my pipeline research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Technology or Role: [a product, e.g. Snowflake, or a job title, e.g. Head of Data Platform]
- Territory (optional): [country in full; default: my territory from setup, e.g. United States of America]
- Vendor to exclude (optional): [the maker, or my own company, e.g. Snowflake Inc.]
- What I sell: [one line, e.g. data-platform migration services — skip if you ran the start-here prompt]

STEPS
1. Resolve the technology (or role) and territory to Draup's names; show them.
2. Technology: filter postings by the product's skill name (e.g. "CrowdStrike Falcon", not "CrowdStrike"); if 0, retry once with the product name. If the top company has under 30 postings (editable), also run a keyword search and say which you used. Role: list the title variants Draup sees and keep only the same seat (drop recruiter and junior variants).
3. Pull the top 40 companies by postings in [Territory], last 12 months, excluding staffing firms and job boards.
4. Remove [Vendor to exclude] and its subsidiaries and unnamed rows; record each. Move IT-services and consulting firms to a separate "Partners hiring" list.
5. Merge brands and subsidiaries into parents, then look up the top 10 end employers in one company list by exact name: workforce and primary industry. Work out postings per 1,000 employees.
6. For the top 3 by postings per 1,000: the most important news item from the last 90 days where the company is the actor. For the #1: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where demand is and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "End employers hiring" (top 10): Rank | Company | Postings (12 months) | Per 1,000 staff | Why now (dated).
- "Partners hiring" (top 5): Company | Postings — co-sell partner or competitor.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: industries driving demand (Industry | Postings | Share %); the "Removed" list with reasons.

RULES
- Label tables with territory, window and filter (product or keyword).
- Raw postings reward size: show per-1,000 beside every count; write "n/a" when workforce is missing.
- A posting count above the company's workforce means a failed match; say so and drop it.
- Postings are openings, not hires. Professional information only.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: which end employers posted most [Technology or Role] jobs in [Territory] in 12 months? Top 10 after removing job boards, staffing firms and the vendor, with postings per 1,000 staff and who to call.
```

### Follow-ups

- For the top 5 employers, show 3 recent postings each with title, date, location and key responsibilities.
- Which of these employers show [Technology] in their tech stack, with usage strength and last-seen date?
- Draft a 70-word opener for the #1 employer that cites its hiring.

### Tips

- Postings per 1,000 staff often reorders the list: a mid-size company hiring hard beats a giant's routine backfill.
- IT-services firms hiring for a technology are building a practice. Treat them as partner or competitor leads, not end customers.

## Find look-alikes of your best customer

- **id:** `prospect-lookalikes`
- **What you get:** Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches, plus who to call first and why now.
- **Use it when:** You have a strong reference customer and want more accounts like it.
- **Best for:** SDR / BDR, Account Executive, Marketing & ABM, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. your best customer's website (e.g. contoso.com, illustrative)); Key products to match (optional) (e.g. SAP, Blue Yonder); Territory (optional) (e.g. HQ country; default: my territory from setup, else the customer's HQ country); What I sell (e.g. retail demand-forecasting software)

### Detailed prompt

```text
Act as my account-targeting analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [best customer's website, e.g. contoso.com (illustrative)]
- Key products to match (optional): [e.g. SAP, Blue Yonder]
- Territory (optional): [HQ country; default: my territory from setup, else the customer's HQ country]
- What I sell: [one line, e.g. retail demand-forecasting software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name and show the match score) and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. Profile it: primary vertical, HQ country, workforce, revenue. With no key products given, pick its 5 products most relevant to [What I sell], skipping office, browser and chat tools.
3. Start with Draup's listed competitors; keep those in the same business at 0.3–3x its workforce (editable) and record removals.
4. Widen: same primary vertical, HQ in [Territory], parent companies only, 0.3–3x workforce, listing only companies whose stack includes the key products and showing which ones. Match by product or vendor, not category. Sort by Opportunity Index (Draup's 0–10 account-attractiveness score). Stop at 20.
5. For the best 5: the most important news item from the last 90 days where the company is the actor. For the #1: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — how many real look-alikes exist and what that means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Best 5 to start with": Company | Why similar | Shared key products | Why now (dated).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: one line with the customer profile used; the full list (Company | Workforce | Revenue ($M, FY) | Shared products | Listed competitor? | Flag); removals.

RULES
- Never include the customer, its subsidiaries or sister companies.
- If fewer than 20 fit, name the criterion you loosened; never loosen silently.
- If I've named competitors (here or in my setup), check the best 5's whole stack: High usage = Red; Medium or first seen in 12 months = Amber; Low or absent = Green (count presence only at High or Medium; say so). Rate a services rival by its share of active engagements: 30%+ Red, 10–29% Amber, under 10% Green.
- Size filters drop companies with no workforce figure; say how many and offer to include them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: find up to 20 look-alikes of [Company] (same industry and HQ country, 0.3–3x its size, sharing its key products), say why each matches, and name who to call at the best one.
```

### Follow-ups

- Write a reference-style opener for each of the best 5 without naming [Company].
- Who owns [Business function] at the top 3? Names and full titles.
- Show the next 10 look-alikes.

### Tips

- Naming 2 or 3 key products gives tighter matches than letting Claude pick.
- Use the website rather than the name; it is the most reliable way to land on the right company.

## Benchmark an account against its peers

- **id:** `prospect-peer-benchmark`
- **What you get:** How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.
- **Use it when:** You want peer context for a meeting, a QBR or a leadership review, scored on what you sell rather than generic size.
- **Best for:** Account Executive, Account & Customer Success Manager, Presales & Solutions, Marketing & ABM, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. delta.com); Peer websites (optional) (e.g. united.com, aa.com); What I sell (e.g. airline operations analytics platform)

### Detailed prompt

```text
Act as my competitive benchmarking analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [account website, e.g. delta.com]
- Peer websites (optional): [up to 4, e.g. united.com, aa.com]
- What I sell: [one line, e.g. airline operations analytics platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name and show the match score) and confirm it's the parent, not a subsidiary; ask me if several match.
2. No peers given? Use Draup's listed competitors and keep the 4 closest in business and size. Look everyone up by website; retry any miss once by name and show the match score, never dropping one silently.
3. One company list for everyone: revenue and growth, workforce and growth %, attrition %, postings (90 days), Opportunity Index (Draup's 0–10 score).
4. Postings in the workloads mapped to What I sell, last 12 months, for all companies in one pass; add postings per 1,000 employees. Name the workloads used.
5. If I've named competitors (here or in my setup), check each company's whole stack for their products, with usage strength and first- and last-seen dates.
6. Count distinct material news events in the last 90 days for each and keep the most material ("10+" if the first 10 all qualify).
7. For [Company]: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where [Company] stands on what matters to [What I sell].
- Recommended next step: a named person (name and full title from step 7), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Benchmark" (up to 8 rows): Metric | [Company] | Peer median | Leader | Read. Rows: revenue growth, workforce growth, postings in my workloads (12 months) and per 1,000, my competitors installed, news events (90 days).
- "Questions to ask": 3 places it trails, phrased as discovery questions, never "you're behind".
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: the full per-company table (fiscal year beside money); each company's most material event (date, headline, source); competitor products found.

RULES
- Rate my competitors by usage in the workloads I sell into: High = Red, Medium or first seen in 12 months = Amber, Low or absent = Green (only High or Medium count as installed; say so); services rivals by engagement share: 30%+ Red, 10–29% Amber, under 10% Green.
- Don't compare on IT spend (modelled from revenue) or Draup's yes/no event flags; count dated events.
- Show USD millions using Draup's conversion rate.
- If I ask for a slide: 5 bullets + 1 table.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: benchmark [Company] against [Peer websites] (or its 4 closest Draup-listed competitors) on growth, postings in what I sell, my competitors in the stack and 90-day news. Then 3 discovery questions and who to call.
```

### Follow-ups

- Which products did the peers adopt in the last 12 months that [Company] doesn't run?
- Turn the questions into a 100-word email to the person in the next step.
- Add 2 more peers and rerun the benchmark.

### Tips

- Works best with 3 to 4 peers of similar size.
- Lead with questions, not comparisons. Buyers open up when asked how they see a gap.

## Sell into your customer's competitors

- **id:** `prospect-competitor-set`
- **What you get:** Your customer's real competitors, ranked, with what happened at each in the last 90 days, a reference angle and a named person to call first.
- **Use it when:** You just won, or have a strong reference at, a company and want to take the story to its rivals.
- **Best for:** Account Executive, SDR / BDR, Marketing & ABM, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Company (e.g. your customer's website (e.g. fabrikam.com, illustrative)); Referenceable? (e.g. no); Proof point (optional) (e.g. cut scheduling overtime across its stores); What I sell (e.g. warehouse workforce-scheduling software)

### Detailed prompt

```text
Act as my account-based marketing analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [customer's website, e.g. fabrikam.com (illustrative)]
- Referenceable?: [yes or no — may I name them? e.g. no]
- Proof point (optional): [e.g. cut scheduling overtime across its stores]
- What I sell: [one line, e.g. warehouse workforce-scheduling software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name and show the match score) and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. Pull Draup's listed competitors (parent companies only), ranked by Opportunity Index (Draup's 0–10 account-attractiveness score), with workforce and revenue.
3. Keep same-primary-vertical companies at 0.3–3x the customer's workforce (editable); record removals. If under 4 remain, add same-vertical, same-HQ-country companies in that range, labelled "added peer".
4. For the top 5, pull top news from the last 90 days and keep material events: deals, new centres, M&A, senior leadership changes, layoffs, launches that touch [What I sell].
5. For the #1 target: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — the best next targets and why, for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 5": Competitor | Workforce | What happened (date, headline) | Reference angle (our result → their situation).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: full ranked list (Opportunity Index, revenue $M with FY, listed or added); "Removed" with reasons.

RULES
- If Referenceable? is no, never name [Company]; say "a leading [vertical] peer".
- Write "No material events in 90 days" rather than padding.
- Don't compare companies on Draup's yes/no event flags; count dated events.
- Show USD millions using Draup's conversion rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: list [Company]'s real competitors, ranked, with up to 2 material events each from the last 90 days, a reference angle and who to call at the best target.
```

### Follow-ups

- Write a 3-email sequence for the #1 competitor using the reference angle.
- Check the whole tech stack of the top 5 for any product that competes with ours.
- Who owns [Business function] at the top 2? Names and full titles.

### Tips

- Check the Removed list; small or unrelated firms are filtered out there.
- Ask your customer before naming them. The prompt defaults to an anonymous reference.

## Find the fastest revenue growers

- **id:** `prospect-revenue-growth-screen`
- **What you get:** The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside, a shortlist growing both revenue and headcount, and who to call first.
- **Use it when:** You want accounts with money and momentum, or a growth angle for a campaign.
- **Best for:** Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Vertical (e.g. Retail); Territory (optional) (e.g. United States of America); Minimum revenue ($M) (e.g. 1,000); Minimum employees (optional) (e.g. 5,000); What I sell (e.g. e-commerce replatforming services)

### Detailed prompt

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Retail]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- Minimum revenue ($M): [e.g. 1,000]
- Minimum employees (optional): [e.g. 5,000]
- What I sell: [one line, e.g. e-commerce replatforming services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical and territory to Draup's names and show them.
2. List companies with primary vertical [Vertical], HQ in [Territory], revenue of at least [Minimum revenue] (and the employee minimum if given). Count them all, merge subsidiaries into parents, then sort by revenue growth and take the top 30.
3. Mark "M&A-driven?" when growth tops 20% (check acquisitions and M&A news for up to 5), "check vertical" when the description doesn't fit, "stale year" when the fiscal year lags by over a year.
4. Set those aside; keep the top 10. Add workforce, workforce growth % and postings (90 days).
5. For the top 3 "growing and hiring": the most important news item from the last 90 days where the company is the actor. For the #1: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — who is growing fastest and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Fastest growers" (top 10): Rank | Company | Revenue growth % (FY) | Workforce growth % | Flag.
- "Growing and hiring": revenue growth over 10% and workforce growth over 0% (editable), one-line angle each.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: revenue ($M, FY), postings (90 days) and Opportunity Index for the top 10; "Set aside" rows and reasons; how many companies had no growth figure.

RULES
- Growth over 20% is "likely M&A until checked"; say what you found.
- Before calling a revenue drop of more than 5% a cut, check for a divestment, demerger or restatement.
- Size filters drop companies with no workforce figure; say how many.
- Show USD millions using Draup's conversion rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: the 10 fastest-growing [Vertical] companies by revenue, HQ in [Territory], $[Minimum revenue]M+, with likely M&A jumps set aside, a shortlist also growing headcount, and who to call at the best one.
```

### Follow-ups

- For the top 5, what are their stated priorities this year?
- Which of these grew revenue with flat headcount, and what does that suggest?
- Draft a growth-themed opener for the Growing and hiring companies.

### Tips

- Very high growth often means an acquisition. The prompt sets these aside until checked.
- Companies report on different fiscal years. Compare growth rates, not raw totals.

## Spot scale-up and cost-out buyers

- **id:** `prospect-growth-and-cost-out`
- **What you get:** Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and a named person to call first.
- **Use it when:** You pitch scale or cost takeout and want companies under growth strain or cost pressure.
- **Best for:** SDR / BDR, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Banking & Financial Services); Territory (optional) (e.g. United States of America); What I sell (e.g. managed IT operations and automation services)

### Detailed prompt

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Banking & Financial Services]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United States of America]
- What I sell: [one line, e.g. managed IT operations and automation services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull Draup's fastest-growing-workforce and biggest-decline lists for the vertical (each a fixed top 50). In the decline list, "attrition" is the % change in workforce.
3. Keep only [Territory] HQs if set, merging subsidiaries into parents. Split each list at 1,000 employees (editable).
4. For the 10 largest shrinking 1,000+ companies, run one news search (last 12 months) for acquisitions, mergers, closures, bankruptcies, layoffs and restructuring.
5. Move merged or closed companies to "Absorbed or defunct"; give the rest a dated reason or "no news found".
6. For the best-fit company on each side: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — who needs scale, who needs cost-out, and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Growing (1,000+)", top 10: Company | Current workforce | Growth % | Likely buyer title.
- "Shrinking (1,000+, independent)", top 10: Company | Current | Change % | Likely reason (date).
- "What to pitch": 2 bullets for growers (scale, enablement), 2 for shrinkers (cost takeout, automation).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: previous workforce figures; smaller companies (names and % only); "Absorbed or defunct" with date.

RULES
- State Draup's comparison period, or "period not stated".
- Never call a decline a layoff without a dated news item; don't lead with small companies' huge percentages.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: [Vertical] companies with the fastest workforce growth and the biggest declines (1,000+ staff), with mergers and closures checked, the pitch angle for each side and who to call first.
```

### Follow-ups

- Check the next 10 shrinking companies the same way.
- For the top 3 shrinking companies, who runs IT and Finance now?
- Write a cost-takeout opener for the #1 shrinking company citing its news.

### Tips

- Shrinking lists can include firms that were merged away. Confirm before you call.
- Percentages for small companies swing widely. Treat them as leads to verify.

## Find startups with real momentum

- **id:** `prospect-startups`
- **What you get:** The startups in a vertical that Draup scores for momentum, with what they do, funding, hiring, why they'd buy and a named person to contact first.
- **Use it when:** You sell to high-growth companies, or want early-stage logos before competitors find them.
- **Best for:** SDR / BDR, Account Executive, Partnerships & Alliances
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Insurance); City (optional) (e.g. London); Territory (optional) (e.g. HQ country; default: my territory from setup, or "global"); What I sell (e.g. cloud cost-management software)

### Detailed prompt

```text
Act as my startup prospecting analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Insurance]
- City (optional): [e.g. London]
- Territory (optional): [HQ country; default: my territory from setup, or "global"]
- What I sell: [one line, e.g. cloud cost-management software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical and, if given, the city to Draup's metro name (e.g. "Greater London Area, United Kingdom"); show both.
2. Pull Draup's top startups for the vertical (fixed top 50), limited to that metro if given, else to HQs in [Territory]. Keep only startups with a momentum score, highest first.
3. Look up the top 10 in one company list, keeping only the same Draup companies: what they do, HQ, workforce growth %, total funding, investors, postings (90 days).
4. For those 10, pull the last funding round (type, date, amount, lead investor).
5. For the best fit: its founders or first functional leaders (up to 3) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — how many momentum startups there are and the best fit for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 10" (highest momentum first): Startup | What they do | Last round (type, date, $M) | Postings (90 days) | Flag.
- "Why they'd buy": one line each for the top 5, tied to funding, hiring or stage.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: HQ, workforce growth %, total funding, lead investor and momentum score for all 10; "X startups scored".

RULES
- Leave out units of large corporations; they aren't startups.
- Flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- If an industry returns zeros, say so, retry with its parent and name it.
- Stop at 10 and offer the next 10.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: the top 10 [Vertical] startups by Draup's momentum score, with what they do, funding, last round, 90-day postings, why each might buy [What I sell], and who to contact at the best one.
```

### Follow-ups

- Continue with startups 11 to 20.
- Which of these raised money in the last 12 months? Show round, amount and date.
- Draft a 70-word opener for the best fit tied to its last round.

### Tips

- Add a city to focus on your territory.
- A recent round plus rising job postings is often the best timing signal at a startup.

## Find the biggest logos in your city

- **id:** `prospect-territory-logos`
- **What you get:** The largest employers in a vertical in one metro, by Draup-estimated local headcount, with global capability centres (GCCs) called out and a named person to call first.
- **Use it when:** You own a city or metro and want the big local employers to prioritise.
- **Best for:** Account Executive, SDR / BDR, Services, SI & Staffing Seller, Sales Leader & RevOps
- **Time:** 1–2 min
- **Inputs:** City (e.g. Bengaluru); Vertical (e.g. Banking & Financial Services); What I sell (e.g. GCC talent and operations services)

### Detailed prompt

```text
Act as my territory planning analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- City: [e.g. Bengaluru]
- Vertical: [industry, e.g. Banking & Financial Services]
- What I sell: [one line, e.g. GCC talent and operations services — skip if you ran the start-here prompt]

STEPS
1. Resolve the city to Draup's metro name (e.g. "Bengaluru Area, India") and the vertical to Draup's name; show both. If the metro returns nothing, try the nearest Draup metro and say which worked.
2. Pull the top employers in [Vertical] in that metro, ranked by local headcount; take the top 25.
3. Merge subsidiaries into parents, look them up in one company list and keep only the exact companies: global workforce, HQ country, and whether the metro is one of their GCC locations (a global capability centre is a company-owned offshore or captive site).
4. Work out local share = local headcount ÷ global workforce. Move IT-services or staffing firms to a separate list unless [Vertical] is IT services.
5. For the best fit for [What I sell]: its top 3 executives located in [City] in the function closest to What I sell, and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — who the big local logos are and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 10" (largest local headcount first): Company | Local headcount (approx.) | Local share % | Site type (HQ / GCC / Other).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: rows 11–25; global workforce and HQ country for all; "GCCs in [City]"; service firms in the list.

RULES
- Local headcount is a Draup estimate and can vary between lookups; present it as approximate.
- A GCC tag can include plants or operations sites; if a site looks like a plant, say so.
- Look up named companies by website or exact name; "contains" matches pull in look-alikes.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first: the 10 biggest [Vertical] employers in [City] by Draup-estimated local headcount, with local share, HQ or GCC site type, and who to call at the best one.
```

### Follow-ups

- For the top 5 GCCs, which functions are they hiring for in [City]?
- Who leads the [City] centre at the top 3 companies?
- Compare [City] with [another city] for the same vertical.

### Tips

- A high local share means the site matters to the company, which often means local decision makers.
- Use local headcount to rank companies, not to size teams.

## Is this inbound lead worth pursuing?

- **id:** `prospect-inbound-qualification`
- **What you get:** A fast Pursue now / Pursue / Nurture / Disqualify verdict on an inbound or referred account: your must-haves, urgency tied to what you sell, a bake-off check against your competitors, and a reply plan.
- **Use it when:** A lead, demo request or referral lands and you need to decide in minutes whether it deserves an AE's time.
- **Best for:** SDR / BDR, Account Executive, Marketing & ABM, Sales Leader & RevOps
- **Time:** 1–2 min
- **Inputs:** Company (e.g. fivebelow.com); Requester title (e.g. Director of Store Operations); What they asked for (e.g. a demo of shift scheduling); My must-haves (e.g. US retailer, 5,000+ staff, $1B+ revenue); Business function (e.g. Operations (security and data sit under IT in Draup)); What I sell (e.g. store-operations software)

### Detailed prompt

```text
Act as my sales development analyst qualifying inbound accounts. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. fivebelow.com]
- Requester title: [who reached out, e.g. Director of Store Operations]
- What they asked for: [e.g. a demo of shift scheduling]
- My must-haves: [checkable facts, e.g. US retailer, 5,000+ staff, $1B+ revenue]
- Business function: [the function I sell to, e.g. Operations; security and data sit under IT in Draup]
- What I sell: [one line, e.g. store-operations software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; ask me if several match. No match: retry once by name and show the match score (ask me if under 0.8); still nothing: say so and stop.
2. Profile: primary vertical, HQ, workforce, revenue and growth, workforce growth %, postings (90 days).
3. Read the requester: does [Requester title] buy or champion in [Business function], and does [What they asked for] fit what I sell?
4. 90-day news where [Company] is the actor, and 12-month [Business function] postings in the workloads closest to What I sell.
5. Check the whole stack for competitors I named (here or in setup), with usage and first-seen dates.
6. The top 3 executives in [Business function], including the most senior leader for what I sell (e.g. the CISO for security).

OUTPUT
- Bottom line: 2 sentences — the verdict and why, for [What I sell].
- Recommended next step: a one-line reply answering [What they asked for], who else to loop in (name, full title), and the dated why-now (or "the request itself is the why-now").
- "Fit": Must-have | Draup value (date) | Meets / Partly / Misses / Unknown.
- "Why now": up to 3 events (date | headline | so-what), or "none in 90 days tied to what I sell".
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: requester read (decision maker, champion, user or researcher); competitor products found; postings count.

RULES
- The inbound is the intent. Pursue = every must-have met and the requester fits. Pursue now = Pursue plus a material 90-day event tied to [Business function] or what I sell; unrelated news never raises urgency.
- Nurture = Partly or Unknown on any must-have, or a student, job-seeker, vendor or researcher; list what to verify. Disqualify = misses a must-have.
- A competitor installed with High or Medium usage, or first seen in the last 12 months: write "likely bake-off or renewal" in the verdict. Ignore Low or very-low-confidence detections and say so.
- Flag revenue growth over 20% as likely M&A until checked.
- Show USD millions using Draup's conversion rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Verdict first (Pursue now, Pursue, Nurture or Disqualify) on the inbound from [Requester title] at [Company] asking for [What they asked for], against [My must-haves]. Check my competitors in their stack; give a reply line and who to loop in.
```

### Follow-ups

- Draft the full reply to the requester using the why-now.
- Map the 3 most senior people for what I sell there, including the CISO or equivalent.
- Show 3 peers of similar size so I can mention them.

### Tips

- Write your must-haves as checkable facts (country, size, revenue, vertical). The verdict is only as sharp as the criteria.
- A pricing request plus your competitor in the stack usually means a bake-off or a renewal check. Ask which.
- Nurture is not a no. Check back when a new event appears.
