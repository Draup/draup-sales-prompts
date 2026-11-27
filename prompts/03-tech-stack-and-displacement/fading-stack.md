# Fading stack: replacement windows

**The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement pitches.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Hunting for a renewal or migration window, or before a modernisation pitch. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 2–4 min | Tech stack, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Technology]` | data management |
| `[What I sell]` | data-platform migration services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my technology renewal and migration analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Technology: [category or workload, e.g. data management, Cybersecurity]
- What I sell: [one line, e.g. data-platform migration services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the products in that category or workload, up to 5 pages.
3. Group each: Fading (no usage strength, or last seen over 12 months ago); Weakening (Low, last seen 6–12 months ago); Active (High or Medium, seen in the last 90 days); Stable (the rest, counted only). Cut-offs are editable defaults.
4. For each Fading or Weakening product, find Active products in the same sub-category: the likely successor or a parallel tool.
5. Pull products first detected in the last 12 months in those sub-categories.
6. Pull stated priorities here about modernisation, migration, consolidation or cost, with source and fiscal quarter.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table "Fading and weakening" (top 15, oldest first): Product | Maker | Sub-category | Last seen | Group | Likely successor (strength) | Read: Replaced / Parallel / Unclear.
- Table "Replacement windows" (top 3): Product | Reason (successor, new arrival or priority, dated) | Likely owner | Opening for [What I sell].
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- "Fading" is the strongest claim allowed. Never say they dropped, retired or cancelled a product.
- A last-seen date shared by many products is a data refresh; with Low strength it's weak evidence.
- If nothing is fading, say the area looks stable.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Keep to about 320 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Which [Technology] products at [Company] have gone quiet in Draup (no usage strength, or not seen in 12 months)? For each, show the active product that likely replaced it, and name 3 replacement windows with a dated why-now.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top replacement window, who owns that workload? Map the buying committee.
```

```text
Show the full active stack in the same sub-categories, so I know what I'd integrate with.
```

```text
Draft a 90-word email that opens on the migration window without naming the old vendor.
```

## Tips for better results

- Last-seen dates matter more than first-seen dates. A tool with no usage strength listed is one Draup no longer detects.
- Treat "fading" as a hypothesis to test in discovery, not a fact to put in an email.

## Related prompts

- [Their stack in one category](../../prompts/03-tech-stack-and-displacement/stack-category.md): What they run in one category, ranked by how actively each tool is used, with stale tools set aside, unfamiliar products explained and an optional vendor ranking with a consolidation read.
- [What they adopted this year](../../prompts/03-tech-stack-and-displacement/recent-adoptions.md): The tools first detected at the account in the last 12 months, each labelled as competing with, complementing or unrelated to what you sell, with any competitor product called out first.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_tech_stack_trend_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `tech-fading-stack`.

</details>

[Back to Tech stack and displacement](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
