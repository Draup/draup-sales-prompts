# Draup for Sales connector: a brief for your IT team

A one-page brief for approving the connector your sales, account and marketing teams have asked for. [Download the PDF](../pdf/draup-for-sales-connector-it-brief.pdf).

> Using Draup for Talent? [Download the Draup for Talent brief](../pdf/draup-for-talent-connector-it-brief.pdf).

**Draup for Sales** is a connector that lets your licensed Draup users ask questions of Draup's company, buyer and market intelligence (company profiles, priorities, executives, technology, hiring and news) from inside Claude, ChatGPT or Microsoft 365 Copilot and Teams. **It gives the AI assistant access to Draup's data, not to yours.** It is published by Draup, Inc. in each platform's official directory, and each platform reviewed it before listing it.

## What it can and cannot reach

- **It connects to one place:** Draup's own service at `mcp.draup.com`, over HTTPS.
- **It has no access to your systems.** It cannot see your email, files, CRM, HR system, network or devices.
- **Nothing is installed** on laptops or servers. It is a hosted connector that the AI platform calls.
- **What goes to Draup:** the lookup the assistant makes, such as a company name, an industry or a job function.
- **What comes back:** Draup's licensed market data. The conversation itself stays under your existing agreement with the AI platform.

## How access is controlled

- **Each user signs in with their own Draup account** in the browser, using OAuth 2.0. No passwords or API keys are pasted into the AI app.
- **Access follows the user's Draup licence and permissions.** A person without a Draup licence gets no data.
- **Every tool is labelled** as read-only or not, as the platforms require, and the assistant asks the user before using a tool unless your admins decide otherwise.

## Draup's security and compliance

- Draup states it upholds **SOC 2, ISO 27001, ISO 42001, GDPR and CCPA**.
- Data is **encrypted in transit and at rest**, and the platform is hosted in the United States.
- Draup treats customer data as confidential and uses it only to deliver the service.
- Compliance documents: [trust.draup.com](https://trust.draup.com). Privacy policy: [draup.com/privacy-policy](https://draup.com/privacy-policy).

## Reviews it has already passed

### Claude · Anthropic Connectors Directory

[View listing](https://claude.ai/directory/draup-for-sales) · [Platform's published requirements](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

- Anthropic reviews listed connectors for safety, security and compatibility, at submission and on an ongoing basis.
- Sign-in must use OAuth 2.0 with certificates from a recognised authority.
- Every tool must declare whether it only reads or can change data.
- The publisher must give Anthropic a test account and a privacy policy, and collect only the data it needs.

### ChatGPT · OpenAI app directory

[View listing](https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7) · [Platform's published requirements](https://developers.openai.com/apps-sdk/app-submission-guidelines/)

- Only verified individuals or organisations can submit.
- A published privacy policy and minimum data collection are required.
- OpenAI's reviewers test the app with a demo account.
- After publication, OpenAI scans the hosted connector daily.

### Microsoft 365 Copilot & Teams · Microsoft Marketplace

[View listing](https://marketplace.microsoft.com/en-us/product/WA200010751) · [Platform's published requirements](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/teams-store-validation-guidelines)

- The app must pass Microsoft's store validation; every "must fix" issue has to be resolved first.
- The privacy policy must cover data storage, retention, deletion and security controls.
- The app may only use domains the publisher controls.
- AI apps must have safeguards against attempts to override their instructions.

## Controls your admins keep

- **Claude (Team, Enterprise).** Connectors stay off until an Owner enables them. Each tool can be set to Always allow, Needs approval or Blocked for the whole organisation, and users cannot override it. [Details](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- **ChatGPT (Enterprise, Edu).** Apps are disabled by default. Admins enable each app, can limit it by role, and can require confirmation before actions. By default OpenAI does not train on business workspace content, including information accessed through apps. [Details](https://help.openai.com/en/articles/11509118)
- **Microsoft 365.** Admins allow or block the app and choose which users or groups get it in the Teams admin center, where they also review its permissions. [Details](https://learn.microsoft.com/en-us/microsoftteams/manage-apps)

## A low-risk way to approve it

1. **Approve this one connector by name** (Draup for Sales, by Draup) instead of opening all external connectors.
2. **Limit it to your licensed Draup users**, or start with a pilot group.
3. **Keep "ask before using a tool" on** to begin with; relax it later if you wish.
4. **Allow one domain** if you filter outbound traffic: `mcp.draup.com` (plus Draup's sign-in page).

## Connection details

- Connector address: `https://mcp.draup.com/mcp/sales`
- Setup guide: https://draup.com/sales/data/model-context-protocol
- Questions: support@draup.com
