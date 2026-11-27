[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Global capability centres (GCCs) and the services play

> **The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell GCC set-up, build-operate-transfer, staff augmentation or managed services to companies with captive centres. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Sales Leader & RevOps | Services sellers | 4–6 min | Talent flow & locations, Outsourcing deals, News signals, Company directory |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | GCC build-operate-transfer and talent services in India |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my GCC and location-strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. GCC build-operate-transfer and talent services in India — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull GCC-tagged sites, all functions: metro, country, indicative size, functions hiring, 12-month postings, growth index. Count each site once; drop sites hiring mainly in manufacturing (likely plants).
3. Pull IT and R&D globalization summaries. Take likely new sites only from news naming a new centre or office; don't rely on Draup's "New Site" location tag, which can also mark established sites.
4. Pull centre setup and expansion news (12 months) where [Company] is the actor.
5. In one company-list lookup, pull the account's top competitors in its primary vertical with GCC counts. Drop suppliers, dealers, its own subsidiaries and firms under one-fifth of its revenue.

OUTPUT
- Bottom line: 2 sentences — GCC maturity and the play for [What I sell].
- "GCC sites": Metro | Country | Functions hiring | Postings (12 mo) | Growth index | Indicative size. By postings.
- "Likely new sites (from news)": Metro | Date | What opened.
- "Footprint" (IT and R&D headcount, sites) and "Peers" (Company | GCC locations).
- "Maturity", a Draup-based read (editable defaults): Nascent = 1–2 GCC metros, one main function; Scaling = 3–5 metros or several fast-growing functions; Mature = 6+ metros, several functions, average or slower growth.
- "Recommended play": BOT or GCC-as-a-service (nascent or new site), CoE expansion (scaling), managed services (mature), or not a GCC account, and why.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Site headcount is approximate and varies between pulls; never quote it as exact.
- If no GCC sites come back, say so; don't infer one.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Map [Company]'s GCCs in Draup: metro, functions hiring, 12-month postings, indicative site size, likely new sites, IT and R&D footprint and peers' GCC counts. Give a maturity read and a services play.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who runs the largest GCC? Find leaders based in that metro.
```

```text
Which IT and services providers deliver from [GCC country] for this account?
```

```text
Which outsourced workloads is the GCC likely to take back in-house?
```

```text
What roles are they hiring at the likely new site?
```

## Tips for better results

- A site with fresh postings but little workforce is often the best moment for build-operate-transfer or staffing support.
- Peers with many more GCCs make a strong "your competitors are already doing this" argument.

## Related prompts

- [Is work coming back in-house? (re-insourcing risk)](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with GCCs and likely new sites called out and net hiring over a stated window.
- [Where to put a delivery team](../../prompts/17-talent-cost-and-location/delivery-location.md): A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_location_insights_key_locations_map_v3`, `get_globalization_summary`, `get_signal_news_v3`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `services-gcc-opportunity`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
