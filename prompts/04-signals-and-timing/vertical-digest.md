# Weekly industry signal digest

**A one-screen digest of the week's material moves in one industry, grouped by theme, with the accounts worth touching.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A weekly routine for vertical sellers and marketers, or before an industry call or event. | Marketing & ABM, Account Executive, Sales Leader & RevOps, SDR / BDR | Everyone | 4–6 min | News signals, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[Country]` | United Kingdom (optional) |
| `[What I sell]` | claims automation software |
| `[Window]` | last 7 days |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my industry news editor. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance, Life Sciences]
- Country: [optional, in full, e.g. United Kingdom]
- What I sell: [one line, e.g. claims automation software — skip if you ran the start-here prompt]
- Window: [default last 7 days; up to 30 days]

STEPS
1. Use Draup's exact industry and country names. If the industry returns nothing, try its parent and name it.
2. Pull the most-covered industry news in the window: M&A, executive moves, partnerships, expansion, layoffs, funding. Review at least 30 items.
3. Check each company really belongs to the industry; tags can leak to similar names or unrelated events.
4. Apply the noise rule; also drop board-nominee filings and minor marketing deals. The named company must be the actor, and if I gave a country, the event must happen there.
5. Keep regional-unit news (e.g. a country CEO change at a global insurer) but name the unit.
6. Rank by relevance to [What I sell], then company size; keep the top 10. For the top 3 companies, attach one fitting stated priority with fiscal quarter.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "This week in [Vertical]": 3 bullets.
- Table (up to 10): Date | Company (unit) | Type | What happened (with any number) | Region | Source and headline | Why it matters for [What I sell].
- "Themes": 2–3 patterns, citing the rows behind each.
- "Accounts to touch": 3–5, each with reason, linked priority and likely owner.
- "Dropped": count by reason.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Keep amounts in the reported currency; convert to USD in brackets only if I ask, using Draup's rate.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 320 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Give me this week's [Vertical] digest: the 10 most material M&A, leadership, partnership, expansion, layoff and funding moves, with date, company, source and why each matters for [What I sell]. Group by theme and name 3–5 accounts to touch.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this digest into a 150-word LinkedIn post for our industry page. Check your Draup licence before publishing Draup data externally.
```

```text
For the accounts to touch, write a 2-sentence opener each.
```

```text
Run the same digest for the last 30 days and show which themes are growing.
```

## Tips for better results

- Industry tags can catch companies with similar names. The "Dropped" count shows how much Claude filtered out.
- Run it every Monday with the same inputs so you can compare themes week to week.

## Related prompts

- [Weekly trigger sweep for my book](../../prompts/04-signals-and-timing/weekly-book-sweep.md): One table of the week's real triggers across up to 10 accounts, each with a so-what and an action, plus a clean list of accounts with nothing new.
- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated table of the companies in your industry and country that just did one thing you choose: M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships.
- [One-page vertical market snapshot](../../prompts/07-vertical-intelligence/vertical-snapshot.md): A one-page view of an industry: revenue and spend, top priorities with likely owners, technologies gaining ground, and who outsources what to whom.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_news_feed_v3`, `get_account_details_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `signals-vertical-digest`.

</details>

[Back to Signals and timing](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
