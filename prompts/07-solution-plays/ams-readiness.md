[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this account ready for AMS consolidation?

> **A 0–20 readiness score for AMS and IT managed services at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before investing pursuit time in one account for an AMS and IT managed-services deal, or ahead of a first meeting. Use "Find accounts ripe for AMS deals" instead to find accounts. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Services sellers | 4–6 min | Company & financials, Outsourcing deals, Priorities & opportunities, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Workloads (optional)]` | a type of work, default Application Development & Maintenance, Infrastructure Management System |
| `[Competitor or incumbent (optional)]` | Accenture |
| `[What I sell]` | application and infrastructure managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my AMS and IT managed-services account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. pfizer.com]
- Workloads (optional): [a type of work, default Application Development & Maintenance, Infrastructure Management System]
- Competitor or incumbent (optional): [e.g. Accenture]
- What I sell: [one line, e.g. application and infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth; Draup-estimated IT spend and split (direction only).
3. Intent: up to 6 IT priorities plus up to 3 named "cost", newest first.
4. Current state: providers ranked by active engagements in [Workloads], up to 50: count, top-3 share and long tail (1–2 engagements).
5. Capability: IT postings by workload (rising in-house hiring in an outsourced workload = re-insourcing flag); last 5 full months vs the 5 before.
6. Incumbents: the top 10 providers from step 4 with their share. Check any rival I named across the whole stack.
7. Owner: IT executives in [Workloads]; keep applications, infrastructure, CIO or CTO titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on separations, IT outsourcing, vendor consolidation, cost programmes or IT layoffs; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need (savings programme naming technology), Momentum (4 = no rising in-house hiring in outsourced workloads; 0 = strong re-insourcing), Fragmentation, Budget, Trigger (separation or cost programme).
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: provider landscape (Provider | Engagements | Share); captives separately.

RULES
- Drop agencies, staffing firms, "Self" and captives from provider counts (list captives separately). Never recommend catch-all workloads (Account Management).
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
Bottom line and next step first: score [Company]'s readiness for AMS and IT managed services (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
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

- Add your rival or the incumbent you replace: a services firm with 30% or more of the engagements is entrenched (Red), so plan a second-vendor entry, not a swap.
- A spin-off or business sale usually creates transition and application-split work for 12 to 24 months.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Related prompts

- [Find accounts ripe for AMS deals](../../prompts/07-solution-plays/ams-targets.md): A ranked list of companies in your industry and territory most ready to buy AMS and IT managed services, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- [How their vendor mix compares with peers](../../prompts/10-outsourcing-and-services/vendor-mix-benchmark.md): Where the account outsources more or less than its industry, which leading industry providers it doesn't use yet, and who to raise it with.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_revenue_by_it_spend_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_demand_category_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plays-ams-readiness`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
