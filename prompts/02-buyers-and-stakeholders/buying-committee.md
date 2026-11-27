# Map the buying committee

**A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before multi-threading an account, or when you only know one contact. | Account Executive, SDR / BDR, Account & Customer Success Manager, Presales & Solutions | Everyone | 2–4 min | Executives & movement, Priorities & opportunities |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Business function or Workload]` | IT, or Artificial Intelligence & Data Science |
| `[Region]` | United States of America (optional) |
| `[What I sell]` | enterprise AI platform and services |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my sales stakeholder analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Business function or Workload: [e.g. IT, or Artificial Intelligence & Data Science]
- Region: [optional, e.g. United States of America]
- What I sell: [one line, e.g. enterprise AI platform and services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull key executives for the function or workload, 10 per page, up to 3 pages, with region only if I gave one.
3. If a workload returns fewer than 5 people, add the 2 closest workloads and say which. Drop clear title–function mismatches.
4. Pull priorities for the same function or workload to match leaders to initiatives.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- One line: people found, pages checked, people kept.
- "Buying committee": Rank | Name | Full title | Unit or brand (flag subsidiaries) | Location | Budget control | Likely role | Linked priority + quarter | LinkedIn. Up to 12, ranked by role, then budget control, then title.
- Likely roles: Economic buyer, Technical buyer, Champion candidate, Influencer, Potential blocker (e.g. incumbent-tool owner, security, procurement).
- "Roles with no clear person": the titles to look for.
- Recommended next step in two parts, each with one dated fact: "Entry point" (the likely champion to open with, and how) and "Sponsor to reach later" (the likely economic buyer, and what you need first).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Economic buyer and champion are candidates, never confirmed.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level (if none appears, say so in Gaps).
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- Professional information only (name, title, employer, Draup's profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Map the buying committee at [Company] for [Business function or Workload]: up to 12 people with full title, unit, location, budget control and likely role (economic buyer, technical buyer, champion, influencer, potential blocker), plus an entry point and a sponsor.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Profile the entry-point contact and give me 2 openers.
```

```text
Which of these people joined in the last 6 months?
```

```text
Do any of them have past companies that are our customers?
```

## Tips for better results

- Use a workload (e.g. Cybersecurity) when your offer is narrow; use a function (e.g. IT) for a broad map.
- Opening cold with the economic buyer often fails. Start with the entry point and earn the sponsor meeting.

## Related prompts

- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive and two openers tied to the account's current priorities.
- [Warm paths among current leaders](../../prompts/02-buyers-and-stakeholders/warm-paths-current-leaders.md): Senior leaders at the account who used to work at your customers, partners or your own company, so you can ask for a warm intro.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet pre-filled with what Draup can show (metrics, buyer candidates, pain, competition) and clear 'must discover' flags for the rest.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`

Status: **tested live**. Prompt id: `people-buying-committee`.

</details>

[Back to Buyers and stakeholders](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
