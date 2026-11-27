[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

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
| `[Company]` | walmart.com |
| `[Hiring rivals]` | amazon.com, target.com |
| `[Location (optional)]` | India |
| `[What I sell]` | RPO and employer-branding services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my talent-acquisition services strategist. Use the Draup for Talent connector for employer-value scores, and the Draup for Sales connector for company lookups. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. walmart.com]
- Hiring rivals: [up to 3 companies it competes with for hires, e.g. amazon.com, target.com]
- Location (optional): [country or metro for location-level scores, e.g. India]
- What I sell: [one line, e.g. RPO and employer-branding services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] and each rival by website and confirm the parent company. Tell me if a rival can't be found and carry on.
2. For each, pull the employer-value scores: overall index, employee reviews analysed, and every pillar and sub-pillar score. Use [Location] scores if given; otherwise company-wide.
3. Find [Company]'s 3 weakest pillars: the lowest scores and the biggest gaps behind the rival average.
4. For each weak pillar, summarise the review themes in your own words (2–3 themes each).

OUTPUT
- Bottom line: 2 sentences — where [Company] trails its hiring rivals and the RPO angle that follows.
- Header: [Company], overall index, reviews analysed, scope (company-wide or [Location]).
- Table: Pillar | [Company] | each rival | Rival average | Gap. Worst gap first.
- "Weakest 3": Pillar | Score | Gap | What employees say (themes).
- "The RPO angle": per weak pillar, one line on how [What I sell] would help (candidate experience, employer messaging, sourcing reach, offer competitiveness).
- Recommended next step: an opening line for the head of talent acquisition, framed around one gap against a named rival, and why now.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Mark any company with fewer than 200 reviews analysed as low confidence (editable default), and don't build the opening line on it.
- Paraphrase review themes. Never quote or identify individual reviewers.
- Keep the tone constructive: frame gaps as opportunities, since this may reach the client.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Company]'s Draup employer-value scores with [Hiring rivals]: overall index, reviews analysed, pillar scores, the 3 weakest pillars with review themes, and RPO angles for [What I sell].
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

- [Hard-to-hire roles: staffing pitch](../../prompts/17-talent-cost-and-location/hard-to-hire.md): Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.
- [Talent rivals: who they lose people to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, and credible peers to benchmark against.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `Account_Candidate_Attraction`

Status: **documented, not live-tested**. Prompt id: `talent-employer-brand`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
