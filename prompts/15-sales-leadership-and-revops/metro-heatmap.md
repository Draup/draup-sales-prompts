[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which cities to base reps and events

> **A ranked map of the metros in one country where an industry's people, big local employers and the employers active in your workloads concentrate, telling you where to base reps, run events, or assign a named-account owner instead.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Deciding where to hire the next field rep, where to hold a roadshow or dinner series, or which city a new office should cover. Use "Which region gets the next rep" first if you're still choosing the country. | Sales Leader & RevOps, Marketing & ABM | Everyone | 4–6 min | Industry ecosystem, Company directory, Executives & movement, News signals, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[Country]` | United States of America |
| `[Metros to compare (optional)]` | Hartford, Dallas, Chicago |
| `[What I sell]` | claims-automation software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my field-sales and events strategist. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Country: [in full, e.g. United States of America]
- Metros to compare (optional): [up to 5, e.g. Hartford, Dallas, Chicago; default the top 5]
- What I sell: [one line, e.g. claims-automation software; skip if saved in setup]

STEPS
1. Use Draup's exact industry, country and metro names; map What I sell to its workloads. If the industry returns zeros, try its parent and name it.
2. Pull Draup's metro map for the industry (a fixed top 50 worldwide, ranked by a relative strength index); keep metros in [Country], plus mine.
3. For the top 5 metros (or up to 5 of mine), pull the industry's top local employers there (up to 50 each) with approximate local headcount.
4. For the same metros, list companies in the industry with a presence there, 1,000+ staff and activity in my workloads (names only, up to 50). That count is the relevance measure.
5. Per metro: local headcount of the top 50, employers with 1,000+ local staff (editable default), top-2 share, 3 biggest employers. Flag employers from another primary industry; don't let them drive the verdict.
6. Classify: Anchor cluster (top 2 hold over 50%; say whether they are HQs or plants), Broad territory (8+ employers with 1,000+ local staff), Mixed. A metro whose anchors are plants of companies run from elsewhere is a site-visit city, not a rep base.
7. For the lead metro's biggest relevant employer, pull its top 3 executives in the function closest to What I sell and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — where to base people and what it means for [What I sell].
- Recommended next step: the decision, its owner and a date; then the first account, with a named person (step 7) and one dated fact. If none, say so.
- "Heatmap": Metro | Local headcount (approx.) | Employers 1,000+ / in my workloads | Type | 3 biggest employers. By relevance, then strength.
- "Where to put people and events": up to 3 rep bases (5 accounts each) and 2 event cities (6 accounts to invite).
- Detail: named-account metros with the 2 accounts that justify a named owner; flagged employers; strength index.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- The strength index is relative; never call it headcount. Write "approx." beside every local headcount.
- These are people, not budget holders: where the HQ is elsewhere, say where decisions are likely made.
- "Who to invite" means the account, not a named person.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Every count and total applies all my conditions.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Parent companies only; merge subsidiaries and alternate names of one company.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: rank the top 5 metros in [Country] for [Vertical], with big local employers, employers active in my workloads and whether each is a broad territory or a few HQ accounts, for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [Metro], which of these employers run a capability centre or HQ there?
```

```text
Add two more metros: [Metro], [Metro].
```

```text
Who leads [Business function] at the 5 accounts in my top rep-base metro?
```

```text
Turn the events section into a 3-city roadshow plan with invite lists.
```

## Tips for better results

- A metro full of 1,000–3,000-person regional sites often makes a better volume territory than one with two giant headquarters.
- Run it for two industries you sell into and overlay the results to find cities that serve both.
- Check where the HQ sits before you staff for a big local employer; the buyer may be in another city.

## Related prompts

- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.
- [Find the biggest logos in your city](../../prompts/06-prospecting-and-lists/territory-logos.md): The largest employers in a vertical in one metro, by Draup-estimated local headcount, with global capability centres (GCCs) called out and a named person to call first.
- [Which region gets the next rep](../../prompts/15-sales-leadership-and-revops/territory-potential.md): A ranked comparison of 2–5 countries for one industry, or 2–4 industries in one country: how many sizeable accounts each holds, how many are active in the work you sell, where your rivals are really in use, and the revenue at stake, with where to add the next rep and the first account to open.
- [Carve balanced territories by geography](../../prompts/11-account-planning/territories.md): An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_vertical_map_data_it`, `get_ecosystem_employers_data`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `leaders-metro-heatmap`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
