[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Win plan against a rival

> **How entrenched a named rival is at the account (rated Red, Amber or Green), the pitch they'll likely make, your wedge, three landmine questions and the named person to align with first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A specific rival is in a live deal with you, as incumbent or the other finalist. Use this for one live deal; use "Is a competitor installed?" instead for a quick check before you pitch. | Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | Tech stack, Outsourcing deals, Hiring & job postings, Priorities & opportunities, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | medtronic.com |
| `[Competitor]` | Databricks (product or services firm) |
| `[Area in the deal]` | Data Engineering (or a function like IT; optional) |
| `[Deal stage]` | shortlist of two (optional) |
| `[What I sell]` | cloud data-platform software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive deal strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. medtronic.com]
- Competitor: [software or services rival, e.g. Databricks or Accenture]
- Area in the deal (optional): [workload or function, e.g. Data Engineering or IT]
- Deal stage (optional): [e.g. shortlist of two]
- What I sell: [one line, e.g. cloud data-platform software — skip if you ran the start-here prompt]

CONTEXT (why this matters)
One deal, not a battlecard.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Map [Area in the deal], or the function closest to [What I sell], to 1–3 workloads; say which.
3. Footprint. Software rival: whole-stack check for its products (strength, last seen, countries). Services rival: active engagements (Draup-derived; never outsourced headcount), tier, workloads, delivery locations.
4. Skills pull (hiring by skill): 12-month count and monthly trend of postings naming [Competitor]'s main product as a skill, in its skill spelling (e.g. CrowdStrike Falcon, not CrowdStrike); if 0, read 3 recent postings in the workload for the spelling and retry once. Note metros.
5. Who else is in the room: High and Medium products in the workloads, or a services rival's top 10 providers.
6. Priorities: up to 5 in the workloads, else the function, else say none (never borrow).
7. People: one page of 10 executives in the workloads; flag skills or past employers tied to [Competitor].
8. News, 12 months: partnerships, vendor selections, hiring plans, any [Company]–[Competitor] announcement; mark the top 90-day item.

OUTPUT
- Bottom line: 2 sentences — the rating and our best path.
- Recommended next step: a named person (name, full title) to align with, the action this week and the dated why-now.
- Table "Rival footprint" (up to 8): Product or engagement | Usage or tier | Last seen | Where.
- Table "Landmines" (3): Question or proof point | What it exposes | When to use it.
- "Their likely pitch": 3 bullets tied to account facts.
- "Our wedge": 2–3 areas where evidence favours us.
- Detail: skills pull, who else is there, priorities, people (Name | Full title | Leaning, likely).
- Gaps: what Draup lacked; ask in discovery.

RULES
- Rating: Red if a [Competitor] product has High usage in the deal's workloads or a services rival holds 30%+ of active engagements there; Amber if Medium, newly detected or 10–29%; else Green.
- Landmines are fair questions grounded in a dated fact; never claim the rival's pricing, roadmap or unshown weaknesses.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
[Competitor] is in my deal at [Company]. Lead with how entrenched they are (Red, Amber, Green) and the named person to align with. Then their footprint, likely pitch, our wedge and 3 landmine questions.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write the discovery script that works the 3 landmines in naturally.
```

```text
Draft a reference-call brief: which of our customers should talk to them and what they should cover.
```

```text
Build the one-page battlecard for [Competitor] in my industry.
```

```text
Which of their leaders came from companies where [Competitor] is big?
```

## Tips for better results

- For job-ad counts use the product's skill name (CrowdStrike Falcon, not CrowdStrike); for the stack, use the maker as Draup spells it (e.g. Salesforce.com).
- Skills in job ads often show a rival's real depth better than the installed-stack view alone.
- Software rival in a services deal (or the reverse)? Run it twice, once for each, and compare.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.
- [Answer objections with their own facts](../../prompts/08-deal-strategy/objection-handler.md): Which objections are real and which are cover, with a short reply and a question back for each, built on dated facts about the account, and the named person to take the answer to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`, `accounts_hiring_summary_v3`, `get_product_competitors`, `get_deals_service_provider_v3`, `get_account_priorities_v3`, `get_priorities_top_workloads_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `deals-competitive-strategy`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
