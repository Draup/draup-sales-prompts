[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# 3-email sequence for one industry persona

> **A ready-to-load 3-email sequence for one persona in one industry, each email built on a priority in the persona's function and a dated move by a real company, plus the first account to load with a named contact.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're starting outbound into an industry and need a sequence grounded in what that industry is working on. Use the ABM openers prompt instead when you already have a named account list. | Marketing & ABM, SDR / BDR, Account Executive | Everyone | 2–4 min | Industry ecosystem, News signals, Executives & movement, Priorities & opportunities |

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
- Territory (optional): [HQ country or region, e.g. Germany; blank uses my saved territory]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut forecast error at Fabrikam Foods]

CONTEXT (optional)
A sequence lands when every email is about the persona's own problem and carries proof that a peer is acting on it. Industry priorities give themes but no dates; proof must come from named, dated companies.

STEPS
1. Match [Vertical] to Draup's industry name and map [Business function] to its 1–3 main workloads; say which. If the industry returns zeros, say so and try the parent industry, naming it.
2. Pull the industry's priorities and judge fit from each priority's text.
3. Pick the 3 closest to [Business function] and [What I sell]. If no priority sits in the function, use the nearest (for Supply Chain: Manufacturing, Procurement, Management & Strategy) and say so.
4. For each, find one named company in [Vertical] acting on it in the last 180 days: first the priority's own examples; if they carry no date, pull the dated [Business function] priorities of 2–3 of the industry's largest parent employers in [Territory] (company list sorted by total workforce), then industry news (search, then the feed for links). The company must be the actor.
5. Name the first account to load: the company behind the strongest dated example (or the largest in [Territory] if none). Pull its top 3 executives in [Business function] and pick the closest match to [Persona].

OUTPUT
- Bottom line: 2 sentences — the persona's top industry pressure and the angle the sequence takes.
- Recommended next step: the first account to load, who to send it to (name and title from step 5), and the dated example. If none, say so.
- Email 1 (day 1): subject (7 words max) and body on priority 1.
- Email 2 (day 4): priority 2, using [Proof point] if given.
- Email 3 (day 9): priority 3, a short close-the-loop note.
- Each body: company example, the problem, one sentence on how [What I sell] helps, one low-effort call to action.
- Detail: "Priorities used": Priority | Why it fits the persona | Company example (month, year, source).
- Gaps: what Draup lacked, to ask in discovery.

RULES
- 120 words or fewer per body. Plain language, no hype, no emoji.
- Present examples as public industry moves, never as our customers.
- No example found: write on the priority alone and flag it. Claim no results beyond [Proof point].

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alikes and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. Flag conflicting or single-source figures as unverified.
- Never return a blank table: say what came back empty and use the fallback.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 500 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: a 3-email sequence (120 words each, with subjects) for a [Persona] in [Vertical], on 3 [Business function] priorities, each with a dated company example, plus the first account to load.
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
List 10 more accounts in [Vertical] to load, each active in [Business function] hiring.
```

```text
Turn priority 1 and its example into a short LinkedIn post for our company page. Check your Draup licence before publishing Draup data externally.
```

## Tips for better results

- Name the persona's function. Industry priorities span every department, and the sequence works best when they're the persona's own problems.
- Re-run it each quarter: industry priorities and the examples behind them change.

## Related prompts

- [Build an industry point of view](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative, a one-line POV and a named first contact.
- [ABM openers for 10 accounts at once](../../prompts/16-content-and-enablement/abm-messages.md): A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.
- [One-page vertical market snapshot](../../prompts/14-industry-intelligence/vertical-snapshot.md): A one-page view of an industry scoped to your region: global size and growth beside a regional size from the top 10 buyers, the priorities that fit what you sell with dated company proof, the top buyers, and who to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_key_priorities`, `ecosystem_get_vertical_organization_top_employers`, `get_account_priorities_v3`, `build_news_filters_v3`, `get_signal_news_v3`, `get_news_feed_v3`, `accounts_executives_key_executives_v3`, `get_universe_companies_v3`

Status: **tested live**. Prompt id: `content-email-sequence`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
