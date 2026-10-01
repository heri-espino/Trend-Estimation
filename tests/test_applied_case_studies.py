from __future__ import annotations

import json
import subprocess
import sys

import pandas as pd


def test_applied_case_studies_smoke_preserves_test_separation(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "run_applied_case_studies.py"
    )
    subprocess.run(
        [
            sys.executable,
            script,
            "--preset",
            "smoke",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    selections = pd.read_csv(tmp_path / "case_selection.csv")
    candidates = pd.read_csv(tmp_path / "candidate_results.csv")
    metadata = json.loads(
        (tmp_path / "run_metadata.json").read_text(encoding="utf-8")
    )

    assert len(selections) == 1
    assert selections.loc[0, "series"] == "GDPC1"
    assert {
        "series",
        "order",
        "window",
        "horizon",
        "n_representative_candidates",
        "selection_score",
        "test_start_date",
    } <= set(selections.columns)

    assert {
        "series",
        "cv_rank",
        "smoothness",
        "cv_error",
        "test_mse",
        "test_rank",
        "delta_cv",
        "delta_test",
        "validation_test_rank_reversal",
    } <= set(candidates.columns)

    assert metadata["suite"] == "applied_multiple_minima"
    assert metadata["selection_uses_test"] is False
    assert metadata["test_role"] == "diagnostic_only"
    assert metadata["candidate_spacing_epsilon"] == 0.10

    assert (tmp_path / "objective_profiles.csv").exists()
    assert (tmp_path / "applied_paths.csv").exists()
    assert (tmp_path / "applied_case_studies.pdf").exists()
