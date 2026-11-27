[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find accounts ripe for cybersecurity

> **A ranked list of companies in your industry and country most ready to buy cybersecurity, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a security platform, managed security or security consolidation campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use the matching readiness check instead when you already have one account. | SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM | Everyone | 6–10 min | Hiring & job postings, Outsourcing deals, News signals, Company directory, Tech stack, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Industry]` | Hospitals & Healthcare Services |
| `[Country]` | United States of America |
| `[What I sell]` | managed detection and response and identity security |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my cybersecurity target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Hospitals & Healthcare Services]
- Country: [HQ country in full, e.g. United States of America]
- What I sell: [one line, e.g. managed detection and response and identity security — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and country to Draup's names and say which you used; if empty, try a member company's primary industry.
2. Hiring: end employers in [Country], primary industry [Industry], posting most in the Cybersecurity workload, 12 months, no staffing firms or job boards; top 20.
3. Outsourcing: [Industry] companies HQ'd in [Country] ranked by active engagements in Cybersecurity; top 15.
4. Incidents: one news search for breaches or ransomware at [Industry] companies in [Country], last 90 days; add up to 3 named companies.
5. Long list of 10: companies in both lists first. Merge subsidiaries into parents; drop security vendors, managed-security providers and IT-services firms, investors, off-industry rows and foreign companies' local teams.
6. One company-list lookup for the 10 by website: workforce, revenue, providers, and only security tools; note legacy on-premise tools and 3+ overlapping tools in one job (firewall, endpoint, SIEM, identity); work out postings per 1,000 employees.
7. Top 5 by provisional score: up to 5 priorities each in the Cybersecurity workload; if none, try the Cybersecurity technology area once.
8. One news search across the top 5 on breaches, regulatory actions, security leadership changes or acquisitions, last 90 days; if nothing fits, use each company's most material dated event, labelled indirect.
9. Top 3: 3 executives each in Cybersecurity; no senior owner: widen once to Chief, EVP and CIO titles.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title; step 9), the action and the dated why-now (step 8); if missing, name the title to find.
- "Ranked targets" (top 10): Rank | Company | Postings per 1,000 staff | Score /10 | Why now (dated).
- "Who to call" (top 3): Company | Person (name, full title) | Opening angle.
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence; Dropped (company, reason); local teams.

Score (editable): Incident 0–3 (3 = own incident in 90 days; 1 = earlier in 12 months); Hiring 0–3 (thirds by postings per 1,000); Stack 0–2 (legacy on-premise or 3+ overlapping tools); Outsourcing 0–1 (3+ engagements); Priority 0–1.

RULES
- Each point traces to a Detail cell. Rank by score, ties by postings per 1,000; never by raw postings or IT spend (no workforce figure: use raw postings, say so).
- Use incident facts as published; never speculate on cause, attacker or impact. Openers lead with help or a peer pattern, never the breach.
- Named competitors (here or in setup): check the top 3's stacks; High usage = Red, Medium or first seen in 12 months = Amber.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: rank [Industry] companies in [Country] for cybersecurity on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run the readiness check on the #1 account.
```

```text
Show the next 10 companies with the same scoring.
```

```text
Write a 70-word opener for each of the top 3, each tied to its why-now.
```

```text
Which of these run a competitor I name? Rate each Red, Amber or Green.
```

## Tips for better results

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- A breach at a close peer is often as useful as one at the account: boards ask 'could that be us?'.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Related prompts

- [Is this account ready for security investment?](../../prompts/07-solution-plays/cyber-readiness.md): A 0–20 readiness score for cybersecurity at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.
- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of companies in your industry and country whose stack includes a competitor's products, with usage strength shown, distributors and inactive names flagged, and a named person at the top account.
- [A rival's customers you can win](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_top_companies_v3`, `get_deals_customer_v3`, `get_universe_companies_v3`, `get_account_priorities_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `plays-cyber-targets`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
