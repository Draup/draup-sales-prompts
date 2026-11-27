[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What changed between two calls

> **Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, plus a 2-line talk track for your next QBR.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Advanced: quarterly, for strategic accounts. Before a strategic meeting, QBR or renewal, to show you know where their story is moving. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps | Everyone | 4–6 min | Earnings calls & filings, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | industrial AI platform services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. industrial AI platform services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first. Pick the two most recent analyst calls for consecutive quarters. If one is a press call or a quarter is missing, say so and use the nearest pair.
3. Open the latest call in full and list its 6–10 main themes (strategy, investment, cost, technology, markets, risks).
4. Open the previous call. If it fails to load or comes back truncated, compare against the priorities Draup sourced in the previous quarter instead, and say so.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Header: both calls with dates, the company's own period names and Draup's quarter labels.
- "Theme shifts": Theme | Previous call | Latest call | Status (New, Stronger, Weaker, Dropped, Continued) | Quote from the latest call (25 words or fewer, speaker) | Likely owner (title). Sort New first, then Stronger, Weaker, Dropped, Continued.
- "What this means for [What I sell]": 3 implications, each tied to a row.
- "QBR talk track": 2 lines: "Last quarter you emphasised X; now you're talking about Y. Here's how we help with Y."
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Quote executives only, word for word.
- Call a theme Dropped only if it got real airtime before and none now.
- Read for themes; reproduce nothing beyond the quotes.
- Quarters are fiscal and Draup's labels can run ahead of the company's wording; show both.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Label anything you infer (buyer role, intent, fit, integration work) as "likely".
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Company]'s two most recent earnings calls: themes marked New, Stronger, Weaker, Dropped or Continued, each with a short quote and fiscal quarter, then 3 implications for [What I sell] and a 2-line QBR talk track.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Go deeper on the top New theme: every quote about it from the latest call.
```

```text
Which executives own the New themes?
```

```text
Turn the implications into 3 talking points for my QBR.
```

## Tips for better results

- This reads two long transcripts, so it takes longer than most prompts. Run it once a quarter per key account.
- New and Stronger themes are often where fresh budget goes; test that in the meeting.

## Related prompts

- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim quotes from leadership on your topic, with speaker, fiscal quarter and call date, or the annual-filing sections to read when there's no call.
- [Numbers from the latest call](../../prompts/01-account-research/numbers-from-the-call.md): Every number management stated on the latest earnings call (guidance, targets, KPIs, investment plans) in one table, with the three that matter for your deal and the question each opens.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): Where the account's priorities cluster, how each fits what you sell, and the single priority to lead with, with its likely owner and linked vendors.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_transcripts`, `account_transcripts_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `research-call-over-call`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
