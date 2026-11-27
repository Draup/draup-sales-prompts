[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Executive profile and openers

> **A short profile of one senior person, found by name or just by title, with time in role, past companies, what they likely own, a competitor check and two openers. If Draup has no one with that title, you're told so up front and given the 3 closest people.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before an email, call or meeting with a specific senior person, even when you only know their title ("the CISO"). Use "One-page account brief" instead when you need the whole account too. | Account Executive, SDR / BDR, Account & Customer Success Manager | Everyone | 2–4 min | Executives & movement, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Executive (name or title)]` | Jane Doe, or CISO |
| `[Company]` | target.com |
| `[Business function]` | IT |
| `[Competitor (optional)]` | CrowdStrike or Accenture; defaults to your saved competitors |
| `[What I sell]` | AI platform engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales research assistant. Use Draup for Sales for every fact.

INPUTS (edit these)
- Executive: [a name or a title, e.g. Jane Doe, or CISO]
- Company: [website, e.g. target.com]
- Business function: [their likely function, e.g. IT]
- Competitor (optional): [vendor, product or services firm, e.g. CrowdStrike; default: my saved competitors]
- What I sell: [one line, e.g. AI platform engineering services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Find the person; there is no name or title search. For a title, first pull the workload closest to it (e.g. Cybersecurity for a CISO). Then page through [Business function], 10 per page, up to 3 pages, and stop at the first match. Allow initials and short forms for names; match titles on the full profile title, not the role tag.
3. No match: don't guess. Say "[name or title] isn't in Draup", list the 3 closest people (name, full title, why close), build the rest for that role, and ask me to confirm the name from the invite.
4. Pull up to 5 recent priorities for their workloads; if none, use their business function.
5. If I named a competitor, check the whole stack for its products; for a services firm, its share of active engagements in those workloads.
6. Pull the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]; if the person isn't in Draup, say so first.
- Recommended next step: one person by name and title (this executive, else the best of the closest 3), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: name, full title, location, LinkedIn. Not found: "Closest in Draup": Name | Full title | Why close.
- "Profile": Time at company | Time in title | Budget control | Workloads | Previous employer and title | Past companies.
- "What they likely own": 2 priorities, each with source and quarter.
- "Competitor check" (if named): product, usage strength, last seen and rating, or "not present at High or Medium".
- "Openers": 2 (35 words or fewer), each tied to a named priority and [What I sell]; one may mention their previous employer.
- "One question to ask": open-ended, citing a priority.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Under 12 months in the title is a timing signal; mention it.
- A deputy, segment or business-unit holder of a title is not the enterprise holder; say which.
- Not found and likely in Europe or the UK: say the profile may be restricted.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. Professional information only.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Competitor rating: a [Competitor] product at High usage in the workloads I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber. Services rival, by share of the account's active engagements in those workloads: 30%+ Red, 10–29% Amber, under 10% Green.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Profile [Executive] (name or title) at [Company]: bottom line and why now, full title, time in role, past companies, 2 openers on current priorities, [Competitor] rated Red/Amber/Green. Not in Draup? Say so and show the 3 closest.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 90-word email using opener 1.
```

```text
Who does this person likely work with? Run "Map the buying committee" around them.
```

```text
What does their previous employer run in my category?
```

## Tips for better results

- A title is enough ("CISO", "VP Supply Chain"). If Draup has no one with it, the answer says so in the first line and gives the 3 closest people instead of guessing.
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
