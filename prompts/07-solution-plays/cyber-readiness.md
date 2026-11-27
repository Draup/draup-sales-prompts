[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this account ready for security investment?

> **A 0–20 readiness score for cybersecurity at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before investing pursuit time in one account for a security platform, managed security or security consolidation deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Tech stack, Hiring & job postings, Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | unitedhealthgroup.com |
| `[Competitor or incumbent (optional)]` | Palo Alto Networks |
| `[What I sell]` | managed detection and response and identity security |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my cybersecurity account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unitedhealthgroup.com]
- Competitor or incumbent (optional): [e.g. Palo Alto Networks]
- What I sell: [one line, e.g. managed detection and response and identity security — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure).
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in the Cybersecurity workload (if none, the Cybersecurity technology area once); keep security, identity, resilience or privacy priorities, newest first, with linked tools and providers.
4. Current state: security vendors ranked by products in the Cybersecurity workload, with top products; flag legacy on-premise tools and categories where 3+ vendors overlap (firewall, endpoint, SIEM, identity).
5. Capability: the top 15 skills in Cybersecurity postings; note incident-response and cloud-security skills; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by Cybersecurity engagements at [Company], top 10. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Cybersecurity; find the CISO or equivalent and anyone under a year in title; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on incidents, breaches, litigation, regulation, acquisitions or security leadership (check main subsidiaries too); if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Pressure (incident, litigation or regulation), Change (acquisition or new leader), Tool sprawl, Capacity gap, Stated intent.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Category | Vendors | Overlap or legacy flag).

RULES
- Use incident and litigation facts as published; never speculate on cause or impact, and never open outreach with them. Drop investor law-firm notices.
- Competitor absent: analyse who is there. Big company, thin data: say the work may be in-house or the data thin, not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

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
Bottom line and next step first: score [Company]'s readiness for cybersecurity (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Map the buying committee around the owner you found.
```

```text
Turn the entry angle into a 100-word email to the person in the next step.
```

```text
Show every security tool with usage strength and last seen, by category.
```

```text
Re-score after I tell you what I learned in discovery.
```

## Tips for better results

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Acquisitions are an underused security trigger: every integration brings identities, endpoints and networks to bring under control.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Related prompts

- [Find accounts ripe for cybersecurity](../../prompts/07-solution-plays/cyber-targets.md): A ranked list of companies in your industry and country most ready to buy cybersecurity, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.
- [What they run in one tech area](../../prompts/03-tech-stack-and-displacement/stack-category.md): What they run in one area, ranked by how central each tool is, with your competitors rated Red, Amber or Green, stale tools set aside and a named person to call.
- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_demand_category_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plays-cyber-readiness`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
