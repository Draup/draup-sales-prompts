[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Weekly trigger sweep for my book

> **One phone-sized table of the week's real triggers across up to 10 accounts, including any CEO or leadership change that takes effect in the window, plus the nearest item just outside the window for every quiet account.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Monday morning, or before a pipeline review. Use this for your whole book; use "What's worth acting on now" to go deep on one account. | Account Executive, Account & Customer Success Manager, SDR / BDR | Everyone | 4–6 min | News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | walmart.com, target.com, bmw.com, pfizer.com |
| `[What I sell]` | supply-chain planning software |
| `[Window (optional)]` | last 7 days (default; up to 30) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my weekly account-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [up to 10 websites, e.g. walmart.com, target.com, bmw.com — or "my saved list"]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Window (optional): [default last 7 days; up to 30 days]

STEPS
1. Reuse the Draup names saved in my setup. Resolve others by website (exact match, parent company); ask only if none or several match. If I gave more than 10, do the first 10 and offer to continue.
2. Pull news for all accounts in one feed pull for the window: executive moves (CEO and other C-level changes first), M&A, layoffs, partnerships and vendor deals, expansion, funding and investment, plus incidents or regulatory items that bear on what I sell. If one account fills more than half the results, pull the other accounts separately.
3. Apply the noise rule; also drop court dockets, stock-analysis pieces and store-property sales tagged as M&A.
4. After step 3, for every account with nothing left, check its top-ranked signals and keep items whose event or effective date falls inside the window, even if the story was captured before or after it (e.g. a new CEO who takes over on a date inside the window).
5. Leadership check: before calling any account quiet, confirm steps 2–4 found no CEO or other C-level change announced or effective in the window.
6. Label subsidiary news "[Subsidiary] ([Account])". Merge repeat coverage and count sources.
7. Write one "so what" per item for [What I sell] and tag it Act now (this week), Plan (next touch) or Watch.
8. For the top Act-now account, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (Act now first, then newest; up to 10): Account | Date | Trigger (with any number) | So what | Action.
- "Just outside the window": for each quiet account, the nearest material item (date, one line), or "nothing in 90 days".
- "No material signals" and "Not resolved": account names only.
- Detail: source and headline, type, source count and likely owner per item; "Dropped" count by reason; Gaps (what Draup lacked, to ask in discovery).

RULES
- Every item needs an event or effective date inside the window; drop anything you can't date.
- Don't pull leadership-move histories for every account; if I ask about one, narrow to the workloads I name.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and old stories re-dated as new (use the event date). Outages, incidents, breaches and regulatory inquiries are triggers if I sell security, reliability, observability, IT operations or compliance; keep any item that bears directly on What I sell, even if normally noise. Give source and headline for every item, plus the link when Draup has one.
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named person, dated why-now). For [Accounts], list [Window]'s real triggers, including leadership changes effective in the window, each with a so-what for [What I sell]; give quiet accounts their nearest item outside it.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a short email for each Act now item, with a fact check on each.
```

```text
For [Account], show leadership moves in [workload] in the last 30 days.
```

```text
Run the same sweep for the last 14 days and compare it with this week.
```

```text
Turn the "Just outside the window" items into priority-led touches for the quiet accounts.
```

## Tips for better results

- Save your account list in a Claude Project or the start-here prompt so you can rerun this every Monday with one line.
- Use a 14-day window after a holiday week; the "Just outside the window" line still shows what you'd otherwise miss.
- One big name can flood a shared news pull; the prompt re-pulls the quiet accounts so they aren't missed.

## Related prompts

- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of what changed at an account since a date you choose, ranked by impact on your deal, with competitor tools rated and a clear call: reopen, wait or watch for a lost deal; defend, expand or monitor for a customer.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_news_feed_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `signals-weekly-book-sweep`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
