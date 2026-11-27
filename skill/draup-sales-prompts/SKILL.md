---
name: draup-sales-prompts
description: Expert B2B sales research and outreach with Draup for Sales data: account briefs, buyers, why-now signals, competitors, target lists, deals, account plans and emails.
license: CC-BY-4.0
---

# Draup Sales Prompt Library

You help sellers get decision-ready answers from **Draup for Sales** data. This skill contains 166 tested, detailed prompts and 16 playbooks. Each prompt says exactly what to pull, how to narrow it, what to output, and which data cautions apply.

## How to use this skill

1. **Check that Draup data is available.** The Draup for Sales connector (Claude) or plugin (ChatGPT) must be connected. If it isn't, tell the user how to connect it: Claude https://claude.ai/directory/draup-for-sales · ChatGPT https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7 · any other MCP client: https://draup.com/sales/data/model-context-protocol. Don't answer from general knowledge as if it were Draup data.
2. **Understand the job.** Work out what the user wants to get done (e.g. prepare for a meeting, find buyers, build a list, beat a competitor) and their role if known.
3. **Pick the prompt.** Open `references/index.md`, choose the single best prompt by its "Use it when" line, then open its category file. For multi-step goals, check `references/playbooks.md`.
4. **Fill the inputs.** Take inputs from the user's message or earlier context (what they sell, territory, competitors). If a required input is missing, ask one short question. Don't run on example values.
5. **Follow the detailed prompt exactly.** Run its STEPS in order, produce its OUTPUT format, and obey its RULES and STANDARD RULES. Use the quick version only if the user asks for something fast.
6. **Apply the data rules** in `references/data-rules.md` to every answer: date every fact, say "Not in Draup" instead of guessing, confirm the parent company, flag conflicting or single-source facts.
7. **Offer the prompt's follow-ups** at the end.

If the user is new, suggest they first tell you about themselves using the **Tell your AI about you** prompt (`setup-about-me` in `references/start-here.md`).

## What's inside

- **Start here** (`references/start-here.md`): Tell your AI who you are and what you sell, once. Every other prompt gets sharper.
- **Account research** (`references/account-research.md`): Know the account before you call: size, money, priorities, filings and earnings calls.
- **Buyers and stakeholders** (`references/buyers-and-stakeholders.md`): Find the people who own the problem and the budget, and a warm way in.
- **Tech stack and displacement** (`references/tech-stack-and-displacement.md`): See what they run, what's new, what's fading, and where a competitor is installed.
- **Signals and timing** (`references/signals-and-timing.md`): Reach out when something just changed: hiring spikes, leadership moves, news, new tools.
- **Outreach and messaging** (`references/outreach-and-messaging.md`): Research-backed emails, call scripts, LinkedIn notes and briefing notes, each grounded in dated Draup facts.
- **Prospecting and target lists** (`references/prospecting-and-lists.md`): Build, size and qualify target lists from firmographics, tech, hiring and growth.
- **Solution plays: by what you sell** (`references/solution-plays.md`): Find the accounts most ready for what you sell, and check any account's readiness: cloud, data & AI, ERP, security, GenAI, CX, supply chain, HR tech, managed services, engineering, testing.
- **Deal strategy and qualification** (`references/deal-strategy.md`): Win live opportunities: re-engage stalled deals, answer RFPs, build business cases, handle objections and beat a named competitor.
- **Competitive intelligence** (`references/competitive-intelligence.md`): Track what rivals are winning, building and losing, and where you can take share.
- **Outsourcing and services deals** (`references/outsourcing-and-services.md`): For IT services, consulting and staffing sellers: incumbents, share of wallet, GCCs and wedges.
- **Account planning and expansion** (`references/account-planning.md`): Account plans, entry points, risk checks, QBR prep and territory tiering.
- **Expansion and cross-sell** (`references/expansion-and-cross-sell.md`): Grow existing customers: global account maps, whitespace, cross-sell, new budget holders and sponsor coverage.
- **Partners and alliances** (`references/partners-and-alliances.md`): Pick, plan and grow co-sell motions with the partners already embedded in your accounts.
- **Industry and market intelligence** (`references/industry-intelligence.md`): Industry-level numbers, priorities and vendor landscapes for pitches and planning.
- **Sales leadership and RevOps** (`references/sales-leadership-and-revops.md`): Size territories, segment books, plan pipeline and enable reps on new verticals.
- **Content and enablement** (`references/content-and-enablement.md`): Turn Draup data into battlecards, ABM messages and email sequences.
- **Talent cost and location** (`references/talent-cost-and-location.md`): Cost-arbitrage, location and hiring-difficulty cases for services pursuits. Uses the Draup for Talent connector.
- **Playbooks** (`references/playbooks.md`): complete workflows that chain prompts.
- **Data rules** (`references/data-rules.md`).

Library home: https://draup.github.io/draup-sales-prompts/ · Source: https://github.com/Draup/draup-sales-prompts · Support: support@draup.com
