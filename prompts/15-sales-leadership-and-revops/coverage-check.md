[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which accounts each rep works this week

> **Your pasted accounts and owners checked against real triggers in the window, tied to what you sell, grouped by owner, with the 5 actions for this week, the named person behind the top action, and which reps' books have gone quiet.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a weekly or monthly team call, when you need to point reps at the accounts that just changed. Use "Weekly trigger sweep for my book" for your own accounts without owners or coaching notes. | Sales Leader & RevOps, Account & Customer Success Manager | Everyone | 4–6 min | News signals, Company directory, Tech stack, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts and owners]` | costco.com – Rep A; starbucks.com – Rep A; fedex.com – Rep B; att.com – Rep B; visa.com – Rep C; mastercard.com – Rep C |
| `[What I sell]` | observability and IT operations software |
| `[My competitors (optional)]` | Datadog, Dynatrace |
| `[Window (optional)]` | last 30 days |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales manager running a pipeline and coverage review. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Accounts and owners: [up to 15 lines of website – owner, e.g. costco.com – Rep A; fedex.com – Rep B]
- What I sell: [one line, e.g. observability and IT operations software; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Datadog, Dynatrace; skip if saved in setup]
- Window (optional): [default last 30 days; up to 90]

STEPS
1. Resolve all accounts by website (exact) in one short lookup; if a website returns nothing, look it up by name once and show the match and its score; ask if only suggestions return. Never drop an account silently. Keep each owner beside the account.
2. Pull one news feed for all accounts in the window, material categories only (leadership, acquisitions, partnerships and vendor deals, expansions and new centres, investments, layoffs), 2 pages. If one account fills over a third of items, pull again without it.
3. For accounts still under 2 items, pull their top-ranked signals and keep items dated inside the window.
4. Drop noise and items where the account isn't the actor (it advised on, supplied or was merely named in someone else's deal). Merge repeats.
5. Tag each trigger: Strong (opens a project or budget), Useful (a reason to call), Context.
6. Rank by strength, then recency; group by owner. If I named competitors, check the stacks of the top 3 action accounts and rate them.
7. For action 1, pull the account's top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where the team should spend this week and what it means for [What I sell].
- Recommended next step: action 1 — who to contact (name and title from step 7), what to do, and the dated trigger. If none is found, say so.
- "This week's 5 actions": Account | Owner | Trigger (what, date) | Strength | Action.
- "By owner": Owner | Strong | Useful | Quiet accounts | Coaching note.
- Detail: quiet accounts with their latest item's date; not resolved; rival ratings; coverage flags (3+ Strong for one owner, or a whole book quiet); sources.
- Gaps: what Draup didn't have, to ask in discovery.
- Slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Every trigger needs a date inside the window; drop anything you can't date.
- A trigger counts once per account, however many outlets covered it.
- Don't pull leadership-move histories for every account.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Rivals count only at High or Medium usage (say how many were Low). Software: High in my workloads Red, Medium or newly detected Amber, else Green. Services, by share of active engagements in my workloads: 30%+ Red, 10–29% Amber, under 10% Green. No "Generic" rows.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: for [Accounts and owners], find triggers in [Window] that matter to [What I sell], group them by owner, rank this week's 5 actions with a named contact for action 1, and list quiet books.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a 60-word note to each owner with their top action.
```

```text
Write the opener for action 1, tied to the trigger.
```

```text
Extend the window to 90 days for the quiet accounts.
```

```text
Rebalance: suggest moving 2 quiet accounts from the busiest owner to the quietest.
```

## Tips for better results

- Paste the owner next to each website; the by-owner view is what makes this a management tool rather than a news digest.
- A big brand can dominate a combined news feed; the per-account check stops quieter accounts being missed.
- Use the coaching notes in one-to-ones rather than reading the full table in the team call.

## Related prompts

- [Weekly trigger sweep for my book](../../prompts/04-signals-and-timing/weekly-book-sweep.md): One phone-sized table of the week's real triggers across up to 10 accounts, including any CEO or leadership change that takes effect in the window, plus the nearest item just outside the window for every quiet account.
- [Sort my book into coverage tiers](../../prompts/15-sales-leadership-and-revops/book-segmentation.md): Up to 20 accounts sorted into Strategic, Growth, Maintain and Deprioritise on an editable potential-versus-momentum rubric that scores your own workloads and rivals, with the coverage model for each tier and the flags behind every placement.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_universe_companies_v3`, `get_news_feed_v3`, `get_top_signals`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `leaders-coverage-check`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
