[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Weekly industry signal digest

> **A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A weekly routine for vertical sellers and marketers, or before an industry call or event. | Marketing & ABM, Account Executive, Sales Leader & RevOps, SDR / BDR | Everyone | 4–6 min | News signals, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[What I sell]` | claims automation software |
| `[Country (optional)]` | United Kingdom |
| `[Window (optional)]` | last 7 days (default; up to 30) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my industry news editor. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [industry, e.g. Insurance, Life Sciences]
- What I sell: [one line, e.g. claims automation software — skip if you ran the start-here prompt]
- Country (optional): [in full, e.g. United Kingdom; blank uses my saved territory]
- Window (optional): [default last 7 days; up to 30 days]

STEPS
1. Use Draup's exact industry and country names. If the industry returns nothing, try its parent and name it.
2. Pull the most-covered industry news in the window: M&A, executive moves, partnerships, expansion, layoffs, funding, plus incidents or regulatory actions that bear on what I sell. Review at least 30 items.
3. Check each company really belongs to the industry; tags can leak to similar names or unrelated events.
4. Apply the noise rule; also drop board-nominee filings and minor marketing deals. The named company must be the actor, and if I gave a country, the event must happen there.
5. Keep regional-unit news (e.g. a country CEO change at a global insurer) but name the unit. Merge repeat coverage and count sources.
6. Rank parent companies by relevance to [What I sell], then size; keep the top 10. For the top 3 companies, attach one fitting stated priority with fiscal quarter.
7. For the best account to touch, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- Table (up to 10): Date | Company (unit) | What happened (with any number) | Why it matters for [What I sell] | Sources (count).
- "Accounts to touch": 3–5, each with reason, linked priority and likely owner.
- Detail: "Themes" (2–3 patterns citing the rows behind each); region, type and source and headline per row; "Dropped" count by reason; Gaps (to ask in discovery).

RULES
- Keep amounts in the reported currency; convert to USD in brackets only if I ask, using Draup's rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and re-dated old stories (use the event date). Outages, incidents, breaches and regulatory inquiries count for security, reliability, IT operations or compliance sellers; keep any item that bears directly on What I sell. Give source, headline and link (if any) per item.
- If sources conflict on a name, date or number, say so and repeat neither as fact; single-source figures are unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named person, a dated why-now). This week's [Vertical] digest: the 10 most material moves with date, source count and why each matters for [What I sell], plus 3–5 accounts to touch.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this digest into a 150-word LinkedIn post for our industry page, using only items with 2+ sources. Check your Draup licence before publishing Draup data externally.
```

```text
For the accounts to touch, write a 2-sentence opener each.
```

```text
Run the same digest for the last 30 days and show which themes are growing.
```

```text
Which of this week's companies run my competitors' products?
```

## Tips for better results

- Industry tags can catch companies with similar names. The "Dropped" count shows how much the assistant filtered out.
- Run it every Monday with the same inputs so you can compare themes week to week.

## Related prompts

- [Weekly trigger sweep for my book](../../prompts/04-signals-and-timing/weekly-book-sweep.md): One phone-sized table of the week's real triggers across up to 10 accounts, including any CEO or leadership change that takes effect in the window, plus the nearest item just outside the window for every quiet account.
- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_news_feed_v3`, `get_account_details_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `signals-vertical-digest`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
