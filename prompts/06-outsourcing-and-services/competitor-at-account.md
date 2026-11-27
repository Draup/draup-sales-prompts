# A competitor's footprint at an account

**How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are planning a displacement or a second-vendor play at an account a competitor already serves. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances | Services sellers | 2–4 min | Outsourcing deals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Competitor]` | Cognizant |
| `[What I sell]` | application modernisation and managed cloud services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my competitive-intelligence analyst for IT services deals. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Competitor: [Services firm, e.g. Cognizant]
- What I sell: [One line, e.g. application modernisation and managed cloud services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the account's outsourcing summary and top 10 providers (no agencies or staffing firms); confirm the competitor's Draup spelling there.
3. Pull the competitor's engagement detail at the account: engagements, estimated headcount, relationship tier, workloads, client and delivery locations. If empty, check the summary for that provider alone.
4. Pull the account's workload counts and the competitor's workload counts at the account (one lookup each), then check which providers hold each of at most 5 workloads: your likely wedges plus the competitor's top 2.

OUTPUT
- Bottom line: 2 sentences — how entrenched [Competitor] is and where [What I sell] gets in.
- Verdict: "[Competitor] is the #N provider at [Company] with X engagements (tier: …)".
- "Top providers": Rank | Provider | Engagements | % of account. Highlight the competitor.
- "[Competitor] footprint": Workload | Its engagements | Other providers | Likely owner (title).
- "Delivery model": onshore/offshore mix of its delivery locations.
- "Wedge workloads": 3 matching [What I sell] where the competitor has 3 engagements or fewer (editable default) or an operational or limited tier, each with the reason and rivals there.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Tiers: strategic = broad, long-standing; operational = runs defined services; specialist = niche skills; limited = a few small engagements. Operational and limited are easiest to unseat.
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- If it has no engagements here, say so and show the top 5 providers.

STANDARD RULES (leave as is)
- Rank providers by engagements yourself; Draup may return them alphabetically.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
How big is [Competitor] at [Company] in Draup? Engagements, relationship tier, workloads and delivery locations, its rank among the account's top providers, and 3 workloads where it is thinnest.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the 10 most recent engagements between [Company] and [Competitor], with month, workload and delivery location.
```

```text
Which executives at [Company] own the wedge workloads?
```

```text
Draft a 3-bullet 'why a second vendor' point of view for the wedge workloads.
```

## Tips for better results

- Spell provider names as Draup does. If a name returns nothing, try the short brand name.
- A thin footprint in a workload you lead is usually a better wedge than attacking the competitor's core.

## Related prompts

- [Outsourcing footprint and incumbents](../../prompts/06-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated its provider base is, and which workloads are ripe for vendor consolidation.
- [Competitor's customers in my vertical](../../prompts/06-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your vertical and country, with how entrenched it is at each: your displacement targets.
- [Battlecard: rival services firm](../../prompts/09-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers, what it wins, recent moves, how to beat it, trap questions and the objection to expect.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_deals_workloads_v3`

Status: **tested live**. Prompt id: `services-competitor-at-account`.

</details>

[Back to Outsourcing and services deals](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
