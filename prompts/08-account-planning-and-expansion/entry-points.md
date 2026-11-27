# Entry points and whitespace

**The five best ways into the account for what you sell, each with dated evidence, incumbents and the likely owner.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You know the account but need a concrete first or next deal to work on. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 2–4 min | Priorities & opportunities, Executives & movement |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | bmw.com |
| `[Business function or Workload]` | Supply Chain |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my pursuit strategist. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. bmw.com]
- Business function or Workload: [Required, e.g. Supply Chain or Demand Management]
- What I sell: [One line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Find the company by its website and confirm it is the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull Draup's opportunities (potential initiatives) for the account, always limited to [Business function or Workload], never unfiltered.
3. Drop initiatives unrelated to [What I sell], and, if the account sells technology, initiatives about its own products. Rank the rest by fit, then by how recent the evidence is.
4. For the top 5, note the initiative, its evidence (source and date), and incumbent tech and providers.
5. Pull key executives in the same function separately (10 per page, up to 3 pages) and match up to 2 per entry point by workload or title.

OUTPUT
- Bottom line: 2 sentences — the best way in and why now.
- "Entry points": # | Initiative | Evidence and date | Incumbent tech | Incumbent providers | Likely owner(s) | Our opening (one line).
- "Lead with": the single best entry point and why, in two sentences.
- "Dropped as unrelated": a one-line list, so I can bring any back.
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Executives are matched by function, not confirmed owners; say so.
- If no executives come back, list the titles to target. If the function returns nothing, try the closest Draup workload.
- Use each person's full profile title, not the seniority label. In banking and consulting, VP/SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Use professional information only (name, title, employer, Draup profile link). No personal contact details; don't infer personal details or past buying relationships.
- Label anything you infer (buyer role, intent, fit) as "likely".
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Find the top 5 entry points at [Company] for [What I sell] from Draup's opportunities in [Business function or Workload]: initiative, dated evidence, incumbent tech and providers, and the executive who likely owns it.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a discovery question for each entry point, citing its evidence.
```

```text
Which providers would we compete with on entry point 1, and how strong are they here?
```

```text
Turn 'Lead with' into a 100-word email to the likely owner.
```

## Tips for better results

- Always narrow by function or workload. Unfiltered, this pulls far too many items.
- If you save your solution offering in the Draup platform, Draup can also surface entry points from executive moves and intent signals.

## Related prompts

- [Draft an account plan](../../prompts/08-account-planning-and-expansion/account-plan.md): An account plan in eight parts: snapshot, their strategy in their own words, buying committee, incumbents, ranked expansion plays, risks and a 90-day plan, plus an optional short SWOT.
- [Who to partner with vs replace, by priority](../../prompts/06-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it, and whether to partner, displace or walk into an open door.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_opportunities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `plan-entry-points`.

</details>

[Back to Account planning and expansion](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
