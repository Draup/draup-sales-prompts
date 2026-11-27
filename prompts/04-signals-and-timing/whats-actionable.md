[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What's worth acting on now

> **An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before outreach, at the start of an account cycle, or when an account has gone quiet. Use this for one account; use "Weekly trigger sweep for my book" for up to 10 accounts at once. | SDR / BDR, Account Executive, Account & Customer Success Manager | Everyone | 2–4 min | News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[What I sell]` | AI governance software |
| `[Territory (optional)]` | North America |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales-trigger analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- What I sell: [one line, e.g. AI governance software — skip if you ran the start-here prompt]
- Territory (optional): [region I cover, e.g. North America — skip if saved in setup]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull its top-ranked news signals and news feed for the last 90 days; review at least 30 items, or say how many there were.
3. Apply the noise rule (it depends on what I sell); also drop store closures counted as layoffs. The company must be the actor.
4. Keep executive moves (VP and above), M&A, partnerships, expansion, investment plans, restructuring, regulatory inquiries or fines, and incidents or launches that touch my space. Merge repeat coverage; count independent sources.
5. Link each trigger to a stated priority in the function closest to [What I sell] only if the text supports it (source, fiscal quarter); else "no direct link".
6. Rank by relevance to [What I sell], then events in my territory, then recency.
7. Pull the top 3 executives in the function closest to [What I sell] and match each trigger to its likeliest owner, checking titles in the profile bio.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Start with Act, Watch or Skip.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for. Add an opening sentence built on a Confirmed trigger.
- Table "Triggers" (up to 5; if fewer than 3 survive, say so and don't pad): Date | Trigger (with any number) | Why it matters to us | Likely owner (name, title) | Sources (1 = unverified).
- Detail: per trigger, source and headline (link), linked priority (quarter) and action; "Dropped as noise" count by type, naming any incident and whether it was kept; Gaps (what Draup lacked, to ask in discovery).

RULES
- If event and capture dates differ by over 30 days, use the event date and flag it.
- Never build the opening sentence on a single-source or conflicting fact.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell (e.g. IT) and say which. If I give a function, map it to its main workloads first and name them.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line first (Act, Watch or Skip) and next step: a named owner and one dated trigger. Then up to 5 real 90-day triggers at [Company] that bear on [What I sell], incidents included, with source counts.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the top trigger into a 70-word email to the person in the next step.
```

```text
Who is the new executive in trigger [N]? Pull their professional profile.
```

```text
Run the same check for the last 30 days only.
```

```text
Which of these triggers has a second source I can quote?
```

## Tips for better results

- Outages, incidents and regulatory inquiries are kept when they bear on what you sell (security, reliability, observability, IT operations, compliance). Put your offer in the start-here prompt so the filter knows.
- A trigger marked "1 = unverified" is fine for prioritising but not for quoting; the email follow-up will warn you before you send it.
- Fewer than 3 real triggers is a useful answer: lead with a priority, not a news hook.

## Related prompts

- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.
- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_top_signals`, `get_account_signals`, `get_signal_news_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `signals-whats-actionable`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
