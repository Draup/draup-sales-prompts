#!/usr/bin/env bash
# Render the print HTML (made by build.py) to PDFs with headless Chrome.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
command -v google-chrome >/dev/null 2>&1 && CHROME="${CHROME_BIN:-google-chrome}"
python3 "$ROOT/scripts/build.py"
mkdir -p "$ROOT/pdf/roles"
PROFILE="$(mktemp -d)"; trap 'rm -rf "$PROFILE"' EXIT
render() { "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --user-data-dir="$PROFILE" --print-to-pdf="$2" "file://$1" >/dev/null 2>&1; echo "wrote ${2#$ROOT/}"; }
render "$ROOT/build/print/quick-start.html" "$ROOT/pdf/draup-sales-prompts-quick-start.pdf"
render "$ROOT/build/print/catalogue.html"   "$ROOT/pdf/draup-sales-prompts-catalogue.pdf"
[ -f "$ROOT/build/print/playbooks.html" ] && render "$ROOT/build/print/playbooks.html" "$ROOT/pdf/draup-sales-prompts-playbooks.pdf"
for f in "$ROOT"/build/print/roles/*.html; do render "$f" "$ROOT/pdf/roles/$(basename "${f%.html}").pdf"; done
