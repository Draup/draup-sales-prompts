[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Map my offering to buyers

> **Your offering mapped to Draup workloads you approve, then the 20 companies in your territory that outsource them most, with their incumbents and where the provider mix is fragmented.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a new service line or practice, or want the biggest buyers of one workload in a vertical or country. | Services, SI & Staffing Seller, Marketing & ABM, Sales Leader & RevOps, SDR / BDR, Partnerships & Alliances | Services sellers | 4–6 min | Outsourcing deals |

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
- Workload: [Optional, if you know the Draup name, e.g. Application Development & Maintenance; skips mapping]

STEPS
1. If Workload is given, confirm it and go to step 3. Otherwise map [What I sell] to up to 8 Draup workloads, each Strong, Partial or Doubtful with a 5-word reason. Automatic mapping can be loose; judge each.
2. Stop for me to confirm or prune (if I said "don't wait", use Strong only).
3. Pull the top 20 companies outsourcing the confirmed workloads in [Country or Vertical] (primary vertical; HQ country). Remove IT services firms, consultancies, staffing firms and agencies.
4. Pull the top 10 providers in the same segment, with share.
5. For the top 10 buyers, pull their top 3 providers in those workloads. Rows 11–20: "not checked".

OUTPUT
- Bottom line: 2 sentences — segment size and where to start.
- "Workload mapping": Workload | Fit | Reason (before the list).
- "Target list": Rank | Company | HQ country | Engagements | Workloads covered | Main incumbent (share) | Fragmented? | Likely owner (title).
- Fragmented = no provider above 40% of that buyer's work (editable default).
- "Segment providers": Rank | Provider | Engagements | % of segment.
- "Where to play": 3–5 fragmented or broadest buyers, one line each.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never run the list without a country or vertical; unfiltered, it returns only global megacaps.
- Never map to catch-all workloads such as Account Management.
- Flag companies that look misclassified; leave them out of Where to play.

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
Map [What I sell] to Draup workloads and show me the mapping to approve. Then list the 20 companies in [Country or Vertical] that outsource them most, with main incumbent and whether the provider mix is fragmented.
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
- A country or vertical keeps the list from leaning toward global megacaps.

## Related prompts

- [Peer deals for social proof](../../prompts/10-outsourcing-and-services/peer-deals.md): Recent outsourcing engagements at the prospect's peers in the workload you sell, plus ready-to-use proof lines.
- [Build and size an ICP list](../../prompts/06-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.
- [Profile a services firm (rival or partner)](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner).

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_relevant_workloads`, `get_deals_customer_v3`, `get_deals_service_provider_v3`

Status: **tested live**. Prompt id: `services-offering-to-buyers`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
