"""Build/check the standalone Dynamic Branch Selection working manuscript.

Usage (from repository root):
    python "working_papers/Working Paper - Dynamic Branch Selection/build.py" --check
    python "working_papers/Working Paper - Dynamic Branch Selection/build.py"
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
MANUSCRIPT = HERE / "manuscript"
MAIN = MANUSCRIPT / "main.tex"
SECTIONS = (
    "01_formulation.tex",
    "02_branch_rules.tex",
    "03_experiments.tex",
    "04_discussion.tex",
)
FIGURES = (
    "fig_workflow_tutorial.pdf",
    "fig_cp08_illustrative_smoothness_selections.pdf",
    "fig_cp08_rule_clipping.pdf",
    "fig_cp08_rule_family_losses.pdf",
)


def check() -> None:
    required = [MAIN, MANUSCRIPT / "references.bib"]
    required.extend(MANUSCRIPT / "sections" / n for n in SECTIONS)
    required.extend(MANUSCRIPT / "figures" / n for n in FIGURES)
    missing = [str(x.relative_to(HERE)) for x in required if not x.is_file()]
    if missing:
        raise ValueError("Missing standalone manuscript files: " + ", ".join(missing))
    sources = [MAIN, *(MANUSCRIPT / "sections" / x for x in SECTIONS)]
    labels = set()
    refs = set()
    for p in sources:
        t = p.read_text(encoding="utf-8")
        labels.update(re.findall(r"\\label\{([^}]+)\}", t))
        for r in re.findall(r"\\(?:Cref|cref|eqref|ref)\{([^}]+)\}", t):
            refs.update(v.strip() for v in r.split(","))
    if refs - labels:
        raise ValueError("Unresolved cross-references: " + ", ".join(sorted(refs - labels)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    check()
    print("Dynamic working-paper source check passed")
    if args.check:
        return
    if not shutil.which("latexmk"):
        raise SystemExit("latexmk is required to generate the PDF.")
    out = HERE / "build"
    out.mkdir(exist_ok=True)
    subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
         f"-outdir={out}", "main.tex"],
        cwd=MANUSCRIPT,
        check=True,
    )
    print(f"Built {out / 'main.pdf'}")


if __name__ == "__main__":
    main()
