[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Quarterly competitor watch for the team

> **A one-page quarterly report on up to 3 rivals: a side-by-side scorecard including hiring in your space, each one's top moves and leadership changes, three team actions and a named account contact for the biggest threat.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| At the start of each quarter, for a team meeting or sales kick-off. Use this for up to 3 rivals side by side; use "What a rival did this quarter" to go deep on one. | Sales Leader & RevOps, Marketing & ABM, Presales & Solutions, Partnerships & Alliances | Everyone | 6–10 min | News signals, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitors]` | capgemini.com, cognizant.com, accenture.com |
| `[What I sell]` | cloud and data managed services |
| `[Quarter]` | last 90 days (optional) |
| `[Last report]` | paste last quarter's scorecard (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence lead writing the quarterly team briefing. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitors: [up to 3 websites, e.g. capgemini.com, cognizant.com, accenture.com]
- What I sell: [one line, e.g. cloud and data managed services — skip if you ran the start-here prompt]
- Quarter (optional): [default last 90 days]
- Last report (optional): [paste last quarter's scorecard to compare]

CONTEXT (why this matters)
Same lenses per rival; a rival adding roles in my space is coming for my deals.

STEPS
1. Find each competitor by website and confirm name, HQ and website (if one doesn't resolve, retry once by name and show the match and score). If I gave more than 3, do the first 3 and offer to continue.
2. For each, pull the quarter's news plus one targeted customer-wins search. Review 20+ items per rival; keep the top 5 by importance to [What I sell].
3. For each, pull the 12-month hiring timeline: last 5 full months vs the 5 before, Growing (+10% or more), Flat or Cutting (−10% or more), editable defaults. A month that jumps over 2x and stays may be a data-coverage change; flag it.
4. For each, pull 12-month postings in the 1–3 workloads closest to [What I sell], with trend.
5. Note dated leadership changes; if I pasted last quarter's scorecard, mark what changed.
6. Pick three team actions tied to dated moves.
7. From the named win most relevant to [What I sell], find the account by website and confirm its HQ and industry (if its executives look like look-alikes, use the next win and say so); pull its top 3 executives in the function closest to [What I sell].

OUTPUT
- Bottom line: 2 sentences — the biggest threat this quarter and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the account in the strongest rival win, the action this week and the dated why-now (or say none).
- Table "Scorecard": Rival | Top move (dated) | Hiring overall (% change) | Hiring in my space | Change vs last report.
- Table "Team actions next quarter" (3): Action | Owner role | Trigger move (dated).
- Per rival: "So what for us", one line, plus its top 3 moves.
- "Patterns" (2 bullets) and "Watch list" (3: unclosed deals, leaders in transition).
- Detail: each rival's top 5 moves (Date | Move | Source) and counts of deals, M&A and leadership changes.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Scorecard counts come only from items that survived the noise rule; say how many were reviewed per rival.
- Label unclosed acquisitions "announced".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If I ask for a slide: 5 bullets + 1 table.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 500 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Quarterly watch on up to 3 [Competitors]. Lead with the biggest threat and a named person at the account it touches. Then a scorecard (top move, hiring overall and in my space), top moves per rival and 3 team actions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the scorecard into a slide-ready table and 3 speaker notes.
```

```text
Deep-dive the strongest move with "How a rival's strategy is shifting".
```

```text
Draft a 150-word note to the sales team with the 3 actions. (Check your Draup licence before sharing Draup data outside your company.)
```

## Tips for better results

- Save the scorecard each quarter and paste it next time; the change column is what leaders read.
- Three rivals per run keeps it fast; split bigger lists across runs.

## Related prompts

- [What a rival did this quarter](../../prompts/09-competitive-intelligence/recent-moves.md): The few moves a competitor made in the last 90 days that change your deals (customer wins, partnerships, launches, deals and leadership), the accounts to defend or attack, and the named person to call at the top one.
- [How a rival's strategy is shifting](../../prompts/09-competitive-intelligence/strategy-shift.md): How a competitor's stated priorities moved across its last three earnings calls, the acquisitions, leaders and cuts behind each shift, what changes in your deals and who to brief.
- [Weekly industry signal digest](../../prompts/04-signals-and-timing/vertical-digest.md): A one-screen digest of the week's material moves in one industry, grouped by theme, with source counts, the accounts worth touching and a named person at the best one.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_signal_news_v3`, `build_news_filters_v3`, `accounts_hiring_timeline_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `compete-quarterly-watch`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
