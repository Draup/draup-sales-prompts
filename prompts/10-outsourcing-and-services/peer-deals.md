[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Peer deals for social proof

> **Recent outsourcing engagements at the prospect's peers in the workload you sell, plus ready-to-use proof lines.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need "companies like you are already doing this" evidence for an email, a deck or a first call. | Services, SI & Staffing Seller, Account Executive, Marketing & ABM | Services sellers | 2–4 min | Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Workload]` | Software Testing |
| `[My company (optional)]` | Northwind Data Services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales researcher building social proof for a services pitch. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Workload: [Draup workload, e.g. Software Testing]
- My company: [Optional, our services firm as Draup spells it, e.g. Northwind Data Services]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary vertical and HQ country.
2. Pull [Workload] engagements at other companies with the same primary vertical and HQ country. Keep the 10 most recent: month, customer, provider, delivery location, one-line description. If fewer than 5, widen to the vertical worldwide and say so.
3. Merge near-duplicates (same customer, provider and work within a quarter).
4. If My company is given, pull our [Workload] engagements in the same vertical, newest first, as reference candidates.

OUTPUT
- Bottom line: 2 sentences — how common this work is among peers and the strongest proof angle.
- "Peer engagements": Month | Customer | Provider | Delivery location | What the work was. Newest first.
- "Who peers use": providers appearing most often, with counts.
- "Our references" (only if My company is given): Month | Customer | What the work was.
- "Proof lines": 3 sentences of 25 words or fewer. Name companies only where I say it's allowed; otherwise describe them by size and industry.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- These are Draup-derived records, paraphrased, with month-level dates. Never present them as quotes, press releases or signed contracts.
- If I ask for public references only, keep engagements Draup marks as publicly reported.
- Leave agencies, staffing, market-research and merchandising firms out of provider lists.

STANDARD RULES (leave as is)
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Find the 10 most recent [Workload] outsourcing engagements at [Company]'s peers (same primary vertical and HQ country) in Draup: month, customer, provider, what the work was. Then write 3 proof lines I can use.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the proof lines into a 90-word email to the head of quality engineering.
```

```text
Which of these peers are also our customers? Here is our list: [Our customers].
```

```text
Show the same for [another Workload].
```

## Tips for better results

- Engagement records have month-level dates. Use them to show a pattern, not to quote a specific contract.
- Describing peers by size and industry is often safer than naming them.

## Related prompts

- [A competitor's footprint at an account](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.
- [Map my offering to buyers](../../prompts/10-outsourcing-and-services/offering-to-buyers.md): Your offering mapped to Draup workloads you approve, then the 20 companies in your territory that outsource them most, with their incumbents and where the provider mix is fragmented.
- [Signal-to-email (one or a few accounts)](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 5 per pass: the freshest relevant signal, the priority it supports, and a short, sourced opener for your persona that ends in one low-friction ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_deals_landing_data`, `get_deals_customer_v3`, `get_deals_service_provider_v3`

Status: **tested live**. Prompt id: `services-peer-deals`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
