[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What's worth acting on now

> **Up to 5 real triggers from the last 90 days, each tied to a stated priority, a likely owner and a suggested action, with the noise stripped out.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before outreach, at the start of an account cycle, or when an account has gone quiet. | SDR / BDR, Account Executive, Account & Customer Success Manager | Everyone | 2–4 min | News signals, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[What I sell]` | AI governance software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales-trigger analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- What I sell: [one line, e.g. AI governance software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the company's top-ranked news signals and its news feed for the last 90 days. Review at least 30 items, or say how many there were.
3. Apply the noise rule; also drop store or branch closures counted as layoffs. The company must be the actor, not a supplier, customer or owner.
4. Keep executive moves (VP and above), M&A, partnerships, expansion, capex or investment plans, restructuring, and launches that touch my space. Merge repeat coverage.
5. Link each trigger to a stated priority only if the text supports it, with source and fiscal quarter; otherwise "no direct link".
6. Rank by relevance to [What I sell], then recency.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table (up to 5): Date | Trigger (with any number) | Type | Source and headline | Linked priority (quarter) | Likely owner | Why it matters for [What I sell] | Action (call, email, loop in partner, watch).
- If fewer than 3 real triggers survive, say so. Don't pad.
- "Dropped as noise": count by type.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If the event and capture dates differ by more than 30 days (editable default), use the event date and flag it.
- In the next step, give the one trigger to act on this week and an opening sentence.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
What are the real triggers at [Company] in the last 90 days? Skip outages, stock chatter, charity and passing mentions. Up to 5, each with date, source, linked priority, likely owner and why it matters for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the top trigger into a 70-word email to the right executive.
```

```text
Who is the new executive in trigger [N]? Pull their professional profile.
```

```text
Run the same check for the last 30 days only.
```

## Tips for better results

- Large companies attract a lot of noise (outages, stock moves, lawsuits). The noise count tells you how much was filtered.
- Fewer than 3 real triggers is a useful answer: lead with a priority, not a news hook.

## Related prompts

- [Signal-to-email (one or a few accounts)](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 5 per pass: the freshest relevant signal, the priority it supports, and a short, sourced opener for your persona that ends in one low-friction ask.
- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of everything material that changed at an account since a date you choose, ranked by impact on your deal.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_top_signals`, `get_account_signals`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `signals-whats-actionable`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
