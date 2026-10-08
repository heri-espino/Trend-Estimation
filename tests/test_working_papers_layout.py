"""Structural regression tests for exactly three independent working papers."""
from __future__ import annotations

from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]
WP = ROOT / "working_papers"
NAMES = {
    "Working Paper - Smoothness Cross Validation",
    "Working Paper - Numerical Methods",
    "Working Paper - Dynamic Branch Selection",
}


def test_three_independent_directories_exist_and_legacy_roots_are_gone():
    actual = {p.name for p in WP.iterdir() if p.is_dir()}
    assert actual == NAMES
    assert (ROOT / "ideas" / "README.md").is_file()
    assert not list(ROOT.glob("paper_*"))
    for name in NAMES:
        assert (WP / name / "README.md").is_file()


def test_each_manuscript_is_standalone():
    pooled = (WP / "Working Paper - Smoothness Cross Validation" / "manuscript/main.tex")
    numeric = (WP / "Working Paper - Numerical Methods" / "main.tex")
    dynamic = (WP / "Working Paper - Dynamic Branch Selection" / "manuscript/main.tex")
    for f in (pooled, numeric, dynamic):
        assert f.is_file()
        source = f.read_text(encoding="utf-8")
        assert r"\begin{document}" in source and r"\end{document}" in source
        assert r"\bibliography{" in source

    psrc = pooled.read_text(encoding="utf-8")
    dsrc = dynamic.read_text(encoding="utf-8")
    nsrc = numeric.read_text(encoding="utf-8")
    assert "05_dynamic_extension" not in psrc
    assert "09_exploratory_evaluation" not in psrc
    assert "02_branch_rules" in dsrc
    assert "03_experiments" in dsrc
    assert r"\section{Temporal correspondence of local minima}" not in nsrc


def test_historical_checkpoints_are_distinct_and_complete():
    pooled = WP / "Working Paper - Smoothness Cross Validation" / "checkpoints"
    dynamic = WP / "Working Paper - Dynamic Branch Selection" / "checkpoints"
    for i in (1, 2, 3):
        assert list(pooled.glob(f"CP{i:02d}_*.md"))
        assert not list(dynamic.glob(f"CP{i:02d}_*.md"))
    for i in (4, 5, 6, 7, 8):
        assert not list(pooled.glob(f"CP{i:02d}_*.md"))
        assert list(dynamic.glob(f"CP{i:02d}_*.md"))
    assert (dynamic / "NUMERICAL_TRACKING_CP05_UNRUN.md").is_file()


def test_dynamic_paper_preflight_checks_all_local_inputs():
    builder = WP / "Working Paper - Dynamic Branch Selection" / "build.py"
    runpy.run_path(str(builder), run_name="test_dynamic_builder")["check"]()
