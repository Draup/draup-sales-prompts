[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which region should own this account

> **Which region and metros hold the revenue, people and decision makers for your function, which region should own the pursuit, and where to hold the first meeting.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning territory ownership for a global account, or deciding where to run the first meetings. | Account Executive, Account & Customer Success Manager, Sales Leader & RevOps, Services, SI & Staffing Seller | Everyone | 2–4 min | Company & financials, Industry ecosystem, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | unilever.com |
| `[Business function]` | IT |
| `[What I sell]` | data and analytics managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my territory planning analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. unilever.com]
- Business function: [e.g. IT]
- What I sell: [one line, e.g. data and analytics managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull revenue by region for the latest fiscal year: share and year-on-year change.
3. Pull key locations (up to 100 rows) and combine them into one row per metro.
4. Pull senior executives in [Business function], 10 per page, up to 3 pages, and count them by country and metro.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Revenue by region": Region | Share % | YoY | Fiscal year.
- "Top 8 metros": Metro | Country | Indicative headcount | 12-month postings | Top 3 functions | HQ or GCC (global capability centre: a company-owned offshore site). Sort by postings.
- "Where [Business function] leaders sit": Country or metro | # senior leaders | Most senior title.
- "Recommended owning region": 3 bullets weighing revenue, people and decision makers, separating where budget sits from where delivery happens.
- "Where to hold the first meeting": one metro and why.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Site headcount is approximate and varies between lookups: call it indicative and back it with postings. GCC tags can include plants; drop mainly-manufacturing sites.
- A "new" site can only be inferred from postings; say so. The HQ metro may be undercounted; don't conclude the HQ is small.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Use only the latest year's regional split.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level (if none appears, say so in Gaps).
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which region should own [Company] for [Business function]? Revenue by region, top 8 metros with postings and GCC flags, where senior [Business function] leaders sit, a recommended owning region and where to hold the first meeting.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
What is each GCC hiring for? Top functions and skills by metro.
```

```text
Name the top 5 leaders in the recommended region.
```

```text
Which service providers deliver from these metros?
```

## Tips for better results

- Budget is often decided at HQ but spent where the delivery centre is. The output separates the two.
- European executive profiles can be restricted, so Europe may look thinner on leaders than it is.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Global capability centres (GCCs) and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_financials_revenue_by_region_post_v3`, `accounts_location_insights_key_locations_map_v3`, `get_globalization_summary`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `research-buying-center`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
