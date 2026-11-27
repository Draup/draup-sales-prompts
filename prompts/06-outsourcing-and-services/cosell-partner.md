# Pick a co-sell partner

**A shortlist of service partners already delivering your workload at the account and experienced with your technology, with the one to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell software and want a GSI or SI partner (global or regional systems integrator) to open or accelerate a deal. | Partnerships & Alliances, Account Executive, Presales & Solutions | Software sellers | 2–4 min | Outsourcing deals, Tech stack |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Workload]` | Data Engineering |
| `[Technology]` | Snowflake |
| `[What I sell]` | Snowflake-native data observability software |
| `[Our current partners (optional)]` | Tailspin Partners |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my partner and alliances manager. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Workload: [Draup workload, e.g. Data Engineering]
- Technology: [Our product or platform as Draup names it, e.g. Snowflake]
- What I sell: [One line, e.g. Snowflake-native data observability software — skip if you ran the start-here prompt]
- Our current partners: [Optional, e.g. Tailspin Partners]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary vertical.
2. Pull the top 10 providers delivering [Workload] at the account, leaving out agencies and staffing firms.
3. For the top 5 (plus current partners in the top 10), pull relationship tier and delivery locations.
4. Pull the top 10 providers whose engagements involve [Technology] in the account's primary vertical, worldwide.
5. Check the account's whole tech stack for [Technology], with last-seen date and usage strength.

OUTPUT
- Bottom line: 2 sentences — the partner to call first and why.
- "Shortlist": Partner | Current partner? | [Workload] engagements here | Tier | [Technology] engagements in vertical | Verdict.
- Verdict: Lead co-sell (here and [Technology]-skilled), Access partner (here, little [Technology]), Skills partner ([Technology]-skilled, not here) or Skip. Current partners first.
- "Call first": one partner, three reasons tied to numbers.
- "Is [Technology] already there?": installed (last seen, strength) or not seen — expand or land.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If [Technology] returns nothing, retry with the vendor or product family name and say which worked.
- A strategic tier means access and possibly loyalty to a rival product; note it, don't assume it.

STANDARD RULES (leave as is)
- Rank providers by engagements yourself; Draup may return them alphabetically.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Which service providers deliver [Workload] at [Company] in Draup, how entrenched are they, and which have [Technology] experience in its industry? Rank them, putting our current partners first, and pick the one to call first.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a short note to [Partner]'s account lead proposing a joint approach.
```

```text
Which other accounts in [Vertical] does [Partner] serve in [Workload]?
```

```text
Map [Company]'s priorities in the workload so we can pitch jointly.
```

## Tips for better results

- The best co-sell partner is often already inside the account in the workload, even if it isn't the biggest provider overall.
- Ask for the partner's other accounts in the industry to build a joint pipeline, not just one deal.

## Related prompts

- [Who to partner with vs replace, by priority](../../prompts/06-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it, and whether to partner, displace or walk into an open door.
- [Profile a services firm (rival or partner)](../../prompts/06-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner).
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `services-cosell-partner`.

</details>

[Back to Outsourcing and services deals](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
