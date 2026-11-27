[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Offshore cost case (base-pay gap)

> **A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You're pitching offshore or nearshore delivery and the buyer wants a cost case grounded in market pay. | Services, SI & Staffing Seller, Presales & Solutions, Account Executive | Services sellers | 4–6 min | Talent cost & supply |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Role]` | Data Engineer |
| `[Years of experience]` | 3–6 |
| `[Onshore location]` | Greater New York City Area, United States |
| `[Offshore locations]` | Bengaluru Area, India; Kraków, Poland; Mexico City, Mexico |
| `[Team size]` | 25 |
| `[What I sell]` | offshore data-engineering delivery |
| `[Exchange rate (optional)]` | the rate your finance team uses this quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal-shaping analyst for services pursuits. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company lookups. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Role: [e.g. Data Engineer]
- Years of experience: [band, e.g. 3–6]
- Onshore location: [metro or country, e.g. Greater New York City Area, United States]
- Offshore locations: [up to 3, e.g. Bengaluru Area, India; Kraków, Poland; Mexico City, Mexico]
- Team size: [FTEs in scope, e.g. 25]
- What I sell: [one line, e.g. offshore data-engineering delivery — skip if you ran the start-here prompt]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use.
2. Match each place to Draup's name (metros look like "Bengaluru Area, India"). If one doesn't match, show the closest and ask.
3. For each location, pull annual base pay at [Years of experience]: median, P10, P90, salaries reported, confidence. If the band is empty, use all levels and say so.
4. With my rates, convert to USD and work out saving per FTE, saving % and team saving against onshore. Without rates, show local pay and ask me for rates.
5. For each offshore location, pull talent supply, 3-year growth and hiring difficulty for the role.

OUTPUT
- Bottom line: 2 sentences — annual base-pay saving for [Team size] FTEs at the best location (or "rates needed"), and whether supply can staff it.
- "Pay": Location | Median (local) | P10–P90 (local) | Median USD | Salaries reported | Confidence | Saving per FTE | Saving %. Onshore first, then by saving.
- "Can it scale?": Location | Talent supply | 3-yr growth | Hiring difficulty | Team as % of supply.
- "Why this matters for [What I sell]": 3 bullets, fact → implication → action.
- Recommended next step: who to take it to (title), what to do, and why now (one dated figure).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Say under the bottom line: base pay only, not loaded cost or a bill rate; excludes transition, attrition and knowledge-transfer cost. Add overhead only with my multiplier.
- Don't build the bottom line on a location with low confidence or under 50 reported salaries (editable default); flag it.

STANDARD RULES (leave as is)
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
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
Compare Draup median base pay for a [Role] ([Years of experience] years) in [Onshore location] vs [Offshore locations], with saving per FTE and for [Team size] FTEs at my rates, plus offshore supply and hiring difficulty.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Apply my loaded-cost multipliers ([onshore]x and [offshore]x) and redo the saving.
```

```text
Add two nearshore options in Latin America and re-rank.
```

```text
Turn this into a one-slide cost case with three bullets for the CFO, noting what the base-pay gap leaves out.
```

## Tips for better results

- Use Draup's metro names (e.g. "Bengaluru Area, India"). If a city doesn't match, Claude shows the closest options.
- Treat the result as a base-pay gap. Your commercial model adds overhead, margin and transition cost on top.

## Related prompts

- [Where to put a delivery team](../../prompts/17-talent-cost-and-location/delivery-location.md): A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.
- [Pay benchmark and rate-card check](../../prompts/17-talent-cost-and-location/pay-benchmark.md): Market pay for a role by employer, including named competitors, the markup a proposed or quoted rate implies, and the rate you'd need at your target markup.
- [Global capability centres (GCCs) and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_base_pay_by_role_locations`, `talent_size_compare_locations`, `talent_dashboard_talent_hdi_analyze_roles`

Status: **documented, not live-tested**. Prompt id: `talent-offshoring-cost-case`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
