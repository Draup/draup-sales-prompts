[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Size a vendor's install base

> **What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion, with a named person at the vendor or a first target to approach.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning a partner motion, sizing a competitor's footprint, or picking which product to build a campaign around. | Partnerships & Alliances, Marketing & ABM, Presales & Solutions | Everyone | 1–2 min | Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vendor]` | servicenow.com |
| `[What I sell]` | ITSM implementation and managed services |
| `[Motion (optional)]` | attach or co-sell (default), or replace |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner and market-sizing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vendor: [website of the vendor to size, partner or competitor, e.g. servicenow.com]
- What I sell: [one line, e.g. ITSM implementation and managed services — skip if you ran the start-here prompt]
- Motion (optional): [attach or co-sell (default), or replace]

STEPS
1. Find [Vendor] by its website (exact match) and confirm it is the parent, not a reseller or regional unit. If none or several match, ask me.
2. Pull the products it builds and how many companies Draup detects using each. Rank by companies, largest first.
3. For the top 3, pull the category and what each does.
4. Mark which products [What I sell] attaches to, competes with, or doesn't touch.
5. For the next step: for attach or co-sell, pull the top 3 executives at [Vendor] who run partners, alliances or channels (full profile titles); for replace, name the lead product's best first target list instead. Also pull the most important news item from the last 90 days where [Vendor] is the actor (e.g. a launch or acquisition).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10): Rank | Product | Category | Companies using it | Relation to [What I sell] (Attach, Compete, None).
- "Where the base is concentrated": 2–3 bullets on which products carry the footprint and which are niche.
- "Why this matters for [What I sell]": the 2 products to lead on and why.
- Detail: the rest of the list (Draup returns up to 20 products per vendor); Gaps (what Draup lacked, to ask in discovery).

RULES
- Counts are companies where Draup sees public evidence of use, not licences, seats or revenue.
- Don't add the counts together to get unique customers; one company often uses several products.
- Draup leaves out "Generic" rows. Say if the list looks capped at 20.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Label anything you infer as "likely".
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 350 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named person, a dated why-now). What does [Vendor] build, and how many companies use each product? Top 10 by install base, each marked attach, compete or none for [What I sell].
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
Draft a one-paragraph co-sell pitch to the partner leader in the next step.
```

```text
Show the same view for [a second vendor] so I can compare footprints.
```

## Tips for better results

- Install-base counts are best for comparing products within one vendor, not for quoting as market share.
- Pair this with the competitor target-list prompt to turn the biggest product into a named list.

## Related prompts

- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of companies in your industry and country whose stack includes a competitor's products, with usage strength shown, distributors and inactive names flagged, and a named person at the top account.
- [Which providers to partner with or replace](../../prompts/10-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_key_solution_offerings_v3`, `get_tech_stack_product_data`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `tech-vendor-install-base`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
