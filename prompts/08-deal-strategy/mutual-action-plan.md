[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Mutual action plan on their calendar

> **A mutual action plan built backwards from your close date that respects the buyer's fiscal calendar, names buyer owners at each step, flags events that could move dates and says who to send the draft to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You've agreed a target close date and want a plan both sides sign up to. Use this once the date is agreed; use "Pick a realistic signature window" instead to test the date first. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 4–6 min | Company & financials, Earnings calls & filings, Executives & movement, News signals, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | starbucks.com |
| `[Deal stage]` | technical evaluation complete |
| `[Target close date]` | 2027-01-29 |
| `[Steps still needed]` | security review, business case sign-off, procurement, legal (optional) |
| `[What I sell]` | data-platform modernisation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my deal desk lead. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- Deal stage: [e.g. technical evaluation complete]
- Target close date: [e.g. 2027-01-29]
- Steps still needed (optional): [e.g. security review, business case sign-off, procurement, legal]
- What I sell: [one line, e.g. data-platform modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Plans that ignore the buyer's calendar slip; give every step a buyer owner.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use the function closest to [What I sell]; say which.
3. Fiscal calendar: the latest fiscal year and end date from Draup's financials; the last 5 earnings calls (label, release date). Infer year-end, the next call and quarter-ends in the window.
4. Stakeholders: function executives (one page of 10) and Procurement executives (5): technology or indirect procurement, and anyone under 1 year in title.
5. Events, last 90 days and announced for the window (15+ items): leadership changes with effective dates, reorganisations, divestments, spin-offs, investor events.
6. Up to 3 recent priorities in the function to anchor the objective.
7. Build backwards from [Target close date] using [Steps still needed], or the default: business case, security review, procurement, legal, executive approval, signature, kickoff.

OUTPUT
- Bottom line: 2 sentences — Achievable, Tight or Unrealistic, with an alternative date if needed.
- Recommended next step: a named person (name, full title) to send the draft plan to, the action this week and the dated why-now (or say none).
- Table "Mutual action plan" (up to 8): Step | Target date | Buyer owner and ours | Exit criteria | Calendar note.
- Table "Buyer calendar" (up to 6): Date | Event (fiscal year-end, quarter-end, earnings call, leadership start) | Effect on the plan.
- "Objective": one sentence in the buyer's words, tied to a dated priority.
- "Timeline risks": up to 3, each with the step it threatens and a mitigation.
- Detail: "Stakeholders" (Name | Full title | Role: approver, reviewer, signer, user | In title since), up to 8.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Never assume a calendar fiscal year; derive it from financials and call dates and say how.
- A senior leader starting or leaving inside the window is a timeline risk; name the effective date.
- Default durations (editable): security review 3 weeks, procurement 3, legal 2, executive approval 1.
- Don't name subsidiary executives as approvers unless the deal is with that unit. Label future call dates "inferred".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Mutual action plan for [Company] from [Deal stage] to [Target close date]. Lead with Achievable, Tight or Unrealistic and who to send the draft to, then milestones with buyer owners and calendar events that could shift dates.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the plan into a one-page document I can share with the buyer (no internal notes).
```

```text
Draft the email proposing this plan to my champion.
```

```text
Which steps can run in parallel to pull the close date in by two weeks?
```

## Tips for better results

- Share the plan as a draft and ask the buyer to correct dates; their edits are the best signal of real intent.
- Name buyer owners by function first; confirm names with your champion before sharing.
- Earnings dates are inferred from past calls; check the investor-relations calendar before you commit.

## Related prompts

- [Pick a realistic signature window](../../prompts/08-deal-strategy/budget-timing.md): Whether your close date fits the buyer's fiscal calendar and budget posture, the events that move money in the next two quarters, the best 4–8 week signature window and the named person to confirm it with.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Arm your champion to sell internally](../../prompts/08-deal-strategy/champion-pack.md): A forwardable brief your champion can use to sell the deal inside: why now in their company's words, cost of waiting, answers for the CFO, CIO and procurement, a 150-word internal email, and who to route it to.
- [Prepare for their procurement team](../../prompts/08-deal-strategy/procurement-landscape.md): The procurement stance to expect (consolidate, cost-down, re-bid or strategic), who already supplies the work in scope and how concentrated they are, the pressure procurement is under and the named procurement lead to reach.
- [Brief for a C-level pursuit meeting](../../prompts/11-account-planning/cxo-pursuit-brief.md): A one-page pursuit brief for a C-level meeting: the 3 workloads to lead with, the buyers, incumbents, a Go or Not-yet evidence check, what to learn in meeting 1 and a 90-day plan.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_financials_v3`, `get_account_transcripts`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `deals-mutual-action-plan`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
