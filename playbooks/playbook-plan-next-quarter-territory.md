[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)

# Sales leader plan: market to coverage

> **Goal:** As a sales leader, size the market for what you sell, pick where to add the next rep, tier the accounts, carve balanced territories, set coverage and next quarter's targets, then run the plan week to week.

**For:** Sales Leader & RevOps, Marketing & ABM · **Time:** About 25 min with quick versions, 70–90 min with detailed · **Steps:** 8

**Step 0.** [Connect Draup for Sales](../guides/connect.md) and run [Tell your AI about you](../prompts/00-start-here/about-me.md) so your assistant knows what you sell. Then run the steps below in the same chat.

## Step 1. One-page vertical market snapshot

Gives the industry picture: size and growth, top priorities and the top buyers.

**Look for:** The 2–3 priorities closest to what you sell. Industry totals are global, so don't use them to compare accounts.

Open the full prompt: [One-page vertical market snapshot](../prompts/14-industry-intelligence/vertical-snapshot.md)

Quick version:

```text
Bottom line and next step first: a one-page snapshot of [Vertical] in [Region]: global size and growth plus the top-10 buyers' regional revenue, the 5 priorities that fit [What I sell] with dated company proof, and who to call first.
```

## Step 2. Which region gets the next rep

Compares 2–5 countries for one industry, or 2–4 industries in one country, on accounts active in your workloads, rivals in use and revenue.

**Look for:** The segment with the most workload-active accounts per rep: add your current coverage so the per-rep score can change the answer. Big groups headquartered elsewhere are listed in the detailed version.

Open the full prompt: [Which region gets the next rep](../prompts/15-sales-leadership-and-revops/territory-potential.md)

Quick version:

```text
Bottom line and next step first: which of [Compare] (2–5 countries for [Vertical], or 2–4 industries in one country) gets the next rep for [What I sell], scored on workload-active accounts, rivals at High or Medium usage, revenue and coverage.
```

## Step 3. Tier my accounts by fit and timing

Tiers up to 25 of the winning segment's top accounts on fit and timing.

**Look for:** A real spread across A, B and C, accounts capped at C for low fit, and the driver behind each A account.

Open the full prompt: [Tier my accounts by fit and timing](../prompts/11-account-planning/propensity-tiering.md)

Quick version:

```text
Bottom line and next step (named person, dated why-now) first. Tier [Accounts] for [What I sell] on fit (postings in my workloads, installed [Competitor]) and timing; Fit under 25 caps at C; show any name-matched website's score.
```

## Step 4. Carve balanced territories by geography

Carves the winning segment into balanced territories by geography. Reuse step 2's country, industry and size cut so the counts match.

**Look for:** No territory more than about 10% off balance, holding or private-equity firms excluded, and every single-account move listed.

Open the full prompt: [Carve balanced territories by geography](../prompts/11-account-planning/territories.md)

Quick version:

```text
Bottom line and next step first. Count [Vertical] companies (primary industry) headquartered in [Country] with [Minimum employees]+ staff, drop owned, holding and private-equity firms, and split the rest into [Number of territories] territories by HQ region, balanced within 10%.
```

## Step 5. Sort my book into coverage tiers

Sets coverage inside each territory: Strategic, Growth, Maintain or Deprioritise. Reuse step 3's account list rather than looking the accounts up again.

**Look for:** No rep with more than about 5 Strategic accounts, and every flagged account (spin-off, merger, private) checked by hand.

Open the full prompt: [Sort my book into coverage tiers](../prompts/15-sales-leadership-and-revops/book-segmentation.md)

Quick version:

```text
Bottom line and next step first: sort [Accounts] into Strategic, Growth, Maintain or Deprioritise for [What I sell], scoring revenue, postings in my workloads, rivals installed and growth, with a coverage model per tier.
```

## Step 6. Next quarter's target accounts, ranked by triggers

Sets next quarter's targets: searches 90-day news account by account for the top 20 workload-active accounts and ranks them by triggers.

**Look for:** Accounts tagged Act this month (ideally two trigger types) and the counts per tag for SDR targets. Accounts beyond the top 20 are "not searched", not quiet.

Open the full prompt: [Next quarter's target accounts, ranked by triggers](../prompts/15-sales-leadership-and-revops/pipeline-targets.md)

Quick version:

```text
Bottom line and next step first: for the top 20 workload-active [Vertical] accounts in [Territory] ([Minimum employees]+ staff), search 90-day news per account, rank by distinct triggers and rival usage, with a dated why-now each for [What I sell].
```

## Step 7. Brief reps on a new industry

Optional: run it when a territory includes an industry the team is new to.

**Look for:** The buyer titles and 10 terms for the enablement session. If it says Draup has no industry priorities, the funding table is company proof.

Open the full prompt: [Brief reps on a new industry](../prompts/15-sales-leadership-and-revops/vertical-enablement.md)

Quick version:

```text
Bottom line and next step first: brief my reps on [Vertical] for [What I sell] — 10 terms, the top priorities in [Business function], buyer titles at [Reference account], rivals in play and 5 discovery questions.
```

## Step 8. Which accounts each rep works this week

Runs the plan week to week: checks each rep's accounts for fresh triggers and names this week's 5 actions.

**Look for:** Owners with several Strong triggers (they need help) and owners whose whole book is quiet (they need new accounts).

Open the full prompt: [Which accounts each rep works this week](../prompts/15-sales-leadership-and-revops/coverage-check.md)

Quick version:

```text
Bottom line and next step first: for [Accounts and owners], find triggers in [Window] that matter to [What I sell], group them by owner, rank this week's 5 actions with a named contact for action 1, and list quiet books.
```

## What you finish with

A sized market view, where to add the next rep, tiered accounts, balanced territories, a coverage model, next quarter's target list and a weekly action list. Ask any leader prompt for a slide version (5 bullets plus 1 table) for the CRO update.

---

[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)
