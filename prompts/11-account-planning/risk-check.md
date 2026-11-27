[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Renewal risk check (red, amber, green)

> **A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| About 90 days before a renewal, or when a deal goes quiet. Use plan-qbr-prep instead the week before a business review, and signals-change-log for a monthly what-changed log. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps | Everyone | 2–4 min | News signals, Executives & movement, Talent flow & locations, Company & financials, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Business function]` | Supply Chain |
| `[Sponsor name and title]` | Jane Doe, VP Supply Chain Systems |
| `[Competitor]` | Blue Yonder, Manhattan Associates |
| `[What I sell]` | warehouse automation software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my customer-success risk analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [Our sponsor's function, e.g. Supply Chain]
- Sponsor name and title: [e.g. Jane Doe, VP Supply Chain Systems — a title alone may match several people]
- Competitor: [Products or firms we lose to, e.g. Blue Yonder, Manhattan Associates]
- What I sell: [One line, e.g. warehouse automation software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Sponsor: look for [Sponsor name] among leaders in [Business function] (up to 3 pages of 10) and in recent exits. Red: left. Amber: title or unit changed. If not found, say "not found in Draup", not "left".
3. Senior exits in [Business function], 6 months, narrowed by its main workloads. Red: the sponsor's level or above. Amber: other director-plus. State rows checked and the latest move date.
4. Layoffs, 90 days. Red: touching [Business function] or over 5% of staff. Amber: other. Workforce growth (talent-flow window; state the months): Red below −3%, Amber −3% to 0%. Revenue growth, latest fiscal year: Red below −5% without a divestment, Amber −5% to +2%.
5. Competitor tools: check the whole tech stack for any product made by [Competitor], whatever area it's filed under. Red: a [Competitor] product with High usage in the same workloads as What I sell. Amber: Medium usage in those workloads, or newly detected in the last 12 months. Low usage or other workloads: list it, rate Green.
6. Negative news, 90 days, where [Company] is the actor. Red: a merger, divestment or restructuring touching [Business function]. Amber: other restructuring or cost-cutting, or a new vendor in our category.

OUTPUT
- Bottom line: 2 sentences — overall rating and the risk to act on.
- Recommended next step: the sponsor or another leader from step 2 (name and title), what to do, and why now (the most important dated news item from step 6 or 4); if none turned up, say so.
- Table: Risk | Rating | Evidence | Date | Source. One row each: Sponsor, Senior exits, Layoffs, Workforce growth, Revenue growth, Competitor tools, Negative news.
- "Overall": Red if 2+ Reds, or Red on Sponsor or Competitor tools; Amber if any Red or 2+ Ambers; else Green.
- "Two actions this month", each tied to a row.
- Gaps: what Draup didn't have — worth asking your sponsor.

RULES
- Cut-offs are editable defaults. No rows = Green (unverified). Data unavailable or sponsor not found = Not in Draup, left out of Overall.
- In the Competitor tools row, name each product with its usage and workload.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 400 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Renewal risk on [Company]: Red/Amber/Green for our sponsor [Sponsor name], [Business function] exits, layoffs, growth, [Competitor] tools installed or new in our workloads, negative news; overall rating, 2 actions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who replaced the leader who left, and do we know them?
```

```text
Draft a check-in email to our sponsor that addresses the top risk without alarming them.
```

```text
Run the same check on my other top 5 customers: [Accounts].
```

## Tips for better results

- Give your sponsor's name, not just a title. Big accounts often have several people with the same title.
- "Green (unverified)" means Draup found nothing, not that the risk is zero. Confirm with your sponsor.
- Name the competitor products you actually lose to. An installed rival with High usage in your workload is rated Red, even if it's been there for years.

## Related prompts

- [QBR prep: talking points and asks](../../prompts/11-account-planning/qbr-prep.md): Three talking points and three asks for your business review, built on what changed at the customer in your sponsor's function, set against the outcomes you delivered.
- [Customer alumni now at your targets](../../prompts/11-account-planning/follow-champions.md): Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_executive_movement`, `get_signal_news_v3`, `get_top_signals`, `accounts_talent_flow_top_metrics_v3`, `get_account_financials_v3`, `get_account_tech_stack_products_v3`, `get_tech_stack_trend_v3`

Status: **tested live**. Prompt id: `plan-risk-check`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
