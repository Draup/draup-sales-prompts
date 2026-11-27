[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Size a vendor's install base

> **What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning a partner motion, sizing a competitor's footprint, or picking which product to build a campaign around. | Partnerships & Alliances, Marketing & ABM, Presales & Solutions | Everyone | 1–2 min | Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vendor]` | servicenow.com |
| `[What I sell]` | ITSM implementation and managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner and market-sizing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vendor: [website of the vendor to size, partner or competitor, e.g. servicenow.com]
- What I sell: [one line, e.g. ITSM implementation and managed services — skip if you ran the start-here prompt]

STEPS
1. Find [Vendor] by its website (exact match) and confirm it is the parent, not a reseller or regional unit. If none or several match, ask me.
2. Pull the products it builds and how many companies Draup detects using each. Rank by companies, largest first.
3. For the top 3, pull the category and what each does.
4. Mark which products [What I sell] attaches to, competes with, or doesn't touch.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table (up to 20 rows): Rank | Product | Category | Companies using it | Relation to [What I sell] (Attach / Compete / None).
- "Where the base is concentrated": 2–3 bullets on which products carry the footprint and which are niche.
- "Why this matters for [What I sell]": attach, co-sell or replace, with the 2 products to lead on and why.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Counts are companies where Draup sees public evidence of use, not licences, seats or revenue.
- Don't add the counts together to get unique customers; one company often uses several products.
- Draup returns up to 20 products per vendor and leaves out "Generic" rows. Say if the list looks capped.
- For the next step, suggest a target list of companies whose stack includes the lead product.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Label anything you infer as "likely".
- Keep to about 250 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
What products does [Vendor] build, and how many companies in Draup use each one? Table sorted by install base, with an attach, co-sell or replace angle for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
List companies in [Vertical] headquartered in [Country] whose stack includes [top product], sorted by revenue.
```

```text
Which of my target accounts also run [top product]?
```

```text
Draft a one-paragraph co-sell pitch to the vendor's partner team.
```

## Tips for better results

- Install-base counts are best for comparing products within one vendor, not for quoting as market share.
- Pair this with the displacement list prompt to turn the biggest product into a named target list.

## Related prompts

- [Displacement target list](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A sized, revenue-ranked list of companies in your industry and country whose stack includes a competitor's products, confirmed in the same pass, with likely-inactive and misfiled names set aside.
- [Who to partner with vs replace, by priority](../../prompts/06-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it, and whether to partner, displace or walk into an open door.
- [Battlecard: rival software vendor](../../prompts/09-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest companies running them, recent moves, how to beat it and the objection to expect.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_key_solution_offerings_v3`, `get_tech_stack_product_data`

Status: **tested live**. Prompt id: `tech-vendor-install-base`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
