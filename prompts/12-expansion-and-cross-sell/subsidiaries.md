[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Subsidiaries and acquisitions to expand into

> **A customer's acquired companies and subsidiaries, each checked for whether it still runs on its own (own hiring, size, people moving to the parent), ranked as expansion targets, with the named person to approach at the top one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| After a customer buys companies, or when the main account is saturated and you want the next logo inside the group. | Account & Customer Success Manager, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | Company & financials, Talent flow & locations, Hiring & job postings, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | medtronic.com |
| `[What I sell]` | ERP integration and managed services |
| `[Window]` | last 3 years (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-expansion analyst for corporate groups. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- What I sell: [one line, e.g. ERP integration and managed services — skip if you ran the start-here prompt]
- Window (optional): [default last 3 years]

CONTEXT (why this matters)
An integrating acquisition is bought for centrally by the parent; a standalone subsidiary has its own leaders and budget and sells like a new logo.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Pull acquisitions in [Window]: date, company, intent, size, and whether Draup holds it as a company.
3. Search Draup's M&A news for [Company], last 12 months, for deals the table misses and any divestments; mark the most important item from the last 90 days.
4. Pull talent flow by company (20 rows, largest movement first). Rows marked as its own subsidiaries are subsidiaries; large one-way flows from an acquired company into [Company] suggest staff moving onto the parent.
5. For the 3 largest acquired companies or subsidiaries Draup holds: profile (workforce, parent shown) and 12-month hiring summary.
6. Rate each: Integrating (few or no own postings, or staff moving to parent), Standalone (own postings continuing), Unclear.
7. For the top target: if Standalone, pull its own top 3 executives; if Integrating, pull the parent's top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the best target and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the target or the parent's integration lead, the action this week and the dated why-now; if none, say so.
- Table "Target check" (top 3): Company | Workforce | Own postings (12 mo) | Rating | Who to approach.
- Table "Acquisitions" (up to 10, newest first): Date | Company | Size or "undisclosed" | In Draup?
- "Expansion plays": per target, the angle for [What I sell] and the timing. "Leave alone": divested or spun-off units, dated.
- Detail: deals from news missing from the table; subsidiaries in talent flow (Company | Moving to parent | Moving back | Read).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- A subsidiary with zero own postings is likely folded into the parent's hiring; don't call it inactive.
- Don't treat internal division names (e.g. "[Company] MedTech") as separate companies unless Draup holds them as one.
- Keep deal sizes as reported; if table and news disagree, show both.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- Talent flow ends about 3 months ago and the last month undercounts exits; state the months.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Label anything you infer as "likely".
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
List [Company]'s acquisitions in [Window] and subsidiaries. Lead with the best target and a named person to approach. For the top 3, check size, own hiring and staff moving to the parent; rate Integrating or Standalone.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [Target], who are the senior leaders and which came from the parent?
```

```text
What does [Target] run in its tech stack compared with the parent?
```

```text
Draft an email to the parent's integration lead offering help with [Target].
```

## Tips for better results

- Deals closed 6–18 months ago are often mid-integration: the busiest window for systems work.
- The acquisitions table can miss big deals; the news step is not optional.

## Related prompts

- [Openings from their recent acquisitions](../../prompts/01-account-research/acquisitions.md): The top 3 integration openings from the account's acquisitions in the last 3 years, who likely owns each, and an optional read of its strategic investments.
- [Map a customer's units, sites and leaders](../../prompts/12-expansion-and-cross-sell/account-map.md): A one-page map of a customer: business units and regions with growth, key sites, the units and brands its leaders sit in and recent acquisitions, marked Ours, Adjacent or Open, with the top white space and who leads it.
- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_partnerships_mergers_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `accounts_talent_flow_insights_companies_v3`, `get_account_details_v3`, `accounts_hiring_summary_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `expand-subsidiaries`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
