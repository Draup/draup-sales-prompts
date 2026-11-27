[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find accounts ripe for ER&D services

> **A ranked list of companies in your industry and territory most ready to buy engineering and R&D services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building an engineering and R&D services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for ER&D services?" instead when you already have one account. | Account Executive, SDR / BDR, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller | Services sellers | 6–10 min | Outsourcing deals, Hiring & job postings, Priorities & opportunities, News signals, Company directory, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Industry]` | Automotive |
| `[Territory (optional)]` | Germany |
| `[Workloads (optional)]` | a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development |
| `[What I sell]` | embedded and product engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my engineering and R&D services target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Automotive]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. Germany]
- Workloads (optional): [a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development]
- What I sell: [one line, e.g. embedded and product engineering services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry, workloads and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in the ER&D function, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in [Workloads]; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop engineering-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers; postings per 1,000 employees.
6. Top 5 by provisional score: each one's providers in [Workloads], captives marked; top 3: up to 3 ER&D priorities.
7. One news search across the top 5 on R&D programmes, engineering centres or new platforms, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in ER&D.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Provider mix 0–3 (3 = top 3 under 60% excluding captives, or a new centre in 12 months; 2 = 60–80%; 1 = over 80%; 0 = captives only); Hiring 0–3 (ER&D postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Priority 0–2 (2 = R&D programme shift in the last 4 fiscal quarters, 1 = older, 0 = none); Outsourcing 0–1 (top third); News 0–1.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Captives (names containing the company's name) are in-house. Rate services rivals from my setup at the top 3 by share of engagements in [Workloads]: 30%+ Red, 10–29% Amber, under 10% Green.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (engineering services); list them under Dropped.
- Postings are openings, not hires; engagements are Draup estimates.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for engineering and R&D services on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run "Is this account ready for ER&D services?" on the #1 account.
```

```text
Show the next 10 companies with the same scoring.
```

```text
Write a 70-word opener for each of the top 3, each tied to its why-now.
```

```text
Which of these use a rival I name? Rate each Red, Amber or Green: software rivals by usage (Low or absent = Green), services rivals by engagement share (30%+ Red, 10–29% Amber, under 10% Green).
```

## Tips for better results

- Ranking on postings per 1,000 staff often reorders the list completely; mid-size players can outrank the giants.
- Hiring by the ER&D function is broader and more reliable than niche engineering workloads.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Related prompts

- [Is this account ready for ER&D services?](../../prompts/07-solution-plays/erd-readiness.md): A 0–20 readiness score for engineering and R&D services at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.
- [Find who hires hardest in a vertical](../../prompts/14-industry-intelligence/hiring-leaders.md): The real end employers hiring hardest in an industry, ranked on postings per 1,000 staff with recruiters and outliers removed, plus hot spots and a named person to call first.
- [Find the biggest buyers of my service](../../prompts/10-outsourcing-and-services/offering-to-buyers.md): Your offering mapped to Draup workloads you approve, then the 20 companies in your territory that outsource them most, their incumbents, where the provider mix is fragmented, and who to call first.
- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_top_companies_v3`, `get_deals_customer_v3`, `get_universe_companies_v3`, `get_account_priorities_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_deals_service_provider_v3`

Status: **tested live**. Prompt id: `plays-erd-targets`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
