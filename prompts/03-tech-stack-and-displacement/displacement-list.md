# Displacement target list

**A sized, revenue-ranked list of companies in your industry and country whose stack includes a competitor's products, confirmed in the same pass, with likely-inactive and misfiled names set aside.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Launching a competitive-replacement campaign or building an SDR list. | SDR / BDR, Marketing & ABM, Sales Leader & RevOps, Account Executive | Everyone | 4–6 min | Company directory, Tech stack |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | Snowflake |
| `[Vertical]` | Retail |
| `[Country]` | United States of America |
| `[Minimum employees]` | 5,000 |
| `[What I sell]` | lakehouse data platform |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my competitive list-building analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [vendor or product, e.g. Snowflake]
- Vertical: [Draup industry, e.g. Retail, Life Sciences]
- Country: [HQ country in full, e.g. United States of America]
- Minimum employees: [e.g. 5,000]
- What I sell: [one line, e.g. lakehouse data platform — skip if you ran the start-here prompt]

STEPS
1. Turn my industry and country into Draup's exact names; say which you used. If the industry returns zeros, try its parent industry and name it.
2. List only companies whose tech stack includes [Competitor] products, showing which ones: primary industry [Vertical], HQ in [Country], at least [Minimum employees] staff, by revenue, highest first. For a product, filter by its maker and keep rows showing it.
3. Count by paging, 10 companies per page (each row is large), until a page returns fewer than 10.
4. Say how many matches lack a workforce figure: run the list once without the size limit, showing companies with no workforce figure first (10 rows). Give the count, or "10+" if all 10 lack one, and name any well-known ones.
5. Show the top 15. Each row's stack is the confirmation; give usage strength and last seen where shown.
6. Check news for the top 5 only. Move rows clearly outside the industry (e.g. distributors) to a separate list.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Table: Rank | Company | HQ city | Workforce | Revenue (USD M, FY) | Draup-estimated IT spend (USD M, FY) | Opportunity Index | [Competitor] products (strength, last seen) | Flag.
- "Possibly inactive or misfiled": Company | Reason.
- "Missing size data": count.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Draup's Opportunity Index score is Draup's own rating of how strong the sales opportunity is (higher is stronger); use it to order, not to quote.
- Don't rank on IT spend; for many companies it is modelled from revenue.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Use primary industry only, sort largest first, and flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- Count by paging (the quick count ignores technology conditions). Stop after 5 pages and report the total so far with a plus.
- Show USD millions using Draup's conversion rate. If Draup gives no rate, name the rate and date and mark it as outside Draup.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Keep to about 320 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
List [Vertical] companies headquartered in [Country] with [Minimum employees]+ staff whose tech stack includes [Competitor] products, showing which ones. Count by paging, show the top 15 by revenue, and flag possibly inactive or misfiled companies.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the next 15 in the same way.
```

```text
For the top 5, what stated priorities could justify a switch?
```

```text
Write a 2-sentence opener for each of the top 5, each tied to one fact.
```

## Tips for better results

- Ask for the count by paging; the quick count ignores the technology condition.
- Industry lists can include some defunct or misfiled companies. Check the flag column before sending the list to SDRs.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.
- [Size a vendor's install base](../../prompts/03-tech-stack-and-displacement/vendor-install-base.md): What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion.
- [Build and size an ICP list](../../prompts/05-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `build_company_filters_v3`, `get_universe_companies_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `tech-displacement-list`.

</details>

[Back to Tech stack and displacement](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
