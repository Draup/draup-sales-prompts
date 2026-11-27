[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Do layoffs open an outsourcing deal?

> **Where and in which roles a company has cut jobs in the last 12 months, read as a possible outsourcing trigger, plus which skills are now more available in the market.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Preview: needs the Draup for Talent connector; not yet live-tested. A target announces cuts, or you want to know whether a restructuring creates an outsourcing or managed-services opening. | Services, SI & Staffing Seller, SDR / BDR, Account Executive | Services sellers | 2–4 min | Talent cost & supply, News signals |

> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully.

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | 3m.com |
| `[Location (optional)]` | United States of America |
| `[Roles of interest (optional)]` | software engineer, QA |
| `[What I sell]` | managed engineering services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my services-pursuit analyst. Use the Draup for Talent connector for layoff data, and the Draup for Sales connector for company facts, executives and news. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. 3m.com]
- Location (optional): [country or metro, e.g. United States of America]
- Roles of interest (optional): [e.g. software engineer, QA]
- What I sell: [one line, e.g. managed engineering services — skip if you ran the start-here prompt]

CONTEXT (optional)
Cuts in one function plus hiring in another often mean work is moving, not disappearing; that's the services opening. Buyers react badly to outreach that leads with job losses, so the message must be about the business problem.

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary or a similarly named firm. If unclear, ask me.
2. Pull the layoffs Draup records at [Company] in the last 12 months, in [Location] if given, grouped by month.
3. Break the same records down by job title (top 10) and location (top 10). Show any roles of interest separately.
4. Map the top titles to business functions (IT, engineering, customer service, finance) and name the functions with the deepest cuts.
5. Pull layoff, restructuring and site news on [Company] from the last 90 days to explain the cuts.
6. Pull the top 3 executives in the function with the deepest cuts (or the function closest to What I sell).

OUTPUT
- Bottom line: 2 sentences — the scale and focus of the cuts, and whether they point to an opening for [What I sell].
- Recommended next step: who to take it to (name and title from step 6), what to do, and why now (one dated fact from step 5). If none is found, say so.
- "Roles affected": Job title | Count | Function. Top 10.
- "Possible outsourcing trigger": 3 bullets on whether work looks outsourced, consolidated or automated, and what [What I sell] could take on. Mark each "likely".
- Detail: by month; by location (top 10); skills now more available in the market, for your delivery hiring plans; news used.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Counts come from profiles Draup holds with a layoff date: a sample that shows the pattern, not the official total. Say so.
- Report counts only. Never name or list individuals, describe people as a pool or bench, or suggest contacting them about the company.
- Keep any outreach about the business problem, not the layoffs.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. No data: write "Not in Draup"; never fill gaps from memory.
- If the Draup for Talent connector is missing or returns an access error, stop and tell me; never estimate from memory.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alike names and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. If sources conflict on a name or number, say so; single-source figures are unverified.
- Use full profile titles. No economic buyer? Search once for Chief, EVP and CIO titles. Leadership data lags about 3 months; professional information only.
- Never return a blank table: say what came back empty and use the fallback; at a big company, warn the work may be in-house or the data thin.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: does [Company]'s last 12 months of layoffs (by month, top titles, top locations; counts only, no names) point to an outsourcing opening for [What I sell], and who to take it to?
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which of these functions does [Company] already outsource, and to whom?
```

```text
Draft a value-led note to the executive named above that doesn't mention the layoffs.
```

```text
Compare with [Peer company]'s layoffs over the same 12 months.
```

## Tips for better results

- Cuts in one function plus hiring in another often mean work is moving, not disappearing. That's the services opening.
- Keep outreach about the business problem, not the cuts. Buyers often react badly to messages that lead with job losses.

## Related prompts

- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): An Act, Watch or Skip verdict and up to 5 real triggers from the last 90 days, kept or dropped with what you sell in mind (incidents and regulatory inquiries count if they bear on your offer), each with a named owner and a source count.
- [Is outsourced work coming back in-house?](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house — re-insourcing risk, capability gap or cost takeout — plus fast-growing in-house teams outside its outsourced list.
- [Renewal risk check (red, amber, green)](../../prompts/11-account-planning/risk-check.md): A Red/Amber/Green risk table for one customer — your named sponsor, senior exits, layoffs, growth, installed and new competitor products in your workloads, negative news — with an overall rating and two actions.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `visualize_layoff_date`, `visualize_job_title`, `visualize_locations`, `build_news_filters_v3`, `get_signal_news_v3`, `accounts_executives_key_executives_v3`

Status: **documented, not live-tested**. Prompt id: `talent-layoff-pool`.

</details>

---

[Back to Talent cost and location](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
