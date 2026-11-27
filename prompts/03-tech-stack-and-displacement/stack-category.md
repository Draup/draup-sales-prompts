# Their stack in one category

**What they run in one category, ranked by how actively each tool is used, with stale tools set aside, unfamiliar products explained and an optional vendor ranking with a consolidation read.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before discovery or a technical call, when you need to know what you would sit next to or replace, or which vendors dominate an area. | Account Executive, Presales & Solutions, Partnerships & Alliances | Everyone | 2–4 min | Tech stack |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Technology]` | data warehousing |
| `[View]` | products (or vendors) |
| `[What I sell]` | cloud data-platform modernisation services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my presales technology analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Technology: [category in plain words, e.g. data warehousing, cybersecurity]
- View: [products or vendors, e.g. products]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Match my category to Draup's narrowest grouping (sub-category, category or workload) and say which you used.
3. Pull its products, up to 5 pages: maker, sub-category, usage strength (High, Medium, Low), last seen, countries.
4. Split them: Active (a usage strength and seen in the last 12 months) and Stale (the rest).
5. If View is vendors, rank makers by number of Active products.
6. For up to 3 lesser-known Active products, pull what each does and how many companies use it.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table "Active" (top 15, High to Low, then newest): Product | Maker | Sub-category | Usage strength | Last seen | Countries | Likely owner.
- Vendors view: Rank | Maker | Active products | Main products | Competes / Complements / Unrelated, then a read: fragmented if no maker holds 25% of active products, concentrated if the top 2 hold over 50% (editable defaults), and the play: consolidation, replacement or attach.
- "Stale": count, plus the 5 most recent.
- "Products you may not know": one line each, with install base.
- "Why this matters for [What I sell]": 3 bullets: where we'd fit, what we'd replace, one discovery question.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Product counts measure breadth, not spend. Say how many products you reviewed.
- Many products share one last-seen date from a data refresh; lean on usage strength.
- Skip labels that aren't products; flag products credited to the wrong maker.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
What does [Company] use for [Technology] in Draup? Active products by usage strength and last seen, stale ones set aside, unfamiliar products explained. Optionally rank vendors by product count and say if it's fragmented or concentrated.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which of the active products have the most hiring behind them in their job ads?
```

```text
Show the same view for [another category] so I can see the adjacent stack.
```

```text
Switch to the vendors view and tell me which makers are fading.
```

## Tips for better results

- Usage strength (High, Medium, Low) tells you how central a tool is. A product with no strength listed is one Draup no longer detects.
- If your category returns nothing, describe it differently ("data warehouse" rather than "analytics") and Claude will try Draup's nearest grouping.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.
- [Fading stack: replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement pitches.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools linked to it, the service providers working it, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_tech_stack_product_data`

Status: **tested live**. Prompt id: `tech-stack-category`.

</details>

[Back to Tech stack and displacement](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
