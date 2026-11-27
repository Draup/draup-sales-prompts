[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Where they're building teams

> **The metros where the account is adding people in one function, with capability centres and likely new sites called out, net hiring over a stated window, and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're planning where to expand inside a customer, or which regional team should own it. | Account & Customer Success Manager, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 2–4 min | Talent flow & locations, Hiring & job postings, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Business function]` | Supply Chain |
| `[What I sell]` | warehouse automation software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account-expansion analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [e.g. Supply Chain, IT, ER&D]
- What I sell: [One line, e.g. warehouse automation software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull key locations for [Business function]: metro, country, indicative workforce, 12-month postings, growth index and site tags (HQ, capability centre). Keep the top 10 by postings, plus every capability-centre row.
3. Infer likely new sites: metros with real postings but little or no workforce. Say they're inferred.
4. Pull net hiring by metro from talent flow (hires minus exits) and state the months covered.
5. People and timing: pull the top 3 leaders in [Business function], preferring those based in the fastest-growing metro, and the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — where they're building and where [What I sell] should land.
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Top metros": Metro | Tag | Postings (12 mo) | Growth index | Net hiring (window).
- "Why this matters for [What I sell]": 3 bullets on where to land or expand and which regional team should own it.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Capability centres and likely new sites" (Metro | Country | Tag or "inferred new" | Postings) and "Fastest growing" (3 metros with the highest growth index among those with 100+ workforce; editable default).

RULES
- Always run with one business function.
- Site workforce is approximate and varies between pulls; treat it as indicative and lean on postings.
- The growth index is postings divided by workforce, so it runs high for small sites; say so when one tops the list.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Label inferences (buyer role, intent, fit) "likely".
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 400 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Where is [Company] building [Business function] teams? Top 10 metros by 12-month postings with growth index, HQ or capability-centre tags, net hiring (state the window) and likely new sites.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run the same for [another Business function] and compare.
```

```text
Who are the leaders based in the fastest-growing metro?
```

```text
What roles are they hiring at the likely new site?
```

## Tips for better results

- A metro with fresh postings but little workforce is often the earliest sign of a team being built.
- Talent-flow numbers lag by a few months. Use job postings for the most recent picture.

## Related prompts

- [Their capability centres and the services play](../../prompts/10-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore sites): where, which functions, how fast they hire, likely new sites, a maturity read, the services play that fits, and who to call.
- [Which region should own this account](../../prompts/01-account-research/buying-center.md): Which region should own the pursuit, where to hold the first meeting and with whom, backed by revenue by region, top metros and where your function's leaders sit.
- [Who they lose talent to](../../prompts/11-account-planning/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_location_insights_key_locations_map_v3`, `accounts_talent_flow_insights_locations_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-expansion-footprint`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
