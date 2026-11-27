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
A rival's weakest installs are the cheapest wins: usage thin, evidence stale, a successor already in. Entrenched installs are expensive fights.

STEPS
1. Find each account by website and confirm the parent; ask only if none or several match. If I gave more than 8, do the first 8 and offer to continue.
2. For each account, check the whole tech stack for products made by [Competitor] (one lookup each, up to 50 rows), whatever area they're filed under. If [Competitor] is a product, check its maker.
3. Record usage strength and last seen. A last-seen date shared by 3+ of an account's rows, or repeated across accounts, is a refresh date.
4. Rate each account by its strongest [Competitor] product seen in the last 90 days (not on a refresh date): High = Entrenched, Medium = Present, Low = Thin, none = Fading. Flag any product first seen within 12 months (the one use of first-seen dates). Editable defaults.
5. For the 3 weakest accounts, pull the stack in the sub-category matching [What I sell] (e.g. Data Warehouse Software, 30 rows each) and name High or Medium products from other vendors: the likely successor.
6. Rank targets: Fading, then Thin, then fewest [Competitor] products first (an easier swap).
7. For the #1 target, pull its top 3 executives in the matching workload (e.g. Data Engineering) or IT, and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the best target and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at the #1 target, the action this week and the dated why-now; if none, say so.
- Table "Install health" (up to 8): Account | Strongest product (strength, last seen) | Products found | Rating.
- Table "Best 3 takeout targets": Account | Successor in place | Why now (dated) | Opening for [What I sell].
- "Leave for later": Entrenched and Present accounts, one line each.
- Detail: successor reads (Replacing, Parallel, Unclear), countries, accounts not resolved.
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Entrenched counts as Red and Present as Amber in any risk check; a newly detected install is a fresh choice, so don't attack it.
- A third-vendor successor already at High means a likely mid-migration: the play is speed, not persuasion.
- "Not found" is not proof they don't use it; say "not detected".

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Trust usage strength and last-seen date; ignore confidence scores and "Generic" rows. A last-seen date shared by many rows is a data refresh. Say "fading", never "dropped".
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Label anything you infer as "likely".
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 420 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
For up to 8 [Accounts], check every [Competitor] product in the stack. Lead with the best takeout target and a named person there. Rate each account Entrenched, Present, Thin or Fading and name the successor already in place.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
For [Account], map the buying committee in the function that owns the product.
```

```text
Check job ads at the best 3 targets for skills naming [Competitor].
```

```text
Write a 90-word email to the named executive at the top target.
```

## Tips for better results

- Keep the list to accounts you can work this quarter; 8 is one pass.
- A rival product still listed but Low across the board is often a renewal you can shape.

## Related prompts

- [Fading tools and replacement windows](../../prompts/03-tech-stack-and-displacement/fading-stack.md): The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.
- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.
- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of companies in your industry and country whose stack includes a competitor's products, with usage strength shown, distributors and inactive names flagged, and a named person at the top account.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `accounts_executives_key_executives_v3`, `get_signal_news_v3`

Status: **tested live**. Prompt id: `compete-fading-installs`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
