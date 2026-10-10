"""Regression tests for the mathematical wiki graph and Obsidian math."""

from tools.validate_wiki import ROOT, WIKI, _frontmatter, validate


def test_wiki_integrity():
    assert validate() == []


def test_each_result_has_independent_reciprocal_proof():
    errors = []
    results = sorted((WIKI / "resultados").glob("RES-*.md"))
    assert len(results) >= 12
    for result in results:
        meta, _ = _frontmatter(result, errors)
        proof_id = meta["prueba"].strip("[]")
        assert (WIKI / "demostraciones" / (proof_id + ".md")).is_file()
        proof_meta, _ = _frontmatter(WIKI / "demostraciones" / (proof_id + ".md"), errors)
        assert proof_meta["resultado"] == f"[[{meta['id']}]]"
    assert errors == []


def test_sources_are_in_repository():
    references = sorted((WIKI / "literatura").glob("LIT-*.md"))
    assert len(references) >= 10
    for source in references:
        meta, _ = _frontmatter(source, [])
        assert (ROOT / meta["origen_repo"]).is_file()
        assert (ROOT / meta["extraccion_repo"]).is_file()
