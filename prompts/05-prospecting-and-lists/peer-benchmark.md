[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Benchmark an account against peers

> **One table comparing an account with its closest peers on growth, hiring, workforce, footprint and recent news, plus where it leads and where to ask questions.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You want peer context for a meeting, or to see how an account compares with its rivals. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Marketing & ABM | Everyone | 2–4 min | Company directory, Company & financials, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | delta.com |
| `[Peer websites (optional)]` | united.com, aa.com, southwest.com |
| `[What I sell]` | airline operations analytics platform |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive benchmarking analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [Account website, e.g. delta.com]
- Peer websites (optional): [Up to 6, e.g. united.com, aa.com, southwest.com]
- What I sell: [one line, e.g. airline operations analytics platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. No peers given? Use Draup's listed competitors; keep the 5 closest in business and size.
3. Pull everyone in one list by website: revenue and growth, IT spend, workforce and growth %, hiring %, attrition %, postings (90 days), outsourcing size, GCC count, Opportunity Index.
4. For each, count distinct material news events in the last 90 days ("10+" if the first 10 all qualify).

OUTPUT
- Bottom line: 2 sentences — where [Company] stands and what it means for [What I sell].
- Benchmark table: rows = metrics; columns = [Company], each peer, peer median. Fiscal year beside money.
- "Where [Company] leads": 3 bullets with numbers.
- "Questions to ask": 3 places it trails, phrased as discovery questions, never "you're behind".
- "Recent news": Company | Events (90 days) | Most material event (date, headline, source).
- "Why this matters": 3 talking points, e.g. "Peers grew hiring X%, you grew Y%".
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- IT spend is a Draup estimate, often modelled from revenue: label it "Draup-estimated"; its growth is not a separate signal.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Look up named companies by website (exact) and check each came back. Name searches match on "contains" and pull in look-alikes, so keep only companies you resolved.
- Don't compare companies on Draup's yes/no event flags; count dated news events from the last 90 days instead.
- Show USD millions using Draup's conversion rate; if Draup gives none, name the rate and date and mark it as outside Draup.
- Drop noise: stock chatter, outages, charity, awards, passing mentions, look-alike names, sister companies and re-dated old stories. Merge duplicates. Give date, source and headline (link when Draup has one).
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Benchmark [Company] against [Peer websites] (or its 5 closest Draup-listed competitors) on revenue growth, workforce growth, hiring, postings, GCCs and 90-day news events. Then give 3 leads, 3 questions and 3 talking points.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Compare AI and data hiring for the same companies over the last 12 months.
```

```text
Which products did the peers adopt in the last 12 months that [Company] doesn't run?
```

```text
Turn the talking points into a 100-word email to the CIO.
```

## Tips for better results

- The table works best with 4 to 6 peers of similar size.
- Lead with questions, not comparisons. Buyers often open up when asked how they see a gap.

## Related prompts

- [Sell into a customer's competitors](../../prompts/05-prospecting-and-lists/competitor-set.md): Your customer's real competitors, ranked by Draup's Opportunity Index score, with what happened at each in the last 90 days, a reference angle and who to call.
- [AI readiness vs peers](../../prompts/08-account-planning-and-expansion/ai-readiness.md): A deep read on the account's AI hiring, priorities, new tools and outsourced AI work, then its AI hiring compared with up to 4 close peers.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `prospect-peer-benchmark`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
