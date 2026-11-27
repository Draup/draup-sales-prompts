# Numbers from the latest call

**Every number management stated on the latest earnings call (guidance, targets, KPIs, investment plans) in one table, with the three that matter for your deal and the question each opens.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a business case, a QBR, or an executive email that should use their numbers, not yours. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps | Everyone | 2–4 min | Earnings calls & filings |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | store and supply-chain technology modernisation |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my financial analyst for a sales team. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. store and supply-chain technology modernisation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first, and open the most recent analyst call. If the newest is a press call, use the latest analyst call and say so.
3. Note each executive's title from the introductions.
4. Extract every number an executive states: results, guidance, targets, capital spending, technology investment, store or site counts, headcount, AI or digital metrics, savings programmes.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Header: call date, the company's own name for the period, Draup's quarter label in brackets.
- "What they said", grouped as Guidance / Investment and capex / Operating KPIs / Technology, AI and digital: Metric | Value | Period it refers to | Actual, guidance or target | Raised, lowered or new (only if said) | Speaker | Quote (20 words or fewer). Up to 25 rows.
- "Numbers that matter for [What I sell]": 3 bullets, each a number, the conversation it opens and the question to ask.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Executives only; skip numbers that appear only in analysts' questions.
- Keep units and currency as stated ("$5 billion to $6 billion", "about 6%"). Don't round or convert unless I ask.
- Separate the period a number refers to from the call's quarter. Mark raised or lowered only if the speaker compares with earlier guidance.
- Draup's quarter label follows the fiscal year and can run ahead of the company's wording; show both.
- No transcript: say so and suggest the filing fallback in the leaders' own words prompt.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Keep to about 150 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Put every number management stated on [Company]'s latest earnings call in a table: metric, value, period, actual or guidance, speaker, short quote. Then the 3 that matter for [What I sell], each with a question to ask.
```

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

- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim quotes from leadership on your topic, with speaker, fiscal quarter and call date, or the annual-filing sections to read when there's no call.
- [What changed between two calls](../../prompts/01-account-research/call-over-call.md): Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, plus a 2-line talk track for your next QBR.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_transcripts`, `account_transcripts_v3`

Status: **tested live**. Prompt id: `research-numbers-from-the-call`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
