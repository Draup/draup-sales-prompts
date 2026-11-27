# Profile a services firm (rival or partner)

**A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner).**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a competitive bid, when a new rival keeps showing up, or before approaching a firm as a partner. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Marketing & ABM | Everyone | 2–4 min | Outsourcing deals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Firm]` | Cognizant |
| `[Rival or partner]` | Rival |
| `[Vertical or Country]` | Life Sciences |
| `[What I sell]` | clinical data management and testing services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my competitive and alliances analyst for services deals. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Firm: [Services firm, e.g. Cognizant]
- Rival or partner: [e.g. Rival]
- Vertical or Country: [Required. Draup industry, e.g. Life Sciences, or HQ country in full]
- What I sell: [One line, e.g. clinical data management and testing services — skip if you ran the start-here prompt]

STEPS
1. Find the firm by website or name; confirm Draup's spelling and that it is the parent.
2. Pull its customer summary: active customers, engagements, main verticals.
3. Pull its top 10 customers and top 10 workloads by engagements, overall and within [Vertical or Country], from the full rankings.
4. Pull its delivery locations, always limited to [Vertical or Country]. Keep the top 10 metros and group them onshore (customers' country), nearshore (same region) or offshore.

OUTPUT
- Bottom line: 2 sentences — how strong [Firm] is in this segment and what that means for [What I sell].
- Header: [Firm] | active customers | engagements | top 3 verticals.
- "Top customers": Rank | Customer | Engagements overall | In segment.
- "Workloads": Workload | Engagements overall | In segment.
- "Delivery hubs": Metro | Country | Engagements | Onshore/Nearshore/Offshore, plus the % split.
- Rival: "How to out-position [Firm]" — 3 angles tied to facts (thin where we lead, offshore-heavy, few big logos).
- Partner: "Where to team" — 3 angles tied to facts (workloads it lacks that we cover, shared customers, complementary hubs).
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never pull delivery locations without the vertical or country limit; the unfiltered list is too large.
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Profile [Firm] from Draup: customers and engagements, top 10 customers and workloads overall and in [Vertical or Country], top 10 delivery hubs with onshore/offshore split, then 3 out-position angles (rival) or 3 teaming angles (partner).
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which [Vertical] companies in [Country] use [Firm] most and look contestable?
```

```text
Show [Firm]'s footprint at [Company].
```

```text
Turn the three angles into a one-page battlecard, or a partner intro note.
```

## Tips for better results

- Compare the overall and in-segment columns: a firm that is huge overall can be thin in your vertical.
- For partners, overlap in customers matters more than size. Shared accounts are where a joint pitch lands.

## Related prompts

- [Competitor's customers in my vertical](../../prompts/06-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your vertical and country, with how entrenched it is at each: your displacement targets.
- [Pick a co-sell partner](../../prompts/06-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account and experienced with your technology, with the one to call first.
- [Battlecard: rival services firm](../../prompts/09-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers, what it wins, recent moves, how to beat it, trap questions and the objection to expect.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_customers_summary_v3`, `get_deals_customer_v3`, `get_deals_workloads_v3`, `get_deals_service_provider_location_v3`

Status: **tested live**. Prompt id: `services-competitor-profile`.

</details>

[Back to Outsourcing and services deals](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
