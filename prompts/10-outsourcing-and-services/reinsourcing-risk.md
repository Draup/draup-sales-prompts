[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is outsourced work coming back in-house?

> **For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a renewal, an expansion pitch or a new pursuit, to decode what the account really intends. | Services, SI & Staffing Seller, Account & Customer Success Manager, Account Executive | Services sellers | 4–6 min | Outsourcing deals, Hiring & job postings, Talent flow & locations, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | managed analytics and BI services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my services account strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. managed analytics and BI services — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull the top 10 outsourced workloads with engagements, narrowed to the business function closest to [What I sell] (say which); if fewer than 5 remain, add the next largest and mark them "outside my function".
3. Pull in-house postings by workload in one pass (up to 60, monthly; narrowing to one workload mixes in co-tagged roles). Compare the last 5 full months with the 5 before.
4. Also list workloads outside that top 10 with postings up over 50% and 50+ in 12 months.
5. Pull capability-centre sites (company-owned offshore sites, all functions) and 12-month centre setup or expansion news; ignore branches, HQ moves and plants.
6. Classify each workload in order: No signal (under 20 postings in 12 months); Re-insourcing risk (up over 20% with a capability centre hiring in that function); Capability gap (up over 20%, no centre); Cost takeout (up 20% or less).
7. People and timing: one page of 10 leaders in the function closest to [What I sell]; for IT keep IT, applications, infrastructure, data, CIO or CTO titles; if none fit, widen per the people rule, then to a leader named in news. Add the most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — biggest risk and biggest opening for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and the dated why-now (or say none).
- "Workload read": Workload | Engagements | In-house postings (12 mo) | Last 5 vs prior 5 | Read.
- "Biggest risk" and "Biggest opening": one workload each, with what to pitch.
- "Growing in-house in my workloads": up to 3 step-4 rows in the workloads closest to [What I sell], shown here, not under Detail.
- Gaps: what Draup lacked; ask in discovery.
- Detail: other step-4 rows (Workload | Postings | Change | Centre link | Likely meaning) and the centre sites.

RULES
- Thresholds are editable defaults. Catch-alls (Project/Programs Management, Account Management): "not assessed".
- Site headcount is indicative; count each site once.
- Each Read is a hypothesis, not a fact.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Postings are openings, not hires; skip partial first and last months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Label inferences "likely".
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. For [Company]'s top 10 outsourced workloads in my function, compare in-house postings over time, check capability centres, and label each: re-insourcing risk, capability gap, cost takeout or no signal.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who leads the capability centre behind the biggest risk?
```

```text
Show the 10 most recent in-house postings for the risk workload, with title, date and location.
```

```text
Draft a renewal-defence talking point for the risk workload.
```

## Tips for better results

- Hiring and outsourcing in the same workload isn't always bad news. Without a captive centre behind it, it often means demand is outgrowing both.
- The fastest in-house growth is often outside the outsourced top 10; that list is where new captive teams show up first.

## Related prompts

- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Outsourcing footprint and consolidation wedge](../../prompts/10-outsourcing-and-services/outsourcing-footprint.md): How much the account outsources, to whom, how concentrated it is, and the workloads where a consolidation pitch for what you sell fits, ending with a named buyer and a dated why-now.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_deals_workloads_v3`, `accounts_hiring_demand_category_v3`, `accounts_location_insights_key_locations_map_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-reinsourcing-risk`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
