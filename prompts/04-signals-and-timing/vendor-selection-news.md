[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who just picked a vendor

> **A dated list of companies in your industry that just selected, deployed or replaced a vendor in your category: competitor wins to watch, peer proof, and the implementation partners involved, with a named person at the best account.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Weekly or monthly competitive watch, or before a campaign in a new industry. | Account Executive, Marketing & ABM, Partnerships & Alliances, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Technology]` | demand forecasting software |
| `[Vertical]` | Retail |
| `[Competitor]` | RELEX, Blue Yonder |
| `[What I sell]` | supply-chain planning software |
| `[My company (optional)]` | Northwind Data Services; Tailspin Partners |
| `[Window (optional)]` | 90 days (default) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Technology: [your category in plain words, e.g. demand forecasting software]
- Vertical: [industry, e.g. Retail, Insurance]
- Competitor: [one or more rival vendors, e.g. RELEX, Blue Yonder]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- My company (optional): [our firm and partners, e.g. Northwind Data Services; Tailspin Partners]
- Window (optional): [default 90 days; up to 12 months]
- Territory (optional): [buyer HQ country or region, e.g. United States of America; blank uses my saved territory]

STEPS
1. Turn my industry into Draup's exact name; say which you used.
2. Search Draup news for the window with 3 phrasings: "[Vertical] company selects or partners with a [Technology] vendor", "... deploys, goes live on or migrates to new [Technology]" and "... replaces its legacy [Technology] system", then one search per competitor. Add links from the news feed where you can. Review at least 30 items.
3. Keep only stories where a named buyer chose a named vendor: buyer, vendor, implementation partner, scope (sites, regions, modules), what it replaced, and stage (Selected, Implementing, Live, Expanded).
4. Drop vendor roundups, rankings, "editorial picks", product launches and single stores named as the buyer. Merge repeat coverage and count sources; a win reported only by the vendor's own release is single-source. Drop stories whose tagged buyer is a look-alike name (check the buyer's country in the text).
5. Look up the 10 most relevant buyers in one company-list lookup for HQ and workforce; merge subsidiaries into parents, rank buyers in [Territory] first, and mark the rest "not checked".
6. For the best buyer to approach, pull the top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- Table (top 10, newest first): Date | Buyer (HQ) | Vendor | Stage | Sources (count).
- "Competitor wins": with later phases still open.
- Detail: implementation partner, scope and what it replaced per row; "Peer proof" (rows where [My company] or a partner won, or "none found"); "Implementation partners seen" (Partner | Wins | Vendors); source and headline per row; Gaps (to ask in discovery).

RULES
- A selection isn't a go-live; always show the stage.
- Search results come back by relevance, not date; sort by date yourself.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News noise: drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alike names, sister companies, recruitment ads, supplier press releases, bank branches, registrar notices, single-store sales and re-dated old stories (use the event date). Outages, incidents, breaches and regulatory inquiries count for security, reliability, IT operations or compliance sellers; keep any item that bears directly on What I sell. Give source, headline and link (if any) per item.
- If sources conflict on a name, date or number, say so and repeat neither as fact; single-source figures are unverified.
- Hiring, new-technology and news data cover the last 12 months; if my window is longer, say what was covered.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named person, a dated why-now). Which [Vertical] companies, my territory first, selected, deployed or replaced a [Technology] vendor in [Window]? Top 10 with buyer, vendor, stage and source count; flag [Competitor] wins.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For each competitor win, which phases or regions are still open?
```

```text
Which implementation partner appears most often? Profile them as a co-sell target.
```

```text
Write a 3-sentence peer-proof email using our most recent win for 5 lookalike accounts.
```

```text
Check the stack at the top 3 competitor wins: is the product already showing as active?
```

## Tips for better results

- Phrase your category the way a press release would ("demand forecasting", "replenishment", "core banking"). Search works on meaning, not exact words.
- Multi-year rollouts often start with one module. A competitor win today can still leave later modules open.

## Related prompts

- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.
- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.
- [Peers' outsourcing deals for social proof](../../prompts/10-outsourcing-and-services/peer-deals.md): Recent outsourcing engagements at the prospect's peers in the work you sell, ready-to-use proof lines, and who to send them to and why now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_signal_news_v3`, `get_news_feed_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `signals-vendor-selection-news`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
