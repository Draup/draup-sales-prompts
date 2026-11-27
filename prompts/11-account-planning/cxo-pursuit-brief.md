[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Brief for a C-level pursuit meeting

> **A one-page pursuit brief for a C-level meeting: the 3 workloads to lead with, the buyers, incumbents, a Go or Not-yet evidence check, what to learn in meeting 1 and a 90-day plan.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have, or want, a meeting with a CIO, CTO, COO or other C-level buyer on a large pursuit. | Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps, Presales & Solutions | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Executives & movement, Outsourcing deals, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Business function]` | IT |
| `[What I sell]` | AI-led application modernisation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pursuit lead. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Business function: [The executive's function, e.g. IT for a CIO]
- What I sell: [One line, e.g. AI-led application modernisation services; skip if saved in setup]

STEPS
1. Find the company by website (no result: try its name once and show the match score). Confirm it's the parent, not a subsidiary or sister company; if several match, ask me. Use Draup's exact name from then on.
2. Money: latest fiscal-year revenue (USD at Draup's rate) and growth.
3. Priorities in [Business function] from the 4 most recent quarter labels in the data; count how many involve each workload.
4. For the top 6 workloads, pull engagements, leading providers and the top provider's tier.
5. Pick 3 lead workloads: most evidence, best fit to [What I sell], no strategic incumbent. Skip catch-alls.
6. Buyers: up to 6 senior leaders in [Business function] (10 per page, up to 3 pages), plus director-plus moves in 6 months narrowed by those workloads. If no C-level, EVP or "Head of" appears, pull the next page of 10 once, look for Chief, EVP or CIO titles and say what you found.
7. Timing: the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the case and the opening angle.
- Recommended next step: one buyer from step 6 (name and title), what to do, and why now (the step-7 item or another dated fact). If none turned up, say so.
- "Lead with": Workload | Priority evidence (quarter) | Incumbent and tier | Our angle.
- "Buyers": Name | Full title | Why they matter | Recent move.
- "Evidence check: Go / Not yet": Go if 2+ matching priorities sit in the 2 latest quarter labels, a reachable senior buyer exists, and a lead workload has no strategic incumbent (editable default); else Not yet and what would change it.
- Gaps: what Draup didn't have, to ask in discovery.
- Detail: money context; "What we must learn in meeting 1" (3 questions); "90-day plan" (two actions per 30 days).

RULES
- In banking and consulting, VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- Pull lists 10 at a time; count first when a list could be long; every total applies all my conditions.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named buyer, dated why-now) first. Build a C-level pursuit brief for [Company]'s [Business function] leader: 3 workloads to lead with (priorities plus incumbents), buyers, a Go or Not-yet check, meeting-1 questions and a 90-day plan.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write 5 hypothesis-led questions for the executive, each citing a fact from the brief.
```

```text
Pick a co-sell partner for the first lead workload.
```

```text
Turn the brief into a 3-slide executive summary.
```

## Tips for better results

- The evidence check is in the prompt. Tighten or loosen it to match how your team qualifies large pursuits.
- Check each buyer's full title yourself. Seniority tags can overstate.

## Related prompts

- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_priorities_top_workloads_v3`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `accounts_executives_key_executives_v3`, `get_account_executive_movement`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-cxo-pursuit-brief`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
