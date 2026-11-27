# One-page account brief

**A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account just landed on your list, or before a first meeting. | Account Executive, Presales & Solutions, Account & Customer Success Manager, SDR / BDR | Everyone | 2–4 min | Company & financials, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | cloud data-platform modernisation services |
| `[Competitor]` | Snowflake (optional; company or product) |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my sales research analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]
- Competitor: [optional company or product, e.g. Snowflake]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile; latest fiscal-year revenue, EBITDA, IT and R&D spend with year-on-year growth and next-year forecast; and revenue by business unit and region. If private, show funding instead.
3. Pull stated priorities and keep the 8 most relevant to [What I sell], newest first.
4. Pull acquisitions from the last 3 years.
5. If I named a competitor, check the whole tech stack for its products, in any area; if it is a services firm, check its outsourcing engagements at the account instead (Draup estimates, not contracts).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "The numbers": Metric | Latest FY | YoY | Next-year forecast; then business units and regions with % share.
- "What they're focused on": Priority | Function | Source + quarter | Likely owner (title). Up to 8.
- "Recent deals": Date | Company acquired | Size or "undisclosed" | Why they bought it. Flag divestments and duplicates.
- "Competitor in the stack" (if named): Product | Maker | Usage strength | Last seen.
- "Why this matters for [What I sell]": 3 bullets: fact → implication → action.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If [Company] sells technology, drop priorities about its own products and its own products from linked tools.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a forecast is more than 15% from the latest actual, or contradicts the latest year-on-year change, show both and call it a model estimate.
- The acquisitions table can be incomplete: if it is thin but priorities or news name an acquired company, check 12 months of M&A news and say so. Divestments come from news only.
- Use the latest year's regional split only. Check for a divestment or restatement before calling a drop over 5% a cut.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
One-page Draup brief on [Company]: size, latest revenue and IT spend with growth, the 8 priorities closest to [What I sell], acquisitions in 3 years, and who to call first. Date every number.
```

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

- Use the company website rather than the name; it is the most reliable way to land on the right company.
- Add your main competitor: finding it, or its absence, in the stack is often the most useful line in the brief.
- Fiscal years and quarters follow the company's own calendar and can run ahead of the calendar year.

## Related prompts

- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Five short bullets you can read in the lobby: who they are, what just happened, where hiring is rising, the priority closest to your offer, and one question to ask.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): Where the account's priorities cluster, how each fits what you sell, and the single priority to lead with, with its likely owner and linked vendors.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `accounts_financials_forecast_v3`, `get_revenue_by_business_v3`, `accounts_financials_revenue_by_region_post_v3`, `get_account_priorities_v3`, `accounts_partnerships_mergers_v3`, `get_signal_news_v3`, `accounts_private_financials_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `research-account-brief`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
