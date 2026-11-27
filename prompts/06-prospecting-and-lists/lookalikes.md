[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Look-alikes of a best customer

> **Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a strong reference customer and want more accounts like it. | SDR / BDR, Account Executive, Marketing & ABM, Sales Leader & RevOps | Everyone | 2–4 min | Company directory, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | your best customer's website (e.g. contoso.com, illustrative) |
| `[Key products to match (optional)]` | SAP, Blue Yonder |
| `[How many]` | 20 |
| `[What I sell]` | retail demand-forecasting software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-targeting analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [Best customer's website, e.g. contoso.com (illustrative)]
- Key products to match (optional): [e.g. SAP, Blue Yonder]
- How many: [default 20]
- What I sell: [one line, e.g. retail demand-forecasting software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. Profile it: primary vertical, HQ country, workforce, revenue. With no key products given, pick its 5 products most relevant to [What I sell], skipping generic office and browser tools.
3. Start with Draup's listed competitors; keep those in the same business at 0.3–3x its workforce (editable default) and record removals.
4. Widen: same primary vertical and HQ country, 0.3–3x workforce, listing only companies whose tech stack includes the key products, showing which ones. Match by product or vendor, not category. Sort by Opportunity Index.

OUTPUT
- Bottom line: 2 sentences — how many real look-alikes exist and what that means for [What I sell].
- One line: the customer profile used.
- Table (top [How many]): Company | Why similar | Workforce | Revenue ($M, FY) | Shared key products | Listed competitor? | Opportunity Index | Who to call (title) | Flag.
- "Best 5 to start with": one reason each.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Never include the customer, its subsidiaries or sister companies.
- If fewer than [How many] fit, name the criterion you loosened; never loosen silently.
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Use primary vertical only, sort largest first, and flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- Size filters drop companies with no workforce figure; say how many and offer to include them.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Find [How many] look-alikes of [Company]: Draup's listed competitors first, then same primary vertical and HQ country at 0.3–3x its workforce whose stack includes its key products. Explain each match and add who to call.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which of the best 5 show a fresh dated event in the last 90 days?
```

```text
Write a reference-style opener for each of the best 5 without naming [Company].
```

```text
Who owns [Business function] at the top 3?
```

## Tips for better results

- Naming 2 or 3 key products gives tighter matches than letting Claude pick.
- Use the website rather than the name; it is the most reliable way to land on the right company.

## Related prompts

- [Sell into a customer's competitors](../../prompts/06-prospecting-and-lists/competitor-set.md): Your customer's real competitors, ranked by Draup's Opportunity Index score, with what happened at each in the last 90 days, a reference angle and who to call.
- [Build and size an ICP list](../../prompts/06-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.
- [Benchmark an account against peers](../../prompts/06-prospecting-and-lists/peer-benchmark.md): One table comparing an account with its closest peers on growth, hiring, workforce, footprint and recent news, plus where it leads and where to ask questions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_tech_stack_products_v3`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `prospect-lookalikes`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
