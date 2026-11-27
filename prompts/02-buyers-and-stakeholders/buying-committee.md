[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Map the buying committee

> **Who to open with and which sponsor to reach later, by name, then a ranked phone-readable list of the people likely to buy, influence or block your deal in one function or workload.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before multi-threading an account, or when you only know one contact. Use this when you need everyone who decides today; use "New leaders and warm intro paths" instead when you want people who just arrived or who came from your customers. | Account Executive, SDR / BDR, Account & Customer Success Manager, Presales & Solutions | Everyone | 2–4 min | Executives & movement, Priorities & opportunities |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | costco.com |
| `[Business function or workload]` | IT, or Artificial Intelligence & Data Science |
| `[Region (optional)]` | United States of America |
| `[What I sell]` | application modernisation and cloud migration services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales stakeholder analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. costco.com]
- Business function or workload: [e.g. IT, or Artificial Intelligence & Data Science]
- Region (optional): [e.g. United States of America]
- What I sell: [one line, e.g. application modernisation and cloud migration services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (no match: retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull key executives for the function or workload, 10 per page, up to 3 pages, with region only if I gave one.
3. If a workload returns fewer than 5 people, add the 2 closest workloads and say which. Drop clear title–function mismatches and flag people at subsidiaries or acquired brands.
4. If no economic buyer (Chief, EVP, CIO or "Head of") appears, pull the next page of 10 in the function once and look for those titles (there is no title search, and the seniority filter is ignored); keep those whose titles fit, and say what you found.
5. Pull priorities for the same function or workload to match leaders to initiatives; drop any that describe what [Company] sells.
6. Pull the most important news item from the last 90 days where [Company] is the actor, for the next step.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step in two parts, each with one dated fact: "Entry point" (the likely champion by name and title, and how to open) and "Sponsor to reach later" (the likely economic buyer by name and title, and what you need first). If either is missing, say so.
- One line: people found, pages checked, people kept, subsidiaries flagged, and whether the step-4 widening ran.
- "Buying committee": Rank | Name | Full title and unit (flag subsidiaries) | Likely role | Linked priority + quarter. Up to 10, ranked by role, then budget control, then title.
- Likely roles: Economic buyer, Technical buyer, Champion candidate, Influencer, Potential blocker (e.g. incumbent-tool owner, security, procurement).
- "Roles with no clear person": the titles to look for.
- Gaps: what Draup didn't have — worth asking in discovery.
- Detail: Name | Location | Budget control | Time in role | LinkedIn; anyone beyond the top 10.

RULES
- Economic buyer and champion are candidates, never confirmed.
- Rank the parent company's own leaders above subsidiary leaders unless the subsidiary is where [What I sell] lands.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- If a step comes back empty or odd, say so and try one fallback; never return a blank template.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title, not the seniority label; check it fits the function; flag subsidiary or branch staff; list everyone sharing a title (VP and SVP are mid-level in banks and consultancies). Mark C-level profiles whose tenure or past employers don't fit [Company] "verify" and keep them out of drafted copy. Professional information only.
- If executives in Europe or the UK return none, rerun without the location and say profiles there may be restricted.
- News: [Company] must be the actor. Drop noise (outages, stock chatter, charity, awards, political commentary, look-alikes, re-dated stories), but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- Phone-first: Bottom line and Recommended next step first; at most 2 tables up front (5 columns and 10 rows max); reference tables under "Detail" at the end. Keep to about 450 words including tables, then offer to continue.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Buying committee at [Company] for [Business function or workload]: entry point and sponsor by name first, then up to 10 people with full title, unit (flag subsidiaries), likely role and linked priority. No economic buyer? Check one more page.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Run "Executive profile and openers" on the entry-point contact and give me 2 openers.
```

```text
Which of these people joined in the last 6 months?
```

```text
Do any of them have past companies that are our customers?
```

## Tips for better results

- Use a workload (e.g. Cybersecurity) when your offer is narrow; use a function (e.g. IT) for a broad map.
- Draup can't search executives by title and ignores the seniority filter, so the prompt checks one more page of the function for Chief, EVP, CIO or Head of titles before saying there's no economic buyer.
- Opening cold with the economic buyer often fails. Start with the entry point and earn the sponsor meeting.

## Related prompts

- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A short profile of one senior person, found by name or just by title, with time in role, past companies, what they likely own, a competitor check and two openers. If Draup has no one with that title, you're told so up front and given the 3 closest people.
- [Warm paths among current leaders](../../prompts/02-buyers-and-stakeholders/warm-paths-current-leaders.md): Senior leaders at the account who used to work at your customers, partners or your own company, who on your side to ask for the intro, and why now.
- [Pre-fill MEDDPICC from outside-in data](../../prompts/02-buyers-and-stakeholders/meddpicc-prefill.md): A MEDDPICC sheet (the deal-qualification checklist) pre-filled with what Draup can show — metrics, buyer candidates, pain, competition rated Red/Amber/Green — and clear 'must discover' flags for the rest.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`, `get_account_priorities_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `people-buying-committee`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
