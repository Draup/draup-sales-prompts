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
- Objections: [not a priority; have a vendor; no budget; build in-house; bad timing — or "all"]
- Area (optional): [workloads or a function, e.g. Cloud Computing — or IT]
- Incumbent or competitor (optional): [e.g. Infosys, or Snowflake]
- What I sell: [one line, e.g. managed cloud and data modernisation services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Objections are usually partly true: acknowledge it, add one hard fact from their company, ask a question; if the evidence agrees, re-qualify.

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Use [Area], or the function closest to [What I sell], as 1–3 workloads; say which.
3. Pull only what the objections need. Not a priority: up to 6 priorities in the function. Already have a vendor: active engagements and top providers in the workloads; for software, check the whole stack for the incumbent's products. No budget: revenue, EBITDA, Draup-estimated IT spend and split. Build in-house: 12 months of postings in the workloads and any in-house priority. Bad timing: 90 days of news on reorganisations, layoffs, leadership changes and big programmes.
4. Owner and trigger: the top 3 executives in the function and the most important 90-day news item.
5. Judge each: Supports, Partly or Undercuts.
6. Reply: acknowledge, one dated fact, reframe, one question.

OUTPUT
- Bottom line: 2 sentences — which objections are real, which are cover, and what it means for [What I sell].
- Recommended next step: a named person (name, full title), the action this week and the dated why-now; if none, say so.
- Table "Objection scorecard": Objection | Verdict | Key fact (dated) | Source.
- Per objection: "Reply" (under 60 words) and "Question back".
- "If it's real": a re-qualification move (narrower scope, another workload, later date).
- Detail: vendor table (Provider or product | Engagements or usage | Where thin), money, hiring.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Each reply uses a fact from the last 12 months, never industry trends.
- A large incumbent isn't a reason to quit: find workloads where it has 3 or fewer engagements. Ignore the company's own products.
- An incumbent product with High usage in my workloads is Red (the objection is real: position as complement or narrower scope); Medium is Amber.
- Falling postings undercut "we'll build in-house"; rising ones support it.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- Trust usage strength and last-seen date; ignore confidence scores and "Generic" rows. A last-seen date shared by many rows is a data refresh. Say "fading", never "dropped".
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
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
