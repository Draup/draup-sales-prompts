# Signal-to-email (one or a few accounts)

**For one account or up to 5 per pass: the freshest relevant signal, the priority it supports, and a short, sourced opener for your persona that ends in one low-friction ask.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Writing first-touch emails or a small ABM wave, and you want every message anchored on something real and recent. | SDR / BDR, Account Executive, Marketing & ABM | Everyone | 4–6 min | News signals, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | bmw.com, target.com |
| `[What I sell]` | supply-chain planning software |
| `[Persona]` | VP Supply Chain |
| `[Contact name]` | Jane Doe (optional) |
| `[Proof point]` | cut forecast error for Contoso Retail (optional) |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my outbound copywriter and researcher. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [one website, or up to 5, e.g. bmw.com, target.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Persona: [who reads it, e.g. VP Supply Chain]
- Contact name: [optional, e.g. Jane Doe]
- Proof point: [optional result you may quote, e.g. cut forecast error for Contoso Retail]

STEPS
1. Find each account by website (exact match, parent company). Ask me if none or several match. If I gave more than 5, do the first 5 and offer to continue.
2. Pull news for all the accounts in one go for the last 60 days: deals and partnerships, expansion, executive moves, M&A, funding or investment plans. Skip launches. Apply the noise rule; the account must be the actor.
3. Per account, pick the one signal most relevant to [What I sell] and the persona.
4. Pick the stated priority in the persona's function that best fits it, with source and fiscal quarter (fiscal labels can run ahead of the calendar, so keep the quarter out of the email).
5. Write the message.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- One account: Signal (date, source, headline) | Priority (source, quarter) | Subject (7 words max) | Opener: 3 sentences, 70 words max: the signal, the priority posed as a question, one low-friction ask (e.g. "worth a 15-minute compare?"). Use the contact's name and proof point only if given.
- Several accounts: Account | Signal (date) | Priority (quarter) | Message (2 sentences, 45 words max, ending in the ask) | Source and headline.
- No qualifying signal: say so and write a priority-only opener.
- "Not found": accounts I need to fix.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Quote numbers exactly as the source states them.
- Pose the signal–priority link as a question, never a claim.
- No flattery, no "I noticed", no hype words, no exclamation marks.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
For each of [Accounts] (up to 5), find one deals, expansion, executive or M&A signal from the last 60 days, pair it with a stated priority, and write a short [Persona] opener ending in one easy ask. Cite sources.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a second-touch email for each account using a different priority.
```

```text
Rewrite the openers for a CIO instead of [Persona].
```

```text
Run the next 5 accounts in the same way.
```

## Tips for better results

- Give Claude a real proof point you're allowed to quote. A specific, permitted result often beats a generic value statement.
- If most accounts come back with no qualifying signal, widen the window to 90 days in a follow-up.

## Related prompts

- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): Up to 5 real triggers from the last 90 days, each tied to a stated priority, a likely owner and a suggested action, with the noise stripped out.
- [ABM messages for a target list](../../prompts/09-content-and-enablement/abm-messages.md): A table of short, personalised openers, 5 accounts per pass, each tied to one stated priority and one dated signal from the last 60 days, with sources and an optional partner or proof angle.
- [Industry email sequence](../../prompts/09-content-and-enablement/email-sequence.md): A ready-to-load 3-email sequence for one persona in one industry, each email built on a current industry priority and a dated real-company example.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `signals-signal-to-email`.

</details>

[Back to Signals and timing](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
