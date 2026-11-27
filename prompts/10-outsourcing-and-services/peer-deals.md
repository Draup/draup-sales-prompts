[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Peers' outsourcing deals for social proof

> **Recent outsourcing engagements at the prospect's peers in the work you sell, ready-to-use proof lines, and who to send them to and why now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need "companies like you are already doing this" evidence for an email, a deck or a first call. | Services, SI & Staffing Seller, Account Executive, Marketing & ABM | Services sellers | 2–4 min | Outsourcing deals, Executives & movement, News signals |

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
- Workload: [Draup workload, e.g. Software Testing; a business function like Quality is fine, I'll map it]
- My company (optional): [Our services firm as Draup spells it, e.g. Northwind Data Services]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary industry and HQ country.
2. If I gave a business function, map it to its 1–2 main workloads and say which. Pull engagements in those workloads at other companies with the same primary industry and HQ country. Keep the 10 most recent: month, customer, provider, delivery location, one-line description. If fewer than 5, widen to the industry worldwide and say so.
3. Merge near-duplicates (same customer, provider and work within a quarter). Drop agencies, staffing firms and investors listed as customers.
4. If My company is given, pull our engagements in those workloads in the same industry, newest first, as reference candidates.
5. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — how common this work is among peers and the strongest proof angle.
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Peer engagements": Month | Customer | Provider | What the work was. Newest first.
- "Proof lines": 3 sentences of 25 words or fewer. Name companies only where I say it's allowed; otherwise describe them by size and industry.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Who peers use" (providers with counts) and "Our references" (Month | Customer | What the work was), if My company is given.

RULES
- These are Draup-derived records, paraphrased, with month-level dates. Never present them as quotes, press releases or signed contracts.
- If I ask for public references only, keep engagements Draup marks as publicly reported.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell. Where a workload is needed and I gave a function, map it to its 1–3 main Draup workloads and say which.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 400 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Find the 10 most recent [Workload] engagements at [Company]'s peers (same industry and HQ country) in Draup: month, customer, provider, the work. Then write 3 proof lines.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the proof lines into a 90-word email to the person in the next step.
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

- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Find the biggest buyers of my service](../../prompts/10-outsourcing-and-services/offering-to-buyers.md): Your offering mapped to Draup workloads you approve, then the 20 companies in your territory that outsource them most, their incumbents, where the provider mix is fragmented, and who to call first.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_deals_landing_data`, `get_deals_customer_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-peer-deals`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
