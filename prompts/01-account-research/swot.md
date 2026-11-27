[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Account SWOT, outside-in

> **A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and the named person to take it to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preparing an executive briefing or a point of view for a strategic pursuit. A shorter SWOT is also an optional section in "Draft an account plan". | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller, Marketing & ABM | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Hiring & job postings, Talent flow & locations, News signals, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | retail supply-chain AI and data services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my strategy analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. retail supply-chain AI and data services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue and EBITDA margin for the last 3 fiscal years, and revenue growth by business unit.
3. Pull the 10 most recent stated priorities, preferring the function closest to [What I sell].
4. Pull hiring workloads trending up and declining over the last 12 months in the function closest to [What I sell]; add the company-wide top 3 for context.
5. Pull workforce growth and the top 5 companies they lose people to.
6. Pull technology added in the last 12 months (High and Medium usage only), the top 3 executives in the function closest to [What I sell] and the top news from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Strengths (growth, margin, capabilities being built), Weaknesses (shrinking units or margins, attrition, priorities without hiring), Opportunities (priorities with hiring and technology behind them), Threats (layoffs, talent loss, cost pressure): 3–4 bullets each, the point then dated evidence in brackets.
- "Where [What I sell] fits": 3 bullets, each tied to a Weakness or Opportunity, with the likely owner by name where step 6 found one.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Drop any bullet without Draup evidence.
- Phrase weaknesses as questions for the buyer, not judgements.
- Talent-flow data ends about 3 months ago; state the months covered.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Evidence-based SWOT of [Company] from Draup: bottom line and who to take it to, then 3–4 dated bullets each for strengths, weaknesses, opportunities and threats, and where [What I sell] fits.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the Opportunities into a 3-slide point of view for the CIO.
```

```text
Which executives own the Weaknesses you listed?
```

```text
Run the same SWOT for [Company 2] and compare.
```

## Tips for better results

- Every bullet cites Draup evidence, so you can defend it in front of the customer.
- Building a full account plan? "Draft an account plan" has a shorter SWOT section; use this one when the SWOT itself is the deliverable.

## Related prompts

- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_revenue_rnd_timelines_v3`, `get_revenue_by_business_v3`, `get_account_priorities_v3`, `accounts_hiring_demand_category_v3`, `accounts_talent_flow_top_metrics_v3`, `accounts_talent_flow_insights_companies_v3`, `get_tech_stack_trend_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-swot`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
