[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# 10-minute pre-call snapshot

> **Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a call in 10 minutes. Use the one-page account brief instead when you have 30 minutes or need the numbers and a competitor check. | Account Executive, SDR / BDR, Account & Customer Success Manager, Presales & Solutions | Everyone | 1–2 min | Company & financials, News signals, Hiring & job postings, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | medtronic.com |
| `[What I sell]` | application modernisation and cloud migration services |
| `[Meeting with (optional)]` | VP Global IT, or a name |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pre-call research assistant. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- What I sell: [one line, e.g. application modernisation and cloud migration services — skip if you ran the start-here prompt]
- Meeting with (optional): [name or title, e.g. VP Global IT]

CONTEXT (why this matters)
Ten minutes is enough for one good opener. Company-wide hiring at a large firm is dominated by store, plant or care roles, so this prompt looks only at the function you sell into.

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile: what they do, workforce, latest revenue and its fiscal year.
3. Pull the top news from the last 90 days where [Company] is the actor.
4. Pull the top 3 workloads (types of work, e.g. Cloud Computing) trending up in hiring (12 months), by postings, in the business function closest to [What I sell] (e.g. IT); if none is rising there, show that function's top 3 by postings with their trend.
5. Pull stated priorities for the function closest to [What I sell] and pick the one closest to [What I sell], preferring the function of the person I'm meeting.
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role), and look there for the person I'm meeting.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- If I named who I'm meeting: one priority they likely own, and their time in role if step 6 found them.
- Then exactly 5 bullets, 25 words or fewer each:
  1. What they do and their size (workforce, revenue, fiscal year).
  2. The 2 most important events from the last 90 days, each dated.
  3. Hiring in [function]: the top 3 workloads with posting counts and trend (rising, flat or falling).
  4. The priority closest to [What I sell], with source and quarter.
  5. One open question that cites a fact from bullets 1–4.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If fewer than 2 real events exist, say so; don't pad.
- If the website match isn't exact or lands on a subsidiary, say which company you used.
- Executive function tags are loose: skip anyone whose title clearly sits outside the function (e.g. a business-unit president).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 350 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Call with [Company] in 10 minutes. Bottom line and who to contact first, then five 25-word bullets: size; 2 events from 90 days; hiring in the function closest to [What I sell]; its closest priority; one question.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Give me 3 more questions like bullet 5, each tied to a different fact.
```

```text
Who else from [Company] should be in the next meeting?
```

```text
Expand bullet 2: what changed and why it matters for [What I sell].
```

```text
Show company-wide hiring too, so I can see where the overall headcount is going.
```

## Tips for better results

- Name who you're meeting. Claude picks the priority in their function and checks their time in role.
- If you have 30 minutes rather than 10, run the one-page account brief instead.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive, two openers tied to the account's current priorities, and a dated reason to reach out now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_top_signals`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `research-precall-snapshot`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
