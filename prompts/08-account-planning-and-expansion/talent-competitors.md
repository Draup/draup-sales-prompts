# Talent rivals: who they lose people to

**The companies an account loses people to and hires from, with net flow: the employers it competes with for skills, and credible peers to benchmark against.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want peers the buyer watches for talent, or a benchmark set that isn't just the annual-report competitor list. | Account & Customer Success Manager, Account Executive, Marketing & ABM | Everyone | 1–2 min | Talent flow & locations |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | walmart.com |
| `[Business function (optional)]` | IT |
| `[What I sell]` | developer productivity software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my account intelligence analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. walmart.com]
- Business function: [Optional, e.g. IT; leave blank for the whole company]
- What I sell: [One line, e.g. developer productivity software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull talent flow by company (and function, if given): companies it loses people to and companies it hires from.
3. Remove the account's own subsidiaries and sister companies, "Self Employed", and blank or unknown employers. Mark staffing and IT services firms.
4. Join the two lists and work out net flow per company (hired from minus lost to).

OUTPUT
- Bottom line: 2 sentences — who it competes with for talent and what that means for [What I sell].
- Window line: "Talent flow for [months], [function or whole company]".
- "Loses talent to" (top 10): Company | People lost | People hired from them | Net.
- "Hires talent from" (top 10): Company | People hired | People lost to them | Net.
- "Talent rivals": companies in both top 10s — they compete for the same skills, which makes them good benchmark peers. They are not necessarily business rivals.
- "Why this matters for [What I sell]": 2–3 bullets (e.g. losing engineers to a tech employer: show what that employer's teams use; staffing firms high in the list: likely contractor dependence).
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Counts are people moves Draup observed in the window, not total headcount.
- Staffing and IT services firms usually mean contractors moving, not competition; keep them out of Talent rivals.
- If a function returns nothing, rerun for the whole company and say so.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Talent-flow data ends about 3 months ago; state the months covered.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Which companies does [Company] lose the most people to, and hire the most from? Top 10 each way with net flow, excluding its own subsidiaries and staffing firms. State the window.
```

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

- [Customer alumni on the move](../../prompts/08-account-planning-and-expansion/follow-champions.md): Senior people who recently left one of your customers, where they went, and which new employers are on your target list, with any champions you name flagged first.
- [AI readiness vs peers](../../prompts/08-account-planning-and-expansion/ai-readiness.md): A deep read on the account's AI hiring, priorities, new tools and outsourced AI work, then its AI hiring compared with up to 4 close peers.
- [Benchmark an account against peers](../../prompts/05-prospecting-and-lists/peer-benchmark.md): One table comparing an account with its closest peers on growth, hiring, workforce, footprint and recent news, plus where it leads and where to ask questions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_talent_flow_insights_companies_v3`

Status: **tested live**. Prompt id: `plan-talent-competitors`.

</details>

[Back to Account planning and expansion](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
