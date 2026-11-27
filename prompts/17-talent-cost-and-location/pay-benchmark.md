[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Pay benchmark and rate-card check

> **Market pay for a role by employer, including named competitors, the markup a proposed or quoted rate implies, and the rate you'd need at your target markup.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You're pricing a staffing or managed-services bid, or a client pushes back that your rates are too high. | Services, SI & Staffing Seller, Presales & Solutions, Account Executive, Sales Leader & RevOps | Services sellers | 2–4 min | Talent cost & supply |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Role]` | Java Developer |
| `[Location]` | Pune Area, India |
| `[Years of experience]` | 5–8 |
| `[Rate to check]` | USD 32 per hour |
| `[Competitor (optional)]` | Infosys, Cognizant, Capgemini |
| `[Target markup range (optional)]` | 1.8–2.4x |
| `[Hours per year]` | 1,880 |
| `[Exchange rate (optional)]` | the rate your finance team uses this quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pricing analyst for services bids. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company lookups. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Role: [e.g. Java Developer]
- Location: [metro or country, e.g. Pune Area, India]
- Years of experience: [band, e.g. 5–8]
- Rate to check: [ours or a competitor's, with unit and currency, e.g. USD 32 per hour]
- Competitor (optional): [e.g. Infosys, Cognizant, Capgemini]
- Target markup range (optional): [e.g. 1.8–2.4x]
- Hours per year: [default 1,880 (editable default)]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use.
2. Match each place to Draup's name (metros look like "Bengaluru Area, India"). If one doesn't match, show the closest and ask.
3. Pull market annual base pay at [Years of experience]: median, P10, P90, salaries reported, confidence.
4. Pull median base pay by employer. Keep the top 15 among employers with 20+ salaries reported (editable default), plus any [Competitor].
5. Convert to hourly with [Hours per year]. If [Rate to check] is in another currency, use my [Exchange rate] or ask for one.
6. Divide [Rate to check] by the hourly median, P10 and P90 for the implied markup. With a target range, work out the rate needed at each end.

OUTPUT
- Bottom line: 2 sentences — where the rate sits against market pay and what that means for the bid.
- "Market": Median | P10 | P90, annual and hourly; salaries reported; confidence.
- "By employer": Rank | Employer | Median pay | Salaries reported. Highlight [Competitor].
- "Rate check": Rate | Markup on median | on P10 | on P90 | Verdict against [Target markup range].
- "Rate needed at target markup": Low end | High end, per hour.
- "What this means": 3 bullets — room on price, competitor pay, and a reply to "you're expensive".
- Recommended next step: who to take it to (title), what to do, and why now (one dated figure).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Base pay excludes benefits, bench, overhead and margin. Never present it as a competitor's bill rate.
- Flag thin salary counts and low-confidence figures.
- Without [Target markup range], show the multiples only; don't call a markup high or low.

STANDARD RULES (leave as is)
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Pay comes back in local currency: show it with its currency code. Convert to USD only if I give you a rate in [Exchange rate], and say which rate you used; otherwise show local currency.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Benchmark [Role] pay in [Location] from Draup: market median and P10–P90, the top 15 employers by median pay with [Competitor] highlighted, the markup [Rate to check] implies, and the rate needed at my target markup.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Redo the rate check for a junior band to see a blended rate.
```

```text
Compare the same role in [Second location] and show the rate I'd need there for the same markup.
```

```text
Write a 3-sentence reply to a client who says our rate is [X]% above competitors.
```

## Tips for better results

- Give your own markup range; without it Claude shows only the multiples, which is safer than guessing what's normal.
- Change hours per year to suit the country: working hours differ a lot between markets.
- Employer pay is what firms pay their people, not what they charge. Use it to explain cost, not to quote a competitor's price.

## Related prompts

- [Offshore cost case (base-pay gap)](../../prompts/17-talent-cost-and-location/offshoring-cost-case.md): A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.
- [Profile a services firm (rival or partner)](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner).
- [Battlecard: rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers, what it wins, recent moves, how to beat it, trap questions and the objection to expect.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_base_pay_by_role_locations`, `get_talent_base_pay_by_companies_roles`

Status: **documented, not live-tested**. Prompt id: `talent-pay-benchmark`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
