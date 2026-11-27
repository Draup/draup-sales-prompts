[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Enablement brief for a partner's sellers

> **A brief you hand to a partner's sales team: where your product fits their practice in your industry, which of their customers run your platform or a rival's, a joint value proposition, 5 qualification questions and 3 objection handlers.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| After a partner agreement is signed, before a joint enablement session or a partner sales kickoff. | Partnerships & Alliances, Marketing & ABM, Presales & Solutions | Software sellers | 4–6 min | Outsourcing deals, Company directory, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Partner]` | Infosys |
| `[Vertical]` | Banking & Financial Services |
| `[Platform]` | Snowflake |
| `[Competitor]` | Databricks |
| `[What I sell]` | data observability for Snowflake |
| `[Proof point (optional)]` | cut data-incident time 40% at a mid-size retailer |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner enablement lead. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Partner: [Services firm as Draup spells it, e.g. Infosys]
- Vertical: [Draup industry, e.g. Banking & Financial Services]
- Platform: [The technology our product runs on or with, as Draup names its maker, e.g. Snowflake]
- Competitor: [Rival maker, e.g. Databricks]
- What I sell: [One line, e.g. data observability for Snowflake; skip if saved in setup]
- Proof point (optional): [e.g. cut data-incident time 40% at a mid-size retailer]

STEPS
1. Confirm Draup's spelling of each input; say which you used.
2. Pull the partner's customer summary: active customers, engagements and top customers overall.
3. Pull the partner's top 10 workloads and top 10 customers in primary industry [Vertical].
4. Pull the partner's [Vertical] customers ranked by engagements that mention [Platform] (top 10): its practice evidence.
5. List the partner's [Vertical] customers whose stack includes [Platform] products (10, by revenue), then those of them with no [Competitor] products (10).
6. A customer in step 3 or 4 that also appears in step 5 is a warm start.
7. People and timing: page through [Partner]'s Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances, partnerships or [Platform]; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
(Written to the partner's sellers, as "you".)
- Bottom line: 2 sentences — where [What I sell] fits their [Vertical] practice and the first 3 customers to raise it with.
- Recommended next step: a person from step 7 (name and title), what I (the partner manager) do, and the dated why-now; if none, say so.
- "Where to start" (up to 10): Customer | Your engagements in [Vertical] | Your [Platform]-related engagements | Stack: [Platform] only, both, or not seen | Play.
- Play: Expand (you already do [Platform] work there), Land ([Platform] present, no [Competitor], little [Platform] work by you), Coexist (both makers present: position alongside).
- "5 qualification questions": Question | What a good answer sounds like.
- Gaps: what Draup didn't have — worth confirming with the partner.
- Detail: why this fits your practice (3 bullets on their workload numbers); joint value proposition (60 words, [Proof point] once); 3 objection handlers (Objection | Response under 40 words | Proof); how to bring us in (routing line).

RULES
- Platform presence is public evidence; confirm before quoting.
- These are outside-in facts; never imply a customer told us.
- Leave catch-all workloads out of "Why this fits".
- Under 10 [Platform]-related engagements (editable)? Call the practice early and lead with Land plays.
- Check our Draup licence before sharing Draup data outside the company.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Trust usage strength and last-seen date, not confidence or first-seen; ignore "Generic" rows; a rival counts only at High or Medium usage.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 500 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and first 3 customers first. Enablement brief for [Partner]'s sellers in [Vertical]: their workloads and customers, who runs [Platform] (with or without [Competitor]), a joint pitch, 5 qualification questions, 3 objection handlers.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the brief into a 5-slide outline for the enablement session.
```

```text
Write a 90-second talk track a partner seller can use on a customer call.
```

```text
Build a joint account plan for the top warm-start customer with [Partner].
```

## Tips for better results

- Lead with the partner's own customers and workloads. Partner sellers skim past vendor-centric decks.
- Keep the brief to what a seller can use on the next call; save the deep data for the partner manager.

## Related prompts

- [Joint account plan with a partner](../../prompts/13-partners-and-alliances/joint-account-plan.md): A one-page plan you and a partner can both sign up to for one account: where the partner already works in your function, the priorities there, your technology's and a rival's position, who to meet and a 90-day plan with owners on both sides.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`accounts_customers_summary_v3`, `get_deals_workloads_v3`, `get_deals_customer_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `partners-enablement-brief`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
