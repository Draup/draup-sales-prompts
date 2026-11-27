[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Roles the client can't hire: staffing pitch

> **Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You sell staffing, staff augmentation or managed delivery and want evidence the client can't easily hire these roles itself. | Services, SI & Staffing Seller, Account Executive, SDR / BDR | Services sellers | 4–6 min | Talent cost & supply, Hiring & job postings |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company (optional)]` | fedex.com |
| `[Roles]` | Salesforce Developer, Data Engineer, SAP FICO Consultant |
| `[Location]` | Memphis, Tennessee Area, United States |
| `[What I sell]` | Salesforce and data staff augmentation |
| `[Exchange rate (optional)]` | the rate your finance team uses this quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my staffing and managed-services strategist. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company facts and the account's job postings. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company (optional): [the account's website, e.g. fedex.com]
- Roles: [up to 5, e.g. Salesforce Developer, Data Engineer, SAP FICO Consultant]
- Location: [metro or country, e.g. Memphis, Tennessee Area, United States]
- What I sell: [one line, e.g. Salesforce and data staff augmentation; skip if saved in setup]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

STEPS
1. Find Draup's standard name for each role. If there's no exact match, show the 3 closest and ask which to use.
2. Match the place to Draup's name (metros look like "Bengaluru Area, India"). If it doesn't match, show the closest and ask.
3. For each role in [Location], pull hiring difficulty (higher means harder to hire), talent supply, 3-year supply growth, open postings and median annual base pay.
4. Classify each: Hard (difficulty in the top third of roles checked, or postings outpacing supply; editable default), Moderate or Easy.
5. If [Company] is given, find it by website (parent, not a subsidiary; if the website returns nothing, look it up by name once and show the score) and count its postings per role in the last 6 months, noting repeats or long-open ones. Then pull its top 3 executives in the function that owns these roles (often IT or HR talent acquisition) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — which role is hardest to hire and what that means for [What I sell].
- Recommended next step: who to take it to (name and title from step 5, or the title to find), what to do, and why now (one dated fact). If none is found, say so.
- Table: Role | Hiring difficulty | Talent supply | Open postings | Verdict. Hardest first.
- "The pitch": one line per Hard role on how [What I sell] removes the hiring problem.
- Detail: median pay (local) and 3-year growth per role; "Account demand" (role, postings in 6 months, repeats or long-open).
- Gaps: what Draup didn't have, to ask in discovery.

RULES
- Explain the hiring-difficulty score in one plain line the first time it appears.
- Don't pitch Easy roles; say they're usually better hired in-house.
- Postings are openings, not hires.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Show pay in local currency with its code; convert to USD only with my [Exchange rate], and say which rate.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- Never return a blank table: say what came back empty and use the fallback.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 400 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: which of [Roles] is hardest to hire in [Location] — difficulty, supply, open postings, median pay — and which makes the best staffing pitch for [What I sell], and to whom.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which nearby metros have more supply for the Hard roles? Show the top 3.
```

```text
Write a 90-word email to [Company]'s head of talent acquisition built on the hardest role.
```

```text
Which employers in [Location] hire the most people in the Hard roles?
```

## Tips for better results

- Pair the difficulty score with the account's own postings: a hard role the client keeps re-posting is often your strongest opening.
- Easy-to-hire roles are a weak staffing pitch. Lead with the scarce ones and expand from there.

## Related prompts

- [Size a skill pool and its employers](../../prompts/17-talent-cost-and-location/role-sizing.md): How many people hold a role in up to 3 countries, how fast supply is growing, and which companies employ the most, split into prospects and services competitors.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.
- [Who's hiring for a tech or role](../../prompts/06-prospecting-and-lists/hiring-led-list.md): The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `talent_dashboard_talent_hdi_analyze_roles`, `talent_size_compare_locations`, `get_talent_demand_across_locations`, `get_base_pay_by_role_locations`, `get_account_id`, `accounts_hiring_job_postings_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **documented, not live-tested**. Prompt id: `talent-hard-to-hire`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
