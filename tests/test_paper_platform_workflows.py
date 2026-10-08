"""Windows produces paper figures; macOS owns LaTeX compilation."""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper_smoothness-cv"


def test_windows_preparation_never_compiles_latex():
    ps = (PAPER / "prepare-paper.ps1").read_text(encoding="utf-8")
    assert "make_workflow_tutorial_figure.py" in ps
    assert '"--check"' in ps
    assert '"-m", "pytest"' in ps
    assert "build.py" in ps
    assert "git push" not in ps  # user reviews and pushes generated figures
    assert 'Invoke-PythonStep -Label "Compile' not in ps
    assert '"paper_smoothness-cv/build.py"\n' not in ps  # unguarded call
    for forbidden in ("& pdflatex", "& latexmk", "& bibtex"):
        assert forbidden not in ps


def test_old_windows_entrypoint_is_preparation_alias_only():
    ps = (PAPER / "build-workflow-paper.ps1").read_text(encoding="utf-8")
    assert "prepare-paper.ps1" in ps
    assert "build.py" not in ps


def test_macos_only_runs_latex_build():
    sh = (PAPER / "compile-paper.sh").read_text(encoding="utf-8")
    assert "set -euo pipefail" in sh
    assert "python3 paper_smoothness-cv/build.py --check" in sh
    assert "python3 paper_smoothness-cv/build.py\n" in sh
    assert "make_workflow_tutorial_figure.py" not in sh
    assert "pytest" not in sh
    assert "pip install" not in sh
    assert "git push" not in sh
