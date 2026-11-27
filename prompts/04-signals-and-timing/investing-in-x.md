# Are they really investing in X?

**A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings and talking points.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you claim an account is "investing in GenAI" (or SAP, or cloud) in a pitch or email. | Account Executive, Presales & Solutions, SDR / BDR | Everyone | 2–4 min | Hiring & job postings, Talent flow & locations, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[Technology]` | generative AI for software development |
| `[What I sell]` | AI developer-productivity platform |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my investment-signals analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Technology: [theme in plain words, e.g. generative AI for software development]
- What I sell: [one line, e.g. AI developer-productivity platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the skills and workloads in the company's job postings over the last 12 months, trending up first, and pick those related to my theme using Draup's exact names. Broad labels ("Generative AI") may match nothing; specific ones ("AI-Assisted Development") usually do.
3. For each: 12-month postings and average per month in the last 5 full months against the 5 before. Flag one-off spikes (one month over half the total). Read declining skills' monthly numbers before trusting the label.
4. Pull 3 recent postings for the strongest skill: title, date, location, key responsibilities.
5. Pull the headcount trend for the matching job family (e.g. software developers): a year before the latest month against the latest month.
6. Pull stated priorities that mention the theme, with source and fiscal quarter.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Verdict: Yes (rising hiring, growing headcount and a stated priority), Early (rising hiring only) or No, with a one-line reason.
- Table (top 8): Skill | 12-month postings | Avg/month, prior 5 | Avg/month, last 5 | Note.
- "Proof postings": Title | Date | Location | What the role does.
- "Headcount": job family, then and now, % change, months covered.
- "Stated priorities": name, source, quarter, likely owner.
- "Talking points": 3, each with a number.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- "Rising" = the last 5 full months beat the 5 before by more than 20% (editable default).
- Salaries are often missing from postings; don't estimate them.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Talent-flow data ends about 3 months ago; state the months covered.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Keep to about 330 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Is [Company] really investing in [Technology]? Show related job-ad skills (last 5 full months vs the 5 before), 3 proof postings, the matching job family's headcount trend and stated priorities, then a Yes / Early / No verdict.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which tools did they start hiring for from near zero this year?
```

```text
Who leads this area? Find executives tagged to the matching workload.
```

```text
Turn the talking points into a 3-sentence opener for the CTO.
```

## Tips for better results

- Use Draup's own skill names. Claude reads them off the trending list first, so broad labels don't come back empty.
- Early is often a good verdict for a seller: hiring is rising but the work isn't fully staffed yet.

## Related prompts

- [What their job ads say about their stack](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press.
- [Priorities with no hiring behind them](../../prompts/04-signals-and-timing/priorities-vs-hiring.md): Which stated priorities have hiring behind them and which don't: the gaps where the account may need to buy rather than build.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings are running above or below normal, which workloads drive it, and whether it's seasonal.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_hiring_job_postings_v3`, `accounts_talent_flow_workforce_trends_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `signals-investing-in-x`.

</details>

[Back to Signals and timing](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
