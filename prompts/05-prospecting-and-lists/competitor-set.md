# Sell into a customer's competitors

**Your customer's real competitors, ranked by Draup's Opportunity Index score, with what happened at each in the last 90 days, a reference angle and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You just won, or have a strong reference at, a company and want to take the story to its rivals. | Account Executive, SDR / BDR, Marketing & ABM, Sales Leader & RevOps | Everyone | 2–4 min | Company directory, News signals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | your customer's website (e.g. fabrikam.com, illustrative) |
| `[Referenceable?]` | no |
| `[Proof point (optional)]` | a hypothetical result, e.g. cut scheduling overtime across its stores |
| `[What I sell]` | warehouse workforce-scheduling software |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my account-based marketing analyst. Use the Draup for Sales connector for every fact.

INPUTS (edit these)
- Company: [Customer's website, e.g. fabrikam.com (illustrative)]
- Referenceable?: [yes or no — may I name them? e.g. no]
- Proof point (optional): [e.g. cut scheduling overtime across its stores]
- What I sell: [one line, e.g. warehouse workforce-scheduling software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it's the parent, not a subsidiary; ask me if several match. Use Draup's exact name from then on.
2. Pull Draup's listed competitors, ranked by Opportunity Index, with workforce and revenue.
3. Keep same-primary-vertical companies at 0.3–3x the customer's workforce (editable default); record removals. If under 4 remain, add same-vertical, same-HQ-country companies in that range, labelled "added peer".
4. For the top 5, pull top news from the last 90 days and keep material events: deals, new centres, M&A, senior leadership changes, layoffs, major launches.

OUTPUT
- Bottom line: 2 sentences — the best next targets and why for [What I sell].
- Table: Rank | Competitor | Opportunity Index | Workforce | Revenue ($M, FY) | News events (90 days, top 5) | Listed or added | Who to call (title).
- Top 5 each: "What happened" (up to 2 events: date | headline | source) and "Reference angle" (our result at [Company] → their situation).
- "Removed": name and reason.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- If Referenceable? is no, never name [Company]; say "a leading [vertical] peer".
- Write "No material events in 90 days" rather than padding.
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- Don't compare companies on Draup's yes/no event flags; count dated news events from the last 90 days instead.
- Show USD millions using Draup's conversion rate; if Draup gives none, name the rate and date and mark it as outside Draup.
- Drop noise: stock chatter, outages, charity, awards, passing mentions, look-alike names, sister companies and re-dated old stories. Merge duplicates. Give date, source and headline (link when Draup has one).
- Keep to about 400 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
List [Company]'s competitors in Draup, ranked by Opportunity Index, after removing unrelated firms. For the top 5, give up to 2 material events from the last 90 days, a reference angle and who to call.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Write a 3-email sequence for the #1 competitor using the reference angle.
```

```text
Who owns [Business function] at the top 2? Names, titles and level.
```

```text
Check the whole tech stack of the top 5 for any product that competes with ours.
```

## Tips for better results

- Check the 'Removed' list; small or unrelated firms are filtered out there.
- Ask your customer before naming them. The prompt defaults to an anonymous reference.

## Related prompts

- [Benchmark an account against peers](../../prompts/05-prospecting-and-lists/peer-benchmark.md): One table comparing an account with its closest peers on growth, hiring, workforce, footprint and recent news, plus where it leads and where to ask questions.
- [Look-alikes of a best customer](../../prompts/05-prospecting-and-lists/lookalikes.md): Up to 20 companies that look like your best customer on industry, size, HQ and shared technology, each with the reason it matches and who to call.
- [Signal-to-email (one or a few accounts)](../../prompts/04-signals-and-timing/signal-to-email.md): For one account or up to 5 per pass: the freshest relevant signal, the priority it supports, and a short, sourced opener for your persona that ends in one low-friction ask.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `prospect-competitor-set`.

</details>

[Back to Prospecting and target lists](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
