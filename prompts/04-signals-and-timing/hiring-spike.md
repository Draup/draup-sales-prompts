# Are they hiring more than usual?

**A plain-English verdict on whether job postings are running above or below normal, which workloads drive it, and whether it's seasonal.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Timing outreach, or checking a hunch that an account is gearing up (or slowing down). | SDR / BDR, Account Executive, Services, SI & Staffing Seller | Everyone | 2–4 min | Hiring & job postings |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Workload]` | Artificial Intelligence & Data Science (optional) |
| `[What I sell]` | data and AI staff augmentation |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my hiring-signals analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Workload: [optional Draup workload, e.g. Artificial Intelligence & Data Science]
- What I sell: [one line, e.g. data and AI staff augmentation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull monthly job postings for the last 12 months, full months only; say which months you used.
3. Work out the monthly average and standard deviation, and the last 5 full months against the 5 before.
4. Verdict on the last 3 full months (editable defaults): Spiking = any month over 2 standard deviations above average; Above normal = their average over 1 above; Slowing = their average over 1 below; Normal = anything else.
5. Label a flagged month seasonal if it's an industry peak (e.g. retail holidays), or company-wide if many unrelated workloads rose together.
6. For each flagged month, list the top 5 workloads against their usual month.
7. If I gave a workload, repeat steps 2–4 for it.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Verdict: one plain-English line (e.g. "Above normal, mostly seasonal store roles") with the 5-vs-5 change in %.
- Table: Month | Postings | Standard deviations from average | Flag.
- "What drove it": Workload | Postings in flagged month | Usual month | Likely owner.
- "[Workload] view": short table and one line against the company trend.
- "Why this matters for [What I sell]": 2–3 bullets.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Standard deviations go in the table; the verdict uses plain words.
- State the exact window, e.g. "Dec 2025 – Oct 2026".
- A seasonal frontline spike is rarely a buying signal; say so when it's the driver.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Keep to about 320 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Is [Company] hiring more than usual? Compare the last 5 full months of postings with the 5 before and with the monthly average, flag unusual months, say what drove them and whether it's seasonal, and repeat for [Workload].
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show 3 recent postings from the flagged month in [Workload], with title, location and date.
```

```text
Which cities did the extra postings come from?
```

```text
Is this backed by a stated priority? Check their priorities in the same workloads.
```

## Tips for better results

- For retailers and logistics firms, look at a technology or corporate workload. Store hiring can swamp the company-wide total.
- Slowing is a signal too: it can mean a freeze, a reorganisation or a shift to outsourcing worth asking about.

## Related prompts

- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings and talking points.
- [What their job ads say about their stack](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press.
- [Priorities with no hiring behind them](../../prompts/04-signals-and-timing/priorities-vs-hiring.md): Which stated priorities have hiring behind them and which don't: the gaps where the account may need to buy rather than build.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_timeline_v3`, `accounts_hiring_demand_category_v3`

Status: **tested live**. Prompt id: `signals-hiring-spike`.

</details>

[Back to Signals and timing](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
