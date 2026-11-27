[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Carve balanced territories by geography

> **An industry-and-country account list, counted first, cleaned of holding and private-equity firms, and split into territories by HQ region, then balanced to within 10% on Draup-estimated IT spend, revenue or count.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Advanced: annual territory planning or when a new rep joins; best run by RevOps or a sales leader. Use plan-propensity-tiering instead to rank a list you already own. | Sales Leader & RevOps | Everyone | 4–6 min | Company directory |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[Country]` | United States of America |
| `[Minimum employees]` | 10000 |
| `[Number of territories]` | 3 |
| `[Balance on (optional)]` | revenue |
| `[Accounts already owned (optional)]` | metlife.com, allstate.com |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my RevOps territory planner. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Country: [HQ country in full, e.g. United States of America]
- Minimum employees: [e.g. 10000]
- Number of territories: [e.g. 3]
- Balance on (optional): [Draup-estimated IT spend (default), revenue or account count]
- Accounts already owned (optional): [Websites to exclude, e.g. metlife.com]

STEPS
1. Confirm Draup's names for the industry and country.
2. Count first: companies whose primary industry is [Vertical], HQ in [Country], with [Minimum employees]+ staff. If more than 100, stop and ask me to raise the threshold.
3. Pull them 10 at a time, largest first by the balance measure: HQ metro, employees, revenue, Draup-estimated IT spend.
4. Remove accounts already owned (match by website). Remove non-operating holding companies, conglomerates and private-equity or investment firms, and list them. Flag misfiled companies (HQ or description doesn't fit) and possibly inactive ones.
5. Group accounts by HQ region (e.g. Northeast, Southeast, Central, West; or metros if there are more than 4 territories). Assign whole regions to territories, then move single accounts only if a territory is more than 10% off balance; list every move.
6. Count companies of the same size and country that have [Vertical] only as a secondary industry; list up to 5 that genuinely operate in it as "Consider adding". Don't assign them.

OUTPUT
- Bottom line: 2 sentences — universe size and how even the split is.
- Recommended next step: who on my team does what, by when (e.g. "RevOps lead reviews the moves with the three regional managers this week"). No account why-now needed.
- "Territory summary": Territory | Regions and main metros | Accounts | Total (USD M, fiscal year) | Share.
- "Moves for balance": each single account moved, from and to, and why.
- Gaps: what Draup didn't have — worth checking in our CRM.
- Detail: one table per territory (Account | HQ metro | Employees | Revenue | IT spend); "Removed" (holding, private-equity, owned); "Consider adding"; "Data flags" (misfiled, possibly inactive, no IT spend so placed by revenue, how many matches lack size data).

RULES
- Size limits drop companies with no workforce figure (often large private firms or mutuals); report how many and offer to include them.
- IT spend is a Draup estimate, often modelled from revenue, so balancing on it is close to balancing on revenue; say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first. Count [Vertical] companies (primary industry) headquartered in [Country] with [Minimum employees]+ staff, drop owned, holding and private-equity firms, and split the rest into [Number of territories] territories by HQ region, balanced within 10%.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Rebalance on account count instead.
```

```text
Add Draup's Opportunity Index score and show the top 5 per territory.
```

```text
Tier each territory's accounts by fit to what we sell.
```

```text
Export the assignments as a table I can paste into a spreadsheet.
```

## Tips for better results

- Geography comes first so each rep gets a coherent patch; balance is then fixed with a few named moves you can argue about.
- Large suppliers whose main industry is different won't appear in the main list. Check "Consider adding".
- Balancing on spend favours fairness of opportunity; balancing on count favours fairness of workload. Pick one.

## Related prompts

- [Tier my accounts by fit and timing](../../prompts/11-account-planning/propensity-tiering.md): Up to 25 accounts scored 0–100 on fit to what you sell (hiring in your workloads, installed competitors) and timing (news, hiring, growth), tiered A, B or C with a spread you can act on, and the driver behind each score.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`build_company_filters_v3`, `get_universe_companies_v3`, `universe_get_entity_first_nlp_res`, `get_universe_companies_count`

Status: **tested live**. Prompt id: `plan-territories`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
