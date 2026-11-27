[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email on a hiring surge

> **Which function is hiring above its own normal, the workloads and roles driving it, a named reader, and a 100-word email on the capability the surge is building, with no counting of their job ads in the copy.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| An account is posting more jobs than usual in a function you sell into and you want to reach out while the team and its budget are taking shape. | SDR / BDR, Account Executive, Services, SI & Staffing Seller | Everyone | 2–4 min | Hiring & job postings, Priorities & opportunities, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | delta.com |
| `[Persona]` | VP Commercial Strategy |
| `[What I sell]` | sales enablement and CRM services |
| `[Business function (optional)]` | Sales & Marketing |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my outbound copywriter for hiring-led triggers. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. delta.com]
- Persona: [reader, e.g. VP Commercial Strategy]
- What I sell: [one line, e.g. sales enablement and CRM services — skip if you ran the start-here prompt]
- Business function (optional): [e.g. Sales & Marketing]

STEPS
1. Find [Company] by website and confirm the parent, not a subsidiary, brand or sister company. If it doesn't resolve, retry once by name; show the match and score. Use Draup's exact name.
2. Pull 12 months of job postings by function: top 6, each with last 5 full months vs the 5 before and any "Trending Up" label. Use [Business function], else the function closest to [What I sell], else the biggest riser that fits.
3. In that function, pull the top 5 workloads with trend and the 4 newest postings: title, date, location, work type and a responsibility hinting at a new team or programme.
4. Pull up to 4 priorities in that function and pick the one the hiring best supports.
5. Label it Surge (over 25% up, editable default), Rising (10 to 25%), Flat, or Seasonal (a one-month spike); write copy only for Surge or Rising.
6. Pull the top 3 executives in [Persona]'s function and pick the likeliest contact. Also pull [Company]'s most important 90-day news item where it is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what to do and why now (one dated fact); if neither, say so and name the title to look for.
- "Check before sending" (directly above the copy): single-source or disputed facts the copy leans on and any "verify" profile, with what to check; or "none".
- Email: subject (6 words max), body (100 words max): the capability being built, in general terms from public job ads ("building out a media sales team"); a question on ramping it; one offer; one ask.
- Table "Functions" (top 6): Function | Postings (12 months) | Last 5 vs prior 5 (%) | Label.
- Table "What's driving it" (top 5): Workload | Postings | Recent months.
- Detail: newest roles (Date | Title | Location | Work type | Hint); linked priority (source, quarter); Gaps (to ask in discovery).

RULES
- Never quote posting counts or percentages in the copy; describe the team being built.
- If over half the newest roles are contract, say it may signal staff augmentation. If no function is Surge or Rising, say so and suggest a priority-led message.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources, never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Postings are openings, not hires. The monthly series has partial first and last months; compare the last 5 full months with the 5 before.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If [Company] sells technology or services, drop priorities, news and hiring about its own products before choosing an angle.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff and mark any C-level profile whose tenure or past employers don't fit the parent "verify" (kept out of copy).
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named reader, a dated why-now). Find where [Company]'s postings near [What I sell] rose most (last 5 full months vs 5 before), show what drives it, and write a 100-word [Persona] email.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show the metros where this function's postings are rising fastest.
```

```text
Who leads this function at [Company]? List up to 5 with full titles.
```

```text
Write a version for a services firm offering to staff part of the build-out.
```

```text
Is there a news item or priority that explains the surge?
```

## Tips for better results

- Read the newest postings' responsibilities: they often name the new programme the surge is for.
- Partial first and last months distort the trend; the 5-versus-5 full-month comparison avoids that.

## Related prompts

- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.
- [Priorities with no hiring behind them](../../prompts/04-signals-and-timing/priorities-vs-hiring.md): Which stated priorities in your function have hiring behind them and which don't: the gaps where the account may need to buy rather than build, with a named person to call.
- [Who's hiring for a tech or role](../../prompts/06-prospecting-and-lists/hiring-led-list.md): The end employers posting most for a technology or buyer role, cleaned of job boards and staffing firms, with hiring per 1,000 staff, who to call and a dated why-now.
- [Email after a new site or centre](../../prompts/05-outreach-and-messaging/new-site.md): The account's newest centres, leases and expansions, fact-checked and matched against its location footprint and local hiring, plus a 100-word email and a LinkedIn note aimed at what the site is being staffed for.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_hiring_job_postings_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `outreach-hiring-surge`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
