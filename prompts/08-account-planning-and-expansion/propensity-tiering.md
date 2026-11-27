# Tier my accounts by propensity to buy

**Up to 25 accounts scored 0–100 on an editable Fit (0–50) and Timing (0–50) rubric, tiered A, B or C and placed on a fit-versus-timing grid, with the driver behind each score.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning a quarter or a territory, or deciding where to spend limited time. | Account Executive, Sales Leader & RevOps, Account & Customer Success Manager, SDR / BDR | Everyone | 4–6 min | Company directory, Company & financials, Hiring & job postings, News signals |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Accounts]` | target.com, walmart.com, siemens.com, zebra.com, bmwgroup.com |
| `[What I sell]` | supply-chain planning software |
| `[Target revenue band]` | $5B–$150B |
| `[Target industries (optional)]` | Retail, Automotive |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my territory planning analyst. Use the Draup for Sales connector for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Accounts: [Up to 25 websites, e.g. target.com, walmart.com, siemens.com]
- What I sell: [One line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Target revenue band: [e.g. $5B–$150B]
- Target industries: [Optional, e.g. Retail, Automotive]

STEPS
1. Look up the accounts by website (exact), 10 per lookup (each row is large). Resolve only websites it missed, one by one; ask if one looks like a subsidiary. Never match by name.
2. Take revenue, revenue growth, Draup-estimated IT spend, Opportunity Index, hiring %, workforce growth and primary vertical.
3. For the 10 highest-Fit accounts, count distinct dated news events (90 days) with the company as actor. Others: "not checked", scored 10.
4. Score, add up and tier.

OUTPUT
- Bottom line: 2 sentences — the A accounts and what they share.
- Table: Tier | Account | Fit | Timing | Total | Grid | Strongest driver | Weakest driver. By total.
- One-line reason per account; "Rubric used"; "Data flags" (missing values, possibly inactive).
- Recommended next step: who to contact (title), what to do, and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Rubric (editable defaults). FIT 50: revenue in band 15 (within 2x 8, else 3); revenue growth 10 (over 5% 10, 0–5% 6, −5–0% 3, else 0); Opportunity Index 15 (score ÷ 10 × 15); industry 5 (in target 5, else 0; all 5 if blank); IT spend 5 (over $500M 5, $100–500M 3, else 1), light as it is modelled from revenue. TIMING 50: news events 20 (0 = 0, 1–2 = 8, 3–5 = 14, 6+ = 20); hiring % 15 (over 10% 15, 5–10% 10, 2–5% 5, else 0); workforce growth 15 (over 3% 15, 0–3% 10, −3–0% 5, else 0).
- Missing value = half that item's points, flagged. Ignore yes/no signal flags.
- Tiers: A 70+, B 50–69, C under 50. Grid: Fit 30+ and Timing 25+ = Pursue now; Fit only = Nurture; Timing only = Opportunistic; neither = Deprioritise.
- For news, skip stock chatter, awards, passing mentions and look-alikes.

STANDARD RULES (leave as is)
- Pull company lists 10 rows at a time and priorities 10 at a time; show the top results first and offer to continue.
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup returns nothing for a section, write "Not in Draup"; never guess or fill from memory.
- Keep to about 350 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

## In a hurry? Quick version

```text
Tier these accounts for [What I sell]: [Accounts]. One Draup company lookup by website, score Fit 0–50 and Timing 0–50 with the editable rubric, tier A/B/C and give each a one-line reason.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Change the rubric: Opportunity Index 5, revenue in band 25, and rerun.
```

```text
For my A accounts, give one why-now signal each from the last 60 days.
```

```text
Count news events for the accounts marked "not checked".
```

```text
Build a one-page account brief for the top-scoring account.
```

## Tips for better results

- The rubric is in the prompt on purpose. Change the weights to match how your team actually wins.
- Use websites, not names. Name matching can pull in dealers and subsidiaries.

## Related prompts

- [Carve balanced territories](../../prompts/08-account-planning-and-expansion/territories.md): An industry-and-country account universe split into N territories balanced on Draup-estimated IT spend (or revenue or count), with HQ clusters kept together and owned accounts excluded.
- [Benchmark an account against peers](../../prompts/05-prospecting-and-lists/peer-benchmark.md): One table comparing an account with its closest peers on growth, hiring, workforce, footprint and recent news, plus where it leads and where to ask questions.
- [Build and size an ICP list](../../prompts/05-prospecting-and-lists/icp-list.md): The true size of your ideal-customer list, size bands, and the top 25 accounts with money, providers, hiring, who to call and a why-now for the best 5.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_universe_companies_v3`, `get_top_signals`

Status: **tested live**. Prompt id: `plan-propensity-tiering`.

</details>

[Back to Account planning and expansion](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
