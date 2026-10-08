"""The macOS LaTeX build must surface the first TeX error, not only latexmk status."""
from __future__ import annotations

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "paper_smoothness-cv" / "build.py"
first_latex_error_context = runpy.run_path(
    str(BUILDER), run_name="test_latex_diagnostics"
)["first_latex_error_context"]


def test_picks_first_file_line_error_not_last_latexmk_wrapper():
    log = (
        "This is pdfTeX\n"
        "(./main.tex\n"
        "some earlier log line\n"
        "./sections/04_forecast_optimal_smoothness.tex:118: Undefined control sequence.\n"
        "l.118 \\foo\n"
        "!  ==> Fatal error occurred, no output PDF file produced!\n"
        "Latexmk: Errors, so I did not complete making targets\n"
    )
    excerpt = first_latex_error_context(log)
    assert "04_forecast_optimal_smoothness.tex:118:" in excerpt
    assert "l.118" in excerpt


def test_picks_first_bang_error():
    log = (
        "LaTeX2e\n"
        "! Missing $ inserted.\n"
        "<inserted text> $\n"
        "l.42 text\n"
        "! Emergency stop.\n"
    )
    excerpt = first_latex_error_context(log)
    assert "Missing $ inserted" in excerpt
    assert "l.42" in excerpt


def test_no_false_error_for_warning_only():
    assert first_latex_error_context(
        "LaTeX Warning: Label(s) may have changed.\nOutput written on main.pdf."
    ) == ""
