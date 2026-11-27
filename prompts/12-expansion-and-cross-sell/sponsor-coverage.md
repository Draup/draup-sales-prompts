[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Check sponsor risk and relationship gaps

> **A risk read on your executive sponsor (tenure, new bosses, announced changes), a coverage grid of who you know versus who matters, likely successors and the 3 named relationships to build next.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a renewal or expansion, after a reorganisation, or when one sponsor carries the account. Use this for relationship coverage; use "Renewal risk check" (plan-risk-check) for the whole account's risk, including competitors. | Account & Customer Success Manager, Sales Leader & RevOps, Account Executive, Services, SI & Staffing Seller | Everyone | 4–6 min | Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | mastercard.com |
| `[Our sponsor]` | Jane Doe, SVP Data Platforms (or my saved account notes) |
| `[Who we know]` | Director Data Engineering; Head of IT Procurement (optional) |
| `[Business function]` | IT (optional) |
| `[What I sell]` | data platform services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account relationship strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. mastercard.com]
- Our sponsor: [name and title, e.g. Jane Doe, SVP Data Platforms — a title alone may match several people]
- Who we know (optional): [titles of other contacts, names optional]
- Business function (optional): [default is the one closest to What I sell, e.g. IT]
- What I sell: [one line, e.g. data platform services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Accounts are lost when one sponsor leaves or is overruled. Good coverage spans three levels in more than one unit; never guess at people's plans.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use [Business function], or the one closest to [What I sell]; say which.
3. Pull senior leaders in the function, 10 per page, up to 3 pages. If fewer than 15 come back, add the top 20 leaders across the company (2 pages) to cover the C-suite.
4. Match [Our sponsor] and [Who we know] to profiles by name and title; unmatched contacts are "not found in Draup".
5. Search Draup's news for executive appointments, departures, interim roles and reorganisations at [Company] in the last 6 months; mark the most important from the last 90 days.
6. Rate sponsor risk: High (new leader above them in 12 months, unit reorganised, or under 6 months in title), Medium (over 6 years in title, or their function lead is interim), Low otherwise. Editable defaults.
7. Build the coverage grid: three levels by unit or region, each Known or Gap.

OUTPUT
- Bottom line: 2 sentences — sponsor risk and the biggest coverage gap. Add: people checked, pages, contacts matched.
- Recommended next step: a named person (name, full title) to build a relationship with next, the action this week and the dated why-now; if none, say so.
- "Sponsor read": one line: title, months in title, risk (High, Medium, Low) and the dated signals behind it.
- Table "Coverage grid": Level | up to 4 units or regions, each cell Known (who) or Gap (most senior person there).
- Table "Build next" (3): Person (name, title) | Why (dated fact) | Intro path through someone we know.
- Detail: likely successors or backups (up to 3, months in title) and leadership changes (Date | Change | Source).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Sponsor risk is internal planning; never put it in customer-facing copy.
- Function tags can be loose (legal or scientific leaders under IT); drop clear mismatches and say how many.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Leadership data can lag about 3 months; give the latest move date seen.
- If European executives return none, say profiles there may be restricted.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Rate [Our sponsor]'s risk at [Company] (tenure, new leaders above, announced changes). Lead with the risk and the named person to build a relationship with next, then a coverage grid and likely successors.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a note from [Our sponsor] introducing us to [Gap leader].
```

```text
Prepare a 1-page executive-sponsor brief for our CEO to meet [Economic buyer].
```

```text
Run this again after the next earnings call and compare.
```

## Tips for better results

- Give your sponsor's name and title; several people often share a title.
- A brand-new CFO or CPO above your sponsor often triggers a vendor review within two quarters.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.
- [New budget holders outside our footprint](../../prompts/12-expansion-and-cross-sell/new-budget-holders.md): Senior leaders new in role (about 18 months or less) in the functions you don't yet sell to, plus announced leadership changes, each with the priority they likely own, a first-90-days angle and the one to contact first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`, `build_news_filters_v3`

Status: **tested live**. Prompt id: `expand-sponsor-coverage`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
