[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Numbers from the latest earnings call

> **The three numbers from the latest earnings call that matter for your deal, the question each opens and who to raise them with, plus every stated number in a reference table.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a business case, a QBR, or an executive email that should use their numbers, not yours. Use "Their leaders' own words on [Topic]" instead when you want quotes on a theme. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps | Everyone | 2–4 min | Earnings calls & filings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | store and supply-chain technology modernisation |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my financial analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. store and supply-chain technology modernisation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first, and open the most recent analyst call. If the newest is a press call, use the latest analyst call and say so.
3. Note each executive's title from the introductions.
4. Extract every number an executive states: results, guidance, targets, capital spending, technology investment, site counts, headcount, AI or digital metrics, savings programmes.
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: call date, the company's own name for the period, Draup's quarter label in brackets.
- "Numbers that matter for [What I sell]": Number | Period it refers to | Speaker | Question it opens. Exactly 3.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Everything they said", grouped as Guidance / Investment and capex / Operating KPIs / Technology, AI and digital: Metric | Value | Period | Actual, guidance or target | Speaker. Up to 15 rows, then offer the rest.

RULES
- Executives only; skip numbers that appear only in analysts' questions.
- Keep units and currency as stated ("$5 billion to $6 billion", "about 6%"). Don't round or convert unless I ask.
- Separate the period a number refers to from the call's quarter. Mark raised or lowered only if the speaker compares with earlier guidance.
- No transcript: say so and suggest the filing fallback in "Their leaders' own words on [Topic]".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
From [Company]'s latest earnings call: bottom line and who to raise it with, then the 3 numbers that matter for [What I sell], each with period, speaker and a question to ask.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Compare these with the previous call's numbers. What moved?
```

```text
Build a one-slide business case using the three numbers that matter.
```

```text
Which of these numbers ties to a stated priority in Draup?
```

## Tips for better results

- Their own guidance is the strongest anchor for a business case. Quote it rather than analyst estimates.
- Press calls usually carry less guidance; the prompt switches to the analyst call.

## Related prompts

- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.
- [What changed between two earnings calls](../../prompts/01-account-research/call-over-call.md): Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, who owns them, and a 2-line talk track for your next QBR.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_transcripts`, `account_transcripts_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-numbers-from-the-call`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
