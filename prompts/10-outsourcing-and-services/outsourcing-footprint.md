[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Outsourcing footprint and consolidation wedge

> **How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before any services pursuit, to size the account and see who you're up against. Use this when you don't yet know which rival matters; use services-competitor-at-account instead when you do. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances | Services sellers | 2–4 min | Outsourcing deals, Executives & movement, News signals |

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
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the account's active service providers and active engagements, once for the whole account and once for the business function closest to [What I sell] (e.g. IT).
3. Pull the top 25 providers by engagements. Set aside agencies, staffing, market-research and merchandising firms and the account's own subsidiaries (one line with their combined share). Keep the top 10 of the rest, and note each one's engagements in that function.
4. Pull the top 15 outsourced workloads (a workload is a type of work, e.g. Application Development & Maintenance).
5. For up to 5 workloads, skipping catch-alls, take those matching [What I sell] first, then the largest others, and pull their providers: how many, and the largest one's share.
6. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — concentrated or long tail, and the best opening for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Verdict line: "Concentrated" if the top 3 providers hold more than 50% of active engagements (editable default), otherwise "Long tail". Every % is a share of the account's total active engagements from step 2; state that total.
- "Consolidation wedge" (up to 3): Workload | Engagements | Providers | Largest provider and share | One-line pitch. Only workloads matching [What I sell] with 5+ providers and none above 40% (editable defaults).
- "Top providers": Rank | Provider | Engagements | % of total | In [function].
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: the 15 workloads (Workload | Engagements | Providers checked?) and the set-aside line.

RULES
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- If no workload matches [What I sell], say so instead of forcing a wedge.
- If a company with $10B+ revenue shows fewer than 20 IT-services engagements, warn that the work may be in-house (check for a capability centre) or the data thin.
- Leave agencies, staffing, market-research and merchandising firms, software vendors and look-alike names out of provider lists.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell. Where a workload is needed and I gave a function, map it to its 1–3 main Draup workloads and say which.
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
Bottom line and a next step (named person, dated why-now) first. Then size [Company]'s outsourcing: active engagements, top 10 IT and services providers by share, concentrated or long tail, and up to 3 consolidation wedges for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show [Competitor]'s footprint at [Company] and where it's thinnest.
```

```text
Who owns the wedge workloads? List up to 5 leaders with full titles.
```

```text
Is any of this work moving in-house? Check in-house hiring in the wedge workloads.
```

```text
Draft a 120-word vendor-consolidation point of view for the person in the next step.
```

## Tips for better results

- A long tail of small providers often means no one owns the workload end to end. That's the opening for a consolidation pitch.
- Engagement counts are Draup-derived. Use them to compare providers inside one account, not as contract values to quote to the client.

## Related prompts

- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [How their vendor mix compares with peers](../../prompts/10-outsourcing-and-services/vendor-mix-benchmark.md): Where the account outsources more or less than its industry, which leading industry providers it doesn't use yet, and who to raise it with.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_deals_workloads_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-outsourcing-footprint`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
