[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who in my market just [did X]?

> **A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a themed list, prepping an industry call, or finding companies that just changed. | SDR / BDR, Marketing & ABM, Account Executive, Services, SI & Staffing Seller | Everyone | 4–6 min | News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Event type]` | expansion or new centres |
| `[Vertical]` | Banking & Financial Services |
| `[Country]` | India |
| `[What I sell]` | cloud migration services |
| `[Window (optional)]` | 6 months (default 90 days) |
| `[Theme (optional)]` | cloud migration (partnerships only) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market-news researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Event type: [one of M&A; layoffs; leadership change; expansion or new centres; funding; partnership — e.g. expansion or new centres]
- Vertical: [industry, e.g. Banking & Financial Services]
- Country: [in full, e.g. India; blank uses my saved territory]
- What I sell: [one line, e.g. cloud migration services — skip if you ran the start-here prompt]
- Window (optional): [default 90 days; up to 12 months]
- Theme (optional): [for partnerships, e.g. cloud migration]

STEPS
1. Use Draup's exact industry and country names; say which you used.
2. Search Draup news first with "Which [Vertical] companies in [Country] [Event type] in the last [Window]?" (main source; up to 20 results, often without links). Then page the news feed for the same filters to add links and catch misses. Review at least 30 items in total.
3. Apply the noise rule. Keep only items where the named company is the actor, the event happened in [Country], and the company really is in [Vertical].
4. By type: M&A: Acquisition, Merger or Divestiture, and Announced or Completed. Layoffs: store and branch closures listed separately; headcount only if stated. Leadership: C-level and VP, at the new employer. Expansion: add Type (capability centre, tech centre, office); leave out factories, stores, branches and wealth centres. Funding: no donations or grants. Partnerships: no sponsorships or marketing tie-ins.
5. Merge repeat coverage (earliest date, source count) and merge subsidiaries into their parents.
6. For the most relevant company, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- Table (top 10, newest first): Date | Company | What happened (with any number) | Sources (count).
- "Pattern": 3 bullets, and why it matters for [What I sell]; name the 3 companies to approach first.
- Detail: rows 11–20; source and headline (link if available) and type for every row; "Excluded" count by reason; Gaps (to ask in discovery).

RULES
- Search results come back by relevance, not date; sort by date yourself.
- One event type per run.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and re-dated old stories (use the event date). Outages, incidents, breaches and regulatory inquiries count for security, reliability, IT operations or compliance sellers; keep any item that bears directly on What I sell. Give source, headline and link (if any) per item.
- If sources conflict on a name, date or number, say so and repeat neither as fact; single-source figures are unverified.
- Hiring, new-technology and news data cover the last 12 months; if my window is longer, say what was covered.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named person, a dated why-now). Which [Vertical] companies in [Country] did [Event type] in the last [Window]? Top 10: date, company, what happened and how many sources report it.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 5 companies, pull a one-line profile: workforce, revenue and HQ.
```

```text
Run the same event type for [another country].
```

```text
Write a 2-sentence opener for each of the top 5, using only items with 2+ sources.
```

```text
Which of these companies already run my competitors' products?
```

## Tips for better results

- The news search finds more but often without links; the feed adds links. The assistant uses both and gives source and headline either way.
- Phrase the theme the way a press release would ("core banking", "cloud migration").
- A single-source item is worth a look but not a quote; the Sources column shows which ones to double-check.

## Related prompts

- [Who just picked a vendor](../../prompts/04-signals-and-timing/vendor-selection-news.md): A dated list of companies in your industry that just selected, deployed or replaced a vendor in your category: competitor wins to watch, peer proof, and the implementation partners involved, with a named person at the best account.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.
- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_news_filters_v3`, `get_signal_news_v3`, `get_news_feed_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `signals-news-question-templates`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
