# Contributing

Thanks for helping make the library better. You don't need to be technical to contribute: a well-described idea in an issue is useful on its own.

## Ways to help

- **Suggest a prompt.** Open an issue with the *New prompt* template: the sales job, who it's for, and an example of a great answer.
- **Report a weak result.** Open an issue with the *Prompt feedback* template: which prompt, what you asked, what came back, and what you expected. Don't include confidential customer data.
- **Improve a prompt yourself.** Edit `data/prompts.json` and open a pull request (below).

## How prompts are written

Every prompt follows the same anatomy so business users always know what to expect:

| Field | What it is |
|---|---|
| `id` | `<category>-<short-name>`, stable once published |
| `title` | Short and plain, ideally 6 words or fewer |
| `outcome` | One sentence: what the user walks away with |
| `when` | One sentence: the moment to use it |
| `roles`, `data`, `time` | Who it's for, which Draup data it uses, rough run time |
| `inputs` | The placeholders, each with an example |
| `prompt` | The detailed version, with **INPUTS / STEPS / OUTPUT / RULES / STANDARD RULES** sections. OUTPUT opens with a *Bottom line* and closes with *Recommended next step* and *Gaps*. |
| `quick` | A version of 40 words or fewer |
| `followups` | 2–4 prompts to continue in the same chat |
| `tips` | 1–3 plain-language tips |
| `tools` | The Draup tools it typically uses (shown only in the "under the hood" section) |
| `status` | `tested` once you have run it against live Draup data on at least two public companies. Draup for Talent prompts that haven't been run live use `schema-only` and show as Preview. New Draup for Sales prompts are merged once tested. |
| `seller` | `software`, `services` or `both` |
| `motion` | Any of `new-logo`, `expand`, `renew`, `displace`, `partner` |

Writing rules:
- Business language only in the prompt text. No tool names or technical terms.
- Square-bracket placeholders with an inline example: `[Company website or name, e.g. siemens.com]`.
- Spell out the output: table columns, top N, sort order, date window, units.
- Include the guardrails: date every number, write "Not in Draup" instead of guessing, and narrow big queries.
- Test on at least two public companies before marking a prompt `tested`.

## Making a change

```bash
git clone https://github.com/Draup/draup-sales-prompts
cd draup-sales-prompts
# edit data/prompts.json (or data/playbooks.json)
python3 scripts/build.py        # validates and regenerates every page
git checkout -b improve-<prompt-id>
git add -A
git commit -m "Improve <prompt-id>: <what changed>"
```

Then open a pull request describing what you changed and how you tested it. Don't edit generated files by hand: `README.md`, `guides/data-guide.md`, everything under `prompts/`, `roles/`, `playbooks/` and `docs/`, and `data/prompts.csv` are rebuilt from the JSON and `templates/`. PDFs are rebuilt by maintainers with `scripts/build_pdfs.sh`.

By contributing you agree your contribution is licensed under CC BY 4.0 (prompts and docs) or MIT (code in `scripts/`, `templates/` and the website).
