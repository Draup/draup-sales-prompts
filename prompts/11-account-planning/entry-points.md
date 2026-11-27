[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Best entry points: expand or new

> **The five best ways in for what you sell, each marked Expand (we already serve it) or New, with dated evidence, incumbents, any installed competitor and the likely owner.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You know the account (often an existing customer) and need a concrete next deal to work on. Use "Draft an account plan" instead for a full plan. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Services, SI & Staffing Seller | Everyone | 2–4 min | Priorities & opportunities, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | bmw.com |
| `[Business function or Workload]` | Supply Chain |
| `[What I sell]` | supply-chain planning software |
| `[Already deployed (optional)]` | demand planning in Europe |
| `[Competitor (optional)]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my pursuit strategist. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Company: [Website, e.g. bmw.com]
- Business function or Workload: [e.g. Supply Chain or Demand Management]
- What I sell: [One line, e.g. supply-chain planning software; skip if saved in setup]
- Already deployed (optional): [What we already run there, e.g. demand planning in Europe; blank for a prospect]
- Competitor (optional): [e.g. Kinaxis, o9 Solutions]

STEPS
1. Find the company by website (no result: try its name once and show the match score). Confirm it's the parent, not a subsidiary or sister company; if several match, ask me. Use Draup's exact name from then on.
2. Map [Business function or Workload] to the 1–2 workloads closest to [What I sell] and say which. Pull the account's potential initiatives narrowed to them (if empty, to the function; never unlimited).
3. Drop initiatives unrelated to [What I sell], templates that don't fit the account's industry and, if it sells technology, initiatives about its own products. Mark any initiative we already serve (from Already deployed) "Expand", the rest "New". Rank by fit, then by how recent the evidence is.
4. For the top 5, note the initiative, its evidence (source and date), incumbent tech, and only providers that plausibly deliver this work.
5. Check the whole tech stack for [Competitor] products in the same workloads. Rate [Competitor]: Red for High usage in my workloads; Amber for Medium there or newly detected in 12 months; otherwise Green, still listed. A services firm: 30%+ of active engagements in my workloads Red, 10–29% Amber, under 10% Green.
6. Pull leaders in the same function (10 per page, up to 3 pages) and match up to 2 per entry point by workload or title.
7. Timing: the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the best way in and why now.
- Recommended next step: one person from step 6 (name and title), what to do, and why now (the step-7 item or another dated fact). If none turned up, say so.
- "Entry points": # | Initiative (Expand or New) | Evidence and date | Incumbents (tech; providers) | Likely owner.
- "Competitor in these workloads": Product | Maker | Usage | Last seen | Rating. Write "none found" if empty.
- "Lead with": the single best entry point and why, in two sentences.
- Gaps: what Draup didn't have, to ask in discovery.
- Detail: "Dropped as unrelated" in one line, so I can bring any back.

RULES
- Owners are matched by function and workload, not confirmed; label them "likely".
- Providers are linked, not confirmed: say "linked" and leave out firms that don't do this work (publishers, architects).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust usage strength and last-seen date, not confidence or first-seen; ignore "Generic" rows; a rival counts only at High or Medium usage.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- If an account sells technology or services, drop priorities, news and hiring about what it sells; never pitch it its own category.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 430 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named owner, dated why-now) first. Top 5 entry points at [Company] for [What I sell] in [Business function or Workload]: initiative, Expand or New (we run [Already deployed]), dated evidence, incumbents, [Competitor] installed, likely owner.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a discovery question for each entry point, citing its evidence.
```

```text
Which providers would we compete with on entry point 1, and how strong are they here?
```

```text
Turn 'Lead with' into a 100-word email to the person in the next step.
```

## Tips for better results

- For a customer, say what you already run there. The answer then separates expansion from new business.
- Name the competitors you meet. An installed rival in the same workload changes the play from land to displace.
- If you save your solution offering in the Draup platform, Draup can also surface entry points from leadership moves and intent signals.

## Related prompts

- [Draft an account plan](../../prompts/11-account-planning/account-plan.md): An account plan led by the bottom line, the first play and who to call: buying committee, ranked expansion plays, incumbents (including installed competitors), risks and a 90-day plan.
- [Which providers to partner with or replace](../../prompts/10-outsourcing-and-services/partner-map.md): For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_opportunities_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-entry-points`.

</details>

---

[Back to Account planning and expansion](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
