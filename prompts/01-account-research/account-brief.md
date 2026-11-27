[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# One-page account brief

> **Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account just landed on your list, or you're prepping a call or meeting (tomorrow or later) with someone there, including when you only know their title. Use "10-minute pre-call snapshot" instead when you only have a few minutes. | Account Executive, Presales & Solutions, Account & Customer Success Manager, SDR / BDR | Everyone | 2–4 min | Company & financials, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | starbucks.com |
| `[What I sell]` | store technology and data platform services |
| `[Meeting with (optional)]` | a name or a title, e.g. CISO |
| `[Competitor (optional)]` | Snowflake or Accenture (company or product); defaults to your saved competitors |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. starbucks.com]
- What I sell: [one line, e.g. store technology and data platform services — skip if you ran the start-here prompt]
- Meeting with (optional): [name or title, e.g. CISO]
- Competitor (optional): [company or product, e.g. Snowflake; default: my saved competitors]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the profile and latest fiscal-year revenue, EBITDA and IT spend with growth (if private, funding instead), plus revenue by business unit and region, kept only if more than one holds 10% or more.
3. Pull stated priorities for the function closest to [What I sell]: the 8 most relevant, newest first (none: say so and use the company-wide list). Pull acquisitions from the last 3 years.
4. Pull the top 3 executives in that function and the 2 most important news items from the last 90 days where [Company] is the actor.
5. If I named who I'm meeting, find them: the workload closest to their title, then the function's next page once, matching full profile titles. Not found: say so and list the 3 closest people.
6. Check the whole stack for [Competitor]'s products, in any area; for a services firm, its share of active engagements in my workloads.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]; say here if the person I'm meeting isn't in Draup.
- Recommended next step: one person by name and title (the person I'm meeting if found, else from step 4), what to do and why now (a dated fact from the last 90 days); say if either is missing.
- "What they're focused on": Priority | Source + quarter | Likely owner (name, else title) | Why it matters. Up to 8.
- "Who to talk to": Name | Full title | Time in role | Linked priority. Up to 3, the person I'm meeting first; if they're not in Draup, the 3 closest.
- "Competitor in the stack": one line each: product or engagement share, usage strength, last seen, Red/Amber/Green.
- "Why this matters for [What I sell]": 3 bullets: fact → implication → action.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "The numbers" (Metric | Latest FY | YoY); business units and regions if kept; "Recent deals" (Date | Company acquired | Size | Why), flagging divestments and duplicates.

RULES
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- The acquisitions table can be incomplete; if news names a deal it lacks, say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Money: annual, millions of reporting currency. IT and R&D spend are modelled and move with revenue, so their growth isn't a signal. Check for a divestment before calling a drop over 5% a cut.
- Competitor rating: a [Competitor] product at High usage in the workloads I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber. Services rival, by share of the account's active engagements in those workloads: 30%+ Red, 10–29% Amber, under 10% Green.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 500 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
One-page Draup brief on [Company], meeting [Meeting with]: bottom line, who to call and why now; that person (or the 3 closest if not in Draup); 8 priorities in my function; revenue growth; [Competitor] rated Red/Amber/Green.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Now run "Map the buying committee" for [Business function].
```

```text
Which of these priorities have the most hiring behind them?
```

```text
Is their budget growing or shrinking? Show the 3-year trend.
```

```text
Turn the 'Why this matters' section into a 90-word email to the person in the next step.
```

## Tips for better results

- Add your main competitor, or save it with "Tell your AI about you": finding it, or its absence, in the stack is often the most useful line in the brief.
- Use the company website rather than the name; it is the most reliable way to land on the right company.
- Business-unit and region tables only appear when the company is genuinely split; a single-market retailer skips them.
- Prepping a meeting? Put the title in Meeting with ("CISO"). If Draup has no one with that title, the brief says so up front and gives the 3 closest people.

## Related prompts

- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Which priority to anchor your pitch on](../../prompts/01-account-research/priorities-by-function.md): The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_revenue_by_business_v3`, `accounts_financials_revenue_by_region_post_v3`, `get_account_priorities_v3`, `accounts_partnerships_mergers_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`, `accounts_private_financials_v3`, `get_account_tech_stack_products_v3`, `get_outsourcing_engagement_details`

Status: **tested live**. Prompt id: `research-account-brief`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
