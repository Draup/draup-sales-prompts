[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Brief reps on a new industry

> **A rep-ready brief on an industry you're entering: the words to use, what it funds in your function, who buys and how the function is organised at a lead account, where your rivals already sit, the services firms you'll meet and 5 discovery questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Onboarding reps to a new industry, launching a vertical team, or preparing a sales kick-off session. Use the industry point-of-view prompt when you need a narrative for customers rather than a brief for your team. | Sales Leader & RevOps, Account Executive, SDR / BDR, Presales & Solutions | Everyone | 4–6 min | Industry ecosystem, Executives & movement, Outsourcing deals, Tech stack, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Energy & Utilities |
| `[Reference account]` | nationalgrid.com |
| `[Business function]` | IT |
| `[What I sell]` | asset-data and field-service modernisation services |
| `[My competitors (optional)]` | IBM Maximo, Accenture |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales enablement lead building a vertical playbook. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Energy & Utilities]
- Reference account: [website of a typical target, e.g. nationalgrid.com]
- Business function: [where we sell, e.g. IT]
- What I sell: [one line, e.g. asset-data and field-service modernisation services — skip if you ran the start-here prompt]
- My competitors (optional): [rival products or firms, e.g. IBM Maximo, Accenture — skip if you ran the start-here prompt]

CONTEXT (optional)
Reps new to an industry lose credibility fast if they don't speak its language or know who owns what. Teach the words, what it funds and how buying is organised, with one real account as the example.

STEPS
1. Use Draup's exact industry and function names; map What I sell to its workloads. Find the reference account by website (parent company). If the industry returns zeros, try its parent and name it.
2. Pull industry priorities; keep the 6 most relevant to [What I sell] in [Business function], plus 2 from other functions that shape the budget (examples undated).
3. From the priority text, pick 10 industry terms a rep must know and define each in one line.
4. Pull growing technologies (a fixed top 50). Drop generic tools (office suites, chat assistants, design tools, browsers, social networks); keep up to 8 and mark my competitors' products.
5. Pull the top outsourcing vendors (a fixed top 50). Drop agencies, staffing, inspection and engineering-only firms unless they matter; keep 8 and mark my competitors.
6. At the reference account: pull executives in [Business function] (10 per page, up to 2 pages) and read full titles to see how the function is organised; check its stack for my competitors' products with usage strength; pull its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — what this industry buys and what it means for [What I sell].
- Recommended next step: the enablement action, its owner and a date; then a first call at [Reference account] with a named person (name and title from step 6) and the dated news fact. If none is found, say so.
- "What they're funding": Priority | What it means for [What I sell] | Company example (undated). Top 6.
- "Who buys": Title pattern | Likely role (economic buyer, technical buyer, champion) | Example title at [Reference account], plus one line on how the function is organised.
- Detail: 10 words to know; technology in play with rival ratings; services firms we'll meet; 5 discovery questions with what a good answer sounds like; a 60-word first-call opener.
- Gaps: what Draup didn't have — worth asking in discovery.
- Slide version (only if I ask): 5 bullets, each with one dated number, plus 1 table.

RULES
- In the brief, use titles as patterns; name people only in the next step.
- Industry priorities are undated themes, not news.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- Rivals: High usage in my workloads is Red, Medium Amber, newly detected Amber; unchecked is "present (usage not checked)". Ignore "Generic" rows.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 500 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: brief my reps on [Vertical] for [What I sell] — 10 terms, the top priorities in [Business function], buyer titles at [Reference account], rivals in play and 5 discovery questions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this into a 10-question quiz for the reps.
```

```text
Redo "Who buys" with [Second reference account] to check the pattern holds.
```

```text
Write a 3-email sequence for the economic-buyer title in this brief.
```

```text
Which of the services firms listed are partners we could recruit?
```

## Tips for better results

- Pick a reference account that looks like your typical target, not the largest company in the industry.
- Read the full titles: in many regulated industries IT is organised by business line, which changes who your rep should call.
- Refresh the brief each half-year; priorities shift faster than reps expect.

## Related prompts

- [Build an industry point of view](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry, optionally scoped to your region: size and growth, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [3-email sequence for one industry persona](../../prompts/16-content-and-enablement/email-sequence.md): A ready-to-load 3-email sequence for one persona in one industry, each email built on a priority in the persona's function and a dated move by a real company, plus the first account to load with a named contact.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_account_id`, `ecosystem_get_vertical_key_priorities`, `ecosystem_get_vertical_techstack_growing`, `ecosystem_get_vertical_outsourcing_vendors`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `leaders-vertical-enablement`.

</details>

---

[Back to Sales leadership and RevOps](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
