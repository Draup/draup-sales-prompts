# Industry point of view for a pitch

**The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative and a one-line POV.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need a 'why this, why now' story for an industry keynote, campaign or first meeting. | Marketing & ABM, Account Executive, Presales & Solutions, Sales Leader & RevOps | Everyone | 2–4 min | Industry ecosystem |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Automotive |
| `[Audience]` | VP Supply Chain |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my industry marketing strategist. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Automotive]
- Audience: [The persona, e.g. VP Supply Chain]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull the vertical's key priorities. If none come back, use the stated priorities of the vertical's 3 largest companies and say so.
3. Choose by relevance yourself: the 5 priorities that best fit [What I sell] and [Audience]'s function. Function labels may not match the audience exactly, so judge by what each priority describes, and explain each choice in one line.
4. For each chosen priority, keep the named company examples with date or quarter.
5. For market context, pull the vertical's revenue and R&D growth and the 3 fastest-growing technologies relevant to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the industry story and why [What I sell] fits it now.
- "Top 5 priorities": # | Priority | Company examples (date) | Likely owner (title) | Why it matters to [Audience] | Why chosen.
- "5-slide narrative": for each slide, a title, 3 bullets and one dated proof point. Slide 1: the market shift (growth and technology adoption). Slides 2–4: the three strongest priorities. Slide 5: why [What I sell] now.
- "One-line POV": 35 words or fewer.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Use only Draup facts and company examples. Never invent statistics or quotes.
- IT spend tracks revenue in Draup; don't use its growth as a separate trend in the narrative.
- Company examples are real public companies; present them as industry evidence, never as our customers.

STANDARD RULES (leave as is)
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- Leave generic tools (browser add-ons, office suites, chat assistants, design tools) out of technology lists.
- Label anything you infer (buyer title, intent, fit) as "likely".
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Pick the 5 [Vertical] priorities most relevant to [What I sell] for a [Audience], each with dated company examples, and turn them into a 5-slide narrative plus a 35-word POV.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this into a 3-email sequence for [Audience], 120 words or fewer each, each with one dated company example.
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

- [One-page vertical market snapshot](../../prompts/07-vertical-intelligence/vertical-snapshot.md): A one-page view of an industry: revenue and spend, top priorities with likely owners, technologies gaining ground, and who outsources what to whom.
- [Industry email sequence](../../prompts/09-content-and-enablement/email-sequence.md): A ready-to-load 3-email sequence for one persona in one industry, each email built on a current industry priority and a dated real-company example.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with the accounts worth touching.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_key_priorities`, `ecosystem_get_vertical_revenue`, `ecosystem_get_vertical_rnd_spend`, `ecosystem_get_vertical_techstack_growing`, `ecosystem_get_vertical_organization_top_employers`, `get_key_account_priorities`

Status: **tested live**. Prompt id: `market-industry-pov`.

</details>

[Back to Industry and market intelligence](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
