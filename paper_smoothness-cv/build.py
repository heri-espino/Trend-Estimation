#!/usr/bin/env python3
"""Build the Journal of Forecasting smoothness-CV manuscript.

Usage
-----
python paper_smoothness-cv/build.py
python paper_smoothness-cv/build.py --check
python paper_smoothness-cv/build.py --clean
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys

PAPER_DIR = Path(__file__).resolve().parent
SOURCE_DIR = PAPER_DIR / "manuscript"
FIGURE_SOURCE_DIR = (
    PAPER_DIR.parent
    / "results"
    / "smoothness_cv"
    / "checkpoint_08"
    / "20261007T072243Z_paper_be492a8"
    / "paper_artifacts"
    / "figures"
)
FIGURE_NAMES = (
    "fig_cp08_illustrative_smoothness_selections.pdf",
    "fig_cp08_rule_clipping.pdf",
    "fig_cp08_rule_family_losses.pdf",
)
VENDOR_DIR = PAPER_DIR / "vendor" / "wiley_njd_v5"
BUILD_DIR = PAPER_DIR / "build"
STAGE_DIR = BUILD_DIR / "stage"
MAIN_TEX = SOURCE_DIR / "main.tex"
FINAL_PDF = PAPER_DIR / "EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf"

EXPECTED_CLASS = r"\documentclass[APA,Utopia2COL]{WileyNJDv5}"
EXPECTED_JOURNAL = r"\journal{Journal of Forecasting}"
LEGACY_RESERVE_INSERTS = r"\reserveinserts{28}"
GUARDED_RESERVE_INSERTS = r"\ifdefined\reserveinserts\reserveinserts{28}\fi"


def validate_layout() -> None:
    required = [
        MAIN_TEX,
        SOURCE_DIR / "references.bib",
        VENDOR_DIR / "WileyNJDv5.cls",
        VENDOR_DIR / "wileyNJD-Harvard.bst",
    ]
    missing = [p.relative_to(PAPER_DIR) for p in required if not p.exists()]
    if missing:
        raise SystemExit(
            "Manuscript layout check failed; missing:\n- "
            + "\n- ".join(map(str, missing))
        )

    source = MAIN_TEX.read_text(encoding="utf-8")
    if EXPECTED_CLASS not in source:
        raise SystemExit("main.tex must use " + EXPECTED_CLASS)
    if EXPECTED_JOURNAL not in source:
        raise SystemExit("main.tex must identify Journal of Forecasting")

    expected_sections = [
        "01_introduction.tex",
        "02_related_work.tex",
        "03_penalized_trend.tex",
        "04_forecast_optimal_smoothness.tex",
        "05_properties.tex",
        "06_evaluation_protocol.tex",
        "07_empirical_evidence.tex",
        "07_scope_and_implications.tex",
        "08_conclusion.tex",
    ]
    missing_sections = [
        name for name in expected_sections
        if not (SOURCE_DIR / "sections" / name).exists()
    ]
    if missing_sections:
        raise SystemExit(
            "Missing manuscript sections:\n- " + "\n- ".join(missing_sections)
        )

    missing_figures = [
        name for name in FIGURE_NAMES
        if not (FIGURE_SOURCE_DIR / name).is_file()
    ]
    if missing_figures:
        raise SystemExit(
            "Missing CP08 figures; run "
            "'python experiments/smoothness_cv/make_checkpoint_08_figures.py' "
            "from the repository root, then retry. Missing:\n- "
            + "\n- ".join(missing_figures)
        )


def clean() -> None:
    shutil.rmtree(BUILD_DIR, ignore_errors=True)
    FINAL_PDF.unlink(missing_ok=True)


def prepare_stage() -> None:
    if STAGE_DIR.exists():
        shutil.rmtree(STAGE_DIR)
    STAGE_DIR.parent.mkdir(parents=True, exist_ok=True)

    shutil.copytree(VENDOR_DIR, STAGE_DIR)
    shutil.copytree(SOURCE_DIR, STAGE_DIR, dirs_exist_ok=True)

    staged_figures = STAGE_DIR / "figures"
    staged_figures.mkdir(parents=True, exist_ok=True)
    for name in FIGURE_NAMES:
        shutil.copy2(FIGURE_SOURCE_DIR / name, staged_figures / name)

    staged_class = STAGE_DIR / "WileyNJDv5.cls"
    source = staged_class.read_text(encoding="utf-8")
    if LEGACY_RESERVE_INSERTS in source:
        staged_class.write_text(
            source.replace(LEGACY_RESERVE_INSERTS, GUARDED_RESERVE_INSERTS),
            encoding="utf-8",
        )

    # Prefer the TeX distribution's internally consistent listings package.
    (STAGE_DIR / "listings.sty").unlink(missing_ok=True)


def run(command: list[str]) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=STAGE_DIR, check=True)


def build() -> Path:
    validate_layout()
    prepare_stage()

    latexmk = shutil.which("latexmk")
    xelatex = shutil.which("xelatex")
    bibtex = shutil.which("bibtex")

    if latexmk and xelatex:
        run([
            latexmk,
            "-xelatex",
            "-bibtex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            "main.tex",
        ])
    elif xelatex and bibtex:
        common = [
            xelatex,
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            "main.tex",
        ]
        run(common)
        run([bibtex, "main"])
        run(common)
        run(common)
    else:
        raise SystemExit(
            "XeLaTeX toolchain not found. Install xelatex and bibtex "
            "(latexmk recommended), or run with --check."
        )

    staged_pdf = STAGE_DIR / "main.pdf"
    if not staged_pdf.exists():
        raise SystemExit("Compilation finished without main.pdf")

    FINAL_PDF.unlink(missing_ok=True)
    shutil.copy2(staged_pdf, FINAL_PDF)
    print(f"Built {FINAL_PDF}")
    return FINAL_PDF


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--clean", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.clean:
        clean()
        if not args.check:
            return 0
    if args.check:
        validate_layout()
        print("Journal of Forecasting manuscript layout check passed")
        return 0
    build()
    return 0


if __name__ == "__main__":
    sys.exit(main())
