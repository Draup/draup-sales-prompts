[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which priority to anchor your pitch on

> **The single priority to lead with, who likely owns it by name, where the account's priorities cluster and the vendors linked to each.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You need to know which initiative to anchor a pitch on. | Account Executive, Presales & Solutions, Account & Customer Success Manager, Services, SI & Staffing Seller | Everyone | 2–4 min | Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | siemens.com |
| `[What I sell]` | cloud data-platform modernisation services |
| `[Business function (optional)]` | IT — leave blank and Claude picks the best fit |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales strategy analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. siemens.com]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]
- Business function (optional): [e.g. IT; leave blank and Claude picks]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull how many priorities mention each workload (a type of work, e.g. Data Engineering). Mark each Strong, Partial or No fit to [What I sell] and keep the top 5 by fit, then count.
3. If I gave no business function, choose the one holding most Strong-fit workloads and say why.
4. Pull up to 8 priorities for that function and sort them by date yourself, newest first.
5. Pull the top 3 executives in that function (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to name the anchor's likely owner.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 5), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "Best anchor for [What I sell]": the one priority to lead with, its likely owner by name, and 2 bullets on why.
- "Top priorities in [Business function]": Priority | Source + quarter | Workloads | Up to 3 linked providers. Up to 8.
- "Where priorities cluster": Rank | Workload | # priorities | Fit (Strong, Partial, No). Top 5.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: a one-line summary of each priority.

RULES
- Leave out linked technology or use cases that clearly don't fit the industry.
- If the function has no priorities, say so and show the 3 nearest functions by priority count.
- Source matters: earnings-call priorities usually outweigh news-derived ones; say which each is.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Tools and providers linked to a priority are "linked", not confirmed. Leave out recruiters, staffing firms, agencies and research firms.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which [Company] priority should I anchor [What I sell] on? Bottom line, the anchor and its likely owner by name, then top 5 workloads by fit and the top 8 priorities in the best-fit function.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the anchor priority, which technology and incumbent vendors are linked?
```

```text
Who else owns the anchor priority? Find executives tagged to its workloads.
```

```text
Is there hiring behind these priorities, or are they just talk?
```

## Tips for better results

- Leaving the function blank lets Claude choose where your offer fits best.
- Priorities from earnings calls often carry more weight than ones inferred from news.

## Related prompts

- [Their leaders' own words on [Topic]](../../prompts/01-account-research/proof-points.md): Up to six verbatim leadership quotes on your topic with speaker and fiscal quarter, who to take them to, or the annual-filing sections to read when there's no call.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, the person you're meeting (or the 3 closest if Draup lacks them), then the priorities in your function, who likely owns them, any competitor in the stack rated Red/Amber/Green and the key numbers.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_priorities_top_workloads_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `research-priorities-by-function`.

</details>

---

[Back to Account research](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
