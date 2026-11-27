[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this partner rising or slowing?

> **A Rising, Steady or Slowing verdict on a prospective partner, scored from its hiring, headcount growth, client wins, acquisitions and footprint in your industry and country, with who to talk to there.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you sign, renew or put marketing funds behind a services partner. Use partners-compare-candidates instead to choose between several. | Partnerships & Alliances, Sales Leader & RevOps | Everyone | 2–4 min | Outsourcing deals, Hiring & job postings, Talent flow & locations, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Partner]` | hcltech.com |
| `[Vertical]` | Automotive |
| `[Country]` | Germany |
| `[What I sell]` | software-defined vehicle testing platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my partner due-diligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Partner: [Website of the services firm, e.g. hcltech.com]
- Vertical: [Draup industry where we'd work together, e.g. Automotive]
- Country: [Customer HQ country in full, e.g. Germany]
- What I sell: [One line, e.g. software-defined vehicle testing platform — skip if you ran the start-here prompt]

STEPS
1. Find the partner by website and confirm the parent, not a regional unit.
2. Pull its customer summary: active customers, engagements and top 3 customers overall.
3. Pull 12 months of monthly job postings. Compare the average of the last 5 full months with the 5 before. If one month more than doubles the one before and stays there (editable default), call it a "step change" that may reflect wider data coverage, not only demand.
4. Pull headcount growth over Draup's latest 12-month workforce window (it ends about 3 months ago; say the dates).
5. Search 12 months of deals, partnerships and M&A news where [Partner] is the actor (review 15+ items, keep up to 8), and pull 12 months of acquisitions; say if the acquisitions list looks incomplete.
6. For customers with primary industry [Vertical] and HQ in [Country]: pull [Partner]'s top 10 customers by engagements, and its delivery locations (top 8, with the share delivered in [Country]).
7. People and timing: pull [Partner]'s top 3 leaders for [Vertical] or alliances (full profile titles) and its most important news item from the last 90 days (client wins, acquisitions, new alliances; analyst rankings and awards are context, not a why-now).

OUTPUT
- Bottom line: 2 sentences — the verdict and what it means for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and why now (the dated news item or another dated fact); if none turned up, say so.
- "Scorecard": Signal | Evidence (dated) | Score from −1 to +1. Defaults (editable): Hiring +1 above +10%, −1 below −10%, else 0 (a step change scores 0 with a note); Headcount +1 above +3%, −1 below 0%; New client wins in 12 months +1 for 3 or more, −1 for none; Acquisitions +1 if any adds a capability close to [What I sell]; Segment footprint +1 if 5+ customers in the segment have 10+ engagements, −1 if fewer than 2.
- Verdict: Rising (+2 or more), Steady (−1 to +1), Slowing (−2 or less).
- "Wins and moves": Date | Event | Counterparty | Why it matters for us.
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: "Footprint in [Vertical], [Country]" (Customer | Engagements), delivery hubs (Metro | Engagements | Onshore or offshore, with the onshore share) and "What this means for us" (3 bullets, each tied to a number).

RULES
- Engagement data lags announcements: if news shows a big new win where engagements are low, say so.
- Sports, sponsorship and stadium "partnerships" are not client wins.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- Talent-flow data ends about 3 months ago; state the months.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named partner leader, dated why-now) first. Is [Partner] rising, steady or slowing? Score its hiring trend, headcount growth, client wins and acquisitions in 12 months, and its footprint in [Vertical], [Country].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run the same check on [second partner] and put the two scorecards side by side.
```

```text
Which of [Partner]'s [Vertical] customers in [Country] run our technology or a rival's?
```

```text
Draft three questions for our partner review that test the weakest signal.
```

## Tips for better results

- Ask the partner about anything scored 0 with a note; a step change in postings or a fresh big win is a good conversation opener.
- Momentum in your segment matters more than company-wide growth. A firm can be growing overall and flat in your industry.

## Related prompts

- [Profile a services firm, rival or partner](../../prompts/10-outsourcing-and-services/competitor-profile.md): A services firm's size, top customers, workloads and delivery hubs in your segment, ending in how to out-position it (rival) or where to team with it (partner), and a named person to act on.
- [Compare candidate partners head to head](../../prompts/13-partners-and-alliances/compare-candidates.md): A weighted scorecard comparing 2–3 candidate partners in one industry and country on workload depth, technology experience, customer breadth, onshore delivery and momentum, with a pick, each candidate's main risk and who to call at the pick.
- [Are they hiring more than usual?](../../prompts/04-signals-and-timing/hiring-spike.md): A plain-English verdict on whether job postings in the function you sell into are running above or below normal, which workloads drive it, whether it's seasonal, and who to call.
- [Openings from their recent acquisitions](../../prompts/01-account-research/acquisitions.md): The top 3 integration openings from the account's acquisitions in the last 3 years, who likely owns each, and an optional read of its strategic investments.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_customers_summary_v3`, `accounts_hiring_timeline_v3`, `accounts_talent_flow_top_metrics_v3`, `get_signal_news_v3`, `accounts_partnerships_mergers_v3`, `get_deals_customer_v3`, `get_deals_service_provider_location_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `partners-momentum-check`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
