[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Compare candidate partners head to head

> **A weighted scorecard comparing 2–3 candidate partners in one industry and country on workload depth, technology experience, customer breadth, onshore delivery and momentum, with a pick, each candidate's main risk and who to call at the pick.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You have budget or capacity for one new partner in a segment and need to choose, or justify the choice to your leadership. Use partners-recruit-si-shortlist instead when you don't have names yet. | Partnerships & Alliances, Sales Leader & RevOps | Everyone | 4–6 min | Outsourcing deals, Talent flow & locations, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Candidates]` | Cognizant, Capgemini, Wipro |
| `[Vertical]` | Life Sciences |
| `[Country]` | United States of America |
| `[Workload]` | Data Engineering |
| `[Technology]` | Databricks |
| `[Weights (optional)]` | workload 30, technology 25, breadth 20, onshore 10, momentum 15 |
| `[What I sell]` | clinical data platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner-selection analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Candidates: [2–3 services firms as Draup spells them, e.g. Cognizant, Capgemini, Wipro]
- Vertical: [Draup industry, e.g. Life Sciences]
- Country: [Customer HQ country in full, e.g. United States of America]
- Workload: [e.g. Data Engineering; a business function is fine, I'll map it]
- Technology: [Our platform or a rival's, e.g. Databricks]
- Weights (optional): [Editable default: workload depth 30, technology 25, customer breadth 20, onshore delivery 10, momentum 15]
- What I sell: [One line, e.g. clinical data platform — skip if you ran the start-here prompt]

STEPS
1. Confirm Draup's spelling of each candidate; list any sister brand separately, unmerged. If I gave a business function, map it to its 1–2 main workloads.
2. In one lookup, pull engagements for all candidates among customers with primary industry [Vertical] and HQ in [Country]. Repeat once for [Workload] only, and once for engagements that mention [Technology].
3. For each candidate, pull its top 5 customers in the segment; compute the share of its segment engagements held by its top 2.
4. For each candidate, pull delivery locations for the segment; compute the share delivered in [Country] (onshore).
5. For each candidate, pull headcount growth over Draup's latest 12-month workforce window.
6. Score each criterion 0–100 relative to the best candidate (best = 100, others = value ÷ best × 100). For customer breadth, use 100 minus the top-2 share before scaling. Apply the weights and total.
7. People and timing: pull the pick's top 3 leaders for [Vertical] or alliances (full profile titles) and its most important news item from the last 90 days (client wins, acquisitions, new alliances; analyst rankings and awards are context, not a why-now).

OUTPUT
- Bottom line: 2 sentences — the pick and what it means for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Scorecard": Criterion | Weight | one column per candidate showing raw value (score) | then a Total row. Criteria: Workload depth ([Workload] engagements in segment), Technology ([Technology]-related engagements), Customer breadth (top-2 share), Onshore delivery (% in [Country]), Momentum (headcount growth %).
- "Pick": one candidate, 3 reasons tied to numbers.
- "Risk per candidate": one line each (e.g. concentration, offshore-heavy, thin technology work).
- Gaps: what Draup didn't have — worth asking each candidate.
- Detail: "Sensitivity" (does the pick change if the technology weight doubles? who wins then) and "If you can sign two" (the most complementary pair and why).

RULES
- If a candidate has fewer than 10 engagements in the segment (editable default), mark its share-based scores "insufficient data" and score them 0, saying so.
- Say plainly when the pick is driven mainly by scale, and show the runner-up's strongest criterion.
- Never present the scorecard as Draup's rating; it's your weighted read of Draup data.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Rank providers by engagements yourself.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named leader at the pick, dated why-now) first. Compare [Candidates] in [Vertical], [Country]: engagements in [Workload] and mentioning [Technology], top-2 customer share, onshore share, headcount growth. Weighted scorecard, pick, sensitivity check, each one's risk.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Rerun the scorecard with technology weighted 40 and workload 20.
```

```text
Run the momentum check on the pick before we sign.
```

```text
Draft a one-paragraph recommendation for my VP with the scorecard attached.
```

## Tips for better results

- Change the weights before you look at the result, not after. It keeps the choice honest.
- A firm with most of its segment work at one or two customers can still be the right partner, but only if those customers are on your target list.

## Related prompts

- [Which SIs to recruit in an industry](../../prompts/13-partners-and-alliances/recruit-si-shortlist.md): A ranked shortlist of systems integrators that deliver your workload in one industry and already work with your technology, with anchor customers, delivery hubs, the one to recruit first and who to call there.
- [Is this partner rising or slowing?](../../prompts/13-partners-and-alliances/momentum-check.md): A Rising, Steady or Slowing verdict on a prospective partner, scored from its hiring, headcount growth, client wins, acquisitions and footprint in your industry and country, with who to talk to there.
- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Who wins services work in a vertical](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers, where your firm ranks, and who to call first.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_deals_service_provider_v3`, `get_deals_customer_v3`, `get_deals_service_provider_location_v3`, `accounts_talent_flow_top_metrics_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `partners-compare-candidates`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
