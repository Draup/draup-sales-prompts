[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)

# Run an ABM campaign for 10–20 accounts

> **Goal:** Pick 10–20 target accounts, tier them, write each one a personalised opener from its own priorities and signals, multithread the top accounts, nurture the rest and refresh the list every week.

**For:** Marketing & ABM, SDR / BDR, Account Executive · **Time:** About 20 min with quick versions, 50–70 min with detailed · **Steps:** 5

**Step 0.** [Connect Draup for Sales](../guides/connect.md) and run [Tell your AI about you](../prompts/00-start-here/about-me.md) so your assistant knows what you sell. Then run the steps below in the same chat.

## Step 1. Tier my accounts by fit and timing

Scores up to 25 candidate accounts on fit and timing for what you sell; keep the top 10–20 for the campaign.

**Look for:** A and B accounts for the campaign, any account capped at C for low fit, and websites matched by name, with their score, to check before you load them.

Open the full prompt: [Tier my accounts by fit and timing](../prompts/11-account-planning/propensity-tiering.md)

Quick version:

```text
Bottom line and next step (named person, dated why-now) first. Tier [Accounts] for [What I sell] on fit (postings in my workloads, installed [Competitor]) and timing; Fit under 25 caps at C; show any name-matched website's score.
```

## Step 2. ABM openers for 10 accounts at once

Writes a 2-sentence opener per account from one priority and one 60-day signal. Run it twice for 20 accounts: accounts 1–10, then 11–20.

**Look for:** Strong rows (signal ties to the priority) launch in week 1; the rest go to the nurture sequence in step 4. Check no opener pitches a technology account its own product category.

Open the full prompt: [ABM openers for 10 accounts at once](../prompts/16-content-and-enablement/abm-messages.md)

Quick version:

```text
Bottom line and next step first: for up to 10 of [Accounts], a 2-sentence opener to a [Persona], in their words, tied to one [Business function] priority and one 60-day signal. Strong first (signal ties to the priority).
```

## Step 3. Emails to three buyers at one account

For the 2–3 A-tier accounts with Strong rows, opens three threads (economic buyer, technical buyer, champion). Reuse step 2's priority and signal for that account.

**Look for:** A named person for each role, a different priority per thread and a staggered send plan.

Open the full prompt: [Emails to three buyers at one account](../prompts/05-outreach-and-messaging/multithread.md)

Quick version:

```text
Bottom line and next step first (who to email first, named). Give [Company]'s economic buyer, technical buyer and champion each a different priority, name a person for each, and write two emails each with a staggered send plan.
```

## Step 4. 3-email sequence for one industry persona

Writes the 3-email nurture sequence for your main persona in the campaign's main industry.

**Look for:** Emails that open with a dated industry move, never presented as your customer. Load the accounts without a Strong row from step 2.

Open the full prompt: [3-email sequence for one industry persona](../prompts/16-content-and-enablement/email-sequence.md)

Quick version:

```text
Bottom line and next step first: a 3-email sequence (120 words each, with subjects) for a [Persona] in [Vertical], on 3 [Business function] priorities, each with a dated company example, plus the first account to load.
```

## Step 5. Weekly trigger sweep for my book

Every Monday of the campaign, checks up to 10 campaign accounts for new triggers (run it twice for 20).

**Look for:** A new trigger at a nurture account: move it to a personal touch that week, using the person and so-what it names.

Open the full prompt: [Weekly trigger sweep for my book](../prompts/04-signals-and-timing/weekly-book-sweep.md)

Quick version:

```text
Bottom line and next step first (named person, dated why-now). For [Accounts], list [Window]'s real triggers, including leadership changes effective in the window, each with a so-what for [What I sell]; give quiet accounts their nearest item outside it.
```

## What you finish with

A tiered campaign list of 10–20 accounts, a sourced opener for each, three-person threads at the top accounts, a nurture sequence for the rest and a weekly trigger check that moves accounts from nurture to personal outreach.

---

[Home](../README.md) · [Connect Draup](../guides/connect.md) · [Use as a skill](../guides/use-as-a-skill.md) · [All prompts](../README.md#find-prompts-by-sales-job) · [Playbooks](../playbooks/README.md) · [Glossary](../guides/glossary.md)
