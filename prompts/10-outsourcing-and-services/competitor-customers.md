[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# A rival's customers you can win

> **A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're building a displacement campaign against one services rival in one industry. Use "A rival's footprint and your wedge" instead for a single account. | Services, SI & Staffing Seller, Account Executive, SDR / BDR, Sales Leader & RevOps | Services sellers | 2–4 min | Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | Capgemini |
| `[Vertical]` | Life Sciences |
| `[Country]` | United States of America (default: my territory) |
| `[Workload (optional)]` | Data Engineering |
| `[What I sell]` | clinical data and analytics managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my displacement-campaign analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [Services firm, e.g. Capgemini]
- Vertical: [Draup industry, e.g. Life Sciences]
- Country: [Customer HQ country in full, e.g. United States of America; default: my territory from setup]
- Workload (optional): [e.g. Data Engineering, or a business function I'll map; blank for all]
- What I sell: [One line, e.g. clinical data and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Confirm Draup's spelling of the competitor, industry and country. Use each customer's primary industry so loosely tagged companies don't slip in.
2. Pull the competitor's customers in that primary industry with HQ in that country (and workload, if given), by engagements. Merge subsidiaries into parents; keep the top 20.
3. For the top 8, pull each account's provider ranking (the competitor's rank and the provider just above or below it), and get all 8 accounts' total engagements in one customer lookup; share = competitor engagements ÷ total.
4. Pull the competitor's top 5 workloads in this industry and country.
5. People and timing: pick the Best 3 (see OUTPUT). For the first one, pull its top 3 leaders in the business function closest to [What I sell] (full profile titles) and its most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — how big [Competitor] is here and which accounts to attack first.
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Headline line: "[Competitor] has N customers and X active engagements in [Vertical], [Country]", plus its top 5 workloads.
- "Targets" (top 10): Rank | Customer | Engagements with rival | Share of account | Read.
- Read: Red (entrenched: #1 or 30%+), Amber (contestable: #2–3, or 10–29%), Green (foothold: outside the top 3 and under 10%; a light presence) — editable defaults. Rows 9–20: "not assessed".
- "Best 3 to target": assessed Amber or Green accounts with the most engagements, one line each with the provider next to the rival.
- Gaps: what Draup lacked; ask in discovery.
- Detail: rows 11–20 and each top-8 account's total engagements and rank.

RULES
- Flag customers that look misclassified, are the competitor's own subsidiaries or are investors; leave them out of Best 3.
- If fewer than 5 customers come back, drop the workload, then widen the country to its region, and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the business function closest to What I sell; map a function I give to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named buyer, dated why-now) first. Which [Vertical] companies headquartered in [Country] use [Competitor] most in Draup? Top 20 by engagements, its share and rank at the top 8, and the 3 most contestable.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show [Competitor]'s footprint and wedge workloads at the first Best-3 account.
```

```text
Assess rows 9–16 the same way.
```

```text
Write a 3-email displacement sequence for the person in the next step.
```

## Tips for better results

- Use the full country name, e.g. United States of America.
- An Amber account (the rival is #2–3) is often easier to win than a Red one where it is the main partner.

## Related prompts

- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_deals_customer_v3`, `get_deals_service_provider_v3`, `get_deals_workloads_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-competitor-customers`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
