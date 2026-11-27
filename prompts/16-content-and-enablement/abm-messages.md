[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# ABM openers for 10 accounts at once

> **A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're launching an ABM play, an SDR sprint or a joint campaign on a named list of 10–30 accounts. Use this for lists; use the signal-to-email prompt instead when you want one or a few carefully timed emails with a subject line and the full signal story. | Marketing & ABM, SDR / BDR, Account Executive, Partnerships & Alliances | Everyone | 6–10 min | Priorities & opportunities, News signals, Executives & movement, Company directory |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | pepsico.com, medtronic.com, 3m.com, fedex.com, starbucks.com |
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
- Accounts: [websites, up to 10 per pass, e.g. pepsico.com, medtronic.com, 3m.com, fedex.com]
- Business function: [e.g. Supply Chain]
- Persona: [the title you're writing to, e.g. VP Supply Chain Planning]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut planning cycle time at Fabrikam Foods]
- Co-sell partner (optional): [e.g. Tailspin Partners]

CONTEXT (optional)
Write in the persona's words: a CFO hears cost and risk; a planning VP hears forecast accuracy, service levels and inventory. One dated, relevant signal beats three generic ones.

STEPS
1. Take the first 10 accounts. Resolve them by website in one company lookup and confirm each is the parent, not a subsidiary or brand. List any you can't resolve and carry on.
2. For each, pull its top 3 [Business function] priorities, newest quarter first, with source and quarter. Keep the best fit for [What I sell].
3. Pull one news feed for all 10, last 60 days, money-or-change categories only (deals, new sites, leadership moves, acquisitions, investments, layoffs). If one account fills over a third of items, pull again without it. For accounts with nothing, check their top-ranked signals inside the 60 days.
4. Keep one item per account where the account is the actor, preferring one linked to the priority. Customer orders placed with the account count only as context.
5. Write 2 sentences to [Persona], in their language: the signal and its date; then the link to the priority and the problem [What I sell] solves for that persona, ending in a soft question. Use [Proof point] in at most two messages. With [Co-sell partner], add ONE joint note for the strongest row.
6. For the first account to send, pull its top 3 executives in [Business function] and pick the closest match to [Persona].

OUTPUT
- Bottom line: 2 sentences — how many accounts have a strong hook and which to send first.
- Recommended next step: who to send first (name and title from step 6), and the dated signal. If none is found, say so.
- Table: Account | Signal (date) | Priority (quarter) | Message | Strength. Strong first. Strong = signal links to priority; OK = both, unlinked; Weak = priority only.
- Detail: sources for each row; the joint partner note; "Skipped" (not found or no [Business function] priority).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- 45 words or fewer per message. No flattery or claims about the reader's own work.
- No qualifying signal: write from the priority alone, mark Weak. Never invent or re-date a signal.
- Quote priorities in Draup's words. After 10 accounts, show the table and continue with the next 10 unless I say stop.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: for up to 10 of [Accounts], a 2-sentence opener to a [Persona], in their words, tied to one [Business function] priority and one 60-day signal. Strong first (signal ties to the priority).
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Do the next 10 accounts on my list.
```

```text
Rewrite each Strong message as a LinkedIn connection request under 300 characters.
```

```text
Rewrite the Strong rows for a CFO persona instead.
```

```text
Write a 3-touch follow-up for the Strong rows: email on day 3, LinkedIn on day 6, a short close-the-loop email on day 10.
```

## Tips for better results

- Narrow to one business function. Priorities across every function bury the one that matters to your persona.
- Weak rows aren't wasted: they often point to accounts that need a call or a different angle rather than an email.
- Change the persona and rerun: the same signal reads very differently to a CFO and a planning lead.

## Related prompts

- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_universe_companies_v3`, `get_account_priorities_v3`, `get_news_feed_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `content-abm-messages`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
