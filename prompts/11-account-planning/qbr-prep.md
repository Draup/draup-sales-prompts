[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# QBR prep: talking points and asks

> **Three talking points and three asks for your business review, built on what changed at the customer in your sponsor's function, set against the outcomes you delivered.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| The week before a quarterly or executive business review. Use plan-risk-check instead about 90 days before renewal, and signals-change-log for a monthly what-changed log. | Account & Customer Success Manager, Account Executive, Sales Leader & RevOps | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Executives & movement, Hiring & job postings, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Review period (optional)]` | 1 Aug 2026 – 31 Oct 2026 |
| `[Business function]` | Supply Chain |
| `[What I sell]` | warehouse automation software, live in 40 distribution centres |
| `[Outcomes we delivered]` | uptime 99.9%, picking time down 12% |
| `[Competitor (optional)]` | Blue Yonder |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my customer-success and QBR analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Review period (optional): [e.g. 1 Aug 2026 – 31 Oct 2026; blank = last full calendar quarter]
- Business function: [Our sponsor's function, e.g. Supply Chain]
- What I sell: [One line, e.g. warehouse automation software, live in 40 distribution centres — skip if you ran the start-here prompt]
- Outcomes we delivered: [Paste this period's results, e.g. uptime 99.9%, picking time down 12%]
- Competitor (optional): [e.g. Blue Yonder]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Priorities in [Business function] dated in [Review period] (10 at a time), with workloads; if none, the 3 most recent, marked as earlier.
3. Leadership: director-plus moves in [Review period], one step-2 workload per pull; keep only people whose current or previous employer is [Company]. If nothing falls in the period, say so and give the latest move date.
4. Hiring: monthly postings in [Business function] in [Review period] versus the same-length period before; top 3 [Business function] workloads trending up.
5. News in [Review period] where [Company] is the actor: deals, expansion, M&A, layoffs, restructuring.
6. Competitor check: any [Competitor] product in the stack in our workloads, with usage and last seen; flag anything newly detected in the period.
7. People: the top 3 leaders in [Business function] (full profile titles).
8. Financials: latest fiscal-year revenue and growth (USD at Draup's rate).

OUTPUT
- Bottom line: 2 sentences — the biggest change and what it means for renewal or expansion.
- Recommended next step: one person from step 7 or the sponsor (name and title), what to do before the meeting, and why now (a dated item from steps 2–5). If none turned up, say so.
- "3 talking points": each links a dated change to [Outcomes we delivered].
- "3 asks": expansion (tied to a priority), reference or case study, executive sponsor.
- "What changed" (up to 8 rows): Date | Type | What changed | Why it matters.
- Gaps: what Draup didn't have — worth asking in the meeting.
- Detail: leadership moves (Name | Move | Full title | Month), hiring numbers, competitor check, financials.

RULES
- Hiring, technology and news cover 12 months at most; if [Review period] is older, say what was covered.
- Check for a divestment before calling a revenue drop a cut.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Lead with 3 talking points, 3 asks and a next step naming a person. QBR for [Company], [Review period]: what changed in [Business function] (priorities, leaders, hiring, news, installed [Competitor] tools), set against [Outcomes we delivered].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the talking points and asks into 3 QBR slides: headline, evidence, ask.
```

```text
Run a renewal risk check before the meeting.
```

```text
Which new priority is the best expansion opportunity, and who owns it?
```

## Tips for better results

- Lead with the outcomes you delivered; Draup's outside-in view works best as the bridge to your asks.
- Leadership data can lag about 3 months, so a quiet leadership section may just mean the data hasn't caught up. The answer states the latest move date.

## Related prompts

- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- [Best entry points: expand or new](../../prompts/11-account-planning/entry-points.md): The five best ways in for what you sell, each marked Expand (we already serve it) or New, with dated evidence, incumbents, any installed competitor and the likely owner.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_forecast_v3`, `get_account_priorities_v3`, `get_account_executive_movement`, `accounts_hiring_timeline_v3`, `accounts_hiring_demand_category_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `plan-qbr-prep`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
