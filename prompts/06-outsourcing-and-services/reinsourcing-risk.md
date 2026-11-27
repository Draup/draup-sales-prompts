[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is work coming back in-house? (re-insourcing risk)

> **For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a renewal, an expansion pitch or a new pursuit, to decode what the account really intends. | Services, SI & Staffing Seller, Account & Customer Success Manager, Account Executive | Services sellers | 4–6 min | Outsourcing deals, Hiring & job postings, Talent flow & locations, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | managed analytics and BI services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my services account strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. managed analytics and BI services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the top 10 outsourced workloads with engagements.
3. Pull in-house postings by workload in one unfiltered pass (up to 60, monthly); filtering by workload mixes in co-tagged roles. Compare the last 5 full months with the 5 before (skip the partial first and last) and name the months.
4. Also list workloads outside that top 10 with postings up over 50% and 50+ in 12 months.
5. Pull GCC sites (all functions) and 12-month centre setup or expansion news where [Company] is the actor; ignore branches, wealth centres, HQ moves and plants.
6. Classify each outsourced workload in order: No signal (under 20 postings in 12 months); Re-insourcing risk (up over 20% and a GCC hiring in that function); Capability gap (up over 20%, no GCC); Cost takeout (up 20% or less: rate and vendor pressure).

OUTPUT
- Bottom line: 2 sentences — biggest risk and opening for [What I sell].
- Table: Workload | Engagements | In-house postings (12 mo) | Last 5 vs prior 5 | GCC link | Read | What to pitch.
- "Growing in-house, outside the outsourced top 10": Workload | Postings | Change | GCC link | Likely meaning.
- "Biggest risk" and "Biggest opening": one workload each.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Thresholds are editable defaults. Catch-all workloads (Project/Programs Management, Account Management): "not assessed".
- GCC site headcount is indicative; count each site once.
- Each Read is a hypothesis, not a fact.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
For [Company]'s top 10 outsourced workloads, compare in-house postings over the last 5 full months with the 5 before, check GCC sites and expansion news, and label each: re-insourcing risk, capability gap, cost takeout or no signal.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who leads the GCC behind the biggest risk?
```

```text
Show the 10 most recent in-house postings for the risk workload, with title, date and location.
```

```text
Draft a renewal-defence talking point for the risk workload.
```

## Tips for better results

- Hiring and outsourcing in the same workload is not always bad news. Without a captive centre behind it, it often means demand is outgrowing both.
- The fastest in-house growth is often outside the outsourced top 10; that list is where new captive teams show up first.

## Related prompts

- [Global capability centres (GCCs) and the services play](../../prompts/06-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.
- [Outsourcing footprint and incumbents](../../prompts/06-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated its provider base is, and which workloads are ripe for vendor consolidation.
- [Renewal risk check (RAG)](../../prompts/08-account-planning-and-expansion/risk-check.md): A Red/Amber/Green risk table for one customer, including your sponsor's status, with dated evidence, an overall rating and two actions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_deals_workloads_v3`, `accounts_hiring_demand_category_v3`, `accounts_location_insights_key_locations_map_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `services-reinsourcing-risk`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
