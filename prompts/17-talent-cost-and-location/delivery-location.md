[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Best city for a delivery team

> **A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. A client asks where you'd staff their team, or you're shaping a captive-centre, centre-of-excellence or build-operate-transfer proposal. | Services, SI & Staffing Seller, Presales & Solutions, Sales Leader & RevOps | Services sellers | 4–6 min | Talent cost & supply |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | medtronic.com |
| `[Role]` | Cloud Engineer |
| `[Country]` | India |
| `[Team size]` | 60 |
| `[What I sell]` | cloud engineering managed services |
| `[Weights (optional)]` | supply 35%, cost 30%, hiring difficulty 20%, location risk 15% |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my location-strategy analyst for services pursuits. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company facts and the client's existing sites. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [the client's website, e.g. medtronic.com]
- Role: [e.g. Cloud Engineer]
- Country: [in full, e.g. India]
- Team size: [e.g. 60]
- What I sell: [one line, e.g. cloud engineering managed services — skip if you ran the start-here prompt]
- Weights (optional): [default supply 35%, cost 30%, hiring difficulty 20%, location risk 15% (editable default)]

CONTEXT (optional)
Clients pick delivery cities on more than pay: a cheap city with thin supply turns into attrition and missed service levels, and a city next to the client's own centre is easier to sell. Show the trade-off, not just the winner.

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use. Then confirm Draup's name for [Country].
2. Pull the 10 metros in [Country] with the most talent supply for the role, with 3-year growth, median annual base pay, open postings and hiring difficulty.
3. Score each 1–10 on supply, cost (cheaper scores higher) and difficulty (easier scores higher).
4. For the top 3, pull Draup's location profile (cost of living, political stability, rule of law, corporate tax), score risk 1–10, and combine all four scores with the weights.
5. Find [Company] by website, confirm the parent, and list its sites or capability centres in [Country].
6. Pull [Company]'s top 3 executives in the function that owns this work and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the lead metro and backup, and whether a [Team size]-person team is realistic there.
- Recommended next step: who to take it to (name and title from step 6), what to do, and why now (one dated fact). If none is found, say so.
- Table: Metro | Talent supply | Median pay (local) | Hiring difficulty | Score. Top 5, by score.
- "Client footprint": [Company]'s sites in [Country] with indicative headcount, or "Not in Draup".
- Detail: top 3 compared on every metric with periods; 3-year growth and open postings; weights used.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Warn on capacity where [Team size] exceeds 2% of a metro's talent supply (editable default) or open postings are high against supply.
- Site headcount is approximate: call it indicative.
- Rank metros on local pay; no conversion is needed within one country.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: the best metro in [Country] for a [Team size]-person [Role] team for [Company], scored on supply, pay, hiring difficulty and location risk, with the client's sites and who to take it to.
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

- [Offshore saving case from market pay](../../prompts/17-talent-cost-and-location/offshoring-cost-case.md): A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_talent_size_hotspots_by_roles`, `get_base_pay_by_role_locations`, `get_talent_demand_across_locations`, `talent_dashboard_talent_hdi_analyze_roles`, `get_location_ecosystem_analyze_locations_v3`, `get_account_id`, `accounts_location_insights_key_locations_map_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **documented, not live-tested**. Prompt id: `talent-delivery-location`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
