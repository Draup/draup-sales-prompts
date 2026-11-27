[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Rival head-to-head in one industry

> **Two services firms compared in one industry and country by active engagements, shared and exclusive customers and workload mix, with the shared accounts to attack, the workloads where you lead and a named person at the top target.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning an industry campaign against a rival services firm, or deciding where your firm should focus versus a competitor. | Services, SI & Staffing Seller, Sales Leader & RevOps, Account Executive, Partnerships & Alliances, Marketing & ABM | Services sellers | 2–4 min | Outsourcing deals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Our firm]` | Wipro, or a second rival if your firm isn't in Draup |
| `[Competitor]` | Cognizant |
| `[Industry]` | Banking & Financial Services |
| `[Country]` | United States of America |
| `[Our accounts]` | paste a list (optional) |
| `[What I sell]` | data engineering and cloud managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive strategist for an IT services firm. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Our firm: [Draup name of your services firm, e.g. Wipro — or a second rival if yours isn't in Draup]
- Competitor: [services firm, e.g. Cognizant]
- Industry: [e.g. Banking & Financial Services]
- Country: [customer HQ country in full, e.g. United States of America]
- Our accounts (optional): [pasted list, if our firm isn't in Draup]
- What I sell: [one line, e.g. data engineering and cloud managed services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Shared accounts are where buyers already compare both firms; exclusive accounts show each fortress; workload mix shows credibility.

STEPS
1. Confirm Draup's names for both firms, industry and country.
2. Pull the provider ranking for [Industry] customers headquartered in [Country] (primary industry only): engagements and rank for both firms, plus the top 10 providers. Drop agencies, staffing and real-estate firms.
3. Pull the top 20 customers by engagements for each firm, same industry and country.
4. Match the lists by exact company name: Shared, Ours only, Theirs only. If I pasted Our accounts, use those for our side.
5. Pull the top 12 workloads by engagements for each firm, same industry and country, and each workload's share of the firm's total. Mark the workloads closest to [What I sell].
6. For each shared account, note who has more engagements and the gap.
7. For the top attack account, find it by website, pull its top 3 executives in the function closest to [What I sell] (one page of 10) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — "[Our firm]: N engagements (#rank); [Competitor]: N (#rank)" and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the top attack account, the action this week and the dated why-now; if none, say so.
- Table "Where to attack" (5): Customer | Ours | Theirs | Workload to lead with. Shared accounts where [Competitor] leads by 3x or less (editable default).
- Table "Workload mix" (top 10): Workload | Ours (share) | Theirs (share) | Edge. No edge called on catch-all workloads.
- "Where we lead": 3 workloads where our share is 5+ points higher (editable default), my offering's workloads first.
- Detail: top 10 providers, all shared accounts with gaps, and 5 fortresses each side.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Every count uses both the industry and country conditions; never report a total from a check that dropped one.
- Count shared accounts on exact names; flag near-matches separately.
- Leave misclassified customers and either firm's subsidiaries out of Where to attack; if a firm has under 5 customers here, widen to the region.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Active engagements (Draup-derived) are estimates, not signed contracts. Rank providers by them; never quote outsourced headcount.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Our firm] and [Competitor] in [Industry], [Country]. Lead with who's ahead and a named person at the top shared account to attack. Then the 5 attack accounts, workload mix and 3 workloads where we lead, all on active engagements.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [Shared account], show both firms' engagements by workload.
```

```text
Which executives at the top 3 attack accounts own [Workload]?
```

```text
Turn Where we lead into a one-page industry point of view.
```

## Tips for better results

- Shared accounts where the rival leads narrowly are usually the fastest share-of-wallet wins.
- If your firm isn't in Draup, paste your customer list; the overlap still works.

## Related prompts

- [A rival's customers you can win](../../prompts/10-outsourcing-and-services/competitor-customers.md): A ranked list of a rival's customers in your industry and country, how entrenched it is at each, and the 3 to attack first, with a named buyer at the best one.
- [A rival's footprint and your wedge](../../prompts/10-outsourcing-and-services/competitor-at-account.md): How deep a rival services firm is at the account (or, if it's absent, who really is), how it delivers, and the workloads where it's weakest: your wedge, with a named buyer and a dated why-now.
- [Who wins services work in a vertical](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_deals_service_provider_v3`, `get_deals_customer_v3`, `get_deals_workloads_v3`, `get_account_id`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `compete-vertical-head-to-head`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
