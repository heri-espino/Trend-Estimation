from pathlib import Path

import pytest

from tools.rename_literature_files import (
    MigrationError,
    apply_plan,
    plan_migration,
    split_managed_name,
    swap_core,
)


def test_swap_core_uses_simultaneous_translation() -> None:
    assert (
        swap_core("Baxter_1999_approximate-band-pass-filters")
        == "Baxter-1999-approximate_band_pass_filters"
    )
    assert (
        swap_core("Islas-Camargo_2019_forecasting-remittances-mexico")
        == "Islas_Camargo-2019-forecasting_remittances_mexico"
    )


def test_split_managed_name_is_idempotent_and_preserves_reference_suffix() -> None:
    assert split_managed_name(
        Path("Baxter_1999_approximate-band-pass-filters.references.md"),
        "references",
    ) == (
        "Baxter_1999_approximate-band-pass-filters",
        ".references.md",
    )
    assert (
        split_managed_name(
            Path("Baxter-1999-approximate_band_pass_filters.md"),
            "extracted",
        )
        is None
    )


def _make_fixture(repo: Path) -> None:
    for name in ("pdf", "extracted", "references"):
        (repo / "literature" / name).mkdir(parents=True)

    old = "Baxter_1999_approximate-band-pass-filters"
    (repo / "literature" / "pdf" / f"{old}.pdf").write_bytes(b"%PDF-test")
    (repo / "literature" / "extracted" / f"{old}.md").write_text(
        "\n".join(
            [
                "---",
                f'id: "{old}"',
                f'source_pdf: "../pdf/{old}.pdf"',
                f'source_filename: "{old}.pdf"',
                f'references_file: "../references/{old}.references.md"',
                "---",
                "Scientific prose-with-hyphens stays unchanged.",
            ]
        ),
        encoding="utf-8",
    )
    (repo / "literature" / "references" / f"{old}.references.md").write_text(
        f'---\nid: "{old}-references"\nsource_pdf: "../pdf/{old}.pdf"\n---\n',
        encoding="utf-8",
    )
    (repo / "notes").mkdir()
    (repo / "notes" / "literature.md").write_text(
        f"See `literature/extracted/{old}.md`.\n",
        encoding="utf-8",
    )


def test_plan_and_apply_update_files_metadata_and_repo_references(tmp_path: Path) -> None:
    _make_fixture(tmp_path)

    plan = plan_migration(tmp_path)
    assert len(plan.renames) == 3
    assert len(plan.text_edits) == 3

    apply_plan(plan)

    new = "Baxter-1999-approximate_band_pass_filters"
    extracted = tmp_path / "literature" / "extracted" / f"{new}.md"
    assert extracted.exists()
    text = extracted.read_text(encoding="utf-8")
    assert f'id: "{new}"' in text
    assert f'source_pdf: "../pdf/{new}.pdf"' in text
    assert f'references_file: "../references/{new}.references.md"' in text
    assert "Scientific prose-with-hyphens stays unchanged." in text
    assert new in (tmp_path / "notes" / "literature.md").read_text(encoding="utf-8")

    second_plan = plan_migration(tmp_path)
    assert not second_plan.renames
    assert not second_plan.text_edits


def test_plan_rejects_existing_destination(tmp_path: Path) -> None:
    _make_fixture(tmp_path)
    destination = (
        tmp_path
        / "literature"
        / "pdf"
        / "Baxter-1999-approximate_band_pass_filters.pdf"
    )
    destination.write_bytes(b"occupied")

    with pytest.raises(MigrationError, match="already exists"):
        plan_migration(tmp_path)
