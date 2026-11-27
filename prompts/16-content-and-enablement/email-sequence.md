[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Industry email sequence

> **A ready-to-load 3-email sequence for one persona in one industry, each email built on a current industry priority and a dated real-company example.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're starting outbound into an industry and need a sequence grounded in what that industry is actually working on. | Marketing & ABM, SDR / BDR, Account Executive | Everyone | 2–4 min | Industry ecosystem, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Automotive |
| `[Persona]` | Head of Supply Chain Planning |
| `[Business function]` | Supply Chain |
| `[What I sell]` | supply-chain planning software |
| `[Proof point (optional)]` | cut forecast error at Fabrikam Foods |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for [Vertical]. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [industry, e.g. Automotive]
- Persona: [title, e.g. Head of Supply Chain Planning]
- Business function: [the persona's function, e.g. Supply Chain]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut forecast error at Fabrikam Foods]

STEPS
1. Match [Vertical] to Draup's industry name. If it returns zeros, say so and try the parent industry, naming it.
2. Pull the industry's current priorities and judge fit from each priority's text.
3. Pick the 3 closest to [Business function] and [What I sell]. If no category matches the function, use the nearest (for Supply Chain: Manufacturing, Procurement, Management & Strategy) and say so.
4. For each, find one named company in [Vertical] acting on it in the last 180 days, from the priority's examples or Draup's industry news (search first, then the news feed for links). The company must be the actor.

OUTPUT
- Bottom line: 2 sentences — the persona's top industry pressure and the angle the sequence takes.
- "Priorities used": Priority | Why it fits the persona | Company example (month, year, source).
- Email 1 (day 1): subject (7 words max) and body on priority 1.
- Email 2 (day 4): priority 2, using [Proof point] if given.
- Email 3 (day 9): priority 3, a short close-the-loop note.
- Each body: company example, the problem, one sentence on how [What I sell] helps, one low-effort call to action.
- Recommended next step: which [Vertical] accounts to load first, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- 120 words or fewer per body. Plain language, no hype, no emoji.
- Present examples as public industry moves, never as our customers.
- No example found: write on the priority alone and flag it. Claim no results beyond [Proof point].

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a name returns nothing, retry once with Draup's spelling and say which worked.
- Drop news noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Merge items about the same event and keep the earliest. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Write a 3-email sequence for a [Persona] in [Vertical], using the 3 Draup industry priorities closest to [Business function] and one dated company example per email. 120 words max each, with subject lines.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a version of email 1 for a CFO in the same industry.
```

```text
Give me two subject-line options for each email to A/B test.
```

```text
Turn priority 1 and its example into a short LinkedIn post for our company page. Check your Draup licence before publishing Draup data externally.
```

## Tips for better results

- Name the persona's function. Industry priorities span every department, and the sequence works best when they're the persona's own problems.
- Re-run it each quarter: industry priorities and the examples behind them change.

## Related prompts

- [Industry point of view for a pitch](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative and a one-line POV.
- [ABM messages for a target list](../../prompts/16-content-and-enablement/abm-messages.md): A table of short, personalised openers, 5 accounts per pass, each tied to one stated priority and one dated signal from the last 60 days, with sources and an optional partner or proof angle.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with the accounts worth touching.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry: revenue and spend, top priorities with likely owners, technologies gaining ground, and who outsources what to whom.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_key_priorities`, `build_news_filters_v3`, `get_signal_news_v3`, `get_news_feed_v3`

Status: **tested live**. Prompt id: `content-email-sequence`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
