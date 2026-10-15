#!/usr/bin/env bash
# macOS / Linux: render the existing 28-figure gallery and compile the Beamer deck.
# Requires the repository's Python environment and latexmk (e.g., MacTeX).
# Historical numerical experiments in results/ are read-only.
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "$script_dir/../../.." && pwd)"

if ! command -v python >/dev/null 2>&1; then
  echo "Python is not available. Activate the trend-estimation conda environment." >&2
  exit 1
fi
if ! command -v latexmk >/dev/null 2>&1; then
  echo "latexmk is not available. Install MacTeX or a TeX distribution that includes latexmk." >&2
  exit 1
fi

echo "[1/2] Generating presentation figures from existing frozen results..."
cd "$repo_root"
python "$script_dir/build_figures.py" --group all --format pdf

echo "[2/2] Compiling the LaTeX Beamer presentation..."
cd "$script_dir"
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build slides.tex
cp -f build/slides.pdf Numerical_Methods_Presentation.pdf

echo
echo "Presentation ready:"
echo "$script_dir/Numerical_Methods_Presentation.pdf"
echo "On macOS, open it with:"
echo "open \"$script_dir/Numerical_Methods_Presentation.pdf\""
