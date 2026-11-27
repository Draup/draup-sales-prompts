[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which tools their job ads are building

> **The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press, with a named person to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Validating a technology priority, or looking for an early, non-obvious why-now in engineering, data and AI. | Account Executive, Presales & Solutions, SDR / BDR, Services, SI & Staffing Seller | Everyone | 2–4 min | Hiring & job postings, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | servicenow.com |
| `[What I sell]` | AI code-review and governance tooling |
| `[Business function (optional)]` | IT |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my hiring and stack-signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. servicenow.com]
- What I sell: [one line, e.g. AI code-review and governance tooling — skip if you ran the start-here prompt]
- Business function (optional): [e.g. IT or ER&D (engineering and R&D); blank uses the function closest to what I sell]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Pull the skills in the company's job postings over the last 12 months in the function: the top 50 plus those trending up. Keep named software tools only.
3. For each tool, compare average postings per month in the last 5 full months with the 5 before. Set aside one-off spikes (one month over half the total).
4. Pull the installed stack for the makers of the top 15 tools: usage strength, last seen, and whether first detected in the last 12 months. For very broad makers (Google, Microsoft, Amazon), also narrow by category. Say which tools you couldn't find.
5. Group each tool (editable defaults): New = 5 or fewer a month before, 20+ (or 5x) after; Building = rising in job ads but Low, absent or new in the stack; Core = in job ads and High or Medium in the stack; Coasting = High in the stack, under 5 postings in 12 months.
6. For the top 3 New or Building tools, pull 2 recent postings each: title, date, location.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] and [Company]'s top 90-day news item where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- Table (top 10, by recent volume): Tool | Avg/month, prior 5 | Avg/month, last 5 | In stack (strength) | Group.
- "What it signals": 3 bullets on the practice change, and the opening for [What I sell] with its likely owner.
- Detail: makers, first-detected flags and sample titles; rows 11–20; Gaps (to ask in discovery).

RULES
- Job-ad mentions measure hiring demand, not licences or spend; say so once.
- If nothing is New, say so and lead with Building.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the function closest to What I sell (e.g. IT) and say which; map any function I give to its main workloads and name them.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- If one company's posting count is in the millions or above its workforce, the company match failed. Say so and drop it.
- Trust last-seen date and usage strength. Ignore the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named owner, dated why-now). Which software tools appear in [Company]'s job ads this year, and how do they match its stack? Sort into New, Building, Core and Coasting.
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
Write a 70-word email to the person in the next step that opens on this practice shift.
```

```text
Which of these tools are made by my competitors?
```

## Tips for better results

- A tool that shows up in job ads before it shows up in the stack is often a project in its first months: a good time to engage.
- Big employers' company-wide results can be swamped by frontline hiring, so the prompt reads the function closest to what you sell unless you name another.

## Related prompts

- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.
- [What tools they adopted this year](../../prompts/03-tech-stack-and-displacement/recent-adoptions.md): The tools first detected at the account in the last 12 months, labelled as competing with, complementing or unrelated to what you sell, with any new competitor product flagged Amber first and a named person to call.
- [What they run in one tech area](../../prompts/03-tech-stack-and-displacement/stack-category.md): What they run in one area, ranked by how central each tool is, with your competitors rated Red, Amber or Green, stale tools set aside and a named person to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_hiring_job_postings_v3`, `get_account_tech_stack_products_v3`, `get_tech_stack_trend_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `signals-practice-shift`.

</details>

---

[Back to Signals and timing](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
