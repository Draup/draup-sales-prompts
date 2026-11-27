[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Their leaders' own words on [Topic]

> **Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want to open with the customer's own words rather than your claims. Use "Numbers from the latest earnings call" instead when you need figures for a business case. | Account Executive, Presales & Solutions, Marketing & ABM, Account & Customer Success Manager | Everyone | 2–4 min | Earnings calls & filings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Topic]` | AI, supply chain, technology investment |
| `[What I sell]` | AI-driven demand forecasting software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Topic: [e.g. AI, supply chain, technology investment]
- What I sell: [one line, e.g. AI-driven demand forecasting software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. List the earnings-call transcripts, newest first, and open the most recent. Note each speaker's title from the introductions, and whether it is an analyst or a press call.
3. Find every passage where an executive talks about [Topic], preferring the CEO and CFO. If [Topic] isn't there, say so and repeat on the previous call.
4. Fallback: if there are no transcripts, or neither call mentions [Topic], pull the annual filings Draup holds for the last 5 years (US SEC filers only).
5. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to choose who to take the quotes to.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- Header: call date, the company's own name for the period with Draup's label in brackets, call type.
- "Quotes": # | Speaker and title | Verbatim quote (40 words or fewer) | What it signals. Up to 6, strongest first.
- "How to use this with [What I sell]": 2 bullets, each pairing a quote with a talking point.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail, fallback only: "Filings to read": Fiscal year | Type | Filed date | Link; then up to 4 sections to read (e.g. Risk Factors, Business), one line each on what to look for.

RULES
- Quote word for word; trim with an ellipsis, never paraphrase inside quotation marks. Executives only, not analysts.
- Don't summarise or quote a filing you haven't opened. Non-US companies usually have none; that's expected.
- Read only what you need; reproduce nothing beyond the quotes.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function. In banking and consulting VP and SVP are mid-level. If several share a title, list them. Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Quote [Company]'s leaders on [Topic] from the latest earnings call: bottom line and who to take it to first, then up to 6 verbatim quotes with speaker, title and fiscal quarter. No call? List filings to read.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Do the same for the previous call. Has the tone on [Topic] changed?
```

```text
Pull every number they stated in this call into a table.
```

```text
Write a 3-line email opener using the strongest quote.
```

## Tips for better results

- Quarters follow the company's fiscal year, which can run a year ahead of the calendar. The prompt shows both labels.
- For US-listed companies, the filing fallback points you to risk-factor language you can cite.

## Related prompts

- [Numbers from the latest earnings call](../../prompts/01-account-research/numbers-from-the-call.md): The three numbers from the latest earnings call that matter for your deal, the question each opens and who to raise them with, plus every stated number in a reference table.
- [What changed between two earnings calls](../../prompts/01-account-research/call-over-call.md): Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, who owns them, and a 2-line talk track for your next QBR.
- [Account SWOT, outside-in](../../prompts/01-account-research/swot.md): A SWOT of the account built only from dated Draup evidence, ending with where your offer fits and the named person to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_transcripts`, `account_transcripts_v3`, `accounts_get_account_annual_reports_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-proof-points`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
