[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Attach targets on a partner platform

> **A sized, ranked list of companies in your industry and country that run a platform you integrate with and show no sign of your rival add-on, with the platform confirmed, a dated why-now and a named owner for the top 3.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| You sell an add-on or integration for a platform (SAP, Salesforce, ServiceNow, Snowflake) and want a co-marketing or marketplace list to work with the platform vendor's field team. | Partnerships & Alliances, Marketing & ABM, SDR / BDR, Account Executive | Software sellers | 4–6 min | Company directory, Tech stack, News signals |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Platform]` | SAP S/4HANA |
| `[Competitor]` | Celonis |
| `[Vertical]` | Automotive |
| `[Country]` | Germany |
| `[What I sell]` | process-mining add-on for SAP |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my platform-alliances and marketplace analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Platform: [Product we integrate with, as Draup names it, e.g. SAP S/4HANA]
- Competitor: [Maker of the rival add-on whose products must be absent, e.g. Celonis]
- Vertical: [Draup industry, e.g. Automotive]
- Country: [HQ country in full, e.g. Germany]
- What I sell: [One line, e.g. process-mining add-on for SAP — skip if you ran the start-here prompt]

STEPS
1. Turn the inputs into Draup's exact names; say which you used.
2. Size the list: companies with primary industry [Vertical], HQ in [Country], [Platform] in their tech stack and no product made by [Competitor] anywhere in the stack. Using the names-only view, check whether a 50th, 100th and 250th match exists, to band the total.
3. Run the same band check without the [Competitor] condition, labelled as such, so I can see what share of [Platform] users show no rival.
4. Pull the top 10 with full detail, by revenue: workforce, revenue, Opportunity Index, parent, main providers.
5. Flag: Subsidiary (name the parent; the add-on may be bought centrally), Misfiled, Possibly inactive.
6. For the top 3 unflagged, confirm the platform: pull the platform maker's products in the platform's exact category only (e.g. "Enterprise Resource Planning Software (ERP)" for S/4HANA), with usage strength and last seen. A maker-only pull can cut the platform off.
7. People and timing: for the same 3, pull the top leader in the function closest to [What I sell] (full profile title) and the most important news item from the last 90 days where the company is the actor.

OUTPUT
- Bottom line: 2 sentences — list size and the account to take to the platform vendor first.
- Recommended next step: a person from step 7 (name and title), what to do (often with the platform vendor's partner manager), and why now (the dated news item or another dated fact); if none turned up, say so.
- Header line: "[Band] run [Platform] with no [Competitor] products; [band] run [Platform] in total."
- "Attach list" (top 10): Rank | Company | Revenue (USD M, FY) | Parent | Flag.
- "Top 3 confirmed": Company | [Platform] strength and last seen | Why now (dated) | Likely owner (name, title) | Opener angle.
- Gaps: what Draup didn't have — worth asking the platform vendor.
- Detail: workforce and Opportunity Index per row; "Likely missing big names" (up to 3, labelled "probably runs [Competitor]; not checked").

RULES
- "No [Competitor] products" means Draup sees no public evidence of them; say "no sign of", never "doesn't use".
- If [Platform] isn't confirmed or was last seen over 12 months ago (editable default), drop the company from the top 3 and say why.
- Shareholding notices and recalls are not a why-now.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has nothing, write "Not in Draup"; never fill from memory. If a name returns nothing, retry once with Draup's spelling.
- Trust usage strength and last-seen date; ignore first-seen dates, confidence scores and "Generic" rows.
- Pull lists and priorities 10 at a time. Count first when a list could be long; never report a total that drops one of my conditions.
- News: the named company must be the actor. Drop stock chatter, charity, sponsorships, awards, political commentary, passing mentions, look-alikes and re-dated stories, but keep any item that bears directly on What I sell, even if it's normally noise. If sources conflict on a name or number, say so and don't repeat either as fact; treat single-source figures as unverified.
- Use full profile titles and professional information only. If several people share a title, list them and ask. Leadership data lags about 3 months; give the latest move date.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows each); reference tables under "Detail". Keep to about 430 words including tables.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line and next step (named owner, dated why-now) first. Which [Vertical] companies in [Country] run [Platform] with no [Competitor] products? Band the total vs all [Platform] users, show the top 10 by revenue, confirm the top 3.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Show rows 11–20 the same way.
```

```text
Draft a short note to the platform vendor's partner manager proposing a joint campaign on the top 10 (check our Draup licence before sharing the list).
```

```text
For the top 3, who else owns [Platform] there? Show leaders with full titles.
```

## Tips for better results

- Platform vendors respond to lists that help them sell their own platform. Lead with accounts where the platform is current and something just changed.
- If the list is mostly mid-size companies, that's often where rival add-ons haven't landed yet. Size your campaign for that segment.

## Related prompts

- [Size a vendor's install base](../../prompts/03-tech-stack-and-displacement/vendor-install-base.md): What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion, with a named person at the vendor or a first target to approach.
- [Target list: companies running a competitor](../../prompts/03-tech-stack-and-displacement/displacement-list.md): A true count and a ranked list of companies in your industry and country whose stack includes a competitor's products, with usage strength shown, distributors and inactive names flagged, and a named person at the top account.
- [Accounts a partner can open for you](../../prompts/13-partners-and-alliances/sourced-pipeline.md): A sized list of companies in your industry and country where a named partner already delivers work and your product (or a rival's) isn't in the stack, with how deep the partner is at the top 5 and a named buyer at the best one.
- [ABM openers for 10 accounts at once](../../prompts/16-content-and-enablement/abm-messages.md): A table of short openers for up to 10 accounts per pass, each written to your persona in their language and tied to one stated priority and one dated signal from the last 60 days, graded Strong, OK or Weak, with sources and an optional joint partner note.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`extract_entities`, `get_universe_companies_v3`, `get_account_tech_stack_products_v3`, `get_top_signals`, `accounts_executives_key_executives_v3`

Status: **tested live**. Prompt id: `partners-platform-attach`.

</details>

---

[Back to Partners and alliances](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
