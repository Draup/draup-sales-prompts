[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who uses [Technology] there

> **Which roles at the account use a given tool, grouped into three buyer personas with the other tools they use and the message for each.**

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
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull the company's roles that list [Technology] as a skill or tool. Names match exactly and in lower case; if nothing returns, try up to 3 variants (e.g. "salesforce crm", "salesforce sales cloud") and say which worked.
3. Take the top 10 roles by count, with job family and other tools.
4. Pull the number of job postings in the last 12 months that mention [Technology], as an activity check.
5. Group the 10 roles into 3 buyer personas (e.g. builders, operators, business owners).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- "Roles using [Technology]": Role | Job family | Other top tools (up to 5).
- One line: postings mentioning [Technology] in the last 12 months.
- "3 personas": name, roles in it, what they likely care about, adjacent tools that signal integration or displacement, a one-line message angle for [What I sell], and the likely senior owner (title).
- "Who to target first" with one reason.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If no roles use the tool, say so and show the 5 closest tools that do appear.
- Adjacent tools made by competitors I've named are displacement angles; say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- If a company's posting count is larger than its workforce, the company match is wrong; say so and leave it out.
- Label anything you infer (buyer role, intent, fit, integration work) as "likely".
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which roles at [Company] use [Technology]? Top 10 roles with job family and other tools, grouped into 3 buyer personas with what each cares about and a message angle for [What I sell].
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

- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Hypothesis-led discovery questions](../../prompts/02-buyers-and-stakeholders/discovery-questions.md): An opening insight and eight discovery questions, each built on a dated fact about the account, with the hypothesis behind it and what a good answer tells you.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a rival's products are live anywhere in the account's stack, how central they are, who else is in the room and which stated priorities could justify a switch.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_get_skills_architecture_v3`, `accounts_hiring_demand_category_v3`

Status: **tested live**. Prompt id: `people-personas-by-tool`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
