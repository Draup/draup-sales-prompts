[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Warm paths among current leaders

> **Senior leaders at the account who used to work at your customers, partners or your own company, so you can ask for a warm intro.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before cold outreach to a senior buyer, or when building an intro plan for a strategic account. | Account Executive, SDR / BDR, Account & Customer Success Manager, Partnerships & Alliances | Everyone | 2–4 min | Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | target.com |
| `[Business function]` | IT |
| `[Our customers]` | Contoso Retail, Fabrikam Foods |
| `[My company]` | Northwind Data Services (optional, to find alumni) |
| `[Partners]` | Tailspin Partners (optional) |
| `[What I sell]` | cloud data-platform modernisation services |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my relationship-mapping analyst. Use Draup for Sales for every fact.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Business function: [e.g. IT]
- Our customers: [comma-separated, e.g. Contoso Retail, Fabrikam Foods]
- My company: [optional, to find alumni, e.g. Northwind Data Services]
- Partners: [optional, e.g. Tailspin Partners]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Pull key executives in [Business function], 10 per page, up to 3 pages.
3. Compare each person's past companies with [Our customers], [My company] and [Partners], allowing name variants ("Contoso" = "Contoso Retail Inc.").
4. If fewer than 3 match, check 3 more pages or widen to all functions, and say which.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- One line: profiles checked, matches found, functions covered.
- "Warm paths": Name | Full title | Matched past company | Match type (Customer, Our alumni, Partner) | Their title there (only if it was their most recent previous role) | Years at [Company] | Budget control | LinkedIn. Customers first, then alumni, then partners; by seniority within each.
- "Intro plan": for the top 3, who on our side to ask and a one-line ask.
- Recommended next step: who to contact (title or name), what to do (call, email, intro, meeting) and why now (one dated fact).
- Gaps: what Draup didn't have — worth asking in discovery.

RULES
- Past companies come without dates unless it was the most recent previous employer: say "previously worked at", not when.
- Don't infer they used or bought our product there.
- If nothing matches, write "No matches in N profiles checked"; don't stretch to near-miss names.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Use each person's full profile title, not the seniority label. In banking and consulting VP and SVP are mid-level; economic buyers are MD, EVP, "Head of" or C-level (if none appears, say so in Gaps).
- Professional information only (name, title, employer, Draup's profile link). No personal contact details; don't infer personal details or past buying relationships.
- Keep to about 300 words plus tables. Show the top results first, then offer to continue rather than pulling everything.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Which senior [Business function] leaders at [Company] previously worked at [Our customers], [My company] or [Partners]? Table: name, full title, matched past company, match type, years at [Company], budget control, LinkedIn.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Draft the intro request to our account manager at the matched customer.
```

```text
Profile the top match and give 2 openers referencing their past company.
```

```text
Run the same check on new leaders from the last 6 months.
```

## Tips for better results

- List customers where you have a strong, referenceable relationship; a weak one makes a poor intro.
- Add your own company to find alumni. Former colleagues are often the fastest door-openers.

## Related prompts

- [New leaders in the last 6 months](../../prompts/02-buyers-and-stakeholders/new-leaders-warm-paths.md): Leaders who joined or were promoted in the last 6 months in your area, where they came from, and which ones arrive from your customers.
- [Map the buying committee](../../prompts/02-buyers-and-stakeholders/buying-committee.md): A ranked list of the people likely to buy, influence or block your deal in one function or workload, with their role in the decision, an entry point and the sponsor to reach later.
- [Executive profile and openers](../../prompts/02-buyers-and-stakeholders/executive-profile.md): A one-screen profile of a named executive and two openers tied to the account's current priorities.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `people-warm-paths-current-leaders`.

</details>

---

[Back to Buyers and stakeholders](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
