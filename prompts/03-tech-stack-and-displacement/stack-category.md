[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What they run in one tech area

> **What they run in one area, ranked by how central each tool is, with your competitors rated Red, Amber or Green, stale tools set aside and a named person to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before discovery or a technical call, when you need to know what you'd sit next to or replace. Use this when you want the whole area; use "Is a competitor installed?" instead when you only care about one rival. | Account Executive, Presales & Solutions, Partnerships & Alliances | Everyone | 2–4 min | Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Technology]` | data warehousing |
| `[What I sell]` | cloud data-platform modernisation services |
| `[Competitor (optional)]` | Snowflake |
| `[View (optional)]` | products (default) or vendors |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my presales technology analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Technology: [area in plain words, e.g. data warehousing, cybersecurity]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]
- Competitor (optional): [vendor or product, e.g. Snowflake — skip if saved in setup]
- View (optional): [products (default) or vendors]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Match my area to Draup's narrowest grouping (sub-category, category or workload) and say which you used. If it returns nothing, try the next broader grouping once.
3. Pull its products, up to 5 pages: maker, sub-category, usage strength (High, Medium, Low), last seen, countries.
4. Split them: Active (a usage strength and seen in the last 12 months) and Stale (the rest).
5. If I named competitors, check the whole stack for their products, whatever area they're filed under (record a product with its maker), and rate each (see rules); count one as present only at High or Medium.
6. If View is vendors, rank makers by Active products: fragmented if no maker holds 25% of them, concentrated if the top 2 hold over 50% (editable defaults).
7. For up to 3 lesser-known Active products, pull what each does and how many companies use it.
8. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table "Active" (top 10, High to Low): Product | Maker | Usage strength | Last seen | Fit (Competes, Complements, Unrelated).
- "My competitors here": product, rating (Red, Amber, Green) and one line of evidence, or "none detected".
- "Why this matters for [What I sell]": 3 bullets: where we'd fit, what we'd replace, one discovery question.
- Detail: vendors view (Rank | Maker | Active products | Main products) with the play (consolidate, replace or attach); "Stale" count plus the 5 most recent; "Products you may not know" with install base; Gaps (what Draup lacked, to ask in discovery).

RULES
- Product counts measure breadth, not spend. Say how many products you reviewed.
- Many products share one last-seen date from a data refresh; lean on usage strength.
- Skip labels that aren't products; flag products credited to the wrong maker.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Rating: High usage in the workloads of What I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named owner and a dated why-now). Then what [Company] runs for [Technology]: active tools by usage strength, my [Competitor] products rated Red, Amber or Green, and stale tools set aside.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which of the active products have the most hiring behind them? Search postings by each product's skill name.
```

```text
Show the same view for [another area] so I can see the adjacent stack.
```

```text
Switch to the vendors view and tell me which makers are fading.
```

```text
Draft a 70-word email to the person in the next step, without naming any tool they haven't named in public.
```

## Tips for better results

- Usage strength (High, Medium, Low) tells you how central a tool is. A product with no strength listed is one Draup no longer detects.
- If your area returns nothing, describe it differently ("data warehouse" rather than "analytics") and the assistant will try Draup's nearest grouping.
- Put your competitors in "Tell your AI about you" once and every tech prompt rates them for you.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.
- [Fading tools and replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_tech_stack_product_data`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `tech-stack-category`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
