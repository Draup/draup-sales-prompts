[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Employer-brand gaps for an RPO pitch

> **How a company scores as an employer against its hiring rivals, its three weakest areas from employee reviews, and RPO or employer-branding angles.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You sell RPO, recruitment marketing or employer-branding services and need a data-led reason to start the conversation. | Services, SI & Staffing Seller, Account Executive, Marketing & ABM | Services sellers | 2–4 min | Talent cost & supply |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | costco.com |
| `[Hiring rivals]` | target.com, walmart.com |
| `[Location (optional)]` | United States of America |
| `[What I sell]` | RPO and employer-branding services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my talent-acquisition services strategist. Use the Draup for Talent connector for employer-value scores, and the Draup for Sales connector for company facts, executives and news. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [website, e.g. costco.com]
- Hiring rivals: [up to 3 companies it competes with for hires, e.g. target.com, walmart.com]
- Location (optional): [country or metro for location-level scores, e.g. United States of America]
- What I sell: [one line, e.g. RPO and employer-branding services; skip if saved in setup]

CONTEXT (optional)
A gap against a named hiring rival opens more doors than an absolute score. Frame it constructively: this analysis may reach the client, and talent leaders respond to opportunities, not criticism.

STEPS
1. Find [Company] and each rival by website and confirm the parent company. If a website returns nothing, look it up by name once and show the match and its score; if it still fails, tell me and carry on.
2. For each, pull the employer-value scores: overall index, employee reviews analysed, and every pillar and sub-pillar score. Use [Location] scores if given; otherwise company-wide.
3. Find [Company]'s 3 weakest pillars: the lowest scores and the biggest gaps behind the rival average.
4. For each weak pillar, summarise the review themes in your own words (2–3 themes each).
5. Pull [Company]'s top 3 executives in Human Resources (prefer talent acquisition or the CHRO) and its most important news item from the last 90 days (hiring drives, new sites, layoffs).

OUTPUT
- Bottom line: 2 sentences — where [Company] trails its hiring rivals and the RPO angle that follows.
- Recommended next step: an opening line for the person named from step 5 (name and title), framed on one gap against a named rival, with the dated why-now. If none is found, say so.
- Table: Pillar | [Company] | Rival average | Gap. Worst gap first, top 6.
- "Weakest 3": Pillar | Gap | What employees say (themes) | The RPO angle for [What I sell].
- Detail: scores per rival and sub-pillar; reviews analysed and scope (company-wide or [Location]).
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Mark any company with fewer than 200 reviews analysed as low confidence (editable default), and don't build the opening line on it.
- Paraphrase review themes. Never quote or identify individual reviewers.
- Keep the tone constructive: frame gaps as opportunities.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: where [Company] trails [Hiring rivals] as an employer — overall index, reviews analysed, the 3 weakest pillars with review themes — and the RPO angle and person to open with for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show how hard it is for [Company] to hire its top 3 roles in [Location].
```

```text
Turn this into a 5-slide outline for an RPO discovery meeting.
```

```text
Which pillar is [Company] strongest on, so we can acknowledge it first?
```

## Tips for better results

- Compare against named hiring rivals. A gap against a known rival usually opens more doors than an absolute score.
- Pair this with hiring difficulty: a weak employer brand plus hard-to-hire roles makes the strongest RPO case.

## Related prompts

- [Roles the client can't hire: staffing pitch](../../prompts/17-talent-cost-and-location/hard-to-hire.md): Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.
- [Who they lose talent to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `Account_Candidate_Attraction`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **documented, not live-tested**. Prompt id: `talent-employer-brand`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
