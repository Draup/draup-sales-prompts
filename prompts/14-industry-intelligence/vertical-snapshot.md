[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# One-page vertical market snapshot

> **A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are entering a vertical, building a territory plan, or need industry context for a pitch or a leadership review. | Sales Leader & RevOps, Marketing & ABM, Account Executive, Services, SI & Staffing Seller | Everyone | 4–6 min | Industry ecosystem |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Aerospace & Defense |
| `[Region (optional)]` | Europe, or North America |
| `[What I sell]` | PLM software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my industry analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Aerospace & Defense]
- Region (optional): [default: my territory from setup; e.g. Europe, or North America]
- What I sell: [one line, e.g. PLM software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical (a sub-industry with zeros: use its parent) and [Region] to Draup's names. If the region doesn't resolve, use Draup's nearest values (e.g. "Northern America" = US and Canada) and list their countries.
2. The vertical's revenue, IT spend and R&D spend, latest year, with growth (global totals).
3. The vertical's key priorities: pick the 5 that fit [What I sell], with dated proof from the 2 largest employers in [Region] in that function. If there are none, say so first and use those 2 employers' dated priorities, labelled "company proof, not industry-wide".
4. Top buyers: the 10 largest parents by workforce, primary vertical [Vertical], HQ in [Region], with revenue; count subsidiaries once. Total their revenue as the regional size. Flag any that sell what I sell. Rivals I named: note who runs them at High or Medium usage (ignore Low; say so).
5. Growing technologies: up to 5 relevant to [What I sell], or "none relevant in Draup".
6. Services sellers only: top outsourcing vendors (no agencies, staffing or research firms) and top 5 workloads, with active engagements (Draup-derived).
7. For the best-fit top buyer: its top 3 executives in that function and top 90-day news item. If it is a top-3 giant, also pick the best-fit mid-size buyer.

OUTPUT
- Bottom line: 2 sentences — the state of [Vertical] in [Region] and what it means for [What I sell].
- Recommended next step: a named person (name, full title), the action and a dated why-now; if missing, the title to find. Add the mid-size buyer if picked.
- "The numbers": Metric | Value ($B) | Growth % | Year: revenue, IT and R&D spend (global; "year not given" if omitted), then the top-10 buyers' revenue in [Region].
- "Top priorities": Priority | Dated proof (company, quarter) | Likely owner | Fit.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: top buyers (rivals present); growing technologies; outsourcing (services sellers); exclusions.

RULES
- Name any company that makes up over a third of a total.
- If a vertical total looks implausible (e.g. R&D under 0.1% of revenue), show it as "Draup figure, unverified".
- "Fit" is judgement (Draup ties no priority to a seller). Vertical lists are a fixed top 50; say so once.
- Flag off-vertical, sanctioned or state-owned buyers. IT spend tracks revenue, so its growth is no trend.
- No generic tools (office suites, chat assistants) in technology lists. If I ask for a slide: 5 bullets + 1 table.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: a one-page snapshot of [Vertical] in [Region]: global size and growth plus the top-10 buyers' regional revenue, the 5 priorities that fit [What I sell] with dated company proof, and who to call first.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the top 3 priorities into a 5-slide point of view for [What I sell].
```

```text
Which 10 companies in [Vertical] in [Region] hire most per 1,000 staff right now?
```

```text
Show the outsourcing league table for this vertical in [Region] (services sellers).
```

## Tips for better results

- Region defaults to your territory; the industry totals stay global, so read the top-10 buyers' revenue as the regional size.
- If one giant dominates a total (one retailer's R&D, say), the snapshot names it; discount the growth figure accordingly.
- The Fit column is the assistant's judgement, not a Draup score. Challenge it.

## Related prompts

- [Build an industry point of view](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.
- [Who wins services work in a vertical](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.
- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `ecosystem_get_vertical_revenue`, `ecosystem_get_vertical_it_spend`, `ecosystem_get_vertical_rnd_spend`, `ecosystem_get_vertical_key_priorities`, `get_account_priorities_v3`, `get_universe_companies_v3`, `ecosystem_get_vertical_techstack_growing`, `ecosystem_get_vertical_outsourcing_vendors`, `ecosystem_get_vertical_outsourcing_workloads`, `accounts_executives_key_executives_v3`, `get_top_signals`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `market-vertical-snapshot`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
