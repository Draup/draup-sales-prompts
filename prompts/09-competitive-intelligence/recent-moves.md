[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# What a rival did this quarter

> **The few moves a competitor made in the last 90 days that change your deals (customer wins, partnerships, launches, deals and leadership), the accounts to defend or attack, and the named person to call at the top one.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| Before a pipeline review or competitive deal, or when the field asks "what is [Competitor] up to?" Use this for one rival; use "Quarterly competitor watch for the team" for up to 3 side by side, or "How a rival's strategy is shifting" after an earnings call. | Account Executive, Account & Customer Success Manager, Presales & Solutions, Sales Leader & RevOps, Marketing & ABM, Partnerships & Alliances | Everyone | 2–4 min | News signals, Company & financials |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | adobe.com |
| `[What I sell]` | digital experience platform |
| `[Territory]` | North America (optional) |
| `[Our customers]` | Contoso Retail, Fabrikam Foods (optional) |
| `[Our differentiators]` | open architecture, faster time to value (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive-intelligence analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. adobe.com]
- What I sell: [one line, e.g. digital experience platform — skip if you ran the start-here prompt]
- Territory (optional): [e.g. North America; default: my territory from setup]
- Our customers (optional): [names or a saved Draup list, e.g. Contoso Retail, Fabrikam Foods]
- Our differentiators (optional): [e.g. open architecture, faster time to value]

CONTEXT (why this matters)
What matters: named customer wins, bundling partnerships, gap-closing launches, leaders leaving.

STEPS
1. Find [Competitor] by website (no match: retry once by name, show match and score) and confirm the parent, not a subsidiary; if unsure, ask me.
2. Search news for [Competitor], last 90 days (20+ items): wins, partnerships, launches, deals, investments, leadership, layoffs.
3. Pull the feed for the same window, limited to [Competitor] (15 items), to catch misses.
4. Pull 12-month acquisitions and reconcile each with the news (date, target, price).
5. Classify each item: Customer win (a named company adopting or expanding [Competitor]), Partnership, Product launch, M&A or investment, Leadership or layoff, Expansion. Merge repeats; prefer [Territory].
6. Write three signals on where [Competitor] is pushing next, each with two dated items.
7. Pick the account to watch: one of [Our customers] named in a move, or else running [Competitor] at High or Medium (check up to 3 stacks; maker as Draup spells it, e.g. Salesforce.com): Defend. Otherwise the newest Customer win in [Territory]: Attack later. Confirm it's the right company and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the move that matters most and what it means for me.
- Recommended next step: a named person (name, full title) at the top account, the action this week and the dated why-now (or say none).
- Table "Moves that matter" (up to 8, newest first): Date | Type | What happened | Named company | Source.
- Table "Accounts to watch" (up to 8): Company | Move | Defend, Avoid for now or Attack later | Why (likely).
- "Three signals": Signal, dated evidence, what it means for me.
- "Counter-message": 3 bullets, tied to [Our differentiators] if given (60 words max).
- Detail: the rest of the log (up to 15) and the acquisitions check.
- Gaps: what Draup lacked; ask in discovery.

RULES
- A partner release that only mentions [Competitor] is a Partnership; a marketplace listing is not a win.
- Keep only items whose event date falls in the window.
- A rival's outage, breach, price rise or layoff is a counter-message trigger for me; keep it. Never pick an "Avoid for now" account for the next step.
- If the acquisitions table and news disagree, show both; a price from news alone is single-source.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date and source every fact (headline for news); gaps are "Not in Draup", never filled from memory.
- News: a question search plus the company feed (deals, M&A, executive moves, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories unless they bear on What I sell. Conflicting names or numbers: say so, repeat neither; single-source figures are unverified.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- People: pick by full profile title, not rank; check it fits the function (Draup names: IT, Sales & Marketing); flag subsidiary or branch staff. No C-level, EVP or "Head of"? Pull the next page of 10 in the function once for Chief, EVP, CIO or "Head of" titles. Mark "verify" any C-level profile whose tenure or past employers don't fit the parent; keep it out of drafted copy. Several share a title? Ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows); about 420 words above Detail, tables included.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
What did [Competitor] do in the last 90 days that matters to [What I sell]? Lead with the bottom line and a named person at the top account to defend, then dated moves, accounts to watch and a counter-message.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn the counter-message into a 120-word email to the named executive at the top Defend account.
```

```text
For [Named company], check whether [Competitor] products show up in their tech stack and how strong they are.
```

```text
Run the same log for my second competitor and compare the two.
```

## Tips for better results

- Run it monthly for your top two rivals; Accounts to watch is usually the most useful output.
- Partner announcements tell you which services firms are now steering deals toward the rival.
- Add your territory and Our customers: Defend then means your own accounts, and the next step lands in your patch.

## Related prompts

- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.
- [Battlecard: beat a rival services firm](../../prompts/16-content-and-enablement/battlecard-services.md): A one-page internal battlecard on a rival services firm: where it delivers in the work you sell, what it wins, recent moves, how to beat it, trap questions, the objection to expect and the first account to use the card on.
- [How a rival's strategy is shifting](../../prompts/09-competitive-intelligence/strategy-shift.md): How a competitor's stated priorities moved across its last three earnings calls, the acquisitions, leaders and cuts behind each shift, what changes in your deals and who to brief.
- [Quarterly competitor watch for the team](../../prompts/09-competitive-intelligence/quarterly-watch.md): A one-page quarterly report on up to 3 rivals: a side-by-side scorecard including hiring in your space, each one's top moves and leadership changes, three team actions and a named account contact for the biggest threat.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_signal_news_v3`, `build_news_filters_v3`, `get_news_feed_v3`, `accounts_partnerships_mergers_v3`, `accounts_executives_key_executives_v3`, `get_account_tech_stack_products_v3`

Status: **tested live**. Prompt id: `compete-recent-moves`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
