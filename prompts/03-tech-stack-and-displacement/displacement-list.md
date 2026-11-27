[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Target list: companies running a competitor

> **A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Launching a competitive-replacement campaign or building an SDR list. | SDR / BDR, Marketing & ABM, Sales Leader & RevOps, Account Executive | Everyone | 4–6 min | Company directory, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | Snowflake |
| `[Vertical]` | Retail |
| `[Territory (optional)]` | United States of America — defaults to your territory from setup |
| `[Minimum employees]` | 5,000 |
| `[What I sell]` | lakehouse data platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive list-building analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [vendor or product, e.g. Snowflake]
- Vertical: [industry, e.g. Retail, Life Sciences]
- Territory (optional): [HQ country or region in full, e.g. United States of America; default: my territory from setup]
- Minimum employees: [e.g. 5,000]
- What I sell: [one line, e.g. lakehouse data platform — skip if you ran the start-here prompt]

STEPS
1. Turn my industry and territory into Draup's exact names; say which you used. If the industry returns zeros, try its parent industry and name it.
2. List only companies whose tech stack includes [Competitor] products: primary industry [Vertical], HQ in [Territory], at least [Minimum employees] staff, largest workforce first (sort by total workforce). For a product, filter by its maker and keep rows showing it. Parent companies only: merge subsidiaries and the same company under different names.
3. Count by paging this exact list, 10 per page, until a page returns fewer than 10. The total must apply every filter. Label it "detected at any usage": the list shows presence, not usage.
4. For the top 10, check usage with one stack lookup each, filtered to the maker. Count a company as running [Competitor] only at High or Medium; list Low-only rows as "detected, not counted".
5. Separately, run the list once without the size limit, companies with no workforce figure first (10 rows), and report how many lack size data (or "10+"). Never mix this into the total.
6. Flag distributors, wholesalers and resellers, possibly inactive companies and rows clearly outside the industry, and offer to exclude them.
7. For the top-ranked company at High or Medium, pull the top 3 executives in the function closest to [What I sell] and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Include the true count and how many of the top 10 run it at High or Medium.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10): Rank | Company | Workforce | [Competitor] products (usage strength) | Flag.
- Detail: revenue (USD M, fiscal year) and Opportunity Index for the same rows; the next 5; "Detected at Low only"; "Flagged" (Company | Reason); "Missing size data": count; Gaps (what Draup lacked, to ask in discovery).

RULES
- Opportunity Index is Draup's own rating of how strong the sales opportunity is (higher is stronger); use it to order, not to quote.
- Don't rank on IT spend; for many companies it is modelled from revenue.
- Low usage everywhere means the competitor is present but not central; say so in the bottom line and don't count those rows.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Rank within [Territory] only. Use primary industry only. Flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- Counts must apply every filter. The quick count ignores technology conditions, so count by paging; stop after 5 pages and report the total so far with a plus.
- Show USD millions using Draup's conversion rate. If Draup gives no rate, name the rate and date and mark it as outside Draup.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit the company, and keep it out of drafted copy.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (named person, dated why-now). How many [Vertical] parent companies in [Territory] with [Minimum employees]+ staff run [Competitor]? Top 10 with usage strength; count only High or Medium; flag distributors.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the next 10 in the same way, distributors excluded, with usage checked.
```

```text
For the top 5, what stated priorities could justify a switch?
```

```text
Write a 2-sentence opener for each of the top 5, each tied to one dated fact.
```

```text
Re-rank the list by Opportunity Index to find reachable mid-size accounts.
```

## Tips for better results

- The total is counted with every filter applied and labelled "detected at any usage"; the top 10 are then checked for High or Medium usage. If the list looks small, lower the minimum size or widen the territory.
- Leave Territory blank to use the one saved in "Tell your AI about you"; without a territory the list ranks the whole world.
- Retail and consumer lists often include distributors and wholesalers; the flag column lets you drop them before the list goes to SDRs.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.
- [Size a vendor's install base](../../prompts/03-tech-stack-and-displacement/vendor-install-base.md): What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion, with a named person at the vendor or a first target to approach.
- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `get_universe_companies_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `tech-displacement-list`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
