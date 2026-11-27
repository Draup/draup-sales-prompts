# Use the whole library as a skill

Instead of copying prompts one by one, you can give your AI the entire library. Then just ask in plain words: "prep me for my call with Kroger" or "who should I contact at Pfizer about cloud migration?". Your assistant picks the right prompt, fills it in and follows it.

You still need Draup for Sales connected for the live data. See [Connect Draup to your AI](connect.md).

| You use | Best option | Time |
|---|---|---|
| **Claude** (claude.ai, desktop) | [Upload the skill](#claude-upload-the-skill) | 2 min |
| **Claude Code** | [Install the plugin](#claude-code-install-the-plugin) (also connects Draup) | 1 min |
| **Claude Projects** | [Add the library to a Project](#claude-projects) | 3 min |
| **ChatGPT** | [Add the library to a Project or custom GPT](#chatgpt-project-or-custom-gpt) | 3 min |
| **Microsoft 365 Copilot or Teams** | [Use the Draup for Sales agent](#microsoft-365-copilot-and-teams) | 2 min |
| **Any other AI** (Gemini, Copilot Studio, your own agent) | [Give it the link or the file](#any-other-ai) | 2 min |

**Downloads:**
- [Skill for Claude (zip)](../dist/draup-sales-prompts-skill.zip)
- [Every prompt in one file](../dist/draup-sales-prompts-all.md), for ChatGPT, Gemini and other AIs

---

## Claude: upload the skill

1. Download [draup-sales-prompts-skill.zip](../dist/draup-sales-prompts-skill.zip). Don't unzip it.
2. In Claude, open **Customize → Skills**, click **+**, choose **Create skill → Upload a skill**, and select the zip.
3. Make sure the skill is switched on, and that **Draup for Sales** is connected under Connectors.
4. Try it: *"Use the Draup sales prompts: give me a 10-minute pre-call snapshot on kroger.com."*

> **Team and Enterprise plans.** On Enterprise, an owner may need to turn on **Skills** and **Code execution and file creation** under *Organization settings → Plugins & skills* first. Once uploaded, you can share the skill with colleagues or publish it to your organisation from the Skills page.

## Claude Code: install the plugin

The plugin installs the skill **and** adds the Draup for Sales connector. Run these inside Claude Code:

```text
/plugin marketplace add Draup/draup-sales-prompts
```

```text
/plugin install draup-sales@draup-sales-prompts
```

Then type `/mcp`, choose **draup-sales** and sign in with your Draup account.

**Prefer the terminal?** Run `claude plugin marketplace add Draup/draup-sales-prompts`, then `claude plugin install draup-sales@draup-sales-prompts`.

**Just the skill, no plugin?** Copy the [`skill/draup-sales-prompts`](../skill/draup-sales-prompts) folder into `~/.claude/skills/`.

## Claude Projects

1. Create a Project, for example "Draup sales research".
2. In the Project's knowledge, click **+ → GitHub**, paste `https://github.com/Draup/draup-sales-prompts` and choose the **`skill/draup-sales-prompts`** folder.
   - You may need to connect GitHub first, under *Customize → Connectors*.
   - Choosing that one folder keeps the Project small.
   - If you prefer, upload [the one-file version](../dist/draup-sales-prompts-all.md) instead.
3. Paste the [Claude Project instructions](../prompts/00-start-here/claude-project.md) into the Project's instructions and fill in the ABOUT ME part.
4. Make sure Draup for Sales is switched on in chats inside the Project.

## ChatGPT: Project or custom GPT

1. Make sure the [Draup for Sales plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7) is added to your ChatGPT.
2. Create a **Project** (or a custom GPT) and upload [draup-sales-prompts-all.md](../dist/draup-sales-prompts-all.md) as a file.
3. Paste this into the Project's (or GPT's) instructions:

```text
You are my sales research assistant. For any sales request, find the best-matching prompt in the attached "Draup Sales Prompt Library" file (see its Prompt index), fill in its inputs from my message (ask me for anything missing), and follow that prompt's STEPS, OUTPUT and RULES exactly, using the Draup for Sales plugin for every fact. Date every fact, write "Not in Draup" instead of guessing, and end with the prompt's recommended next step.
```

4. Start a chat in the Project and turn on Draup for Sales from the tools menu.

> The prompts were tested in Claude. They use plain language and are designed to work in ChatGPT too.

## Microsoft 365 Copilot and Teams

Draup also offers **Draup for Sales** as an agent for Microsoft 365 Copilot, Teams and Outlook: [Microsoft Marketplace listing](https://marketplace.microsoft.com/en-us/product/WA200010751).

1. Ask your Microsoft 365 admin to approve the **Draup for Sales** app from the Microsoft Marketplace, or click **Get it now** on the listing if you have permission.
2. Open Microsoft 365 Copilot or Teams and select the **Draup for Sales** agent.
3. Paste any prompt from this library into the agent's chat, or simply ask in your own words.

> The Copilot and Teams agent is a separate Draup app. The prompts in this library were written and tested in Claude. In Copilot, start with the quick versions and use the detailed versions where you need the full output format.

## Any other AI

**Give it the link.** If your assistant can browse the web, paste this:

```text
Use the Draup Sales Prompt Library at https://draup.github.io/draup-sales-prompts/llms.txt. For my request, pick the matching prompt, fill in its inputs, and follow its steps, output format and rules exactly, using Draup for Sales data.
```

**Or give it the file.** Upload [draup-sales-prompts-all.md](../dist/draup-sales-prompts-all.md) as knowledge (a Gemini Gem, a Copilot Studio agent, or your own agent's retrieval store) and use the instructions from the ChatGPT section above.

**Building your own agent?** Connect it to Draup for Sales over MCP ([connection guide](connect.md#option-3-any-mcp-client-custom-connector)) and load the [`skill/draup-sales-prompts`](../skill/draup-sales-prompts) folder as its instructions.

---

## Which should I use: skill or single prompts?

- **Skill:** best for everyday use. Ask naturally and let your assistant pick the prompt.
- **Single prompts** (copied from the [library](https://draup.github.io/draup-sales-prompts/)): best when you want full control over the inputs, or you're sharing one prompt with a colleague.

Both use the same tested prompts.

Questions? See [Connect Draup to your AI](connect.md#troubleshooting) or email **support@draup.com**.

[Back to the library](../README.md)
