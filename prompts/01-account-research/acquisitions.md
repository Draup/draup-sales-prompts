[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Acquisitions, strategic bets and the openings they create

> **The account's acquisitions in the last 3 years, grouped by theme, the integration work each creates and the top 3 openings for you, plus an optional read of its strategic investments.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account has been buying or investing in companies and you sell integration, data, migration, change or platform work. | Account Executive, Services, SI & Staffing Seller, Presales & Solutions, Account & Customer Success Manager, Partnerships & Alliances | Everyone | 2–4 min | Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | ERP and data integration services |
| `[Strategic bets]` | yes (optional; adds investments from the last 12 months) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my M&A analyst for a sales team. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. ERP and data integration services — skip if you ran the start-here prompt]
- Strategic bets: [yes or no, e.g. yes — adds 12 months of investments]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull acquisitions from the last 3 years.
3. Search 12 months of M&A news with [Company]'s name in the question, not just news tagged to [Company] (the acquired firm is often the one tagged). Add deals where [Company] is the buyer that the table lacks; list divestments separately.
4. Infer each deal's integration work: systems, data, security, process, people.
5. If Strategic bets is yes, pull investments (12 months), drop debt financing, merge repeat rounds and compare themes with stated priorities.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Acquisitions": Date | Target | What it does | Size | Theme | Likely integration work | Source (table or news). Newest first.
- "Top 3 integration openings for [What I sell]": deal, months since close, likely owner (title).
- "Divestments (news)": Date | Business sold | Buyer.
- Optional "Strategic bets: investments in the last 12 months": Company | What it does | Rounds | Total ($M) | Latest date; then up to 3 bets, each with a matching priority or "none yet".
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Flag rows whose date, target and size don't fit together, and duplicates; count each deal once.
- Deals closed 3–18 months ago (editable default) are usually the best openings. Investment amounts are whole rounds, not [Company]'s cheque.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Drop news noise: outages (unless I sell security), stock chatter, charity, awards, passing mentions, look-alike or sister companies, and re-dated old stories (use the event date in the text). Give source, headline and link if Draup has one.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
List [Company]'s acquisitions from the last 3 years (date, target, size, theme, likely integration work and owner), cross-checked with M&A news, then the top 3 openings for [What I sell]. Optionally add investments from the last 12 months.
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
Draft a 100-word note to the likely owner of the top opening.
```

## Tips for better results

- Most deal sizes are undisclosed. That's normal; the date and theme matter more for timing.
- If the deals table looks empty for a company you know has been buying, the news cross-check usually finds the missing deals.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.
- [New leaders in the last 6 months](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted in the last 6 months in your area, where they came from, and which ones arrive from your customers.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): Where the account's priorities cluster, how each fits what you sell, and the single priority to lead with, with its likely owner and linked vendors.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_partnerships_mergers_v3`, `build_news_filters_v3`, `get_signal_news_v3`, `accounts_partnerships_investments_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `research-acquisitions`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
