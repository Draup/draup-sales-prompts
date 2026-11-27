[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# How a rival's strategy is shifting

> **How a competitor's stated priorities moved across its last three earnings calls, the acquisitions, leaders and cuts behind each shift, what changes in your deals and who to brief.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| After a rival's earnings call, a big acquisition or a leadership change. Use this for the strategic read; use "What a rival did this quarter" (compete-recent-moves) for a dated list of moves. | Sales Leader & RevOps, Presales & Solutions, Marketing & ABM, Account Executive, Partnerships & Alliances | Everyone | 4–6 min | Earnings calls & filings, Priorities & opportunities, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Competitor]` | salesforce.com |
| `[What I sell]` | customer service platform |
| `[Area to watch]` | customer service and AI agents (optional) |
| `[Account to defend or win]` | att.com (optional) |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my competitive strategist who reads earnings calls. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [website, e.g. salesforce.com]
- What I sell: [one line, e.g. customer service platform — skip if you ran the start-here prompt]
- Area to watch (optional): [e.g. customer service and AI agents]
- Account to defend or win (optional): [website of a live deal or key customer, e.g. visa.com]

CONTEXT (why this matters)
A real shift shows three ways: a louder priority on the call, money behind it, people behind it. Read a tech vendor's priorities as product moves.

STEPS
1. Find [Competitor] by website and confirm it's the parent, not a subsidiary; if unsure, ask me.
2. List its earnings-call transcripts; note the latest three with fiscal quarter and release date.
3. Pull its key priorities grouped by function (up to 3 each, with fiscal quarter). Sort into New in the latest quarter, Repeated, and Older only. Focus on [Area to watch], or else on areas closest to [What I sell].
4. Search Draup's news for [Competitor], last 6 months: executive appointments and exits, acquisitions, divestments, layoffs. Review at least 20 items; mark the most important from the last 90 days.
5. Pull acquisitions in the last 12 months and reconcile with news. Flag announced-but-not-closed deals.
6. For each theme, link the priority, the money and the people.
7. If I gave [Account to defend or win], find it by website and pull its top 3 executives in the function closest to [What I sell] (one page of 10).

OUTPUT
- Bottom line: 2 sentences — the shift that matters most and what it means for [What I sell].
- Recommended next step: a named person (name, full title) at [Account to defend or win], the action this week, and [Competitor]'s dated move as the why-now; with no account given, name the role to brief.
- Table "Strategy read" (3): Shift | Strength (Strong = call + money + people; Moderate = two; Talk only) | Dated evidence | What changes in deals.
- Table "Money and people behind it" (up to 8): Date | Move | Size if given | Theme.
- "Trap question": one discovery question that exposes the rival's integration or execution risk.
- Detail: calls covered (Fiscal quarter | Release date) and priority shifts (Theme | New, Repeated or Fading | Latest quarter | Example priority).
- Gaps: what Draup didn't have; ask it in discovery.

RULES
- Keep only acquisitions and leadership items where [Competitor] is the actor and the event is in the window.
- Never estimate layoff numbers.
- Say where they'll bundle or discount, what new objection to expect, and where they're distracted.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me.
- Date and source every fact (headline for news). Write "Not in Draup" for gaps; never fill from memory.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do. News-based priorities carry a month instead.
- News: one question search plus the company feed (deals, M&A, executive moves, investments, layoffs), company as actor. Drop stock chatter, charity, awards, political commentary, passing mentions, look-alikes and re-dated stories; keep any item bearing directly on What I sell, even if normally noise. If sources conflict on a name or number, say so and repeat neither; single-source figures are unverified.
- The acquisitions table can miss deals; check 12 months of M&A news too. Divestments come from news only.
- Pick people by profile title, not rank; skip subsidiary, misfiled or look-alike profiles; use Draup's function names (IT, Sales & Marketing). No C-level, EVP or "Head of"? Check one unfiltered page for the parent's Chief, EVP or CIO. If several share a title, ask. No personal contact details.
- Phone-first: Bottom line and next step first; max 2 tables up front (5 columns, 10 rows). Keep everything above Detail to about 450 words, tables included; Detail and Gaps follow or are offered.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
How has [Competitor]'s strategy shifted across its last 3 earnings calls? Lead with the bottom line and who to brief. Rate each shift Strong, Moderate or Talk only, and say what changes in my deals.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Pull the latest call and quote the two passages that support the strongest shift.
```

```text
Which of my accounts run the products [Competitor] just acquired?
```

```text
Update my battlecard for [Competitor] with these shifts.
```

## Tips for better results

- "Talk only" themes are often marketing; Strong themes are what their reps will push next quarter.
- Acquisitions mid-integration are a classic opening: ask customers about roadmap certainty.

## Related prompts

- [What changed between two earnings calls](../../prompts/01-account-research/call-over-call.md): Themes that are new, stronger, weaker or dropped between the last two earnings calls, each with a quote, who owns them, and a 2-line talk track for your next QBR.
- [What a rival did this quarter](../../prompts/09-competitive-intelligence/recent-moves.md): The few moves a competitor made in the last 90 days that change your deals (customer wins, partnerships, launches, deals and leadership), the accounts to defend or attack, and the named person to call at the top one.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_transcripts`, `get_key_account_priorities`, `get_signal_news_v3`, `build_news_filters_v3`, `accounts_partnerships_mergers_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `compete-strategy-shift`.

</details>

---

[Back to Competitive intelligence](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
