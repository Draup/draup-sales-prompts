[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# A rival's footprint and your wedge

> **How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're planning a displacement or second-vendor play at an account a rival already serves. Use "Outsourcing footprint and consolidation wedge" instead when you don't know who's there yet. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances | Services sellers | 2–4 min | Outsourcing deals, Executives & movement, News signals |

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
Act as my services competitive analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Competitor: [Services firm, e.g. Cognizant]
- What I sell: [One line, e.g. application modernisation and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull active engagements and top 10 providers for the whole account and the function closest to [What I sell], without agencies and staffing firms. Confirm the competitor's Draup spelling.
3. Pull the competitor's engagement detail: engagements, tier, workloads, client and delivery locations.
4. If it has 2 engagements or fewer here (editable default), say so and run steps 3 and 5 on the largest provider instead. Under 20 IT-services engagements or an own capability centre? Flag the work may be in-house.
5. Pull the account's and the analysed provider's workload counts; check who holds up to 5 non-catch-all workloads: wedges matching [What I sell] plus the provider's top 2.
6. People and timing: the top 3 leaders in the function closest to [What I sell] and the most important 90-day news item where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the rating of [Competitor] (or the largest provider, if absent) and where I get in.
- Recommended next step: a person from step 6 (name and title), what to do, and the dated why-now (or say none).
- Verdict line: "[Provider] is #N at [Company] with X active engagements (Y in [function]); tier: …; rating: Red, Amber or Green" (by share of active engagements in my workloads).
- "Wedge workloads" (up to 3): Workload | Its engagements | Who else holds it | Why it's a wedge. Workloads matching [What I sell] where the provider has 3 or fewer engagements (editable default) or an operational or limited tier.
- "Top providers": Rank | Provider | Engagements | % of account | In [function]; highlight the analysed provider.
- Gaps: what Draup lacked; ask in discovery.
- Detail: the provider's footprint by workload and its onshore/nearshore/offshore share.

RULES
- Tiers: strategic (broad, long-standing), operational (defined services), specialist (niche), limited (a few small engagements); operational and limited are easiest to unseat.
- Never recommend catch-all workloads (Project/Programs Management, Account Management).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow pulls to the business function closest to What I sell; map a function I give to its 1–3 main workloads and say which.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Rate a services rival by its share of the account's active engagements in the relevant workloads: Red 30%+ (entrenched), Amber 10–29%, Green under 10% (light; room to wedge in).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
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
