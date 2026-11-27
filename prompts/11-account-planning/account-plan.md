[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Draft an account plan

> **An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Annual or half-year account planning, or when you inherit a strategic account. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps | Everyone | 6–10 min | Company & financials, Priorities & opportunities, Executives & movement, Tech stack, Outsourcing deals, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | bmw.com |
| `[What I sell]` | supply-chain planning software |
| `[Business function]` | Supply Chain |
| `[Already buy from us (optional)]` | demand planning for two regions |
| `[Our goal (optional)]` | double ARR in 12 months |
| `[Competitor (optional)]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my strategic account planner. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [Website, e.g. bmw.com]
- What I sell: [One line, e.g. supply-chain planning software; skip if saved in setup]
- Business function: [The function that buys from us, e.g. Supply Chain]
- Already buy from us (optional): [e.g. demand planning for two regions]
- Our goal (optional): [e.g. double ARR in 12 months]
- Competitor (optional): [Up to 3, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find the company by website (no result: try its name once and show the match score). Confirm it's the parent, not a subsidiary or sister company; if several match, ask me. Use Draup's exact name from then on.
2. Snapshot: profile, latest revenue (USD at Draup's rate), Opportunity Index.
3. Strategy: top 5 [Business function] priorities, newest first, with source, quarter and workloads.
4. Buying committee: top 8 leaders in [Business function] by title and budget control (up to 3 pages of 10).
5. Incumbents: products on those workloads (strength, last seen), top providers in the function, and any [Competitor] product anywhere in the stack. Rate [Competitor] by the rivals rule; list Green ones too.
6. Risks: senior exits in 6 months (by workload; state the latest move date), layoffs in 90 days, [Competitor] products newly detected in 12 months.
7. Timing: its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the prize and the first play.
- Recommended next step: one person from step 4 (name and title), what to do, and the dated why-now (step 7 or another dated fact). If none, say so.
- "Expansion plays" (top 3, building on what they buy): Play | Evidence and date | Builds on | Likely owner; a High-usage [Competitor] product in the workload makes it a displacement.
- "Buying committee" (top 5): Name | Full title | Budget control | Why they matter.
- Gaps: what Draup didn't have, to ask in discovery.
- Detail, each dated and sourced: snapshot; strategy (Priority | Quarter | Workloads); incumbents with [Competitor] rating; 3 risks; 90-day plan toward [Our goal] (two actions per 30 days, owner role each). SWOT only if I ask.

RULES
- In banking and consulting, VP and SVP are mid-level.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the function closest to What I sell; map a function to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Rivals count only at High or Medium usage (say how many were Low). Software: High in my workloads Red, Medium or newly detected Amber, else Green. Services, by share of active engagements in my workloads: 30%+ Red, 10–29% Amber, under 10% Green. Trust usage and last-seen date, not confidence; no "Generic" rows.
- Pull lists 10 at a time; count first when a list could be long; every total applies all my conditions.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 500 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line, first play and a named contact with a dated why-now first. Then an account plan for [Company]: [Business function] priorities, buying committee, incumbents and installed [Competitor] products, ranked plays for [What I sell], risks, 90-day plan.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Add the short SWOT section.
```

```text
Turn the 90-day plan into a mutual action plan I can share with my champion.
```

```text
Run a renewal risk check on this account.
```

```text
Write a 120-word executive summary of this plan for my VP.
```

## Tips for better results

- Paste what they already buy and your goal. The expansion plays and 90-day plan get much sharper.
- Name the competitors you meet. A rival installed with High usage in your workload turns an expansion play into a displacement.

## Related prompts

- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [Best entry points: expand or new](../../prompts/11-account-planning/entry-points.md): The five best ways in for what you sell, each marked Expand (we already serve it) or New, with dated evidence, incumbents, any installed competitor and the likely owner.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and the named person to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_deals_service_provider_v3`, `get_account_executive_movement`, `get_top_signals`, `get_tech_stack_trend_v3`

Status: **tested live**. Prompt id: `plan-account-plan`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
