[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Pre-fill MEDDPICC from outside-in data

> **A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| After the first meeting, or before a deal review, to see what you know and what you still have to find out. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Presales & Solutions | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Executives & movement, Tech stack, Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | cloud data-platform modernisation services |
| `[Business function]` | IT |
| `[Competitor (optional)]` | Accenture or Snowflake (company or product) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal-qualification analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. cloud data-platform services — skip if you ran the start-here prompt]
- Business function: [e.g. IT]
- Competitor (optional): [e.g. Snowflake or Accenture]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Metrics: latest revenue and growth, and targets or guidance in relevant priorities.
3. Economic buyer: [Business function] executives, up to 3 pages of 10; keep senior titles with high budget control. If none is C-level, EVP or "Head of", widen once to C-level titles without the function filter.
4. Pain: the 5 most recent priorities in [Business function], with workloads.
5. Competition: if [Competitor] sells software, check the whole tech stack for any product it makes, in any area; if a services firm, pull its active engagements here. Then the top incumbents on the pain workloads.
6. Champion: start with executives under a year in their title from the people already pulled. Only if there are none, check hires and promotions (last 6 months) for the main workload, keeping only people whose current employer is [Company]; say so.
7. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from steps 3 or 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "MEDDPICC": Letter | What Draup suggests | Evidence + date | Status (Evidence, Hypothesis, Must discover) | Question to confirm. Rows: Metrics, Economic buyer, Decision criteria, Decision process, Paper process, Identify pain, Champion, Competition (with its Red, Amber or Green rating).
- Decision criteria: hypotheses from stack and priorities. Decision and Paper process: "Must discover" (fiscal year end hints timing).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: incumbent providers on the pain workloads with active engagements.

RULES
- Economic buyer and champion are candidates, never confirmed.
- Rank providers by engagements yourself; drop recruiters, staffing, agency and research firms; flag subsidiaries.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Leadership-move data can lag about 3 months; give the latest move date you saw.
- Competitor rating: a [Competitor] product with High usage in the workloads I sell is Red; Medium is Amber; newly detected in the last 12 months is a separate Amber signal.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Pre-fill MEDDPICC for [What I sell] at [Company] in [Business function]: bottom line and who to see next, then metrics, economic buyer candidates, pain, and [Competitor] rated Red/Amber/Green. Mark the rest must-discover.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write the 5 questions that would close the biggest unknowns.
```

```text
Profile the top economic-buyer candidate.
```

```text
Show [Competitor]'s footprint at this account in detail.
```

## Tips for better results

- Outside-in data can suggest Metrics, Pain and Competition well. Decision process, Paper process and Champion usually need a conversation.
- Re-run after each meeting and overwrite the Must-discover rows with what you learned.

## Related prompts

- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and the named person to take it to.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`, `get_outsourcing_summary_v3`, `get_account_executive_movement`, `get_top_signals`

Status: **tested live**. Prompt id: `people-meddpicc-prefill`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
