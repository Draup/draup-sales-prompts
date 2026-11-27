#!/usr/bin/env python3
"""Build every human-facing file in this repo from data/*.json.

    python3 scripts/build.py            # validate + generate markdown, CSV, site, print HTML
    python3 scripts/build.py --check    # validate only (used in CI)
"""
import csv
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
META = json.loads((DATA / "meta.json").read_text(encoding="utf-8"))
PROMPTS = json.loads((DATA / "prompts.json").read_text(encoding="utf-8"))
PLAYBOOKS = json.loads((DATA / "playbooks.json").read_text(encoding="utf-8")) if (DATA / "playbooks.json").exists() else []

CATS = {c["id"]: c for c in META["categories"]}
ROLES = META["roles"]
LAYERS = META["data"]
BY_ID = {p["id"]: p for p in PROMPTS}
REQUIRED = ["id", "category", "title", "outcome", "when", "roles", "data", "time", "inputs", "quick", "prompt", "followups", "tips", "tools", "status"]
TECH_WORDS = re.compile(r"\b(v3|endpoint|payload|api|json|mcp__|response_data|get_[a-z_]+)\b", re.I)


def fail(msgs):
    print("\n".join("ERROR: " + m for m in msgs))
    sys.exit(1)


def validate():
    errs, ids = [], set()
    for p in PROMPTS:
        pid = p.get("id", "<missing id>")
        for k in REQUIRED:
            if k not in p or p[k] in ("", None):
                errs.append(f"{pid}: missing {k}")
        if pid in ids:
            errs.append(f"{pid}: duplicate id")
        ids.add(pid)
        if p.get("category") not in CATS:
            errs.append(f"{pid}: unknown category {p.get('category')}")
        elif not pid.startswith(p["category"] + "-"):
            errs.append(f"{pid}: id must start with '{p['category']}-'")
        for r in p.get("roles", []):
            if r not in ROLES:
                errs.append(f"{pid}: unknown role {r}")
        for d in p.get("data", []):
            if d not in LAYERS:
                errs.append(f"{pid}: unknown data layer {d}")
        for field in ("title", "outcome", "quick", "prompt"):
            m = TECH_WORDS.search(p.get(field, ""))
            if m:
                errs.append(f"{pid}: technical word '{m.group(0)}' in {field}")
        if "```" in p.get("prompt", "") + p.get("quick", ""):
            errs.append(f"{pid}: prompt contains a code fence")
        for h in ("INPUTS", "STEPS", "OUTPUT", "RULES"):
            if p.get("category") != "setup" and h not in p.get("prompt", ""):
                errs.append(f"{pid}: prompt missing {h} section")
        if p.get("status") not in ("tested", "schema-only"):
            errs.append(f"{pid}: status must be tested or schema-only")
        if p.get("seller", "both") not in META.get("sellers", {"both": 1}):
            errs.append(f"{pid}: unknown seller {p.get('seller')}")
    for p in PROMPTS:
        for r in p.get("related", []):
            if r not in BY_ID:
                errs.append(f"{p['id']}: related id '{r}' not found")
    for pb in PLAYBOOKS:
        for s in pb.get("steps", []):
            if s.get("prompt_id") not in BY_ID:
                errs.append(f"playbook {pb.get('id')}: prompt_id '{s.get('prompt_id')}' not found")
    if errs:
        fail(errs)
    print(f"OK: {len(PROMPTS)} prompts, {len(PLAYBOOKS)} playbooks valid")


# ---------- helpers ----------
def slug(p):
    return p["id"][len(p["category"]) + 1:]


def ppath(p):
    return f"prompts/{CATS[p['category']]['folder']}/{slug(p)}.md"


def link(p, frm=""):
    rel = "../" * frm.count("/")
    return f"[{p['title']}]({rel}{ppath(p)})"


def roles_txt(p):
    return ", ".join(ROLES[r]["name"] for r in p["roles"])


def layers_txt(p):
    return ", ".join(LAYERS[d]["name"] for d in p["data"])


def write(rel, text):
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text.rstrip() + "\n", encoding="utf-8")


def esc_cell(s):
    return s.replace("|", "\\|").replace("\n", " ")


def in_cat(cid):
    return [p for p in PROMPTS if p["category"] == cid]


def featured():
    ids = META.get("featured") or []
    out = [BY_ID[i] for i in ids if i in BY_ID]
    if not out:
        out = [in_cat(c["id"])[0] for c in META["categories"] if in_cat(c["id"]) and c["id"] != "setup"]
    return out


START = next((p for p in PROMPTS if p["id"] == "setup-about-me"), None)
TALENT_NOTE = "> **Preview.** This prompt uses the separate **Draup for Talent** connector (pay, talent supply, hiring difficulty). It follows the documented data and was not live-tested for this release, so check results carefully."


# ---------- prompt pages ----------
def prompt_page(p):
    rel = ppath(p)
    up = "../" * rel.count("/")
    lines = [f"# {p['title']}", "", f"**{p['outcome']}**", ""]
    lines += [f"| Use it when | Best for | Seller type | Time | Draup data |", "|---|---|---|---|---|",
              f"| {esc_cell(p['when'])} | {roles_txt(p)} | {META.get('sellers', {}).get(p.get('seller', 'both'), 'Everyone')} | {p['time']} | {layers_txt(p)} |", ""]
    if p["status"] == "schema-only":
        lines += [TALENT_NOTE, ""]
    if p["category"] != "setup" and START:
        lines += [f"> **Tip:** run [{START['title']}]({up}{ppath(START)}) once in the chat first. Claude will then fill in *What I sell*, territory and competitors for you.", ""]
    if p["inputs"]:
        lines += ["## 1. Fill in", "", "| Placeholder | Example |", "|---|---|"]
        lines += [f"| `[{esc_cell(i['name'])}]` | {esc_cell(i['example'])} |" for i in p["inputs"]]
        lines += [""]
    how = ("Copy this into your Claude Project's instructions and fill in the `[bracketed]` parts once." if p["id"] == "setup-claude-project"
           else "Replace the `[bracketed]` parts, then paste into Claude with the Draup for Sales connector switched on.")
    lines += ["## 2. Copy the detailed prompt", "", how, "", "```text", p["prompt"], "```", ""]
    lines += ["## In a hurry? Quick version", "", "```text", p["quick"], "```", ""]
    if p["followups"]:
        lines += ["## 3. Keep going: follow-up prompts", "", "Paste these into the same chat after the first answer.", ""]
        for f in p["followups"]:
            lines += ["```text", f, "```", ""]
    if p["tips"]:
        lines += ["## Tips for better results", ""] + [f"- {t}" for t in p["tips"]] + [""]
    rel_links = [BY_ID[r] for r in p.get("related", []) if r in BY_ID]
    if rel_links:
        lines += ["## Related prompts", ""] + [f"- {link(r, rel)}: {r['outcome']}" for r in rel_links] + [""]
    lines += ["<details>", "<summary>Under the hood: Draup tools this prompt typically uses</summary>", "",
              ", ".join(f"`{t}`" for t in p["tools"]), "",
              f"Status: **{'tested live' if p['status']=='tested' else 'documented, not live-tested'}**. Prompt id: `{p['id']}`.", "", "</details>", "",
              f"[Back to {CATS[p['category']]['name']}](README.md) · [All prompts]({up}README.md#find-prompts-by-sales-job)"]
    write(rel, "\n".join(lines))


def category_page(c):
    ps = in_cat(c["id"])
    rel = f"prompts/{c['folder']}/README.md"
    lines = [f"# {c['name']}", "", c["desc"], "", f"{len(ps)} prompts. Click one to open its full prompt, quick version and follow-ups.", "",
             "| Prompt | What you get | Best for | Time |", "|---|---|---|---|"]
    for p in ps:
        tag = " *(Preview: Talent connector)*" if p["status"] == "schema-only" else ""
        lines.append(f"| [{p['title']}]({slug(p)}.md){tag} | {esc_cell(p['outcome'])} | {roles_txt(p)} | {p['time']} |")
    lines += ["", "[Back to the library](../../README.md)"]
    write(rel, "\n".join(lines))


def role_page(code, r):
    ps = [p for p in PROMPTS if code in p["roles"]]
    rel = f"roles/{r['slug']}.md"
    lines = [f"# Prompts for {r['name']}", "", r["desc"], "", f"{len(ps)} prompts, grouped by sales job.", ""]
    if START:
        lines += [f"**First:** run {link(START, rel)} once per chat so every answer is tailored to what you sell.", ""]
    for c in META["categories"]:
        cps = [p for p in ps if p["category"] == c["id"] and p["category"] != "setup"]
        if not cps:
            continue
        lines += [f"## {c['name']}", "", "| Prompt | What you get |", "|---|---|"]
        lines += [f"| {link(p, rel)} | {esc_cell(p['outcome'])} |" for p in cps] + [""]
    pbs = [pb for pb in PLAYBOOKS if code in pb.get("for", [])]
    if pbs:
        lines += ["## Playbooks for you", ""] + [f"- [{pb['title']}](../playbooks/{pb['id']}.md): {pb['goal']}" for pb in pbs] + [""]
    lines += ["[Back to the library](../README.md)"]
    write(rel, "\n".join(lines))


def playbook_pages():
    if not PLAYBOOKS:
        return
    idx = ["# Playbooks", "", "Playbooks chain several prompts into a complete sales workflow. Run the steps in one Claude chat so each answer builds on the last.", "",
           "| Playbook | Goal | For | Time |", "|---|---|---|---|"]
    for pb in PLAYBOOKS:
        idx.append(f"| [{pb['title']}]({pb['id']}.md) | {esc_cell(pb['goal'])} | {', '.join(ROLES[r]['name'] for r in pb.get('for', []) if r in ROLES)} | {pb.get('time','')} |")
        rel = f"playbooks/{pb['id']}.md"
        lines = [f"# {pb['title']}", "", f"**Goal:** {pb['goal']}", "",
                 f"**For:** {', '.join(ROLES[r]['name'] for r in pb.get('for', []) if r in ROLES)} · **Time:** {pb.get('time','')}", ""]
        if START:
            lines += [f"**Step 0.** Run {link(START, rel)} so Claude knows what you sell.", ""]
        for n, s in enumerate(pb["steps"], 1):
            p = BY_ID[s["prompt_id"]]
            lines += [f"## Step {n}. {p['title']}", "", s.get("why", ""), "", f"**Look for:** {s.get('what_to_look_for','')}", "",
                      f"Open the full prompt: {link(p, rel)}", "", "Quick version:", "", "```text", p["quick"], "```", ""]
        lines += ["## What you finish with", "", pb.get("finish", ""), "", "[All playbooks](README.md) · [Back to the library](../README.md)"]
        write(rel, "\n".join(lines))
    idx += ["", "[Back to the library](../README.md)"]
    write("playbooks/README.md", "\n".join(idx))


# ---------- landing page ----------
def readme():
    n = len(PROMPTS)
    tested = sum(p["status"] == "tested" for p in PROMPTS)
    L = []
    L += [f"# {META['title']}", "", f"**{META['tagline']}**", "",
          f"{n} detailed prompts · {len(PLAYBOOKS)} playbooks · 8 sales roles · free to use and adapt ([CC BY 4.0](LICENSE))", "",
          f"[**Open the interactive library**]({META['pages']}) · [**Download the PDF guides**](#download-the-guides) · [**Start in 3 steps**](#start-in-3-steps)", ""]
    L += ["## What you can do with it", "",
          "- **Walk into every meeting prepared.** Get a one-page brief on any account in two minutes, covering size, money, priorities and recent moves.",
          "- **Find the right people.** Map the buying committee, spot new leaders and find warm paths in through your existing customers.",
          "- **Reach out at the right moment.** Catch hiring spikes, leadership changes, new tools and news the week they happen.",
          "- **Build better target lists.** Size your market and list companies that match your ICP, use a competitor or are hiring for what you sell.",
          "- **Win services deals.** See who the incumbent providers are, how deep they go, and where the wedge is.",
          "- **Plan and grow accounts.** Draft account plans, risk checks, QBR prep and territory tiers backed by data.", ""]
    L += ["## Start in 3 steps", "",
          "1. **Connect Draup in Claude.** In Claude, open *Settings → Connectors*, add **Draup for Sales** and sign in with your Draup account. ([Full setup guide](guides/getting-started.md))"]
    if START:
        L += [f"2. **Tell Claude about you, once.** Paste [{START['title']}]({ppath(START)}) at the top of a new chat with your role, offering, territory and competitors. Or save it in a Claude Project so it's always on."]
    L += ["3. **Pick a prompt, fill the `[brackets]`, paste.** Each prompt has a detailed version for the best results, a quick version, and follow-ups to keep going.", "", "Every answer opens with a two-line **bottom line** and closes with a **recommended next step** (who to contact, what to do, why now) and the **gaps** worth asking about in discovery.", ""]
    L += ["## Start with these", "", "| Prompt | What you get | Time |", "|---|---|---|"]
    L += [f"| {link(p)} | {esc_cell(p['outcome'])} | {p['time']} |" for p in featured()] + [""]
    L += ["## Find prompts by role", "", "| Your role | What the prompts help you do |", "|---|---|"]
    L += [f"| [{r['name']}](roles/{r['slug']}.md) | {r['desc']} |" for r in ROLES.values()] + [""]
    L += ["## Find prompts by sales job", "", "| Sales job | What it covers | Prompts |", "|---|---|---|"]
    L += [f"| [{c['name']}](prompts/{c['folder']}/README.md) | {c['desc']} | {len(in_cat(c['id']))} |" for c in META["categories"] if in_cat(c["id"])] + [""]
    if PLAYBOOKS:
        L += ["## Playbooks: complete workflows", "", "Each playbook chains prompts into one end-to-end job.", ""]
        L += [f"- [**{pb['title']}**](playbooks/{pb['id']}.md): {pb['goal']}" for pb in PLAYBOOKS] + [""]
    L += ["## Download the guides", "", "Printable PDFs for people who prefer a document to a website:", "",
          "| Guide | What's inside |", "|---|---|",
          "| [Quick-start guide](pdf/draup-sales-prompts-quick-start.pdf) | Setup, the start-here prompt, the 12 most useful quick prompts, and tips. |",
          "| [Full prompt catalogue](pdf/draup-sales-prompts-catalogue.pdf) | Every prompt in full, with inputs, follow-ups and tips. |",
          "| [Playbooks](pdf/draup-sales-prompts-playbooks.pdf) | Step-by-step workflows for common sales jobs. |",
          "| Role cheat sheets | The quick prompts for each role: " + " · ".join(f"[{r['name']}](pdf/roles/{r['slug']}.pdf)" for r in ROLES.values()) + " |", ""]
    L += ["## How every prompt is built", "",
          "Each prompt is written to get a decision-ready answer, not a data dump:", "",
          "- **Inputs:** the few things you fill in, each with an example.",
          "- **Steps:** exactly which Draup data to pull, in what order, and how to narrow it.",
          "- **Output:** the tables and sections you get back, with columns, top-N and units spelled out.",
          "- **Rules:** guardrails that keep answers honest. Every number is dated, and when Draup has no data the answer says \"Not in Draup\" instead of guessing.", "",
          f"{tested} of {n} prompts were tested live against Draup data on public companies before release. The rest use the Draup for Talent connector and are marked in the library.", ""]
    L += ["## The data behind the prompts", "", "| Draup data | What's in it |", "|---|---|"]
    L += [f"| {v['name']} | {v['desc']} |" for v in LAYERS.values()] + ["", "More detail, including how to read each data type: [Data guide](guides/data-guide.md). New to the terms? See the [Glossary](guides/glossary.md).", ""]
    L += ["## Good to know", "",
          "- **Your access applies.** The connector is read-only and shows what your Draup subscription covers.",
          "- **Check before you send.** Draup data is a strong starting point. Verify facts you put in front of a customer, especially names and numbers.",
          "- **Keep customer data private.** Don't paste confidential CRM or customer data into prompts unless your company's AI policy allows it.", ""]
    L += ["## Contributing", "", "Have a prompt that works well? See [CONTRIBUTING.md](CONTRIBUTING.md). Add it to `data/prompts.json`, run `python3 scripts/build.py`, and open a pull request.", ""]
    L += ["## License", "", "Prompts and guides: [Creative Commons Attribution 4.0](LICENSE). Scripts: [MIT](LICENSE-CODE). \"Draup\" is a trademark of its owner; this license grants no trademark rights (see [NOTICE](NOTICE)).", "",
          f"*Version {META['version']} · updated {META['updated']}*"]
    write("README.md", "\n".join(L))


def data_guide():
    L = ["# Data guide", "", "What each kind of Draup data contains, and how to read it so your answers are accurate.", ""]
    for k, v in LAYERS.items():
        ps = [p for p in PROMPTS if k in p["data"]]
        L += [f"## {v['name']}", "", v["desc"], "", f"Used by {len(ps)} prompts, for example: " + ", ".join(link(p, 'guides/x') for p in ps[:4]) + ".", ""]
    L += [(ROOT / "templates" / "data-guide-reading.md").read_text(encoding="utf-8") if (ROOT / "templates" / "data-guide-reading.md").exists() else ""]
    write("guides/data-guide.md", "\n".join(L))


def export_csv():
    f = ROOT / "data" / "prompts.csv"
    with f.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "category", "title", "outcome", "when", "roles", "data", "time", "quick_prompt", "detailed_prompt", "followups", "tips", "status"])
        for p in PROMPTS:
            w.writerow([p["id"], CATS[p["category"]]["name"], p["title"], p["outcome"], p["when"], roles_txt(p), layers_txt(p), p["time"], p["quick"], p["prompt"], " || ".join(p["followups"]), " || ".join(p["tips"]), p["status"]])


def site():
    tpl = (ROOT / "templates" / "site.html").read_text(encoding="utf-8")
    payload = {"meta": META, "prompts": PROMPTS, "playbooks": PLAYBOOKS}
    js = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    write("docs/index.html", tpl.replace("/*__DATA__*/null", js))
    write("docs/.nojekyll", "")


# ---------- print HTML for PDFs ----------
PRINT_CSS = (ROOT / "templates" / "print.css").read_text(encoding="utf-8") if (ROOT / "templates" / "print.css").exists() else ""


def h(s):
    return html.escape(s)


def pre(s):
    t = h(s)
    t = re.sub(r"\[([^\]\n]+)\]", r'<mark>[\1]</mark>', t)
    return f"<pre>{t}</pre>"


def print_doc(title, body, sub=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{h(title)}</title><style>{PRINT_CSS}</style></head><body>
<header class="cover"><div class="eyebrow">Draup Sales Prompt Library</div><h1>{h(title)}</h1><p>{h(sub)}</p><p class="ver">Version {META['version']} · {META['updated']} · {h(META['repo'])}</p></header>
{body}</body></html>"""


def print_prompt(p, full=True):
    b = [f"<article class='prompt'><h3>{h(p['title'])}</h3><p class='outcome'>{h(p['outcome'])}</p>",
         f"<p class='meta'><b>Use it when:</b> {h(p['when'])} <b>Best for:</b> {h(roles_txt(p))} <b>Time:</b> {h(p['time'])}</p>"]
    if p["status"] == "schema-only":
        b.append("<p class='note'>Needs the Draup for Talent connector. Documented, not live-tested.</p>")
    if full:
        b.append("<h4>Detailed prompt</h4>" + pre(p["prompt"]))
        b.append("<h4>Quick version</h4>" + pre(p["quick"]))
        if p["followups"]:
            b.append("<h4>Follow-ups</h4><ul>" + "".join(f"<li>{h(f)}</li>" for f in p["followups"]) + "</ul>")
        if p["tips"]:
            b.append("<h4>Tips</h4><ul>" + "".join(f"<li>{h(t)}</li>" for t in p["tips"]) + "</ul>")
    else:
        b.append(pre(p["quick"]))
    b.append("</article>")
    return "".join(b)


def print_html():
    out = ROOT / "build" / "print"
    out.mkdir(parents=True, exist_ok=True)
    # catalogue
    body = ["<section class='toc'><h2>Contents</h2><ol>" + "".join(f"<li>{h(c['name'])} <span>({len(in_cat(c['id']))})</span></li>" for c in META["categories"] if in_cat(c["id"])) + "</ol></section>"]
    for c in META["categories"]:
        ps = in_cat(c["id"])
        if not ps:
            continue
        body.append(f"<section class='cat'><h2>{h(c['name'])}</h2><p class='desc'>{h(c['desc'])}</p>" + "".join(print_prompt(p) for p in ps) + "</section>")
    (out / "catalogue.html").write_text(encoding="utf-8", data=print_doc("Full prompt catalogue", "".join(body), f"{len(PROMPTS)} detailed prompts for Claude with the Draup for Sales connector."))
    # playbooks
    if PLAYBOOKS:
        pb_body = []
        for pb in PLAYBOOKS:
            steps = "".join(f"<li><b>{h(BY_ID[s['prompt_id']]['title'])}</b>: {h(s.get('why',''))}<br><i>Look for:</i> {h(s.get('what_to_look_for',''))}{pre(BY_ID[s['prompt_id']]['quick'])}</li>" for s in pb["steps"])
            pb_body.append(f"<section class='pb'><h2>{h(pb['title'])}</h2><p class='desc'>{h(pb['goal'])}</p><p class='meta'><b>For:</b> {h(', '.join(ROLES[r]['name'] for r in pb.get('for', []) if r in ROLES))} <b>Time:</b> {h(pb.get('time',''))}</p><ol class='steps'>{steps}</ol><p><b>You finish with:</b> {h(pb.get('finish',''))}</p></section>")
        (out / "playbooks.html").write_text(encoding="utf-8", data=print_doc("Playbooks", "".join(pb_body), "Step-by-step sales workflows that chain several prompts."))
    # role sheets
    (out / "roles").mkdir(exist_ok=True)
    for code, r in ROLES.items():
        ps = [p for p in PROMPTS if code in p["roles"] and p["category"] != "setup"]
        body = "<section class='sheet'>" + "".join(f"<div class='q'><h3>{h(p['title'])}</h3>{pre(p['quick'])}</div>" for p in ps) + "</section>"
        (out / "roles" / f"{r['slug']}.html").write_text(encoding="utf-8", data=print_doc(f"Cheat sheet: {r['name']}", body, r["desc"] + " Quick versions; full prompts are in the catalogue."))
    # quick start
    qs = (ROOT / "templates" / "quick-start.html").read_text(encoding="utf-8") if (ROOT / "templates" / "quick-start.html").exists() else ""
    if qs:
        top = "".join(f"<div class='q'><h3>{h(p['title'])}</h3><p class='outcome'>{h(p['outcome'])}</p>{pre(p['quick'])}</div>" for p in featured()[:12])
        qs = qs.replace("{{START_PROMPT}}", pre(START["prompt"]) if START else "").replace("{{TOP_PROMPTS}}", top)
        (out / "quick-start.html").write_text(encoding="utf-8", data=print_doc("Quick-start guide", qs, "Get useful answers from Draup in Claude in five minutes."))


def clean():
    import shutil
    for d in ("prompts", "roles", "playbooks"):
        shutil.rmtree(ROOT / d, ignore_errors=True)


def main():
    validate()
    if "--check" in sys.argv:
        return
    clean()
    for p in PROMPTS:
        prompt_page(p)
    for c in META["categories"]:
        if in_cat(c["id"]):
            category_page(c)
    for code, r in ROLES.items():
        role_page(code, r)
    playbook_pages()
    readme()
    data_guide()
    export_csv()
    if (ROOT / "templates" / "site.html").exists():
        site()
    print_html()
    print("Built README, prompt pages, roles, playbooks, CSV, site and print HTML.")


if __name__ == "__main__":
    main()
