[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Priorities with no hiring behind them

> **Which stated priorities in your function have hiring behind them and which don't: the gaps where the account may need to buy rather than build, with a named person to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Shaping a services or software pitch, or deciding which priority to lead with. | Account Executive, Services, SI & Staffing Seller, Presales & Solutions | Everyone | 2–4 min | Priorities & opportunities, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | intelligent automation and RPA services |
| `[Business function (optional)]` | Supply Chain |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. intelligent automation and RPA services — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Supply Chain, IT; blank uses the function closest to what I sell]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Pull the workloads in the stated priorities for the function, ranked by how many priorities involve each. Keep the top 15. If the function has none, say so and don't borrow from others.
3. Pull hiring by workload for the last 12 months, up to 5 pages: postings and trend. Set frontline workloads (store operations, food and beverage, warehousing) aside unless they relate to what I sell.
4. Match each priority workload to its hiring; where names differ, use the closest and say so.
5. Mark each (editable defaults): Backed = top 20 hiring workload or trending up; Partial = 50+ postings but not Backed; Thin = under 50; Silent = none; Not comparable = strategy or governance work that rarely appears in job ads.
6. For the 3 biggest gaps (most priorities, least hiring), pull the priority names with source and fiscal quarter.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] and [Company]'s top 90-day news item where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- "Build-or-buy gaps" (top 3): priority, source and quarter, hiring numbers, and why [What I sell] could fill it.
- Table (top 10): Workload | Priorities involving it | Postings (12 months) | Trend | Read.
- Detail: the remaining workloads; "Already backed" (2–3 workloads they're building in-house, with likely owners); Gaps (to ask in discovery).

RULES
- Little hiring doesn't prove they will buy; they may already outsource the work. Say so, and suggest checking their outsourcing for those workloads.
- State the hiring window.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the function closest to What I sell (e.g. IT) and say which; map any function I give to its main workloads and name them.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 380 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Compare [Company]'s priority workloads in my function with 12 months of hiring; mark each Backed, Partial, Thin or Silent, and name the 3 biggest build-or-buy gaps for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top gap, which service providers already work that workload at [Company]?
```

```text
Who owns the top gap? List executives tagged to that workload.
```

```text
Write a one-paragraph point of view on the top gap for the person in the next step.
```

```text
Run the same check for [another function].
```

## Tips for better results

- Silent or Thin workloads with several priorities are worth testing as buy signals, after you check who already does the work for them.
- Backed workloads still matter. They show where the account has in-house teams you'd work alongside.

## Related prompts

- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_priorities_top_workloads_v3`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `signals-priorities-vs-hiring`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
