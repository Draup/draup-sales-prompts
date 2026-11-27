# 10-minute pre-call snapshot

**Five short bullets you can read in the lobby: who they are, what just happened, where hiring is rising, the priority closest to your offer, and one question to ask.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a call in 10 minutes and no time for a full brief. | Account Executive, SDR / BDR, Account & Customer Success Manager, Presales & Solutions | Everyone | 1–2 min | Company & financials, News signals, Hiring & job postings, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | industrial AI and edge-cloud integration services |
| `[Meeting with]` | VP Digital Industries IT (optional) |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my pre-call research assistant. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. industrial AI and edge-cloud integration services — skip if you ran the start-here prompt]
- Meeting with: [optional title, e.g. VP Digital Industries IT]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile: what they do, workforce, latest revenue and its fiscal year.
3. Pull the top news from the last 90 days where [Company] is the actor.
4. Pull the top 3 workloads trending up in hiring (12 months), by postings; if fewer than 3 are rising, show those and say so.
5. Pull stated priorities and pick the one closest to [What I sell], preferring the function of the person I'm meeting.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- 0. If I named who I'm meeting: one priority they likely own, and their time in role if the title is on the first executives page for that function.
- Then exactly 5 bullets, 25 words or fewer each:
  1. What they do and their size (workforce, revenue, fiscal year).
  2. The 2 most important events from the last 90 days, each dated.
  3. The top 3 workloads trending up, with posting counts.
  4. The priority closest to [What I sell], with source and quarter.
  5. One open question that cites a fact from bullets 1–4.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If fewer than 2 real events exist, say so; don't pad.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Drop news noise: outages (unless I sell security), stock chatter, charity, awards, passing mentions, look-alike or sister companies, and re-dated old stories (use the event date in the text). Give source, headline and link if Draup has one.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Keep to about 180 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Call with [Company] in 10 minutes. Five bullets, 25 words each: what they do and size; 2 events from the last 90 days; top 3 workloads trending up; the priority closest to [What I sell]; one question.
```

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

## Tips for better results

- Name who you're meeting. Claude picks the priority in their function instead of the company-wide top one.
- If you have 30 minutes rather than 10, run the one-page account brief instead.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Hypothesis-led discovery questions](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive and two openers tied to the account's current priorities.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_top_signals`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `research-precall-snapshot`.

</details>

[Back to Account research](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
