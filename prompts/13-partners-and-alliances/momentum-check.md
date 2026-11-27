[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this partner rising or slowing?

> **A Rising, Steady or Slowing verdict on a prospective partner, scored from its hiring, headcount growth, client wins, acquisitions and footprint in your industry and country, with who to talk to there.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before you sign, renew or put marketing funds behind a services partner. Use "Compare candidate partners head to head" instead to choose between several. | Partnerships & Alliances, Sales Leader & RevOps | Everyone | 2–4 min | Outsourcing deals, Hiring & job postings, Talent flow & locations, News signals, Executives & movement |

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
Act as my partner due-diligence analyst. Use Draup for Sales for every fact. No outside knowledge unless I ask, labelled.

INPUTS (edit these)
- Partner: [Website of the services firm, e.g. hcltech.com]
- Vertical: [Draup industry where we'd work together, e.g. Automotive]
- Country: [Customer HQ country in full, e.g. Germany]
- What I sell: [One line, e.g. software-defined vehicle testing platform; skip if saved in setup]

STEPS
1. Find the partner by website and confirm the parent, not a regional unit.
2. Pull its customer summary: active customers, engagements and top 3 customers overall.
3. Pull 12 months of monthly postings. A month that more than doubles and stays there is a "step change" (possibly wider data coverage, not demand).
4. Pull headcount growth over Draup's latest 12-month workforce window (it ends about 3 months ago; say the dates).
5. Search 12 months of deals, partnerships and M&A news where [Partner] is the actor (review 15+ items, keep up to 8), and pull 12 months of acquisitions; say if the acquisitions list looks incomplete.
6. For customers with primary industry [Vertical] and HQ in [Country]: pull [Partner]'s top 10 customers by engagements, and its delivery locations (top 8, with the share delivered in [Country]).
7. People and timing: page through [Partner]'s Sales & Marketing executives (10 a page, up to 3; no vertical filter, as services firms are tagged IT Services) and keep 3 whose titles name [Vertical], a sector, alliances or partnerships; if none, say so and give the closest title. Then pull its most important news item from the last 90 days (client wins, acquisitions, alliances; rankings and awards aren't a why-now).

OUTPUT
- Bottom line: 2 sentences — the verdict and what it means for [What I sell].
- Recommended next step: a person from step 7 (name and title), what to do, and the dated why-now; if none, say so.
- "Scorecard": Signal | Evidence (dated) | Score from −1 to +1. Defaults (editable): Hiring +1 above +10%, −1 below −10%, else 0 (a step change scores 0 with a note); Headcount +1 above +3%, −1 below 0%; New client wins in 12 months +1 for 3 or more, −1 for none; Acquisitions +1 if any adds a capability close to [What I sell]; Segment footprint +1 if 5+ customers in the segment have 10+ engagements, −1 if fewer than 2.
- Verdict: Rising (+2 or more), Steady (−1 to +1), Slowing (−2 or less).
- "Wins and moves": Date | Event | Counterparty | Why it matters for us.
- Gaps: what Draup didn't have — worth asking the partner.
- Detail: footprint in [Vertical], [Country] (Customer | Engagements); delivery hubs with onshore share; 3 "what this means for us" bullets tied to numbers.

RULES
- Engagement data lags announcements: if news shows a big new win where engagements are low, say so.
- Sports, sponsorship and stadium "partnerships" are not client wins.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Engagements are "active engagements (Draup-derived)", not contracts; never quote outsourced headcount.
- Postings are openings, not hires; skip the partial first and last months and compare the last 5 full months with the 5 before.
- News: the company must be the actor; drop stock chatter, politics, charity, awards, passing mentions, look-alikes, sister companies and re-dated stories; keep anything bearing on What I sell. Conflicting sources: say so; single-source figures are unverified.
- People: full profile titles that fit the function; flag subsidiary or branch staff and mark C-level profiles that don't fit the parent (tenure, past employers) "verify", out of copy. No economic buyer? Check the next page of 10 for Chief, EVP, CIO or "Head of". Data lags about 3 months; professional information only.
- Phone-first: bottom line and next step first; up front at most 2 tables (5 columns, 10 rows), the rest under "Detail"; about 450 words including tables, then offer more.
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
