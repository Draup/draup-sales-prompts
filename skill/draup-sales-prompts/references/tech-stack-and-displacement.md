# Tech stack and displacement

See what they run, what's new, what's fading, and where a competitor is installed.

## What they run in one tech area

- **id:** `tech-stack-category`
- **What you get:** What they run in one area, ranked by how central each tool is, with your competitors rated Red, Amber or Green, stale tools set aside and a named person to call.
- **Use it when:** Before discovery or a technical call, when you need to know what you'd sit next to or replace. Use this when you want the whole area; use "Is a competitor installed?" instead when you only care about one rival.
- **Best for:** Account Executive, Presales & Solutions, Partnerships & Alliances
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); Technology (e.g. data warehousing); What I sell (e.g. cloud data-platform modernisation services); Competitor (optional) (e.g. Snowflake); View (optional) (e.g. products (default) or vendors)

### Detailed prompt

```text
Act as my presales technology analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Technology: [area in plain words, e.g. data warehousing, cybersecurity]
- What I sell: [one line, e.g. cloud data-platform modernisation services — skip if you ran the start-here prompt]
- Competitor (optional): [vendor or product, e.g. Snowflake — skip if saved in setup]
- View (optional): [products (default) or vendors]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Match my area to Draup's narrowest grouping (sub-category, category or workload) and say which you used. If it returns nothing, try the next broader grouping once.
3. Pull its products, up to 5 pages: maker, sub-category, usage strength (High, Medium, Low), last seen, countries.
4. Split them: Active (a usage strength and seen in the last 12 months) and Stale (the rest).
5. If I named competitors, check the whole stack for their products, whatever area they're filed under (record a product with its maker), and rate each (see rules); count one as present only at High or Medium.
6. If View is vendors, rank makers by Active products: fragmented if no maker holds 25% of them, concentrated if the top 2 hold over 50% (editable defaults).
7. For up to 3 lesser-known Active products, pull what each does and how many companies use it.
8. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table "Active" (top 10, High to Low): Product | Maker | Usage strength | Last seen | Fit (Competes, Complements, Unrelated).
- "My competitors here": product, rating (Red, Amber, Green) and one line of evidence, or "none detected".
- "Why this matters for [What I sell]": 3 bullets: where we'd fit, what we'd replace, one discovery question.
- Detail: vendors view (Rank | Maker | Active products | Main products) with the play (consolidate, replace or attach); "Stale" count plus the 5 most recent; "Products you may not know" with install base; Gaps (what Draup lacked, to ask in discovery).

RULES
- Product counts measure breadth, not spend. Say how many products you reviewed.
- Many products share one last-seen date from a data refresh; lean on usage strength.
- Skip labels that aren't products; flag products credited to the wrong maker.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Rating: High usage in the workloads of What I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 400 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (a named owner and a dated why-now). Then what [Company] runs for [Technology]: active tools by usage strength, my [Competitor] products rated Red, Amber or Green, and stale tools set aside.
```

### Follow-ups

- Which of the active products have the most hiring behind them? Search postings by each product's skill name.
- Show the same view for [another area] so I can see the adjacent stack.
- Switch to the vendors view and tell me which makers are fading.
- Draft a 70-word email to the person in the next step, without naming any tool they haven't named in public.

### Tips

- Usage strength (High, Medium, Low) tells you how central a tool is. A product with no strength listed is one Draup no longer detects.
- If your area returns nothing, describe it differently ("data warehouse" rather than "analytics") and the assistant will try Draup's nearest grouping.
- Put your competitors in "Tell your AI about you" once and every tech prompt rates them for you.

## Is a competitor installed?

- **id:** `tech-competitor-installed`
- **What you get:** Whether a named competitor is really installed (High or Medium usage), where it sits, any overlapping product or one the account owns, the priorities that could trigger a switch, and three bullets on how to win.
- **Use it when:** Before you pitch a replacement, when a deal stalls and you suspect an incumbent, or before you mention a tool in outreach. Use this for one or two named competitors; use "What they run in one tech area" instead for the whole area.
- **Best for:** Account Executive, Presales & Solutions, Marketing & ABM, SDR / BDR
- **Time:** 2–4 min
- **Inputs:** Company (e.g. jpmorganchase.com); Competitor (e.g. Snowflake); Relationship (optional) (e.g. rival to displace (default), adjacent tool, or platform we run on); What I sell (e.g. lakehouse data platform)

### Detailed prompt

```text
Act as my competitive analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. jpmorganchase.com]
- Competitor: [vendor or product, one or two, e.g. Snowflake, Google BigQuery]
- Relationship (optional): [rival to displace (default), adjacent tool we sit beside, or platform we run on]
- What I sell: [one line, e.g. lakehouse data platform — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Resolve each competitor to its maker (keep the product name) and search the whole stack by that maker, whatever area it's filed under, up to 5 pages: usage strength, last seen, workloads. Rate each product (see rules). For a broad maker (e.g. Google), keep products in [What I sell]'s space and count the rest. A row named only after the maker is weaker evidence than a named product; say which row carries the verdict.
3. Check whether [Company] makes or owns a product in the same sub-category. If so, it is more likely to consolidate onto its own tool than switch.
4. Pull the other Active products in the same sub-categories (a second product doing the same job is an overlap) and stated priorities in those workloads, newest first (none: use the function closest to [What I sell]).
5. Count job postings from the last 12 months naming the competitor's product as a skill, by its skill name (e.g. CrowdStrike Falcon, not CrowdStrike); if 0, read 3 recent postings in the workload for the exact spelling and retry once.
6. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]; say here if [Company] owns a rival product.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Verdict: "Installed and active", "Detected at Low only (not counted)", "Installed but fading" or "Not detected in Draup", with the rating and the evidence.
- Table "Competitor footprint": Product | Usage strength | Last seen | Workloads | Rating.
- Table "Switch triggers" (rival) or "Openings" (otherwise), up to 3: Priority | Source and quarter | Likely owner | Why it opens a door.
- "How to win" (rival only): 3 bullets, each tied to a fact above: the wedge (overlap, new estate or subsidiary), who to start with, and the proof to bring.
- Detail: "Who else is in the room" (top 8: Product | Maker | Usage strength | Last seen); hiring evidence (or "none found"); Gaps (what Draup lacked, to ask in discovery).

RULES
- Frame by Relationship. Displace a rival. Never suggest displacing an adjacent tool; look for integration gaps. A platform we run on is a fit signal. Rate rivals only; others get "n/a".
- Active = High or Medium usage, seen in the last 12 months; Low = detected, not counted as present; no usage strength = "fading". "Not detected" is not proof they don't use it.
- Judge a sub-category by the product, not Draup's label (firewalls can sit under SIEM).

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- Rating: High usage in the workloads of What I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). Is [Competitor] installed at [Company] at High or Medium usage? Rate it Red/Amber/Green, flag overlaps or a product [Company] owns, then 3 bullets on how to win.
```

### Follow-ups

- Run "Map the buying committee" on the workloads where [Competitor] sits.
- Find 10 more companies in the same industry whose stack includes [Competitor] products.
- Turn the "How to win" wedge into a 90-word email to the person in the next step.
- Run it again with Relationship set to adjacent tool and compare the openings.

### Tips

- Set Relationship when the tool isn't a true rival. Datadog is adjacent for a data-observability seller, and a platform such as Snowflake is something you need in the stack, not something to replace.
- If the account makes a product in the same category, the verdict says so first: a company that owns its own tool rarely switches to yours.
- Draup sees tools through public evidence such as job ads. A tool that runs quietly in the background may show as Low or not at all.
- Hiring counts use the product's skill name ("CrowdStrike Falcon"), not the maker; a maker-name search can return a false 0.

## What tools they adopted this year

- **id:** `tech-recent-adoptions`
- **What you get:** The tools first detected at the account in the last 12 months, labelled as competing with, complementing or unrelated to what you sell, with any new competitor product flagged Amber first and a named person to call.
- **Use it when:** Looking for a why-now: a new tool usually means a new project, a new owner and fresh budget.
- **Best for:** Account Executive, SDR / BDR, Presales & Solutions
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); What I sell (e.g. supply-chain planning software); Competitor (optional) (e.g. Kinaxis, o9 Solutions)

### Detailed prompt

```text
Act as my technology signals analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- Competitor (optional): [one or more, e.g. Kinaxis, o9 Solutions — skip if saved in setup]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull every product first detected at the company in the last 12 months, up to 5 pages, and review them all before narrowing. Note the earliest and latest first-detected dates.
3. If I named competitors, search the whole stack by each maker; flag any product first detected in this window at High or Medium (Amber) and rate older installs too (see rules); note Low-only detections without counting them.
4. Drop Low-usage products unless they're in my category or made by a competitor.
5. Label each: Competes (does what [What I sell] does), Complements (sits next to it or feeds it) or Unrelated.
6. Look for clusters in Competes and Complements (e.g. several new security tools).
7. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Headline: "N products first detected between [earliest] and [latest]; X compete, Y complement."
- "Competitor alert": product, first-detected month, usage strength, rating, or "none".
- Table (top 10; Competes, then Complements, newest first): First detected | Product | Maker | Usage strength | Relation.
- "Why this matters for [What I sell]": 3 bullets on the likely projects, each naming a product.
- Detail: the remaining rows (up to 25) and counts by category for the rest; Gaps (what Draup lacked, to ask in discovery).

RULES
- Recent first-detected dates are reliable here; only a date that predates the product isn't. It marks Draup's first public evidence, not a contract.
- Additions only; don't infer removals. Say how many products you reviewed and dropped.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore the confidence score and "Generic" rows. Say "fading", never "dropped".
- Check the whole tech stack for products made by [Competitor], whatever area they're filed under; if [Competitor] is a product (e.g. Google BigQuery), record it and its maker.
- Rating: High usage in the workloads of What I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). What did Draup first detect at [Company] in the last 12 months? Flag any new [Competitor] product first, then label the rest Competes, Complements or Unrelated to [What I sell].
```

### Follow-ups

- For the top 3 complementary adoptions, who likely owns them? Find executives in the matching workloads.
- Which older tools in the same categories look like they are fading?
- Write a 3-sentence opener that references the strongest new adoption without saying how we know.
- Check whether the strongest new tool also shows up in their job ads, searching by its skill name.

### Tips

- A cluster of new tools in one area is often a stronger signal than any single product.
- List your main competitors in the input (or in "Tell your AI about you") so the assistant checks their whole product range, not just this year's additions.

## Fading tools and replacement windows

- **id:** `tech-fading-stack`
- **What you get:** The tools that have gone quiet in one area, what seems to be taking their place, and the 3 best-timed replacement windows, each with a dated reason and a named person to call.
- **Use it when:** Hunting for a renewal or migration window, or before a modernisation pitch.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller
- **Time:** 2–4 min
- **Inputs:** Company (e.g. target.com); Technology (e.g. data management); What I sell (e.g. data-platform migration services)

### Detailed prompt

```text
Act as my technology renewal and migration analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Technology: [area or workload, e.g. data management, cybersecurity]
- What I sell: [one line, e.g. data-platform migration services — skip if you ran the start-here prompt]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Pull the products in that area, up to 5 pages, and say which grouping you used.
3. Group each: Fading (no usage strength, or last seen over 12 months ago); Weakening (Low, last seen 6–12 months ago); Active (High or Medium, seen in the last 90 days); Stable (the rest, counted only). Cut-offs are editable defaults.
4. For each Fading or Weakening product, find Active products in the same sub-category: the likely successor or a parallel tool.
5. Pull products first detected in the last 12 months in those sub-categories.
6. Pull stated priorities in the function closest to [What I sell] about modernisation, migration, consolidation or cost, with source and fiscal quarter.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table "Replacement windows" (top 3): Product | Why now (successor, new arrival or priority, dated) | Likely owner | Opening for [What I sell].
- Table "Fading and weakening" (top 10, oldest first): Product | Maker | Last seen | Group | Read (Replaced, Parallel, Unclear).
- Detail: likely successors with usage strength; new arrivals; Stable count; Gaps (what Draup lacked, to ask in discovery).

RULES
- "Fading" is the strongest claim allowed. Never say they dropped, retired or cancelled a product.
- A last-seen date shared by many products is a data refresh; with Low strength it's weak evidence.
- If nothing is fading, say the area looks stable and lead the next step with a priority instead.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- Pull company lists and priorities 10 at a time; show the top results first and offer to continue.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). Which [Technology] tools at [Company] have gone quiet in Draup, what likely replaced each, and which 3 replacement windows suit [What I sell], each with a dated reason?
```

### Follow-ups

- For the top replacement window, run "Map the buying committee" on that workload.
- Show the full active stack in the same sub-categories, so I know what I'd integrate with.
- Draft a 90-word email to the person in the next step that opens on the migration window without naming the old vendor.
- Check whether the likely successor also appears in their job ads.

### Tips

- Last-seen dates matter more than first-seen dates. A tool with no usage strength listed is one Draup no longer detects.
- Treat "fading" as a hypothesis to test in discovery, not a fact to put in an email.

## Size a vendor's install base

- **id:** `tech-vendor-install-base`
- **What you get:** What a vendor sells and how many companies use each product, so you can size an attach, co-sell or competitive-replacement motion, with a named person at the vendor or a first target to approach.
- **Use it when:** Planning a partner motion, sizing a competitor's footprint, or picking which product to build a campaign around.
- **Best for:** Partnerships & Alliances, Marketing & ABM, Presales & Solutions
- **Time:** 1–2 min
- **Inputs:** Vendor (e.g. servicenow.com); What I sell (e.g. ITSM implementation and managed services); Motion (optional) (e.g. attach or co-sell (default), or replace)

### Detailed prompt

```text
Act as my partner and market-sizing analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Vendor: [website of the vendor to size, partner or competitor, e.g. servicenow.com]
- What I sell: [one line, e.g. ITSM implementation and managed services — skip if you ran the start-here prompt]
- Motion (optional): [attach or co-sell (default), or replace]

STEPS
1. Find [Vendor] by its website (exact match; if none, retry once by name and show the match and its score) and confirm it is the parent, not a reseller or regional unit. If several match, ask me.
2. Pull the products it builds and how many companies Draup detects using each. Rank by companies, largest first.
3. For the top 3, pull the category and what each does.
4. Mark which products [What I sell] attaches to, competes with, or doesn't touch.
5. For the next step: for attach or co-sell, pull the top 3 executives at [Vendor] who run partners, alliances or channels (full profile titles); for replace, name the lead product's best first target list instead. Also pull the most important news item from the last 90 days where [Vendor] is the actor (e.g. a launch or acquisition).

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10): Rank | Product | Category | Companies using it | Relation to [What I sell] (Attach, Compete, None).
- "Where the base is concentrated": 2–3 bullets on which products carry the footprint and which are niche.
- "Why this matters for [What I sell]": the 2 products to lead on and why.
- Detail: the rest of the list (Draup returns up to 20 products per vendor); Gaps (what Draup lacked, to ask in discovery).

RULES
- Counts are companies where Draup sees public evidence of use, not licences, seats or revenue.
- Don't add the counts together to get unique customers; one company often uses several products.
- Draup leaves out "Generic" rows. Say if the list looks capped at 20.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Label anything you infer as "likely".
- If sources conflict on a name, date or number, say so and don't repeat either as fact. Treat single-source figures as unverified.
- People: full profile title; check it fits partners, alliances or channels; flag subsidiary or regional staff. Professional information only (name, title, employer, Draup's profile link); no personal contact details.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 350 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (a named person, a dated why-now). What does [Vendor] build, and how many companies use each product? Top 10 by install base, each marked attach, compete or none for [What I sell].
```

### Follow-ups

- List companies in [Vertical] headquartered in my territory whose stack includes [top product] at High or Medium usage, sorted by revenue.
- Which of my target accounts also run [top product]?
- Draft a one-paragraph co-sell pitch to the partner leader in the next step.
- Show the same view for [a second vendor] so I can compare footprints.

### Tips

- Install-base counts are best for comparing products within one vendor, not for quoting as market share.
- Pair this with "Target list: companies running a competitor" to turn the biggest product into a named list.

## Who's already working each priority

- **id:** `tech-priority-stack-incumbent-map`
- **What you get:** For each stated priority in one function: the tools and service providers already linked to it, rated where they're your competitors, and whether to displace, co-sell or go greenfield, judged for a software or a services seller.
- **Use it when:** Use this when you want, priority by priority, which tools and providers are already in place and where to displace, co-sell or go first. Use "Which providers to partner with or replace" instead when you're choosing between named partners, and "Pick the SI to co-sell with" when you need one integrator for a deal.
- **Best for:** Account Executive, Presales & Solutions, Services, SI & Staffing Seller, Partnerships & Alliances
- **Time:** 4–6 min
- **Inputs:** Company (e.g. target.com); Business function (e.g. Supply Chain); What I sell (e.g. supply-chain planning software); I sell (e.g. software (or services)); Competitor (optional) (e.g. Kinaxis, o9 Solutions)

### Detailed prompt

```text
Act as my account strategy analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Company: [website, e.g. target.com]
- Business function: [e.g. Supply Chain, IT]
- What I sell: [one line, e.g. supply-chain planning software — skip if you ran the start-here prompt]
- I sell: [software or services — skip if you ran the start-here prompt]
- Competitor (optional): [vendors or services firms, e.g. Kinaxis, o9 Solutions]

STEPS
1. Find [Company] by its website (exact match; if none, retry once by name; show the match and score) and confirm it is the parent, not a subsidiary, brand or sister company. If several match or it looks wrong, ask me. Use Draup's exact name from then on.
2. Map [Business function] to its main workloads and name them. Pull stated priorities in the function, newest first; keep up to 8. If none, try the closest function and say so.
3. For each priority: workloads, source and quarter, up to 6 linked tools, up to 6 linked providers.
4. Pull the stack once, filtered to the makers of [Competitor] and the linked tools (look up very broad makers such as Microsoft separately). Keep tools with a usage strength seen in 12 months; rate competitor products (see rules).
5. Count each provider's active engagements in the function's workloads (one lookup filtered to those workloads); add the provider's account-wide total only if it came back. Leave staffing, BPO, agency and market-research firms out of the plays.
6. Tag each priority. Software seller: Displace = a competitor product at High or Medium in its workloads; Co-sell = an IT services firm works it. Services seller: Displace = a rival services firm holds 10%+ of its engagements; Co-sell = a linked software product needs services. Either: Greenfield = nothing relevant; else Not ours.
7. For the next step, pull the top 3 executives in the function closest to [What I sell] and the top news item from the last 90 days where [Company] is the actor.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell].
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (newest first, up to 8): Priority (quarter) | Incumbent tools (rating) | Providers (in function) | Play | Likely owner.
- "Top 3 plays": priority, incumbent or partner, opening.
- Detail: linked tools with usage strength and last seen; provider engagement counts in the function (and account-wide if returned); Gaps (what Draup lacked, to ask in discovery).

RULES
- Provider counts are "active engagements (Draup-derived)", not contracts; rank providers by them yourself and rate rivals by share.
- If the same integrators appear on every priority, call it weak evidence, not Co-sell everywhere.
- Tools and providers are linked by workload, not confirmed; say "linked", never "used for".

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Rating: High usage in the workloads of What I sell = Red, Medium = Amber, Low or undetected = Green (not counted as present; say so). New in 12 months at High or Medium adds a separate Amber. Services rival, by share of the account's active engagements in those workloads: 30%+ Red, 10–29% Amber, under 10% Green.
- If [Company] sells technology or services, drop priorities, news and hiring about what it sells before choosing an angle; never pitch it its own product category.
- Quarter and year labels follow the company's fiscal calendar and can run ahead of the calendar year; say so when they do.
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit [Company], and keep it out of drafted copy. No Chief, EVP, CIO or "Head of" in the top 3? Pull the next page of 10 once (no title search).
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 450 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named owner, dated why-now). Map [Company]'s [Business function] priorities to the tools and providers linked to each, rate my [Competitor] products, and tag each priority Displace, Co-sell, Greenfield or Not ours.
```

### Follow-ups

- For the top Displace priority, how deep is [Competitor]? Show every product with usage strength and last seen.
- Who owns each of the top 3 priorities? List executives in the matching workloads.
- Turn the top play into a one-page point of view for the person in the next step.
- Compare the top two providers head to head in [Business function].

### Tips

- A priority with no linked tools or providers is often greenfield: an easier place to be first.
- Set "I sell" correctly. A services firm on a priority is a partner for a software seller but the incumbent for a services seller.
- Provider counts are filtered to your function, so a big agency that works marketing won't look like your supply-chain incumbent.

## Target list: companies running a competitor

- **id:** `tech-displacement-list`
- **What you get:** A true count and a ranked list of parent companies in your industry and territory whose stack includes a competitor's products, with usage checked for the top 10 (only High or Medium counted), distributors and inactive names flagged, and a named person at the top account.
- **Use it when:** Launching a competitive-replacement campaign or building an SDR list.
- **Best for:** SDR / BDR, Marketing & ABM, Sales Leader & RevOps, Account Executive
- **Time:** 4–6 min
- **Inputs:** Competitor (e.g. Snowflake); Vertical (e.g. Retail); Territory (optional) (e.g. United States of America — defaults to your territory from setup); Minimum employees (e.g. 5,000); What I sell (e.g. lakehouse data platform)

### Detailed prompt

```text
Act as my competitive list-building analyst. Use Draup for Sales for every fact. Don't use outside knowledge unless I ask, and label it if you do.

INPUTS (edit these)
- Competitor: [vendor or product, e.g. Snowflake]
- Vertical: [industry, e.g. Retail, Life Sciences]
- Territory (optional): [HQ country or region in full, e.g. United States of America; default: my territory from setup]
- Minimum employees: [e.g. 5,000]
- What I sell: [one line, e.g. lakehouse data platform — skip if you ran the start-here prompt]

STEPS
1. Turn my industry and territory into Draup's exact names; say which you used. If the industry returns zeros, try its parent industry and name it.
2. List only companies whose tech stack includes [Competitor] products: primary industry [Vertical], HQ in [Territory], at least [Minimum employees] staff, largest workforce first (sort by total workforce). For a product, filter by its maker and keep rows showing it. Parent companies only: merge subsidiaries and the same company under different names.
3. Count by paging this exact list, 10 per page, until a page returns fewer than 10. The total must apply every filter. Label it "detected at any usage": the list shows presence, not usage.
4. For the top 10, check usage with one stack lookup each, filtered to the maker. Count a company as running [Competitor] only at High or Medium; list Low-only rows as "detected, not counted".
5. Separately, run the list once without the size limit, companies with no workforce figure first (10 rows), and report how many lack size data (or "10+"). Never mix this into the total.
6. Flag distributors, wholesalers and resellers, possibly inactive companies and rows clearly outside the industry, and offer to exclude them.
7. For the top-ranked company at High or Medium, pull the top 3 executives in the function closest to [What I sell] and its most important news item from the last 90 days.

OUTPUT
- Bottom line: 2 sentences — the answer and what it means for [What I sell]. Include the true count and how many of the top 10 run it at High or Medium.
- Recommended next step: who (name and full title), what (call, email, intro or meeting) and why now (one dated fact). If Draup has neither, say so and name the title to look for.
- Table (top 10): Rank | Company | Workforce | [Competitor] products (usage strength) | Flag.
- Detail: revenue (USD M, fiscal year) and Opportunity Index for the same rows; the next 5; "Detected at Low only"; "Flagged" (Company | Reason); "Missing size data": count; Gaps (what Draup lacked, to ask in discovery).

RULES
- Opportunity Index is Draup's own rating of how strong the sales opportunity is (higher is stronger); use it to order, not to quote.
- Don't rank on IT spend; for many companies it is modelled from revenue.
- Low usage everywhere means the competitor is present but not central; say so in the bottom line and don't count those rows.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me first.
- Date every fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory. If a name returns nothing, retry once with Draup's spelling and say which worked.
- Rank within [Territory] only. Use primary industry only. Flag "possibly inactive" (zero postings in 90 days, or no revenue and no workforce).
- Counts must apply every filter. The quick count ignores technology conditions, so count by paging; stop after 5 pages and report the total so far with a plus.
- Show USD millions using Draup's conversion rate. If Draup gives no rate, name the rate and date and mark it as outside Draup.
- Trust last-seen date and usage strength. Ignore first-seen dates, the confidence score and "Generic" rows. Say "fading", never "dropped".
- People: full profile title; check it fits the function; flag subsidiary or branch staff; mark a C-level profile "verify" if its tenure or past employers don't fit the company, and keep it out of drafted copy.
- Phone-first: bottom line and next step first; at most 2 tables up front (5 columns, 10 rows max); the rest under "Detail". Keep to about 380 words including tables, then offer to continue.
```

### Quick version

```text
Bottom line and next step first (named person, dated why-now). How many [Vertical] parent companies in [Territory] with [Minimum employees]+ staff run [Competitor]? Top 10 with usage strength; count only High or Medium; flag distributors.
```

### Follow-ups

- Show the next 10 in the same way, distributors excluded, with usage checked.
- For the top 5, what stated priorities could justify a switch?
- Write a 2-sentence opener for each of the top 5, each tied to one dated fact.
- Re-rank the list by Opportunity Index to find reachable mid-size accounts.

### Tips

- The total is counted with every filter applied and labelled "detected at any usage"; the top 10 are then checked for High or Medium usage. If the list looks small, lower the minimum size or widen the territory.
- Leave Territory blank to use the one saved in "Tell your AI about you"; without a territory the list ranks the whole world.
- Retail and consumer lists often include distributors and wholesalers; the flag column lets you drop them before the list goes to SDRs.
