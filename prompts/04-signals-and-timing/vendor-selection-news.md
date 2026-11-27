[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who just picked a vendor

> **A dated list of companies in your industry that just selected, deployed or replaced a vendor in your category: competitor wins to watch, peer proof, and the implementation partners involved.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Weekly or monthly competitive watch, or before a campaign in a new industry. | Account Executive, Marketing & ABM, Partnerships & Alliances, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Technology]` | supply-chain planning software |
| `[Vertical]` | Retail |
| `[Competitor]` | RELEX, Blue Yonder |
| `[My company]` | Northwind Data Services; Tailspin Partners (optional) |
| `[Window]` | 90 days |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Technology: [your category in plain words, e.g. demand forecasting software]
- Vertical: [Draup industry, e.g. Retail, Insurance]
- Competitor: [one or more rival vendors, e.g. RELEX, Blue Yonder]
- My company: [optional, our firm and partners, e.g. Northwind Data Services; Tailspin Partners — skip if you ran the start-here prompt]
- Window: [default 90 days; up to 12 months]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Turn my industry into Draup's exact name; say which you used.
2. Search Draup news for the window with 3 phrasings: "[Vertical] company selects or partners with a [Technology] vendor", "... deploys, goes live on or migrates to new [Technology]" and "... replaces its legacy [Technology] system", then one search per competitor. Add links from the news feed where you can. Review at least 30 items.
3. Keep only stories where a named buyer chose a named vendor: buyer, vendor, implementation partner, scope (sites, regions, modules), what it replaced, and stage (Selected, Implementing, Live, Expanded).
4. Drop vendor roundups, rankings, "editorial picks", product launches and single stores named as the buyer. Merge repeat coverage.
5. Look up the 10 most relevant buyers in one company-list lookup for HQ and workforce; mark the rest "not checked".

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table (newest first): Date | Buyer (HQ, workforce) | Vendor | Implementation partner | Scope / replaced | Stage | Source and headline.
- "Competitor wins": with later phases still open.
- "Peer proof": rows where [My company] or a partner won, or "none found".
- "Implementation partners seen": Partner | Wins | Vendors.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- A selection isn't a go-live; always show the stage.
- Search results come back by relevance, not date; sort by date yourself.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Drop noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Also drop bank branches, registrar notices, recruitment ads, surveys that only mention the company, supplier press releases and single-store property sales. Give the source and headline for every item, plus the link when Draup has one.
- Hiring, new-technology and news data cover the last 12 months; if my window is longer, say what was covered.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which [Vertical] companies selected, deployed or replaced a [Technology] vendor in the last [Window]? Table of date, buyer, vendor, implementation partner, scope, stage and source. Highlight [Competitor] wins and wins by [My company].
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

## Tips for better results

- Phrase your category the way a press release would ("demand forecasting", "replenishment", "core banking"). Search works on meaning, not exact words.
- Multi-year rollouts often start with one module. A competitor win today can still leave later modules open.

## Related prompts

- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated table of the companies in your industry and country that just did one thing you choose: M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships.
- [Displacement target list](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A sized, revenue-ranked list of companies in your industry and country whose stack includes a competitor's products, confirmed in the same pass, with likely-inactive and misfiled names set aside.
- [Peer deals for social proof](../../prompts/06-outsourcing-and-services/peer-deals.md): Recent outsourcing engagements at the prospect's peers in the workload you sell, plus ready-to-use proof lines.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_signal_news_v3`, `get_news_feed_v3`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `signals-vendor-selection-news`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
