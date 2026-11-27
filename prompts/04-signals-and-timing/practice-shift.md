[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What their job ads say about their stack

> **The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Validating a technology priority, or looking for an early, non-obvious why-now in engineering, data and AI. | Account Executive, Presales & Solutions, SDR / BDR, Services, SI & Staffing Seller | Everyone | 2–4 min | Hiring & job postings, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | servicenow.com |
| `[Business function]` | IT (optional) |
| `[What I sell]` | AI code-review and governance tooling |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my hiring and stack-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. servicenow.com]
- Business function: [optional, e.g. IT or ER&D]
- What I sell: [one line, e.g. AI code-review and governance tooling — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the skills in the company's job postings over the last 12 months (in [Business function] if given): the top 50 plus those trending up. Keep named software tools only.
3. For each tool, compare average postings per month in the last 5 full months with the 5 before. Set aside one-off spikes (one month over half the total).
4. Pull the installed stack for the makers of the top 15 tools: usage strength, last seen, and whether first detected in the last 12 months. For very broad makers (Google, Microsoft, Amazon), also narrow by category (e.g. data management, DevOps), because a maker-only pull can miss tools. Say which tools you couldn't find.
5. Group each tool (editable defaults): New = 5 or fewer a month before, 20+ (or 5x) after; Building = rising in job ads but Low, absent or new in the stack; Core = in job ads and High or Medium in the stack; Coasting = High in the stack, under 5 postings in 12 months.
6. For the top 3 New or Building tools, pull 2 recent postings each: title, date, location.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table (top 20, by recent volume): Tool | Maker | Avg/month, prior 5 | Avg/month, last 5 | In stack (strength, first detected) | Group | Sample title.
- "What it signals": 3 bullets on the practice change behind the numbers.
- "Why this matters for [What I sell]": the opening and its likely owner.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Job-ad mentions measure hiring demand, not licences or spend; say so once.
- If nothing is New, say so and lead with Building.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Trust last-seen date and usage strength. Ignore the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Keep to about 340 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which software tools appear in [Company]'s job ads over the last 12 months, and how do they match its installed stack? Sort them into New, Building, Core and Coasting, with the last 5 full months against the 5 before.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show 3 full job descriptions for the top New tool so I can quote the responsibilities.
```

```text
Has anyone senior been hired into this area recently? Check executive moves in the matching workload.
```

```text
Write a 70-word email that opens on this practice shift.
```

## Tips for better results

- A tool that shows up in job ads before it shows up in the stack is often a project in its first months: a good time to engage.
- Run it with the IT or ER&D function for big employers. Company-wide results can be swamped by frontline hiring.

## Related prompts

- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings and talking points.
- [What they adopted this year](../../prompts/03-tech-stack-and-displacement/recent-adoptions.md): The tools first detected at the account in the last 12 months, each labelled as competing with, complementing or unrelated to what you sell, with any competitor product called out first.
- [Their stack in one category](../../prompts/03-tech-stack-and-displacement/stack-category.md): What they run in one category, ranked by how actively each tool is used, with stale tools set aside, unfamiliar products explained and an optional vendor ranking with a consolidation read.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_hiring_job_postings_v3`, `get_account_tech_stack_products_v3`, `get_tech_stack_trend_v3`

Status: **tested live**. Prompt id: `signals-practice-shift`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
