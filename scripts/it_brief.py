#!/usr/bin/env python3
"""Build the one-page connector brief for IT and security teams.

Writes build/print/it-brief-<product>.html (rendered to PDF by build_it_brief.sh)
and guides/for-it-teams.md for the product this repo covers.
Usage: python3 scripts/it_brief.py [sales|talent ...]
"""
import html
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGO = (ROOT / "assets" / "draup-logo.svg").read_text(encoding="utf-8")
AS_OF = "November 2026"

PRODUCTS = {
    "sales": {
        "name": "Draup for Sales",
        "users": "sales, account and marketing teams",
        "data": "company, buyer and market intelligence (company profiles, priorities, executives, technology, hiring and news)",
        "example": "a company name, an industry or a job function",
        "claude": "https://claude.ai/directory/draup-for-sales",
        "chatgpt": "https://chatgpt.com/plugins/plugin_asdk_app_6ad0b735a0d88191b98c333a6fe40ce7",
        "teams": "https://marketplace.microsoft.com/en-us/product/WA200010751",
        "mcp": "https://mcp.draup.com/mcp/sales",
        "docs": "https://draup.com/sales/data/model-context-protocol",
    },
    "talent": {
        "name": "Draup for Talent",
        "users": "talent acquisition, HR and workforce planning teams",
        "data": "labour-market intelligence (talent supply, pay benchmarks, skills, locations and hiring demand)",
        "example": "a job role, a skill, a city or a company name",
        "claude": "https://claude.ai/directory/draup-for-talent",
        "chatgpt": "https://chatgpt.com/plugins/plugin_asdk_app_6ad0b72ec66c8191a18824950ffe0a60",
        "teams": "https://marketplace.microsoft.com/en-us/product/wa200012890",
        "mcp": "https://mcp.draup.com/mcp/talent",
        "docs": "https://draup.com/talent/data/model-context-protocol",
    },
}

SOURCES = {
    "anthropic_policy": "https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy",
    "anthropic_admin": "https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities",
    "openai_review": "https://developers.openai.com/apps-sdk/app-submission-guidelines/",
    "openai_admin": "https://help.openai.com/en/articles/11509118",
    "ms_review": "https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/teams-store-validation-guidelines",
    "ms_admin": "https://learn.microsoft.com/en-us/microsoftteams/manage-apps",
    "privacy": "https://draup.com/privacy-policy",
    "trust": "https://trust.draup.com",
}

# Each section: (heading, [bullets]). Bullets may contain {placeholders} and inline HTML.
def sections(p):
    return {
        "summary": (
            f"<b>{p['name']}</b> is a connector that lets your licensed Draup users ask questions of Draup's "
            f"{p['data']} from inside Claude, ChatGPT or Microsoft 365 Copilot and Teams. "
            "<b>It gives the AI assistant access to Draup's data, not to yours.</b> "
            "It is published by Draup, Inc. in each platform's official directory, and each platform reviewed it before listing it."
        ),
        "reach": ("What it can and cannot reach", [
            "<b>It connects to one place:</b> Draup's own service at <code>mcp.draup.com</code>, over HTTPS.",
            "<b>It has no access to your systems.</b> It cannot see your email, files, CRM, HR system, network or devices.",
            "<b>Nothing is installed</b> on laptops or servers. It is a hosted connector that the AI platform calls.",
            f"<b>What goes to Draup:</b> the lookup the assistant makes, such as {p['example']}.",
            "<b>What comes back:</b> Draup's licensed market data. The conversation itself stays under your existing agreement with the AI platform.",
        ]),
        "access": ("How access is controlled", [
            "<b>Each user signs in with their own Draup account</b> in the browser, using OAuth 2.0. No passwords or API keys are pasted into the AI app.",
            "<b>Access follows the user's Draup licence and permissions.</b> A person without a Draup licence gets no data.",
            "<b>Every tool is labelled</b> as read-only or not, as the platforms require, and the assistant asks the user before using a tool unless your admins decide otherwise.",
        ]),
        "posture": ("Draup's security and compliance", [
            "Draup states it upholds <b>SOC 2, ISO 27001, ISO 42001, GDPR and CCPA</b>.",
            "Data is <b>encrypted in transit and at rest</b>, and the platform is hosted in the United States.",
            "Draup treats customer data as confidential and uses it only to deliver the service.",
            f"Compliance documents: <a href='{SOURCES['trust']}'>trust.draup.com</a>. Privacy policy: <a href='{SOURCES['privacy']}'>draup.com/privacy-policy</a>.",
        ]),
        "reviews": ("Reviews it has already passed", [
            ("Claude", "Anthropic Connectors Directory", p["claude"], SOURCES["anthropic_policy"], [
                "Anthropic reviews listed connectors for safety, security and compatibility, at submission and on an ongoing basis.",
                "Sign-in must use OAuth 2.0 with certificates from a recognised authority.",
                "Every tool must declare whether it only reads or can change data.",
                "The publisher must give Anthropic a test account and a privacy policy, and collect only the data it needs.",
            ]),
            ("ChatGPT", "OpenAI app directory", p["chatgpt"], SOURCES["openai_review"], [
                "Only verified individuals or organisations can submit.",
                "A published privacy policy and minimum data collection are required.",
                "OpenAI's reviewers test the app with a demo account.",
                "After publication, OpenAI scans the hosted connector daily.",
            ]),
            ("Microsoft 365 Copilot &amp; Teams", "Microsoft Marketplace", p["teams"], SOURCES["ms_review"], [
                "The app must pass Microsoft's store validation; every \"must fix\" issue has to be resolved first.",
                "The privacy policy must cover data storage, retention, deletion and security controls.",
                "The app may only use domains the publisher controls.",
                "AI apps must have safeguards against attempts to override their instructions.",
            ]),
        ]),
        "controls": ("Controls your admins keep", [
            (f"<b>Claude (Team, Enterprise).</b> Connectors stay off until an Owner enables them. Each tool can be set to "
             f"Always allow, Needs approval or Blocked for the whole organisation, and users cannot override it. "
             f"<a href='{SOURCES['anthropic_admin']}'>Details</a>"),
            (f"<b>ChatGPT (Enterprise, Edu).</b> Apps are disabled by default. Admins enable each app, can limit it by role, "
             f"and can require confirmation before actions. By default OpenAI does not train on business workspace content, "
             f"including information accessed through apps. <a href='{SOURCES['openai_admin']}'>Details</a>"),
            (f"<b>Microsoft 365.</b> Admins allow or block the app and choose which users or groups get it in the Teams admin center, "
             f"where they also review its permissions. <a href='{SOURCES['ms_admin']}'>Details</a>"),
        ]),
        "path": ("A low-risk way to approve it", [
            f"<b>Approve this one connector by name</b> ({p['name']}, by Draup) instead of opening all external connectors.",
            "<b>Limit it to your licensed Draup users</b>, or start with a pilot group.",
            "<b>Keep \"ask before using a tool\" on</b> to begin with; relax it later if you wish.",
            "<b>Allow one domain</b> if you filter outbound traffic: <code>mcp.draup.com</code> (plus Draup's sign-in page).",
        ]),
    }


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font-family:-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;color:#14233b;font-size:7.8pt;line-height:1.32;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;display:flex;flex-direction:column;overflow:hidden}
header{background:linear-gradient(135deg,#041631,#0a2e66);color:#fff;padding:6.5mm 12mm 5mm}
header .row{display:flex;align-items:center;justify-content:space-between}
header svg{height:7.5mm;width:auto;color:#fff}
header .tag{font-size:7.4pt;letter-spacing:.14em;text-transform:uppercase;color:#6dcef9;font-weight:700}
header h1{font-size:17pt;line-height:1.15;margin:3.5mm 0 1mm;font-weight:800;letter-spacing:-.01em}
header p{margin:0;color:#cfe1ff;font-size:9pt}
main{padding:4.5mm 12mm 0;flex:1;display:flex;flex-direction:column;gap:3mm}
.summary{background:#eef5ff;border-left:1.2mm solid #146ef5;border-radius:1.5mm;padding:2.8mm 4mm;font-size:8.7pt;line-height:1.4}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.col{display:flex;flex-direction:column;gap:3.2mm}
h2{font-size:9.4pt;margin:0 0 1.5mm;color:#0a2e66;font-weight:800;text-transform:uppercase;letter-spacing:.05em;border-bottom:.35mm solid #d6e2f5;padding-bottom:1mm}
ul{margin:0;padding-left:3.6mm}
li{margin:0 0 1.05mm}
li::marker{color:#146ef5}
a{color:#0b57d0;text-decoration:none}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:7.9pt;background:#eef2f8;padding:0 1mm;border-radius:.8mm;white-space:nowrap}
.plat{border:.3mm solid #d6e2f5;border-radius:1.6mm;padding:1.8mm 3mm .8mm;margin-bottom:1.6mm}
.plat h3{margin:0 0 1.1mm;font-size:8.8pt;color:#14233b}
.plat h3 span{font-weight:500;color:#52627a}
.plat h3 a{font-weight:600;font-size:7.4pt;margin-left:1.5mm}
.plat li{margin-bottom:.7mm}
.path{background:#f5f8fc;border:.3mm solid #d6e2f5;border-radius:1.6mm;padding:2.6mm 4mm 1.4mm}
.path ol{margin:0;padding-left:4.2mm;columns:2;column-gap:7mm}
.path li{break-inside:avoid;margin-bottom:1.3mm}
.path li::marker{font-weight:800;color:#146ef5}
footer{margin-top:auto;padding:2mm 12mm 5mm;font-size:7.1pt;color:#52627a;line-height:1.4}
footer .facts{display:flex;gap:1mm 5mm;flex-wrap:wrap;border-top:.35mm solid #d6e2f5;padding-top:2mm;margin-bottom:0;color:#14233b;font-size:7.3pt}
footer .facts b{color:#0a2e66}
"""


def render_html(key):
    p = PRODUCTS[key]
    s = sections(p)
    plats = "".join(
        f"<div class='plat'><h3>{n} <span>· {html.escape(d)}</span></h3>{ul(b)}"
        f"<div style='font-size:7pt;margin:-.3mm 0 .8mm'><a href='{listing}'>View the listing</a> · <a href='{src}'>The platform's published requirements</a></div></div>"
        for n, d, listing, src, b in s["reviews"][1]
    )
    path = "<ol>" + "".join(f"<li>{i}</li>" for i in s["path"][1]) + "</ol>"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{p['name']} connector: brief for IT and security teams</title><style>{CSS}</style></head><body><div class="page">
<header><div class="row">{LOGO}<span class="tag">For IT and security teams</span></div>
<h1>{p['name']} connector: a brief for your IT team</h1>
<p>A one-page brief for approving the connector your {p['users']} have asked for.</p></header>
<main>
<div class="summary">{s['summary']}</div>
<div class="cols">
<div class="col">
<section><h2>{s['reach'][0]}</h2>{ul(s['reach'][1])}</section>
<section><h2>{s['access'][0]}</h2>{ul(s['access'][1])}</section>
<section><h2>{s['controls'][0]}</h2>{ul(s['controls'][1])}</section>
</div>
<div class="col">
<section><h2>{s['reviews'][0]}</h2>{plats}</section>
<section><h2>{s['posture'][0]}</h2>{ul(s['posture'][1])}</section>
</div>
</div>
<div class="path"><h2 style="border:0;padding:0;margin-bottom:1.8mm">{s['path'][0]}</h2>{path}</div>
</main>
<footer><div class="facts"><span><b>Connector address</b> <code>{p['mcp']}</code></span>
<span><b>Setup guide</b> <a href="{p['docs']}">{p['docs'].replace('https://','')}</a></span>
<span><b>Questions</b> <a href="mailto:support@draup.com">support@draup.com</a></span><span style="margin-left:auto;color:#52627a">Draup, Inc. · {AS_OF}</span></div>
</footer>
</div></body></html>"""


def strip_tags(t):
    import re
    t = re.sub(r"<a href='([^']+)'>([^<]+)</a>", r"[\2](\1)", t)
    t = re.sub(r"</?b>", "**", t)
    t = re.sub(r"</?code>", "`", t)
    return t


def render_md(key):
    p = PRODUCTS[key]
    s = sections(p)
    out = [f"# {p['name']} connector: a brief for your IT team", "",
           f"A one-page brief for approving the connector your {p['users']} have asked for. "
           f"[Download the PDF](../pdf/draup-for-{key}-connector-it-brief.pdf).", "",
           "> Using Draup for Talent? [Download the Draup for Talent brief](../pdf/draup-for-talent-connector-it-brief.pdf).", "",
           strip_tags(s["summary"]), ""]
    for k in ("reach", "access", "posture"):
        out += [f"## {s[k][0]}", ""] + [f"- {strip_tags(i)}" for i in s[k][1]] + [""]
    out += [f"## {s['reviews'][0]}", ""]
    for n, d, listing, src, b in s["reviews"][1]:
        out += [f"### {n.replace('&amp;','&')} · {d}", "", f"[View listing]({listing}) · [Platform's published requirements]({src})", ""]
        out += [f"- {i}" for i in b] + [""]
    out += [f"## {s['controls'][0]}", ""] + [f"- {strip_tags(i)}" for i in s["controls"][1]] + [""]
    out += [f"## {s['path'][0]}", ""] + [f"{n}. {strip_tags(i)}" for n, i in enumerate(s["path"][1], 1)] + [""]
    out += ["## Connection details", "", f"- Connector address: `{p['mcp']}`", f"- Setup guide: {p['docs']}",
            "- Questions: support@draup.com", ""]
    return "\n".join(out)


if __name__ == "__main__":
    keys = sys.argv[1:] or list(PRODUCTS)
    outdir = ROOT / "build" / "print"
    outdir.mkdir(parents=True, exist_ok=True)
    for k in keys:
        (outdir / f"it-brief-{k}.html").write_text(render_html(k), encoding="utf-8")
        print(f"wrote build/print/it-brief-{k}.html")
    (ROOT / "guides" / "for-it-teams.md").write_text(render_md("sales"), encoding="utf-8")
    print("wrote guides/for-it-teams.md")
