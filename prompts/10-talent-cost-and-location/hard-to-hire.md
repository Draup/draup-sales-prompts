# Hard-to-hire roles: staffing pitch

**Which of an account's roles are hardest to hire in its key location, with supply, demand and pay, turned into a staffing or managed-services pitch.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. You sell staffing, staff augmentation or managed delivery and want evidence the client can't easily hire these roles itself. | Services, SI & Staffing Seller, Account Executive, SDR / BDR | Services sellers | 4–6 min | Talent cost & supply, Hiring & job postings |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company (optional)]` | target.com |
| `[Roles]` | Salesforce Developer, Data Engineer, SAP FICO Consultant |
| `[Location]` | Greater Minneapolis-St. Paul Area, United States |
| `[What I sell]` | Salesforce and data staff augmentation |
| `[Exchange rate (optional)]` | the rate your finance team uses this quarter |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my staffing and managed-services strategist. Use the Draup for Talent connector for pay, talent-supply and hiring-difficulty facts, and the Draup for Sales connector for company lookups and the account's job postings. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company (optional): [the account's website, e.g. target.com]
- Roles: [up to 5, e.g. Salesforce Developer, Data Engineer, SAP FICO Consultant]
- Location: [metro or country, e.g. Greater Minneapolis-St. Paul Area, United States]
- What I sell: [one line, e.g. Salesforce and data staff augmentation — skip if you ran the start-here prompt]
- Exchange rate (optional): [your rate to USD for each local currency, e.g. the rate your finance team uses this quarter]

STEPS
1. Find Draup's standard name for each role. If there's no exact match, show the 3 closest and ask which to use.
2. Match each place to Draup's name (metros look like "Bengaluru Area, India"). If one doesn't match, show the closest and ask.
3. For each role in [Location], pull hiring difficulty, talent supply, 3-year supply growth, open postings (current demand) and median annual base pay.
4. Classify each: Hard (difficulty in the top third of roles checked, or postings outpacing supply; editable default), Moderate or Easy.
5. If [Company] is given, find it by website (parent, not a subsidiary) and count its postings per role in the last 6 months, noting repeats or long-open ones.

OUTPUT
- Bottom line: 2 sentences — which role is hardest to hire and what that means for [What I sell].
- Table: Role | Hiring difficulty | Talent supply | 3-yr growth | Open postings | Median pay (local) | Verdict. Hardest first.
- "Account demand" (if [Company] given): Role | Postings, last 6 months | Repeat or long-open postings.
- "The pitch": one line per Hard role on how [What I sell] removes the hiring problem.
- Recommended next step: who to take it to (title), what to do, and why now (one dated figure).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Explain the hiring-difficulty score in one plain line the first time it appears (higher means harder to hire).
- Don't pitch Easy roles; say they're usually better hired in-house.
- Postings are openings, not hires.

STANDARD RULES (leave as is)
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- Pay comes back in local currency: show it with its currency code. Convert to USD only if I give you a rate in [Exchange rate], and say which rate you used; otherwise show local currency.
- Talent-supply sizes and hiring-difficulty scores are Draup estimates; say so once.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
For [Roles] in [Location], show Draup hiring difficulty, talent supply, 3-year growth, open postings and median pay, hardest first, and tell me which role makes the best staffing pitch for [What I sell].
```

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

- [Size a role and who employs it](../../prompts/10-talent-cost-and-location/role-sizing.md): How many people hold a role in up to 3 countries, how fast supply is growing, and which companies employ the most, split into prospects and services competitors.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings are running above or below normal, which workloads drive it, and whether it's seasonal.
- [Who's hiring for a tech or role](../../prompts/05-prospecting-and-lists/hiring-led-list.md): The end employers posting the most jobs for a technology or buyer role, cleaned of job boards and staffing firms, with who to call and the industries driving demand.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`search_talent_entities_v3`, `get_talent_dashboard_locations`, `talent_dashboard_talent_hdi_analyze_roles`, `talent_size_compare_locations`, `get_talent_demand_across_locations`, `get_base_pay_by_role_locations`, `get_account_id`, `accounts_hiring_job_postings_v3`

Status: **documented, not live-tested**. Prompt id: `talent-hard-to-hire`.

</details>

[Back to Talent cost and location](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
