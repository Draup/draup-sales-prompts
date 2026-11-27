[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Expansion business case from growth units

> **A short, evidence-led case for expanding into a customer's fastest-growing unit or region: where growth is, the priorities funding it, a Draup-estimated spend pool, a 150-word executive summary and the named owner to send it to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before proposing an expansion to an existing customer's sponsor or your own deal desk. Use this to grow an existing customer; use "Business-case inputs from their numbers" (deals-business-case-inputs) instead for a new deal's value model. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | boeing.com |
| `[Current footprint]` | Commercial Airplanes, North America; $400K a year (or my saved account notes) |
| `[Expansion idea]` | extend predictive maintenance analytics to Global Services |
| `[What I sell]` | industrial IoT analytics software and services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my value consultant writing an expansion business case. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. boeing.com]
- Current footprint: [where we are and roughly what it's worth, e.g. Commercial Airplanes, North America; $400K a year]
- Expansion idea: [one line, e.g. extend predictive maintenance analytics to Global Services]
- What I sell: [one line, e.g. industrial IoT analytics software and services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Expansion cases ride the customer's own growth story: where growth is, what leadership committed to, why our proof de-risks it.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Pull latest revenue, EBITDA, R&D and IT spend with growth, and forecasts.
3. Pull revenue by business unit and by region; name the fastest-growing unit and region (or say Draup has no unit split).
4. Pull key priorities grouped by function; keep those supporting [Expansion idea] or the growth unit, with quarter and stated targets.
5. Pull the Draup-estimated IT spend split (software, internal staffing, IT outsourcing, hardware) for the latest two years.
6. Pull workloads (types of work) trending up in hiring (12 months) linked to [Expansion idea].
7. Owner and trigger: the top 3 executives in the function closest to [Expansion idea] (one page of 10) and the most important news item from the last 90 days.
8. Size a range: the relevant IT-spend category scaled by the growth unit's revenue share, against [Current footprint].

OUTPUT
- Bottom line: 2 sentences — the size of the opportunity and what it means for [What I sell].
- Recommended next step: a named person (name, full title) who owns the expansion area, the action this week and the dated why-now; if none, say so.
- Table "Growth story" (up to 8): Unit, region or metric | Share or value | Growth | Year.
- Table "Spend pool": Category | Latest | Prior year | Note; then the sized range with the maths shown.
- "What leadership committed to" (priority, quarter, fit), "Why us" (3 bullets) and "Risks" (up to 3, dated).
- "Executive summary": 150 words max, for our sponsor to forward.
- Detail: hiring behind it and full financials.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- The sized range is not their budget; show the formula.
- If hiring looks thin for the company's size, say so and lean on priorities.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- IT spend is Draup-estimated, often modelled from revenue; don't treat its growth as a signal. Use USD millions at Draup's rate. A forecast over 15% off the latest actual is a model estimate.
- Use the latest year's regional split; compute growth from amounts and check for divestments before calling a drop a cut.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 500 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Build an expansion case for [Expansion idea] at [Company]. Lead with the size of the opportunity and the named owner to send it to. Show growth units, supporting priorities, a Draup-estimated spend pool and a 150-word summary.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the executive summary into a 5-slide outline.
```

```text
Which leaders own the priorities in the case?
```

```text
Stress-test the case: what would make the sponsor say no?
```

## Tips for better results

- Quote management's own words from the priorities; sponsors reuse them in budget requests.
- Fill in what the current footprint is worth; the comparison makes the ask feel proportionate.

## Related prompts

- [Business units worth targeting first](../../prompts/01-account-research/business-units.md): The two business units to target first, ranked by growth, with the priority behind each and a named leader to approach.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- [Brief for a C-level pursuit meeting](../../prompts/11-account-planning/cxo-pursuit-brief.md): A one-page pursuit brief for a C-level meeting: the 3 workloads to lead with, the buyers, incumbents, a Go or Not-yet evidence check, what to learn in meeting 1 and a 90-day plan.
- [Business-case inputs from their numbers](../../prompts/08-deal-strategy/business-case-inputs.md): The size of the prize as a range, built on the account's own revenue, margin, spend, outsourcing and hiring, with every number labelled, a worked example you can edit and the named owner to validate it with.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_forecast_v3`, `get_revenue_by_business_v3`, `accounts_financials_revenue_by_region_post_v3`, `get_key_account_priorities`, `accounts_financials_revenue_by_it_spend_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `expand-business-case`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
