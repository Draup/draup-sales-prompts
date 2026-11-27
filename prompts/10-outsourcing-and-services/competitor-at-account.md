[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# A rival's footprint and your wedge

> **How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're planning a displacement or second-vendor play at an account a rival already serves. Use services-outsourcing-footprint instead when you don't know who's there yet. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances | Services sellers | 2–4 min | Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Competitor]` | Cognizant |
| `[What I sell]` | application modernisation and managed cloud services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence analyst for IT services deals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Competitor: [Services firm, e.g. Cognizant]
- What I sell: [One line, e.g. application modernisation and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the account's active engagements and top 10 providers, for the whole account and for the business function closest to [What I sell] (e.g. IT), leaving out agencies and staffing firms. Confirm the competitor's Draup spelling.
3. Pull the competitor's engagement detail at the account: engagements, relationship tier, workloads, client and delivery locations.
4. If it has 2 engagements or fewer here (editable default), say so, show the top 5 IT and services providers, and run steps 3 and 5 on the largest one instead. If the account runs its own capability centre or has fewer than 20 IT-services engagements, flag that the work may be in-house.
5. Pull the account's workload counts and the analysed provider's workload counts at the account. Then check who holds each of at most 5 workloads: wedges matching [What I sell] plus the provider's top 2, skipping catch-alls.
6. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — how entrenched [Competitor] (or the largest provider, if the rival is absent) is, and where [What I sell] gets in.
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Verdict line: "[Provider] is #N at [Company] with X active engagements (Y in [function]); tier: …".
- "Wedge workloads" (up to 3): Workload | Its engagements | Who else holds it | Why it's a wedge. Workloads matching [What I sell] where the analysed provider has 3 engagements or fewer (editable default) or an operational or limited tier.
- "Top providers": Rank | Provider | Engagements | % of account total | In [function]. Highlight the analysed provider.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: the provider's footprint by workload; its onshore, nearshore and offshore delivery share.

RULES
- Tiers: strategic = broad, long-standing; operational = defined services; specialist = niche; limited = a few small engagements. Operational and limited are easiest to unseat.
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.

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
Bottom line and next step (named person, dated why-now) first. How big is [Competitor] at [Company] in Draup: rank, engagements, tier, delivery locations, and 3 thin workloads matching [What I sell]? If it's absent, analyse the largest provider.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the 10 most recent engagements between [Company] and [Competitor], with month, workload and delivery location.
```

```text
Which leaders at [Company] own the wedge workloads?
```

```text
Draft a 3-bullet 'why a second vendor' point of view for the person in the next step.
```

## Tips for better results

- Spell provider names as Draup does. If a name returns nothing, try the short brand name.
- If your rival isn't there, the prompt switches to the largest provider, so an empty result still gives you a plan.
- A thin footprint in a workload you lead is usually a better wedge than attacking the rival's core.

## Related prompts

- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [A rival's customers you can win](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_deals_workloads_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-competitor-at-account`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
