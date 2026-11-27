[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is a competitor installed?

> **A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you pitch a replacement, when a deal stalls and you suspect an incumbent, or before you mention a tool in outreach. Use this for one or two named competitors; use "What they run in one tech area" instead for the whole area. | Account Executive, Presales & Solutions, Marketing & ABM, SDR / BDR | Software sellers | 2–4 min | Tech stack, Priorities & opportunities, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[Competitor]` | Snowflake |
| `[Relationship (optional)]` | rival to displace (default), adjacent tool, or platform we run on |
| `[What I sell]` | lakehouse data platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Competitor: [vendor or product, one or two, e.g. Snowflake, Google BigQuery]
- Relationship (optional): [rival to displace (default), adjacent tool we sit beside, or platform we run on]
- What I sell: [one line, e.g. lakehouse data platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Resolve each competitor to its maker (keep a product's name too) and search the whole stack by that maker, up to 5 pages: usage strength, last seen, countries, workloads; rate each product (see rules). For a broad maker (e.g. Google), keep products in [What I sell]'s space and count the rest.
3. Check whether [Company] makes or owns a product in the same sub-category (its own or acquired brands in its stack). If so, it is more likely consolidating onto its own tool than switching.
4. Pull the other Active products in the same sub-categories, stated priorities in those workloads (newest first; skip ones about products [Company] sells) and the count of job postings in the last 12 months naming the competitor's products.
5. For the next step, pull the top 3 executives in the function closest to [What I sell] (full profile titles; flag subsidiaries) and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. If step 3 found a product [Company] owns, say so here.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: "Installed and active", "Installed but fading" or "Not detected in Draup", with the rating and the evidence.
- Table "Competitor footprint": Product | Usage strength | Last seen | Workloads | Rating.
- Table (up to 3), "Switch triggers" for a rival or "Openings" otherwise: Priority | Source and quarter | Likely owner | Why it opens a door for us.
- Detail: "Who else is in the room" (top 8: Product | Maker | Usage strength | Last seen); hiring evidence (or "none found"); Gaps (what Draup lacked, to ask in discovery).

RULES
- Frame by Relationship. Displace a rival. Never suggest displacing an adjacent tool; look for integration gaps. A platform we run on is a fit signal. Rate rivals only; for the others write "n/a".
- "Active" = a usage strength and seen in the last 12 months; otherwise "fading".
- "Not detected" is not proof they don't use it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Check the whole tech stack for products made by [Competitor], whatever area they're filed under; if [Competitor] is a product (e.g. Google BigQuery), record it and its maker.
- Rating: an installed competitor product with High usage in the workloads of What I sell is Red, Medium is Amber, else Green. Newly detected (first seen within 12 months) is a separate Amber signal.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Is [Competitor] installed anywhere in [Company]'s stack? Rate it Red, Amber or Green, say if [Company] owns a rival product itself, and treat it as a [Relationship].
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
Turn the top switch trigger or opening into a 90-word email to the person in the next step.
```

```text
Run it again with Relationship set to adjacent tool and compare the openings.
```

## Tips for better results

- Set Relationship when the tool isn't a true rival. Datadog is adjacent for a data-observability seller, and a platform such as Snowflake is something you need in the stack, not something to replace.
- If the account makes a product in the same category, the verdict says so first: a company that owns its own tool rarely switches to yours.
- Draup sees tools through public evidence such as job ads. A tool that runs quietly in the background may show as Low or not at all.

## Related prompts

- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of companies in your industry and country whose stack includes a competitor's products, with usage strength shown, distributors and inactive names flagged, and a named person at the top account.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_account_priorities_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `tech-competitor-installed`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
