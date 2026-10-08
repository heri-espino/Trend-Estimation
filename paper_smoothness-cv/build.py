#!/usr/bin/env python3
"""Build the plain, single-column LaTeX forecasting manuscript.

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
import re

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
WORKFLOW_FIGURE = SOURCE_DIR / "figures" / "fig_workflow_tutorial.pdf"
WORKFLOW_GENERATOR = (
    "python experiments/smoothness_cv/make_workflow_tutorial_figure.py"
)
BUILD_DIR = PAPER_DIR / "build"
STAGE_DIR = BUILD_DIR / "stage"
MAIN_TEX = SOURCE_DIR / "main.tex"
FINAL_PDF = PAPER_DIR / "EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf"

EXPECTED_CLASS = r"\documentclass[11pt]{article}"


def validate_layout() -> None:
    required = [MAIN_TEX, SOURCE_DIR / "references.bib"]
    missing = [p.relative_to(PAPER_DIR) for p in required if not p.is_file()]
    if missing:
        raise SystemExit(
            "Manuscript layout check failed; missing:\n- "
            + "\n- ".join(map(str, missing))
        )

    source = MAIN_TEX.read_text(encoding="utf-8")
    if EXPECTED_CLASS not in source:
        raise SystemExit("main.tex must use " + EXPECTED_CLASS)
    for removed_command in (
        r"\journal{", r"\articletype{", r"\bmsection",
        r"\documentclass[APA,Utopia2COL]{WileyNJDv5}",
    ):
        if removed_command in source:
            raise SystemExit(
                f"main.tex still has a Wiley-specific command: {removed_command}"
            )

    expected_sections = (
        "01_introduction.tex",
        "02_related_work.tex",
        "03_penalized_trend.tex",
        "04_forecast_optimal_smoothness.tex",
        "05_properties.tex",
        "06_evaluation_protocol.tex",
        "07_empirical_evidence.tex",
        "07_scope_and_implications.tex",
        "08_conclusion.tex",
    )
    missing_sections = [
        name for name in expected_sections
        if not (SOURCE_DIR / "sections" / name).is_file()
    ]
    if missing_sections:
        raise SystemExit(
            "Missing manuscript sections:\n- " + "\n- ".join(missing_sections)
        )

    if not WORKFLOW_FIGURE.is_file():
        raise SystemExit(
            f"Missing workflow tutorial figure: {WORKFLOW_FIGURE}. "
            f"From the repository root, run: {WORKFLOW_GENERATOR}"
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
    shutil.copytree(SOURCE_DIR, STAGE_DIR)
    staged_figures = STAGE_DIR / "figures"
    staged_figures.mkdir(parents=True, exist_ok=True)
    for name in FIGURE_NAMES:
        shutil.copy2(FIGURE_SOURCE_DIR / name, staged_figures / name)


def run(command: list[str]) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=STAGE_DIR, check=True)


def first_latex_error_context(log_text: str, *, before: int = 5, after: int = 16) -> str:
    """Return first fatal TeX error, not latexmk's final wrapper status."""
    lines = log_text.splitlines()
    triggers = (
        re.compile(r"^!\s"),
        re.compile(r"(?:^|[/\\])[^:\s]+\.tex:\d+:\s"),
        re.compile(r"^(?:LaTeX|Package [\w.-]+)\s+Error:"),
        re.compile(r"^Emergency stop\."),
    )
    for idx, line in enumerate(lines):
        if any(pattern.search(line) for pattern in triggers):
            start = max(0, idx - before)
            stop = min(len(lines), idx + after + 1)
            return "\n".join(
                f"{line_no + 1:>5}: {lines[line_no]}"
                for line_no in range(start, stop)
            )
    return ""


def report_latex_failure() -> None:
    log_path = STAGE_DIR / "main.log"
    print("\n=== First LaTeX error ===", file=sys.stderr)
    if not log_path.exists():
        print(
            f"No main.log found at {log_path}; inspect the command output above.",
            file=sys.stderr,
        )
        return
    log = log_path.read_text(encoding="utf-8", errors="replace")
    excerpt = first_latex_error_context(log)
    if not excerpt:
        excerpt = "\n".join(log.splitlines()[-35:])
        print(
            "No standard TeX error marker found; last 35 log lines:",
            file=sys.stderr,
        )
    print(excerpt, file=sys.stderr)
    print(f"\nFull log: {log_path}", file=sys.stderr)
    print(
        "To print this again without rebuilding: "
        "python3 paper_smoothness-cv/build.py --diagnose",
        file=sys.stderr,
    )


def build() -> Path:
    validate_layout()
    prepare_stage()

    pdflatex = shutil.which("pdflatex")
    bibtex = shutil.which("bibtex")
    latexmk = shutil.which("latexmk")
    if not pdflatex or not bibtex:
        raise SystemExit(
            "A standard LaTeX installation with pdflatex and bibtex "
            "is required. Run with --check to validate sources only."
        )

    if latexmk:
        run([
            latexmk, "-pdf", "-interaction=nonstopmode",
            "-halt-on-error", "-file-line-error", "main.tex",
        ])
    else:
        common = [
            pdflatex, "-interaction=nonstopmode",
            "-halt-on-error", "-file-line-error", "main.tex",
        ]
        run(common)
        run([bibtex, "main"])
        run(common)
        run(common)

    staged_pdf = STAGE_DIR / "main.pdf"
    if not staged_pdf.is_file():
        raise SystemExit("Compilation finished without main.pdf")
    shutil.copy2(staged_pdf, FINAL_PDF)
    print(f"Built {FINAL_PDF}")
    return FINAL_PDF


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--diagnose", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.clean:
        clean()
        if not args.check:
            return 0
    if args.diagnose:
        report_latex_failure()
        return 0
    if args.check:
        validate_layout()
        print("Standard article LaTeX layout check passed")
        return 0
    try:
        build()
    except subprocess.CalledProcessError as exc:
        report_latex_failure()
        print(
            f"\nLaTeX compilation failed (exit code {exc.returncode}). "
            "Fix the first error above, then rerun the macOS build.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
