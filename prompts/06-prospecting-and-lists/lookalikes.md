[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Find look-alikes of your best customer

> **Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches, plus who to call first and why now.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a strong reference customer and want more accounts like it. | SDR / BDR, Account Executive, Marketing & ABM, Sales Leader & RevOps | Everyone | 2–4 min | Company directory, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | your best customer's website (e.g. contoso.com, illustrative) |
| `[Key products to match (optional)]` | SAP, Blue Yonder |
| `[Territory (optional)]` | HQ country; default: my territory from setup, else the customer's HQ country |
| `[What I sell]` | retail demand-forecasting software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-targeting analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [best customer's website, e.g. contoso.com (illustrative)]
- Key products to match (optional): [e.g. SAP, Blue Yonder]
- Territory (optional): [HQ country; default: my territory from setup, else the customer's HQ country]
- What I sell: [one line, e.g. retail demand-forecasting software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name and show the match score) and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. Profile it: primary vertical, HQ country, workforce, revenue. With no key products given, pick its 5 products most relevant to [What I sell], skipping office, browser and chat tools.
3. Start with Draup's listed competitors; keep those in the same business at 0.3–3x its workforce (editable) and record removals.
4. Widen: same primary vertical, HQ in [Territory], parent companies only, 0.3–3x workforce, listing only companies whose stack includes the key products and showing which ones. Match by product or vendor, not category. Sort by Opportunity Index (Draup's 0–10 account-attractiveness score). Stop at 20.
5. For the best 5: the most important news item from the last 90 days where the company is the actor. For the #1: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — how many real look-alikes exist and what that means for [What I sell].
- Recommended next step: a named person (name and full title from step 5), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Best 5 to start with": Company | Why similar | Shared key products | Why now (dated).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: one line with the customer profile used; the full list (Company | Workforce | Revenue ($M, FY) | Shared products | Listed competitor? | Flag); removals.

RULES
- Never include the customer, its subsidiaries or sister companies.
- If fewer than 20 fit, name the criterion you loosened; never loosen silently.
- If I've named competitors (here or in my setup), check the best 5's whole stack: High usage = Red; Medium or first seen in 12 months = Amber; Low or absent = Green (count presence only at High or Medium; say so). Rate a services rival by its share of active engagements: 30%+ Red, 10–29% Amber, under 10% Green.
- Size filters drop companies with no workforce figure; say how many and offer to include them.

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
Bottom line and next step first: find up to 20 look-alikes of [Company] (same industry and HQ country, 0.3–3x its size, sharing its key products), say why each matches, and name who to call at the best one.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a reference-style opener for each of the best 5 without naming [Company].
```

```text
Who owns [Business function] at the top 3? Names and full titles.
```

```text
Show the next 10 look-alikes.
```

## Tips for better results

- Naming 2 or 3 key products gives tighter matches than letting Claude pick.
- Use the website rather than the name; it is the most reliable way to land on the right company.

## Related prompts

- [Sell into your customer's competitors](../../prompts/06-prospecting-and-lists/competitor-set.md): Your customer's real competitors, ranked, with what happened at each in the last 90 days, a reference angle and a named person to call first.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [Benchmark an account against its peers](../../prompts/06-prospecting-and-lists/peer-benchmark.md): How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_tech_stack_products_v3`, `get_universe_companies_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-lookalikes`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
