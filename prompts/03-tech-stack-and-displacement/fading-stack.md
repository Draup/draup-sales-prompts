[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Fading tools and replacement windows

> **The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Hunting for a renewal or migration window, or before a modernisation pitch. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 2–4 min | Tech stack, Priorities & opportunities, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Technology]` | data management |
| `[What I sell]` | data-platform migration services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my technology renewal and migration analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Technology: [area or workload, e.g. data management, cybersecurity]
- What I sell: [one line, e.g. data-platform migration services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the products in that area, up to 5 pages, and say which grouping you used.
3. Group each: Fading (no usage strength, or last seen over 12 months ago); Weakening (Low, last seen 6–12 months ago); Active (High or Medium, seen in the last 90 days); Stable (the rest, counted only). Cut-offs are editable defaults.
4. For each Fading or Weakening product, find Active products in the same sub-category: the likely successor or a parallel tool.
5. Pull products first detected in the last 12 months in those sub-categories.
6. Pull stated priorities in the function closest to [What I sell] about modernisation, migration, consolidation or cost, with source and fiscal quarter.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table "Replacement windows" (top 3): Product | Why now (successor, new arrival or priority, dated) | Likely owner | Opening for [What I sell].
- Table "Fading and weakening" (top 10, oldest first): Product | Maker | Last seen | Group | Read (Replaced, Parallel, Unclear).
- Detail: likely successors with usage strength; new arrivals; Stable count; Gaps (what Draup lacked, to ask in discovery).

RULES
- "Fading" is the strongest claim allowed. Never say they dropped, retired or cancelled a product.
- A last-seen date shared by many products is a data refresh; with Low strength it's weak evidence.
- If nothing is fading, say the area looks stable and lead the next step with a priority instead.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Which [Technology] tools at [Company] have gone quiet in Draup, what likely replaced each, and which 3 replacement windows suit [What I sell], each with a dated reason?
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top replacement window, run "Map the buying committee" on that workload.
```

```text
Show the full active stack in the same sub-categories, so I know what I'd integrate with.
```

```text
Draft a 90-word email to the person in the next step that opens on the migration window without naming the old vendor.
```

```text
Check whether the likely successor also appears in their job ads.
```

## Tips for better results

- Last-seen dates matter more than first-seen dates. A tool with no usage strength listed is one Draup no longer detects.
- Treat "fading" as a hypothesis to test in discovery, not a fact to put in an email.

## Related prompts

- [What they run in one tech area](../../prompts/03-tech-stack-and-displacement/stack-category.md): What they run in one area, ranked by how central each tool is, with your competitors rated Red, Amber or Green, stale tools set aside and a named person to call.
- [What tools they adopted this year](../../prompts/03-tech-stack-and-displacement/recent-adoptions.md): The tools first detected at the account in the last 12 months, labelled as competing with, complementing or unrelated to what you sell, with any new competitor product flagged Amber first and a named person to call.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_tech_stack_trend_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `tech-fading-stack`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
