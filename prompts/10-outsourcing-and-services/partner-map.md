[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who to partner with vs replace, by priority

> **For each priority in one function, the providers and tech vendors linked to it, and whether to partner, displace or walk into an open door.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are deciding who to partner with and who you'd be replacing at an account. | Partnerships & Alliances, Services, SI & Staffing Seller, Account Executive | Everyone | 2–4 min | Priorities & opportunities, Outsourcing deals, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Business function]` | IT |
| `[I sell]` | software |
| `[What I sell]` | AI and automation platform |
| `[Our current partners (optional)]` | Tailspin Partners |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my alliances and pursuit strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Business function: [e.g. IT, Supply Chain]
- I sell: [software, services or both — skip if you ran the start-here prompt]
- What I sell: [One line, e.g. AI and automation platform — skip if you ran the start-here prompt]
- Our current partners: [Optional, e.g. Tailspin Partners]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull priorities in [Business function], sort by date yourself, and keep the 8 most relevant to [What I sell], with source and quarter.
3. For each, list up to 4 linked providers and 4 linked products. Skip the account's subsidiaries and, if it sells technology, its own products.
4. Pull the account's provider ranking once and read each linked provider's engagements from it.
5. Tag each Partner (complements what I sell), Displace (does what I sell) or Neutral, using I sell: for software sellers, services firms are usually Partners.

OUTPUT
- Bottom line: 2 sentences — who to team with and who you'd replace.
- "Priority map": Priority | Source and quarter | Linked providers (engagements) | Linked tech | Play | Likely owner (title).
- Play: Partner-led, Displacement, or Open (nothing linked, or only providers with 2 engagements or fewer, editable default).
- "Best partners to call": up to 3, our current partners first, with why.
- "Who we'd displace": up to 3, with engagements.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave agencies, staffing, market-research and merchandising firms out of provider lists.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Tools and providers are linked to priorities by workload, not confirmed: say "linked", never "used for". Quarter labels follow the fiscal year and can run ahead of the calendar.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
For [Company]'s top 8 priorities in [Business function], which service providers and tech vendors are linked to each in Draup? Tag each Partner, Displace or Neutral for [What I sell] and give a play per priority.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Pick the best co-sell partner for the top Open priority.
```

```text
Show the buying committee for [Business function].
```

```text
Draft a note to the partner's account lead proposing a joint approach.
```

## Tips for better results

- A provider linked to a priority works in the same workloads; it has not necessarily won that initiative. Check its engagement count before pitching a partnership.
- Open priorities with no strong incumbent are often the quickest entry.

## Related prompts

- [Pick a co-sell partner](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account and experienced with your technology, with the one to call first.
- [Entry points and whitespace](../../prompts/11-account-planning/entry-points.md): The five best ways into the account for what you sell, each with dated evidence, incumbents and the likely owner.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools linked to it, the service providers working it, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_deals_service_provider_v3`

Status: **tested live**. Prompt id: `services-partner-map`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
