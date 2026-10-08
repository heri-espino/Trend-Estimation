"""Pooled forecasting article is self-contained and does not build dynamic appendices."""
from __future__ import annotations

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "working_papers" / "Working Paper - Smoothness Cross Validation"
MAIN = PAPER / "manuscript" / "main.tex"
BUILD = PAPER / "build.py"


def test_article_has_no_wiley_front_matter_or_dynamic_appendices():
    source = MAIN.read_text(encoding="utf-8")
    assert r"\documentclass[11pt]{article}" in source
    assert r"\bibliographystyle{plainnat}" in source
    assert r"\usepackage[round,authoryear]{natbib}" in source
    assert r"\input{sections/03_penalized_trend}" in source
    assert r"\input{sections/05_properties}" in source
    assert "WileyNJDv5" not in source
    assert r"\input{sections/05_dynamic_extension}" not in source
    assert r"\input{sections/09_exploratory_evaluation}" not in source
    assert r"\appendix" not in source


def test_plain_builder_keeps_cp03_evidence_and_has_valid_section_labels():
    source = BUILD.read_text(encoding="utf-8")
    assert 'shutil.which("pdflatex")' in source
    assert 'shutil.which("bibtex")' in source
    assert 'shutil.copytree(SOURCE_DIR, STAGE_DIR)' in source
    assert "fig_sim05_objective_curves.pdf" in source
    assert "fig_cp08_" not in source
    namespace = runpy.run_path(str(BUILD), run_name="test_builder")
    namespace["validate_layout"]()
