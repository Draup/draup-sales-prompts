[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Executive profile and openers

> **A one-screen profile of a named executive, two openers tied to the account's current priorities, and a dated reason to reach out now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before an email, call or meeting with a specific senior person. | Account Executive, SDR / BDR, Account & Customer Success Manager | Everyone | 2–4 min | Executives & movement, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Executive name]` | Jane Doe |
| `[Company]` | target.com |
| `[Business function]` | IT |
| `[What I sell]` | AI platform engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales research assistant. Use Draup for Sales for every fact.

INPUTS (edit these)
- Executive name: [e.g. Jane Doe]
- Company: [website, e.g. target.com]
- Business function: [their likely function, e.g. IT]
- What I sell: [one line, e.g. AI platform engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. There is no name search: page through key executives in [Business function], 10 per page, up to 50, and stop when you find the name (allow initials and short forms).
3. If not found, show the top 5 in that function (name, full title) and ask which I mean. Don't guess.
4. Pull up to 5 recent priorities for their workloads; if none come back, use their business function.
5. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (usually this executive), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: name, full title from the profile, location, LinkedIn.
- "Profile": Time at company | Time in current title | Budget control | Workloads | Previous employer and title | Past companies.
- "What they likely own": 2 priorities from their area, each with source and quarter.
- "Openers": 2 openers (35 words or fewer), each tied to a named priority and [What I sell]; one may mention their previous employer.
- "One question to ask": open-ended, citing a priority.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Under 12 months in the current title is a timing signal; mention it.
- Say if the person belongs to a subsidiary or acquired brand.
- If not found and likely in Europe or the UK, say the profile may be restricted.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 380 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Profile [Executive name] at [Company] ([Business function]): bottom line and why reach out now, then full title, time in role, past companies, budget control, 2 openers tied to current priorities and one question.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 90-word email using opener 1.
```

```text
Who does this person likely work with? Map the buying committee around them.
```

```text
What does their previous employer run in my category?
```

## Tips for better results

- Give the function you think they're in. Large companies have thousands of profiles, so the right function makes the search much faster.
- Openers tied to a named priority often land better than ones tied to the person's career.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `people-executive-profile`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
