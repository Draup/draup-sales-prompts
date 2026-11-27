[Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)

# Explain where a Draup number comes from

> **A plain-English, shareable answer on how Draup builds a number (IT spend, outsourcing activity, talent flow and so on) and how far to trust it, written for the person who asked, with the help-centre link.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A prospect or your own exec asks where a Draup number comes from and how much to trust it, or before you put a Draup figure on a slide. | Presales & Solutions, Account Executive, Account & Customer Success Manager, Marketing & ABM | Everyone | 1–2 min |  |

**Before you start:** [connect Draup for Sales](../../guides/connect.md) in Claude or ChatGPT, and run [Tell your AI about you](../../prompts/00-start-here/about-me.md) once in the chat so *What I sell*, territory and competitors fill in automatically.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Metric or question]` | How does Draup estimate a company's IT spend? |
| `[Audience]` | a CFO at a prospect |

## 2. Copy the detailed prompt

Copy it with the button in the box's top-right corner, replace the `[bracketed]` parts, and paste into Claude or ChatGPT with Draup for Sales switched on.

```text
Act as my presales engineer. Answer only from Draup's own help-centre content, through the Draup for Sales connector. Don't use outside knowledge or guess at methodology, and label anything that isn't from the help centre.

INPUTS (edit these)
- Metric or question: [what you were asked, e.g. How does Draup estimate a company's IT spend?]
- Audience: [who will read it, e.g. a CFO at a prospect]

CONTEXT (optional)
Trust in a number grows when you say plainly what it is: a reported figure, a modelled estimate, or a count built from public signals such as job postings and news. Overstating precision loses a CFO faster than admitting a range. Known traps worth checking: IT spend is modelled from revenue for many companies; industry totals are global; leadership data can lag about 3 months, while news and hiring are near real-time.

STEPS
1. Ask Draup's help centre the question as written. If it's vague (e.g. "Is the data accurate?"), break it into the specific metric being questioned and ask about that.
2. If the first answer doesn't cover how the number is built, ask once more with a narrower question (e.g. "Where does Draup's IT spend data come from?" or "How often is it refreshed?").
3. Keep the help-centre article titles and links that come back.
4. Decide which kind of number it is: reported, modelled estimate, or signal-based count. If the help centre doesn't say, write "not stated".

OUTPUT
- Bottom line: 2 sentences — what the number is (reported figure or Draup estimate) and how to present it to [Audience].
- Recommended next step: who to send it to and how (e.g. reply to the CFO's email with the link), and the follow-up question to expect.
- "How it's built": 3–4 plain sentences on where the data comes from, how the number is built and how often it's refreshed (if the help centre says).
- "How to present it": one sentence, e.g. "a modelled estimate for sizing, not an audited figure".
- "Source": help-centre article title(s) and link(s).
- Gaps: what the help centre didn't cover — worth raising with Draup support.

RULES
- Use only what the help centre returned. If it has no relevant article, write "The Draup help centre doesn't cover this" and suggest asking Draup support.
- Write for [Audience]: no internal jargon or field names.
- Don't overstate precision. If the help centre says modelled or estimated, keep that word.
- One metric at a time; offer the next.

STANDARD RULES (leave as is)
- If an input still shows its example, use my saved context or ask me first.
- Date every fact. If the help centre has nothing, say so; never fill gaps from memory.
- Phone-first: open with Bottom line and Recommended next step. Keep to about 200 words plus the links.
```

<details>
<summary><b>In a hurry? Quick version</b></summary>

```text
Bottom line first: in 4–5 plain sentences, explain how Draup works out [Metric or question] for [Audience], whether it's reported or estimated, using only Draup's help centre, with the article link and one line on how to present it.
```

</details>

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this into a two-line footnote I can put under a slide.
```

```text
Now answer the follow-up they're likely to ask: how current is this data?
```

```text
Explain the same thing for an outsourcing-activity number instead.
```

```text
Write a 'Before you trust a number' box for my team covering IT spend, industry totals and leadership data.
```

## Tips for better results

- Ask about one metric at a time. "How is IT spend estimated?" usually gets a far better answer than "How accurate is Draup?".
- Send the link with the answer, so the buyer can read the method in Draup's own words.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): Bottom line and a named person to call with a dated why-now, then the priorities in your function, the people who likely own them, any competitor in the stack and the key numbers.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the deal size and pitch that fit, and who to take it to.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_knowledge_base_data`

Status: **tested live**. Prompt id: `content-how-draup-knows`.

</details>

---

[Back to Content and enablement](README.md) · [Home](../../README.md) · [Connect Draup](../../guides/connect.md) · [Use as a skill](../../guides/use-as-a-skill.md) · [All prompts](../../README.md#find-prompts-by-sales-job) · [Playbooks](../../playbooks/README.md) · [Glossary](../../guides/glossary.md)
