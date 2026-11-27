[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# One-page account brief

> **Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account just landed on your list, or before a first meeting. Use the 10-minute pre-call snapshot instead when you only have a few minutes. | Account Executive, Presales & Solutions, Account & Customer Success Manager, SDR / BDR | Everyone | 2–4 min | Company & financials, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | starbucks.com |
| `[What I sell]` | store technology and data platform services |
| `[Competitor (optional)]` | Snowflake or Accenture (company or product) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- What I sell: [one line, e.g. store technology and data platform services — skip if you ran the start-here prompt]
- Competitor (optional): [company or product, e.g. Snowflake]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile and latest fiscal-year revenue, EBITDA and IT spend with growth (if private, funding instead), and revenue by business unit and region, kept only if more than one unit or region holds 10% or more.
3. Pull stated priorities for the function closest to [What I sell]; keep the 8 most relevant, newest first. If it has none, say so and use the company-wide list.
4. Pull acquisitions from the last 3 years.
5. Pull the top 3 executives for the function closest to [What I sell] and the 2 most important news items from the last 90 days where [Company] is the actor.
6. If I named a competitor, check the whole tech stack for its products, in any area; if it is a services firm, check its active engagements (Draup-derived) at the account instead.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "What they're focused on": Priority | Source + quarter | Likely owner (name from step 5, else title) | Why it matters. Up to 8.
- "Who to talk to": Name | Full title | Time in role | Linked priority. Up to 3.
- "Competitor in the stack" (if named): one line rated Red, Amber or Green with product, usage strength and last seen.
- "Why this matters for [What I sell]": 3 bullets: fact → implication → action.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "The numbers" (Metric | Latest FY | YoY); business units and regions if kept; "Recent deals" (Date | Company acquired | Size | Why), flagging divestments and duplicates.

RULES
- If [Company] sells technology, drop priorities about its own products and its own products from linked tools.
- The acquisitions table can be incomplete; if news names a deal it lacks, say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Money is annual, in millions of reporting currency. IT and R&D spend are Draup estimates that often move with revenue; don't treat their growth as a separate signal. Check for a divestment or restatement before calling a drop over 5% a cut.
- Competitor rating: a [Competitor] product with High usage in the workloads I sell is Red; Medium is Amber; newly detected in the last 12 months is a separate Amber signal.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
One-page Draup brief on [Company]: bottom line, who to call (name, title) and why now; 8 priorities in the function closest to [What I sell]; latest revenue with growth; [Competitor] in the stack. Date every number.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Now map the buying committee for [Business function].
```

```text
Which of these priorities have the most hiring behind them?
```

```text
Is their budget growing or shrinking? Show the 3-year trend.
```

```text
Turn the 'Why this matters' section into a 90-word email to the person in the next step.
```

## Tips for better results

- Add your main competitor: finding it, or its absence, in the stack is often the most useful line in the brief.
- Use the company website rather than the name; it is the most reliable way to land on the right company.
- Business-unit and region tables only appear when the company is genuinely split; a single-market retailer skips them.

## Related prompts

- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_revenue_by_business_v3`, `accounts_financials_revenue_by_region_post_v3`, `get_account_priorities_v3`, `accounts_partnerships_mergers_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`, `accounts_private_financials_v3`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`

Status: **tested live**. Prompt id: `research-account-brief`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
