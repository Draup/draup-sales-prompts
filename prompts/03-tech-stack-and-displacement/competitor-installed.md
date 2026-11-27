[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is a competitor installed?

> **Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.**

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
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Resolve each competitor to its maker (keep the product name) and search the whole stack by that maker, whatever area it's filed under, up to 5 pages: usage strength, last seen, workloads. Rate each product (see rules). For a broad maker (e.g. Google), keep products in [What I sell]'s space and count the rest. A row named only after the maker is weaker evidence than a named product; say which row carries the verdict.
3. Check whether [Company] makes or owns a product in the same sub-category. If so, it is more likely to consolidate onto its own tool than switch.
4. Pull the other Active products in the same sub-categories (a second product doing the same job is an overlap) and stated priorities in those workloads, newest first (none: use the function closest to [What I sell]).
5. Count job postings from the last 12 months naming the competitor's product as a skill, by its skill name (e.g. CrowdStrike Falcon, not CrowdStrike); if 0, read 3 recent postings in the workload for the exact spelling and retry once.
6. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]; say here if [Company] owns a rival product.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: "Installed and active", "Detected at Low only (not counted)", "Installed but fading" or "Not detected in Draup", with the rating and the evidence.
- Table "Competitor footprint": Product | Usage strength | Last seen | Workloads | Rating.
- Table "Switch triggers" (rival) or "Openings" (otherwise), up to 3: Priority | Source and quarter | Likely owner | Why it opens a door.
- "How to win" (rival only): 3 bullets, each tied to a fact above: the wedge (overlap, new estate or subsidiary), who to start with, and the proof to bring.
- Detail: "Who else is in the room" (top 8: Product | Maker | Usage strength | Last seen); hiring evidence (or "none found"); Gaps (what Draup lacked, to ask in discovery).

RULES
- Frame by Relationship. Displace a rival. Never suggest displacing an adjacent tool; look for integration gaps. A platform we run on is a fit signal. Rate rivals only; others get "n/a".
- Active = High or Medium usage, seen in the last 12 months; Low = detected, not counted as present; no usage strength = "fading". "Not detected" is not proof they don't use it.
- Judge a sub-category by the product, not Draup's label (firewalls can sit under SIEM).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Rating: High usage in the workloads of What I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Is [Competitor] installed at [Company] at High or Medium usage? Rate it Red/Amber/Green, flag overlaps or a product [Company] owns, then 3 bullets on how to win.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run "Map the buying committee" on the workloads where [Competitor] sits.
```

```text
Find 10 more companies in the same industry whose stack includes [Competitor] products.
```

```text
Turn the "How to win" wedge into a 90-word email to the person in the next step.
```

```text
Run it again with Relationship set to adjacent tool and compare the openings.
```

## Tips for better results

- Set Relationship when the tool isn't a true rival. Datadog is adjacent for a data-observability seller, and a platform such as Snowflake is something you need in the stack, not something to replace.
- If the account makes a product in the same category, the verdict says so first: a company that owns its own tool rarely switches to yours.
- Draup sees tools through public evidence such as job ads. A tool that runs quietly in the background may show as Low or not at all.
- Hiring counts use the product's skill name ("CrowdStrike Falcon"), not the maker; a maker-name search can return a false 0.

## Related prompts

- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_account_priorities_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `tech-competitor-installed`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
