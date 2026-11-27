[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Signal-led emails for up to 10 accounts

> **For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Use this when you have one to 10 named accounts and want each email anchored on that account's own recent event. Use "ABM openers for 10 accounts at once" instead for a longer campaign list, a fixed theme or a joint partner note. | SDR / BDR, Account Executive, Marketing & ABM | Everyone | 4–6 min | News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | bmw.com, target.com |
| `[What I sell]` | supply-chain planning software |
| `[Persona]` | VP Supply Chain |
| `[Territory (optional)]` | North America |
| `[Contact name (optional)]` | Jane Doe |
| `[Proof point (optional)]` | cut forecast error for Contoso Retail |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter and researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [one website, or up to 10, e.g. bmw.com, target.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Persona: [reader, e.g. VP Supply Chain]
- Territory (optional): [region I cover, e.g. North America]
- Contact name (optional): [e.g. Jane Doe]
- Proof point (optional): [e.g. cut forecast error for Contoso Retail]

STEPS
1. Find each account by website (parent company). If one doesn't resolve, retry once by name and show the match and score; ask if several match. Never drop an account silently. Up to 10 per pass: after each 5, show the table and continue unless I say stop.
2. Pull 60 days of news for all accounts in one feed pull: deals, expansion, executive moves, M&A, investment plans, and incidents that bear on what I sell. If one account fills over half the results, pull the quiet ones separately. The account must be the actor.
3. Per account, pick the signal most relevant to [What I sell] and the persona, preferring events in my territory (say if none).
4. Fact-check it and pick the persona's best-fit stated priority (source, fiscal quarter).
5. For one account, or a list's strongest row, pull the top 3 executives in the persona's function and name the best match.
6. Write in [Persona]'s language and goals.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- "Check before sending": each message leaning on a single-source or conflicting fact or a "verify" profile, and what to check (or "none").
- One account: signal (date, source, fact check), priority, Subject (7 words max) and opener (70 words max): the signal, the priority as a question, one easy ask. Contact name and proof point only if given.
- Several accounts: Account | Signal (date; in territory?) | Fact check | Message (2 sentences, 45 words max, ending in the ask).
- Detail: source and headline per account; priority used; priority-only openers where no signal qualified; "Not found" accounts; Gaps (to ask in discovery).

RULES
- Quote only Confirmed numbers, exactly as the source states them. Keep fiscal quarters out of the copy.
- Pose the signal–priority link as a question; no flattery, "I noticed", hype or exclamation marks.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and re-dated old stories (use the event date). Outages, incidents, breaches and regulatory inquiries count for security, reliability, IT operations or compliance sellers; keep any item that bears directly on What I sell. Give source, headline and link (if any) per item.
- Fact check before copy: tag each fact Confirmed (company announcement, filing or 2+ sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an account sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first. For each of [Accounts] (up to 10), pick the 60-day signal most relevant to [What I sell] and my [Territory], fact-check it, and write a 45-word [Persona] opener ending in one ask.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a second-touch email for each account using a different priority.
```

```text
Rewrite the openers for a CIO instead of [Persona].
```

```text
Run the next 10 accounts in the same way.
```

```text
For the rows marked Single source, find a second source or swap in another signal.
```

## Tips for better results

- Give the assistant a real proof point you're allowed to quote. A specific, permitted result often beats a generic value statement.
- Add your territory once in the start-here prompt; signals in your region rank first and the table says when an account has none.
- If most accounts come back with no qualifying signal, widen the window to 90 days in a follow-up.

## Related prompts

- [ABM openers for 10 accounts at once](../../prompts/16-content-and-enablement/abm-messages.md): A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- [3-email sequence for one industry persona](../../prompts/16-content-and-enablement/email-sequence.md): A ready-to-load 3-email sequence for one persona in one industry, each email built on a priority in the persona's function and a dated move by a real company, plus the first account to load with a named contact.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `signals-signal-to-email`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
