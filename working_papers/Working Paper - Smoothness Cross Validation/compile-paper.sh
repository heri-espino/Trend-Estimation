#!/usr/bin/env bash
# macOS: compile LaTeX ONLY. All figures are generated and committed on Windows.
# From the repository root: bash working_papers/Working Paper - Smoothness Cross Validation/compile-paper.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 is required." >&2
  exit 1
fi
if ! command -v pdflatex >/dev/null 2>&1; then
  echo "ERROR: pdflatex was not found. Install/activate a MacTeX distribution." >&2
  exit 1
fi
if ! command -v bibtex >/dev/null 2>&1; then
  echo "ERROR: bibtex was not found. Install/activate a TeX distribution." >&2
  exit 1
fi

echo "=== Validate committed LaTeX sources and figures ==="
python3 "working_papers/Working Paper - Smoothness Cross Validation/build.py" --check

echo "=== Compile standard article using pdflatex/BibTeX ==="
python3 "working_papers/Working Paper - Smoothness Cross Validation/build.py"

PDF="working_papers/Working Paper - Smoothness Cross Validation/EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf"
if [[ ! -s "$PDF" ]]; then
  echo "ERROR: compiled PDF not found or empty: $PDF" >&2
  exit 1
fi

echo
echo "macOS LaTeX compilation complete: $PDF"
echo "Review the PDF, commit it and push the result to GitHub."
git status --short
