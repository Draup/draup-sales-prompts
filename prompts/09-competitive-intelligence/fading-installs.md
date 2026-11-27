[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Accounts where a rival is fading

> **Your target accounts rated by how strong a rival's installed products are (Entrenched, Present, Thin or Fading), the successor already in place, and the best 3 takeout targets with a named person at the top one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Planning a takeout campaign against a software rival across a named account list. | Account Executive, SDR / BDR, Presales & Solutions, Sales Leader & RevOps | Software sellers | 4–6 min | Tech stack |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | Teradata |
| `[Accounts]` | visa.com, fedex.com, att.com, boeing.com |
| `[What I sell]` | cloud data warehouse |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive displacement analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [software vendor or product, e.g. Teradata]
- Accounts: [up to 8 websites, e.g. visa.com, fedex.com, att.com, boeing.com]
- What I sell: [one line, e.g. cloud data warehouse — skip if you ran the start-here prompt]

CONTEXT (why this matters)
A rival's weakest installs are the cheapest wins: thin usage, stale evidence, a successor in place.

STEPS
1. Find each account by website and confirm the parent (retry an unresolved site once by name, show the match and score; never drop one silently); ask only if none or several match. If I gave more than 8, do the first 8 and offer to continue.
2. For each account, check the whole stack for [Competitor] products (one lookup, up to 50 rows), whatever area they're filed under. If [Competitor] is a product, check its maker as Draup spells it.
3. Record strength and last seen; a date shared by 3+ of an account's rows, or across accounts, is a refresh date.
4. Rate each account by its strongest [Competitor] product seen in the last 90 days (not on a refresh date): High = Red (entrenched), Medium = Amber, Low only = Green (thin), none = Green (fading). Flag any product first seen within 12 months (the one use of first-seen dates). Editable defaults.
5. For the 3 weakest accounts, pull the sub-category matching [What I sell] (e.g. Data Warehouse Software, 30 rows) and name other vendors' High or Medium products: the likely successor.
6. Rank targets: Green (fading), then Green (thin), then fewest [Competitor] products first (an easier swap).
7. For the #1 target, pull its top 3 executives in the matching workload (e.g. Data Engineering) or IT, and its most important 90-day news item.

OUTPUT
- Bottom line: 2 sentences — the best target and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the #1 target, the action this week and the dated why-now (or say none).
- Table "Install health" (up to 8): Account | Strongest product (strength, last seen) | Products found | Rating.
- Table "Best 3 takeout targets": Account | Successor in place | Why now (dated) | Opening for [What I sell].
- "Leave for later": Red and Amber accounts, one line each.
- Detail: successor reads (Replacing, Parallel, Unclear), countries, unresolved accounts.
- Gaps: what Draup lacked; ask in discovery.

RULES
- Low-only installs don't count as present (Green); a newly detected install is a fresh choice, so don't attack it.
- A successor already at High means a likely mid-migration: the play is speed.
- Say "not detected", never "not used". Label inferences "likely".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- Trust usage strength and last-seen date, not confidence scores or "Generic" rows; a date shared by many rows is a refresh. A rival counts only at High or Medium usage; say you ignored Low. Say "fading", never "dropped".
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
For up to 8 [Accounts], check every [Competitor] product in the stack. Lead with the best takeout target and a named person there. Rate each account Red, Amber or Green (thin or fading) and name the successor already in place.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [Account], map the buying committee in the function that owns the product.
```

```text
Check job ads at the best 3 targets for skills naming [Competitor]'s product (product spelling, not the maker; retry once if 0).
```

```text
Write a 90-word email to the named executive at the top target.
```

## Tips for better results

- Keep the list to accounts you can work this quarter; 8 is one pass.
- A rival product still listed but Low across the board is often a renewal you can shape.

## Related prompts

- [Fading tools and replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.
- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `compete-fading-installs`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
