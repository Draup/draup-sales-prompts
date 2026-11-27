# Partners and alliances

Pick, plan and grow co-sell motions with the partners already embedded in your accounts.

## Which SIs to recruit in an industry

- **id:** `partners-recruit-si-shortlist`
- **What you get:** A ranked shortlist of systems integrators that deliver your workload in one industry and already work with your technology, with anchor customers, delivery hubs, the one to recruit first and who to call there.
- **Use it when:** You're building or refreshing a partner programme for an industry and need to know which SIs actually have the practice. Use "Compare candidate partners head to head" instead when you already have 2–3 names.
- **Best for:** Partnerships & Alliances, Sales Leader & RevOps, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Vertical (e.g. Insurance); Workload (e.g. Data Engineering); Technology (e.g. Snowflake); Territory (optional) (e.g. United States of America); Our current partners (optional) (e.g. Tailspin Partners); What I sell (e.g. data observability software for insurers)

### Detailed prompt

```text
Act as my partner-programme strategist recruiting systems integrators (SIs). Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Workload: [The type of work my product serves, e.g. Data Engineering; a business function is fine, I'll map it]
- Technology: [Our platform or a rival's, as Draup names it, e.g. Snowflake]
- Territory (optional): [Customer HQ country in full, e.g. United States of America; default: my territory from setup; say "worldwide" for all]
- Our current partners (optional): [e.g. Tailspin Partners]
- What I sell: [One line, e.g. data observability software for insurers; skip if saved in setup]

STEPS
1. Use Draup's exact names; map a business function to its 1–2 main workloads. Say which you used.
2. Rank providers by [Workload] engagements for customers in [Vertical] (HQ in [Territory]); keep the top 15, removing and listing agencies, staffing firms and captives.
3. Rank providers again for the same industry and territory by engagements that mention [Technology], top 15. Then count all industry engagements mentioning [Technology], for each provider's share.
4. Pick 3 candidates high in both lists, current partners first. Pull each one's top 5 customers for [Technology] work in the industry.
5. For the same 3, pull delivery locations for [Workload] in the industry. Keep the top 5 metros, grouped onshore (customers' country), nearshore or offshore; onshore share = onshore engagements ÷ all 5.
6. People and timing: page through the recruit-first SI's Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances, partnerships or [Technology]; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
- Bottom line: 2 sentences — the SI to recruit first and why.
- Recommended next step: a person from step 6 (name and title), what to do, and the dated why-now; if none, say so.
- "Shortlist" (top 10): Rank | Provider (current partners marked) | [Workload] engagements | [Technology]-related engagements (share of industry total) | Verdict.
- Verdict: Recruit first (top 10 in both lists and 3+ [Technology]-related engagements), Practice partner (strong in the workload, little [Technology]), Technology specialist (strong in [Technology], thin in the workload) or Watch.
- "Top 3 profiles": Provider | Top customers for [Technology] | Single-account depth? | Top delivery hubs | Onshore share.
- Gaps: what Draup didn't have — ask in the first partner call.
- Detail: "Shared customers" (customers that appear for 2+ of the top 3) and "Removed" (Provider | Reason).

RULES
- Flag "single-account depth" when one customer holds over half a provider's [Technology]-related engagements; never "Recruit first" on that alone.
- Say "[Technology]-related", never "certified".
- Under 20 [Technology] engagements (editable)? Retry with the vendor's name, then drop the country; say which worked.
- Mark delivery metros that don't fit the provider "check location".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step (named SI leader, dated why-now) first. Which providers lead [Workload] in [Vertical] in [Territory], and which have [Technology]-related work? Top 10; Recruit first needs both lists and 3+ [Technology] engagements.
```

### Follow-ups

- Draft a recruitment email to the person in the next step, citing two facts from the shortlist.
- Run the same shortlist for [second Technology] so I can see who works with both.
- For [Provider], which of its [Vertical] customers don't run [Technology] yet? That's our joint pipeline.

### Tips

- Rank on the technology list as well as the workload list: a firm that is huge in the workload but rarely touches your technology needs heavy enablement.
- Mid-size specialists often show up high in the technology list. They can be easier to win as partners than the largest firms.
- SI executives are tagged IT Services, not by industry, so the answer finds industry and alliance leaders by their titles; if none show up, ask the SI for its industry lead.

## Accounts a partner can open for you

- **id:** `partners-sourced-pipeline`
- **What you get:** A sized list of companies in your industry and country where a named partner already delivers work and your product (or a rival's) isn't in the stack, with how deep the partner is at the top 5 and a named buyer at the best one.
- **Use it when:** Before a joint pipeline review, a partner business plan or a co-marketing campaign, when you need accounts the partner can open for you.
- **Best for:** Partnerships & Alliances, Account Executive, Sales Leader & RevOps, Marketing & ABM
- **Time:** 4–6 min
- **Inputs:** Partner (e.g. Accenture); Vertical (e.g. Retail); Country (e.g. United States of America); Not installed (e.g. Databricks); What I sell (e.g. lakehouse analytics platform for retailers)

### Detailed prompt

```text
Act as my partner pipeline analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Partner: [Services firm as Draup spells it, e.g. Accenture]
- Vertical: [Draup industry, e.g. Retail]
- Country: [HQ country in full, e.g. United States of America; default: my territory from setup]
- Not installed: [Maker whose products must be absent: ours, or a rival's, e.g. Databricks]
- What I sell: [One line, e.g. lakehouse analytics platform for retailers; skip if saved in setup]

STEPS
1. Use Draup's exact names for all inputs; say which.
2. Size the list: companies with primary industry [Vertical], HQ in [Country], [Partner] among their engaged providers, and no product made by [Not installed] anywhere in the stack. Band the total: request single rows at positions 10, 50, 100 and 250; the last that returns a company sets the band.
3. Band again without the [Not installed] condition, labelled, to show how much of [Partner]'s base already runs [Not installed].
4. Pull the top 10 matches in full, by revenue (if most rows lack revenue, sort by total workforce and say so): workforce, revenue, Opportunity Index, other providers, parent.
5. Flag: Subsidiary (name the parent), Misfiled, Possibly inactive. If more than 3 of the top 10 are flagged, move them to Detail and backfill the table with the next unflagged rows. List private companies without revenue but larger than row 5 as "Large private companies".
6. For the top 5 unflagged rows, pull [Partner]'s engagement detail: workloads, engagements (how many in workloads matching [What I sell]), tier and locations.
7. At the top unflagged account, pull the top 3 leaders in the function closest to [What I sell] and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — how much pipeline exists and which account to raise with [Partner] first.
- Recommended next step: a person from step 7 (name and title), what to raise with [Partner]'s client lead, and the dated why-now; if none, say so.
- Header line: "[Band] companies match; without the [Not installed] condition, [band]." One line on what the difference implies.
- "Pipeline" (top 10): Rank | Company | Revenue (USD M, FY) | Other providers (3) | Flag.
- "Partner depth" (top 5): Company | [Partner] engagements (in my workloads / total) | Tier | Depth | Joint angle for [What I sell].
- Depth: Deep (5+ engagements, or any matching [What I sell]), Light (1–4); editable.
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: workforce, Opportunity Index, parent; flagged rows moved out of the table, with the reason; "Large private companies".

RULES
- "No [Not installed] products" means no public evidence: a hypothesis to confirm with the partner.
- Judge depth on engagements, not the tier label.
- Under 10 matches? Widen to the region and say so.
- If the provider list and [Partner]'s engagement detail disagree, say so; trust the detail.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Trust usage strength and last-seen date, not confidence or first-seen; ignore "Generic" rows; a rival counts only at High or Medium usage.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step (named buyer, dated why-now) first. Which [Vertical] companies in [Country] use [Partner] and show no [Not installed] products? Band the total, top 10 unflagged by revenue, the partner's depth at the top 5.
```

### Follow-ups

- Show rows 11–20 the same way.
- For the top 3, what stated priorities in data and analytics could justify a joint pitch?
- Draft a one-page joint account list I can send to [Partner]'s alliance team (check our Draup licence first).

### Tips

- If the list is small or full of mid-size names, the big accounts probably already run the excluded maker. That's useful for the partner conversation too.
- Lead the partner review with accounts where the partner works in a workload next to yours; that's where an introduction is credible.

## Joint account plan with a partner

- **id:** `partners-joint-account-plan`
- **What you get:** A one-page plan you and a partner can both sign up to for one account: where the partner already works in your function, the priorities there, your technology's and a rival's position, who to meet and a 90-day plan with owners on both sides.
- **Use it when:** After you've picked a co-sell partner for an account and need a shared plan before the joint kickoff call. Use "Pick the SI to co-sell with" instead if you haven't picked the partner yet.
- **Best for:** Partnerships & Alliances, Account Executive, Services, SI & Staffing Seller, Presales & Solutions
- **Time:** 4–6 min
- **Inputs:** Company (e.g. allianz.com); Partner (e.g. Capgemini); Our technology (e.g. Snowflake); Competitor (optional) (e.g. Databricks); Business function (e.g. IT); What I sell (e.g. data quality and observability software)

### Detailed prompt

```text
Act as my alliance manager. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [Website, e.g. allianz.com]
- Partner: [Services firm as Draup spells it, e.g. Capgemini]
- Our technology: [Our product or its maker as Draup names it, e.g. Snowflake]
- Competitor (optional): [Rival maker, e.g. Databricks]
- Business function: [Where the buyers sit, e.g. IT]
- What I sell: [One line, e.g. data quality and observability software; skip if saved in setup]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary. No result: try its name once and show the match score. Use Draup's exact name from then on.
2. Pull the account's top 10 providers, once limited to [Business function] and once for the whole account; note [Partner]'s rank and engagements in each.
3. Pull [Partner]'s engagement detail at the account (workloads, tier, locations) and its engagements per workload. Pick up to 3 joint workloads closest to [What I sell], skipping catch-alls.
4. Pull priorities in the joint workloads, newest first; keep the 5 most relevant (source, quarter, whether [Partner] or our tools are linked).
5. Check the whole tech stack for products made by [Our technology] and [Competitor], whatever area they're filed under: usage strength and last seen. Count only High or Medium usage. Rate [Competitor]: Red for High usage in my workloads; Amber for Medium there or newly detected in 12 months; otherwise Green, still listed.
6. Pull 10 leaders in [Business function]; keep up to 4, group-level first, with each one's unit.
7. Timing: up to 2 reasons to act from the last 90 days of news.

OUTPUT
- Bottom line: 2 sentences — the joint play and why it beats either firm alone.
- Recommended next step: one person from step 6 (name and title), who opens (us or [Partner]), and why now (a step-7 item). If none turned up, say so.
- "Joint workloads": Workload | [Partner] engagements | Linked priorities | [Our technology] status | [Competitor] rating.
- "90-day plan": Days | Action | Our owner | [Partner] owner | Done when, for days 1–30 (access), 31–60 (discovery, proof), 61–90 (joint proposal).
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: partner position (rank and engagements in function and total, tier, locations); priorities to pitch together (Priority | Quarter | [Partner] linked? | Likely owner); people (Name | Full title | Unit | Who opens).

RULES
- Under 3 [Partner] engagements in the joint workloads (editable)? Call the plan partner-light and name the best-placed provider.
- A strategic-tier partner protects its scope: position [What I sell] as speeding its delivery.
- [Competitor] Red? Plan a bake-off or coexist position; say which.
- Priority links to tools or providers are by workload: say "linked".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 480 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step (named leader, dated why-now) first. Joint plan for [Company] with [Partner]: its engagements in [Business function] vs total, joint workloads and priorities, [Our technology] and [Competitor] in the stack, and a 90-day plan.
```

### Follow-ups

- Turn the plan into a one-slide summary for the joint kickoff call.
- Draft the email from me to [Partner]'s client lead proposing the kickoff, under 120 words.
- Show the next 10 leaders in [Business function], with full titles.

### Tips

- Send the partner the joint-workloads table before the kickoff; it shows you've done homework on their account, not just yours.
- A partner that is big at the account can still be light in your function. The plan checks both counts and says when the partner is light.

## Is this partner rising or slowing?

- **id:** `partners-momentum-check`
- **What you get:** A Rising, Steady or Slowing verdict on a prospective partner, scored from its hiring, headcount growth, client wins, acquisitions and footprint in your industry and country, with who to talk to there.
- **Use it when:** Before you sign, renew or put marketing funds behind a services partner. Use "Compare candidate partners head to head" instead to choose between several.
- **Best for:** Partnerships & Alliances, Sales Leader & RevOps
- **Time:** 2–4 min
- **Inputs:** Partner (e.g. hcltech.com); Vertical (e.g. Automotive); Country (e.g. Germany); What I sell (e.g. software-defined vehicle testing platform)

### Detailed prompt

```text
Act as my partner due-diligence analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Partner: [Website of the services firm, e.g. hcltech.com]
- Vertical: [Draup industry where we'd work together, e.g. Automotive]
- Country: [Customer HQ country in full, e.g. Germany]
- What I sell: [One line, e.g. software-defined vehicle testing platform; skip if saved in setup]

STEPS
1. Find the partner by website and confirm the parent, not a regional unit.
2. Pull its customer summary: active customers, engagements and top 3 customers overall.
3. Pull 12 months of monthly postings. A month that more than doubles and stays there is a "step change" (possibly wider data coverage, not demand).
4. Pull headcount growth over Draup's latest 12-month workforce window (it ends about 3 months ago; say the dates).
5. Search 12 months of deals, partnerships and M&A news where [Partner] is the actor (review 15+ items, keep up to 8), and pull 12 months of acquisitions; say if the acquisitions list looks incomplete.
6. For customers with primary industry [Vertical] and HQ in [Country]: pull [Partner]'s top 10 customers by engagements, and its delivery locations (top 8, with the share delivered in [Country]).
7. People and timing: page through [Partner]'s Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances or partnerships; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
- Bottom line: 2 sentences — the verdict and what it means for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and the dated why-now; if none, say so.
- "Scorecard": Signal | Evidence (dated) | Score from −1 to +1. Defaults (editable): Hiring +1 above +10%, −1 below −10%, else 0 (a step change scores 0 with a note); Headcount +1 above +3%, −1 below 0%; New client wins in 12 months +1 for 3 or more, −1 for none; Acquisitions +1 if any adds a capability close to [What I sell]; Segment footprint +1 if 5+ customers in the segment have 10+ engagements, −1 if fewer than 2.
- Verdict: Rising (+2 or more), Steady (−1 to +1), Slowing (−2 or less).
- "Wins and moves": Date | Event | Counterparty | Why it matters for us.
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: footprint in [Vertical], [Country] (Customer | Engagements); delivery hubs with onshore share; 3 "what this means for us" bullets tied to numbers.

RULES
- Engagement data lags announcements: if news shows a big new win where engagements are low, say so.
- Sports, sponsorship and stadium "partnerships" are not client wins.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step (named partner leader, dated why-now) first. Is [Partner] rising, steady or slowing? Score its hiring trend, headcount growth, client wins and acquisitions in 12 months, and its footprint in [Vertical], [Country].
```

### Follow-ups

- Run the same check on [second partner] and put the two scorecards side by side.
- Which of [Partner]'s [Vertical] customers in [Country] run our technology or a rival's?
- Draft three questions for our partner review that test the weakest signal.

### Tips

- Ask the partner about anything scored 0 with a note; a step change in postings or a fresh big win is a good conversation opener.
- Momentum in your segment matters more than company-wide growth. A firm can be growing overall and flat in your industry.

## Attach targets on a partner platform

- **id:** `partners-platform-attach`
- **What you get:** A sized, ranked list of companies in your industry and country that run a platform you integrate with and show no sign of your rival add-on, with the platform confirmed, a dated why-now and a named owner for the top 3.
- **Use it when:** You sell an add-on or integration for a platform (SAP, Salesforce, ServiceNow, Snowflake) and want a co-marketing or marketplace list to work with the platform vendor's field team.
- **Best for:** Partnerships & Alliances, Marketing & ABM, SDR / BDR, Account Executive
- **Time:** 4–6 min
- **Inputs:** Platform (e.g. SAP S/4HANA); Competitor (e.g. Celonis); Vertical (e.g. Automotive); Country (e.g. Germany); What I sell (e.g. process-mining add-on for SAP)

### Detailed prompt

```text
Act as my platform-alliances and marketplace analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Platform: [Product we integrate with, as Draup names it, e.g. SAP S/4HANA]
- Competitor: [Maker of the rival add-on whose products must be absent, e.g. Celonis]
- Vertical: [Draup industry, e.g. Automotive]
- Country: [HQ country in full, e.g. Germany; default: my territory from setup]
- What I sell: [One line, e.g. process-mining add-on for SAP; skip if saved in setup]

STEPS
1. Turn the inputs into Draup's exact names; say which you used.
2. Size the list: companies with primary industry [Vertical], HQ in [Country], [Platform] in their tech stack and no product made by [Competitor] anywhere in the stack. Band the total: request single rows at positions 10, 50, 100 and 250; the last that returns a company sets the band.
3. Band again without the [Competitor] condition, labelled, to show what share of [Platform] users show no rival.
4. Pull the top 10 with full detail, by revenue: workforce, revenue, Opportunity Index, parent, main providers.
5. Flag: Subsidiary (name the parent; the add-on may be bought centrally), Misfiled, Possibly inactive.
6. For the top 3 unflagged, confirm the platform: pull the platform maker's products in the platform's exact category only (e.g. "Enterprise Resource Planning Software (ERP)" for S/4HANA), with usage strength and last seen. A maker-only pull can cut the platform off.
7. People and timing: for the same 3, pull the top leader in the function closest to [What I sell] (full profile title) and the most important news item from the last 90 days where the company is the actor.

OUTPUT
- Bottom line: 2 sentences — list size and the account to take to the platform vendor first.
- Recommended next step: a person from step 7 (name and title), what to do (often with the platform vendor's partner manager), and the dated why-now; if none, say so.
- Header line: "[Band] run [Platform] with no [Competitor] products; [band] run [Platform] in total."
- "Attach list" (top 10): Rank | Company | Revenue (USD M, FY) | Parent | Flag.
- "Top 3 confirmed": Company | [Platform] strength and last seen | Why now (dated) | Likely owner (name, title) | Opener angle.
- Gaps: what Draup didn't have — worth asking the platform vendor.
- Detail: workforce and Opportunity Index per row; "Likely missing big names" (up to 3, labelled "probably runs [Competitor]; not checked").

RULES
- "No [Competitor] products" means Draup sees no public evidence of them; say "no sign of", never "doesn't use".
- If [Platform] isn't confirmed or was last seen over 12 months ago (editable default), drop the company from the top 3 and say why.
- Shareholding notices and recalls are not a why-now.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust usage strength and last-seen date, not confidence or first-seen; ignore "Generic" rows; a rival counts only at High or Medium usage.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Parent companies only; merge subsidiaries and alternate names of one company.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 430 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step (named owner, dated why-now) first. Which [Vertical] companies in [Country] run [Platform] with no [Competitor] products? Band the total vs all [Platform] users, show the top 10 by revenue, confirm the top 3.
```

### Follow-ups

- Show rows 11–20 the same way.
- Draft a short note to the platform vendor's partner manager proposing a joint campaign on the top 10 (check our Draup licence before sharing the list).
- For the top 3, who else owns [Platform] there? Show leaders with full titles.

### Tips

- Platform vendors respond to lists that help them sell their own platform. Lead with accounts where the platform is current and something just changed.
- If the list is mostly mid-size companies, that's often where rival add-ons haven't landed yet. Size your campaign for that segment.

## Enablement brief for a partner's sellers

- **id:** `partners-enablement-brief`
- **What you get:** A brief you hand to a partner's sales team: where your product fits their practice in your industry, which of their customers run your platform or a rival's, a joint value proposition, 5 qualification questions and 3 objection handlers.
- **Use it when:** After a partner agreement is signed, before a joint enablement session or a partner sales kickoff.
- **Best for:** Partnerships & Alliances, Marketing & ABM, Presales & Solutions
- **Time:** 4–6 min
- **Inputs:** Partner (e.g. Infosys); Vertical (e.g. Banking & Financial Services); Platform (e.g. Snowflake); Competitor (e.g. Databricks); What I sell (e.g. data observability for Snowflake); Proof point (optional) (e.g. cut data-incident time 40% at a mid-size retailer)

### Detailed prompt

```text
Act as my partner enablement lead. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Partner: [Services firm as Draup spells it, e.g. Infosys]
- Vertical: [Draup industry, e.g. Banking & Financial Services]
- Platform: [The technology our product runs on or with, as Draup names its maker, e.g. Snowflake]
- Competitor: [Rival maker, e.g. Databricks]
- What I sell: [One line, e.g. data observability for Snowflake; skip if saved in setup]
- Proof point (optional): [e.g. cut data-incident time 40% at a mid-size retailer]

STEPS
1. Confirm Draup's spelling of each input; say which you used.
2. Pull the partner's customer summary: active customers, engagements and top customers overall.
3. Pull the partner's top 10 workloads and top 10 customers in primary industry [Vertical].
4. Pull the partner's [Vertical] customers ranked by engagements that mention [Platform] (top 10): its practice evidence.
5. List the partner's [Vertical] customers whose stack includes [Platform] products (10, by revenue), then those of them with no [Competitor] products (10).
6. A customer in step 3 or 4 that also appears in step 5 is a warm start.
7. People and timing: page through [Partner]'s Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances, partnerships or [Platform]; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
(Written to the partner's sellers, as "you".)
- Bottom line: 2 sentences — where [What I sell] fits their [Vertical] practice and the first 3 customers to raise it with.
- Recommended next step: a person from step 7 (name and title), what I (the partner manager) do, and the dated why-now; if none, say so.
- "Where to start" (up to 10): Customer | Your engagements in [Vertical] | Your [Platform]-related engagements | Stack: [Platform] only, both, or not seen | Play.
- Play: Expand (you already do [Platform] work there), Land ([Platform] present, no [Competitor], little [Platform] work by you), Coexist (both makers present: position alongside).
- "5 qualification questions": Question | What a good answer sounds like.
- Gaps: what Draup didn't have — worth confirming with the partner.
- Detail: why this fits your practice (3 bullets on their workload numbers); joint value proposition (60 words, [Proof point] once); 3 objection handlers (Objection | Response under 40 words | Proof); how to bring us in (routing line).

RULES
- Platform presence is public evidence; confirm before quoting.
- These are outside-in facts; never imply a customer told us.
- Leave catch-all workloads out of "Why this fits".
- Under 10 [Platform]-related engagements (editable)? Call the practice early and lead with Land plays.
- Check our Draup licence before sharing Draup data outside the company.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Trust usage strength and last-seen date, not confidence or first-seen; ignore "Generic" rows; a rival counts only at High or Medium usage.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 500 words including tables, then offer more.
```

### Quick version

```text
Bottom line and first 3 customers first. Enablement brief for [Partner]'s sellers in [Vertical]: their workloads and customers, who runs [Platform] (with or without [Competitor]), a joint pitch, 5 qualification questions, 3 objection handlers.
```

### Follow-ups

- Turn the brief into a 5-slide outline for the enablement session.
- Write a 90-second talk track a partner seller can use on a customer call.
- Build a joint account plan for the top warm-start customer with [Partner].

### Tips

- Lead with the partner's own customers and workloads. Partner sellers skim past vendor-centric decks.
- Keep the brief to what a seller can use on the next call; save the deep data for the partner manager.

## Compare candidate partners head to head

- **id:** `partners-compare-candidates`
- **What you get:** A weighted scorecard comparing 2–3 candidate partners in one industry and country on workload depth, technology experience, customer breadth, onshore delivery and momentum, with a pick, each candidate's main risk and who to call at the pick.
- **Use it when:** You have budget or capacity for one new partner in a segment and need to choose, or justify the choice to your leadership. Use "Which SIs to recruit in an industry" instead when you don't have names yet.
- **Best for:** Partnerships & Alliances, Sales Leader & RevOps
- **Time:** 4–6 min
- **Inputs:** Candidates (e.g. Cognizant, Capgemini, Wipro); Vertical (e.g. Life Sciences); Country (e.g. United States of America); Workload (e.g. Data Engineering); Technology (e.g. Databricks); Weights (optional) (e.g. workload 30, technology 25, breadth 20, onshore 10, momentum 15); What I sell (e.g. clinical data platform)

### Detailed prompt

```text
Act as my partner-selection analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Candidates: [2–3 services firms as Draup spells them, e.g. Cognizant, Capgemini, Wipro]
- Vertical: [Draup industry, e.g. Life Sciences]
- Country: [Customer HQ country in full, e.g. United States of America]
- Workload: [e.g. Data Engineering; a business function is fine, I'll map it]
- Technology: [Our platform or a rival's, e.g. Databricks]
- Weights (optional): [Editable default: workload depth 30, technology 25, customer breadth 20, onshore delivery 10, momentum 15]
- What I sell: [One line, e.g. clinical data platform; skip if saved in setup]

STEPS
1. Confirm Draup's spelling of each candidate; list any sister brand separately, unmerged. If I gave a business function, map it to its 1–2 main workloads.
2. In one lookup, pull engagements for all candidates among customers with primary industry [Vertical] and HQ in [Country]. Repeat once for [Workload] only, and once for engagements that mention [Technology].
3. For each candidate, pull its top 5 customers in the segment; compute its top-2 customers' share of its segment engagements.
4. For each candidate, pull delivery locations for the segment; compute the share delivered in [Country] (onshore).
5. For each candidate, pull headcount growth over Draup's latest 12-month workforce window.
6. Score each criterion 0–100 relative to the best candidate (best = 100, others = value ÷ best × 100). For customer breadth, use 100 minus the top-2 share before scaling. Apply the weights and total.
7. People and timing: page through the pick's Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances, partnerships or [Technology]; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
- Bottom line: 2 sentences — the pick and what it means for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and the dated why-now; if none, say so.
- "Scorecard": Criterion | Weight | one column per candidate, raw value (score) | Total row. Criteria: Workload depth ([Workload] engagements in segment), Technology ([Technology]-related engagements), Customer breadth (top-2 share), Onshore delivery (% in [Country]), Momentum (headcount growth %).
- "Pick": one candidate, 3 reasons tied to numbers.
- "Risk per candidate": one line each (e.g. concentration, offshore-heavy, thin technology work).
- Gaps: what Draup didn't have — worth asking each candidate.
- Detail: "Sensitivity" (does the pick change if the technology weight doubles? who wins then) and "If you can sign two" (the most complementary pair and why).

RULES
- Under 10 segment engagements (editable)? Mark its share-based scores "insufficient data" and score them 0.
- Say plainly when the pick is driven mainly by scale, and show the runner-up's strongest criterion.
- The scorecard is my weighted read of Draup data, not Draup's rating.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

### Quick version

```text
Bottom line and next step (named leader at the pick, dated why-now) first. Compare [Candidates] in [Vertical], [Country]: engagements in [Workload] and mentioning [Technology], top-2 customer share, onshore share, headcount growth. Weighted scorecard, pick, sensitivity check, each one's risk.
```

### Follow-ups

- Rerun the scorecard with technology weighted 40 and workload 20.
- Run the momentum check on the pick before we sign.
- Draft a one-paragraph recommendation for my VP with the scorecard attached.

### Tips

- Change the weights before you look at the result, not after. It keeps the choice honest.
- A firm with most of its segment work at one or two customers can still be the right partner, but only if those customers are on your target list.
