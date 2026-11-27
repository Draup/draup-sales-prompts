[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What changed between two earnings calls

> **Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, who owns them, and a 2-line talk track for your next QBR.**

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
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to name who owns the New themes.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: both calls with dates, the company's own period names and Draup's quarter labels.
- "Theme shifts": Theme | Status (New, Stronger, Weaker, Dropped, Continued) | Quote from the latest call (25 words or fewer, speaker) | Likely owner. Up to 8, New first.
- "What this means for [What I sell]": 3 implications, each tied to a row.
- "QBR talk track": 2 lines: "Last quarter you emphasised X; now you're talking about Y. Here's how we help with Y."
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: for each theme, one line on how it was framed in the previous call.

RULES
- Quote executives only, word for word.
- Call a theme Dropped only if it got real airtime before and none now.
- Read for themes; reproduce nothing beyond the quotes.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Label anything you infer (buyer role, intent, fit) as "likely".
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Company]'s two latest earnings calls: bottom line and who to raise it with, then themes marked New, Stronger, Weaker, Dropped or Continued, each with a short quote, and a 2-line QBR talk track.
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

- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.
- [Numbers from the latest earnings call](../../prompts/01-account-research/numbers-from-the-call.md): The three numbers from the latest earnings call that matter for your deal, the question each opens and who to raise them with, plus every stated number in a reference table.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_transcripts`, `account_transcripts_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-call-over-call`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
