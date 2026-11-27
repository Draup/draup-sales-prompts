# Where they're building teams

**The metros where the account is adding people in one function, with GCCs and likely new sites called out and net hiring over a stated window.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are planning where to expand inside a customer, or which regional team should own it. | Account & Customer Success Manager, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 2–4 min | Talent flow & locations, Hiring & job postings |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Business function]` | Supply Chain |
| `[What I sell]` | warehouse automation software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my account-expansion analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [e.g. Supply Chain, IT, ER&D]
- What I sell: [One line, e.g. warehouse automation software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull key locations for [Business function]: metro, country, indicative workforce, 12-month postings, growth index and site tags (HQ, GCC). Keep the top 10 by postings, plus every GCC row.
3. Infer likely new sites: metros with real postings but little or no workforce. Say they are inferred.
4. Pull net hiring by metro from talent flow (hires minus exits) and state the months covered.

OUTPUT
- Bottom line: 2 sentences — where they are building and where [What I sell] should land.
- "Top metros": Metro | Country | Tag | Postings (12 mo) | Growth index | Indicative workforce | Net hiring (window). By postings.
- "GCCs and likely new sites": Metro | Country | Tag or "inferred new" | Postings (12 mo).
- "Fastest growing": 3 metros with the highest growth index among those with 100+ workforce (editable default).
- "Why this matters for [What I sell]": 3 bullets on where to land or expand and which regional team should own it.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Always run with one business function.
- Site workforce is approximate and varies between pulls; treat it as indicative and lean on postings.
- The growth index is postings divided by workforce, so it runs high for small sites; say so when one tops the list.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Talent-flow data ends about 3 months ago; state the months covered.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Where is [Company] building [Business function] teams? Top 10 metros by 12-month postings with growth index, HQ/GCC tags, indicative site size and net hiring (state the window), plus likely new sites.
```

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

- [Global capability centres (GCCs) and the services play](../../prompts/06-outsourcing-and-services/gcc-opportunity.md): The account's global capability centres (company-owned offshore or captive sites): where, which functions, how fast they hire, likely new sites, and whether build-operate-transfer (BOT), centre-of-excellence (CoE) expansion or managed services fits.
- [Which region should own this account](../../prompts/01-account-research/buying-center.md): Which region and metros hold the revenue, people and decision makers for your function, which region should own the pursuit, and where to hold the first meeting.
- [Talent rivals: who they lose people to](../../prompts/08-account-planning-and-expansion/talent-competitors.md): The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, and credible peers to benchmark against.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_location_insights_key_locations_map_v3`, `accounts_talent_flow_insights_locations_v3`

Status: **tested live**. Prompt id: `plan-expansion-footprint`.

</details>

[Back to Account planning and expansion](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
