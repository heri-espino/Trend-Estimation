"""The pooled LaTeX builder diagnoses the first fatal TeX error."""
from __future__ import annotations

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "working_papers" / "Working Paper - Smoothness Cross Validation" / "build.py"
first_latex_error_context = runpy.run_path(
    str(BUILDER), run_name="test_latex_diagnostics"
)["first_latex_error_context"]


def test_first_file_line_error():
    log = (
        "This is pdfTeX\n(./main.tex\nsome earlier log line\n"
        "./sections/04_forecast_optimal_smoothness.tex:118: Undefined control sequence.\n"
        "l.118 \\foo\n! Fatal error occurred!\nLatexmk: Errors\n"
    )
    excerpt = first_latex_error_context(log)
    assert "04_forecast_optimal_smoothness.tex:118:" in excerpt
    assert "l.118" in excerpt


def test_first_bang_error():
    excerpt = first_latex_error_context(
        "LaTeX2e\n! Missing $ inserted.\n<inserted text> $\nl.42 text\n! Emergency stop.\n"
    )
    assert "Missing $ inserted" in excerpt and "l.42" in excerpt


def test_warning_is_not_error():
    assert first_latex_error_context(
        "LaTeX Warning: Label(s) may have changed.\nOutput written on main.pdf."
    ) == ""
