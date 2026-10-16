"""Static guards for the numerical-methods Beamer source.

In particular, JS-generated LaTeX must never lose a backslash before
\varepsilon (which previously introduced an invisible U+000B character).
"""
from __future__ import annotations

from pathlib import Path
import re

PRESENTATION = (
    Path(__file__).resolve().parents[1]
    / "working_papers"
    / "Working Paper - Numerical Methods"
    / "presentation"
)


def test_beamer_source_has_no_control_characters_or_damaged_math() -> None:
    source = (PRESENTATION / "slides.tex").read_text(encoding="utf-8")
    unexpected = sorted({
        ord(char)
        for char in source
        if ord(char) < 32 and char not in "\t\n\r"
    })
    assert not unexpected, f"Unexpected Unicode control codes: {unexpected}"

    damaged = (
        "$S(lambda)$",
        "$lambdain",
        "$Sin[0,1]$",
        "$mathrm{",
        "$ker D_d$",
        "$lambda$",
        "$Sapprox",
        "$\u000barepsilon",
        "candidate_results.csv",  # underscore requires escaping in LaTeX text mode
    )
    for fragment in damaged:
        assert fragment not in source, f"Damaged LaTeX in slide deck: {fragment!r}"

    assert r"$\varepsilon" in source
    assert r"$S(\lambda)$" in source
    assert r"\mathrm{EDF}" in source


def test_beamer_includes_all_28_distinct_figure_ids() -> None:
    source = (PRESENTATION / "slides.tex").read_text(encoding="utf-8")
    ids = re.findall(r"\\FigureSlide\{([0-9]{2}_[a-z0-9_]+)\}", source)
    assert len(ids) == 28
    assert len(set(ids)) == 28
    assert [int(name[:2]) for name in ids] == list(range(1, 29))
    for name in ids:
        assert (PRESENTATION / "STORYBOARD.md").read_text(encoding="utf-8").find(name) >= 0


def test_beamer_build_scripts_exist_for_mac_and_windows() -> None:
    assert (PRESENTATION / "build_all.sh").is_file()
    assert (PRESENTATION / "build_all.ps1").is_file()
    assert (PRESENTATION / "build_figures.py").is_file()
