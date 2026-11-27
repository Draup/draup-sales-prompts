[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Battlecard: rival software vendor

> **A one-page internal battlecard on a rival software vendor: its most-used products, the largest companies running them, recent moves, how to beat it and the objection to expect.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A software rival keeps showing up in your deals, or you're preparing a team for a competitive pursuit. | Account Executive, Presales & Solutions, Marketing & ABM | Software sellers | 4–6 min | Tech stack, Company directory, Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | snowflake.com or Google BigQuery |
| `[What I sell]` | cloud data-warehouse platform |
| `[Vertical (optional)]` | Automotive |
| `[Where we lose to them (optional)]` | lost Contoso Retail on bundled pricing |
| `[Proof we can cite (optional)]` | Fabrikam Foods migrated off a legacy warehouse in one quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive analyst for software deals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [rival vendor's website or product, e.g. snowflake.com or Google BigQuery]
- What I sell: [one line, e.g. cloud data-warehouse platform — skip if you ran the start-here prompt]
- Vertical (optional): [e.g. Automotive]
- Where we lose to them (optional): [paste win/loss notes, e.g. lost on bundled pricing]
- Proof we can cite (optional): [e.g. Fabrikam Foods left a legacy warehouse in one quarter]

STEPS
1. Find [Competitor] by website and confirm the parent, not a subsidiary or brand. If I named a product, note its maker and use the maker. If unclear, ask me.
2. Pull HQ, workforce, latest revenue and growth, and their top 5 products by companies using them.
3. In one list, pull the 10 largest companies (by workforce) whose tech stack includes [Competitor] products, in primary industry [Vertical] if given. Flag subsidiaries.
4. For the top 5, check the whole tech stack for any product made by [Competitor], whatever area it's filed under.
5. Search Draup's news on them (last 180 days), then the news feed for links. Review 30+ items.

OUTPUT
- Bottom line: 2 sentences — how entrenched they are and where [What I sell] can win.
- "What they sell most": Product | Companies using it. Top 5.
- "Where they're installed": Rank | Company | Industry | Workforce | Their products | Usage strength | Last seen | Likely owner. Largest first.
- "Recent moves": up to 6 rows, Date | Move | Source | Why it matters.
- "How we win": 3 angles tied to facts above and [Proof we can cite]; one landmine.
- "Where we lose": a counter for each pattern in my notes, if given.
- "Trap questions": 3 discovery questions that surface their weak spots without naming them.
- "Objection to expect": their likely claim and a one-line, data-backed reply.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Mark product columns for rows 6–10 "not checked".
- Mark the card "Internal use". Claim no results beyond [Proof we can cite].

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Tech stack: trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Show USD millions using Draup's conversion rate and show the original currency once. If Draup gives no rate, name the rate and date and mark it as outside Draup.
- Drop news noise: outages and breaches (unless I sell security), stock chatter, charity, sponsorships and awards, passing mentions, look-alike names, sister companies, and old stories re-dated as new (use the event date in the text). Merge items about the same event and keep the earliest. Give the source and headline for every item, plus the link when Draup has one.
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Build an internal Draup battlecard on software rival [Competitor]: top 5 products by install count, the 10 largest companies running them, 180 days of moves, three ways [What I sell] wins and three trap questions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Check rows 6–10 product by product and add usage strength and last-seen dates.
```

```text
Which of my target accounts run [Competitor]? Check [Accounts], 5 at a time.
```

```text
Turn 'How we win' into a one-page objection-handling sheet for SDRs.
```

## Tips for better results

- If your rival is a product inside a bigger company (a cloud database, say), name the product. Claude records the maker and checks every product it makes.
- Last-seen date matters more than the install count: a product not seen recently may be on its way out.

## Related prompts

- [Battlecard: rival services firm](../../prompts/09-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers, what it wins, recent moves, how to beat it, trap questions and the objection to expect.
- [Size a vendor's install base](../../prompts/03-tech-stack-and-displacement/vendor-install-base.md): What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.
- [Displacement target list](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A sized, revenue-ranked list of companies in your industry and country whose stack includes a competitor's products, confirmed in the same pass, with likely-inactive and misfiled names set aside.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_account_key_solution_offerings_v3`, `get_universe_companies_v3`, `get_account_tech_stack_products_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `get_news_feed_v3`

Status: **tested live**. Prompt id: `content-battlecard-product`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
