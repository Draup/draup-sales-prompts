[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Next quarter's target accounts, ranked by triggers

> **A territory-wide list of accounts ranked by distinct triggers in the last 90 days, activity in the work you sell and rival presence, with one dated why-now each, the person to call at the top account, and the off-list companies acting in your territory.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Setting next quarter's pipeline-generation targets for SDRs and AEs in one territory, or planning a campaign wave. Use "Board slides: where we hunt next quarter" to present the plan, and "Which accounts each rep works this week" for named books. | Sales Leader & RevOps, SDR / BDR, Account Executive, Marketing & ABM | Everyone | 6–10 min | Company directory, News signals, Hiring & job postings, Tech stack, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Automotive |
| `[Country]` | Germany |
| `[Minimum employees]` | 5,000 |
| `[What I sell]` | software-defined-vehicle engineering services |
| `[My competitors (optional)]` | Capgemini Engineering, Bertrandt |
| `[Accounts to exclude (optional)]` | bmwgroup.com |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pipeline-generation strategist for a territory. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Automotive]
- Country: [HQ country in full, e.g. Germany]
- Minimum employees: [e.g. 5,000]
- What I sell: [one line, e.g. software-defined-vehicle engineering services — skip if you ran the start-here prompt]
- My competitors (optional): [rival products or firms, e.g. Capgemini Engineering, Bertrandt — skip if you ran the start-here prompt]
- Accounts to exclude (optional): [websites in active deals, e.g. bmwgroup.com]

STEPS
1. Use Draup's exact industry and country names; map What I sell to its workloads.
2. List the territory: primary industry [Vertical], HQ in [Country], [Minimum employees]+ staff (names only, up to 50, by revenue). Repeat once adding "active in my workloads" and mark those. Remove exclusions.
3. Run three 90-day news searches in [Vertical] and [Country]: (a) leadership changes; (b) expansions and investments; (c) partnerships, vendor selections, acquisitions and divestments.
4. Keep items where a listed company is the actor and the event concerns [Country]; merge repeats. Off-list companies' real events go to "Acting in the territory".
5. For the 10 accounts with the most trigger types, pull full rows in one lookup by exact name, showing only my competitors' products: hiring %, 90-day postings, rivals present.
6. Score (editable): each trigger type 20 (max 60); workload-active 20; rival present 10; hiring % over 8% adds 10. Act this month 60+, Next quarter 30–59, Watch under 30. If over half share a tag, re-tag by rank (top 30%, next 40%, rest) and say so.
7. For the top account, pull its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — how many accounts to work now and what it means for [What I sell].
- Recommended next step: who to contact first (name and title from step 7), what to do, and the dated trigger. If none is found, say so.
- "Target list" (top 10): Account | Triggers (type, date) | In my workloads / rival | Tag | Why now.
- "Targets for next quarter": counts per tag; a split by rep or SDR if I give team size.
- Detail: acting in the territory; accounts with no triggers; dropped items by reason; likely owner title per account.
- Gaps: what Draup didn't have — worth asking in discovery.
- Slide version (only if I ask): 5 bullets, each with one dated number, plus 1 table.

RULES
- Job cuts, plant restructuring or a site sale are triggers only for cost-out, transformation or services offers; say which.
- Board appointments and regional sales hires count only if the role is in my buying area.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Size limits drop companies with no workforce figure (often private firms or mutuals); say so.
- Counts and totals must apply every condition I set; never report one from a check that dropped a condition.
- Rivals: High usage in my workloads is Red, Medium Amber, newly detected Amber; unchecked is "present (usage not checked)". Ignore "Generic" rows.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: rank [Vertical] accounts in [Country] ([Minimum employees]+ staff) by distinct 90-day triggers, activity in my workloads and rival presence, with a dated why-now each for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 70-word opener for each Act-this-month account, tied to its trigger.
```

```text
Add the 11th to 20th accounts and score them the same way.
```

```text
Who leads [Business function] at my top 5 accounts?
```

```text
Rerun with only partnership and vendor-selection news.
```

## Tips for better results

- Accounts with two different trigger types are usually worth more than one account with five articles on the same story.
- The "Acting in the territory" list often holds the best surprises: foreign companies building local sites and private groups your size limit missed.
- Rerun it in the last two weeks of each quarter to refresh targets.

## Related prompts

- [Who in my market just [did X]?](../../prompts/04-signals-and-timing/news-question-templates.md): A clean, dated list of the companies in your industry and country that just did one thing you choose (M&A, layoffs, leadership changes, expansion or new centres, funding, or partnerships), with source counts and a named person at the best account.
- [Weekly trigger sweep for my book](../../prompts/04-signals-and-timing/weekly-book-sweep.md): One phone-sized table of the week's real triggers across up to 10 accounts, including any CEO or leadership change that takes effect in the window, plus the nearest item just outside the window for every quiet account.
- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.
- [Board slides: where we hunt next quarter](../../prompts/15-sales-leadership-and-revops/where-to-hunt-slide.md): Three board-ready slides for one industry — the market in numbers, the 8 accounts to hunt next quarter chosen on fit with what you sell, and what the team needs — with speaker notes and every number dated and sourced.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_universe_companies_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `leaders-pipeline-targets`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
