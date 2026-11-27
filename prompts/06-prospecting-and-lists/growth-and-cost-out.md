[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Growing and shrinking companies: scale vs cost-out buyers

> **Who in a vertical is adding people fast (scale-up buyers) and who is shrinking (cost-out buyers), with merged or closed companies removed and who to call.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You are looking for companies under growth strain or cost pressure to pitch scale or cost takeout. | SDR / BDR, Account Executive, Services, SI & Staffing Seller, Sales Leader & RevOps | Everyone | 4–6 min | Industry ecosystem, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Vertical]` | Banking & Financial Services |
| `[Country (optional)]` | United States of America |
| `[What I sell]` | managed IT operations and automation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my market research analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Vertical: [Industry, e.g. Banking & Financial Services]
- Country (optional): [HQ country in full, e.g. United States of America]
- What I sell: [one line, e.g. managed IT operations and automation services — skip if you ran the start-here prompt]

STEPS
1. Resolve the vertical to Draup's name and show it.
2. Pull Draup's fastest-growing-workforce and biggest-decline lists for the vertical (each a fixed top 50). In the decline list, "attrition" is the % change in workforce.
3. Keep only [Country] HQs if given. Split each list at 1,000 employees (editable default).
4. For the 10 largest shrinking 1,000+ companies, run one vertical news search (last 12 months) for acquisitions, mergers, closures, bankruptcies, layoffs and restructuring.
5. Move merged or closed companies to "Absorbed or defunct"; give the rest a dated reason or "no news found".

OUTPUT
- Bottom line: 2 sentences — who needs scale, who needs cost-out, and what it means for [What I sell].
- "Growing (1,000+)": Company | Previous | Current | Growth % | HQ country | Who to call (title).
- "Shrinking (1,000+, independent)", top 10: Company | Previous | Current | Change % | Likely reason (date) | Who to call (title).
- "Smaller companies": names and % only.
- "Absorbed or defunct": name, what happened, date.
- "What to pitch": scale and enablement for growers; cost takeout and automation for shrinkers. 2 bullets each.
- Recommended next step: who to contact (title), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- State Draup's comparison period, or "period not stated".
- Never call a decline a layoff without a dated news item; don't lead with small companies' huge percentages.
- "Who to call" = likely buyer title for [What I sell] at that company's size.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill from memory.
- If an industry returns zeros, say so, retry with its parent (e.g. Airlines → Transportation & Logistics) and name it.
- Drop noise: stock chatter, outages, charity, awards, passing mentions, look-alike names, sister companies and re-dated old stories. Merge duplicates. Give date, source and headline (link when Draup has one).
- Keep to about 450 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Show [Vertical] companies with the fastest workforce growth and the biggest declines, split into 1,000+ and smaller. Check the 10 largest decliners for mergers, closures or layoffs, and give the pitch angle and who to call.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Check the next 10 shrinking companies the same way.
```

```text
For the top 3 shrinking companies, who runs IT and Finance now?
```

```text
Write a cost-takeout opener for the #1 shrinking company citing its news.
```

## Tips for better results

- Shrinking lists can include firms that were merged away. Confirm before you call.
- Percentages for small companies swing widely. Treat them as leads to verify.

## Related prompts

- [Fastest revenue growers in my ICP](../../prompts/06-prospecting-and-lists/revenue-growth-screen.md): The fastest-growing companies by revenue in your segment, with M&A-driven jumps set aside and a shortlist growing both revenue and headcount.
- [Is work coming back in-house? (re-insourcing risk)](../../prompts/10-outsourcing-and-services/reinsourcing-risk.md): For each outsourced workload, whether the account is building the same skills in-house, plus fast-growing in-house teams outside its outsourced list: cost takeout, capability gap or re-insourcing risk.
- [What's worth acting on now](../../prompts/04-signals-and-timing/whats-actionable.md): Up to 5 real triggers from the last 90 days, each tied to a stated priority, a likely owner and a suggested action, with the noise stripped out.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `ecosystem_get_organization_increasing_workforce`, `ecosystem_get_organization_decreasing_workforce`, `build_news_filters_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `prospect-growth-and-cost-out`.

</details>

---

[Back to Prospecting and target lists](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
