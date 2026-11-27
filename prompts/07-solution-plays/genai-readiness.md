[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this account ready for generative AI?

> **A 0–20 readiness score for generative AI at one account, with incumbents rated Red, Amber or Green, a named owner with a dated why-now, an entry angle and four fact-based discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before investing pursuit time in one account for a generative AI platform, AI-agent or AI services deal, or ahead of a first meeting. Use the matching target-list prompt instead to find accounts. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Account & Customer Success Manager | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Tech stack, Hiring & job postings, Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | allianz.com |
| `[Competitor or incumbent (optional)]` | Accenture |
| `[What I sell]` | generative AI implementation and AI agent services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my generative-AI account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. allianz.com]
- Competitor or incumbent (optional): [e.g. Accenture]
- What I sell: [one line, e.g. generative AI implementation and AI agent services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website; confirm it is the parent, not a subsidiary or sister company (ask if unsure). If it sells AI products, drop its own products throughout.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 priorities in the Generative AI technology area (if fewer than 3, add Artificial Intelligence & Data Science and say so), newest first, with linked tools and providers.
4. Current state: AI and machine-learning products with usage and last seen; mark GenAI platforms, copilots, agent frameworks and retrieval tools, and the 1–2 platforms they build on.
5. Capability: the top 15 skills in AI and data-science postings; call out GenAI, model-provider and governance skills; last 5 full months vs the 5 before.
6. Incumbents: providers ranked by Artificial Intelligence & Data Science engagements at [Company], top 10. If I named a competitor, check the whole stack for its products, any category.
7. Owner: executives in Artificial Intelligence & Data Science; keep AI, data, digital, CTO or CDO titles; check titles against the function; no senior owner: widen once to Chief, EVP and CIO titles. If news names a different leader, say so.
8. Why now: the most important 90-day news where [Company] is the actor, on GenAI, AI agents, AI investments and partnerships; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: a named person (name, full title; step 7), the action and the dated why-now (step 8); if missing, name the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Stated intent, Platform maturity, Skills and governance, Money committed, Delivery gap (4 = intent and platform ahead of hiring or partners).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: my competitor's product installed with High usage in my workloads = Red; Medium, or first seen in 12 months (newly detected) = Amber; else Green (open door).
- "Entry angle": 2 sentences tied to one priority and one gap. "Discovery questions": 4 one-liners, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: GenAI stack (Product | Type | Usage | Last seen).

RULES
- Classic analytics or ML tools alone are not GenAI evidence. A model-provider skill shows intent to use it, not a contract.
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
Bottom line and next step first: score [Company]'s readiness for generative AI (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
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
Show the 10 most recent GenAI postings with title, date and tools named.
```

```text
Re-score after I tell you what I learned in discovery.
```

## Tips for better results

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Model-provider names appearing as skills in job ads are often the clearest sign of which platform a company has picked.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Related prompts

- [Find accounts ripe for generative AI](../../prompts/07-solution-plays/genai-targets.md): A ranked list of companies in your industry and country most ready to buy generative AI, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- [AI readiness against close peers](../../prompts/11-account-planning/ai-readiness.md): A read on the account's AI hiring, priorities, new tools and outsourced AI work, its AI hiring compared with up to 4 close peers, and who to raise it with.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.
- [What tools they adopted this year](../../prompts/03-tech-stack-and-displacement/recent-adoptions.md): The tools first detected at the account in the last 12 months, labelled as competing with, complementing or unrelated to what you sell, with any new competitor product flagged Amber first and a named person to call.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_demand_category_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plays-genai-readiness`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
