# "How does Draup know this?"

**A plain-English, shareable answer on how Draup builds a number (IT spend, outsourcing size, talent flow and so on), with the help-centre link.**

| Use it when | Best for | Seller type | Time | Draup data |
|---|---|---|---|---|
| A prospect or your own exec asks where a Draup number comes from and how much to trust it. | Presales & Solutions, Account Executive, Account & Customer Success Manager, Marketing & ABM | Everyone | 1–2 min |  |

> **Tip:** run [Tell Claude about you](../../prompts/00-start-here/about-me.md) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.

## 1. Fill in

| Placeholder | Example |
|---|---|
| `[Metric or question]` | How does Draup estimate a company's IT spend? |
| `[Audience]` | a CFO at a prospect |

## 2. Copy the detailed prompt

Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.

```text
Act as my presales engineer. Answer only from Draup's own help-centre content, through the Draup for Sales connector. Don't use outside knowledge or guess at methodology, and label anything that isn't from the help centre.

INPUTS (edit these)
- Metric or question: [what you were asked, e.g. How does Draup estimate a company's IT spend?]
- Audience: [who will read it, e.g. a CFO at a prospect]

STEPS
1. Ask Draup's help centre the question as written. If it is vague (e.g. "Is the data accurate?"), break it into the specific metric being questioned and ask about that.
2. If the first answer doesn't cover how the number is built, ask once more with a narrower question (e.g. "Where does Draup's IT spend data come from?" or "How often is it refreshed?").
3. Keep the help-centre article titles and links that come back.

OUTPUT
- Bottom line: 2 sentences — what the number is (reported figure or Draup estimate) and how to present it to [Audience].
- "How it's built": 3–4 plain sentences on where the data comes from, how the number is built and how often it's refreshed (if the help centre says).
- "How to present it": one sentence, e.g. "a modelled estimate for sizing, not an audited figure".
- "Source": help-centre article title(s) and link(s).
- Recommended next step: who to send it to and how (e.g. reply to the CFO's email with the link), and the follow-up question to expect.
- Gaps: what the help centre didn't cover — worth raising with Draup support.

RULES
- Use only what the help centre returned. If it has no relevant article, write "The Draup help centre doesn't cover this" and suggest asking Draup support.
- Write for [Audience]: no internal jargon or field names.
- Don't overstate precision. If the help centre says modelled or estimated, keep that word.

STANDARD RULES (leave as is)
- If an input still shows its bracketed example, use my saved context or ask me before starting.
- Date every number and fact. If Draup has no data, write "Not in Draup"; never fill gaps from memory.
- Keep to about 150 words plus the links. Answer one metric at a time, then offer the next.
```

## In a hurry? Quick version

```text
In 4–5 plain sentences, explain how Draup works out [Metric or question] for [Audience], using only the Draup help centre, with the article link and one line on how to present the number.
```

## 3. Keep going: follow-up prompts

Paste these into the same chat after the first answer.

```text
Turn this into a two-line footnote I can put under a slide.
```

```text
Now answer the follow-up they're likely to ask: how current is this data?
```

```text
Explain the same thing for an outsourcing-size number instead.
```

## Tips for better results

- Ask about one metric at a time. "How is IT spend estimated?" usually gets a far better answer than "How accurate is Draup?".
- Send the link with the answer, so the buyer can read the method in Draup's own words.

## Related prompts

- [One-page account brief](../../prompts/01-account-research/account-brief.md): A one-page brief on size, money, priorities, recent deals and any competitor in the stack, ending with who to call and why now.
- [Is their budget growing or shrinking?](../../prompts/01-account-research/budget-posture.md): A verdict on whether the account's budget is growing, holding or shrinking, the IT spend split, and the deal size and pitch that fit.

<details>
<summary>Under the hood: Draup tools this prompt typically uses</summary>

`get_knowledge_base_data`

Status: **tested live**. Prompt id: `content-how-draup-knows`.

</details>

[Back to Content and enablement](README.md) · [All prompts](../../README.md#find-prompts-by-sales-job)
