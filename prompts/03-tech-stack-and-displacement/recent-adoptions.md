[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What they adopted this year

> **The tools first detected at the account in the last 12 months, each labelled as competing with, complementing or unrelated to what you sell, with any competitor product called out first.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Looking for a why-now: a new tool usually means a new project, a new owner and fresh budget. | Account Executive, SDR / BDR, Presales & Solutions | Everyone | 2–4 min | Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[What I sell]` | supply-chain planning software |
| `[Competitor]` | Kinaxis, o9 Solutions |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my technology signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Competitor: [optional, one or more, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find [Company] by its website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company. If none or several match, or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull every product first detected at the company in the last 12 months, up to 5 pages, and review them all before narrowing. Note the earliest and latest first-detected dates.
3. If I named competitors, search the whole stack by each maker and flag any product first detected in this window.
4. Drop Low-usage products unless they're in my category or made by a competitor.
5. Label each: Competes (does what [What I sell] does), Complements (sits next to it or feeds it) or Unrelated.
6. Look for clusters in Competes and Complements (e.g. several new security tools).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Headline: "N products first detected between [earliest] and [latest]; X compete, Y complement."
- "Competitor alert" (first): product, first-detected month, usage strength, countries — or "none".
- Table (up to 25 rows): First detected (month) | Product | Maker | Category | Usage strength | Relation | Likely owner. Competes, then Complements, then Unrelated; newest first within each. Counts by category for the rest.
- "Why this matters for [What I sell]": 3 bullets on the likely projects, each naming a product.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting), and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Recent first-detected dates are reliable here; only a date that predates the product isn't. It marks Draup's first public evidence, not a contract.
- Additions only; don't infer removals. Say how many products you reviewed and dropped.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust last-seen date and usage strength. Ignore the confidence score and "Generic" rows. Say "fading", never "dropped".
- Check the whole tech stack for any product made by [Competitor], whatever area it's filed under. If [Competitor] is a product (e.g. Google BigQuery), record the product and its maker.
- If [Company] sells technology itself, ignore its own products and priorities about products it sells.
- Keep to about 320 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
What technology did Draup first detect at [Company] in the last 12 months? Group by category, newest first, label each as competing with, complementing or unrelated to [What I sell], and call out any [Competitor] products first.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For the top 3 complementary adoptions, who likely owns them? Find executives in the matching workloads.
```

```text
Which older tools in the same categories look like they are fading?
```

```text
Write a 3-sentence opener that references the strongest new adoption.
```

## Tips for better results

- A cluster of new tools in one area is often a stronger signal than any single product.
- List your main competitors in the input so Claude checks their whole product range, not just this year's additions.

## Related prompts

- [Fading stack: replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement pitches.
- [What their job ads say about their stack](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press.
- [What changed since [Date]](../../prompts/04-signals-and-timing/change-log.md): A dated log of everything material that changed at an account since a date you choose, ranked by impact on your deal.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_tech_stack_trend_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `tech-recent-adoptions`.

</details>

---

[Back to Tech stack and displacement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
