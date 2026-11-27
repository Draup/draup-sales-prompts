# Hypothesis-led discovery questions

**An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a discovery call, so you lead with insight instead of 'tell me about your priorities'. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Everyone | 2–4 min | Priorities & opportunities, Tech stack, Hiring & job postings, Executives & movement, News signals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | supply-chain and fulfilment modernisation services |
| `[Meeting with]` | SVP Technology (optional) |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my discovery coach. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. supply-chain and fulfilment modernisation services — skip if you ran the start-here prompt]
- Meeting with: [optional title, e.g. SVP Technology]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the 8 most recent stated priorities, preferring the meeting person's function.
3. Pull technology added in the last 12 months (High and Medium usage).
4. Pull hiring workloads trending up over 12 months (ignore partial first and last months).
5. Pull hires and promotions (6 months) for the most relevant workload, and the top 90-day news.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Opening insight": 2 sentences to open with, built on the strongest fact.
- "Discovery questions": # | Question | Hypothesis | Evidence (dated fact) | What a good answer tells me. Exactly 8: 3 priorities, 2 technology, 2 hiring, 1 leadership or news. Order: strategy, specifics, then timing and budget.
- "If you only ask two": the two that best qualify [What I sell].
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Open questions only, no pitches.
- Phrase evidence as a well-read seller would ("I saw you've been building out AI engineering"), never as surveillance.
- Each question cites a different fact; if a source has no data, use another and say so.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If leadership-move results are too large to read, say so and use executive-movement news for the same period instead.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Drop news noise: outages (unless I sell security), stock chatter, charity, awards, passing mentions, look-alike or sister companies, and re-dated old stories (use the event date in the text). Give source, headline and link if Draup has one.
- Draup shows about the 10 latest moves per type and can't filter them by function: narrow by workload, say how many rows you checked and the latest move date, and keep only rows where [Company] is the current employer.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Give me a 2-sentence opening insight and 8 discovery questions for [Company], each tied to a dated Draup fact (priority, technology, hiring, leadership move or news), with the hypothesis and what a good answer tells me.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write the answers I'd hope to hear and how I'd respond to each.
```

```text
Turn the top 2 questions into a meeting agenda email.
```

```text
Pre-fill MEDDPICC for this deal from the same evidence.
```

## Tips for better results

- Questions grounded in their own priorities often earn more airtime than generic discovery.
- Say who you're meeting; the prompt shifts the priorities to their function.

## Related prompts

- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Five short bullets you can read in the lobby: who they are, what just happened, where hiring is rising, the priority closest to your offer, and one question to ask.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet pre-filled with what Draup can show (metrics, buyer candidates, pain, competition) and clear 'must discover' flags for the rest.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive and two openers tied to the account's current priorities.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_tech_stack_trend_v3`, `accounts_hiring_demand_category_v3`, `get_account_executive_movement`, `get_top_signals`

Status: **tested live**. Prompt id: `people-discovery-questions`.

</details>

[Back to Buyers and stakeholders](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
