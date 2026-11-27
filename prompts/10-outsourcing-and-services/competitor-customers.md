[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Competitor's customers in my vertical

> **A ranked list of a rival's customers in your vertical and country, with how entrenched it is at each: your displacement targets.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are building a displacement campaign against one services competitor in one vertical. | Services, SI & Staffing Seller, Account Executive, SDR / BDR, Sales Leader & RevOps | Services sellers | 2–4 min | Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | Capgemini |
| `[Vertical]` | Life Sciences |
| `[Country]` | United States of America |
| `[Workload (optional)]` | Data Engineering |
| `[What I sell]` | clinical data and analytics managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my displacement-campaign analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [Services firm, e.g. Capgemini]
- Vertical: [Draup industry, e.g. Life Sciences]
- Country: [Customer HQ country in full, e.g. United States of America]
- Workload: [Optional, e.g. Data Engineering; blank for all]
- What I sell: [One line, e.g. clinical data and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Confirm Draup's spelling of the competitor, vertical and country. Use each customer's primary vertical so loosely tagged companies don't slip in.
2. Pull the competitor's customers in that primary vertical with HQ in that country (and workload, if given), by engagements. Keep the top 20.
3. For the top 8, pull each account's provider ranking: total engagements, the competitor's rank and share, and the provider just above or below it.
4. Pull the competitor's top 5 workloads in this vertical and country.

OUTPUT
- Bottom line: 2 sentences — how big [Competitor] is here and which accounts to attack first.
- Headline: "[Competitor] has N customers and X engagements in [Vertical], [Country]", plus its top 5 workloads.
- "Targets" (top 20): Rank | Customer | Engagements with competitor | Share of account | Rank at account | Other major provider | Read.
- Read: Entrenched (#1 or above 30%), Contestable (10–30%), Foothold (below 10%) — editable defaults. Rows 9–20: "not assessed".
- "Best 3 to target": assessed Contestable or Foothold accounts with the most engagements, one line each.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Flag customers that look misclassified or are the competitor's own subsidiaries; leave them out of Best 3.
- If fewer than 5 customers come back, drop the workload, then widen the country to its region, and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which [Vertical] companies headquartered in [Country] use [Competitor] most, per Draup? Top 20 by engagements, its share and rank at the top 8, and which accounts look contestable.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show [Competitor]'s footprint and wedge workloads at the first account in Best 3.
```

```text
Assess rows 9–16 the same way.
```

```text
Write a 3-email displacement sequence for the CIO at the top Contestable account.
```

## Tips for better results

- Use the full country name, e.g. United States of America.
- A Contestable account is often easier to win than one where the competitor is the main partner.

## Related prompts

- [A competitor's footprint at an account](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.
- [Profile a services firm (rival or partner)](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner).
- [Battlecard: rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers, what it wins, recent moves, how to beat it, trap questions and the objection to expect.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_deals_customer_v3`, `get_deals_service_provider_v3`, `get_deals_workloads_v3`

Status: **tested live**. Prompt id: `services-competitor-customers`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
