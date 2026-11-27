[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Discovery questions built on their data

> **An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a discovery call, so you lead with insight instead of 'tell me about your priorities'. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Everyone | 2–4 min | Priorities & opportunities, Tech stack, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | supply-chain and fulfilment modernisation services |
| `[Meeting with (optional)]` | SVP Technology, or a name |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my discovery coach. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. supply-chain and fulfilment modernisation services — skip if you ran the start-here prompt]
- Meeting with (optional): [name or title, e.g. SVP Technology]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the 8 most recent stated priorities in the meeting person's function, or else the function closest to [What I sell].
3. Pull technology added in the last 12 months (High and Medium usage) in that function; if none, use the function's current High and Medium stack and say so.
4. Pull hiring workloads trending up over 12 months in that function (ignore partial first and last months).
5. Pull hires and promotions for the most relevant workload; if only exits come back, note the count and use news instead.
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Opening insight": 2 sentences to open with, built on the strongest fact.
- "Discovery questions": # | Question | Hypothesis | Evidence (dated fact) | What a good answer tells me. Exactly 8: 3 priorities, 2 technology, 2 hiring, 1 leadership or news. Order: strategy, specifics, then timing and budget.
- "If you only ask two": the two that best qualify [What I sell].
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Open questions only, no pitches.
- Phrase evidence as a well-read seller would ("I saw you've been building out AI engineering"), never as surveillance.
- Each question cites a different fact; if a source has no data, use another and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- Leadership-move data can lag about 3 months; give the latest move date you saw.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Discovery prep for [Company]: bottom line and who else to invite, a 2-sentence opening insight, then 8 questions, each tied to a dated Draup fact, with the hypothesis and what a good answer tells me.
```

</details>

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
- Say who you're meeting; the prompt shifts priorities, technology and hiring to their function.

## Related prompts

- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive, two openers tied to the account's current priorities, and a dated reason to reach out now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_tech_stack_trend_v3`, `get_account_tech_stack_products_v3`, `accounts_hiring_demand_category_v3`, `get_account_executive_movement`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `people-discovery-questions`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
