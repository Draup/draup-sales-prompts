[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Build an industry point of view

> **The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need a 'why this, why now' story for an industry keynote, campaign or first meeting. | Marketing & ABM, Account Executive, Presales & Solutions, Sales Leader & RevOps | Everyone | 2–4 min | Industry ecosystem |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Automotive |
| `[Audience]` | VP Supply Chain |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my industry marketing strategist. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [industry, e.g. Automotive]
- Audience: [the persona, e.g. VP Supply Chain]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull the vertical's key priorities. If none come back, use the stated priorities of its 3 largest employers and say so.
3. Choose the 5 priorities that best fit [What I sell] and [Audience]'s function. Judge by what each describes, since function labels may not match the audience, and explain each choice in one line.
4. Draup's vertical priorities carry no dates. For each chosen priority, keep the named company examples, then pull the dated priorities of 2–3 of the vertical's largest employers in that function and use those as proof (company, quarter or month).
5. Market context: the vertical's revenue and R&D growth, and the 3 fastest-growing technologies relevant to [What I sell]; if none qualify, say "Not in Draup" rather than listing generic tools.
6. For the company behind the strongest proof: its top 3 executives in [Audience]'s function and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the industry story and why [What I sell] fits it now.
- Recommended next step: a named person (name and full title from step 6), the action and one dated why-now fact; if Draup has neither, say so and name the title to find.
- "Top 5 priorities": # | Priority | Dated proof | Likely owner (title) | Why it matters to [Audience].
- "5-slide narrative": per slide a title, 3 short bullets and one dated proof point. Slide 1: the market shift. Slides 2–4: the three strongest priorities. Slide 5: why [What I sell] now.
- "One-line POV": 35 words or fewer.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: why each priority was chosen; growth figures with year (or "year not given").

RULES
- Use only Draup facts and company examples. Never invent statistics or quotes.
- Company examples are real public companies; present them as industry evidence, never as our customers.
- IT spend tracks revenue in Draup; don't use its growth as a trend.
- If an industry returns zeros, say so, retry with its parent and name it.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every number; write "Not in Draup" for gaps and never fill them from memory.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: pick the 5 [Vertical] priorities that fit [What I sell] for a [Audience], each with dated proof from named companies, then a 5-slide narrative and a 35-word POV.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this into a 3-email sequence for [Audience], 120 words or fewer each, each with one dated example.
```

```text
Which 10 [Vertical] companies are most active on priority #1?
```

```text
Make a version for a CFO audience.
```

## Tips for better results

- Name a specific persona in Audience. 'VP Supply Chain' gives sharper picks than 'executives'.
- Check your Draup licence before publishing Draup data externally, for example in a keynote or blog.

## Related prompts

- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry, optionally scoped to your region: size and growth, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.
- [3-email sequence for one industry persona](../../prompts/16-content-and-enablement/email-sequence.md): A ready-to-load 3-email sequence for one persona in one industry, each email built on a priority in the persona's function and a dated move by a real company, plus the first account to load with a named contact.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_key_priorities`, `ecosystem_get_vertical_organization_top_employers`, `get_account_priorities_v3`, `ecosystem_get_vertical_revenue`, `ecosystem_get_vertical_rnd_spend`, `ecosystem_get_vertical_techstack_growing`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `market-industry-pov`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
