[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Openings from their recent acquisitions

> **The top 3 integration openings from the account's acquisitions in the last 3 years, who likely owns each, and an optional read of its strategic investments.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account has been buying or investing in companies and you sell integration, data, migration, change or platform work. | Account Executive, Services, SI & Staffing Seller, Presales & Solutions, Account & Customer Success Manager, Partnerships & Alliances | Everyone | 2–4 min | Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | ERP and data integration services |
| `[Strategic bets (optional)]` | yes — adds investments from the last 12 months |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my M&A analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. ERP and data integration services — skip if you ran the start-here prompt]
- Strategic bets (optional): [yes or no, e.g. yes — adds 12 months of investments]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull acquisitions from the last 3 years.
3. Search 12 months of M&A news with [Company]'s name in the question, not just news tagged to [Company] (the acquired firm is often the one tagged). Add deals where [Company] is the buyer that the table lacks; list divestments separately.
4. Infer each deal's integration work: systems, data, security, process, people.
5. If Strategic bets is yes, pull investments (12 months), drop debt financing, merge repeat rounds and compare themes with stated priorities.
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role; widen as in the executives rule) and the most important news item from the last 90 days where [Company] is the actor, to name who owns the top opening.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Top 3 integration openings for [What I sell]": deal, months since close, likely owner.
- "Acquisitions": Date | Target | Theme | Likely integration work | Source (table or news). Newest first, up to 10.
- Optional "Strategic bets": up to 3, each with a matching priority or "none yet".
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: what each target does and its size; "Divestments (news)": Date | Business sold | Buyer; investments table (Company | Rounds | Total $M | Latest date).

RULES
- Flag rows whose date, target and size don't fit together, and duplicates; count each deal once.
- Deals closed 3–18 months ago (editable default) are usually the best openings. Investment amounts are whole rounds, not [Company]'s cheque.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
[Company]'s acquisitions from the last 3 years, cross-checked with M&A news: bottom line and who to contact, then date, target, theme and likely integration work, and the top 3 openings for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which executives joined [Company] from the acquired companies?
```

```text
What tech stack did the top acquisition bring in?
```

```text
Show strategic investments over the last 3 years to see whether the bets are new.
```

```text
Draft a 100-word note to the owner of the top opening.
```

## Tips for better results

- Most deal sizes are undisclosed. That's normal; the date and theme matter more for timing.
- If the deals table looks empty for a company you know has been buying, the news cross-check usually finds the missing deals.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [New leaders and warm intro paths](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_partnerships_mergers_v3`, `build_news_filters_v3`, `get_signal_news_v3`, `accounts_partnerships_investments_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-acquisitions`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
