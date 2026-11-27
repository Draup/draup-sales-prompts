# Pre-fill MEDDPICC from outside-in data

**A MEDDPICC sheet pre-filled with what Draup can show (metrics, buyer candidates, pain, competition) and clear 'must discover' flags for the rest.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| After the first meeting, or before a deal review, to see what you know and what you still have to find out. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Presales & Solutions | Everyone | 4–6 min | Company & financials, Priorities & opportunities, Executives & movement, Tech stack, Outsourcing deals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | cloud data-platform modernisation services |
| `[Business function]` | IT |
| `[Competitor]` | Accenture or Snowflake (optional; company or product) |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my deal-qualification analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. cloud data-platform services — skip if you ran the start-here prompt]
- Business function: [e.g. IT]
- Competitor: [optional, e.g. Snowflake or Accenture]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Metrics: latest revenue and growth, and targets or guidance in relevant priorities.
3. Economic buyer: [Business function] executives, up to 3 pages of 10; keep senior titles with high budget control.
4. Pain: the 5 most recent priorities in [Business function], with workloads.
5. Competition: if [Competitor] sells software, check the whole tech stack for any product it makes, in any area; if a services firm, pull its engagements here (Draup estimates, not contracts). Then the top incumbents on the pain workloads.
6. Champion: start with executives under a year in their title from the people already pulled. Only if there are none, check hires and promotions (last 6 months) for the main workload, keeping only people whose current employer is [Company]; say so.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "MEDDPICC": Letter | What Draup suggests | Evidence + date | Status (Evidence, Hypothesis, Must discover) | Question to confirm. Rows: Metrics, Economic buyer, Decision criteria, Decision process, Paper process, Identify pain, Champion, Competition.
- Decision criteria: hypotheses from stack and priorities. Decision and Paper process: "Must discover" (fiscal year end hints timing).
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Economic buyer and champion are candidates, never confirmed.
- Drop recruiters, staffing, agency and research firms from provider lists; flag subsidiaries.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- Rank providers by engagements yourself; Draup may return them alphabetically.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level (if none appears, say so in Gaps).
- Professional information only (name, title, employer, Draup's profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Pre-fill MEDDPICC for [What I sell] at [Company] in [Business function]: metrics, economic buyer candidates, pain, competition (whole-stack check for [Competitor]). Mark decision criteria, process, paper process and champion as hypotheses or must-discover.
```

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

- [Hypothesis-led discovery questions](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and who to take it to.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`, `get_outsourcing_summary_v3`, `get_account_executive_movement`

Status: **tested live**. Prompt id: `people-meddpicc-prefill`.

</details>

[Back to Buyers and stakeholders](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
