[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Outsourcing footprint and incumbents

> **How much the account outsources, to whom, how concentrated its provider base is, and which workloads are ripe for vendor consolidation.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before any services pursuit, to size the account and see who you are up against. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances | Services sellers | 2–4 min | Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | data engineering and analytics managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outsourcing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. data engineering and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the outsourcing summary: active service providers, active engagements and Draup-estimated outsourced headcount.
3. Pull the top 25 providers by engagements. Set aside agencies, staffing, market-research and merchandising firms and the account's subsidiaries (give their combined share in one line). Keep the top 15 of the rest, with each one's share and the combined top-3 and top-15 shares.
4. Pull the top 10 outsourced workloads with engagement counts.
5. For the top 5 workloads, pull providers (up to 200 rows): how many, and the largest one's share. If exactly 50 come back, call the count a floor.

OUTPUT
- Bottom line: 2 sentences — concentrated or long tail, and the best opening for [What I sell].
- Verdict: "Concentrated" if the top 3 hold more than 50% of engagements (editable default), otherwise "Long tail", with both shares.
- "Snapshot": Providers | Engagements | Draup-estimated outsourced headcount.
- "Incumbents": Rank | Provider | Engagements | % of total, largest first.
- "Workloads": Workload | Engagements | Providers | Largest provider and share | Likely owner (title).
- "Consolidation wedge": up to 3 workloads matching [What I sell] with 5+ providers and none above 40% (editable default), each with a one-line pitch.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- If no top-10 workload matches [What I sell], say so instead of forcing a wedge.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Size [Company]'s outsourcing in Draup: providers, engagements, Draup-estimated outsourced headcount, top 15 IT and services providers by share, top 10 workloads, a concentrated-or-long-tail verdict and up to 3 consolidation workloads.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show [Competitor]'s footprint at [Company] and where it is thinnest.
```

```text
Which executives own the consolidation workloads?
```

```text
Draft a 120-word vendor-consolidation point of view for the CIO.
```

## Tips for better results

- A long tail of small providers often means no one owns the workload end to end. That is the opening for a consolidation pitch.
- Outsourced headcount is a Draup estimate. Use it to compare accounts, not as a number to quote to the client.

## Related prompts

- [A competitor's footprint at an account](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.
- [Vendor mix vs the vertical](../../prompts/10-outsourcing-and-services/vendor-mix-benchmark.md): Where the account outsources more or less than its industry, and which leading industry providers it doesn't use yet.
- [Is work coming back in-house? (re-insourcing risk)](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_deals_workloads_v3`

Status: **tested live**. Prompt id: `services-outsourcing-footprint`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
