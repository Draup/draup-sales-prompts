[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Cross-sell from their adjacent stack

> **The tools a customer runs next to what you already sell them, graded Active, Thin or Fading and rated for incumbent strength, with the priorities and job ads that justify a cross-sell, up to 3 plays and the named owner to pitch.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have a product installed and want to sell the next one, or attach a service to it. | Account & Customer Success Manager, Account Executive, Presales & Solutions | Software sellers | 4–6 min | Tech stack, Priorities & opportunities, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | visa.com |
| `[What we already sell them]` | our data integration platform (or my saved account notes) |
| `[Adjacent areas]` | Data Governance Software, Data Quality Software (optional) |
| `[What I sell]` | data governance and quality platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my cross-sell strategist for a software account team. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. visa.com]
- What we already sell them: [product or category, e.g. our data integration platform — or my saved account notes]
- Adjacent areas (optional): [1–3 software categories, e.g. Data Governance Software, Data Quality Software; if blank, pick the 2–3 next to what we sell]
- What I sell: [one line, e.g. data governance and quality platform — skip if you ran the start-here prompt]

CONTEXT (why this matters)
The easiest expansion is next door to a working install, if the area is open rather than locked by a strong incumbent.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Confirm our install: check the stack for that product or maker (strength, last seen); if not detected, say so.
3. Pull the stack in [Adjacent areas], up to 40 rows each; if a category returns nothing, retry the closest Draup category and say which worked.
4. Grade each tool: Active (High or Medium, seen in 90 days), Thin (Low, seen in 90 days), Fading (no strength, or last seen over 90 days ago). Drop obvious misfilings.
5. Pull up to 5 priorities in the adjacent areas' workloads; keep only those actually about the area.
6. Pull the top 15 job-ad skills for the matching workload (12 months).
7. Owner and trigger: from one page of 10 executives in the matching workload or function, the 3 whose title or skills best fit the adjacent area; and the most important news item from the last 90 days.
8. Build up to 3 plays: Replace (fading or thin incumbent), Consolidate (3+ overlapping tools) or Complement (strong incumbent).

OUTPUT
- Bottom line: 2 sentences — open or locked, and the best play for [What I sell].
- Recommended next step: a named person (name, full title) who owns the adjacent area, the action this week and the dated why-now; if none, say so.
- Table "Cross-sell plays" (up to 3): Play | Target tools | Evidence (dated) | Opening line (25 words max).
- Table "Adjacent landscape" (top 10): Product | Maker | Strength, last seen | Grade.
- One line on our install, and "Incumbents to respect": coexist or compete.
- Detail: the full landscape and why-now evidence (priorities, skills).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- An incumbent with High usage there is Red (locked: complement it); Medium is Amber.
- A product first seen in 12 months and already Medium or High is a fresh choice; complement it.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Trust usage strength and last-seen date; ignore confidence scores and "Generic" rows. A last-seen date shared by many rows is a data refresh. Say "fading", never "dropped".
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
At [Company], confirm our installed product, then grade every tool in [Adjacent areas]. Lead with the best cross-sell play and the named owner to pitch, with a dated why-now. Show incumbent strength, matching priorities and job-ad skills.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Map the buying committee for [Adjacent area].
```

```text
Draft a consolidation business case for the Consolidate play.
```

```text
Which peers of [Company] already run our adjacent product?
```

## Tips for better results

- Name exact Draup categories in Adjacent areas; if unsure, leave it blank and Claude will pick the ones next to what you sell.
- Fragmented areas with several Low tools often signal no clear owner; find one.

## Related prompts

- [What they run in one tech area](../../prompts/03-tech-stack-and-displacement/stack-category.md): What they run in one area, ranked by how central each tool is, with your competitors rated Red, Amber or Green, stale tools set aside and a named person to call.
- [Fading tools and replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_account_priorities_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `expand-adjacent-tech`.

</details>

---

[Back to Expansion and cross-sell](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
