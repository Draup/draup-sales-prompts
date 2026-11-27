[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Where to put a delivery team

> **A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. A client asks where you'd staff their team, or you're shaping a captive-centre, CoE or build-operate-transfer proposal. | Services, SI & Staffing Seller, Presales & Solutions, Sales Leader & RevOps | Services sellers | 4–6 min | Talent cost & supply |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Role]` | Cloud Engineer |
| `[Country]` | India |
| `[Team size]` | 60 |
| `[What I sell]` | cloud engineering managed services |
| `[Weights (optional)]` | supply 35%, cost 30%, hiring difficulty 20%, location risk 15% |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my location-strategy analyst for services pursuits. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company lookups and the client's existing sites. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [the client's website, e.g. pfizer.com]
- Role: [e.g. Cloud Engineer]
- Country: [in full, e.g. India]
- Team size: [e.g. 60]
- What I sell: [one line, e.g. cloud engineering managed services — skip if you ran the start-here prompt]
- Weights (optional): [default supply 35%, cost 30%, hiring difficulty 20%, location risk 15% (editable default)]

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use. Then confirm Draup's name for [Country].
2. Pull the 10 metros in [Country] with the most talent supply for the role, with 3-year growth, median annual base pay, open postings and hiring difficulty.
3. Score each 1–10 on supply, cost (cheaper scores higher) and difficulty (easier scores higher).
4. For the top 3, pull Draup's location profile (cost of living, political stability, rule of law, corporate tax), score risk 1–10, and combine all four scores with the weights.
5. Find [Company] by website, confirm the parent, and list its sites or captive centres in [Country].

OUTPUT
- Bottom line: 2 sentences — the lead metro and backup, and whether a [Team size]-person team is realistic there.
- Table: Rank | Metro | Talent supply | 3-yr growth | Median pay (local) | Open postings | Hiring difficulty | Score. Top 5, by score.
- "Top 3 compared": Metric | Metro 1 | Metro 2 | Metro 3 | Period.
- "Client footprint": [Company]'s sites in [Country] with indicative headcount, or "Not in Draup".
- "Weights used".
- Recommended next step: who to take it to (title), what to do, and why now (one dated figure).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Warn on capacity where [Team size] exceeds 2% of a metro's talent supply (editable default) or open postings are high against supply.
- Site headcount is approximate: call it indicative.
- Rank metros on local pay; no conversion is needed within one country.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Pay comes back in local currency: show it with its currency code. Convert to USD only if I give you a rate in [Exchange rate], and say which rate you used; otherwise show local currency.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Rank the top 5 metros in [Country] to build a [Team size]-person [Role] team for [Company], on Draup talent supply, median pay, hiring difficulty and location risk. Show the scoring and weights.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Re-run with cost weighted highest, then supply, then hiring difficulty.
```

```text
Compare the top metro with the best metro in [Second country].
```

```text
Which large employers in the top metro compete hardest for this role?
```

## Tips for better results

- Change the weights to match the buyer's real worry: cost-led and scale-led buyers often pick different cities.
- Take the capacity warning seriously: a cheap city with thin supply can turn into attrition and missed service levels.

## Related prompts

- [Offshore cost case (base-pay gap)](../../prompts/10-talent-cost-and-location/offshoring-cost-case.md): A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.
- [Global capability centres (GCCs) and the services play](../../prompts/06-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.
- [Where a vertical's teams sit](../../prompts/07-vertical-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, with hubs that host both: where its delivery and engineering work happens.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_talent_size_hotspots_by_roles`, `get_base_pay_by_role_locations`, `get_talent_demand_across_locations`, `talent_dashboard_talent_hdi_analyze_roles`, `get_location_ecosystem_analyze_locations_v3`, `get_account_id`, `accounts_location_insights_key_locations_map_v3`

Status: **documented, not live-tested**. Prompt id: `talent-delivery-location`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
