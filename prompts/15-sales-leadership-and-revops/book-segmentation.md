[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Sort my book into coverage tiers

> **Up to 20 accounts sorted into Strategic, Growth, Maintain and Deprioritise on an editable potential-versus-momentum rubric that scores your own workloads and rivals, with the coverage model for each tier and the flags behind every placement.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Setting coverage for a new fiscal year, rebalancing books between reps, or deciding which accounts get a named AE, a pooled team or a digital motion. Use the propensity-tiering prompt instead when the question is who might buy this quarter. | Sales Leader & RevOps, Account & Customer Success Manager, Account Executive | Everyone | 4–6 min | Company directory, Company & financials, Outsourcing deals, Hiring & job postings, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | boeing.com, airbus.com, rtx.com, northropgrumman.com, l3harris.com |
| `[What I sell]` | OT and device security software |
| `[My competitors (optional)]` | CrowdStrike, Palo Alto Networks |
| `[Current customers (optional)]` | l3harris.com |
| `[Reps available (optional)]` | 3 |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales operations lead designing account coverage. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [up to 20 websites, 10 per pass, e.g. boeing.com, airbus.com, rtx.com, l3harris.com]
- What I sell: [one line, e.g. OT and device security software — skip if you ran the start-here prompt]
- My competitors (optional): [rival products or firms, e.g. CrowdStrike, Palo Alto Networks — skip if you ran the start-here prompt]
- Current customers (optional): [websites, e.g. l3harris.com]
- Reps available (optional): [e.g. 3]

STEPS
1. Map What I sell to its 1–3 main workloads and say which. Look up the accounts by website (exact), 10 per lookup, showing only my competitors' products. Resolve misses one by one; ask if only suggestions return.
2. Take revenue and year, revenue growth, hiring %, workforce growth, workforce and rivals present.
3. Per account, pull 12-month postings in my workloads (keep only those) and work out postings per 1,000 employees.
4. POTENTIAL 0–50 (editable): workload postings per 1,000 — top third 20, middle 12, else 4; revenue — over $20B 15, $5–20B 10, $1–5B 6, else 2; rival present 10 (current customers: risk flag, 5); Opportunity Index 5.
5. MOMENTUM 0–50 (editable): revenue growth — over 8% 20, 3–8% 14, 0–3% 8, else 3; hiring % — over 10% 15, 6–10% 10, 3–6% 5, else 1; workforce growth — over 3% 15, 0–3% 10, else 3. Missing value = half points, flagged; revenue moving over 25% in a year = check for a merger or spin-off, score 8.
6. Segment (editable): Strategic = Potential 30+ and Momentum 25+; Maintain = Potential 30+ only; Growth = Momentum 25+ only; else Deprioritise. Customers stay at Maintain or above. Over half in one segment? Re-segment by rank (top 30%, next 40%, rest) and say so.
7. For the top Strategic account, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the shape of the book and what it means for [What I sell].
- Recommended next step: the coverage decision, its owner and a date; then the first account to open, with a named person (name and title from step 7) and one dated fact. If none is found, say so.
- "Segments": Account | Segment | Potential | Momentum | Strongest driver. Strategic first.
- "Coverage model": Strategic = named AE, sponsor, account plan; Growth = pooled AEs; Maintain = AM-led cadence; Deprioritise = digital or partner-led. Counts per tier; flag over 5 Strategic per rep.
- Detail: postings and rivals per account; flags; rubric.
- Gaps: what Draup didn't have — worth asking in discovery.
- Slide version (only if I ask): 5 bullets, each with one dated number, plus 1 table.

RULES
- Opportunity Index is Draup's own rating; never quote it as a company fact.
- Flagged accounts reach Strategic only as "Strategic (confirm)".

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- Rivals: High usage in my workloads is Red, Medium Amber, newly detected Amber; unchecked is "present (usage not checked)". Ignore "Generic" rows.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: sort [Accounts] into Strategic, Growth, Maintain or Deprioritise for [What I sell], scoring revenue, postings in my workloads, rivals installed and growth, with a coverage model per tier.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Check usage strength (High, Medium, Low) of my rivals at the 5 Strategic and Maintain accounts.
```

```text
Change the rubric: workload postings 30, revenue 10, and rerun.
```

```text
Split the Strategic and Growth accounts across [Reps available] reps, balanced on Potential.
```

```text
Give one dated why-now signal from the last 60 days for each Strategic account.
```

## Tips for better results

- Run it after propensity tiering: tiering says who might buy now, segmentation says who deserves a named owner all year.
- When a rival shows up at nearly every account, the workload-postings score is what separates them; ask for usage strength before calling an account contested.
- Private companies often lack revenue in Draup; score them by hand rather than letting them fall to Deprioritise.

## Related prompts

- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.
- [Carve balanced territories by geography](../../prompts/11-account-planning/territories.md): An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.
- [Which accounts each rep works this week](../../prompts/15-sales-leadership-and-revops/coverage-check.md): Your pasted accounts and owners checked against real triggers in the window, tied to what you sell, grouped by owner, with the 5 actions for this week, the named person behind the top action, and which reps' books have gone quiet.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_universe_companies_v3`, `get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `leaders-book-segmentation`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
