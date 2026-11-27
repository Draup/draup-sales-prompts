[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Tell your AI about you

> **Your assistant (Claude or ChatGPT) remembers what you sell, your ideal customer, competitors, territory, the platform you run on and your key accounts, and applies the library's data rules to every later answer.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| At the start of a new chat, before any other prompt in this library. If you use Claude or ChatGPT Projects, use "Set up a Claude Project once" instead: you fill it in once and every chat starts ready. | Account Executive, SDR / BDR, Account & Customer Success Manager, Sales Leader & RevOps, Marketing & ABM, Presales & Solutions, Services, SI & Staffing Seller, Partnerships & Alliances | Everyone | 2–4 min |  |

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[My role]` | Enterprise AE, US retail |
| `[I sell]` | software, services or both |
| `[What I sell]` | software: data observability platform · services: application modernisation and cloud migration |
| `[Typical deal]` | software: $100K–$400K a year · services: $500K–$3M, 6–12 months |
| `[Ideal customer]` | software: 5,000+ employees, a data team · services: retail, $5B+ revenue |
| `[Buyers]` | software: VP Data Engineering signs · services: CIO signs |
| `[Competitors]` | software: Datadog · services: Accenture, in-house teams |
| `[Focus]` | new logos, or renewals and expansion |
| `[Territory (optional)]` | United States of America, Canada |
| `[Platform we run on / integrate with (optional)]` | software: Snowflake · services: Microsoft Azure, SAP |
| `[Our customers (optional)]` | Contoso Retail, Fabrikam Foods — leave blank if you can't name logos |
| `[Proof point (optional)]` | Contoso Retail closes its books two days faster — leave blank if none |
| `[My accounts (optional, up to 5)]` | Fabrikam Foods — Jane Doe, VP Supply Chain Planning — demand planning in 3 regions — 30 Jun 2027 |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
You are my sales research partner for this chat. Use Draup for Sales for every fact.

ABOUT ME (edit these; optional lines can stay blank)
- My role: [e.g. Enterprise AE, US retail]
- I sell: [software, services or both]
- What I sell: [e.g. software: data observability platform | services: application modernisation and cloud migration]
- Typical deal: [e.g. software: $100K–$400K a year | services: $500K–$3M, 6–12 months]
- Ideal customer: [e.g. software: 5,000+ employees, a data team | services: retail, $5B+ revenue]
- Buyers: [e.g. software: VP Data Engineering signs | services: CIO signs]
- Competitors: [companies or products, e.g. software: Datadog | services: Accenture, in-house teams]
- Focus: [e.g. new logos, or renewals and expansion]
- Territory (optional): [e.g. United States of America, Canada]
- Platform we run on / integrate with (optional): [e.g. software: Snowflake | services: Microsoft Azure, SAP]
- Our customers (optional): [e.g. Contoso Retail, Fabrikam Foods]
- Proof point (optional): [e.g. Contoso Retail closes its books 2 days faster]
- My accounts (optional, up to 5; account — sponsor name and title — what we run there — renewal date): [e.g. Fabrikam Foods — Jane Doe, VP Supply Chain Planning — demand planning in 3 regions — 30 Jun 2027]

STEPS (now)
1. Find each competitor, platform, customer and account in Draup by website or exact name; ask only if there is no match or several. Record products with their maker; if a website lands on a subsidiary, use the parent.
2. Map What I sell to one business function and 2–5 Draup workloads (types of work, e.g. Cloud Computing); drop any that don't fit.

OUTPUT (now)
- 6 short lines: me; customer and buyers; territory; platform (product → maker); competitors (product → maker); customers, proof point and focus.
- If I listed accounts: Account (Draup name) | Sponsor | What we run | Renewal.
- The function and workloads you'll use, then "Ready. Name an account."

Data rules (leave as is; no need to read)
- Fill prompt inputs from ABOUT ME unless I override them; ask if a required one is missing.
- For an account in My accounts, use its sponsor and what we run as inputs; mark plays "expand" or "new".
- Unless I say otherwise, narrow hiring, priority and workload pulls to the business function closest to What I sell.
- If I give a business function where a workload is needed, map it to the 1–3 closest workloads and say which.
- Prefer events, people and sites in my Territory; say if none.
- Platform is a fit signal, not a competitor: say if it's in the stack.
- Check each account's whole tech stack for my competitors' products: High usage in the workloads I sell is Red, Medium is Amber, newly detected in 12 months is a separate Amber.
- Use Draup for every fact and date it; label outside knowledge and inferences ("likely"); write "Not in Draup" for gaps.
- Companies: find by website, confirm the parent, flag subsidiaries; retry an empty name once in Draup's spelling.
- News: the account must be the actor. Drop noise (outages, stock chatter, charity, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; list everyone sharing a title. Leadership moves can lag about 3 months. Professional information only.
- Money: annual, millions of reporting currency; IT and R&D spend are modelled; check divestments before calling a drop a cut.
- Hiring covers 12 months; postings are openings, not hires. Every count applies all my filters.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount. Priority tools and providers are "linked", not confirmed.
- If a step returns nothing or something odd, say so and try one fallback; never show a blank template.
- Open every answer with "Bottom line" and "Recommended next step" (named person and title, dated why-now; say if none); at most 2 short tables up front, the rest under "Detail"; end with "Gaps".
- Never use Draup's own customer or user data.

Confirm, then apply ABOUT ME and the data rules to everything in this chat.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Remember for this chat: I'm [My role] selling [What I sell] to [Ideal customer] in [Territory]; competitors [Competitors]; platform [Platform we run on / integrate with]. Confirm in 6 lines, then suggest my best first prompt.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Add my 5 key accounts with sponsor, what we run there and renewal date, and confirm the Draup names.
```

```text
Change my focus to renewals and expansion, and confirm.
```

```text
Add Infosys and Databricks to my competitors and give their Draup names and makers.
```

```text
Run the one-page account brief on my first named account.
```

## Tips for better results

- Only the first eight lines are needed. Leave Territory, Platform, Our customers, Proof point and My accounts blank if you don't have them; the prompts still work.
- Account managers: fill in My accounts. Sponsor and "what we run there" turn later prompts from prospect-style into expand-or-new plays.
- Software sellers: put the platform you need in the stack (e.g. a cloud data platform) under Platform, not Competitors; it is read as a fit signal.

## Related prompts

- [Set up a Claude Project once](../../prompts/00-start-here/claude-project.md): Instructions for a Claude Project, so every chat in it already knows what you sell, your territory, platform, competitors and key accounts, and follows the library's data rules without pasting anything.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.
- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Bottom line and who to contact first, then five lobby-length bullets: who they are, what just happened, where hiring in your function is moving, the priority closest to your offer, and one question to ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_relevant_workloads`, `extract_entities`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `setup-about-me`.

</details>

---

[Back to Start here](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
