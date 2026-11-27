"""Build the Agent Skill, the all-in-one file and llms.txt from data/*.json.

Called by build.py. Outputs:
  skill/draup-sales-prompts/            the skill folder (SKILL.md + references/)
  plugins/draup-sales/skills/...        same skill inside the Claude Code plugin
  dist/draup-sales-prompts-skill.zip    zip for claude.ai upload (folder at zip root)
  dist/draup-sales-prompts-all.md       one file with every prompt, for ChatGPT/other AIs
  llms.txt, docs/llms.txt               index for AIs given the link
"""
import json
import shutil
import zipfile
from pathlib import Path

SKILL_NAME = "draup-sales-prompts"


def _rules(prompts):
    setup = next((p for p in prompts if p["id"] == "setup-about-me"), None)
    if not setup:
        return ""
    txt = setup["prompt"]
    for marker in ("Data rules", "RULES"):
        i = txt.find(marker)
        if i != -1:
            return txt[i:]
    return ""


def build(root, meta, prompts, playbooks, cats, by_id):
    root = Path(root)
    links = meta.get("links", {})
    sk = root / "skill" / SKILL_NAME
    if sk.exists():
        shutil.rmtree(sk)
    (sk / "references").mkdir(parents=True)

    used = [c for c in meta["categories"] if any(p["category"] == c["id"] for p in prompts)]

    # references: one file per category
    for c in used:
        ps = [p for p in prompts if p["category"] == c["id"]]
        out = [f"# {c['name']}", "", c["desc"], ""]
        for p in ps:
            out += [f"## {p['title']}", "", f"- **id:** `{p['id']}`", f"- **What you get:** {p['outcome']}", f"- **Use it when:** {p['when']}",
                    f"- **Best for:** {', '.join(meta['roles'][r]['name'] for r in p['roles'])}", f"- **Time:** {p['time']}"]
            if p["status"] == "schema-only":
                out.append("- **Note:** needs the separate Draup for Talent connector; not live-tested.")
            if p["inputs"]:
                out += ["- **Inputs:** " + "; ".join(f"{i['name']} (e.g. {i['example']})" for i in p["inputs"])]
            out += ["", "### Detailed prompt", "", "```text", p["prompt"], "```", "", "### Quick version", "", "```text", p["quick"], "```", ""]
            if p["followups"]:
                out += ["### Follow-ups", ""] + [f"- {f}" for f in p["followups"]] + [""]
            if p["tips"]:
                out += ["### Tips", ""] + [f"- {t}" for t in p["tips"]] + [""]
        (sk / "references" / f"{c['folder'][3:]}.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    # index
    idx = ["# Prompt index", "", "Pick the prompt whose job matches the user's request, then open its file and follow that prompt exactly.", "",
           "| id | Title | Use it when | File |", "|---|---|---|---|"]
    for c in used:
        for p in prompts:
            if p["category"] == c["id"]:
                idx.append(f"| `{p['id']}` | {p['title']} | {p['when'].replace('|', '/')} | references/{c['folder'][3:]}.md |")
    (sk / "references" / "index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    # playbooks
    pb = ["# Playbooks", "", "Multi-step workflows. Run the steps in order in one conversation; each step names the prompt id to use.", ""]
    for b in playbooks:
        pb += [f"## {b['title']}", "", f"**Goal:** {b['goal']}", f"**For:** {', '.join(meta['roles'][r]['name'] for r in b.get('for', []) if r in meta['roles'])} · **Time:** {b.get('time','')}", ""]
        for n, s in enumerate(b["steps"], 1):
            t = by_id[s["prompt_id"]]["title"] if s["prompt_id"] in by_id else s["prompt_id"]
            pb.append(f"{n}. **{t}** (`{s['prompt_id']}`): {s.get('why','')} *Look for:* {s.get('what_to_look_for','')}")
        pb += ["", f"**Finish with:** {b.get('finish','')}", ""]
    (sk / "references" / "playbooks.md").write_text("\n".join(pb) + "\n", encoding="utf-8")

    rules = _rules(prompts)
    extra = """
## Data quirks to know

- Name vendors the way Draup spells them in the tech stack (for example "salesforce.com", not "Salesforce"). Search job postings by the product's skill name (for example "CrowdStrike Falcon"), and retry once with the plain product name if the count is 0.
- Countries need Draup's full names ("United States of America"). Regions like "North America" may not resolve; try "Northern America" or list the countries.
- Website lookups can land on a subsidiary. Confirm the parent; if a website doesn't resolve, try the company name and show the match score.
- Executive data can't be searched by name or title, and the seniority filter is ignored. Page through the function 10 at a time and check each title.
- Count a competitor as present only at High or Medium usage.
- Rate services rivals by share of the account's engagements in the relevant work: 30% or more Red, 10 to 29% Amber, under 10% Green.
- Sort company lists by total workforce or IT spend; sorting by employee count is not supported.
"""
    (sk / "references" / "data-rules.md").write_text("# Data rules\n\nApply these to every answer.\n\n```text\n" + rules.strip() + "\n```\n" + extra, encoding="utf-8")

    cat_lines = "\n".join(f"- **{c['name']}** (`references/{c['folder'][3:]}.md`): {c['desc']}" for c in used)
    desc = ("Sales research and outreach with Draup data. Use to prep for calls, find who to contact, check and "
            "displace rivals, handle objections, build lists, plan accounts and write emails.")
    assert ": " not in desc and len(desc) <= 200
    assert len(desc) <= 200, len(desc)
    ROUTES = [
        ("Prep me for a call / meeting with [company or person]", "research-precall-snapshot", "research-account-brief"),
        ("Tell me about [company] / account brief", "research-account-brief", "research-swot"),
        ("Who should I contact / who owns [area] at [company]", "people-buying-committee", "people-new-leaders-warm-paths"),
        ("Who is [person] / profile an executive", "people-executive-profile", "people-discovery-questions"),
        ("Why reach out now / what changed at [company]", "signals-whats-actionable", "signals-change-log"),
        ("Is [competitor] installed at [company]? How do I displace it?", "tech-competitor-installed", "deals-competitive-strategy"),
        ("Write an email / opener to [person or company]", "signals-signal-to-email", "outreach-new-executive"),
        ("LinkedIn note or InMail to [person]", "outreach-linkedin-exec", "outreach-new-executive"),
        ("Cold call script / voicemail", "outreach-cold-call", "outreach-linkedin-exec"),
        ("Handle an objection", "deals-objection-handler", "deals-champion-pack"),
        ("Build or size a target list / ICP", "prospect-icp-list", "prospect-hiring-led-list"),
        ("Which accounts are ready for [what I sell]?", "plays-cloud-targets", "plays-data-targets"),
        ("Who outsources to whom / incumbent providers", "services-outsourcing-footprint", "services-competitor-at-account"),
        ("Account plan / QBR / renewal risk", "plan-account-plan", "plan-risk-check"),
        ("Tier my accounts / plan territories", "plan-propensity-tiering", "leaders-territory-potential"),
        ("Industry overview for [vertical]", "market-vertical-snapshot", "market-industry-pov"),
        ("Which partner should I co-sell with?", "services-cosell-partner", "partners-recruit-si-shortlist"),
        ("Weekly news on my accounts", "signals-weekly-book-sweep", "signals-vertical-digest"),
    ]
    routing = "| The user says | Use | Or |\n|---|---|---|\n" + "\n".join(
        f"| {say} | `{a}` ({by_id[a]['title']}) | `{b}` |" for say, a, b in ROUTES if a in by_id and b in by_id)
    skill_md = f"""---
name: {SKILL_NAME}
description: {desc}
license: CC-BY-4.0
---

# Draup Sales Prompt Library

You help sellers get decision-ready answers from **Draup for Sales** data. This skill contains {len(prompts)} detailed prompts ({sum(p["status"] == "tested" for p in prompts)} tested on live Draup data, {sum(p["status"] != "tested" for p in prompts)} previews that need the Draup for Talent connector) and {len(playbooks)} playbooks. Each prompt says exactly what to pull, how to narrow it, what to output, and which data cautions apply.

## How to use this skill

1. **Check that Draup data is available.** The Draup for Sales connector (Claude) or plugin (ChatGPT) must be connected. If it isn't, tell the user how to connect it: Claude {links.get('claude','')} · ChatGPT {links.get('chatgpt','')} · any other MCP client: {links.get('mcp_docs','')}. Don't answer from general knowledge as if it were Draup data.
2. **Understand the job.** Work out what the user wants to get done (e.g. prepare for a meeting, find buyers, build a list, beat a competitor) and their role if known.
3. **Pick the prompt.** Open `references/index.md`, choose the single best prompt by its "Use it when" line, then open its category file. For multi-step goals, check `references/playbooks.md`.
4. **Fill the inputs.** Take inputs from the user's message or earlier context (what they sell, territory, competitors). If required inputs are missing, ask for them together in one short message (at most two questions). Don't run on example values. If the user names a person or title Draup doesn't have, say so in your first line and show the 3 closest people Draup does have.
5. **Follow the detailed prompt exactly.** Run its STEPS in order, produce its OUTPUT format, and obey its RULES and STANDARD RULES. Use the quick version only if the user asks for something fast.
6. **Apply the data rules** in `references/data-rules.md` to every answer: date every fact, say "Not in Draup" instead of guessing, confirm the parent company, flag conflicting or single-source facts.
7. **Offer the prompt's follow-ups** at the end.

If the user is new, suggest they first tell you about themselves using the **Tell your AI about you** prompt (`setup-about-me` in `references/start-here.md`).

## Common requests and the prompt to use

{routing}

For anything else, search `references/index.md` by the job the user wants done.

## What's inside

{cat_lines}
- **Playbooks** (`references/playbooks.md`): complete workflows that chain prompts.
- **Data rules** (`references/data-rules.md`).

Library home: {meta['pages']} · Source: {meta['repo']} · Support: {links.get('support','')}
"""
    (sk / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (sk / "LICENSE.txt").write_text("Prompts and guides: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).\nCredit: \"Draup Sales Prompt Library by Draup, Inc.\" " + meta["repo"] + "\n\"Draup\" is a trademark of Draup, Inc.\n", encoding="utf-8")

    # plugin copy
    pl = root / "plugins" / "draup-sales" / "skills" / SKILL_NAME
    if pl.exists():
        shutil.rmtree(pl)
    shutil.copytree(sk, pl)

    # Claude Code plugin + marketplace
    plug = root / "plugins" / "draup-sales"
    (plug / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    version = meta.get("version", "1.0.0")
    (plug / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "draup-sales",
        "version": version,
        "description": "Draup Sales Prompt Library: tested prompts and playbooks for sales research and outreach, plus the Draup for Sales connector.",
        "author": {"name": "Draup, Inc.", "url": "https://draup.com"},
        "homepage": meta["pages"],
        "repository": meta["repo"],
        "license": "CC-BY-4.0",
        "keywords": ["sales", "prompts", "draup", "account-research", "mcp"]
    }, indent=2) + "\n", encoding="utf-8")
    (plug / ".mcp.json").write_text(json.dumps({"mcpServers": {"draup-sales": {"type": "http", "url": links.get("mcp_url", "https://mcp.draup.com/mcp/sales")}}}, indent=2) + "\n", encoding="utf-8")
    (root / ".claude-plugin").mkdir(exist_ok=True)
    (root / ".claude-plugin" / "marketplace.json").write_text(json.dumps({
        "name": "draup-sales-prompts",
        "owner": {"name": "Draup, Inc.", "url": "https://draup.com"},
        "metadata": {"description": "Draup Sales Prompt Library for Claude Code", "version": version},
        "plugins": [{"name": "draup-sales", "source": "./plugins/draup-sales",
                     "description": "Tested sales prompts and playbooks for Draup for Sales, with the Draup for Sales connector included."}]
    }, indent=2) + "\n", encoding="utf-8")

    # zip for claude.ai
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    zp = dist / f"{SKILL_NAME}-skill.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(sk.rglob("*")):
            if f.is_file():
                info = zipfile.ZipInfo(str(Path(SKILL_NAME) / f.relative_to(sk)), date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, f.read_bytes())

    # all-in-one file
    howto = skill_md.split("## How to use this skill", 1)[1].split("## What's inside", 1)[0].strip()
    for a, b in (("Open `references/index.md`", "Use the **Prompt index** below"), ("then open its category file", "then go to that prompt's section in this file"),
                 ("check `references/playbooks.md`", "check the **Playbooks** section"), ("in `references/data-rules.md`", "in the **Data rules** section at the end"),
                 ("(`setup-about-me` in `references/start-here.md`)", "(`setup-about-me`, in the Start here section)"), ("search `references/index.md`", "search the Prompt index")):
        howto = howto.replace(a, b)
    idx_rows = ["## Prompt index", "", "| id | Title | Use it when | Section |", "|---|---|---|---|"]
    for c in used:
        for p in prompts:
            if p["category"] == c["id"]:
                idx_rows.append(f"| `{p['id']}` | {p['title']} | {p['when'].replace('|', '/')} | {c['name']} |")
    allmd = [f"# Draup Sales Prompt Library (all prompts)", "",
             f"{len(prompts)} prompts and {len(playbooks)} playbooks for Claude, ChatGPT or any AI assistant connected to Draup for Sales. Source: {meta['repo']} · Licence: CC BY 4.0, credit \"Draup Sales Prompt Library by Draup, Inc.\"", "",
             "## Instructions for the assistant", "", howto, "", "\n".join(idx_rows), ""]
    for c in used:
        allmd.append((sk / "references" / f"{c['folder'][3:]}.md").read_text(encoding="utf-8"))
    allmd.append((sk / "references" / "playbooks.md").read_text(encoding="utf-8"))
    allmd.append((sk / "references" / "data-rules.md").read_text(encoding="utf-8"))
    (dist / f"{SKILL_NAME}-all.md").write_text("\n\n".join(allmd), encoding="utf-8")

    # llms.txt
    raw = meta["repo"].replace("github.com", "raw.githubusercontent.com") + "/main"
    llms = [f"# {meta['title']}", "", f"> {meta['tagline']}", "",
            "Use these prompts with the Draup for Sales connector (Claude) or plugin (ChatGPT). Pick the prompt that matches the user's job, fill its inputs, and follow its steps, output format and rules exactly.", "",
            "## Start here", "",
            f"- [Prompt index]({raw}/skill/{SKILL_NAME}/references/index.md): start here; pick a prompt by job, then open its sales-job file below",
            f"- [How to use the prompts]({raw}/skill/{SKILL_NAME}/SKILL.md): instructions and common requests",
            f"- [Data rules]({raw}/skill/{SKILL_NAME}/references/data-rules.md)",
            f"- [Connect Draup]({meta['repo']}/blob/main/guides/connect.md)", "", "## Prompts by sales job", ""]
    for c in used:
        llms.append(f"- [{c['name']}]({raw}/skill/{SKILL_NAME}/references/{c['folder'][3:]}.md): {c['desc']}")
    llms += ["", "## Optional", "", f"- [Playbooks]({raw}/skill/{SKILL_NAME}/references/playbooks.md)", f"- [All prompts in one file]({raw}/dist/{SKILL_NAME}-all.md): large (about 1 MB); for uploading to ChatGPT Projects or a knowledge store, not for browsing", f"- [Interactive library]({meta['pages']})"]
    txt = "\n".join(llms) + "\n"
    (root / "llms.txt").write_text(txt, encoding="utf-8")
    (root / "docs" / "llms.txt").write_text(txt, encoding="utf-8")
