[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Battlecard: beat a rival services firm

> **A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A services rival keeps showing up in your pursuits, or you're preparing a team for a competitive bid or renewal. Selling software? Use "Battlecard: beat a rival software vendor" instead. | Services, SI & Staffing Seller, Account Executive, Presales & Solutions, Marketing & ABM | Services sellers | 4–6 min | Outsourcing deals, Company & financials, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | infosys.com |
| `[What I sell]` | SAP S/4HANA migration and managed services |
| `[Vertical (optional)]` | Automotive |
| `[Where we lose to them (optional)]` | lost the Contoso Retail bid on offshore price |
| `[Proof we can cite (optional)]` | halved SAP ticket backlog at Fabrikam Foods |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive analyst for services pursuits. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [rival services firm's website, e.g. infosys.com]
- What I sell: [one line, e.g. SAP S/4HANA migration and managed services — skip if you ran the start-here prompt]
- Vertical (optional): [e.g. Automotive]
- Where we lose to them (optional): [paste win/loss notes, e.g. lost on offshore price]
- Proof we can cite (optional): [e.g. halved SAP ticket backlog at Fabrikam Foods]

CONTEXT (optional)
Whole-firm totals flatter a big rival; the numbers that matter are in my workloads (types of work, e.g. ERP Implementation).

STEPS
1. Find [Competitor] by website and confirm it is the parent, not a subsidiary or brand; if unclear, ask me. Map What I sell to its 1–3 main workloads and say which.
2. Pull HQ, workforce, and latest fiscal-year revenue and growth (in USD).
3. Pull its top 10 customers by active engagements in my workloads (primary industry [Vertical] if given), and the firm-wide top 10 for contrast. Show both counts.
4. Pull its top 8 workloads overall and its top 3 delivery locations from the firm's summary (the full location list is very long).
5. Search 180 days of news on them (deals, acquisitions, leadership); review 30+ items.
6. Pick the first account to use the card on: a top-10 customer in my workloads where they hold few engagements (3 or fewer, editable default). Pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — their size and strength in my workloads, and where [What I sell] can win.
- Recommended next step: the first account, who to contact (name and title from step 6), what to do, and the dated fact. If none is found, say so.
- "Where they deliver my work": Customer | Industry | Engagements in my workloads / total. Top 10.
- "How we win": 3 angles tied to facts above and [Proof we can cite]; one landmine where they're strongest.
- "Trap questions": 3 discovery questions that surface their weak spots without naming them.
- "Objection to expect": their likely claim and a one-line, data-backed reply.
- Detail: what they win (workload, engagements); delivery hubs; recent moves (date, move, source, why it matters; up to 6); "Where we lose" counters for each pattern in my notes.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never build an angle on catch-all workloads (Project/Programs Management, Account Management).
- Mark the card "Internal use": customer lists are for targeting, not for quoting to clients.
- Claim no results beyond [Proof we can cite].

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- Engagements are "active engagements (Draup-derived)": activity estimates, not contracts or headcount.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: internal battlecard on [Competitor] for [What I sell] — top customers in my workloads, 180 days of moves, three ways we win, three trap questions, and the first account to use it on.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which of my target accounts already use [Competitor]? Check [Accounts], 5 at a time.
```

```text
Turn 'How we win' and the trap questions into a 90-second talk track for a discovery call.
```

```text
Build the same card for the services rival we meet second most, and compare the two side by side.
```

```text
Show [Competitor]'s engagement trend in my workloads at [Account].
```

## Tips for better results

- Paste your win/loss notes. The 'Where we lose' section is often the part reps use most.
- Read the 'in my workloads / total' column: a rival with hundreds of engagements firm-wide can be thin in your area.

## Related prompts

- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [A rival's customers you can win](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `accounts_customers_summary_v3`, `get_deals_customer_v3`, `get_deals_workloads_v3`, `get_deals_service_provider_location_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `get_news_feed_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `content-battlecard-services`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
