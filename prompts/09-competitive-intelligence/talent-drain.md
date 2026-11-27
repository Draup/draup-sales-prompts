[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Where a rival's people are going

> **Who a competitor loses people to and hires from, its workforce trend, the clients absorbing its staff (a sign of insourcing or delivery strain) and the named person to talk to at the most exposed client.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a displacement pitch, or when a rival's delivery quality or stability is your angle. | Services, SI & Staffing Seller, Account Executive, Sales Leader & RevOps, Partnerships & Alliances | Everyone | 2–4 min | Talent flow & locations, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | cognizant.com |
| `[What I sell]` | application modernisation and managed services |
| `[Region]` | United States (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence analyst for workforce signals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. cognizant.com]
- What I sell: [one line, e.g. application modernisation and managed services — skip if you ran the start-here prompt]
- Region (optional): [country or metro, e.g. United States]

CONTEXT (why this matters)
A rival losing people faster than it hires, or to its clients, is under delivery pressure.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Pull talent flow by company, by people lost, 25 rows ([Region] if given). Remove its subsidiaries, "Self Employed" and blanks.
3. If the region result looks almost the same as global, say the region may not have applied and show global; if its top row is under 25 people, say the region is too thin and show global.
4. Split rows into Rival vendors (services firms, software vendors, consultancies) and End clients (companies that buy from [Competitor]). Net flow = hired from minus lost to.
5. Pull the monthly workforce trend (hires, exits, net, total) for the same window.
6. Search news for [Competitor] leadership moves and layoffs (6 months); mark the most important from the last 90 days.
7. For the top end client absorbing staff (or else the top end client in the list), find it by name and pull its top 3 executives in the function closest to [What I sell] (one page of 10) and its most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the pressure on [Competitor] and what it means for [What I sell]. Add the window: "Talent flow for [months], [region or global]".
- Recommended next step: a named person (name, full title) at the most exposed end client, the action this week and the dated why-now (or say none).
- Table "Loses people to" (top 10): Company | Type (rival vendor, end client) | Lost | Hired from | Net.
- Table "Monthly trend" (last 6 full months): Month | Hires | Exits | Net; then one line on direction.
- "Clients absorbing their staff": end clients with 50+ people lost to and few hired back (editable default), each with a likely read (insourcing, rebadging, new captive).
- "Leadership changes" (6 months, up to 5) and "How to use this": 3 bullets.
- Detail: net winners against them (top 3) and the full monthly trend with workforce.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Counts are people moves Draup observed in the window, not total headcount or attrition rates.
- Never tell a client that [Competitor] is losing staff on their account; use it to shape questions. Label inferences "likely".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Talent flow ends about 3 months ago and the last month undercounts exits; state the months.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Where are [Competitor]'s people going? Lead with the bottom line and a named person at the client most likely absorbing its staff, then who it loses talent to and hires from, and monthly hires vs exits.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [End client], show its outsourcing providers and [Competitor]'s engagements there.
```

```text
Which job families is [Competitor] losing most in [Region]?
```

```text
Write 3 discovery questions on delivery continuity I can ask the named executive.
```

## Tips for better results

- End clients high in the lose-to list are often your best displacement targets.
- Pair this with "A rival's footprint and your wedge" for the client it flags.

## Related prompts

- [Who they lose talent to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_talent_flow_insights_companies_v3`, `accounts_talent_flow_workforce_trends_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `compete-talent-drain`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
