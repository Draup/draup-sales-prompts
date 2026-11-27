# Top hiring companies in a vertical

**The real end employers posting the most jobs in an industry, with outliers and recruiters removed, hiring intensity shown and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want the most active companies in a vertical this year: active hiring often means active budgets. | SDR / BDR, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 2–4 min | Industry ecosystem, Hiring & job postings |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Life Sciences |
| `[What I sell]` | talent-acquisition software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my market research analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Life Sciences]
- What I sell: [one line, e.g. talent-acquisition software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull Draup's top hiring companies for the vertical (a fixed top 50) and note the time window Draup states.
3. Remove staffing and recruiting firms and job boards, and record each removal.
4. Take the top 25 left. Look them up in one company list and keep only the exact companies: workforce, primary vertical and postings in the last 90 days.
5. Remove outliers: a company whose posting count is above its workforce, or an unfamiliar firm posting far more than household names. Keep the top 20.
6. Work out postings per 1,000 employees.

OUTPUT
- Bottom line: 2 sentences — who is hiring hardest and what it means for [What I sell].
- Header: vertical and time window ("window not stated" if Draup gives none).
- Table (top 20, most postings first): Rank | Company | Postings | Postings (90 days) | Workforce | Postings per 1,000 staff | Primary vertical | Who to call (title) | Flag.
- "Removed": name and reason.
- "Hot spots for [What I sell]": 5 companies with the highest intensity or strongest recent hiring, one reason each.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Flag "check vertical" when a company's primary vertical isn't [Vertical].
- If a company has no workforce figure, write "n/a" for intensity rather than dropping it.
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- A posting count in the millions or above the company's workforce means a failed match; say so and drop it.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Show the top 20 [Vertical] companies by job postings after removing staffing firms, recruiters and outliers. Add workforce, postings per 1,000 staff and who to call, and name 5 hot spots for [What I sell].
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5, which functions and skills are they hiring for most?
```

```text
Which of these are hiring most in [Country]?
```

```text
Draft a hiring-themed opener for the #1 hot spot.
```

## Tips for better results

- Postings per 1,000 staff shows who is hiring hard for their size, not just who is biggest.
- Check the 'Removed' list if a name you expected is missing.

## Related prompts

- [Who's hiring for a tech or role](../../prompts/05-prospecting-and-lists/hiring-led-list.md): The end employers posting the most jobs for a technology or buyer role, cleaned of job boards and staffing firms, with who to call and the industries driving demand.
- [One-page vertical market snapshot](../../prompts/07-vertical-intelligence/vertical-snapshot.md): A one-page view of an industry: revenue and spend, top priorities with likely owners, technologies gaining ground, and who outsources what to whom.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings are running above or below normal, which workloads drive it, and whether it's seasonal.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_organization_top_top_hiring_accounts`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `market-hiring-leaders`.

</details>

[Back to Industry and market intelligence](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
