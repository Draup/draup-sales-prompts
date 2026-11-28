#!/usr/bin/env bash
# Render the one-page IT brief(s) to PDF with headless Chrome.
# Writes pdf/draup-for-sales-connector-it-brief.pdf and pdf/draup-for-talent-connector-it-brief.pdf
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
command -v google-chrome >/dev/null 2>&1 && CHROME="${CHROME_BIN:-google-chrome}"
python3 "$ROOT/scripts/it_brief.py"
PROFILE="$(mktemp -d)"; trap 'rm -rf "$PROFILE"' EXIT
render() { "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --user-data-dir="$PROFILE" --print-to-pdf="$2" "file://$1" >/dev/null 2>&1; echo "wrote $2"; }
mkdir -p "$ROOT/pdf"
render "$ROOT/build/print/it-brief-sales.html" "$ROOT/pdf/draup-for-sales-connector-it-brief.pdf"
render "$ROOT/build/print/it-brief-talent.html" "$ROOT/pdf/draup-for-talent-connector-it-brief.pdf"
