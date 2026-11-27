[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find accounts ripe for generative AI

> **A ranked list of companies in your industry and territory most ready to buy generative AI, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a generative AI platform, AI-agent or AI services campaign, an SDR list or next quarter's targets in one industry. Use this to find accounts; use "Is this account ready for generative AI?" instead when you already have one account. | SDR / BDR, Account Executive, Sales Leader & RevOps, Marketing & ABM, Services, SI & Staffing Seller | Everyone | 6–10 min | Hiring & job postings, Outsourcing deals, Company directory, Tech stack, Priorities & opportunities, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Industry]` | Insurance |
| `[Territory (optional)]` | United Kingdom |
| `[What I sell]` | generative AI implementation and AI agent services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my generative-AI target-list analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Industry: [e.g. Insurance]
- Territory (optional): [HQ country in full; default: my territory from setup, e.g. United Kingdom]
- What I sell: [one line, e.g. generative AI implementation and AI agent services — skip if you ran the start-here prompt]

STEPS
1. Resolve industry and territory to Draup's names; say which. Industry fails: retry each part (split on "/" or "and"), then a member company's primary industry.
2. Hiring: top 20 end employers in [Territory], primary industry [Industry], by postings in postings naming Generative AI, Large Language Models, Prompt Engineering or Retrieval Augmented Generation, 12 months, no staffing firms or job boards.
3. Outsourcing: [Industry] companies HQ'd in [Territory] ranked by active engagements in Artificial Intelligence & Data Science; top 15.
4. Long list of 10, both lists first: merge subsidiaries into parents; drop AI vendors and IT-services firms, investors, off-industry rows and foreign firms' local teams.
5. One company-list lookup for the 10 by website: workforce, revenue, providers, AI and machine-learning tools only, marking GenAI platforms (hosted models, copilots, agents, retrieval); postings per 1,000 employees.
6. Top 5 by provisional score: up to 5 Generative AI priorities each (if none, Artificial Intelligence & Data Science; say so).
7. One news search across the top 5 on GenAI launches, AI agents or AI partnerships, last 90 days; else each one's most material dated event, labelled indirect.
8. Top 3: 3 executives each in Artificial Intelligence & Data Science.

OUTPUT
- Bottom line: 2 sentences — who leads and what it means for [What I sell].
- Recommended next step: the #1 account's person (name, full title), the action and the dated why-now; if missing, the title to find.
- "Ranked targets" (top 10): Rank | Company | Score /10 | Why now (dated) | Who to call (top 3: name, full title, angle).
- Gaps: what Draup didn't have.
- Detail: score breakdown with evidence and postings per 1,000; Dropped (company, reason); local teams.

Score (editable): Priority 0–3 (3 = GenAI or agentic priority in the last 4 fiscal quarters, 2 = AI without GenAI, 1 = older AI priority, 0 = none); Hiring 0–3 (postings per 1,000 by thirds: 3, 2, 1; none 0; under 5,000 staff, at most 2); Stack 0–2 (2 = two or more GenAI platforms, 1 = one); News 0–1 (dated launch); Outsourcing 0–1. Stage in Detail: Scaling, Piloting or Exploring.

RULES
- Rank by score, ties by postings per 1,000, never raw postings or IT spend (no workforce figure: raw postings, say so).
- Classic analytics or machine-learning tools alone are not GenAI evidence; drop generic chat widgets.
- Sells it, not buys it: drop companies whose matching priorities or news describe products they sell (AI software or platforms); list them under Dropped.
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
Bottom line and next step first: rank [Industry] companies in [Territory] for generative AI on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run "Is this account ready for generative AI?" on the #1 account.
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
- Tools without a priority often mean pilots stuck short of production, which is a strong services opening.
- Check Dropped and the local-teams list: big names misfiled under another industry or HQ'd abroad land there.

## Related prompts

- [Is this account ready for generative AI?](../../prompts/07-solution-plays/genai-readiness.md): A 0–20 readiness score for generative AI at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.
- [AI readiness against close peers](../../prompts/11-account-planning/ai-readiness.md): A read on the account's AI hiring, priorities, new tools and outsourced AI work, its AI hiring compared with up to 4 close peers, and who to raise it with.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.
- [Who's hiring for a tech or role](../../prompts/06-prospecting-and-lists/hiring-led-list.md): The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.
- [Build an industry point of view](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `talent_demand_top_companies_v3`, `get_deals_customer_v3`, `get_universe_companies_v3`, `get_account_priorities_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `plays-genai-targets`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
