[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Is this inbound account worth it?

> **A fast pursue / nurture / disqualify verdict on an inbound or referred account, based on your must-haves, with urgency from recent events, a read on the requester and a reply plan.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A lead, demo request or referral lands and you need to decide in minutes whether it deserves an AE's time. | SDR / BDR, Account Executive, Marketing & ABM | Everyone | 1–2 min | Company directory, Company & financials, News signals, Hiring & job postings |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | fivebelow.com |
| `[Requester title]` | Director of Store Operations |
| `[What they asked for]` | a demo of shift scheduling |
| `[My must-haves]` | US retailer, 5,000+ staff, $1B+ revenue |
| `[Business function]` | Operations |
| `[What I sell]` | store-operations software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my sales development analyst qualifying inbound accounts. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [Website, e.g. fivebelow.com]
- Requester title: [Who reached out, e.g. Director of Store Operations]
- What they asked for: [e.g. a demo of shift scheduling]
- My must-haves: [e.g. US retailer, 5,000+ staff, $1B+ revenue]
- Business function: [The function I sell to, e.g. Operations]
- What I sell: [one line, e.g. store-operations software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on. If it isn't in Draup, say so and stop.
2. Pull its company profile: primary vertical, HQ, workforce, revenue and growth, workforce growth %, postings (90 days).
3. Read the requester: does [Requester title] buy or champion in [Business function], and does [What they asked for] fit what I sell?
4. Pull top news (last 90 days) and [Business function] postings (last 12 months).

OUTPUT
- Bottom line: 2 sentences — the verdict (Pursue now, Pursue, Nurture or Disqualify) and why, for [What I sell].
- Fit table: Must-have | Draup value (date) | Meets / Partly / Misses / Unknown.
- "Requester": likely role (decision maker, champion, user, researcher) and ask fit.
- "Why now": up to 3 events (date | headline | source | so-what), or "none in 90 days", plus [Business function] postings in the last 12 months.
- Recommended next step: a one-line reply answering [What they asked for], who else to loop in (title), and why now.
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- The inbound is the intent. Pursue = every must-have met and the requester fits. News only raises urgency: Pursue now = Pursue + a material 90-day event.
- Nurture = Partly or Unknown (a missing number) on any must-have, or a student, job-seeker, vendor or researcher; list what to verify. Disqualify = misses a must-have.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Show USD millions using Draup's conversion rate; if Draup gives none, name the rate and date and mark it as outside Draup.
- Drop noise: stock chatter, outages, charity, awards, passing mentions, look-alike names, sister companies and re-dated old stories. Merge duplicates. Give date, source and headline (link when Draup has one).
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Qualify the inbound from [Requester title] at [Company], who asked for [What they asked for], against my must-haves ([My must-haves]). Pursue if all are met; give urgency from 90-day news, [Business function] hiring and a reply plan.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Who are the top 3 people in [Business function] there? Names, titles and level.
```

```text
Draft the full reply to the requester using one why-now event.
```

```text
Show 3 peers of similar size so I can mention them.
```

## Tips for better results

- Write your must-haves as clear, checkable facts (country, size, revenue, vertical). The verdict is only as sharp as the criteria.
- 'Nurture' is not a no. Check back when a new event appears.

## Related prompts

- [Build and size an ICP list](../../prompts/05-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): Up to 5 real triggers from the last 90 days, each tied to a stated priority, a likely owner and a suggested action, with the noise stripped out.
- [10-minute pre-call snapshot](../../prompts/01-account-research/precall-snapshot.md): Five short bullets you can read in the lobby: who they are, what just happened, where hiring is rising, the priority closest to your offer, and one question to ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_details_v3`, `get_universe_companies_v3`, `get_top_signals`, `accounts_hiring_summary_v3`

Status: **tested live**. Prompt id: `prospect-inbound-qualification`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
