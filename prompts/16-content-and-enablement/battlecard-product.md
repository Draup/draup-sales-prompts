[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Battlecard: beat a rival software vendor

> **A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A software rival keeps showing up in your deals, or you're preparing a team for a competitive pursuit. Selling services? Use "Battlecard: beat a rival services firm" instead. | Account Executive, Presales & Solutions, Marketing & ABM | Software sellers | 4–6 min | Tech stack, Company directory, Company & financials, News signals, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | datadoghq.com or Datadog |
| `[What I sell]` | observability and IT operations software |
| `[Vertical (optional)]` | Retail |
| `[Where we lose to them (optional)]` | lost Contoso Retail on bundled pricing |
| `[Proof we can cite (optional)]` | Fabrikam Foods cut alert noise by half in one quarter |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive analyst for software deals. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [rival vendor's website or product, e.g. datadoghq.com or Datadog]
- What I sell: [one line, e.g. observability and IT operations software — skip if you ran the start-here prompt]
- Vertical (optional): [e.g. Retail]
- Territory (optional): [HQ country in full, e.g. United States of America; blank uses my saved territory, or ask]
- Where we lose to them (optional): [paste win/loss notes, e.g. lost on bundled pricing]
- Proof we can cite (optional): [e.g. Fabrikam Foods halved alert noise]

CONTEXT (optional)
Implementers and resellers look like big users; they're partners, not targets.

STEPS
1. Find [Competitor] by website and confirm the parent. If I named a product, use its maker. If unclear, ask me.
2. Pull HQ, workforce, revenue and growth (USD), and top 5 products by installs.
3. In one short company list (default view, sorted by total_workforce, never employee_count), pull the 10 largest parent companies running [Competitor] products, in primary industry [Vertical] and HQ in [Territory]. Exclude IT services, consulting and outsourcing firms and say how many. Merge subsidiaries into parents; flag holding companies.
4. For the top 5, check the whole stack for any [Competitor] product in any area (usage, last seen). Count installs only at High or Medium on a named product; Low but seen in the last 6 months is "light"; not seen for 6 months is "fading"; if only the Generic row is High, say "present, product not identified".
5. Search 180 days of their news (launches, acquisitions, partnerships, leadership); review 30+ items.
6. First account: the largest Amber or fading install in [Territory] whose top executives sit at the parent, not a branch or subsidiary. Pull its top 3 executives in the function closest to What I sell and its top 90-day news item.

OUTPUT
- Bottom line: 2 sentences — how entrenched they are and where [What I sell] can win.
- Recommended next step: the first account, who to contact (name and title from step 6), what to do, and the dated fact. If none, say so.
- "Where they're installed": Company | Industry | Workforce | Main product | Usage rating. Rows 6–10: "usage not checked".
- "How we win": 3 angles tied to facts above and [Proof we can cite]; one landmine.
- "Trap questions": 3 questions that expose their weak spots without naming them.
- "Objection to expect": their likely claim and a reply.
- Detail: top products by install count; excluded implementers; recent moves (up to 6, dated, sourced); "Where we lose" counters.
- Gaps: what Draup lacked, to ask in discovery.

RULES
- Mark the card "Internal use". Claim no results beyond [Proof we can cite].
- No install in [Vertical] or [Territory]? Say so and show neighbouring industries or regions.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage, not first-seen dates; say "fading", never "dropped".
- Rivals: High usage in my workloads is Red, Medium Amber, newly detected Amber; unchecked is "present (usage not checked)"; ignore "Generic" rows.
- News: the company must be the actor. Drop stock chatter, politics, charity, sponsorships, awards, passing mentions, look-alikes and re-dated stories; keep outages, breaches or inquiries only if they bear on What I sell. Flag conflicting or single-source figures as unverified.
- Never return a blank table: say what came back empty and use the fallback.
- People (professional information only): check each full title against the function; flag subsidiary or branch staff. To widen, pull the next page of 10 in the function once and look for Chief, EVP, CIO or 'Head of' titles. A C-level profile whose tenure or past employers don't fit the parent is "verify": keep them out of copy.
- Phone-first: Bottom line and next step first; up front at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 450 words including tables; then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first: battlecard on [Competitor] for [What I sell]: the 10 largest parent end users in my territory running it (no IT services firms), usage, 180 days of moves, how we win, first account.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Check rows 6–10 product by product and add usage strength and last-seen dates.
```

```text
Which of my target accounts run [Competitor]? Check [Accounts], 5 at a time.
```

```text
Turn 'How we win' into a one-page objection-handling sheet for SDRs.
```

```text
List the IT services firms you excluded: they may be partners worth recruiting.
```

## Tips for better results

- If your rival is a product inside a bigger company (a cloud database, say), name the product. Claude records the maker and checks every product it makes.
- Usage strength and last-seen date matter more than the install count: Medium or fading installs are where switching conversations start.
- Set a Territory (or save one in setup). Without it the list ranks the world's largest companies, so the first account can be one you can't sell to.

## Related prompts

- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.
- [Size a vendor's install base](../../prompts/03-tech-stack-and-displacement/vendor-install-base.md): What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion, with a named person at the vendor or a first target to approach.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.
- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_account_financials_v3`, `get_account_key_solution_offerings_v3`, `get_universe_companies_v3`, `get_account_tech_stack_products_v3`, `get_signal_news_v3`, `build_news_filters_v3`, `get_news_feed_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `content-battlecard-product`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
