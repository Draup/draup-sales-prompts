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
