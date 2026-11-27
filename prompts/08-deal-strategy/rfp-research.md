[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# RFP research and bid/no-bid call

> **A bid, bid-to-learn or qualify-out call on an RFP, with the likely evaluation priorities, who is already there, the named panel member to reach, three win themes and the questions to submit in the Q&A window.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An RFP, RFI or tender has landed and you have days, not weeks, to decide whether to bid and how to position. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 6–10 min | Company & financials, Priorities & opportunities, Outsourcing deals, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | mastercard.com |
| `[RFP scope]` | managed data-platform modernisation for payments analytics |
| `[Area in scope]` | Data Engineering, Cloud Computing (or a function like IT) |
| `[Known bidders]` | Accenture, Infosys (optional) |
| `[What I sell]` | data-platform modernisation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my bid manager. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. mastercard.com]
- RFP scope: [one line from the RFP, e.g. managed data-platform modernisation for payments analytics]
- Area in scope: [1–3 workloads or a function, e.g. Data Engineering, Cloud Computing — or IT]
- Known bidders (optional): [e.g. Accenture, Infosys]
- What I sell: [one line, e.g. data-platform modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
RFPs mirror priorities the buyer already stated, often shaped by an incumbent. An incumbent-heavy RFP with no matching priority is usually column fodder.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Turn [Area in scope] into 1–3 workloads (types of work, e.g. Data Engineering); if I gave a function, map it and say which.
3. Evaluation priorities: up to 10 in those workloads (if fewer than 3, widen to the function), with quarter and outcome lines.
4. Incumbents: engagements and partners in those workloads, then the top 10 providers, minus staffing and agency firms.
5. Installed tools: the top 10 products in those workloads by usage (High, then Medium), with vendor.
6. Known bidders: engagements in scope (services) or whole-stack check (software).
7. Panel: executives in those workloads, up to 2 pages of 10.
8. News, 12 months: vendor selections, partnerships, technology budgets, leadership changes. Review 20+ items; mark the most important from the last 90 days.
9. Money: revenue and growth.

OUTPUT
- Bottom line: 2 sentences — Bid, Bid-to-learn or Qualify-out, and the deciding fact. Bid if 2+ High-weight priorities match and no provider holds over 40% of in-scope engagements (editable default).
- Recommended next step: a named person (name, full title) from the panel, the action this week and the dated why-now; if none, say so.
- Table "Likely evaluation priorities" (up to 6): Priority | Source + quarter | Weight | How to answer it. High weight = from the 2 latest quarters (publication month for news priorities) and on scope.
- Table "Who is already there" (up to 8): Provider or vendor | Engagements or products | Share in scope | Threat (Incumbent, Contender, Minor).
- "Win themes": 3: theme, their words (dated), our proof, ghosting line.
- "Q&A questions": 5 that expose gaps or hidden incumbent advantages.
- Detail: panel (Name | Full title | Linked priority, up to 6), known-bidder footprint, money.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Ghosting lines describe a weakness, never a named rival.
- Quote any technology budget figure from news.
- A known bidder's product with High usage in scope is Red (incumbent advantage); Medium is Amber.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 500 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
RFP at [Company], scope [RFP scope]. Lead with bid, bid-to-learn or qualify-out, and the named panel member to reach with a dated why-now. Then likely evaluation priorities, incumbents in [Area in scope], 3 win themes and 5 Q&A questions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft the executive summary of our response (250 words) using the win themes.
```

```text
Turn the evaluation priorities into a compliance matrix with our response approach per row.
```

```text
Profile the top panel member and suggest how to address them in the orals.
```

```text
Show the 10 most recent engagements of the top incumbent in these workloads.
```

## Tips for better results

- Paste the RFP's own scope sentence; the closer it matches the buyer's language, the better the priority match.
- Use the Q&A questions to make the buyer state things the incumbent already knows.
- If the call is Qualify-out, spending the bid budget elsewhere is often the better decision.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.
- [Win plan against a rival](../../prompts/08-deal-strategy/competitive-strategy.md): How entrenched a named rival is at the account (rated Red, Amber or Green), the pitch they'll likely make, your wedge, three landmine questions and the named person to align with first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_product_competitors`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `deals-rfp-research`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
