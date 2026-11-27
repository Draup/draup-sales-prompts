[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this account ready for ER&D services?

> **A 0–20 readiness score for engineering and R&D services at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before investing pursuit time in one account for an engineering and R&D services deal, or ahead of a first meeting. Use "Find accounts ripe for ER&D services" instead to find accounts. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Services sellers | 4–6 min | Company & financials, Outsourcing deals, Priorities & opportunities, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | bosch.com |
| `[Workloads (optional)]` | a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development |
| `[Competitor or incumbent (optional)]` | LTTS |
| `[What I sell]` | embedded and product engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my engineering and R&D services account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. bosch.com]
- Workloads (optional): [a type of work, default Embedded & Firmware Engineering, Vehicle Electronics, Mechanical Design & Development]
- Competitor or incumbent (optional): [e.g. LTTS]
- What I sell: [one line, e.g. embedded and product engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated R&D spend and growth.
3. Intent: up to 6 ER&D priorities plus up to 3 named "engineering", newest first.
4. Current state: engineering providers ranked by active engagements in [Workloads]; captives (names containing the company's name) are in-house.
5. Capability: ER&D postings by workload, flagging [Workloads] that slow while priorities grow; last 5 full months vs the 5 before.
6. Incumbents: the top 10 providers from step 4, captives left out of share. Check any rival I named across the whole stack.
7. Owner: executives in ER&D; keep engineering, R&D or CTO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on R&D programmes, engineering centres or new platforms; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (R&D programme shift), Momentum (4 = ER&D postings rising; 0 = falling), Provider mix (4 = top 3 under 60% excluding captives), Budget (R&D spend growing), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: provider landscape with captives marked; R&D spend (Draup-estimated).

RULES
- Captives are never rivals. Private with no revenue or R&D spend: "Not in Draup", Budget 2. If [Workloads] return little, use step 5's top ER&D workloads and say so.
- Competitor absent: analyse who is there. Big company, thin data: say "in-house or thin data", not Early.
- Products show footprint, not spend (say "fading", never "dropped"); engagements are Draup estimates, not contracts.

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
Bottom line and next step first: score [Company]'s readiness for engineering and R&D services (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
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
Which incumbent is weakest in the workloads I lead? Show its footprint.
```

```text
Re-score after I tell you what I learned in discovery.
```

## Tips for better results

- Add your rival or the incumbent you replace: finding it, or not, is often the deciding line.
- Captive engineering centres take new work first; find out what they can't absorb.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Related prompts

- [Find accounts ripe for ER&D services](../../prompts/07-solution-plays/erd-targets.md): A ranked list of companies in your industry and territory most ready to buy engineering and R&D services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_demand_category_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plays-erd-readiness`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
