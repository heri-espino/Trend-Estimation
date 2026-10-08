"""Guard the forecasting paper's plain LaTeX build against template regressions."""
from __future__ import annotations

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper_smoothness-cv"
MAIN = PAPER / "manuscript" / "main.tex"
EVALUATION = PAPER / "manuscript" / "sections" / "06_evaluation_protocol.tex"
BUILD = PAPER / "build.py"


def test_plain_article_has_no_wiley_front_matter():
    main = MAIN.read_text(encoding="utf-8")
    assert r"\documentclass[11pt]{article}" in main
    assert r"\bibliographystyle{plain}" in main
    for command in (
        r"\journal{", r"\articletype{", r"\bmsection",
        r"\authormark", r"\titlemark", r"\abstract[",
        "WileyNJDv5", r"\keywords{",
    ):
        assert command not in main
    assert r"\begin{abstract}" in main
    assert r"\end{abstract}" in main


def test_workflow_figure_uses_single_column_float():
    tex = EVALUATION.read_text(encoding="utf-8")
    assert r"\begin{figure}[p]" in tex
    assert r"\end{figure}" in tex
    assert r"\includegraphics[" in tex
    assert "{figures/fig_workflow_tutorial.pdf}" in tex
    assert r"\begin{figure*}" not in tex


def test_plain_builder_uses_standard_tools_and_preserves_frozen_figures():
    source = BUILD.read_text(encoding="utf-8")
    assert 'shutil.which("pdflatex")' in source
    assert 'shutil.which("bibtex")' in source
    assert 'shutil.copytree(SOURCE_DIR, STAGE_DIR)' in source
    assert "wiley_njd_v5" not in source
    namespace = runpy.run_path(str(BUILD), run_name="test_builder")
    namespace["validate_layout"]()
