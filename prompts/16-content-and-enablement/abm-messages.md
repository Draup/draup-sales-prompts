[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# ABM messages for a target list

> **A table of short, personalised openers, 5 accounts per pass, each tied to one stated priority and one dated signal from the last 60 days, with sources and an optional partner or proof angle.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're launching an ABM play, an SDR sprint or a joint campaign with a partner on a named list and need a first touch that isn't generic. | Marketing & ABM, SDR / BDR, Account Executive, Partnerships & Alliances | Everyone | 6–10 min | Priorities & opportunities, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | bmw.com, target.com, pfizer.com |
| `[Business function]` | Supply Chain |
| `[Persona]` | VP Supply Chain Planning |
| `[What I sell]` | supply-chain planning software |
| `[Proof point (optional)]` | cut planning cycle time at Fabrikam Foods |
| `[Co-sell partner (optional)]` | Tailspin Partners |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my ABM copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [websites, 5 per pass, e.g. bmw.com, target.com, pfizer.com]
- Business function: [e.g. Supply Chain]
- Persona: [e.g. VP Supply Chain Planning]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut planning cycle time at Fabrikam Foods]
- Co-sell partner (optional): [e.g. Tailspin Partners]

STEPS
1. Take the first 5 accounts. Find each by website and confirm the parent, not a subsidiary or brand. List any you can't resolve and carry on.
2. For each, pull its [Business function] priorities and keep the best fit for [What I sell], newest quarter first, with source and quarter.
3. For each, pull news from the last 60 days and keep one item showing money or change: deal or partnership, new site, leadership move, acquisition, funding or layoff. Prefer one linked to the priority.
4. Write 2 sentences: the signal and its date; then the link to the priority and a problem [What I sell] solves, ending in a soft question. Use [Proof point] in at most two messages. With [Co-sell partner], write a joint note.

OUTPUT
- Bottom line: 2 sentences — how many accounts have a strong hook and which to send first.
- Table: Account | Priority (quarter, source) | Signal (date, source) | Message | Strength. Strong first. Strong = signal links to priority; OK = both, unlinked; Weak = priority only.
- "Skipped": accounts not found or with no [Business function] priority.
- Recommended next step: who to send first, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- 45 words or fewer per message. No flattery or claims about the reader's own work.
- Also skip product launches, supplier press releases naming the account, and single-store property sales.
- No qualifying signal: write from the priority alone, mark Weak. Never invent or re-date a signal.
- Quote priorities in Draup's words. After 5 accounts, offer the next 5.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Tools and providers are linked to a priority by workload, not confirmed on it. Say "linked", never "used for". Quarter labels follow the company's fiscal year and can run ahead of the calendar.
- Drop news noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Merge items about the same event and keep the earliest. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
For the first 5 of [Accounts], write a 2-sentence opener to a [Persona] tied to one [Business function] priority and one Draup signal from the last 60 days. Table with sources and dates, Strong first; then offer the next 5.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Do the next 5 accounts on my list.
```

```text
Rewrite each Strong message as a LinkedIn connection request under 300 characters.
```

```text
For the Strong rows, find the most likely [Persona] at each account and show name and title (professional information only).
```

```text
Write a 3-touch follow-up for the Strong rows: email on day 3, LinkedIn on day 6, a short close-the-loop email on day 10.
```

## Tips for better results

- Narrow to one business function. Priorities across every function bury the one that matters to your buyer.
- Weak rows aren't wasted: they often point to accounts that need a call or a different angle rather than an email.

## Related prompts

- [Signal-to-email (one or a few accounts)](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 5 per pass: the freshest relevant signal, the priority it supports, and a short, sourced opener for your persona that ends in one low-friction ask.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): Up to 5 real triggers from the last 90 days, each tied to a stated priority, a likely owner and a suggested action, with the noise stripped out.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Pick a co-sell partner](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account and experienced with your technology, with the one to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_key_account_priorities`, `get_top_signals`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `content-abm-messages`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
