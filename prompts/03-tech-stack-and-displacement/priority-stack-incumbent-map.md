[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who's already working each priority

> **For each stated priority in one function: the tools linked to it, the service providers working it, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Shaping an account strategy or a displacement campaign, before you pick an entry point. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Partnerships & Alliances | Everyone | 4–6 min | Priorities & opportunities, Tech stack, Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Business function]` | Supply Chain |
| `[What I sell]` | supply-chain planning software |
| `[I sell]` | software (or services) |
| `[Competitor]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Business function: [e.g. Supply Chain, IT]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- I sell: [software or services, e.g. software — skip if you ran the start-here prompt]
- Competitor: [optional vendors or services firms, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull stated priorities in [Business function], re-sorted newest first yourself. Keep up to 8. If none, try the closest function and say so.
3. For each: workloads, source and quarter, up to 6 linked tools, up to 6 linked providers.
4. Pull the stack once, filtered to the makers of [Competitor] and the linked tools. For very broad makers (Microsoft, Amazon, Google), look them up separately within the priorities' areas, because a single combined pull can cut off their products. Keep tools with a usage strength seen in 12 months; drop generic labels and non-software partners.
5. Leave staffing, BPO, agency, market-research and merchandising firms out of the plays.
6. Tag each priority. Software seller: Displace = a competitor product is active in its workloads or linked; Co-sell = an IT services firm works it; Greenfield = nothing relevant. Services seller: Displace = a rival services firm works it; Co-sell = an active, linked software product needs services; Greenfield = nothing relevant. Else Not ours.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table (newest first): Priority | Source and quarter | Workloads | Linked tools (strength, last seen) | Providers | Play | Likely owner.
- "Top 3 plays": priority, incumbent or partner, opening.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Provider links are Draup-derived outsourcing records, not public contracts.
- If the same few integrators appear on every priority, call it weak evidence; don't tag every row Co-sell.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- Rank providers by engagements yourself; Draup may return them alphabetically.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Check the whole tech stack for any product made by [Competitor], whatever area it's filed under. If [Competitor] is a product (e.g. Google BigQuery), record the product and its maker.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Tools and providers are linked to a priority by workload, not confirmed on it. Say "linked", never "used for". Quarter labels follow the company's fiscal year and can run ahead of the calendar; say so once.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Map [Company]'s [Business function] priorities to the tools and service providers linked to each. Check the stack for [Competitor] products, and tag each priority Displace, Co-sell, Greenfield or Not ours for a [software / services] seller.
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
Turn the top play into a one-page point of view for the function head.
```

## Tips for better results

- A priority with no linked tools or providers is often greenfield: an easier place to be first.
- Set "I sell" correctly. A services firm on a priority is a partner for a software seller but the incumbent for a services seller.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.
- [A competitor's footprint at an account](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`

Status: **tested live**. Prompt id: `tech-priority-stack-incumbent-map`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
