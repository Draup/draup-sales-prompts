[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who's already working each priority

> **For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Use this when you want, priority by priority, which tools and providers are already in place and where to displace, co-sell or go first. Use "Who to partner with vs replace, by priority" instead when you're choosing between named partners, and "Pick a co-sell partner" when you need one integrator for a deal. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Partnerships & Alliances | Everyone | 4–6 min | Priorities & opportunities, Tech stack, Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Business function]` | Supply Chain |
| `[What I sell]` | supply-chain planning software |
| `[I sell]` | software (or services) |
| `[Competitor (optional)]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Business function: [e.g. Supply Chain, IT]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- I sell: [software or services — skip if you ran the start-here prompt]
- Competitor (optional): [vendors or services firms, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Map [Business function] to its main workloads and name them. Pull stated priorities in the function, newest first; keep up to 8. If none, try the closest function and say so.
3. For each priority: workloads, source and quarter, up to 6 linked tools, up to 6 linked providers.
4. Pull the stack once, filtered to the makers of [Competitor] and the linked tools (look up very broad makers such as Microsoft separately). Keep tools with a usage strength seen in 12 months; rate competitor products (see rules).
5. Count each provider's active engagements in the function's workloads, shown as "in [Business function] / total". Leave staffing, BPO, agency and market-research firms out of the plays.
6. Tag each priority. Software seller: Displace = a competitor product is active in its workloads; Co-sell = an IT services firm works it. Services seller: Displace = a rival services firm works it; Co-sell = a linked software product needs services. Either: Greenfield = nothing relevant; else Not ours.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (newest first, up to 8): Priority (quarter) | Incumbent tools (rating) | Providers (in function) | Play | Likely owner.
- "Top 3 plays": priority, incumbent or partner, opening.
- Detail: linked tools with usage strength and last seen; provider engagement counts (in function / total); Gaps (what Draup lacked, to ask in discovery).

RULES
- Provider counts are "active engagements (Draup-derived)", not contracts; rank providers by them yourself.
- If the same integrators appear on every priority, call it weak evidence, not Co-sell everywhere.
- Tools and providers are linked to a priority by workload, not confirmed on it. Say "linked", never "used for".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Check the whole tech stack for products made by [Competitor], whatever area they're filed under; if [Competitor] is a product (e.g. Google BigQuery), record it and its maker.
- Rating: an installed competitor product with High usage in the workloads of What I sell is Red, Medium is Amber, else Green. Newly detected (first seen within 12 months) is a separate Amber signal.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Map [Company]'s [Business function] priorities to the tools and providers linked to each, rate my [Competitor] products, and tag each priority Displace, Co-sell, Greenfield or Not ours.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top Displace priority, how deep is [Competitor]? Show every product with usage strength and last seen.
```

```text
Who owns each of the top 3 priorities? List executives in the matching workloads.
```

```text
Turn the top play into a one-page point of view for the person in the next step.
```

```text
Compare the top two providers head to head in [Business function].
```

## Tips for better results

- A priority with no linked tools or providers is often greenfield: an easier place to be first.
- Set "I sell" correctly. A services firm on a priority is a partner for a software seller but the incumbent for a services seller.
- Provider counts are filtered to your function, so a big agency that works marketing won't look like your supply-chain incumbent.

## Related prompts

- [Which providers to partner with or replace](../../prompts/10-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.
- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`, `accounts_executives_key_executives_v3`, `get_top_signals`, `get_outsourcing_summary_v3`

Status: **tested live**. Prompt id: `tech-priority-stack-incumbent-map`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
