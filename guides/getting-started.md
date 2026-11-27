# Getting started

This takes about five minutes. You need a Claude account and a Draup account with Draup for Sales access.

## 1. Connect Draup for Sales in Claude

1. Open Claude (claude.ai or the desktop app) and go to **Settings → Connectors**.
2. Click **Browse connectors** and search for **Draup for Sales** (it is listed in Claude's connector directory).
3. Click **Connect** and sign in with your Draup account.
4. In a new chat, open the tools menu and check that **Draup for Sales** is switched on.

> **On a Claude Team or Enterprise plan?** Your workspace admin may need to enable the connector first. If you can't find it, ask your admin or your Draup account team.

The connector is **read-only**: Claude can look things up in Draup but cannot change anything. You see the data your Draup subscription includes.

> Some prompts in the *Talent cost and location* section also use the **Draup for Talent** connector. Connect it the same way if your plan includes it.

## 2. Tell Claude about you, once

Open [Start here: about me](../prompts/00-start-here/about-me.md), fill in your role, what you sell, your territory, competitors and customers, and paste it as the first message of a chat. Claude confirms a short summary and uses it for every later prompt in that chat, so you rarely need to fill in *What I sell*.

**Make it permanent with a Claude Project.** Create a Project (for example "Draup research"), open its instructions, and paste [Claude Project instructions](../prompts/00-start-here/claude-project.md). Every chat in that Project then starts with your context and the library's data rules.

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
| Claude answers without using Draup | Check the connector is switched on in the chat's tools menu, then say "use Draup for this". |
| "Authentication failed" or a 401 error | Reconnect the connector in Settings → Connectors. |
| Wrong company | Give the website, or say "use the parent company, not [subsidiary]". |
| Empty result for an industry or country | Try Draup's naming ("Life Sciences", not "Pharma"; "United States of America"). |
| Answer cut short | Ask for fewer items (top 10) or a narrower function, or split the request. |
| An executive list is empty for Europe | Some regional profile data may be restricted. Ask Claude to search globally and filter. |
