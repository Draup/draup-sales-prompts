[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# CXO pursuit brief

> **A one-page pursuit brief for a C-level meeting: money context, the 3 workloads to lead with, the buyers, incumbents, an evidence check and a 90-day plan.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have, or want, a meeting with a CIO, CTO, COO or other C-level buyer on a large pursuit. | Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps, Presales & Solutions | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Executives & movement, Outsourcing deals |

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
Act as my pursuit lead. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Business function: [The CXO's function, e.g. IT for a CIO]
- What I sell: [One line, e.g. AI-led application modernisation services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Money: latest fiscal-year revenue (USD at Draup's rate), Draup-estimated IT spend, growth.
3. Priorities in [Business function] from the 4 most recent quarter labels in the data; count how many involve each workload.
4. For the top 6 workloads, pull engagements, leading providers and the top provider's tier.
5. Pick 3 lead workloads: most evidence, best fit to [What I sell], no strategic incumbent.
6. Buyers: up to 6 senior leaders in [Business function] (10 per page, max 3 pages), plus director-plus moves in 6 months narrowed by those workloads.

OUTPUT
- Bottom line: 2 sentences — the case and the opening angle.
- "Lead with": Workload | Priority evidence (quarter) | Incumbent and tier | Our angle.
- "Buyers": Name | Full title | Why they matter | Recent move.
- "Evidence check: Go / Not yet": Go if 2+ matching priorities sit in the 2 latest quarter labels, a reachable senior buyer exists, and a lead workload has no strategic incumbent (editable default); else Not yet and what would change it.
- "What we must learn in meeting 1": 3 questions.
- "90-day plan": two actions per 30 days.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- Use each person's full profile title, not the seniority label. In banking and consulting, VP/SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- Rank providers by engagements yourself; Draup may return them alphabetically.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Use professional information only (name, title, employer, Draup profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Build a CXO pursuit brief for [Company]'s [Business function] leader: money context, 3 workloads to lead with (priorities plus incumbents), senior buyers, an evidence check (Go / Not yet), what to learn in meeting 1, and a 90-day plan.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write 5 hypothesis-led questions for the CXO, each citing a fact from the brief.
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

- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan in eight parts: snapshot, their strategy in their own words, buying committee, incumbents, ranked expansion plays, risks and a 90-day plan, plus an optional short SWOT.
- [A competitor's footprint at an account](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `get_priorities_top_workloads_v3`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `accounts_executives_key_executives_v3`, `get_account_executive_movement`

Status: **tested live**. Prompt id: `plan-cxo-pursuit-brief`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
