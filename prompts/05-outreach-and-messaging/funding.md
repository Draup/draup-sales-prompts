[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email after a funding or investment

> **A dated, fact-checked read of the account's latest raise or announced investment, where the money is going by function, and a 100-word email plus a LinkedIn note that ties it to one priority.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account has just raised money or announced a big investment plan (new region, plant, capital programme) and budgets are being set. | Account Executive, SDR / BDR, Marketing & ABM | Everyone | 2–4 min | Company & financials, News signals, Hiring & job postings, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | databricks.com |
| `[Persona]` | VP Engineering |
| `[What I sell]` | cloud cost management software |
| `[Proof point (optional)]` | cut cloud spend for Fabrikam Foods |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for growth-stage and investing accounts. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. databricks.com]
- Persona: [reader, e.g. VP Engineering]
- What I sell: [one line, e.g. cloud cost management software — skip if you ran the start-here prompt]
- Proof point (optional): [e.g. cut cloud spend for Fabrikam Foods]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name. Note public or private.
2. Pull funding history: the last 3 rounds (date, USD millions, type, lead investors), or say it has none.
3. Pull 6 months of fundraise-and-investment news, newest first, 10 items. Sort each: Raised, Committed (announced spending), Reported (talks) or Invested in others. Fact-check each amount.
4. Pull 12 months of job postings by function: top 6 with trend, last 5 full months vs the 5 before.
5. Pull up to 6 priorities in [Persona]'s function, newest quarter first, and link the newest Raised or Committed event to the hiring and best-fit priority.
6. Pull the top 3 executives in [Persona]'s function and pick the likeliest contact.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): single-source or disputed facts the copy leans on and any "verify" profile, with what to check; or "none".
- Email: subject (6 words max), body (100 words max): the event and its date in one clause; the stated use; a question linking it to [Persona]'s priority; one concrete offer; one ask. [Proof point] only if given.
- LinkedIn note: 280 characters max.
- Table "Money events" (newest first): Date | Type | Amount | Stated use | Fact check.
- Table "Where it is going" (top 6): Function | Postings (12 months) | Last 5 vs prior 5 | Trend.
- Detail: sources and lead investors; invested-in-others items, one line each; linked priority (source, quarter); Gaps (to ask in discovery).

RULES
- Never congratulate or mention valuation; quote an amount only if Confirmed, as the source states it.
- Reported or in-talks items aren't closed: never write them as done; prefer a closed event for the hook. If the only events are investments in other companies, write from hiring and priority instead.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources, never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- News: [Company] must be the actor; drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes, sister companies and re-dated stories; keep incidents or regulatory items bearing on What I sell. Give source and headline.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 420 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named reader, a dated event). List [Company]'s funding and investment news from 6 months, fact-check the amounts, show where hiring is rising, and write a 100-word email to a [Persona].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write the same email for the CFO, focused on spending the new money with control.
```

```text
Which metros are getting the new hiring? Show the top 5 with postings.
```

```text
Draft a second touch for day 6 that uses the hiring trend instead of the funding.
```

```text
Find a second source for the amount so I can quote it.
```

## Tips for better results

- The strongest hook is often the stated use of funds (a new region or team), not the amount.
- Corporate venture arms make many investments in other companies; those rarely mean the account itself has new budget.
- Amounts reported by one outlet, or reported differently by two, stay out of the email until you confirm them.

## Related prompts

- [Private company funding and who signs](../../prompts/01-account-research/private-funding.md): How much a private company has raised, its last round and valuation, whether it is in growth mode, and who signs, by name.
- [Are they really investing in X?](../../prompts/04-signals-and-timing/investing-in-x.md): A Yes / Early / No verdict on whether hiring, headcount and stated priorities back up a technology theme, with proof postings, three talking points and a named person to call.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.
- [Email after a new site or centre](../../prompts/05-outreach-and-messaging/new-site.md): The account's newest centres, leases and expansions, fact-checked and matched against its location footprint and local hiring, plus a 100-word email and a LinkedIn note aimed at what the site is being staffed for.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `accounts_private_financials_v3`, `get_news_feed_v3`, `accounts_hiring_demand_category_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-funding`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
