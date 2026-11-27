[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Benchmark an account against its peers

> **How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want peer context for a meeting, a QBR or a leadership review, scored on what you sell rather than generic size. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Marketing & ABM, Sales Leader & RevOps | Everyone | 2–4 min | Company directory, Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | delta.com |
| `[Peer websites (optional)]` | united.com, aa.com |
| `[What I sell]` | airline operations analytics platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive benchmarking analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [account website, e.g. delta.com]
- Peer websites (optional): [up to 4, e.g. united.com, aa.com]
- What I sell: [one line, e.g. airline operations analytics platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name and show the match score) and confirm it's the parent, not a subsidiary; ask me if several match.
2. No peers given? Use Draup's listed competitors and keep the 4 closest in business and size. Look everyone up by website; retry any miss once by name and show the match score, never dropping one silently.
3. One company list for everyone: revenue and growth, workforce and growth %, attrition %, postings (90 days), Opportunity Index (Draup's 0–10 score).
4. Postings in the workloads mapped to What I sell, last 12 months, for all companies in one pass; add postings per 1,000 employees. Name the workloads used.
5. If I've named competitors (here or in my setup), check each company's whole stack for their products, with usage strength and first- and last-seen dates.
6. Count distinct material news events in the last 90 days for each and keep the most material ("10+" if the first 10 all qualify).
7. For [Company]: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — where [Company] stands on what matters to [What I sell].
- Recommended next step: a named person (name and full title from step 7), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Benchmark" (up to 8 rows): Metric | [Company] | Peer median | Leader | Read. Rows: revenue growth, workforce growth, postings in my workloads (12 months) and per 1,000, my competitors installed, news events (90 days).
- "Questions to ask": 3 places it trails, phrased as discovery questions, never "you're behind".
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: the full per-company table (fiscal year beside money); each company's most material event (date, headline, source); competitor products found.

RULES
- Rate my competitors by usage in the workloads I sell into: High = Red, Medium or first seen in 12 months = Amber, Low or absent = Green (only High or Medium count as installed; say so); services rivals by engagement share: 30%+ Red, 10–29% Amber, under 10% Green.
- Don't compare on IT spend (modelled from revenue) or Draup's yes/no event flags; count dated events.
- Show USD millions using Draup's conversion rate.
- If I ask for a slide: 5 bullets + 1 table.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: benchmark [Company] against [Peer websites] (or its 4 closest Draup-listed competitors) on growth, postings in what I sell, my competitors in the stack and 90-day news. Then 3 discovery questions and who to call.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which products did the peers adopt in the last 12 months that [Company] doesn't run?
```

```text
Turn the questions into a 100-word email to the person in the next step.
```

```text
Add 2 more peers and rerun the benchmark.
```

## Tips for better results

- Works best with 3 to 4 peers of similar size.
- Lead with questions, not comparisons. Buyers open up when asked how they see a gap.

## Related prompts

- [Sell into your customer's competitors](../../prompts/06-prospecting-and-lists/competitor-set.md): Your customer's real competitors, ranked, with what happened at each in the last 90 days, a reference angle and a named person to call first.
- [AI readiness against close peers](../../prompts/11-account-planning/ai-readiness.md): A read on the account's AI hiring, priorities, new tools and outsourced AI work, its AI hiring compared with up to 4 close peers, and who to raise it with.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `talent_demand_top_companies_v3`, `get_account_tech_stack_products_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-peer-benchmark`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
