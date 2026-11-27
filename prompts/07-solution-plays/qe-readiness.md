[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this account ready for QE services?

> **A 0–20 readiness score for quality engineering and testing at one account, with incumbents rated Red, Amber or Green (services rivals by share of engagements), a named owner with a dated why-now, an entry angle and four fact-based discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before investing pursuit time in one account for a quality engineering and testing deal, or ahead of a first meeting. Use "Find accounts ripe for QE services" instead to find accounts. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Services sellers | 4–6 min | Company & financials, Tech stack, Priorities & opportunities, Hiring & job postings, Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | ford.com |
| `[Workloads (optional)]` | a type of work, default Software Testing, Quality Assurance |
| `[Competitor or incumbent (optional)]` | Wipro, or Tricentis |
| `[What I sell]` | test automation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my quality-engineering account strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. ford.com]
- Workloads (optional): [a type of work, default Software Testing, Quality Assurance]
- Competitor or incumbent (optional): [e.g. Wipro, or Tricentis]
- What I sell: [one line, e.g. test automation services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name, show the match score); confirm it's the parent (ask if unsure). If it sells technology or services, drop priorities, news and hiring about its own products.
2. Money: latest revenue and growth, and Draup-estimated IT spend (direction only).
3. Intent: up to 6 IT and ER&D priorities plus up to 3 named "quality", software quality only, newest first.
4. Current state: the testing stack for [Workloads], up to 30 rows, no manufacturing quality tools; High or Medium usage in 6 months = core.
5. Capability: testing postings in IT and ER&D (under 60 a year = small in-house team); last 5 full months vs the 5 before.
6. Incumbents: providers in [Workloads] ranked by active engagements, top 10; joint ventures and captives are in-house. Check any rival I named across the whole stack.
7. Owner: executives in [Workloads], then IT; keep testing or quality titles. If news names a different leader, say so.
8. Why now: the top 90-day news where [Company] is the actor, on software recalls or outages, release failures or core-system changes; if none, widen to 6 months and say so.

OUTPUT
- Bottom line: 2 sentences — verdict (Ready now 15+, Warming 10–14, Early under 10), score /20, and what it means for [What I sell].
- Recommended next step: the owner (name, full title), the action and the dated why-now; if missing, the title to find.
- "Readiness score": Dimension | Dated evidence | Score (0–4). Dimensions (editable): Need, Momentum (4 = testing postings or releases rising; 0 = falling), Change window (a fading commercial tool or a recent software recall), Budget (cost programme), Trigger.
- "Incumbents": Vendor or provider | Footprint | Rating | Read. Rating: a services rival by share of active engagements in my workloads (30%+ Red, 10–29% Amber, under 10% Green); a software rival by usage (High Red; Medium or new in 12 months Amber; Low or absent Green; say if Low was ignored).
- "Entry angle": 2 sentences on one priority and one gap. "Discovery questions": 4, each opening with a dated fact.
- Gaps: what Draup didn't have.
- Detail: current state (Tool | Maker | Usage | Last seen | Read).

RULES
- Recalls or outages count only when tied to software; plant quality goes in Entry angle.
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
Bottom line and next step first: score [Company]'s readiness for quality engineering and testing (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
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
- A software recall or failed over-the-air update is the strongest testing trigger; lead with help, not the incident.
- A low score with a strong trigger is usually worth a call; a high score with no trigger is a nurture.

## Related prompts

- [Find accounts ripe for QE services](../../prompts/07-solution-plays/qe-targets.md): A ranked list of companies in your industry and territory most ready to buy quality engineering and testing, scored 0–10 and ranked on hiring per 1,000 staff, with a named person to call at the top 3 and a dated why-now.
- [Fading tools and replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_demand_category_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plays-qe-readiness`.

</details>

---

[Back to Solution plays: by what you sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
