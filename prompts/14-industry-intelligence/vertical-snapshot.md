[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# One-page vertical market snapshot

> **A one-page view of an industry: revenue and spend, top priorities with likely owners, technologies gaining ground, and who outsources what to whom.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are entering a vertical, building a territory plan, or need industry context for a pitch. | Sales Leader & RevOps, Marketing & ABM, Account Executive, Services, SI & Staffing Seller | Everyone | 4–6 min | Industry ecosystem |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Retail |
| `[What I sell]` | supply-chain planning software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my industry analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Retail]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it. A sub-industry (e.g. Airlines) can return zeros: use the parent, say so, and filter company lists back to the sub-industry where you can.
2. Pull the vertical's revenue, IT spend and R&D spend for the latest year, with growth.
3. Pull key priorities and pick the 5 most relevant to [What I sell], each with a company example. If none come back, use the 3 largest companies' stated priorities and label them.
4. Pull growing technologies (fixed top 50); keep up to 5 vertical-specific or relevant ones, and say if fewer survive.
5. Pull top outsourcing vendors (drop agencies, staffing, market-research and merchandising firms; keep up to 10), the top 10 buyers and top 5 workloads.

OUTPUT
- Bottom line: 2 sentences — the state of [Vertical] and what it means for [What I sell].
- "The numbers": Metric | Value ($B) | Growth % | Year ("latest, year not given" if omitted).
- "Top priorities": Priority | What it means | Company example (Draup gives no date; say "undated") | Likely owner (title) | Fit.
- "Technology gaining ground": Technology | Vendor | Companies adopting | Why it matters.
- "Outsourcing": top vendors, buyers and workloads, each with active engagements.
- "Excluded": what you removed.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Every list is Draup's fixed top 50, not the whole market; say so once.
- Flag buyers whose business doesn't fit [Vertical].
- Vertical IT spend tracks revenue; don't present its growth as a separate trend.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- Leave generic tools (browser add-ons, office suites, chat assistants, design tools) out of technology lists.
- Engagements and outsourced headcount are Draup-derived estimates, not public contracts. Never call them signed deals.
- IT spend, R&D spend and local headcount are Draup estimates; say so once.
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Give me a one-page Draup snapshot of [Vertical]: revenue, IT and R&D spend with growth, the 5 priorities most relevant to [What I sell], 5 vertical-specific growing technologies, top vendors (no agencies or staffing), top outsourcers and workloads.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the top 3 priorities into a 5-slide point of view for [What I sell].
```

```text
Which 10 companies in [Vertical] are hiring most right now?
```

```text
Where are this vertical's IT and R&D teams concentrated?
```

## Tips for better results

- If a section comes back empty, it is usually the industry name. Ask Claude to try the parent industry.
- Ask to see the 'Excluded' list if you want to know what was filtered out.

## Related prompts

- [Industry point of view for a pitch](../../prompts/14-industry-intelligence/industry-pov.md): The 5 industry priorities that matter most for what you sell, each with dated company proof and a likely owner, turned into a 5-slide narrative and a one-line POV.
- [Vertical vendor league table](../../prompts/14-industry-intelligence/vendor-league.md): Who really wins outsourcing work in a vertical, after removing agencies and staffing firms, plus top workloads and buyers and where your firm ranks.
- [Where a vertical's teams sit](../../prompts/14-industry-intelligence/talent-hubs.md): The metros where an industry's IT and R&D teams are concentrated, with hubs that host both: where its delivery and engineering work happens.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_vertical_revenue`, `ecosystem_get_vertical_it_spend`, `ecosystem_get_vertical_rnd_spend`, `ecosystem_get_vertical_key_priorities`, `ecosystem_get_vertical_techstack_growing`, `ecosystem_get_vertical_outsourcing_vendors`, `ecosystem_get_vertical_outsourcing_customers`, `ecosystem_get_vertical_outsourcing_workloads`, `ecosystem_get_vertical_organization_top_employers`, `get_key_account_priorities`

Status: **tested live**. Prompt id: `market-vertical-snapshot`.

</details>

---

[Back to Industry and market intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
