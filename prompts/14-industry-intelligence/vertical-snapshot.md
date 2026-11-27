[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# One-page vertical market snapshot

> **A one-page view of an industry, optionally scoped to your region: size and growth, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are entering a vertical, building a territory plan, or need industry context for a pitch or a leadership review. | Sales Leader & RevOps, Marketing & ABM, Account Executive, Services, SI & Staffing Seller | Everyone | 4–6 min | Industry ecosystem |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Aerospace & Defense |
| `[Region (optional)]` | Europe, or North America and Europe |
| `[What I sell]` | PLM and engineering-data software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my industry analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Aerospace & Defense]
- Region (optional): [e.g. Europe, or North America and Europe]
- What I sell: [one line, e.g. PLM and engineering-data software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name. A sub-industry (e.g. Airlines) can return zeros: use the parent and say so. Resolve [Region] to Draup's region names (e.g. Western, Northern, Southern and Eastern Europe) and show them.
2. Pull the vertical's revenue, IT spend and R&D spend for the latest year, with growth. These totals are global even when I give a region.
3. Pull the vertical's key priorities and pick the 5 most relevant to [What I sell]. Draup gives them no dates, so for the top 2 pull the dated priorities of the 2 largest employers (in [Region] if given) in that function and use those as proof.
4. Top buyers: list companies with primary vertical [Vertical] (HQ in [Region] if given), largest workforce first, top 10.
5. Pull growing technologies (fixed top 50); keep up to 5 relevant to [What I sell], or say "none relevant in Draup".
6. Services sellers only (from my setup or What I sell): top outsourcing vendors (no agencies, staffing, research or merchandising firms) and top 5 workloads, with active engagements (Draup-derived).
7. For the top buyer most relevant to [What I sell]: its top 3 executives in that function and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the state of [Vertical] and what it means for [What I sell].
- Recommended next step: a named person (name and full title from step 7), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "The numbers": Metric | Value ($B) | Growth % | Year ("latest, year not given" if omitted). Say the totals are global.
- "Top priorities": Priority | Dated proof (company, quarter) | Likely owner (title) | Fit (my judgement).
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: top buyers in [Region]; technology gaining ground (Technology | Companies adopting, window not stated); outsourcing (services sellers only); what you excluded.

RULES
- Draup marks every vertical priority as not tied to a seller, so "Fit" is your judgement; say so.
- Every vertical list is Draup's fixed top 50, not the whole market; say so once.
- Flag buyers whose business doesn't fit [Vertical], and sanctioned or state-owned firms where relevant.
- Vertical IT spend tracks revenue; don't present its growth as a separate trend.
- Leave generic tools (office suites, browsers, chat assistants, design tools) out of technology lists.
- If I ask for a slide: 5 bullets + 1 table.

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
Bottom line and next step first: a one-page snapshot of [Vertical] (in [Region] if given): size and growth, the 5 priorities that fit [What I sell] with dated company proof, the top buyers, and who to call first.
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
Show the outsourcing league table for this vertical (services sellers).
```

## Tips for better results

- Add a region to scope buyers and proof to your territory; the industry totals stay global.
- If a section comes back empty, it is usually the industry name. Ask Claude to try the parent industry.
- The Fit column is the assistant's judgement, not a Draup score. Challenge it.

## Related prompts

- [Build an industry point of view](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.
- [Who wins services work in a vertical](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.
- [Find where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, hubs that host both, where to focus, and a named person at the biggest local employer.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `ecosystem_get_vertical_revenue`, `ecosystem_get_vertical_it_spend`, `ecosystem_get_vertical_rnd_spend`, `ecosystem_get_vertical_key_priorities`, `get_account_priorities_v3`, `get_universe_companies_v3`, `ecosystem_get_vertical_techstack_growing`, `ecosystem_get_vertical_outsourcing_vendors`, `ecosystem_get_vertical_outsourcing_workloads`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-vertical-snapshot`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
