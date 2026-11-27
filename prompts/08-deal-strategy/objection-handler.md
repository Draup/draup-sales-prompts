[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Answer objections with their own facts

> **Which objections are real and which are cover, with a short reply and a question back for each, built on dated facts about the account, and the named person to take the answer to.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A buyer has pushed back (not a priority, already have a vendor, no budget, we'll build in-house, bad timing), or before a meeting where you expect pushback. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 4–6 min | Priorities & opportunities, Company & financials, Outsourcing deals, Tech stack, Hiring & job postings, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | adobe.com |
| `[Objections]` | already have a vendor; bad timing (or: all) |
| `[Area]` | Cloud Computing, Data Engineering (or a function like IT; optional) |
| `[Incumbent or competitor]` | Infosys (optional) |
| `[What I sell]` | managed cloud and data modernisation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my objection-handling coach. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. adobe.com]
- Objections: [not a priority, have a vendor, no budget, build in-house, bad timing, or "all"]
- Area (optional): [workload or function, e.g. Cloud Computing or IT]
- Incumbent (optional): [e.g. Infosys, or Snowflake]
- What I sell: [one line, e.g. managed cloud and data modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Most objections are partly true.

STEPS
1. Find [Company] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Use [Area], or the function closest to [What I sell], as 1–3 workloads; say which.
3. Pull per objection. Not a priority: up to 6 function priorities. Already have a vendor: if I sell software, check the whole stack for the incumbent's products and any second product in the same sub-category (overlap is the opening); if services, active engagements and top providers in the workloads. No budget: revenue, EBITDA, IT spend and split. Build in-house: 12-month postings and in-house priorities. Bad timing: 90-day news on reorganisations, layoffs, leaders, big programmes.
4. Owner and trigger: top 3 function executives and the most important 90-day news item.
5. Judge each (Supports, Partly, Undercuts) and reply: acknowledge, one fact from the last 12 months (no industry trends), reframe, one question.

OUTPUT
- Bottom line: 2 sentences — which are real, which are cover, and what that means for me.
- Recommended next step: a named person (name, full title), the action this week and the dated why-now (or say none).
- Table "Objection scorecard": Objection | Verdict | Key fact (dated) | Source.
- Per objection: "Reply" (under 60 words) and "Question back".
- "If it's real": a re-qualification move (narrower scope, a workload where the incumbent has 3 or fewer engagements, later date).
- Detail: vendors (Provider or product | Engagements or usage | Where thin), money, hiring.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Rate the incumbent: Red (objection real: complement or narrow scope) if a product has High usage in my workloads or a services firm holds 30%+ of engagements there; Amber if Medium or 10–29%; else Green.
- Falling postings undercut "build in-house" and favour consolidation for "have a vendor"; rising ones support building.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Active engagements (Draup-derived) are estimates, not contracts; never quote outsourced headcount.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- If [Company] sells technology or services, drop priorities, news and hiring about its own offerings before choosing an angle; never pitch it its own category.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Answer these objections at [Company] with dated Draup facts: [Objections]. Lead with which are real, which are cover, and the named person to take it to. For each: verdict, the key fact, a 60-word reply and a question back.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Role-play the buyer: raise these objections one by one and score my replies.
```

```text
Turn the 'already have a vendor' answer into a one-page second-vendor point of view.
```

```text
Write a follow-up email that answers the objection I heard today in under 120 words.
```

## Tips for better results

- Ask for "all" before a big meeting; pick one or two right after a call so the answers stay sharp.
- A Supports verdict is useful: it tells you to change scope or timing rather than push harder.

## Related prompts

- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- [Arm your champion to sell internally](../../prompts/08-deal-strategy/champion-pack.md): A forwardable brief your champion can use to sell the deal inside: why now in their company's words, cost of waiting, answers for the CFO, CIO and procurement, a 150-word internal email, and who to route it to.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_outsourcing_summary_v3`, `get_deals_service_provider_v3`, `get_outsourcing_engagement_details`, `get_account_tech_stack_products_v3`, `get_account_financials_v3`, `accounts_financials_revenue_by_it_spend_v3`, `accounts_hiring_timeline_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `deals-objection-handler`.

</details>

---

[Back to Deal strategy and qualification](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
