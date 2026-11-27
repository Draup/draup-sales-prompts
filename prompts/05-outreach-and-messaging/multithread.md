[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Emails to three buyers at one account

> **A thread map for one account (economic buyer, technical buyer and champion), each named from Draup and tied to a different stated priority, with two fact-checked emails per person and a staggered send plan.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A deal depends on more than one person and you want to open three conversations at once without sending the same email three times. | Account Executive, SDR / BDR, Account & Customer Success Manager, Sales Leader & RevOps | Everyone | 4–6 min | Priorities & opportunities, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | supply-chain planning software |
| `[Personas (optional)]` | CFO, Head of Supply Chain IT, SVP Supply Chain Planning |
| `[Proof point (optional)]` | cut planning cycle time at Fabrikam Foods |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-based sequencing strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Personas (optional): [three titles, e.g. CFO, Head of Supply Chain IT, SVP Supply Chain Planning; blank and I'll suggest them]
- Proof point (optional): [e.g. cut planning cycle time at Fabrikam Foods]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Pull the account's key priorities grouped by function in one pass (up to 3 per function).
3. Give each persona a distinct priority: Economic buyer (Finance or Management & Strategy), Technical buyer (IT or the function's systems), Champion (the operating function closest to [What I sell]). Use my titles if given.
4. For each persona's function, pull 5 key executives and pick the likeliest by full profile title; drop titles that don't fit and flag subsidiaries. No economic buyer? Widen once as the People rule says. A "verify" C-level profile gets no email: address that thread to the office or hold it.
5. Pull top-ranked news from the last 90 days; keep one Confirmed item all three threads can use (the account must be the actor).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for. Start with the champion.
- "Check before sending" (directly above the copy): single-source or disputed facts the copy leans on and any "verify" profile, with what to check; or "none".
- Per persona: Email 1 (subject 6 words max, body 90 words max) on that persona's priority; Email 2 (day 4, 50 words max) on the shared news item or a second fact; same single ask in both.
- Table "Thread map": Persona | Name | Full title | Priority (quarter) | Angle in one line.
- Send plan: champion day 1, technical buyer day 3, economic buyer day 6, and what to do if one replies.
- Detail: priorities in Draup's words with source; "Roles with no clear person" (titles to look for); Gaps (to ask in discovery).

RULES
- Never reuse a paragraph across threads. Never write "I've also contacted your colleagues" or CC anyone. Buyer roles are candidates, labelled "likely".
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources, never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 500 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (who to email first, named). Give [Company]'s economic buyer, technical buyer and champion each a different priority, name a person for each, and write two emails each with a staggered send plan.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Add a fourth thread for procurement, tied to a sourcing priority.
```

```text
Write a LinkedIn connection note for each of the three people.
```

```text
One of them replied positively; draft the internal-champion brief I should send them.
```

```text
Swap the economic buyer for the CIO and rewrite that thread.
```

## Tips for better results

- The grouped-priorities view covers every function in one pass, so you can see at a glance which leaders share an agenda.
- In conglomerates, executive lists often include business-unit heads under a shared function tag; check the full title before you pick.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.
- [ABM openers for 10 accounts at once](../../prompts/16-content-and-enablement/abm-messages.md): A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.
- [LinkedIn note and InMail to an executive](../../prompts/05-outreach-and-messaging/linkedin-exec.md): A confirmed profile for one named executive, a 300-character connection note with no pitch, a 110-word InMail tied to a stated priority in their remit, and a short message for after they accept.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_key_account_priorities`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `outreach-multithread`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
