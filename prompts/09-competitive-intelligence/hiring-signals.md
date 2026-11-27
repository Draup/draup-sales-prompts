[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What a rival is building next

> **What a competitor is likely building or selling next, read from its own job ads (rising workloads, skills and new roles in the last 5 months), with proof postings, a talk track and the named person to brief.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a roadmap or positioning review, or when you suspect a rival is entering your space. | Presales & Solutions, Sales Leader & RevOps, Marketing & ABM, Partnerships & Alliances, Account Executive | Everyone | 4–6 min | Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | databricks.com |
| `[What I sell]` | AI agents for sales teams |
| `[Focus area]` | Artificial Intelligence & Data Science (optional) |
| `[Account to defend or win]` | visa.com (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence analyst who reads job ads for strategy. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. databricks.com]
- What I sell: [one line, e.g. AI agents for sales teams — skip if you ran the start-here prompt]
- Focus area (optional): [a workload, i.e. a type of work, e.g. Artificial Intelligence & Data Science]
- Account to defend or win (optional): [website of a live deal or key customer, e.g. visa.com]

CONTEXT (why this matters)
Companies hire 6–12 months ahead of launches. The signal is change, not volume; skills spiking in lockstep or on every posting are tagging artefacts.

STEPS
1. Find [Competitor] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. Pull hiring by workload (12 months, global, top 15) with monthly trends. Compare the last 5 full months with the 5 before: Rising (+25% or more, editable default), Steady or Falling. Draw no conclusions from catch-all workloads (Account Management, Project/Programs Management).
3. Pull the top 20 skills within [Focus area], or else the workloads closest to [What I sell], with trends; flag Rising skills.
4. Pull job titles trending up (12 months); if fewer than 3, use the rising workloads.
5. For the 2 most surprising rising skills or titles, pull 4 recent postings each and read the responsibilities. Drop a skill as an artefact if it appears in unrelated roles (HR, finance) or rises in lockstep with an unrelated skill.
6. Turn what survives into build signals: the offer or segment the hiring points to.
7. Dated trigger: [Competitor]'s most important news item from the last 90 days that bears on the build signals.
8. If I gave [Account to defend or win], find it by website and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — what they're likely building and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at [Account to defend or win], the action this week, and [Competitor]'s dated move as the why-now; with no account given, name the role to brief.
- Table "Build signals" (up to 3): Likely building or selling | Evidence | Threat or opening | Likely timing.
- Table "Where hiring is moving" (top 10): Workload | Postings (12 mo) | Last 5 vs prior 5 | Read.
- "Talk track": 2 bullets for my team (50 words max).
- Detail: rising skills and titles (kept or dropped as artefact) and proof postings (Date | Title | Location | quote).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- A signal needs two kinds of evidence (e.g. a rising skill plus a posting naming the offer); otherwise label it "weak".
- Never infer revenue or customers from postings.
- Under 300 postings in 12 months is a small sample; keep conclusions tentative.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
What is [Competitor] building next, judged from its job ads? Lead with the bottom line and who to brief, then rising workloads and roles (last 5 full months vs prior 5), proof postings and up to 3 build signals.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show where those rising roles are based: which metros and countries.
```

```text
Compare this with what [Competitor] said on its latest earnings call.
```

```text
Write a one-page internal brief for product marketing on the top build signal.
```

## Tips for better results

- New job titles (e.g. forward-deployed roles for a new segment) are usually stronger signals than skill counts.
- Read 3–4 actual postings before acting on any skill spike.
- Add a live deal as the account and the next step names the person to brief there.

## Related prompts

- [Which tools their job ads are building](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press, with a named person to call.
- [How a rival's strategy is shifting](../../prompts/09-competitive-intelligence/strategy-shift.md): How a competitor's stated priorities moved across its last three earnings calls, the acquisitions, leaders and cuts behind each shift, what changes in your deals and who to brief.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_hiring_demand_category_v3`, `accounts_hiring_job_postings_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `compete-hiring-signals`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
