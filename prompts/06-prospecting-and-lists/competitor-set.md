[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Sell into your customer's competitors

> **Your customer's real competitors, ranked, with what happened at each in the last 90 days, a reference angle and a named person to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You just won, or have a strong reference at, a company and want to take the story to its rivals. | Account Executive, SDR / BDR, Marketing & ABM, Sales Leader & RevOps | Everyone | 2–4 min | Company directory, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | your customer's website (e.g. fabrikam.com, illustrative) |
| `[Referenceable?]` | no |
| `[Proof point (optional)]` | cut scheduling overtime across its stores |
| `[What I sell]` | warehouse workforce-scheduling software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-based marketing analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [customer's website, e.g. fabrikam.com (illustrative)]
- Referenceable?: [yes or no — may I name them? e.g. no]
- Proof point (optional): [e.g. cut scheduling overtime across its stores]
- What I sell: [one line, e.g. warehouse workforce-scheduling software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name and show the match score) and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. Pull Draup's listed competitors (parent companies only), ranked by Opportunity Index (Draup's 0–10 account-attractiveness score), with workforce and revenue.
3. Keep same-primary-vertical companies at 0.3–3x the customer's workforce (editable); record removals. If under 4 remain, add same-vertical, same-HQ-country companies in that range, labelled "added peer".
4. For the top 5, pull top news from the last 90 days and keep material events: deals, new centres, M&A, senior leadership changes, layoffs, launches that touch [What I sell].
5. For the #1 target: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — the best next targets and why, for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 5": Competitor | Workforce | What happened (date, headline) | Reference angle (our result → their situation).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: full ranked list (Opportunity Index, revenue $M with FY, listed or added); "Removed" with reasons.

RULES
- If Referenceable? is no, never name [Company]; say "a leading [vertical] peer".
- Write "No material events in 90 days" rather than padding.
- Don't compare companies on Draup's yes/no event flags; count dated events.
- Show USD millions using Draup's conversion rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: list [Company]'s real competitors, ranked, with up to 2 material events each from the last 90 days, a reference angle and who to call at the best target.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 3-email sequence for the #1 competitor using the reference angle.
```

```text
Check the whole tech stack of the top 5 for any product that competes with ours.
```

```text
Who owns [Business function] at the top 2? Names and full titles.
```

## Tips for better results

- Check the Removed list; small or unrelated firms are filtered out there.
- Ask your customer before naming them. The prompt defaults to an anonymous reference.

## Related prompts

- [Benchmark an account against its peers](../../prompts/06-prospecting-and-lists/peer-benchmark.md): How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.
- [Find look-alikes of your best customer](../../prompts/06-prospecting-and-lists/lookalikes.md): Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches, plus who to call first and why now.
- [Signal-led emails for up to 10 accounts](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 10 per pass: the most relevant recent signal (preferring your territory), the priority it supports, a fact check, and a short opener written in your persona's language that ends in one easy ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-competitor-set`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
