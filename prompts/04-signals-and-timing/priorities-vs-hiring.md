[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Priorities with no hiring behind them

> **Which stated priorities have hiring behind them and which don't: the gaps where the account may need to buy rather than build.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Shaping a services or software pitch, or deciding which priority to lead with. | Account Executive, Services, SI & Staffing Seller, Presales & Solutions | Everyone | 2–4 min | Priorities & opportunities, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | intelligent automation and RPA services |
| `[Business function]` | Supply Chain (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. intelligent automation and RPA services — skip if you ran the start-here prompt]
- Business function: [optional, e.g. Supply Chain, IT]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the workloads in the stated priorities, ranked by how many priorities involve each (narrowed to [Business function] if given). Keep the top 15.
3. Pull hiring by workload for the last 12 months, up to 5 pages: postings and trend. Set frontline workloads (store operations, food and beverage, warehousing) aside unless they relate to what I sell.
4. Match each priority workload to its hiring; where names differ, use the closest and say so.
5. Mark each (editable defaults): Backed = top 20 hiring workload or trending up; Partial = 50+ postings but not Backed; Thin = under 50; Silent = none; Not comparable = strategy or governance work that rarely appears in job ads.
6. For the 3 biggest gaps (most priorities, least hiring), pull the priority names with source and fiscal quarter.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table: Workload | Priorities involving it | Postings (12 months) | Trend | Read | Likely owner.
- "Build-or-buy gaps" (top 3): priority, source and quarter, hiring numbers, and why [What I sell] could fill it.
- "Already backed": 2–3 workloads they are building in-house.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Little hiring doesn't prove they will buy; they may already outsource the work. Say so, and suggest checking their outsourcing for those workloads.
- State the hiring window.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Keep to about 320 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Company]'s top 15 priority workloads with its hiring over the last 12 months. Mark each Backed, Partial, Thin or Silent, and name the 3 biggest build-or-buy gaps for [What I sell] with the priorities behind them.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top gap, which service providers already work that workload at [Company]?
```

```text
Who owns the top gap? List executives tagged to that workload.
```

```text
Write a one-paragraph point of view on the top gap for the function head.
```

## Tips for better results

- Silent or Thin workloads with several priorities are worth testing as buy signals, after you check who already does the work for them.
- Backed workloads still matter. They show where the account has in-house teams you'd work alongside.

## Related prompts

- [Is work coming back in-house? (re-insourcing risk)](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools linked to it, the service providers working it, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings and talking points.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_priorities_top_workloads_v3`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `signals-priorities-vs-hiring`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
