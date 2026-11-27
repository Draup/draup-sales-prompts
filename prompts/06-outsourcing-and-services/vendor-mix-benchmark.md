# Vendor mix vs the vertical

**Where the account outsources more or less than its industry, and which leading industry providers it doesn't use yet.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need a peer-based argument for a new service line, or to find consolidation targets. For internal planning. | Services, SI & Staffing Seller, Partnerships & Alliances, Account Executive, Sales Leader & RevOps | Services sellers | 2–4 min | Outsourcing deals, Industry ecosystem |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | cloud infrastructure managed services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my services benchmarking analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. cloud infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary vertical.
2. Pull the account's top 50 outsourced workloads with engagements, and each one's share of that total.
3. Pull the vertical's top 50 outsourced workloads and shares the same way. If it returns zeros, try the parent industry and name it.
4. For the vertical's top 20, compute an index: account share ÷ vertical share. Under 0.5 = under-indexed; over 2.0 = over-indexed (editable defaults).
5. Pull the account's top 10 providers and the vertical's top 10, leaving out agencies, staffing, market-research and merchandising firms. Find leaders missing at the account.

OUTPUT
- Bottom line: 2 sentences — the clearest gap or excess and what it means for [What I sell].
- "Workload mix": Workload | Account engagements | Account share | Vertical share | Index | Read | Likely owner (title). By vertical share.
- "Under-indexed": up to 3 matching [What I sell], each as a question ("peers outsource this more; is it in-house?").
- "Over-indexed": up to 3 that may suit consolidation or rate pressure.
- "Providers": Vertical rank | Vendor | At the account? (engagements or No).
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Shares are of each top-50 total, not all work; say so. The index is fragile: internal use only, never in front of the client.
- Exclude catch-all workloads (Project/Programs Management, Account Management, Talent Acquisition) from Under and Over picks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Compare [Company]'s outsourced workload mix and top providers with its industry's in Draup. Show where it is under- or over-indexed and which leading industry providers it doesn't use.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Is [Company] hiring in-house for the under-indexed workloads?
```

```text
Which industry peers outsource the under-indexed workload most? Give me 5 names as proof.
```

```text
Draft a 100-word peer-benchmark email for the head of IT infrastructure, without the index numbers.
```

## Tips for better results

- An under-indexed workload is either greenfield or done in-house. A quick look at job postings tells you which.
- Use the multiplier to plan, not to pitch. In front of the client, talk about what peers do, not the index.

## Related prompts

- [Outsourcing footprint and incumbents](../../prompts/06-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated its provider base is, and which workloads are ripe for vendor consolidation.
- [Vertical vendor league table](../../prompts/07-vertical-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers and where your firm ranks.
- [Is work coming back in-house? (re-insourcing risk)](../../prompts/06-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_deals_workloads_v3`, `ecosystem_get_vertical_outsourcing_workloads`, `get_deals_service_provider_v3`, `ecosystem_get_vertical_outsourcing_vendors`

Status: **tested live**. Prompt id: `services-vendor-mix-benchmark`.

</details>

[Back to Outsourcing and services deals](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
