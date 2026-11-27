[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Joint account plan with a partner

> **A one-page plan you and a partner can both sign up to for one account: where the partner already works in your function, the priorities there, your technology's and a rival's position, who to meet and a 90-day plan with owners on both sides.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| After you've picked a co-sell partner for an account and need a shared plan before the joint kickoff call. Use services-cosell-partner instead if you haven't picked the partner yet. | Partnerships & Alliances, Account Executive, Services, SI & Staffing Seller, Presales & Solutions | Everyone | 4–6 min | Outsourcing deals, Priorities & opportunities, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | allianz.com |
| `[Partner]` | Capgemini |
| `[Our technology]` | Snowflake |
| `[Competitor (optional)]` | Databricks |
| `[Business function]` | IT |
| `[What I sell]` | data quality and observability software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my alliance manager. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. allianz.com]
- Partner: [Services firm as Draup spells it, e.g. Capgemini]
- Our technology: [Our product or its maker as Draup names it, e.g. Snowflake]
- Competitor (optional): [Rival maker, e.g. Databricks]
- Business function: [Where the buyers sit, e.g. IT]
- What I sell: [One line, e.g. data quality and observability software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary. Use Draup's exact name from then on.
2. Pull the account's top 10 providers, once limited to [Business function] and once for the whole account; note [Partner]'s rank and engagements in each.
3. Pull [Partner]'s engagement detail at the account (workloads, tier, locations) and its engagements per workload. Pick up to 3 joint workloads closest to [What I sell], skipping catch-alls.
4. Pull priorities in the joint workloads, newest first; keep the 5 most relevant with source and quarter, noting whether [Partner] or our tools are linked.
5. Check the whole tech stack for products made by [Our technology] and [Competitor], whatever area they're filed under: usage strength and last seen. Rate [Competitor]: Red for High usage in the workloads I sell into; Amber for Medium usage there or anything newly detected in 12 months; otherwise Green, still listed.
6. Pull 10 leaders in [Business function]; keep up to 4, preferring group-level people, and label each person's unit.
7. Timing: from the last 90 days of news, keep at most 2 reasons to act now (skip the account's own product launches).

OUTPUT
- Bottom line: 2 sentences — the joint play and why it beats either firm alone.
- Recommended next step: one person from step 6 (name and title), who opens (us or [Partner]), and why now (a step-7 item). If none turned up, say so.
- "Joint workloads": Workload | [Partner] engagements | Linked priorities | [Our technology] status | [Competitor] rating.
- "90-day plan": Days | Action | Our owner (role) | [Partner] owner (role) | Done when — for days 1–30 (align, access), 31–60 (discovery, proof) and 61–90 (joint proposal).
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: "Partner position" (rank and engagements in function and total, tier, locations); "Priorities to pitch together" (Priority | Quarter | [Partner] linked? | Joint play | Likely owner); "People" (Name | Full title | Unit | Who opens).

RULES
- If [Partner] has fewer than 3 engagements in the joint workloads (editable default), call the plan partner-light and name the best-placed provider in those workloads.
- A strategic-tier partner protects its scope: position [What I sell] as speeding its delivery.
- If [Competitor] is rated Red, plan for a bake-off or a coexist position and say which.
- Links between priorities and tools or providers are by workload: say "linked", never "used for".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- If [Company] sells technology, drop priorities and tools about its own products.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 480 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named leader, dated why-now) first. Joint plan for [Company] with [Partner]: its engagements in [Business function] vs total, joint workloads and priorities, [Our technology] and [Competitor] in the stack, and a 90-day plan.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the plan into a one-slide summary for the joint kickoff call.
```

```text
Draft the email from me to [Partner]'s client lead proposing the kickoff, under 120 words.
```

```text
Show the next 10 leaders in [Business function], with full titles.
```

## Tips for better results

- Send the partner the joint-workloads table before the kickoff; it shows you've done homework on their account, not just yours.
- A partner that is big at the account can still be light in your function. The plan checks both counts and says when the partner is light.

## Related prompts

- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Which providers to partner with or replace](../../prompts/10-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- [Enablement brief for a partner's sellers](../../prompts/13-partners-and-alliances/enablement-brief.md): A brief you hand to a partner's sales team: where your product fits their practice in your industry, which of their customers run your platform or a rival's, a joint value proposition, 5 qualification questions and 3 objection handlers.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_deals_workloads_v3`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `partners-joint-account-plan`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
