# New leaders in the last 6 months

**Leaders who joined or were promoted in the last 6 months in your area, where they came from, and which ones arrive from your customers.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Monthly, or when an account goes quiet: new leaders often review vendors in their first 90 days. | SDR / BDR, Account Executive, Account & Customer Success Manager | Everyone | 2–4 min | Executives & movement |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Workload]` | Artificial Intelligence & Data Science, Cybersecurity |
| `[Our customers]` | Contoso Retail, Fabrikam Foods |
| `[What I sell]` | AI security and governance software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my sales stakeholder analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Workload: [1–3 workloads, e.g. Artificial Intelligence & Data Science, Cybersecurity]
- Our customers: [optional, e.g. Contoso Retail, Fabrikam Foods]
- What I sell: [one line, e.g. AI security and governance software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull executive hires and promotions, one workload at a time.
3. Keep moves from the last 6 months where the person's current company is [Company].
4. Compare each new hire's previous company with [Our customers], allowing name variants ("Contoso" = "Contoso Retail Inc.").

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- One line per workload: rows checked, rows kept, latest move date in the data.
- "New leaders": Date | Hire or Promotion | Name | New title | Previous company | Workload | Warm path? Newest first.
- "Warm paths": each person who came from one of [Our customers], and who on our side likely knows them.
- "First-90-days plays": the top 3 people to approach, each with a one-line angle tied to [What I sell].
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out exits; the customer-alumni prompt covers them.
- Drop rows that clearly aren't about [Company], such as look-alike company names.
- If a workload has no recent moves, say "none in the last 6 months"; don't widen silently.
- A warm path means they worked at our customer, not that they bought from us.

STANDARD RULES (leave as is)
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Draup shows about the 10 latest moves per type and can't filter them by function: narrow by workload, say how many rows you checked and the latest move date, and keep only rows where [Company] is the current employer.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Who joined or was promoted at [Company] in the last 6 months in [Workload]? Date, name, full title, previous company. Flag anyone who came from [Our customers]. Drop exits and unrelated rows.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Profile the top new leader and draft a congratulations note with a relevant angle.
```

```text
Also check current senior leaders whose past companies include [Our customers].
```

```text
Show exits in the same workloads: where did they go?
```

## Tips for better results

- Run it per workload. Without one you only see the most recent moves company-wide.
- A leader who came from one of your customers is often the warmest intro you can get.

## Related prompts

- [Warm paths among current leaders](../../prompts/02-buyers-and-stakeholders/warm-paths-current-leaders.md): Senior leaders at the account who used to work at your customers, partners or your own company, so you can ask for a warm intro.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive and two openers tied to the account's current priorities.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Customer alumni on the move](../../prompts/08-account-planning-and-expansion/follow-champions.md): Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_executive_movement`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `people-new-leaders-warm-paths`.

</details>

[Back to Buyers and stakeholders](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
