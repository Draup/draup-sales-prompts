[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Pick the SI to co-sell with

> **A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell software and want a systems integrator (SI) already inside the account to open or speed up a deal. Use "Which providers to partner with or replace" instead when you want the partner-or-displace play for every priority, and "Joint account plan with a partner" once you've picked the partner. | Partnerships & Alliances, Account Executive, Presales & Solutions | Software sellers | 2–4 min | Outsourcing deals, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Workload or business function]` | Data Engineering |
| `[Technology]` | Snowflake |
| `[What I sell]` | Snowflake-native data observability software |
| `[Our current partners (optional)]` | Tailspin Partners |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner and alliances manager. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Workload or business function: [e.g. Data Engineering, or IT — I'll map a function to its main workloads]
- Technology: [Our product or platform as Draup names it, e.g. Snowflake]
- What I sell: [One line, e.g. Snowflake-native data observability software — skip if you ran the start-here prompt]
- Our current partners (optional): [e.g. Tailspin Partners]

STEPS
1. Find the company by its website (no match: retry once by name, show match and score) and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on. Note its primary industry.
2. If I gave a business function, map it to the 1–3 workloads closest to [What I sell] and say which.
3. Pull the top 10 providers in those workloads at the account, leaving out agencies and staffing firms, and each one's total engagements at the account. Show "in workload / total".
4. For the top 5 (plus current partners in the top 10), pull relationship tier and delivery locations.
5. Pull the top 10 providers whose engagements involve [Technology] in the account's primary industry, worldwide.
6. Check the account's whole tech stack for [Technology] and other products by its maker: usage strength and last seen.
7. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the partner to call first and why.
- Recommended next step: a person from step 7 (name and title), what to do (with or through the partner), and the dated why-now (or say none).
- "Shortlist": Partner (current partners marked) | In workload / total | Tier | [Technology] engagements in industry | Verdict.
- Verdict: Lead co-sell (here in the workload and [Technology]-skilled), Access partner (here, little [Technology]), Skills partner ([Technology]-skilled, not here) or Skip. Current partners first.
- "Call first": one partner, three reasons tied to numbers.
- "Is [Technology] already there?": installed (strength, last seen) or not seen — expand or land.
- Gaps: what Draup lacked; ask in discovery.

RULES
- If [Technology] returns nothing, retry with the vendor or product family name and say which worked.
- A strategic tier means access and possibly loyalty to a rival product; note it, don't assume it.
- Never rank partners on whole-account counts; a firm big elsewhere in the account may do none of this work.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: full profile titles and professional information only, checked against the function; flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? List them and ask. Leadership data lags about 3 months.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each), reference tables under "Detail"; about 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Which providers deliver [Workload] at [Company] (engagements in that work vs total), which have [Technology] experience in its industry, and which one do I call first?
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a short note to [Partner]'s account lead proposing a joint approach to the person in the next step.
```

```text
Which other accounts in [Vertical] does [Partner] serve in [Workload]?
```

```text
Build a joint account plan for [Company] with [Partner].
```

## Tips for better results

- The best co-sell partner is usually already inside the account in your workload, even if it isn't the biggest provider overall.
- Ask for the partner's other accounts in the industry to build a joint pipeline, not just one deal.

## Related prompts

- [Which providers to partner with or replace](../../prompts/10-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-cosell-partner`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
