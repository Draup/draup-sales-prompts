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
| `[Our firm]` | Wipro (or "not in Draup") |
| `[Competitor]` | Cognizant |
| `[Industry]` | Banking & Financial Services |
| `[Country]` | United States of America (default: my territory) |
| `[Our accounts and strengths]` | paste accounts and workloads we lead in (optional) |
| `[What I sell]` | data engineering and cloud managed services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my services competitive strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Our firm: [Draup name, e.g. Wipro; or "not in Draup: Infosys" to compare two rivals]
- Competitor: [services firm, e.g. Cognizant]
- Industry: [e.g. Banking & Financial Services]
- Country: [customer HQ country in full, e.g. United States of America; default: my territory]
- Our accounts and strengths (optional): [if our firm isn't in Draup: accounts and workloads we lead in]
- What I sell: [one line, e.g. data engineering and cloud managed services — skip if you ran the start-here prompt]

CONTEXT (why this matters)
Buyers already compare both firms at shared accounts.

STEPS
1. Confirm Draup's names for both firms, industry and country.
2. Pull the provider ranking for [Industry] customers headquartered in [Country] (primary industry): both firms' engagements and rank, plus the top 10. Drop agencies, staffing and real-estate firms.
3. Pull each firm's top 20 customers (same industry and country) and match by exact name: Shared, Ours only, Theirs only; note each shared account's leader and gap. Pasted Our accounts are our side; if Our firm is "not in Draup" and I pasted none, compare the two named rivals. Merge subsidiaries into parents.
4. Pull each firm's top 12 workloads, same industry and country, with each one's share of the firm's total; mark mine.
5. For the top attack account, find it by website (else by name, showing match and score), pull its top 3 executives in the function closest to [What I sell] (one page of 10) and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — "[Our firm]: N engagements (#rank); [Competitor]: N (#rank)" and what it means for me.
- Recommended next step: a named person (name, full title) at the top attack account, the action this week and the dated why-now (or say none).
- Table "Where to attack" (5): Customer | Ours | Theirs | Workload to lead with: shared accounts where [Competitor] leads by 3x or less (editable default).
- Table "Workload mix" (top 10): Workload | Ours (share) | Theirs (share) | Edge (none on catch-alls).
- "Where we lead": up to 3 workloads where our share is 5+ points higher (editable default), mine first; say if none.
- Our firm not in Draup: label columns by firm name, never "Ours"; retitle "Where to attack" "Where a challenger fits" (shared accounts where the two are close, plus thin workloads); "Where we lead" only from my pasted accounts and strengths, else skip.
- Detail: top 10 providers, shared accounts with gaps, 5 fortresses each side.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Every count uses both industry and country.
- Leave misclassified customers and either firm's subsidiaries out of Where to attack; under 5 customers for a firm? Widen to the region.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Active engagements (Draup-derived) are estimates, not contracts; rank providers by them and never quote outsourced headcount.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 450 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Compare [Our firm] and [Competitor] in [Industry], [Country]. Lead with who's ahead and a named person at the top shared account to attack. Then 5 attack accounts, workload mix and where we lead, all on active engagements.
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
- If your firm isn't in Draup, write "not in Draup" and paste your accounts and strengths; the answer compares the two rivals and shows where a challenger fits.

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
