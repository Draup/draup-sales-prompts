[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Are they hiring more than usual?

> **A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Timing outreach, or checking a hunch that an account is gearing up (or slowing down). | SDR / BDR, Account Executive, Services, SI & Staffing Seller | Everyone | 2–4 min | Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | data and AI staff augmentation |
| `[Workload (optional)]` | Artificial Intelligence & Data Science |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my hiring-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. data and AI staff augmentation — skip if you ran the start-here prompt]
- Workload (optional): [a type of work, e.g. Artificial Intelligence & Data Science; blank uses the function closest to what I sell]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull monthly job postings for the last 12 months, company-wide and for the function closest to [What I sell] (or [Workload]); full months only, and say which months you used.
3. Work out the monthly average and standard deviation, and the last 5 full months against the 5 before.
4. Verdict on the last 3 full months (editable defaults): Spiking = any month over 2 standard deviations above average; Above normal = their average over 1 above; Slowing = over 1 below; Normal = anything else.
5. Label a flagged month seasonal if it's an industry peak (e.g. retail holidays), or company-wide if many unrelated workloads rose together.
6. For each flagged month, list the top 5 workloads against their usual month.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: one plain-English line (e.g. "Above normal in IT, not seasonal") with the 5-vs-5 change in %, for the function and company-wide.
- Table (last 6 full months, function view): Month | Postings | Gap from average (standard deviations) | Flag.
- Table "What drove it" (top 5): Workload | Postings in flagged month | Usual month | Likely owner.
- Detail: the full 12-month series; the company-wide view; "Why this matters for [What I sell]" (2–3 bullets); Gaps (what Draup lacked, to ask in discovery).

RULES
- Standard deviations go in the table; the verdict uses plain words.
- State the exact window, e.g. "Dec 2025 – Oct 2026".
- A seasonal frontline spike is rarely a buying signal; say so when it's the driver.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Is [Company] hiring more than usual in the function closest to [What I sell]? Last 5 full months vs the 5 before, flagged months, drivers, and whether it's seasonal.
```

</details>

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

```text
Write a 70-word email to the person in the next step about the capability being built, with no posting counts.
```

## Tips for better results

- The function view is the one that matters: store or warehouse hiring can swamp a retailer's company-wide total.
- Slowing is a signal too: it can mean a freeze, a reorganisation or a shift to outsourcing worth asking about.

## Related prompts

- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.
- [Which tools their job ads are building](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press, with a named person to call.
- [Priorities with no hiring behind them](../../prompts/04-signals-and-timing/priorities-vs-hiring.md): Which stated priorities in your function have hiring behind them and which don't: the gaps where the account may need to buy rather than build, with a named person to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_timeline_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `signals-hiring-spike`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
