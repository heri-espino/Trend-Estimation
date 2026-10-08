"""Independent paper build entry points preserve the manual-only build policy."""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "working_papers" / "Working Paper - Smoothness Cross Validation"


def test_windows_preparation_is_check_only():
    ps = (PAPER / "prepare-paper.ps1").read_text(encoding="utf-8")
    assert '"--check"' in ps
    assert '"-m","pytest"' in ps
    assert "build.py" in ps
    assert "make_workflow_tutorial_figure.py" not in ps
    assert "git push" not in ps
    assert "pdflatex" not in ps
    assert "latexmk" not in ps


def test_windows_legacy_alias_runs_only_preparation():
    ps = (PAPER / "build-workflow-paper.ps1").read_text(encoding="utf-8")
    assert "prepare-paper.ps1" in ps
    assert "build.py" not in ps


def test_macos_compile_script_resolves_repo_root_and_quotes_paths():
    sh = (PAPER / "compile-paper.sh").read_text(encoding="utf-8")
    assert "set -euo pipefail" in sh
    assert '/../..' in sh
    assert 'python3 "working_papers/Working Paper - Smoothness Cross Validation/build.py" --check' in sh
    assert 'python3 "working_papers/Working Paper - Smoothness Cross Validation/build.py"' in sh
    assert "make_workflow_tutorial_figure.py" not in sh
    assert "pytest" not in sh
    assert "git push" not in sh


def test_pdf_github_workflow_is_manual_and_three_targets():
    yml = (ROOT / ".github/workflows/build-papers.yml").read_text(encoding="utf-8")
    assert "workflow_dispatch:" in yml
    assert "  push:" not in yml
    for target in ("smoothness-cv", "numerical", "branches"):
        assert f"          - {target}" in yml
    assert "paper_smoothness-cv/" not in yml
