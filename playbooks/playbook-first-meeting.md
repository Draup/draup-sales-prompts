# First meeting in 30 minutes

**Goal:** Walk into a first meeting knowing the account, the people in the room and the questions that will earn a second meeting.

**For:** Account Executive, SDR / BDR, Presales & Solutions · **Time:** 25–35 min

**Step 0.** Run [Tell Claude about you](../prompts/00-start-here/about-me.md) so Claude knows what you sell.

## Step 1. 10-minute pre-call snapshot

Gives you the 10-minute picture: size, money, current priorities and what just changed.

**Look for:** One priority and one recent change you can mention in the first two minutes. Check it's the parent company, not a subsidiary.

Open the full prompt: [10-minute pre-call snapshot](../prompts/01-account-research/precall-snapshot.md)

Quick version:

```text
Call with [Company] in 10 minutes. Five bullets, 25 words each: what they do and size; 2 events from the last 90 days; top 3 workloads trending up; the priority closest to [What I sell]; one question.
```

## Step 2. Map the buying committee

Shows who owns the problem and the budget in the function you sell into, including a potential blocker.

**Look for:** Your entry point (likely champion), the sponsor to reach later (economic buyer) and any potential blocker. Go by full titles, not seniority labels. If profiles in Europe or the UK come back empty, ask about the team in the meeting.

Open the full prompt: [Map the buying committee](../prompts/02-buyers-and-stakeholders/buying-committee.md)

Quick version:

```text
Map the buying committee at [Company] for [Business function or Workload]: up to 12 people with full title, unit, location, budget control and likely role (economic buyer, technical buyer, champion, influencer, potential blocker), plus an entry point and a sponsor.
```

## Step 3. Hypothesis-led discovery questions

Turns the snapshot into hypothesis-led questions, each tied to a cited fact.

**Look for:** Pick the 3 questions you'll definitely ask, and the one that tests whether the priority has budget this year.

Open the full prompt: [Hypothesis-led discovery questions](../prompts/02-buyers-and-stakeholders/discovery-questions.md)

Quick version:

```text
Give me a 2-sentence opening insight and 8 discovery questions for [Company], each tied to a dated Draup fact (priority, technology, hiring, leadership move or news), with the hypothesis and what a good answer tells me.
```

## Step 4. Battlecard: rival software vendor

Optional: run it when a known rival is in the deal. Selling services? Use “Battlecard: rival services firm” instead.

**Look for:** The objection their rep will raise and one trap question you can work into discovery.

Open the full prompt: [Battlecard: rival software vendor](../prompts/09-content-and-enablement/battlecard-product.md)

Quick version:

```text
Build an internal Draup battlecard on software rival [Competitor]: top 5 products by install count, the 10 largest companies running them, 180 days of moves, three ways [What I sell] wins and three trap questions.
```

## What you finish with

A one-page meeting brief: account snapshot, who's who, an opening line, your discovery questions with the evidence behind each, and (if a rival is in play) the objection to expect.

[All playbooks](README.md) · [Back to the library](../README.md)
