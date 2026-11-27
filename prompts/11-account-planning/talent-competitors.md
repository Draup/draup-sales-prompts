[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Who they lose talent to

> **The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, credible benchmark peers, and who to raise it with.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want peers the buyer watches for talent, or a benchmark set that isn't just the annual-report competitor list. | Account & Customer Success Manager, Account Executive, Marketing & ABM | Everyone | 1–2 min | Talent flow & locations, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Business function (optional)]` | IT |
| `[What I sell]` | developer productivity software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my account intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function (optional): [e.g. IT; blank uses the function closest to What I sell]
- What I sell: [One line, e.g. developer productivity software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull talent flow by company for [Business function] (or the function closest to [What I sell]): companies it loses people to and companies it hires from.
3. Remove the account's own subsidiaries and sister companies, "Self Employed", and blank or unknown employers. Mark staffing and IT services firms.
4. Join the two lists and work out net flow per company (hired from minus lost to).
5. People and timing: at [Company], pull the top 3 leaders in the business function closest to [What I sell] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — who it competes with for talent and what that means for [What I sell].
- Recommended next step: a person from step 5 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- Window line: "Talent flow for [months], [function]".
- "Loses talent to" (top 10): Company | People lost | People hired from them | Net.
- "Hires talent from" (top 10): Company | People hired | People lost to them | Net.
- "Talent rivals": companies in both top 10s — they compete for the same skills, which makes them good benchmark peers. They aren't necessarily business rivals.
- "Why this matters for [What I sell]": 2–3 bullets (e.g. losing engineers to a tech employer: show what that employer's teams use; staffing firms high in the list: likely contractor dependence).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Counts are people moves Draup observed in the window, not total headcount.
- Staffing and IT services firms usually mean contractors moving, not competition; keep them out of Talent rivals.
- If the function returns nothing, rerun for the whole company and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Label inferences (buyer role, intent, fit) "likely".
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 380 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. Which companies does [Company] lose the most people to, and hire the most from? Top 10 each way with net flow, excluding its subsidiaries and staffing firms. State the window.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Benchmark [Company] against its top 3 talent rivals on hiring and growth.
```

```text
Which senior leaders left [Company] for these rivals recently?
```

```text
Which skills are they losing most to [rival]?
```

## Tips for better results

- Talent rivals are often better benchmark peers than the competitors named in an annual report.
- The data lags by a few months, so it describes the recent past, not this month.

## Related prompts

- [Customer alumni now at your targets](../../prompts/11-account-planning/follow-champions.md): Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.
- [AI readiness against close peers](../../prompts/11-account-planning/ai-readiness.md): A read on the account's AI hiring, priorities, new tools and outsourced AI work, its AI hiring compared with up to 4 close peers, and who to raise it with.
- [Benchmark an account against its peers](../../prompts/06-prospecting-and-lists/peer-benchmark.md): How an account compares with its closest peers on growth, hiring in what you sell, your competitors in the stack and recent news, with discovery questions and who to call.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_talent_flow_insights_companies_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-talent-competitors`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
