[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Weekly trigger sweep for my book

> **One table of the week's real triggers across up to 10 accounts, each with a so-what and an action, plus a clean list of accounts with nothing new.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Monday morning, or before a pipeline review. | Account Executive, Account & Customer Success Manager, SDR / BDR | Everyone | 4–6 min | News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | walmart.com, target.com, bmw.com, pfizer.com |
| `[What I sell]` | supply-chain planning software |
| `[Window]` | last 7 days |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my weekly account-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [up to 10 websites, e.g. walmart.com, target.com, bmw.com — or "my saved list"]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Window: [default last 7 days; up to 30 days]

STEPS
1. Reuse the Draup names saved in my setup. Resolve others by website (exact match, parent company); ask only if none or several match. If I gave more than 10, do the first 10 and offer to continue.
2. Pull news for all accounts in one go for the window: executive moves, M&A, layoffs, partnerships and vendor deals, expansion, funding and investment.
3. For accounts with nothing, check their top-ranked signals and keep only items dated inside the window.
4. Apply the noise rule; also drop court dockets, stock-analysis pieces and store-property sales tagged as M&A.
5. Label subsidiary news with the subsidiary and parent (e.g. "[Subsidiary] ([Account])"). Merge repeat coverage.
6. Write one "so what" per item for [What I sell] and tag it Act now (this week), Plan (next touch) or Watch.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Top 3 this week": one line each.
- Table (Act now first, then newest): Account | Date | Trigger (with any number) | Type | Source and headline | So what | Likely owner | Action.
- "No material signals": accounts with nothing that survived.
- "Not resolved": accounts I need to fix.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Every item needs a date inside the window; drop anything you can't date.
- Don't pull leadership-move histories for every account; if I ask about one, narrow to the workloads I name.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
For [Accounts] (up to 10), list executive changes, M&A, layoffs, partnerships, expansion and funding news from [Window], newest first, with source, a one-line so-what for [What I sell] and an action. List accounts with nothing material.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a short email for each Act now item.
```

```text
For [Account], show leadership moves in [workload] in the last 30 days.
```

```text
Run the same sweep for the last 30 days and compare it with this week.
```

## Tips for better results

- Save your account list in a Claude Project or the start-here prompt so you can rerun this every Monday with one line.
- "No material signals" is useful: those accounts need a priority-led touch instead.

## Related prompts

- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of everything material that changed at an account since a date you choose, ranked by impact on your deal.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with the accounts worth touching.
- [Signal-to-email (one or a few accounts)](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 5 per pass: the freshest relevant signal, the priority it supports, and a short, sourced opener for your persona that ends in one low-friction ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `signals-weekly-book-sweep`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
