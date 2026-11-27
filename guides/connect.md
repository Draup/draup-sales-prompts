# Connect Draup to your AI

The prompts in this library need **Draup for Sales** switched on in your AI assistant. Pick the option that matches the tool you use. Each takes about two minutes.

| You use | Do this | Link |
|---|---|---|
| **Claude** (claude.ai, desktop or mobile) | Add the Draup for Sales connector from Claude's directory | [Open in Claude](https://claude.ai/directory/draup-for-sales) |
| **ChatGPT** | Add the Draup for Sales plugin | [Open in ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7) |
| **Another MCP client** (Claude Code, Cursor, VS Code, Windsurf, Copilot Studio, your own agent) | Add Draup as a custom MCP connector | [Custom setup below](#option-3-any-mcp-client-custom-connector) |

**Before you start, you need:**
- **Draup for Sales access and a Draup user account.** You sign in with it when you connect, and you see only the data your subscription covers.
- **The connector is read-only.** It looks things up in Draup and never changes anything in your Draup account.

---

## Option 1: Claude (recommended)

1. **Open the listing.** Go to the [Draup for Sales listing in Claude's directory](https://claude.ai/directory/draup-for-sales). Or, in Claude, open **Settings → Connectors → Browse connectors** and search for **Draup for Sales**.
2. **Connect.** Click **Connect**. A Draup sign-in page opens.
3. **Sign in.** Sign in with your Draup account and approve access.
4. **Switch it on.** In a new chat, open the tools menu (the **+** or sliders icon under the message box) and make sure **Draup for Sales** is on.
5. **Tell your AI about you.** Paste the [start-here prompt](../prompts/00-start-here/about-me.md), then pick any prompt from the library.

**Make it permanent.** Create a Claude Project (for example "Draup research") and paste the [Claude Project instructions](../prompts/00-start-here/claude-project.md) into it. Every chat in that Project then starts with your context and the library's data rules.

**Built-in prompts.** The connector also ships with a few ready-made prompts, such as a buying-committee map, a why-now timing brief and a displacement playbook. Find them in the **+** menu under Draup for Sales. This library goes further: 90 detailed prompts and 10 playbooks.

> **On a Claude Team or Enterprise plan?** An owner or admin may need to enable the connector for your organisation first. If you can't find it, ask your Claude admin.

## Option 2: ChatGPT

1. **Open the listing.** Go to the [Draup for Sales plugin in ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7). Or, in ChatGPT, open **Plugins** and search for **Draup for Sales**.
2. **Add it.** Add the plugin and sign in with your Draup account when asked.
3. **Use it in a chat.** Start a new chat and select **Draup for Sales** from the tools menu, or ask "use Draup for Sales" in your message.
4. **Paste a prompt.** Paste the [start-here prompt](../prompts/00-start-here/about-me.md), then any prompt from the library.

> These prompts were written and tested in Claude. They use plain language and are designed to work in ChatGPT with the Draup for Sales plugin too. If an answer doesn't use Draup data, add "Use Draup for Sales for this" and resend.

> **On a ChatGPT Business or Enterprise workspace?** Your workspace admin may need to allow the plugin first.

## Option 3: Any MCP client (custom connector)

Draup for Sales is a standard remote MCP server, so any client that supports MCP can connect. These steps follow [Draup's MCP documentation](https://draup.com/sales/data/model-context-protocol).

### Draup for Sales MCP address

```text
https://mcp.draup.com/mcp/sales
```

### Chat apps: Claude custom connector, other chat clients

1. **Add a custom connector.** Open your client's connector settings and choose **Add custom connector**. In Claude: *Settings → Connectors → Add custom connector*.
2. **Paste the address.** Paste the address above and give it a name, such as "Draup for Sales".
3. **Add credentials if asked.** If you're prompted for a client ID and client secret, use the ones Draup provides (see [Getting credentials](#getting-credentials)).
4. **Connect and sign in.** Click **Connect**. A Draup sign-in opens in your browser; sign in and approve access. You never handle a password or token yourself.

### Claude Code

Run:

```bash
claude mcp add --transport http draup-sales https://mcp.draup.com/mcp/sales
```

Then type `/mcp` inside Claude Code, choose **draup-sales** and sign in with your Draup account.

### Coding tools: Cursor, VS Code, Windsurf, Cline

These tools connect with a token that Draup issues to you. Add an entry like this to your tool's MCP settings file:

```json
{
  "mcpServers": {
    "draup-sales": {
      "url": "https://mcp.draup.com/mcp?product-id=3",
      "headers": {
        "Authorization": "Bearer <YOUR_DRAUP_TOKEN>"
      }
    }
  }
}
```

Notes:
- The settings file's exact shape varies by tool. VS Code, for example, nests servers under `"mcp": { "servers": { … } }`. Check your tool's MCP documentation and [Draup's example](https://draup.com/sales/data/model-context-protocol).
- Keep tokens out of shared files and repositories. Use your tool's secret or environment-variable support where it has one.

### Your own agent, Copilot Studio or other platforms

- **Your own agent:** point any MCP SDK's streamable-HTTP client at the address above. Authenticate with a Draup bearer token, or with OAuth client credentials for server-to-server agents.
- **Microsoft Copilot Studio:** Draup's MCP server is available as a certified connector. See [Draup's MCP documentation](https://draup.com/sales/data/model-context-protocol).
- **Older clients that only support local (stdio) servers:** they can connect through a bridge such as `mcp-remote`, which runs locally and forwards to the remote address.

### Getting credentials

Your Draup account team provisions tokens and OAuth clients. Tell them which product you use (Draup for Sales) and how you're connecting: chat app, coding tool or custom agent. You can also reach Draup support at **support@draup.com**.

---

## Check it works

Paste this into a new chat:

```text
Use Draup for Sales: what does microsoft.com do, how big is it, and what are its top three stated priorities? Date every fact.
```

Your assistant should look Microsoft up in Draup and answer with dated facts. If it answers from general knowledge instead, see the next section.

## Troubleshooting

| What you see | What to do |
|---|---|
| The assistant answers without using Draup | Check that Draup for Sales is switched on in the chat's tools menu, then add "use Draup for Sales for this". |
| "Authentication failed", a 401 error, or the connection drops | Disconnect and reconnect Draup for Sales in your settings, then sign in again. |
| You can't find Draup for Sales in the directory | Your organisation may need an admin to enable it. Or add it as a custom connector (Option 3). |
| Some data is missing | You see only what your Draup subscription includes. Ask your Draup account team about access. |
| A coding tool won't connect | Check the token is current and the settings file's format matches your tool. Restart the tool after editing. |

Next: [Getting started](getting-started.md) · [Start-here prompt](../prompts/00-start-here/about-me.md) · [Back to the library](../README.md)
