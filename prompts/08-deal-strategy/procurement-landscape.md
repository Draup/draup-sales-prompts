[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Prepare for their procurement team

> **The procurement stance to expect (consolidate, cost-down, re-bid or strategic), who already supplies the work in scope and how concentrated they are, the pressure procurement is under and the named procurement lead to reach.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A deal is heading to procurement or a vendor-selection process, or the buyer mentions consolidation or a preferred-supplier list. | Account Executive, Services, SI & Staffing Seller, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 4–6 min | Outsourcing deals, Priorities & opportunities, Executives & movement, News signals, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | roche.com |
| `[Work in scope]` | Application Development & Maintenance (or a function like IT) |
| `[Deal type]` | services (or software) |
| `[What I sell]` | application management services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my procurement strategy advisor for sellers. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. roche.com]
- Work in scope: [workload or function being bought, e.g. Application Development & Maintenance — or IT]
- Deal type: [services or software]
- What I sell: [one line, e.g. application management services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Fragmented providers under a cost programme mean consolidation; a concentrated base means an incumbent to dislodge.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Work in scope] to 1–3 workloads (types of work) and say which.
3. Whole account: active engagements and partners.
4. In scope: active engagements and partners in those workloads, then the top 10 providers; compute the top-3 share.
5. Software deals: the top 10 technology vendors in the workloads, with main products.
6. Up to 5 Procurement priorities, with outcome lines and linked tools and providers.
7. Pressure, last 12 months of news: savings programmes, restructuring, layoffs, divestments, vendor consolidation, outsourcing deals. Review at least 20 items; mark the most important from the last 90 days.
8. Procurement executives, one page of 10: look for IT, indirect, digital or technology procurement titles; flag subsidiaries. If none, take the top 3 executives in the function that owns the work.

OUTPUT
- Bottom line: 2 sentences — the stance to expect (Consolidate, Cost-down, Competitive re-bid or Strategic partner) and what it means for [What I sell].
- Recommended next step: a named person (name, full title) in procurement, or the business owner if none, the action this week and the dated why-now (or say none).
- Table "Provider landscape" (top 10 in scope): Rank | Provider | Active engagements | Share. Then the top-3 share and a label: Concentrated over 50%, Fragmented under 30% (editable defaults), else Mixed.
- Table "Pressure on procurement" (up to 5): Date | Programme or event | Figure | Source.
- "What they'll ask for" (rate card, outcome pricing, transition plan, savings commitment) and "How to prepare": 3 moves.
- Detail: whole-account context, procurement tools, software vendors, "Procurement contacts" (Name | Full title | Unit | IT/indirect or direct materials).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Exclude advertising, media, PR, staffing and market-research firms when the deal is IT or services work, and say so.
- A savings programme counts only if news names a target, date or scope.
- If no IT, indirect or technology procurement lead appears, say so rather than naming a direct-materials buyer.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Procurement read for [Company] on [Work in scope]. Lead with the stance to expect and the named procurement lead to reach. Then incumbents and their share, cost programmes with figures, and 3 moves to prepare.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a consolidation proposal outline that reduces their provider count in [Work in scope].
```

```text
Which of the incumbents are thinnest here? Show their engagements and tiers.
```

```text
Write a 100-word note to the procurement lead framing our offer against their savings programme.
```

## Tips for better results

- Ask your champion who in procurement covers technology services; Draup's procurement pages often skew to direct materials.
- Fragmented plus a savings target usually means a consolidation play beats a pure price play.

## Related prompts

- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [How their vendor mix compares with peers](../../prompts/10-outsourcing-and-services/vendor-mix-benchmark.md): Where the account outsources more or less than its industry, which leading industry providers it doesn't use yet, and who to raise it with.
- [Business-case inputs from their numbers](../../prompts/08-deal-strategy/business-case-inputs.md): The size of the prize as a range, built on the account's own revenue, margin, spend, outsourcing and hiring, with every number labelled, a worked example you can edit and the named owner to validate it with.
- [RFP research and bid/no-bid call](../../prompts/08-deal-strategy/rfp-research.md): A bid, bid-to-learn or qualify-out call on an RFP, with the likely evaluation priorities, who is already there, the named panel member to reach, three win themes and the questions to submit in the Q&A window.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_product_competitors`, `get_account_priorities_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `deals-procurement-landscape`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
