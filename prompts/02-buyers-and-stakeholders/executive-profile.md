# Executive profile and openers

**A one-screen profile of a named executive and two openers tied to the account's current priorities.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before an email, call or meeting with a specific senior person. | Account Executive, SDR / BDR, Account & Customer Success Manager | Everyone | 2–4 min | Executives & movement, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Executive name]` | Jane Doe |
| `[Company]` | target.com |
| `[Business function]` | IT |
| `[What I sell]` | AI platform engineering services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my sales research assistant. Use the Draup for Sales connector for every fact.

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

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Header: name, full title from the profile, location, LinkedIn.
- "Profile": Time at company | Time in current title | Budget control | Workloads | Previous employer and title | Past companies | Schools.
- "What they likely own": 2 priorities from their area, each with source and fiscal quarter.
- "Openers": 2 openers (35 words or fewer), each tied to a named priority and [What I sell]; one may mention their previous employer.
- "One question to ask": open-ended, citing a priority.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Under 12 months in the current title is a timing signal; mention it.
- Say if the person belongs to a subsidiary or acquired brand.
- If not found and likely in Europe or the UK, say the profile may be restricted.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level (if none appears, say so in Gaps).
- Professional information only (name, title, employer, Draup's profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 250 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Find [Executive name] in [Company]'s [Business function] leaders and profile them: full title, time in role, past companies, schools, workloads, budget control. Then 2 openers tied to current priorities in their area and one question.
```

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

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Hypothesis-led discovery questions](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Five short bullets you can read in the lobby: who they are, what just happened, where hiring is rising, the priority closest to your offer, and one question to ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `people-executive-profile`.

</details>

[Back to Buyers and stakeholders](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
