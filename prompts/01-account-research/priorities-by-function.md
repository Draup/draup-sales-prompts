# Which priority to anchor your pitch on

**Where the account's priorities cluster, how each fits what you sell, and the single priority to lead with, with its likely owner and linked vendors.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need to know which initiative to anchor a pitch on. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Everyone | 2–4 min | Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | cloud data-platform modernisation services |
| `[Business function]` | IT (optional; Claude picks the best fit) |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my sales strategy analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]
- Business function: [optional, e.g. IT; leave blank and Claude picks]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull how many priorities mention each workload. Mark each Strong, Partial or No fit to [What I sell] and keep the top 5 by fit, then count.
3. If I gave no business function, choose the one holding most Strong-fit workloads and say why.
4. Pull up to 8 priorities for that function and sort them by date yourself, newest first.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Where priorities cluster": Rank | Workload | # priorities | Fit | Reason (5 words or fewer). Top 5.
- "Top priorities in [Business function]": Priority | One-line summary | Source (earnings call or news) + quarter | Workloads | Likely owner (title) | Up to 3 linked providers.
- "Best anchor for [What I sell]": the one priority to lead with and 2 bullets on why.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out linked technology or use cases that clearly don't fit the industry.
- In the provider column, leave out the company's own subsidiaries, recruiters, staffing firms, agencies and market-research firms.
- If the function has no priorities, say so and show the 3 nearest functions by priority count.
- If [Company] sells technology, drop priorities about its own products and its own products from linked tools.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Tools and providers are linked to priorities by workload, not confirmed: say "linked", never "used for". Quarter labels are fiscal and can run ahead of the calendar.
- Label anything you infer (buyer role, intent, fit, integration work) as "likely".
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Rank the top 5 workloads in [Company]'s priorities by fit to [What I sell], then list the top 8 priorities in the best-fit function with source, quarter, likely owner and linked providers. Name one anchor.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the anchor priority, which technology and incumbent vendors are linked?
```

```text
Who owns the anchor priority? Find executives tagged to its workloads.
```

```text
Is there hiring behind these priorities, or are they just talk?
```

## Tips for better results

- Leaving the function blank lets Claude choose where your offer fits best.
- Priorities from earnings calls often carry more weight than ones inferred from news.

## Related prompts

- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim quotes from leadership on your topic, with speaker, fiscal quarter and call date, or the annual-filing sections to read when there's no call.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_priorities_top_workloads_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `research-priorities-by-function`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
