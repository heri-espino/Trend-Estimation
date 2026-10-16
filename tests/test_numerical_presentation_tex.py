r"""Static guards for the numerical-methods Beamer source.

In particular, JS-generated LaTeX must never lose a backslash before
\varepsilon (which previously introduced an invisible U+000B character).
"""
from __future__ import annotations

from pathlib import Path
import re
import ast

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


def test_spanish_presentation_text_and_plotting_sources() -> None:
    source = (PRESENTATION / "slides.tex").read_text(encoding="utf-8")
    assert r"\usepackage[spanish,es-nodecimaldot]{babel}" in source
    assert "Interpretación." in source
    assert "Validación cruzada cronológica" in source
    assert "¿Qué resultados hemos obtenido?" in source
    assert "Figura pendiente de generar" in source
    assert "Figure not yet rendered" not in source

    for module_name in (
        "figures_concepts.py",
        "figures_algorithm.py",
        "figures_benchmarks.py",
        "figures_applied.py",
    ):
        src = (PRESENTATION / module_name).read_text(encoding="utf-8")
        ast.parse(src, filename=module_name)
        assert "fijado_csv" not in src, "Do not translate Python function names."
        assert "pd.Tiempostamp" not in src, "Do not translate Pandas class names."
        assert "  |  " in src, "Every figure title should have a numbered heading."
        assert not any(ord(c) < 32 and c not in "\t\n\r" for c in src)
