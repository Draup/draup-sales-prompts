[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)

# Build a quarter's pipeline for one solution

> **Goal:** Go from one solution area (for example cloud migration, data, ERP, security or HR tech) to a scored target list, qualified accounts with a named buyer, the incumbents to work around, and timed first touches that cite each account's own evidence.

**For:** Account Executive, SDR / BDR, Sales Leader & RevOps, Services, SI & Staffing Seller, Marketing & ABM · **Time:** About 20 min with quick versions, 60–75 min with detailed · **Steps:** 6

**Step 0.** [Connect Draup for Sales](../guides/connect.md) and run [Tell your AI about you](../prompts/00-start-here/about-me.md) so your assistant knows what you sell. Then run the steps below in the same chat.

## Step 1. Find accounts ripe for cloud migration

Builds the evidence-scored target list for your solution area in one industry and country. The example is cloud migration; swap in the matching target-list prompt for data, ERP, security, HR tech and the others.

**Look for:** The top 3, the evidence behind each score and who to call. The set-aside list (misfiled, HQ elsewhere, companies that sell the technology themselves) is in the detailed version.

Open the full prompt: [Find accounts ripe for cloud migration](../prompts/07-solution-plays/cloud-targets.md)

Quick version:

```text
Bottom line and next step first: rank [Industry] companies in [Territory] for cloud migration on a 0–10 score (hiring per 1,000 staff, priorities, stack, outsourcing, 90-day news) and name who to call at the top 3.
```

## Step 2. Is this account ready for cloud migration?

Qualifies each top account from step 1. Use the readiness prompt that matches your solution.

**Look for:** A strong score with a dated why-now and a named owner; if the score is low, move to the next account rather than forcing it.

Open the full prompt: [Is this account ready for cloud migration?](../prompts/07-solution-plays/cloud-readiness.md)

Quick version:

```text
Bottom line and next step first: score [Company]'s readiness for cloud migration (0–20) on five dated dimensions, rate the incumbents, name the owner with a dated why-now, and give 4 discovery questions.
```

## Step 3. Map the buying committee

Turns the owner from step 2 into a full committee in the matching function. Reuse the owner named in step 2 as the starting point.

**Look for:** The entry point and sponsor it names first, by full title, and anyone flagged as subsidiary staff.

Open the full prompt: [Map the buying committee](../prompts/02-buyers-and-stakeholders/buying-committee.md)

Quick version:

```text
Buying committee at [Company] for [Business function or workload]: entry point and sponsor by name first, then up to 10 people with full title, unit (flag subsidiaries), likely role and linked priority. No economic buyer? Check one more page.
```

## Step 4. Who's already working each priority

Shows, for each priority in the function, which tools and providers already work it.

**Look for:** One priority tagged Displace or Greenfield: that's your wedge.

Open the full prompt: [Who's already working each priority](../prompts/03-tech-stack-and-displacement/priority-stack-incumbent-map.md)

Quick version:

```text
Bottom line and next step first (named owner, dated why-now). Map [Company]'s [Business function] priorities to the tools and providers linked to each, rate my [Competitor] products, and tag each priority Displace, Co-sell, Greenfield or Not ours.
```

## Step 5. Peers' outsourcing deals for social proof

Finds recent engagements at each account's peers in your workload, so the first touch carries social proof.

**Look for:** One of the 3 proof lines per account, cited as a public industry example, never as your own customer.

Open the full prompt: [Peers' outsourcing deals for social proof](../prompts/10-outsourcing-and-services/peer-deals.md)

Quick version:

```text
Bottom line and next step (named person, dated why-now) first. Find the 10 most recent [Workload] engagements at [Company]'s peers (same industry and HQ country) in Draup: month, customer, provider, the work. Then write 3 proof lines.
```

## Step 6. Signal-led emails for up to 10 accounts

Writes the first touch from the freshest relevant signal. Reuse the why-now from step 2 if it's under 60 days old.

**Look for:** One fact-checked signal in a 45-word opener ending in one ask, sent to the entry point from step 3. No signal in 60 days? Keep the account in nurture.

Open the full prompt: [Signal-led emails for up to 10 accounts](../prompts/04-signals-and-timing/signal-to-email.md)

Quick version:

```text
Bottom line and next step first. For each of [Accounts] (up to 10), pick the 60-day signal most relevant to [What I sell] and my [Territory], fact-check it, and write a 45-word [Persona] opener ending in one ask.
```

## What you finish with

A quarter's pipeline for one solution area: a scored target list, a readiness verdict and wedge for the top accounts, a named champion and sponsor for each, a peer proof line and a ready-to-send opener.

---

[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)
