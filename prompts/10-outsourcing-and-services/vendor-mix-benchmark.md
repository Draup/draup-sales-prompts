[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# How their vendor mix compares with peers

> **Where the account outsources more or less than its industry, which leading industry providers it doesn't use yet, and who to raise it with.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need a peer-based argument for a new service line, or to find consolidation targets. For internal planning. | Services, SI & Staffing Seller, Partnerships & Alliances, Account Executive, Sales Leader & RevOps | Services sellers | 2–4 min | Outsourcing deals, Industry ecosystem, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | cloud infrastructure managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my services benchmarking analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. cloud infrastructure managed services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary industry.
2. Pull the account's top 50 outsourced workloads with engagements, and each one's share of that total.
3. Pull the industry's top 50 outsourced workloads and shares the same way. If it returns zeros, try the parent industry and name it.
4. For the industry's top 20, compute an index: account share ÷ industry share. Under 0.5 = under-indexed; over 2.0 = over-indexed (editable defaults).
5. Pull the account's top 10 providers and the industry's top 10, leaving out agencies, staffing, market-research and merchandising firms. Find leaders missing at the account.
6. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the clearest gap or excess and what it means for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Workload mix" (top 10 by industry share): Workload | Account share | Industry share | Index | Read.
- "Under-indexed": up to 3 matching [What I sell], each as a question ("peers outsource this more; is it in-house?"). "Over-indexed": up to 3 that may suit consolidation or rate pressure.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: rows 11–20 of the mix and "Providers" (Industry rank | Provider | At the account? engagements or No).

RULES
- Shares are of each top-50 total, not all work; say so. The index is fragile: internal use only, never in front of the client.
- Exclude catch-all workloads (Project/Programs Management, Account Management, Talent Acquisition) from Under and Over picks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Compare [Company]'s outsourced workload mix and top providers with its industry's in Draup. Show where it's under- or over-indexed and which leading industry providers it doesn't use.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Is [Company] hiring in-house for the under-indexed workloads?
```

```text
Which industry peers outsource the under-indexed workload most? Give me 5 names as proof.
```

```text
Draft a 100-word peer-benchmark email to the person in the next step, without the index numbers.
```

## Tips for better results

- An under-indexed workload is either greenfield or done in-house. A quick look at job postings tells you which.
- Use the index to plan, not to pitch. In front of the client, talk about what peers do, not the multiplier.

## Related prompts

- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [Who wins services work in a vertical](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_deals_workloads_v3`, `ecosystem_get_vertical_outsourcing_workloads`, `get_deals_service_provider_v3`, `ecosystem_get_vertical_outsourcing_vendors`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-vendor-mix-benchmark`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
