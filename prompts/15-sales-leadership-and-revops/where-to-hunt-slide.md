[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Board slides: where we hunt next quarter

> **Three board-ready slides for one industry — the market in numbers, the 8 accounts to hunt next quarter chosen on fit with what you sell, and what the team needs — with speaker notes and every number dated and sourced.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preparing a quarterly business review, a board update or a sales kick-off section on where the team will hunt next quarter. Use "Next quarter's target accounts" when you need a working list for reps rather than slides. | Sales Leader & RevOps, Marketing & ABM | Everyone | 4–6 min | Industry ecosystem, News signals, Outsourcing deals, Tech stack, Executives & movement, Company directory |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[Territory (optional)]` | United States of America |
| `[What I sell]` | claims and underwriting data services |
| `[My competitors (optional)]` | Guidewire, Duck Creek |
| `[Our position (optional)]` | 4 customers in the vertical, 1 partner |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my chief of staff to the sales leader, building board slides. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Territory (optional): [e.g. United States of America; default: my territory from setup; narrows the account picks — industry totals stay global]
- What I sell: [one line, e.g. claims and underwriting data services; skip if saved in setup]
- My competitors (optional): [rival products or firms, e.g. Guidewire, Duck Creek; skip if saved in setup]
- Our position (optional): [e.g. 4 customers in the vertical, 1 partner]

STEPS
1. Use Draup's exact industry and territory names; map What I sell to its workloads. If the industry returns zeros, try its parent and name it.
2. Pull the industry's revenue and growth (Draup may give no year; say so).
3. Pull industry priorities; keep the 3 most relevant to [What I sell] (examples are undated; say so).
4. Pull the top outsourcing buyers and fastest-growing companies by workforce (fixed top 50s, worldwide); keep growers with 1,000+ staff, in [Territory].
5. Run one 90-day news search in the industry and territory (acquisitions, expansions, partnerships, investments, leadership changes); review up to 20 items.
6. Shortlist 12 candidates (two-list companies first) and check them in one company list by exact name, showing only my competitors' products and whether each is active in my workloads. Pick 8: workload-active first, then two-list, then the strongest single reason. For the top 3 picks, check rival usage (only High or Medium counts); for the rest write "rival listed, usage not checked".
7. For the top pick, pull its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where we hunt and what it means for [What I sell].
- Recommended next step: the first board ask and its owner; then the first account, with a named person (step 7) and one dated fact. If none, say so.
- Slide 1 "[Vertical]: the market": one-sentence headline, revenue and growth, 3 priorities with what each means for us.
- Slide 2 "Where we hunt next quarter": Account | Why it fits (workloads, rival) | Why now (dated) | Likely owner (title). 8 rows.
- Slide 3 "What we need": 3 asks, each tied to a slide-2 fact and Our position.
- Detail: speaker notes (60 words per slide); sources and caveats.
- Gaps: what Draup didn't have, to ask in discovery.
- One-slide version (only if asked): 5 dated bullets plus 1 table.

RULES
- Use growth-list companies only from the core business; mark brokers, health groups and agencies.
- If an industry total is driven by one company (over a third), name it.
- Why-now counts only if dated in the last 90 days with the company as actor.
- Industry totals are global estimates; never add them to company figures.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 500 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: 3 board slides on [Vertical] for [What I sell] — market numbers, 8 accounts to hunt next quarter (each active in my workloads, with a dated why-now) and the asks.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn slide 2 into a one-page brief per account for the team.
```

```text
Redo the slides for [Second vertical] so I can compare.
```

```text
Add a fourth slide: which services rivals lead in this industry and where we rank.
```

```text
Shorten everything to one slide for the board pack.
```

## Tips for better results

- Accounts that appear on two lists and are active in your workloads usually make a stronger board story than the biggest logo.
- Keep the speaker notes; they hold the caveats the slide can't.
- If you share these slides outside the company, check your Draup licence before publishing Draup data externally.

## Related prompts

- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.
- [Spot scale-up and cost-out buyers](../../prompts/06-prospecting-and-lists/growth-and-cost-out.md): Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and a named person to call first.
- [Next quarter's target accounts, ranked by triggers](../../prompts/15-sales-leadership-and-revops/pipeline-targets.md): A territory-wide list of accounts ranked by distinct triggers in the last 90 days, activity in the work you sell and rival presence, with one dated why-now each, the person to call at the top account, and the off-list companies acting in your territory.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_revenue`, `ecosystem_get_vertical_key_priorities`, `ecosystem_get_vertical_outsourcing_customers`, `ecosystem_get_organization_increasing_workforce`, `get_signal_news_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `leaders-where-to-hunt-slide`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
