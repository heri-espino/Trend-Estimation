"""Validate/build the INCOMPLETE mean-difference forecasting working manuscript.

This script is MANUAL ONLY; do not run PDF builds in automatic CI.

From repository root:
  python "working_papers/Working Paper - Trend Simulation and Mean-Difference Forecasting/build.py" --check
  python "working_papers/Working Paper - Trend Simulation and Mean-Difference Forecasting/build.py"
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess

BASE=Path(__file__).resolve().parent
MANUSCRIPT=BASE/"manuscript"
SECTIONS=(
    "01_introduction.tex",
    "02_model.tex",
    "03_theory.tex",
    "04_simulation.tex",
    "05_discussion.tex",
)


def check():
    files=[
        MANUSCRIPT/"main.tex",MANUSCRIPT/"references.bib",
        *(MANUSCRIPT/"sections"/x for x in SECTIONS),
    ]
    missing=[str(x.relative_to(BASE)) for x in files if not x.is_file()]
    if missing:
        raise FileNotFoundError("Missing working manuscript parts: "+", ".join(missing))
    print("Working-paper scaffold present (not a scientific/publishing acceptance test).")


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check",action="store_true")
    opts=p.parse_args(argv)
    check()
    if opts.check:
        return
    if not shutil.which("latexmk"):
        raise RuntimeError("Install latexmk/TeX Live/MiKTeX for manual builds.")
    output=BASE/"build"
    output.mkdir(exist_ok=True)
    subprocess.run(
        ["latexmk","-pdf","-interaction=nonstopmode","-halt-on-error",
         f"-outdir={output}","main.tex"],
        cwd=MANUSCRIPT,check=True
    )
    print("Working draft built:",output/"main.pdf")


if __name__=="__main__":
    main()
