[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Accounts a partner can open for you

> **A sized list of companies in your industry and country where a named partner already delivers work and your product (or a rival's) isn't in the stack, with how deep the partner is at the top 5 and a named buyer at the best one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a joint pipeline review, a partner business plan or a co-marketing campaign, when you need accounts the partner can open for you. | Partnerships & Alliances, Account Executive, Sales Leader & RevOps, Marketing & ABM | Software sellers | 4–6 min | Company directory, Outsourcing deals, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Partner]` | Accenture |
| `[Vertical]` | Retail |
| `[Country]` | United States of America |
| `[Not installed]` | Databricks |
| `[What I sell]` | lakehouse analytics platform for retailers |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner pipeline analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Partner: [Services firm as Draup spells it, e.g. Accenture]
- Vertical: [Draup industry, e.g. Retail]
- Country: [HQ country in full, e.g. United States of America]
- Not installed: [Maker whose products must be absent: ours, or a rival's, e.g. Databricks]
- What I sell: [One line, e.g. lakehouse analytics platform for retailers — skip if you ran the start-here prompt]

STEPS
1. Turn the partner, industry, country and maker into Draup's exact names; say which you used.
2. Size the list: companies with primary industry [Vertical], HQ in [Country], [Partner] among their engaged providers, and no product made by [Not installed] anywhere in the stack. Using the names-only view, check whether a 50th, 100th and 250th match exists to band the total (under 50, 50–99, 100–249, 250+).
3. Run the same band check once without the [Not installed] condition, labelled as such, so I can see what share of [Partner]'s base here already runs [Not installed].
4. Pull the top 10 matches in full, by revenue: workforce, revenue, Opportunity Index, other providers, parent.
5. Flag: Subsidiary (name the parent), Misfiled, Possibly inactive. List private companies without revenue that are larger than the 5th row under "Large private companies".
6. For the top 5 unflagged rows, pull [Partner]'s engagement detail: workloads, engagements (how many in workloads matching [What I sell]), tier and locations.
7. People and timing: at the top unflagged account, pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — how much pipeline exists and which account to raise with [Partner] first.
- Recommended next step: a person from step 7 (name and title), what to do (raised with [Partner]'s client lead for that account), and why now (the dated news item or another dated fact); if none turned up, say so.
- Header line: "[Band] companies match; without the [Not installed] condition, [band]." One line on what the difference implies.
- "Pipeline" (top 10): Rank | Company | Revenue (USD M, FY) | Other providers (3) | Flag.
- "Partner depth" (top 5): Company | [Partner] engagements (in my workloads / total) | Tier | Depth | Joint angle for [What I sell].
- Depth: Deep (5+ engagements, or any in a workload that matches [What I sell]), Light (1–4); editable defaults.
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: workforce, Opportunity Index, parent; "Large private companies".

RULES
- "No [Not installed] products" means Draup sees no public evidence of them; present it as a hypothesis to confirm with the partner, not proof.
- Judge depth on engagements, not the tier label; one small engagement can carry a "Strategic" tier.
- If fewer than 10 match, widen the country to its region, and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named buyer, dated why-now) first. Which [Vertical] companies in [Country] use [Partner] and show no [Not installed] products? Band the total, show the top 10 by revenue and the partner's depth at the top 5.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show rows 11–20 the same way.
```

```text
For the top 3, what stated priorities in data and analytics could justify a joint pitch?
```

```text
Draft a one-page joint account list I can send to [Partner]'s alliance team (check our Draup licence first).
```

## Tips for better results

- If the list is small or full of mid-size names, the big accounts probably already run the excluded maker. That's useful for the partner conversation too.
- Lead the partner review with accounts where the partner works in a workload next to yours; that's where an introduction is credible.

## Related prompts

- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of companies in your industry and country whose stack includes a competitor's products, with usage strength shown, distributors and inactive names flagged, and a named person at the top account.
- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Joint account plan with a partner](../../prompts/13-partners-and-alliances/joint-account-plan.md): A one-page plan you and a partner can both sign up to for one account: where the partner already works in your function, the priorities there, your technology's and a rival's position, who to meet and a 90-day plan with owners on both sides.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_universe_companies_v3`, `get_outsourcing_engagement_details`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `partners-sourced-pipeline`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
