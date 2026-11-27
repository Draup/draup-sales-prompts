[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# AI readiness against close peers

> **A read on the account's AI hiring, priorities, new tools and outsourced AI work, its AI hiring compared with up to 4 close peers, and who to raise it with.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell AI, data or automation and need a maturity read or a peer comparison. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Marketing & ABM | Everyone | 4–6 min | Hiring & job postings, Priorities & opportunities, Tech stack, Outsourcing deals, Company directory, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | enterprise generative AI platform |
| `[Peers (optional)]` | lilly.com, abbvie.com, novartis.com, bms.com |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my AI market analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. enterprise generative AI platform; skip if saved in setup]
- Peers (optional): [Up to 4 websites, e.g. lilly.com, abbvie.com; blank = Draup's closest competitors]

STEPS
1. Find the company by website (no result: try its name once and show the match score). Confirm it's the parent, not a subsidiary or sister company; if several match, ask me. Use Draup's exact name from then on.
2. Peers, in one company-list lookup: my websites, or the account's top competitors in its primary industry, keeping the 4 closest in revenue (0.3–3x, editable default), with workforce.
3. Account deep-dive: "Artificial Intelligence & Data Science" postings (12 months, monthly); AI, Generative AI or Machine Learning priorities (count, latest two with quarter); AI tools newly detected in 12 months (up to 5, no generic tools such as chat assistants or office add-ons); outsourced AI engagements and top 3 providers.
4. For each peer, pull only AI & Data Science postings with the monthly trend.
5. Compare AI postings per 1,000 employees; under 10% apart is level (editable default).
6. People and timing: at [Company], pull the top 3 leaders in the function that owns AI and data (often IT) and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — where the account stands and the opening for [What I sell].
- Recommended next step: a person from step 6 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Peers": Company | AI postings (12 mo) | Per 1,000 employees | Trend | Read (Ahead, Level or Behind). Account first.
- "Account deep-dive": 4 dated bullets — AI postings and trend, AI priorities, new AI tools, outsourced AI work.
- "Questions to raise": 3, each naming a peer and a number.
- Gaps: what Draup didn't have, to ask in discovery.
- Detail: peer workforce figures and "Why this matters for [What I sell]" (2 bullets and one peer-evidence sentence).

RULES
- Compare peers on AI hiring only. Tool additions are newly detected, not confirmed rollouts.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Pull lists 10 at a time; count first when a list could be long; every total applies all my conditions.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 420 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Read [Company]'s AI readiness: AI postings and trend, AI priorities, new AI tools and outsourced AI work. Then compare AI hiring per 1,000 employees with up to 4 peers.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the 10 most recent AI postings at [Company], with title, date and location.
```

```text
Which leaders at [Company] own the AI priorities?
```

```text
Write a 120-word peer-comparison email to the person in the next step.
```

## Tips for better results

- A low AI hiring rate alongside several AI priorities often means the work is outsourced or not yet staffed. Both are openings.
- Pick peers the buyer actually watches. Paste their websites if Draup's competitors don't fit.

## Related prompts

- [Who they lose talent to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.
- [Benchmark an account against its peers](../../prompts/06-prospecting-and-lists/peer-benchmark.md): How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `get_tech_stack_trend_v3`, `get_deals_workloads_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-ai-readiness`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
