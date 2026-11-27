[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this inbound lead worth pursuing?

> **A fast Pursue now / Pursue / Nurture / Disqualify verdict on an inbound or referred account: your must-haves, urgency tied to what you sell, a bake-off check against your competitors, and a reply plan.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A lead, demo request or referral lands and you need to decide in minutes whether it deserves an AE's time. | SDR / BDR, Account Executive, Marketing & ABM, Sales Leader & RevOps | Everyone | 1–2 min | Company directory, Company & financials, News signals, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | fivebelow.com |
| `[Requester title]` | Director of Store Operations |
| `[What they asked for]` | a demo of shift scheduling |
| `[My must-haves]` | US retailer, 5,000+ staff, $1B+ revenue |
| `[Business function]` | Operations (security and data sit under IT in Draup) |
| `[What I sell]` | store-operations software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales development analyst qualifying inbound accounts. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. fivebelow.com]
- Requester title: [who reached out, e.g. Director of Store Operations]
- What they asked for: [e.g. a demo of shift scheduling]
- My must-haves: [checkable facts, e.g. US retailer, 5,000+ staff, $1B+ revenue]
- Business function: [the function I sell to, e.g. Operations; security and data sit under IT in Draup]
- What I sell: [one line, e.g. store-operations software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; ask me if several match. No match: retry once by name and show the match score (ask me if under 0.8); still nothing: say so and stop.
2. Profile: primary vertical, HQ, workforce, revenue and growth, workforce growth %, postings (90 days).
3. Read the requester: does [Requester title] buy or champion in [Business function], and does [What they asked for] fit what I sell?
4. 90-day news where [Company] is the actor, and 12-month [Business function] postings in the workloads closest to What I sell.
5. Check the whole stack for competitors I named (here or in setup), with usage and first-seen dates.
6. The top 3 executives in [Business function], including the most senior leader for what I sell (e.g. the CISO for security).

OUTPUT
- Bottom line: 2 sentences — the verdict and why, for [What I sell].
- Recommended next step: a one-line reply answering [What they asked for], who else to loop in (name, full title), and the dated why-now (or "the request itself is the why-now").
- "Fit": Must-have | Draup value (date) | Meets / Partly / Misses / Unknown.
- "Why now": up to 3 events (date | headline | so-what), or "none in 90 days tied to what I sell".
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: requester read (decision maker, champion, user or researcher); competitor products found; postings count.

RULES
- The inbound is the intent. Pursue = every must-have met and the requester fits. Pursue now = Pursue plus a material 90-day event tied to [Business function] or what I sell; unrelated news never raises urgency.
- Nurture = Partly or Unknown on any must-have, or a student, job-seeker, vendor or researcher; list what to verify. Disqualify = misses a must-have.
- A competitor installed with High or Medium usage, or first seen in the last 12 months: write "likely bake-off or renewal" in the verdict. Ignore Low or very-low-confidence detections and say so.
- Flag revenue growth over 20% as likely M&A until checked.
- Show USD millions using Draup's conversion rate.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell; map a function to its main workloads and say which.
- News: the company must be the actor. Drop stock chatter, political commentary, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories. Keep any item that bears directly on What I sell, even if it's normally noise. Give date, source and headline.
- If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Counts apply every filter I set.
- People: check titles against the function; flag subsidiary or branch staff; mark C-level profiles whose tenure or past employers don't fit "verify" and keep them out of drafted copy. No senior owner: pull the next page of 10 in the function once and look for Chief, EVP, CIO or "Head of" titles.
- At most 2 tables up front (5 columns, 10 rows); reference tables go under "Detail". Keep to about 350 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Verdict first (Pursue now, Pursue, Nurture or Disqualify) on the inbound from [Requester title] at [Company] asking for [What they asked for], against [My must-haves]. Check my competitors in their stack; give a reply line and who to loop in.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft the full reply to the requester using the why-now.
```

```text
Map the 3 most senior people for what I sell there, including the CISO or equivalent.
```

```text
Show 3 peers of similar size so I can mention them.
```

## Tips for better results

- Write your must-haves as checkable facts (country, size, revenue, vertical). The verdict is only as sharp as the criteria.
- A pricing request plus your competitor in the stack usually means a bake-off or a renewal check. Ask which.
- Nurture is not a no. Check back when a new event appears.

## Related prompts

- [Size your ideal-customer list](../../prompts/06-prospecting-and-lists/icp-list.md): The true count of companies matching every filter, distributors set aside, and the 5 accounts to start with, each with who to call and a dated why-now.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `get_signal_news_v3`, `accounts_hiring_summary_v3`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `prospect-inbound-qualification`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
