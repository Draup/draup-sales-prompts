[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is our rate defensible against market pay?

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
| `[Hours per year (optional)]` | 1,880 |
| `[Exchange rate (optional)]` | the rate your finance team uses this quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pricing analyst for services bids. Use the Draup for Talent connector for pay facts, and the Draup for Sales connector for company facts. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Role: [e.g. Java Developer]
- Location: [metro or country, e.g. Pune Area, India]
- Years of experience: [band, e.g. 5–8]
- Rate to check: [ours or a competitor's, with unit and currency, e.g. USD 32 per hour]
- Competitor (optional): [e.g. Infosys, Cognizant, Capgemini]
- Target markup range (optional): [e.g. 1.8–2.4x]
- Hours per year (optional): [default 1,880 (editable default)]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

CONTEXT (optional)
"You're expensive" is easier to answer with market pay than with a discount. The markup over what the market pays its people shows how much room you have and what a competitor must be absorbing to undercut you.

STEPS
1. Find Draup's standard name for the role. If there's no exact match, show the 3 closest and ask which to use.
2. Match the place to Draup's name (metros look like "Bengaluru Area, India"). If it doesn't match, show the closest and ask.
3. Pull market annual base pay at [Years of experience]: median, P10, P90, salaries reported, confidence.
4. Pull median base pay by employer. Keep the top 15 among employers with 20+ salaries reported (editable default), plus any [Competitor].
5. Convert to hourly with [Hours per year]. If [Rate to check] is in another currency, use my [Exchange rate] or ask for one.
6. Divide [Rate to check] by the hourly median, P10 and P90 for the implied markup. With a target range, work out the rate needed at each end.

OUTPUT
- Bottom line: 2 sentences — where the rate sits against market pay and what that means for the bid.
- Recommended next step: who to take it to (the bid owner or the client's procurement lead, by title), what to say, and the one number to lead with. If you can't name a person, say so.
- "Rate check": Rate | Markup on median | on P10 | on P90 | Verdict against [Target markup range].
- "Rate needed at target markup": Low end | High end, per hour.
- Detail: market pay annual and hourly with salaries reported and confidence; by employer (rank, employer, median pay, salaries reported) with [Competitor] highlighted; 3 bullets — room on price, competitor pay, and a reply to "you're expensive".
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Base pay excludes benefits, bench, overhead and margin. Never present it as a competitor's bill rate.
- Flag thin salary counts and low-confidence figures.
- Without [Target markup range], show the multiples only; don't call a markup high or low.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Show pay in local currency with its code; convert to USD only with my [Exchange rate], and say which rate.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: where [Rate to check] sits against [Role] market pay in [Location] — median and P10–P90, the markup it implies, the rate needed at my target markup, and how named competitors pay.
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

- [Offshore saving case from market pay](../../prompts/17-talent-cost-and-location/offshoring-cost-case.md): A per-FTE and team-level base-pay gap for moving a role offshore, with the talent supply and hiring difficulty to show the team can be staffed.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `get_base_pay_by_role_locations`, `get_talent_base_pay_by_companies_roles`

Status: **documented, not live-tested**. Prompt id: `talent-pay-benchmark`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
