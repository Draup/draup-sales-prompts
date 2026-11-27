[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Tell your AI about you

> **Your assistant (Claude or ChatGPT) remembers who you are, whether you sell software or services, your ideal customer, territory, competitors and proof point, and applies the library's data rules to every later answer.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| At the start of a new chat, before any other prompt in this library. If you use Claude or ChatGPT Projects, the Project version is the better path: you set it once. | Account Executive, SDR / BDR, Account & Customer Success Manager, Sales Leader & RevOps, Marketing & ABM, Presales & Solutions, Services, SI & Staffing Seller, Partnerships & Alliances | Everyone | 2–4 min |  |

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[My role]` | Enterprise AE, North America retail |
| `[I sell]` | software, services or both |
| `[What I sell]` | moving legacy data warehouses to the cloud, plus managed data engineering |
| `[Typical deal]` | $250K–$1.5M first year, 6–9 month cycle |
| `[Ideal customer]` | Retail and consumer goods, 5,000+ employees, $1B+ revenue, hiring data engineers |
| `[Buyers]` | CIO, Chief Data Officer, VP Data Engineering; the CIO signs |
| `[Territory]` | United States of America and Canada; named accounts target.com, kroger.com |
| `[Competitors]` | Accenture, Snowflake, Google BigQuery, in-house build |
| `[Our customers]` | Contoso Retail, Fabrikam Foods |
| `[Focus]` | new logos; displacing incumbent providers |
| `[Proof point]` | Contoso Retail closes its books two days faster |
| `[Answer format]` | tables first, then 3 bullets; under 400 words; USD |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
You are my sales research partner for this chat. Use Draup for Sales for every fact.

ABOUT ME (edit these)
- My role: [e.g. Enterprise AE, North America retail]
- I sell: [software, services or both, e.g. services]
- What I sell: [e.g. cloud data-platform migration plus managed data engineering]
- Typical deal: [e.g. $250K–$1.5M, 6–9 months]
- Ideal customer: [e.g. Retail, 5,000+ employees, $1B+ revenue]
- Buyers: [e.g. CIO, Chief Data Officer; the CIO signs]
- Territory: [e.g. United States of America; target.com, kroger.com]
- Competitors: [companies or products, e.g. Accenture, Google BigQuery]
- Our customers: [e.g. Contoso Retail, Fabrikam Foods]
- Focus: [e.g. displacing incumbents]
- Proof point: [e.g. Contoso Retail closes its books two days faster]
- Answer format: [e.g. tables first, under 400 words]

STEPS (now)
1. Find each competitor and customer in Draup. Use the exact match; ask only if there is none or several. Record a product competitor with its maker.
2. Map What I sell to Draup business functions and workloads, dropping any that don't fit.

OUTPUT (now)
- 6 lines: me and what I sell; customer and buyers; territory; competitors (product → maker) and customers as Draup names; focus and proof point; format.
- The mapped workloads, then "Ready. Name an account."

RULES (every later answer; leave as is)
- Fill prompt inputs from ABOUT ME unless I override them; ask if one is missing.
- Use Draup for every fact; label outside knowledge. Date every number. Write "Not in Draup" for gaps; never guess. Label inferences "likely".
- Companies: find by website, confirm the parent, flag subsidiaries; resolve each name before listing. Retry an empty name once with Draup's spelling ("Accenture", not "Accenture plc"; "United States of America"; "Life Sciences"; business functions such as "IT" or "Supply Chain").
- When I've named competitors, check each account's whole stack for their products before writing why-this-matters.
- Narrow pulls by function or workload; show the top 10 first, then offer more.
- Executives: full profile title, not the seniority label (in banking and consulting VP and SVP are mid-level); 10 per page, 3 pages max; if Europe or the UK returns none, rerun without location; professional information only. Moves: about 10 latest per type, so narrow by workload.
- Money: annual, millions of reporting currency, fiscal years (can run ahead of the calendar); latest regional split only; check divestments before calling a drop over 5% a cut. IT and R&D spend are Draup estimates that often track revenue. Forecasts over 15% off the latest actual are model estimates.
- Tech: trust last-seen date and usage strength; ignore first-seen dates and "Generic" rows; say "fading", not "dropped". Ignore an account's own products if it sells technology.
- Hiring and news cover 12 months. Postings are openings, not hires; skip partial first and last months. Drop news noise (outages, stock chatter, charity, look-alikes, re-dated stories); the account must be the actor.
- Engagements and outsourced headcount are Draup estimates, not contracts. Priority tools and providers are "linked", not confirmed.
- Never use Draup's own customer or user data. End every answer with "Recommended next step" and "Gaps".

Confirm the 6-line summary, then apply ABOUT ME and the RULES to everything I ask in this chat.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Remember for this chat: I'm [My role]; I sell [I sell]: [What I sell] to [Ideal customer] in [Territory]; competitors [Competitors]; customers [Our customers]. Confirm in 6 lines and use these defaults.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Change my focus to expanding existing customers and confirm.
```

```text
Add Infosys and Databricks to my competitors and give their Draup names and makers.
```

```text
Run the one-page account brief on the first named account in my territory.
```

## Tips for better results

- Fill in "I sell": several prompts read a partner as a co-sell ally for software sellers but as an incumbent to displace for services sellers.
- List competitors as products when that is how you meet them (for example a cloud data platform). Claude records the maker so it can spot them in an account's tech stack.
- Use company websites and full country names; they match Draup most reliably.

## Related prompts

- [Claude Project instructions (recommended)](../../prompts/00-start-here/claude-project.md): Instructions for a Claude Project, so every chat in it knows who you are and follows the library's data rules without pasting anything.
- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Five short bullets you can read in the lobby: who they are, what just happened, where hiring is rising, the priority closest to your offer, and one question to ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_relevant_workloads`, `extract_entities`

Status: **tested live**. Prompt id: `setup-about-me`.

</details>

---

[Back to Start here](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
