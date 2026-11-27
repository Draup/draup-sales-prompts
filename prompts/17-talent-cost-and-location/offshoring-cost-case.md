[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Offshore saving case from market pay

> **A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You're pitching offshore or nearshore delivery and the buyer wants a cost case grounded in market pay, not your rate card. | Services, SI & Staffing Seller, Presales & Solutions, Account Executive | Services sellers | 4–6 min | Talent cost & supply |

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
| `[Client (optional)]` | pepsico.com |
| `[Exchange rate (optional)]` | the rate your finance team uses this quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal-shaping analyst for services pursuits. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company facts. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Role: [e.g. Data Engineer]
- Years of experience: [band, e.g. 3–6]
- Onshore location: [metro or country, e.g. Greater New York City Area, United States]
- Offshore locations: [up to 3, e.g. Bengaluru Area, India; Kraków, Poland; Mexico City, Mexico]
- Team size: [FTEs in scope, e.g. 25]
- What I sell: [one line, e.g. offshore data-engineering delivery — skip if you ran the start-here prompt]
- Client (optional): [website of the buyer, e.g. pepsico.com]
- Exchange rate (optional): [your rate to USD per currency, e.g. your finance team's quarterly rate]

CONTEXT (optional)
A saving built from market pay beats one from your rate card, if you say what it leaves out and show the location can staff the team.

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use.
2. Match each place to Draup's name (metros look like "Bengaluru Area, India"). If one doesn't match, show the closest and ask.
3. Per location, pull annual base pay at [Years of experience]: median, P10, P90, salaries reported, confidence (empty band: use all levels, say so).
4. With my rates, work out saving per FTE, saving % and team saving in USD against onshore; without rates, show local pay and ask.
5. For each offshore location, pull talent supply, 3-year growth and hiring difficulty for the role.
6. If I named a client, pull its top 3 executives in the function that owns this work and its top 90-day news item.

OUTPUT
- Bottom line: 2 sentences — annual base-pay saving for [Team size] FTEs at the best location (or "rates needed"), and whether supply can staff it; say it's base pay, not loaded cost.
- Recommended next step: who to take it to (name and title from step 6, or the title to find), what to do, and why now (one dated fact). If none is found, say so.
- "Pay": Location | Median USD (or local) | Salaries reported | Saving per FTE | Saving %. Onshore first, then by saving.
- "Can it scale?": Location | Talent supply | Hiring difficulty | Team as % of supply.
- Detail: P10–P90 (local), confidence, 3-year supply growth; 3 bullets on what this means for [What I sell].
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- The saving excludes transition, attrition and knowledge-transfer cost. Add overhead only with my multiplier.
- Don't build the bottom line on a location with low confidence or under 50 reported salaries (editable default); flag it.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Show pay in local currency with its code; convert to USD only with my [Exchange rate], and say which rate.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: the base-pay saving for [Team size] [Role]s ([Years of experience] years) moving from [Onshore location] to [Offshore locations], at my exchange rates, and whether offshore supply can staff it.
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

- [Best city for a delivery team](../../prompts/17-talent-cost-and-location/delivery-location.md): A ranked shortlist of metros in one country for a delivery team, scored on talent supply, cost, hiring difficulty and location risk with editable weights, plus the client's existing footprint.
- [Is our rate defensible against market pay?](../../prompts/17-talent-cost-and-location/pay-benchmark.md): Market pay for a role by employer, including named competitors, the markup a proposed or quoted rate implies, and the rate you'd need at your target markup.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_base_pay_by_role_locations`, `talent_size_compare_locations`, `talent_dashboard_talent_hdi_analyze_roles`, `get_account_id`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **documented, not live-tested**. Prompt id: `talent-offshoring-cost-case`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
