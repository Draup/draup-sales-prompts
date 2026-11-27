# Account SWOT, outside-in

**A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and who to take it to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preparing an executive briefing or a point of view for a strategic pursuit. A shorter SWOT is also an optional section in the account-plan prompt. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller, Marketing & ABM | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Hiring & job postings, Talent flow & locations, News signals, Tech stack |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | retail supply-chain AI and data services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my strategy analyst for a sales team. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. retail supply-chain AI and data services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue and EBITDA margin for the last 3 fiscal years, and revenue growth by business unit.
3. Pull the 10 most recent stated priorities.
4. Pull hiring workloads trending up and declining over the last 12 months.
5. Pull workforce growth and the top 5 companies they lose people to.
6. Pull technology added in the last 12 months (High and Medium usage only), and the top news from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Strengths (growth, margin, capabilities being built), Weaknesses (shrinking units or margins, attrition, priorities without hiring), Opportunities (priorities with hiring and technology behind them), Threats (layoffs, talent loss, cost pressure): 3–4 bullets each, the point then dated evidence in brackets.
- "Where [What I sell] fits": 3 bullets, each tied to a Weakness or Opportunity, with likely owner (title).
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Drop any bullet without Draup evidence.
- Phrase weaknesses as questions for the buyer, not judgements.
- Check for a divestment or restatement before calling a revenue drop a weakness.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Talent-flow data ends about 3 months ago; state the months covered.
- Drop news noise: outages (unless I sell security), stock chatter, charity, awards, passing mentions, look-alike or sister companies, and re-dated old stories (use the event date in the text). Give source, headline and link if Draup has one.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Build an evidence-based SWOT of [Company] from Draup: 3-year financials, priorities, hiring, talent flow, technology adopted and 90-day news. Every point cites a dated fact. End with where [What I sell] fits.
```

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
- Building a full account plan? The account-plan prompt has a shorter SWOT section; use this one when the SWOT itself is the deliverable.

## Related prompts

- [Draft an account plan](../../prompts/08-account-planning-and-expansion/account-plan.md): An account plan in eight parts: snapshot, their strategy in their own words, buying committee, incumbents, ranked expansion plays, risks and a 90-day plan, plus an optional short SWOT.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet pre-filled with what Draup can show (metrics, buyer candidates, pain, competition) and clear 'must discover' flags for the rest.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `accounts_financials_revenue_rnd_timelines_v3`, `get_revenue_by_business_v3`, `get_account_priorities_v3`, `accounts_hiring_demand_category_v3`, `accounts_talent_flow_top_metrics_v3`, `accounts_talent_flow_insights_companies_v3`, `get_tech_stack_trend_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-swot`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
