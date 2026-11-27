[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who uses [Technology] there

> **Which roles at the account use a given tool, grouped into three buyer personas with the message for each, and the senior person to target first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning persona-based outreach or ABM around a product you integrate with or replace. | Presales & Solutions, Marketing & ABM, Account Executive | Everyone | 2–4 min | Hiring & job postings, Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | jpmorganchase.com |
| `[Technology]` | salesforce |
| `[What I sell]` | CRM data quality and automation |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my persona research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Technology: [tool name, e.g. salesforce]
- What I sell: [one line, e.g. CRM data quality and automation — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the company's roles that list [Technology] as a skill or tool. Names match exactly and in lower case; if nothing returns, try up to 3 variants (e.g. "salesforce crm", "salesforce sales cloud") and say which worked.
3. Take the top 10 roles by count, with job family and other tools.
4. Pull the number of job postings in the last 12 months naming [Technology] as a skill, as an activity check: use the product's skill name (e.g. "Salesforce Sales Cloud", not "Salesforce"); if 0, retry once with the product name.
5. Group the 10 roles into 3 buyer personas (e.g. builders, operators, business owners).
6. Pull the top 3 executives in the business function closest to [What I sell] (full title, time in role) and the most important news item from the last 90 days where [Company] is the actor, to name the senior owner to target.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: one person by name and title (from step 6), what to do (call, email, intro, meeting) and why now (a dated fact from the last 90 days); say if either is missing.
- "3 personas": name, roles in it, what they likely care about, adjacent tools that signal integration or displacement, a one-line message angle for [What I sell], and the likely senior owner.
- "Roles using [Technology]": Role | Job family | Other top tools (up to 5). Top 10.
- One line: postings mentioning [Technology] in the last 12 months.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If no roles use the tool, say so and show the 5 closest tools that do appear.
- Adjacent tools made by competitors I've named are displacement angles; say so.
- If a company's posting count is larger than its workforce, the company match is wrong; say so and leave it out.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Postings are openings, not hires. Ignore the first and last months of a monthly series; they are usually partial.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. No Chief, EVP, CIO or "Head of" title? Pull the next page of 10 in the function once (there is no title search). Professional information only.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 400 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which roles at [Company] use [Technology]? Bottom line and who to target first, then top 10 roles with other tools, grouped into 3 buyer personas with a message angle for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Find senior executives who manage these personas.
```

```text
Write one 80-word email per persona.
```

```text
Which of the adjacent tools compete with ours?
```

## Tips for better results

- Type the tool in lower case and in its common short form first ("salesforce", "sap", "jira").
- Adjacent tools tell you what to integrate with, or what you might replace.

## Related prompts

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.
- [Discovery questions built on their data](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_get_skills_architecture_v3`, `accounts_hiring_demand_category_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `people-personas-by-tool`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
