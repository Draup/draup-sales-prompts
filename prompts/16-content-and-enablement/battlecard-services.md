[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Battlecard: rival services firm

> **A one-page internal battlecard on a rival services firm: where it delivers, what it wins, recent moves, how to beat it, trap questions and the objection to expect.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A services rival keeps showing up in your pursuits, or you're preparing a team for a competitive bid or renewal. | Services, SI & Staffing Seller, Account Executive, Presales & Solutions, Marketing & ABM | Services sellers | 4–6 min | Outsourcing deals, Company & financials, News signals |

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

STEPS
1. Find [Competitor] by website and confirm it is the parent, not a subsidiary or brand. If unclear, ask me.
2. Pull HQ, workforce, and latest fiscal-year revenue and growth.
3. Pull total customers and engagements, then the top 10 customers by engagements (primary industry [Vertical] only, if given).
4. Pull their top 8 workloads, and their top 3 delivery locations from the firm's summary (the full location ranking is very long).
5. Search Draup's news on them (last 180 days: deals, acquisitions, leadership), then the news feed for links. Review 30+ items.

OUTPUT
- Bottom line: 2 sentences — their size and strength, and where [What I sell] can win.
- "Where they deliver": Rank | Customer | Primary industry | Engagements | Likely owner. Top 10, most first.
- "What they win": Workload | Engagements. Top 8.
- "Recent moves": up to 6 rows, Date | Move | Source | Why it matters.
- "How we win": 3 angles tied to facts above and [Proof we can cite]; one landmine where they're strongest.
- "Where we lose": a counter for each pattern in my notes, if given.
- "Trap questions": 3 discovery questions that surface their weak spots without naming them.
- "Objection to expect": their likely claim and a one-line, data-backed reply.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never build an angle on catch-all workloads (Project/Programs Management, Account Management).
- Mark the card "Internal use": customer lists are for targeting, not for quoting to clients.
- Claim no results beyond [Proof we can cite].

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Engagements are Draup-derived estimates, not public contracts. Never call them signed deals.
- Show USD millions using Draup's conversion rate and show the original currency once. If Draup gives no rate, name the rate and date and mark it as outside Draup.
- Drop news noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Merge items about the same event and keep the earliest. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Build an internal Draup battlecard on services rival [Competitor]: top 10 customers by engagements, top workloads, 180 days of moves, three ways [What I sell] wins, three trap questions and the objection to expect.
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

## Tips for better results

- Paste your win/loss notes. The 'Where we lose' section is often the part reps use most.
- Narrow to one vertical when the rival is very large; the customer list is sharper and closer to your deals.

## Related prompts

- [Battlecard: rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest companies running them, recent moves, how to beat it and the objection to expect.
- [Profile a services firm (rival or partner)](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner).
- [Competitor's customers in my vertical](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your vertical and country, with how entrenched it is at each: your displacement targets.
- [A competitor's footprint at an account](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account, how it delivers, and the workloads where it is weakest: your wedge.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `accounts_customers_summary_v3`, `get_deals_customer_v3`, `get_deals_workloads_v3`, `get_deals_service_provider_location_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `get_news_feed_v3`

Status: **tested live**. Prompt id: `content-battlecard-services`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
