[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Arm your champion to sell internally

> **A forwardable brief your champion can use to sell the deal inside: why now in their company's words, cost of waiting, answers for the CFO, CIO and procurement, a 150-word internal email, and who to route it to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a champion who supports the deal but needs ammunition to win budget or reach the economic buyer. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Hiring & job postings, News signals, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | 3m.com |
| `[Champion]` | Jane Doe, Director Supply Chain Analytics |
| `[Decision maker]` | SVP Global Supply Chain (optional) |
| `[Competitor or status quo]` | SAP IBP, or spreadsheets (optional) |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal coach who writes for champions. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Champion: [name and title, e.g. Jane Doe, Director Supply Chain Analytics]
- Decision maker (optional): [e.g. SVP Global Supply Chain]
- Status quo (optional): [e.g. SAP IBP, or spreadsheets]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
The pack must read as the champion's own argument, short enough to forward.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the champion's function; say which.
3. Their words: up to 6 function priorities with quarter and outcome; mark earnings-call ones.
4. Money: revenue and EBITDA growth.
5. Momentum: 12-month monthly function postings (rising, flat or falling).
6. Recent events, last 90 days (15+ items): investments, orders, cost actions, leadership moves.
7. Peer moves: 6 months of industry news where a named peer adopted what I sell.
8. Check the whole stack for any named status-quo tool's maker.
9. Decision maker: if I gave none, pick the likely economic buyer from the top 3 function executives (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the case the champion can make and what it means for [What I sell].
- Recommended next step: a named person (name, full title) the champion should route the pack to, the action this week and the dated why-now (or say none).
- "Why now": 3 bullets, each a dated fact plus implication; lead with an earnings-call priority if any.
- Table "If they ask…": Who (CFO, CIO, Procurement) | Answer | Fact behind it (dated).
- "Internal email": 150 words max, champion to decision maker, no vendor name in the first two sentences, a specific ask.
- "Cost of waiting": 2 bullets tied to stated outcomes.
- Detail: peer moves (or "No peer proof in Draup"), status-quo usage, "Don't say" (2 claims).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Write Why now and the email in the buyer's voice ("we", "our"); no superlatives about us.
- Priority outcome lines are Draup summaries, not verbatim quotes.
- A status-quo tool at High usage in my workloads is Red: frame us as an addition or phased swap; Medium is Amber; else Green.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low. Say "fading", never "dropped".
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 480 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Champion pack for [Champion] at [Company]. Lead with the case and the named decision maker to route it to before a dated event, then 3 dated why-now facts, CFO/CIO/procurement answers and a 150-word internal email.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the pack into a 3-slide internal deck the champion can present.
```

```text
Write the champion's talk track for a 5-minute slot in the staff meeting.
```

```text
What would the CFO's objections be? Answer each with a dated fact.
```

## Tips for better results

- Send the email draft to your champion as a suggestion, not a script; they'll edit it into their own voice.
- Earnings-call priorities carry the most weight internally because leadership said them in public.
- If peer proof comes back empty, swap in your own customer reference rather than stretching the evidence.

## Related prompts

- [Business-case inputs from their numbers](../../prompts/08-deal-strategy/business-case-inputs.md): The size of the prize as a range, built on the account's own revenue, margin, spend, outsourcing and hiring, with every number labelled, a worked example you can edit and the named owner to validate it with.
- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Answer objections with their own facts](../../prompts/08-deal-strategy/objection-handler.md): Which objections are real and which are cover, with a short reply and a question back for each, built on dated facts about the account, and the named person to take the answer to.
- [Mutual action plan on their calendar](../../prompts/08-deal-strategy/mutual-action-plan.md): A mutual action plan built backwards from your close date that respects the buyer's fiscal calendar, names buyer owners at each step, flags events that could move dates and says who to send the draft to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_account_financials_v3`, `accounts_hiring_timeline_v3`, `get_signal_news_v3`, `get_top_signals`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `deals-champion-pack`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
