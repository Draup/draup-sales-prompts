[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Spot scale-up and cost-out buyers

> **Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and a named person to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You pitch scale or cost takeout and want companies under growth strain or cost pressure. | SDR / BDR, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | Industry ecosystem, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Banking & Financial Services |
| `[Country (optional)]` | United States of America |
| `[What I sell]` | managed IT operations and automation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Banking & Financial Services]
- Country (optional): [HQ country in full, e.g. United States of America]
- What I sell: [one line, e.g. managed IT operations and automation services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull Draup's fastest-growing-workforce and biggest-decline lists for the vertical (each a fixed top 50). In the decline list, "attrition" is the % change in workforce.
3. Keep only [Country] HQs if given. Split each list at 1,000 employees (editable).
4. For the 10 largest shrinking 1,000+ companies, run one news search (last 12 months) for acquisitions, mergers, closures, bankruptcies, layoffs and restructuring.
5. Move merged or closed companies to "Absorbed or defunct"; give the rest a dated reason or "no news found".
6. For the best-fit company on each side: its top 3 executives in the function closest to What I sell.

OUTPUT
- Bottom line: 2 sentences — who needs scale, who needs cost-out, and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Growing (1,000+)", top 10: Company | Current workforce | Growth % | Likely buyer title.
- "Shrinking (1,000+, independent)", top 10: Company | Current | Change % | Likely reason (date).
- "What to pitch": 2 bullets for growers (scale, enablement), 2 for shrinkers (cost takeout, automation).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: previous workforce figures; smaller companies (names and % only); "Absorbed or defunct" with date.

RULES
- State Draup's comparison period, or "period not stated".
- Never call a decline a layoff without a dated news item; don't lead with small companies' huge percentages.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: [Vertical] companies with the fastest workforce growth and the biggest declines (1,000+ staff), with mergers and closures checked, the pitch angle for each side and who to call first.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Check the next 10 shrinking companies the same way.
```

```text
For the top 3 shrinking companies, who runs IT and Finance now?
```

```text
Write a cost-takeout opener for the #1 shrinking company citing its news.
```

## Tips for better results

- Shrinking lists can include firms that were merged away. Confirm before you call.
- Percentages for small companies swing widely. Treat them as leads to verify.

## Related prompts

- [Find the fastest revenue growers](../../prompts/06-prospecting-and-lists/revenue-growth-screen.md): The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside, a shortlist growing both revenue and headcount, and who to call first.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_organization_increasing_workforce`, `ecosystem_get_organization_decreasing_workforce`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-growth-and-cost-out`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
