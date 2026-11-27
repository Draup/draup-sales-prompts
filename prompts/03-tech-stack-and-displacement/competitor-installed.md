[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is a competitor installed?

> **A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you pitch a replacement, or when a deal stalls and you suspect an incumbent. | Account Executive, Presales & Solutions, Marketing & ABM | Software sellers | 2–4 min | Tech stack, Priorities & opportunities, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[Competitor]` | Snowflake |
| `[What I sell]` | lakehouse data platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive displacement analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Competitor: [vendor or product, one or more, e.g. Snowflake, Google BigQuery]
- What I sell: [one line, e.g. lakehouse data platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Resolve each competitor to its maker (for a product, keep the product name too).
3. Search the whole stack by that maker, up to 5 pages, confirming each row. For a broad maker (e.g. Google), keep products in [What I sell]'s space and count the rest.
4. For each competitor product: usage strength, last seen, countries, workloads.
5. Pull the other Active products in the same sub-categories.
6. Pull stated priorities in those workloads, newest first. If [Company] sells technology itself, skip priorities about products it sells.
7. Count job postings in the last 12 months naming the competitor's products as a skill.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Verdict: "Installed and active", "Installed but fading" or "Not detected in Draup", with the evidence.
- Table "Competitor footprint": Product | Maker | Usage strength | Last seen | Countries | Workloads.
- Table "Who else is in the room" (top 8, strongest first): Product | Maker | Usage strength | Last seen.
- "Hiring evidence": postings naming the competitor (12 months), or "none found".
- Table "Switch triggers" (up to 3): Priority | Source and fiscal quarter | Likely owner | Why it could justify a switch.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- "Active" = a usage strength and seen in the last 12 months; otherwise "fading".
- Give a start date only if the first-seen date falls after the product launched; otherwise "start date unknown".
- "Not detected" is not proof they don't use it.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Check the whole tech stack for any product made by [Competitor], whatever area it's filed under. If [Competitor] is a product (e.g. Google BigQuery), record the product and its maker.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Check [Company]'s whole tech stack for any product made by [Competitor], whatever area it's filed under. Show usage strength, last seen and countries, what else runs alongside it, and 3 priorities that could justify a switch.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who owns the workloads where [Competitor] sits? Map the buying committee.
```

```text
Find 10 more companies in the same industry whose stack includes [Competitor] products.
```

```text
Turn the switch triggers into a 90-word email to the head of data.
```

## Tips for better results

- Spell the vendor the way it brands itself ("Snowflake", not "Snowflake Computing Inc."). If you name a product, Claude also checks everything else its maker sells.
- Draup sees tools through public evidence such as job ads. A tool that runs quietly in the background may show as Low or not at all.

## Related prompts

- [Displacement target list](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A sized, revenue-ranked list of companies in your industry and country whose stack includes a competitor's products, confirmed in the same pass, with likely-inactive and misfiled names set aside.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools linked to it, the service providers working it, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_account_priorities_v3`, `accounts_hiring_demand_category_v3`

Status: **tested live**. Prompt id: `tech-competitor-installed`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
