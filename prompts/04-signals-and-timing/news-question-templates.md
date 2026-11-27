[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who in my market just [did X]?

> **A clean, dated table of the companies in your industry and country that just did one thing you choose: M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Building a themed list, prepping an industry call, or finding companies that just changed. | SDR / BDR, Marketing & ABM, Account Executive, Services, SI & Staffing Seller | Everyone | 4–6 min | News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Event type]` | expansion or new centres |
| `[Vertical]` | Banking & Financial Services |
| `[Country]` | India |
| `[Window]` | 6 months |
| `[Theme]` | cloud migration (partnerships only, optional) |
| `[What I sell]` | cloud migration services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market-news researcher. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Event type: [one of M&A; layoffs; leadership change; expansion or new centres; funding; partnership — e.g. expansion or new centres]
- Vertical: [Draup industry, e.g. Banking & Financial Services]
- Country: [in full, e.g. India]
- Window: [up to 12 months, e.g. 6 months]
- Theme: [optional, for partnerships, e.g. cloud migration]
- What I sell: [one line, e.g. cloud migration services — skip if you ran the start-here prompt]

STEPS
1. Use Draup's exact industry and country names; say which you used.
2. Search Draup news first with "Which [Vertical] companies in [Country] [Event type] in the last [Window]?" (main source; up to 20 results, often without links). Then page the news feed for the same filters to add links and catch misses. Review at least 30 items in total.
3. Apply the noise rule. Keep only items where the named company is the actor (not a supplier, customer or owner), the event happened in [Country], and the company really is in [Vertical].
4. By type: M&A — Acquisition, Merger or Divestiture, and Announced or Completed. Layoffs — store and branch closures in a separate table; headcount only if stated. Leadership — C-level and VP, at the new employer. Expansion — add Type (GCC, tech centre, office); leave out factories, stores, dealerships, branches and wealth centres. Funding — no donations or grants. Partnerships — no sponsorships or marketing tie-ins.
5. Merge repeat coverage, keeping the earliest date.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table (up to 20, newest first): Date | Company | What happened (with any number) | Type | Source and headline (link if available).
- "Excluded": count by reason.
- "Pattern": 3 bullets, and why it matters for [What I sell].
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Search results come back by relevance, not date; sort by date yourself.
- One event type per run.
- In the next step, name the 3 companies to approach first.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Hiring, new-technology and news data cover the last 12 months; if my window is longer, say what was covered.
- Keep to about 380 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which [Vertical] companies in [Country] did [Event type: M&A / layoffs / leadership change / expansion or new centres / funding / partnership] in the last [Window]? Table: date, company, what happened, type, source and headline.
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
Write a 2-sentence opener for each of the top 5 based on the news.
```

## Tips for better results

- The news search finds more but often without links; the feed adds links. Claude uses both and gives source and headline either way.
- Phrase the theme the way a press release would ("core banking", "cloud migration").

## Related prompts

- [Who just picked a vendor](../../prompts/04-signals-and-timing/vendor-selection-news.md): A dated list of companies in your industry that just selected, deployed or replaced a vendor in your category: competitor wins to watch, peer proof, and the implementation partners involved.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with the accounts worth touching.
- [Global capability centres (GCCs) and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_news_filters_v3`, `get_signal_news_v3`, `get_news_feed_v3`

Status: **tested live**. Prompt id: `signals-news-question-templates`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
