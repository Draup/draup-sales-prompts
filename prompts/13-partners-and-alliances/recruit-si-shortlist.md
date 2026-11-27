[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which SIs to recruit in an industry

> **A ranked shortlist of systems integrators that deliver your workload in one industry and already work with your technology, with anchor customers, delivery hubs, the one to recruit first and who to call there.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're building or refreshing a partner programme for an industry and need to know which SIs actually have the practice. Use "Compare candidate partners head to head" instead when you already have 2–3 names. | Partnerships & Alliances, Sales Leader & RevOps, Marketing & ABM | Software sellers | 4–6 min | Outsourcing deals, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Insurance |
| `[Workload]` | Data Engineering |
| `[Technology]` | Snowflake |
| `[Territory (optional)]` | United States of America |
| `[Our current partners (optional)]` | Tailspin Partners |
| `[What I sell]` | data observability software for insurers |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner-programme strategist recruiting systems integrators (SIs). Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Vertical: [Draup industry, e.g. Insurance]
- Workload: [The type of work my product serves, e.g. Data Engineering; a business function is fine, I'll map it]
- Technology: [Our platform or a rival's, as Draup names it, e.g. Snowflake]
- Territory (optional): [Customer HQ country in full, e.g. United States of America; default: my territory from setup; say "worldwide" for all]
- Our current partners (optional): [e.g. Tailspin Partners]
- What I sell: [One line, e.g. data observability software for insurers; skip if saved in setup]

STEPS
1. Use Draup's exact names; map a business function to its 1–2 main workloads. Say which you used.
2. Rank providers by [Workload] engagements for customers in [Vertical] (HQ in [Territory]); keep the top 15, removing and listing agencies, staffing firms and captives.
3. Rank providers again for the same industry and territory by engagements that mention [Technology], top 15. Then count all industry engagements mentioning [Technology], for each provider's share.
4. Pick 3 candidates high in both lists, current partners first. Pull each one's top 5 customers for [Technology] work in the industry.
5. For the same 3, pull delivery locations for [Workload] in the industry. Keep the top 5 metros, grouped onshore (customers' country), nearshore or offshore; onshore share = onshore engagements ÷ all 5.
6. People and timing: page through the recruit-first SI's Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances, partnerships or [Technology]; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
- Bottom line: 2 sentences — the SI to recruit first and why.
- Recommended next step: a person from step 6 (name and title), what to do, and the dated why-now; if none, say so.
- "Shortlist" (top 10): Rank | Provider (current partners marked) | [Workload] engagements | [Technology]-related engagements (share of industry total) | Verdict.
- Verdict: Recruit first (top 10 in both lists and 3+ [Technology]-related engagements), Practice partner (strong in the workload, little [Technology]), Technology specialist (strong in [Technology], thin in the workload) or Watch.
- "Top 3 profiles": Provider | Top customers for [Technology] | Single-account depth? | Top delivery hubs | Onshore share.
- Gaps: what Draup didn't have — ask in the first partner call.
- Detail: "Shared customers" (customers that appear for 2+ of the top 3) and "Removed" (Provider | Reason).

RULES
- Flag "single-account depth" when one customer holds over half a provider's [Technology]-related engagements; never "Recruit first" on that alone.
- Say "[Technology]-related", never "certified".
- Under 20 [Technology] engagements (editable)? Retry with the vendor's name, then drop the country; say which worked.
- Mark delivery metros that don't fit the provider "check location".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Rank providers by engagements yourself.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named SI leader, dated why-now) first. Which providers lead [Workload] in [Vertical] in [Territory], and which have [Technology]-related work? Top 10; Recruit first needs both lists and 3+ [Technology] engagements.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft a recruitment email to the person in the next step, citing two facts from the shortlist.
```

```text
Run the same shortlist for [second Technology] so I can see who works with both.
```

```text
For [Provider], which of its [Vertical] customers don't run [Technology] yet? That's our joint pipeline.
```

## Tips for better results

- Rank on the technology list as well as the workload list: a firm that is huge in the workload but rarely touches your technology needs heavy enablement.
- Mid-size specialists often show up high in the technology list. They can be easier to win as partners than the largest firms.
- SI executives are tagged IT Services, not by industry, so the answer finds industry and alliance leaders by their titles; if none show up, ask the SI for its industry lead.

## Related prompts

- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Who wins services work in a vertical](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Compare candidate partners head to head](../../prompts/13-partners-and-alliances/compare-candidates.md): A weighted scorecard comparing 2–3 candidate partners in one industry and country on workload depth, technology experience, customer breadth, onshore delivery and momentum, with a pick, each candidate's main risk and who to call at the pick.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_deals_service_provider_v3`, `deals_get_data_count`, `get_deals_customer_v3`, `get_deals_service_provider_location_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `partners-recruit-si-shortlist`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
