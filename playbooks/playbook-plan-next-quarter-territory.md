[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)

# Sales leader plan: market to coverage

> **Goal:** As a sales leader, size the market for what you sell, pick the region to staff, tier the accounts, carve balanced territories and set each rep's coverage, then run the plan week to week.

**For:** Sales Leader & RevOps, Marketing & ABM · **Time:** 60–80 min · **Steps:** 6

**Step 0.** [Connect Draup for Sales](../guides/connect.md) and run [Tell your AI about you](../prompts/00-start-here/about-me.md) so your assistant knows what you sell. Then run the steps below in the same chat.

## Step 1. One-page vertical market snapshot

Gives the industry picture: size and growth, top priorities with likely owners, and technologies gaining ground.

**Look for:** The 2–3 priorities closest to what you sell. Industry totals are global and IT spend is modelled, so don't use them to compare accounts.

Open the full prompt: [One-page vertical market snapshot](../prompts/14-industry-intelligence/vertical-snapshot.md)

Quick version:

```text
Bottom line and next step first: a one-page snapshot of [Vertical] (in [Region] if given): size and growth, the 5 priorities that fit [What I sell] with dated company proof, the top buyers, and who to call first.
```

## Step 2. Which region gets the next rep

Compares 2–5 regions on how many sizeable accounts are active in your workloads, where your rivals sit, and revenue at stake.

**Look for:** The region with the most accounts active in your workloads per rep. Read "What's missing" for big groups headquartered elsewhere before you commit headcount.

Open the full prompt: [Which region gets the next rep](../prompts/15-sales-leadership-and-revops/territory-potential.md)

Quick version:

```text
Bottom line and next step first: which of [Regions] gets the next rep for [What I sell] in [Vertical] ([Minimum employees]+ staff), scored on accounts active in my workloads, rivals and revenue, plus the first account and person.
```

## Step 3. Tier my accounts by fit and timing

Tiers the chosen region's top accounts on fit and timing for what you sell.

**Look for:** A real spread across A, B and C (it re-tiers by rank if over half land in one tier), with the driver behind each A account.

Open the full prompt: [Tier my accounts by fit and timing](../prompts/11-account-planning/propensity-tiering.md)

Quick version:

```text
Bottom line and next step (named person, dated why-now) first. Tier [Accounts] for [What I sell]: fit (postings in my workloads, installed [Competitor]) and timing (news, hiring, growth), A/B/C relative to the list, one-line reason each.
```

## Step 4. Carve balanced territories by geography

Carves the accounts into balanced territories by geography: whole regions first, single accounts moved only to fix a big imbalance.

**Look for:** No territory more than about 10% off balance, no city split across reps, and holding or private-equity firms excluded.

Open the full prompt: [Carve balanced territories by geography](../prompts/11-account-planning/territories.md)

Quick version:

```text
Bottom line and next step first. Count [Vertical] companies (primary industry) headquartered in [Country] with [Minimum employees]+ staff, drop owned, holding and private-equity firms, and split the rest into [Number of territories] territories by HQ region, balanced within 10%.
```

## Step 5. Sort my book into coverage tiers

Sets coverage inside each territory: Strategic, Growth, Maintain or Deprioritise, scored on your workloads and rivals as well as size and momentum.

**Look for:** No rep with more than about 5 Strategic accounts, and every flagged account (spin-off, merger, private) checked by hand.

Open the full prompt: [Sort my book into coverage tiers](../prompts/15-sales-leadership-and-revops/book-segmentation.md)

Quick version:

```text
Bottom line and next step first: sort [Accounts] into Strategic, Growth, Maintain or Deprioritise for [What I sell], scoring revenue, postings in my workloads, rivals installed and growth, with a coverage model per tier.
```

## Step 6. Which accounts each rep works this week

Runs the plan week to week: checks each rep's accounts for fresh triggers and names this week's 5 actions.

**Look for:** Owners with several Strong triggers and no plan (they need help) and owners whose whole book is quiet (they need new accounts).

Open the full prompt: [Which accounts each rep works this week](../prompts/15-sales-leadership-and-revops/coverage-check.md)

Quick version:

```text
Bottom line and next step first: for [Accounts and owners], find triggers in [Window] that matter to [What I sell], group them by owner, rank this week's 5 actions with a named contact for action 1, and list quiet books.
```

## What you finish with

A sized market view, the region to staff next, tiered accounts, balanced territories per rep, a coverage model with named Strategic accounts, and a weekly action list. Ask any leader prompt for a slide version (5 bullets + 1 table) for the board.

---

[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)
