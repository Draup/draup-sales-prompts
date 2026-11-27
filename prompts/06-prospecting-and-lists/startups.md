[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Startups with real momentum

> **The startups in a vertical that Draup scores for momentum, with what they do, funding, hiring and who to contact.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell to high-growth companies, or want early-stage logos before competitors find them. | SDR / BDR, Account Executive, Partnerships & Alliances | Everyone | 4–6 min | Industry ecosystem, Company & financials |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[City (optional)]` | London |
| `[What I sell]` | cloud cost-management software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my startup prospecting analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Insurance]
- City (optional): [e.g. London]
- What I sell: [one line, e.g. cloud cost-management software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical and, if given, the city to Draup's metro name (e.g. "Greater London Area, United Kingdom"); show both.
2. Pull Draup's top startups for the vertical (fixed top 50), limited to that metro if given. Show only startups with a momentum score, highest first.
3. Look up the top 10 in one company list, keeping only the same Draup companies: what they do, HQ, workforce growth %, total funding, investors, postings (90 days).
4. For those 10, pull the last funding round (type, date, amount, lead investor).

OUTPUT
- Bottom line: 2 sentences — how many momentum startups there are and the best fit for [What I sell].
- One line: "X startups scored; top 10 shown".
- Table (highest momentum first): Rank | Startup | What they do | HQ | Workforce growth % | Total funding ($M) | Last round (type, date) | Lead investor | Postings (90 days) | Momentum score | Who to contact (title) | Flag.
- "Why they'd buy": one line each for the top 5, tied to funding, hiring or stage.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out units of large corporations; they aren't startups.
- "Who to contact" = likely title at a startup that size (often a founder or first functional lead).
- Stop at 10 and offer the next 10.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- Use primary vertical only, sort largest first, and flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- Show USD millions using Draup's conversion rate; if Draup gives none, name the rate and date and mark it as outside Draup.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
List the top 10 [Vertical] startups by Draup's momentum score, with what they do, HQ, total funding, last round, 90-day postings and who to contact. Add why each might buy [What I sell], then offer the next 10.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Continue with startups 11 to 20.
```

```text
Which of these raised money in the last 12 months? Show round, amount and date.
```

```text
Who are the founders or tech leaders at the top 3?
```

## Tips for better results

- Add a city to focus on your territory.
- A recent round plus rising job postings is often the best timing signal at a startup.

## Related prompts

- [Growing and shrinking companies: scale vs cost-out buyers](../../prompts/06-prospecting-and-lists/growth-and-cost-out.md): Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and who to call.
- [Private company funding](../../prompts/01-account-research/private-funding.md): How much a private company has raised, its last round and valuation, equity history, whether it is in growth mode, and who signs.
- [Build and size an ICP list](../../prompts/06-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_organization_top_startups`, `get_universe_companies_v3`, `accounts_private_financials_v3`

Status: **tested live**. Prompt id: `prospect-startups`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
