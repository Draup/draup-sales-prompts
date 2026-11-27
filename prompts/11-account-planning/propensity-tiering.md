[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Tier my accounts by fit and timing

> **Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning a quarter or a territory, or deciding where to spend limited time. Use "Carve balanced territories by geography" instead to split a whole market between reps. | Account Executive, Sales Leader & RevOps, Account & Customer Success Manager, SDR / BDR | Everyone | 4–6 min | Company directory, Company & financials, Hiring & job postings, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | target.com, merck.com, fedex.com |
| `[What I sell]` | supply-chain planning software |
| `[Target revenue band (optional)]` | $5B–$150B |
| `[Competitor (optional)]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my territory planning analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Accounts: [Up to 25 websites, e.g. target.com, merck.com, fedex.com]
- What I sell: [One line, e.g. supply-chain planning software; skip if saved in setup]
- Target revenue band (optional): [e.g. $5B–$150B]
- Competitor (optional): [e.g. Kinaxis, o9 Solutions]

STEPS
1. Look up the accounts by website, 10 per lookup. A website that returns nothing: look it up by name once and show the match score; prefer the parent, and ask if the score is under 0.8 or the match is a subsidiary. Never drop an account silently.
2. Take revenue, growth, Opportunity Index, hiring %, workforce growth and industry.
3. Map [What I sell] to 1–3 Draup workloads and say which. For each account, pull 12-month postings in those workloads (one small lookup each) and rank them.
4. With competitors named, find which accounts list their products (one lookup), then check usage in my workloads for the top 10 by Fit.
5. For the top 10 by Fit, count distinct dated 90-day news events with the company as actor (tied to [What I sell] counts double). Others: "not checked", 8 points.
6. Score and tier (re-tier rule, then fit gate).
7. At the top account, pull the top 3 leaders in the function closest to [What I sell] and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the A accounts and what they share.
- Recommended next step: a person from step 7 (name and title), what to do, and the dated why-now; if none, say so.
- Table: Tier | Account | Total (Fit + Timing) | Strongest driver | Weakest driver. By total.
- One-line reason per A account.
- Gaps: what Draup didn't have, to ask in discovery.
- Detail: per-account values (postings, competitor usage, news count), rubric, "Data flags" (missing values, name matches with scores, subsidiaries, possibly inactive, fit-gate caps).

RULES
- Rubric (editable defaults). FIT 50: relevance 20 (postings in my workloads: list's top third 20, middle 10, else 0); competitor installed 5 (High or Medium in my workloads 5, High or Medium elsewhere 2, Low or none 0: a displacement play); Opportunity Index 10 (score); revenue in band 10 (in 10, within 2x 5, else 2; 10 if no band); revenue growth 5 (over 5% 5, 0–5% 3). TIMING 50: news 20 (0, 1–2 = 8, 3–5 = 14, 6+ = 20); hiring % 15 (over 10% 15, 5–10% 10, 2–5% 5); workforce growth 15 (over 3% 15, 0–3% 10, −3–0% 5).
- Leave out IT spend (modelled from revenue).
- Tiers: A 70+, B 50–69, C under 50. If more than half the list lands in one tier, re-tier by rank (top 30% A, next 40% B, rest C) and say so.
- Fit gate, applied last: Fit under 25 of 50 caps an account at C, whatever its Timing; show "low fit" as its weakest driver.
- Missing value: half points, flagged.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Tier [Accounts] for [What I sell] on fit (postings in my workloads, installed [Competitor]) and timing; Fit under 25 caps at C; show any name-matched website's score.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Change the rubric: relevance 30, Opportunity Index 0, and rerun.
```

```text
For my A accounts, give one why-now signal each from the last 60 days.
```

```text
Count news events for the accounts marked "not checked".
```

```text
Build a one-page account brief for the top-scoring account.
```

## Tips for better results

- The rubric is in the prompt on purpose. Change the weights to match how your team actually wins.
- Use websites, not names. Some parents use unusual domains (home.barclays, group.bnpparibas), and some websites land on a subsidiary; if a website fails, the answer shows the name match and its score so you can check it.
- The fit gate stops a busy but irrelevant account (lots of news, little hiring in your workloads) from reaching the A or B tier.

## Related prompts

- [Carve balanced territories by geography](../../prompts/11-account-planning/territories.md): An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.
- [Benchmark an account against its peers](../../prompts/06-prospecting-and-lists/peer-benchmark.md): How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `get_top_signals`, `accounts_hiring_timeline_v3`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `plan-propensity-tiering`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
