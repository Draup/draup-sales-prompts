[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find the biggest buyers of my service

> **Your offering mapped to Draup workloads you approve, then the 20 companies in your territory that outsource them most, their incumbents, where the provider mix is fragmented, and who to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a new service line or practice, or want the biggest buyers of one type of work in an industry or country. | Services, SI & Staffing Seller, Marketing & ABM, Sales Leader & RevOps, SDR / BDR, Partnerships & Alliances | Services sellers | 4–6 min | Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[What I sell]` | We modernise legacy mainframe and .NET applications to cloud-native, then run them as a managed service. |
| `[Country or Vertical]` | Germany |
| `[Workload (optional)]` | Application Development & Maintenance |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my go-to-market analyst for a services practice. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- What I sell: [One paragraph, e.g. We modernise legacy mainframe and .NET applications to cloud-native, then run them as a managed service.]
- Country or Vertical: [Required. HQ country in full, e.g. Germany, or a Draup industry, e.g. Banking & Financial Services]
- Workload (optional): [If you know the Draup name, e.g. Application Development & Maintenance; skips the mapping]

STEPS
1. If Workload is given, confirm it and go to step 3. Otherwise map [What I sell] to up to 8 Draup workloads (types of work), each Strong, Partial or Doubtful with a 5-word reason. Automatic mapping can be loose; judge each.
2. Stop for me to confirm or prune (if I said "don't wait", use Strong only).
3. Pull the top 20 companies outsourcing the confirmed workloads in [Country or Vertical] (primary industry; HQ country). Remove IT services firms, consultancies, staffing firms, agencies and investors.
4. Pull the top 10 providers in the same segment, with share.
5. For the top 10 buyers, pull their top 3 providers in those workloads. Rows 11–20: "not checked".
6. People and timing: at the top buyer in "Where to play", pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- "Workload mapping" (shown first, before the list): Workload | Fit | Reason.
- Bottom line: 2 sentences — segment size and where to start.
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Target list" (top 10): Rank | Company | Engagements | Main incumbent (share) | Fragmented?
- Fragmented = no provider above 40% of that buyer's work in these workloads (editable default).
- "Where to play": 3–5 fragmented or broadest buyers, one line each.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: rows 11–20 and "Segment providers" (Rank | Provider | Engagements | % of segment).

RULES
- Never run the list without a country or industry; unlimited, it returns only global megacaps.
- Never map to catch-all workloads such as Account Management.
- Flag companies that look misclassified; leave them out of Where to play.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Rank providers by engagements yourself.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Map [What I sell] to Draup workloads for me to approve. Then give the bottom line, a named first call, and the 20 companies in [Country or Vertical] outsourcing that work most, with main incumbent and fragmentation.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Add Draup's Opportunity Index score for each company and re-rank.
```

```text
For the top 5, who owns these workloads?
```

```text
Show peer engagements in the confirmed workloads I can use as social proof.
```

```text
Format this as a target list I can paste into my CRM (company, website, reason).
```

## Tips for better results

- Check the workload mapping before the list is built. One wrong workload can fill the list with the wrong companies.
- A country or industry keeps the list from leaning toward global megacaps.

## Related prompts

- [Peers' outsourcing deals for social proof](../../prompts/10-outsourcing-and-services/peer-deals.md): Recent outsourcing engagements at the prospect's peers in the work you sell, ready-to-use proof lines, and who to send them to and why now.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_relevant_workloads`, `get_deals_customer_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-offering-to-buyers`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
