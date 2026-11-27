[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Are they really investing in X?

> **A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you claim an account is "investing in GenAI" (or SAP, or cloud) in a pitch or email. | Account Executive, Presales & Solutions, SDR / BDR | Everyone | 2–4 min | Hiring & job postings, Talent flow & locations, Priorities & opportunities, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[Technology]` | generative AI for software development |
| `[What I sell]` | AI developer-productivity platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my investment-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

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
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Start with the verdict: Yes (rising hiring, growing headcount and a stated priority), Early (rising hiring only) or No.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 8): Skill | 12-month postings | Avg/month, prior 5 | Avg/month, last 5 | Note.
- "Talking points": 3, each with a number and its date.
- Detail: proof postings (Title | Date | Location | What the role does); headcount (job family, then and now, % change, months covered); stated priorities (name, source, quarter, likely owner); Gaps (what Draup lacked, to ask in discovery).

RULES
- "Rising" = the last 5 full months beat the 5 before by more than 20% (editable default).
- Salaries are often missing from postings; don't estimate them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Talent-flow data ends about 3 months ago; state the months covered.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line (Yes, Early or No) and next step first, with a named owner. Is [Company] really investing in [Technology]? Related job-ad skills, last 5 full months vs the 5 before, 3 proof postings, headcount trend and stated priorities.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which tools did they start hiring for from near zero this year?
```

```text
Who leads this area? Find executives tagged to the matching workload.
```

```text
Turn the talking points into a 3-sentence opener for the person in the next step.
```

```text
Compare the same theme at [a peer] so I can say whether they're ahead or behind.
```

## Tips for better results

- Use Draup's own skill names. The assistant reads them off the trending list first, so broad labels don't come back empty.
- Early is often a good verdict for a seller: hiring is rising but the work isn't fully staffed yet.

## Related prompts

- [Which tools their job ads are building](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press, with a named person to call.
- [Priorities with no hiring behind them](../../prompts/04-signals-and-timing/priorities-vs-hiring.md): Which stated priorities in your function have hiring behind them and which don't: the gaps where the account may need to buy rather than build, with a named person to call.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_hiring_job_postings_v3`, `accounts_talent_flow_workforce_trends_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `signals-investing-in-x`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
