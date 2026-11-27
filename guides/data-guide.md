# Data guide

What each kind of Draup data contains, and how to read it so your answers are accurate.

## Company & financials

Profile, revenue, EBITDA, IT and R&D spend, forecasts, revenue by business unit and region, IT spend split, private funding.

Used by 22 prompts, for example: [One-page account brief](../prompts/01-account-research/account-brief.md), [10-minute pre-call snapshot](../prompts/01-account-research/precall-snapshot.md), [Is their budget growing or shrinking?](../prompts/01-account-research/budget-posture.md), [Which region should own this account](../prompts/01-account-research/buying-center.md).

## Earnings calls & filings

Earnings-call and press-call transcripts with speakers, plus annual filings for US-listed companies.

Used by 3 prompts, for example: [Their leaders' own words on [Topic]](../prompts/01-account-research/proof-points.md), [Numbers from the latest call](../prompts/01-account-research/numbers-from-the-call.md), [What changed between two calls](../prompts/01-account-research/call-over-call.md).

## Priorities & opportunities

Stated initiatives from earnings calls and news, by function and workload, with the tech and service providers attached; Draup-generated entry points.

Used by 26 prompts, for example: [One-page account brief](../prompts/01-account-research/account-brief.md), [10-minute pre-call snapshot](../prompts/01-account-research/precall-snapshot.md), [Which priority to anchor your pitch on](../prompts/01-account-research/priorities-by-function.md), [What changed between two calls](../prompts/01-account-research/call-over-call.md).

## Executives & movement

Key executives with level, budget control, workloads, past companies and LinkedIn; recent hires, promotions and exits.

Used by 15 prompts, for example: [Which region should own this account](../prompts/01-account-research/buying-center.md), [Private company funding](../prompts/01-account-research/private-funding.md), [Map the buying committee](../prompts/02-buyers-and-stakeholders/buying-committee.md), [New leaders in the last 6 months](../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md).

## Tech stack

Products in use with last-seen dates and usage strength, vendor landscape per workload, products adopted in the last 12 months.

Used by 20 prompts, for example: [Account SWOT, outside-in](../prompts/01-account-research/swot.md), [Who uses [Technology] there](../prompts/02-buyers-and-stakeholders/personas-by-tool.md), [Hypothesis-led discovery questions](../prompts/02-buyers-and-stakeholders/discovery-questions.md), [Pre-fill MEDDPICC from outside-in data](../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md).

## Hiring & job postings

Posting volume and monthly trend, skills trending up or down, full job descriptions, market-wide 'who is hiring for X'.

Used by 21 prompts, for example: [10-minute pre-call snapshot](../prompts/01-account-research/precall-snapshot.md), [Private company funding](../prompts/01-account-research/private-funding.md), [Account SWOT, outside-in](../prompts/01-account-research/swot.md), [Who uses [Technology] there](../prompts/02-buyers-and-stakeholders/personas-by-tool.md).

## Talent flow & locations

Hiring, attrition and net change by month, company and metro; key locations with HQ, GCC and new-site flags.

Used by 8 prompts, for example: [Account SWOT, outside-in](../prompts/01-account-research/swot.md), [Are they really investing in X?](../prompts/04-signals-and-timing/investing-in-x.md), [Is work coming back in-house? (re-insourcing risk)](../prompts/06-outsourcing-and-services/reinsourcing-risk.md), [Global capability centres (GCCs) and the services play](../prompts/06-outsourcing-and-services/gcc-opportunity.md).

## News signals

Account and market news by category: M&A, layoffs, funding, expansion, executive moves, partnerships, product launches.

Used by 27 prompts, for example: [10-minute pre-call snapshot](../prompts/01-account-research/precall-snapshot.md), [Is their budget growing or shrinking?](../prompts/01-account-research/budget-posture.md), [Acquisitions, strategic bets and the openings they create](../prompts/01-account-research/acquisitions.md), [Account SWOT, outside-in](../prompts/01-account-research/swot.md).

## Outsourcing deals

Customer-to-provider engagements: who outsources which workloads to whom, relationship tier, delivery locations.

Used by 18 prompts, for example: [Pre-fill MEDDPICC from outside-in data](../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md), [Who's already working each priority](../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md), [Outsourcing footprint and incumbents](../prompts/06-outsourcing-and-services/outsourcing-footprint.md), [A competitor's footprint at an account](../prompts/06-outsourcing-and-services/competitor-at-account.md).

## Industry ecosystem

Industry revenue, IT and R&D spend, priorities, fast-growing tech, top vendors and outsourcers, growing and shrinking companies, startups, talent hubs.

Used by 12 prompts, for example: [Which region should own this account](../prompts/01-account-research/buying-center.md), [Growing and shrinking companies: scale vs cost-out buyers](../prompts/05-prospecting-and-lists/growth-and-cost-out.md), [Startups with real momentum](../prompts/05-prospecting-and-lists/startups.md), [Biggest logos in my territory](../prompts/05-prospecting-and-lists/territory-logos.md).

## Company directory

List building and market sizing by industry, HQ, size, technology, service providers and outsourced workloads.

Used by 13 prompts, for example: [Displacement target list](../prompts/03-tech-stack-and-displacement/displacement-list.md), [Build and size an ICP list](../prompts/05-prospecting-and-lists/icp-list.md), [Look-alikes of a best customer](../prompts/05-prospecting-and-lists/lookalikes.md), [Benchmark an account against peers](../prompts/05-prospecting-and-lists/peer-benchmark.md).

## Talent cost & supply

Base pay by role and city, talent pool size and growth, hiring difficulty, layoffs, employer brand (Draup for Talent connector).

Used by 7 prompts, for example: [Offshore cost case (base-pay gap)](../prompts/10-talent-cost-and-location/offshoring-cost-case.md), [Where to put a delivery team](../prompts/10-talent-cost-and-location/delivery-location.md), [Hard-to-hire roles: staffing pitch](../prompts/10-talent-cost-and-location/hard-to-hire.md), [Layoffs: outsourcing trigger](../prompts/10-talent-cost-and-location/layoff-pool.md).

## Reading the data well

These notes come from testing every prompt against live Draup data. The detailed prompts already apply them for you; they're here so you can read answers with confidence.

| Topic | What to know |
|---|---|
| Company match | Use the website. Large groups have subsidiaries and regional units with similar names; confirm Claude picked the parent. |
| Financials | Annual figures in the company's reporting currency and fiscal year, shown in millions. Draup supplies a conversion rate, so ask for USD when comparing companies. A drop can be a divestment or restatement rather than a cut. |
| IT spend | A Draup estimate. For many companies it is modelled from revenue, so its growth often mirrors revenue growth. Use it for scale, not as a separate signal. |
| Regional revenue | Trust the latest year's percentages; older-year splits can be inconsistent. |
| Forecasts | Draup's modelled projection for next year, not company guidance. |
| Annual filings | Available for US SEC filers. For other companies, use their investor-relations site. |
| Earnings calls | Quarters are the company's fiscal quarters. Some "calls" are press briefings rather than analyst calls. |
| Priorities | Drawn from earnings calls and news, tagged with business function, workloads and quarter. The tech and service providers shown with a priority are linked by workload, not confirmed contracts. |
| Executives | A strong starting point. Read each person's full title rather than the seniority label, which can overstate level; in banking and consulting, VPs are mid-level. Some regional profiles may be restricted. Recent-movement data shows the latest few moves per type, so narrow by workload. |
| Tech stack | Rely on the last-seen date and usage strength. First-seen dates can be unreliable. "Generic" product rows are catch-alls. |
| Hiring | Trailing 12 months of job postings, updated continuously. Skills must match Draup's naming; the prompts ask Claude to pick from Draup's own skill list. |
| Talent flow | Built from professional profiles. It runs about three months behind and undercounts very large companies. |
| Locations | Site headcount is indicative and GCC tags can include plants. The prompts corroborate it with job postings at each site. |
| News signals | Categorised news with noise filtered by the prompts (outages, stock commentary, look-alike names). Some search results come without links; ask for the source and headline. |
| Outsourcing | Engagements between customers and service providers, with workloads, delivery locations and relationship tier. "Outsourced headcount" is a Draup estimate. Engagement records are Draup-derived, not published contracts. |
| Industry lists | Use the primary industry for clean lists; "any industry" includes companies with a secondary tag. Industry-level figures work for top-level industries; for a niche (e.g. airlines) the prompts fall back to the parent industry and say so. |
| Company directory | Very broad coverage, so a few listed companies may have closed or merged; the list prompts flag companies with no recent hiring as possibly inactive. Size filters leave out companies without a headcount figure, and the prompts tell you how many. To compare named companies, give their websites so Claude matches each one exactly. |
