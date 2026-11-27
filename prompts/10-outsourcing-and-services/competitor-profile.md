[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Profile a services firm, rival or partner

> **A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a competitive bid, when a new rival keeps showing up, or before approaching a firm as a partner. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Marketing & ABM | Everyone | 2–4 min | Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Firm]` | Cognizant |
| `[Rival or partner]` | Rival |
| `[Vertical or Country]` | Life Sciences |
| `[What I sell]` | clinical data management and testing services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive and alliances analyst for services deals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Firm: [Services firm, e.g. Cognizant]
- Rival or partner: [e.g. Rival]
- Vertical or Country: [Required. Draup industry, e.g. Life Sciences, or customer HQ country in full]
- What I sell: [One line, e.g. clinical data management and testing services — skip if you ran the start-here prompt]

STEPS
1. Find the firm by website or name; confirm Draup's spelling and that it's the parent. If a sister brand also matches, list it separately.
2. Pull its customer summary: active customers, engagements, main industries.
3. Pull its top 10 customers and top 10 workloads by engagements, overall and within [Vertical or Country].
4. Pull its delivery locations, always limited to [Vertical or Country]. Keep the top 10 metros and group them onshore (customers' country), nearshore (same region) or offshore.
5. People and timing: pull the most important news from the last 90 days where [Firm] is the actor (client wins, acquisitions, alliances). Partner: pull [Firm]'s top 3 leaders for [Vertical or Country] or alliances. Rival: pull the top 3 leaders, in the function closest to [What I sell], at its largest in-segment customer, where a displacement play would start.

OUTPUT
- Bottom line: 2 sentences — how strong [Firm] is in this segment and what that means for [What I sell].
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Header line: [Firm] | active customers | engagements | top 3 industries.
- "Top customers": Rank | Customer | Engagements overall | In segment.
- Rival: "How to out-position [Firm]" — 3 angles tied to facts (thin where we lead, offshore-heavy, few big logos). Partner: "Where to team" — 3 angles tied to facts (workloads it lacks that we cover, shared customers, complementary hubs).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Workloads" (Workload | Overall | In segment) and "Delivery hubs" (Metro | Country | Engagements | Onshore/Nearshore/Offshore, plus the % split).

RULES
- Never pull delivery locations without the industry or country limit; the full list is too large.
- Show catch-all workloads (Project/Programs Management, Account Management) but never recommend them.
- Analyst rankings and awards are context, never a why-now.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 430 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Profile [Firm] from Draup: customers and engagements, top customers and workloads overall and in [Vertical or Country], delivery hubs with onshore share, then 3 out-position (rival) or teaming (partner) angles.
```

</details>

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

- Compare the overall and in-segment columns: a firm that is huge overall can be thin in your industry.
- For partners, overlap in customers matters more than size. Shared accounts are where a joint pitch lands.

## Related prompts

- [A rival's customers you can win](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.
- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_customers_summary_v3`, `get_deals_customer_v3`, `get_deals_workloads_v3`, `get_deals_service_provider_location_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `services-competitor-profile`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
