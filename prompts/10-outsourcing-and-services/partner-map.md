[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Which providers to partner with or replace

> **For each priority in one function, the providers and tech vendors linked to it with their engagements in that function, and whether to partner, displace or walk through an open door.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You're deciding who to partner with and who you'd be replacing at one account. Use this when you want the play for every priority; use services-cosell-partner instead when you sell software and need one SI to co-sell with, and tech-priority-stack-incumbent-map when you only need who's working each priority. | Partnerships & Alliances, Services, SI & Staffing Seller, Account Executive | Everyone | 2–4 min | Priorities & opportunities, Outsourcing deals, Tech stack, Executives & movement, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | pfizer.com |
| `[Business function]` | IT |
| `[I sell]` | software |
| `[What I sell]` | AI and automation platform |
| `[Partners to evaluate (optional)]` | Tailspin Partners, Accenture |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my alliances and pursuit strategist. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [Website, e.g. pfizer.com]
- Business function: [e.g. IT, Supply Chain, Human Resources]
- I sell: [software, services or both — skip if you ran the start-here prompt]
- What I sell: [One line, e.g. AI and automation platform — skip if you ran the start-here prompt]
- Partners to evaluate (optional): [Our current or candidate partners, e.g. Tailspin Partners, Accenture]

STEPS
1. Find the company by its website and confirm it's the parent, not a subsidiary or sister company. If several match, ask me. Use Draup's exact name from then on.
2. Pull priorities in [Business function], sort by date and keep up to 8 most relevant to [What I sell], with source and quarter (if fewer exist, say how many).
3. For each priority, list up to 4 linked providers and 4 linked products. Skip the account's subsidiaries, agencies and staffing firms.
4. Pull the account's provider ranking twice: limited to [Business function] (if that returns nothing, to its main workloads), and for the whole account. Show each provider's engagements as "in function / total".
5. Tag each Partner (complements what I sell), Displace (does what I sell) or Neutral. For software sellers, services firms and platforms we run on are Partner or Neutral, not Displace.
6. If I named partners to evaluate, compare them head to head: engagements in [Business function] at the account, in total there, and in [Business function] across the account's industry.
7. People and timing: at [Company], pull the top 3 leaders in [Business function] and the most important news item from the last 90 days where it is the actor.

OUTPUT
- Bottom line: 2 sentences — who to team with and who you'd replace.
- Recommended next step: a person from step 7 (name and title), what to do (often via the best partner's account lead), and why now (the dated news item or another dated fact); if none turned up, say so.
- "Priority map": Priority (source, quarter) | Linked providers (in function / total) | Linked tech | Play | Likely owner.
- Play: Partner-led, Displacement, or Open (nothing linked, or only providers with 2 or fewer engagements in the function; editable default).
- "Best partners to call": up to 3, named partners first, each with in-function engagements and why.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: "Who we'd displace" (up to 3, with engagements) and the head-to-head table from step 6.

RULES
- Tools and providers are linked to priorities by workload, not confirmed: say "linked", never "used for".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Engagement counts are "active engagements (Draup-derived)", not signed contracts. Don't show outsourced headcount.
- Rank providers by engagements yourself.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- If [Company] sells technology, drop priorities and tools about its own products.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 450 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named person, dated why-now) first. For [Company]'s top priorities in [Business function], which providers and tech vendors are linked to each, with engagements in that function? Tag Partner, Displace or Open for [What I sell].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Pick the best co-sell partner for the top Open priority.
```

```text
Show the buying committee for [Business function].
```

```text
Draft a note to the best partner's account lead proposing a joint session with the person in the next step.
```

## Tips for better results

- A provider linked to a priority works in the same workloads; it hasn't necessarily won that initiative. Check its in-function engagements before pitching a partnership.
- Name the partners you're weighing. The head-to-head comparison is often the most useful part of the answer.
- Open priorities with no strong incumbent are often the quickest entry.

## Related prompts

- [Pick the SI to co-sell with](../../prompts/10-outsourcing-and-services/cosell-partner.md): A shortlist of service partners already delivering your workload at the account — counted within that workload, not account-wide — and experienced with your technology, with the one to call first.
- [Best entry points: expand or new](../../prompts/11-account-planning/entry-points.md): The five best ways in for what you sell, each marked Expand (we already serve it) or New, with dated evidence, incumbents, any installed competitor and the likely owner.
- [Who's already working each priority](../../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md): For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_priorities_v3`, `get_deals_service_provider_v3`, `accounts_executives_key_executives_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `services-partner-map`.

</details>

---

[Back to Outsourcing and services deals](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
