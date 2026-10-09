"""Fast static checks for the three paper-specific Markdown research notebooks.

These contracts prevent another agent from silently replacing theory,
simulation descriptions and careful status labelling with outdated
Val1/Val2 notes or publication-ready claims that are not supported.
"""
from pathlib import Path
import re

import pytest

ROOT=Path(__file__).resolve().parents[1]
WORKING=ROOT/"working_papers"
PAPERS={
    "Smoothness Cross Validation":"Paper 1",
    "Dynamic Branch Selection":"Paper 2",
    "Numerical Methods":"Paper 3",
}
REQUIRED_NOTES=(
    "RESEARCH_NOTEBOOK.md",
    "PROOF_LEDGER.md",
    "SIMULATION_ATLAS.md",
)


@pytest.mark.parametrize("paper",PAPERS)
def test_each_paper_has_research_narrative_proofs_and_simulation_atlas(paper):
    root=WORKING/f"Working Paper - {paper}"
    assert root.is_dir()
    index=root/"notes"/("INDEX.md" if paper=="Smoothness Cross Validation" else "README.md")
    entry=index.read_text(encoding="utf-8")
    for name in REQUIRED_NOTES:
        note=root/"notes"/name
        assert note.is_file(),note
        text=note.read_text(encoding="utf-8")
        assert len(text)>3000,(paper,name,"insufficient methodological detail")
        assert name in entry,(paper,name,"missing index link")


@pytest.mark.parametrize("paper",PAPERS)
def test_research_notes_do_not_erase_mathematical_vs_empirical_boundaries(paper):
    root=WORKING/f"Working Paper - {paper}"/"notes"
    notebook=(root/"RESEARCH_NOTEBOOK.md").read_text(encoding="utf-8").lower()
    proofs=(root/"PROOF_LEDGER.md").read_text(encoding="utf-8").lower()
    figures=(root/"SIMULATION_ATLAS.md").read_text(encoding="utf-8").lower()
    assert "h" in notebook and "s" in notebook
    assert "demostr" in proofs or "derivad" in proofs
    assert "pendiente" in proofs or "hipótesis" in proofs
    assert "ruido" in figures and ("tau" in figures or r"\tau" in figures)
    assert "pronóstico" in figures or "forecast" in figures
    assert "figura" in figures
    assert "no" in figures


def test_dynamic_tracking_never_presents_old_val2_as_current_method():
    root=WORKING/"Working Paper - Dynamic Branch Selection"/"notes"
    theory=(root/"RESEARCH_NOTEBOOK.md").read_text(encoding="utf-8").lower()
    assert "después" in theory
    assert "ponderamos" in theory
    assert "val1/val2" in theory
    assert "outer test" in theory
    assert "mismo m" in theory


def test_numerical_source_of_truth_distinguishes_known_tau_from_known_roots():
    root=WORKING/"Working Paper - Numerical Methods"/"notes"
    atlas=(root/"SIMULATION_ATLAS.md").read_text(encoding="utf-8").lower()
    assert "raíces" in atlas and "tau" in atlas
    assert "sturm" in atlas
    assert "certific" in atlas
    assert "referencia" in atlas


def test_every_new_markdown_relative_link_stays_inside_repository_and_resolves():
    documents=[WORKING/"NOTES_TO_MANUSCRIPT.md"]
    for name in PAPERS:
        notes=WORKING/f"Working Paper - {name}"/"notes"
        documents.extend(notes/file for file in REQUIRED_NOTES)
    pattern=re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for document in documents:
        raw=document.read_text(encoding="utf-8")
        for url in pattern.findall(raw):
            if url.startswith(("http://","https://","mailto:","#")):
                continue
            path=url.split("#",1)[0]
            if not path:
                continue
            linked=(document.parent/path).resolve()
            assert linked.is_file(),f"Broken link in {document}: {url}"


def test_handoff_and_shared_notes_workflow_are_linked():
    for path in (ROOT/"AGENTS.md",ROOT/"AI_HANDOFF.md",WORKING/"README.md"):
        text=path.read_text(encoding="utf-8")
        assert "NOTES_TO_MANUSCRIPT.md" in text
    handbook=(WORKING/"NOTES_TO_MANUSCRIPT.md").read_text(encoding="utf-8")
    for name in REQUIRED_NOTES:
        assert name in handbook
