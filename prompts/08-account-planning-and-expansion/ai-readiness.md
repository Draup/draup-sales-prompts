# AI readiness vs peers

**A deep read on the account's AI hiring, priorities, new tools and outsourced AI work, then its AI hiring compared with up to 4 close peers.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell AI, data or automation and need a maturity read or a peer comparison. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Marketing & ABM | Everyone | 4–6 min | Hiring & job postings, Priorities & opportunities, Tech stack, Outsourcing deals, Company directory |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[What I sell]` | enterprise generative AI platform |
| `[Peers (optional)]` | lilly.com, abbvie.com, novartis.com, bms.com |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my AI market analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- What I sell: [One line, e.g. enterprise generative AI platform — skip if you ran the start-here prompt]
- Peers: [Optional, up to 4 websites, e.g. lilly.com, abbvie.com; blank = Draup's closest competitors]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Peers, in one company-list lookup: my websites, or the account's top competitors in its primary vertical, keeping the 4 closest in revenue (0.3–3x, editable default), with workforce.
3. Account deep-dive: "Artificial Intelligence & Data Science" postings (12 months, monthly); AI, Generative AI or Machine Learning priorities (count, latest two with quarter); AI tools newly detected in 12 months (up to 5, no generic tools); outsourced AI engagements and top 3 providers.
4. For each peer, pull only AI & Data Science postings with monthly trend.
5. Compare AI postings per 1,000 employees; under 10% apart is level (editable default).

OUTPUT
- Bottom line: 2 sentences — where the account stands and the opening for [What I sell].
- "Account deep-dive": AI postings and trend | AI priorities | New AI tools | Outsourced AI work, each dated.
- "Peers": Company | Workforce | AI postings (12 mo) | Per 1,000 employees | Trend | Read (Ahead / Level / Behind). Account first.
- "Questions to raise": 3, each naming a peer and a number.
- "Why this matters for [What I sell]": 2 bullets and one peer-evidence sentence.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Compare peers on AI hiring only. Tool additions are newly detected, not confirmed rollouts.
- Priorities' quarter labels follow the fiscal year.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Read [Company]'s AI readiness in Draup: AI postings and trend, AI priorities, AI tools newly detected and outsourced AI work. Then compare its AI hiring per 1,000 employees with up to 4 peers.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the 10 most recent AI postings at [Company], with title, date and location.
```

```text
Which executives at [Company] own the AI priorities?
```

```text
Write a 120-word peer-comparison email to the Chief Data Officer.
```

## Tips for better results

- A low AI hiring rate alongside several AI priorities often means the work is outsourced or not yet staffed. Both are openings.
- Pick peers the buyer actually watches. Paste their websites if Draup's competitors don't fit.

## Related prompts

- [Talent rivals: who they lose people to](../../prompts/08-account-planning-and-expansion/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, and credible peers to benchmark against.
- [Benchmark an account against peers](../../prompts/05-prospecting-and-lists/peer-benchmark.md): One table comparing an account with its closest peers on growth, hiring, workforce, footprint and recent news, plus where it leads and where to ask questions.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings and talking points.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `get_tech_stack_trend_v3`, `get_deals_workloads_v3`, `get_deals_service_provider_v3`

Status: **tested live**. Prompt id: `plan-ai-readiness`.

</details>

[Back to Account planning and expansion](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
