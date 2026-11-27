[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# New leaders and warm intro paths

> **Leaders who joined or were promoted recently in your area, where they came from, and current leaders who used to work at your customers, so you know who to congratulate and who can introduce you.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Monthly, or when an account goes quiet: new leaders often review vendors in their first 90 days. Use this for people who just arrived or came from your customers; use "Map the buying committee" instead when you need everyone who decides today. | SDR / BDR, Account Executive, Account & Customer Success Manager | Everyone | 2–4 min | Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | 3m.com |
| `[Workload]` | Inventory Management, Demand Management — a type of work, not a function like Supply Chain; a function gets mapped for you |
| `[Our customers (optional)]` | Contoso Retail, Fabrikam Foods |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales stakeholder analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Workload: [1–3 Draup workloads, e.g. Inventory Management, Demand Management — not a function like Supply Chain; if I give a function, map it to workloads first]
- Our customers (optional): [e.g. Contoso Retail, Fabrikam Foods]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. If I gave a business function, map it to the 1–3 closest Draup workloads and say which.
3. Pull executive hires and promotions, one workload at a time; keep rows where [Company] is the current employer.
4. Keep moves from the last 6 months. Leadership data can lag about 3 months: if none fall inside, show the latest moves from the 3 months before, labelled "just outside the window".
5. Compare each new hire's past companies (whole history, not just the last one) with [Our customers], allowing name variants ("Contoso" = "Contoso Retail Inc.").
6. If fewer than 3 warm paths, also check current senior leaders in the matching business function (10 per page, up to 3 pages; no title search) whose past companies include [Our customers]. Flag any with under 6 months in their title as new.
7. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title, what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- One line per workload: rows checked, rows kept, latest move date in the data.
- "New leaders": Date | Name | New title | Came from (company, or "promoted") | Warm path? Newest first, up to 10.
- "Warm paths": Name | Current title | Customer in their past | Found as (new leader or current leader) | Who on our side to ask.
- "First-90-days plays": the top 3 people to approach, each with a one-line angle tied to [What I sell].
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Leave out exits; "Customer alumni now at your targets" covers them.
- Drop rows that clearly aren't about [Company], such as look-alike company names.
- If a workload has no moves even in the wider window, say "none found"; don't widen further silently.
- A warm path means they worked at our customer, not that they bought from us.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- If I give a business function where a workload is needed, map it to the 1–3 closest Draup workloads, say which, then continue.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. Professional information only.
- Leadership-move data can lag about 3 months; give the latest move date you saw.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
New leaders at [Company] in [Workload]: bottom line and who to contact first, then hires and promotions in the last 6 months (date, name, title, came from) and any current leaders who worked at [Our customers].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Profile the top new leader and draft a congratulations note with a relevant angle.
```

```text
Check pages 4–6 of current leaders for more warm paths.
```

```text
Show exits in the same workloads: where did they go?
```

```text
Draft the intro request to our account team at the matched customer.
```

## Tips for better results

- Type a workload if you know it; if you type a function such as Supply Chain, the prompt maps it to workloads and says which.
- Leadership-move data can lag about 3 months, so the prompt shows moves just outside the window rather than an empty table.
- A leader who came from one of your customers is often the warmest intro you can get.

## Related prompts

- [Warm paths among current leaders](../../prompts/02-buyers-and-stakeholders/warm-paths-current-leaders.md): Senior leaders at the account who used to work at your customers, partners or your own company, who on your side to ask for the intro, and why now.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A short profile of one senior person, found by name or just by title, with time in role, past companies, what they likely own, a competitor check and two openers. If Draup has no one with that title, you're told so up front and given the 3 closest people.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Customer alumni now at your targets](../../prompts/11-account-planning/follow-champions.md): Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_executive_movement`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `people-new-leaders-warm-paths`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
