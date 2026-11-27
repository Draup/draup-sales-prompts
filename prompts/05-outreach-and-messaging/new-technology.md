[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Email on a new or rival tool

> **Whether a technology or rival product is really in use at the account, how central it is (rated Red, Amber or Green if it's a competitor), where it shows up in public job ads, the priority it links to, and a 100-word email that never reveals stack tracking.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You've heard an account adopted a technology, or a competitor's product turned up there, and you want a timely, credible message: a complement, displace or integrate play. | Account Executive, SDR / BDR, Presales & Solutions, Partnerships & Alliances | Everyone | 2–4 min | Tech stack, Hiring & job postings, Priorities & opportunities, Executives & movement |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Company]` | intel.com |
| `[Technology or competitor]` | Databricks |
| `[Play]` | complement (or displace, or integrate) |
| `[Persona]` | Director of Data Engineering |
| `[What I sell]` | data observability software |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my technical outbound copywriter. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. intel.com]
- Technology or competitor: [product or vendor, e.g. Databricks]
- Play: [complement, displace or integrate]
- Persona: [who reads it, e.g. Director of Data Engineering]
- What I sell: [one line, e.g. data observability software — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by website (exact match) and confirm it is the parent, not a subsidiary, brand or sister company; if unsure, ask me. Use Draup's exact name from then on.
2. Check the whole stack for products by [Technology or competitor]: category, usage strength, first and last evidence. Mark each Active (seen in 6 months) or Fading, and New if first seen in 12 months; rate competitors.
3. If [Company] makes or owns a product in the same category, say a displace play is unlikely.
4. Pull the 3 newest job postings naming the tool (title, date, what the team does with it) and the 12-month count.
5. Pull up to 3 priorities in the tool's workload and judge the [Play] opening: complement (Active, central), displace (Low or Fading), integrate (New, and priorities mention connecting systems).
6. Pull the top 3 executives in [Persona]'s function (full profile titles; flag subsidiaries) and pick the likeliest contact. Also pull the most important news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: the [Play] opening as Strong, Moderate or Weak, with one reason.
- "Check before sending" (directly above the copy): any fact the copy leans on that is single-source or disputed, and what to verify; or "none".
- Email: subject (6 words max) and body (100 words max): the team or programme from the job ads; a question tied to the priority; one offer for [Play]; one ask. Name the tool only if it appears in their public job ads.
- Table "In the stack": Product | Usage strength | Last seen | Status | Rating.
- Detail: job ads with the 12-month count; linked priority (Draup's words, source, quarter); Gaps (what Draup lacked, to ask in discovery).

RULES
- "First seen" is Draup's first public evidence, not a contract date; never write "you just bought".
- Never disparage the tool or its maker. If it isn't in the stack or job ads, say so and stop before writing.
- Copy: one ask; no flattery, "I noticed", hype, exclamation marks or fiscal quarters; pose links to their plans as questions; cite only public sources (announcements, news, earnings calls, job ads), never Draup or how you found them.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling.
- Search by maker, whatever area products are filed under; for very broad makers (Microsoft, Google, Amazon), also name the category.
- Rating: an installed competitor product with High usage in the workloads of What I sell is Red, Medium is Amber, else Green. Newly detected (first seen within 12 months) is a separate Amber signal.
- If [Company] sells technology itself, skip priorities about products it sells.
- Fact check: tag each fact Confirmed (company announcement, filing or 2+ independent sources), Single source or Conflicting; keep single-source numbers and disputed names or dates out of the copy.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Phone-first: bottom line, next step and copy first; at most 2 tables (5 columns, 10 rows); the rest under "Detail". About 400 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step first (a named reader, a dated why-now). Check [Company]'s stack for [Technology or competitor] with usage strength and rating; count job ads naming it; link a priority; write a 100-word [Play] email to a [Persona].
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Which other tools appear next to [Technology or competitor] in the same job ads?
```

```text
Who owns this area at [Company]? Show up to 5 people with full titles.
```

```text
Rewrite the email for the integrate play, aimed at an enterprise architect.
```

```text
Run the competitor check for a second vendor in the same category.
```

## Tips for better results

- Job ads are public, so they're the safest way to mention a tool in an email.
- A tool with High usage and recent evidence is usually central: lead with a complement or integration angle rather than a rip-and-replace.
- If the account makes its own tool in the same category, the verdict will say so; a displace pitch rarely lands there.

## Related prompts

- [Is a competitor installed?](../../prompts/03-tech-stack-and-displacement/competitor-installed.md): A clear verdict on whether a competitor's products are live in the account's stack, rated Red, Amber or Green, framed correctly as a rival to displace, an adjacent tool or a platform you run on, with a named person to call.
- [What tools they adopted this year](../../prompts/03-tech-stack-and-displacement/recent-adoptions.md): The tools first detected at the account in the last 12 months, labelled as competing with, complementing or unrelated to what you sell, with any new competitor product flagged Amber first and a named person to call.
- [Which tools their job ads are building](../../prompts/04-signals-and-timing/practice-shift.md): The software tools in the account's job ads, matched against its installed stack and sorted into New, Building, Core and Coasting, so you see where people and budget are moving before it hits the press, with a named person to call.
- [Battlecard: beat a rival software vendor](../../prompts/16-content-and-enablement/battlecard-product.md): A one-page internal battlecard on a rival software vendor: its most-used products, the largest end-user companies running them with usage strength, recent moves, how to beat it, the objection to expect and the first account to use the card on.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_account_id`, `get_account_tech_stack_products_v3`, `accounts_hiring_job_postings_v3`, `get_account_priorities_v3`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `outreach-new-technology`.

</details>

---

[Back to Outreach and messaging](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
