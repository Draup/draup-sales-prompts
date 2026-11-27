[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Their capability centres and the services play

> **The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell capability-centre set-up, build-operate-transfer, staff augmentation or managed services to companies with captive centres. | Services, SI & Staffing Seller, Account Executive, Partnerships & Alliances, Sales Leader & RevOps | Services sellers | 4–6 min | Talent flow & locations, Outsourcing deals, News signals, Company directory, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | GCC build-operate-transfer and talent services in India |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my capability-centre and location-strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. GCC build-operate-transfer and talent services in India — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull sites Draup tags as global capability centres (GCCs), all functions: metro, country, indicative size, functions hiring, 12-month postings, growth index. Count each site once; drop sites hiring mainly in manufacturing (likely plants).
3. Pull IT and R&D footprint summaries. Take likely new sites only from news naming a new centre or office; Draup's "New Site" tag can also mark established sites.
4. Pull centre setup and expansion news (12 months) where [Company] is the actor.
5. In one company-list lookup, pull the account's top competitors in its primary industry with centre counts. Drop suppliers, dealers, its own subsidiaries and firms under one-fifth of its revenue.
6. People and timing: pull the top 3 leaders in the function closest to [What I sell], preferring those based in the largest centre's country, and the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — centre maturity and the play for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Centres": Metro | Country | Functions hiring | Postings (12 mo) | Indicative size. By postings.
- "Maturity" (editable defaults): Nascent = 1–2 centre metros, one main function; Scaling = 3–5 metros or several fast-growing functions; Mature = 6+ metros, several functions, average or slower growth.
- "Recommended play": build-operate-transfer or centre-as-a-service (nascent or new site), centre-of-excellence expansion (scaling), managed services (mature), or not a centre account, and why.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Likely new sites (from news)" (Metro | Date | What opened), IT and R&D footprint, and "Peers" (Company | Centre locations).

RULES
- Site headcount is approximate and varies between pulls; never quote it as exact.
- If no centres come back, say so; don't infer one.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Label inferences (buyer role, intent, fit) "likely".
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 430 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Map [Company]'s capability centres in Draup: metro, functions hiring, 12-month postings, indicative size, likely new sites and peers' centre counts. Give a maturity read and the services play.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who runs the largest centre? Find leaders based in that metro.
```

```text
Which IT and services providers deliver from [centre country] for this account?
```

```text
Which outsourced workloads is the centre likely to take back in-house?
```

```text
What roles are they hiring at the likely new site?
```

## Tips for better results

- A site with fresh postings but little workforce is often the best moment for build-operate-transfer or staffing support.
- Peers with many more centres make a strong "your competitors are already doing this" argument.

## Related prompts

- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- [Where they're building teams](../../prompts/11-account-planning/expansion-footprint.md): The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.
- [Best city for a delivery team](../../prompts/17-talent-cost-and-location/delivery-location.md): A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_location_insights_key_locations_map_v3`, `get_globalization_summary`, `get_signal_news_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-gcc-opportunity`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
