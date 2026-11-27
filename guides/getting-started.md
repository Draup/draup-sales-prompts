# Getting started

This takes about five minutes. You need Claude or ChatGPT, and a Draup account with Draup for Sales access.

## 1. Connect Draup to Claude or ChatGPT

| You use | Do this |
|---|---|
| **Claude** | [Add Draup for Sales from Claude's directory](https://claude.ai/directory/draup-for-sales), click **Connect** and sign in with your Draup account. |
| **ChatGPT** | [Add the Draup for Sales plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7) and sign in with your Draup account. |
| **Microsoft 365 Copilot or Teams** | [Get the Draup for Sales agent](https://marketplace.microsoft.com/en-us/product/WA200010751) from the Microsoft Marketplace (your admin may need to approve it). |
| **Another MCP client** | Add Draup as a custom connector: see [Connect Draup to your AI](connect.md#option-3-any-mcp-client-custom-connector). |

**Tip:** to let your AI pick the right prompt for you, add the whole library as a skill. See [Use the library as a skill](use-as-a-skill.md).

Full step-by-step instructions, admin notes and troubleshooting: **[Connect Draup to your AI](connect.md)**.

## 2. Tell your assistant about you, once

Open [Tell your AI about you](../prompts/00-start-here/about-me.md). Fill in your role, what you sell, your territory, competitors and customers, and paste it as the first message of a chat. Your assistant confirms a short summary and uses it for every later prompt in that chat, so you rarely need to fill in *What I sell*.

**Make it permanent.** In Claude, create a Project (for example "Draup research"), open its instructions, and paste [Claude Project instructions](../prompts/00-start-here/claude-project.md). Every chat in that Project then starts with your context and the library's data rules. In ChatGPT, you can do the same with a ChatGPT Project's instructions.

## 3. Run your first prompt

Good first choices:

- [One-page account brief](../prompts/01-account-research/account-brief.md): pick an account you're working on.
- [Map the buying committee](../prompts/02-buyers-and-stakeholders/buying-committee.md): who to talk to there.
- [What's actionable this quarter](../prompts/04-signals-and-timing/whats-actionable.md): why reach out now.

Each prompt page has:

| Part | What it's for |
|---|---|
| **Fill in** | The placeholders, with examples |
| **Detailed prompt** | The full version. Use it for anything you'll share or act on |
| **Quick version** | A short version for fast lookups |
| **Follow-ups** | Paste into the same chat to go deeper |
| **Tips** | How to get better results and read the data |

On GitHub, hover over a prompt box and click the copy icon in its top-right corner.

## 4. Get better answers

- **Use the website** (`siemens.com`) rather than the company name. If Claude finds a subsidiary or a similarly named company, tell it which one you mean.
- **Narrow it down.** Name a business function (IT, Supply Chain, Finance & Accounting…) or a workload (Cloud, AI & Data Science…). Big companies have thousands of records.
- **Use Draup's names** for industries and countries: "Banking & Financial Services", "Life Sciences", "United States of America". The prompts ask Claude to try alternatives when a name finds nothing.
- **Stay in one chat** for a whole account or workflow so Claude reuses what it has found.
- **Save your solution offering in your Draup profile.** Draup then tailors its opportunity suggestions to what you sell.

## Troubleshooting

| What you see | What to do |
|---|---|
| The assistant answers without using Draup | Check Draup for Sales is switched on in the chat's tools menu, then say "use Draup for Sales for this". |
| "Authentication failed" or a 401 error | Reconnect the connector in Settings → Connectors. |
| Wrong company | Give the website, or say "use the parent company, not [subsidiary]". |
| Empty result for an industry or country | Try Draup's naming ("Life Sciences", not "Pharma"; "United States of America"). |
| Answer cut short | Ask for fewer items (top 10) or a narrower function, or split the request. |
| An executive list is empty for Europe | Some regional profile data may be restricted. Ask Claude to search globally and filter. |
