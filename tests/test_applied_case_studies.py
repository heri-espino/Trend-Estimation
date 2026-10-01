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
    long_selection = pd.read_csv(
        tmp_path / "long_horizon_order_selection.csv"
    )
    long_candidates = pd.read_csv(
        tmp_path / "long_horizon_order_candidates.csv"
    )
    long_paths = pd.read_csv(
        tmp_path / "long_horizon_order_paths.csv"
    )
    protocol = pd.read_csv(
        tmp_path / "temporal_split_protocol.csv",
        parse_dates=[
            "train_start_date",
            "train_end_date",
            "validation_start_date",
            "validation_end_date",
            "development_start_date",
            "development_end_date",
            "final_train_start_date",
            "final_train_end_date",
            "test_start_date",
            "test_end_date",
            "scored_test_start_date",
            "scored_test_end_date",
        ],
    )
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
    assert metadata["long_horizon_diagnostic"]["orders"] == [1, 2, 3, 4]
    assert metadata["long_horizon_diagnostic"]["test_role"].startswith(
        "visual diagnostic"
    )

    assert set(long_selection["order"]) == {1, 2, 3, 4}
    assert set(long_selection["horizon"]) == {8}
    assert set(long_candidates["order"]) == {1, 2, 3, 4}
    assert {"order", "window", "horizon", "smoothness", "cv_rank"} <= set(
        long_candidates.columns
    )
    assert {"order", "window", "horizon", "segment", "candidate_path"} <= set(
        long_paths.columns
    )
    assert set(long_paths["segment"]) == {"train", "test"}

    assert not protocol.empty
    assert (protocol["validation_end_date"] <= protocol["development_end_date"]).all()
    assert (protocol["train_end_date"] < protocol["validation_start_date"]).all()
    assert (protocol["final_train_end_date"] == protocol["development_end_date"]).all()
    assert (protocol["development_end_date"] < protocol["test_start_date"]).all()
    assert (protocol["scored_test_end_date"] <= protocol["test_end_date"]).all()

    assert (tmp_path / "objective_profiles.csv").exists()
    assert (tmp_path / "applied_paths.csv").exists()
    assert (tmp_path / "long_horizon_order_selection.csv").exists()
    assert (tmp_path / "long_horizon_order_candidates.csv").exists()
    assert (tmp_path / "long_horizon_order_paths.csv").exists()
    assert (tmp_path / "temporal_split_protocol.csv").exists()
    assert (tmp_path / "applied_case_studies.pdf").exists()
    assert (tmp_path / "temporal_split.pdf").exists()

    # Figure-only mode must reuse the frozen CSV results rather than rerun
    # configuration or smoothness selection.
    (tmp_path / "applied_case_studies.pdf").unlink()
    (tmp_path / "temporal_split.pdf").unlink()
    subprocess.run(
        [
            sys.executable,
            script,
            "--figures-from-run",
            str(tmp_path),
        ],
        check=True,
    )
    assert (tmp_path / "applied_case_studies.pdf").exists()
    assert (tmp_path / "temporal_split.pdf").exists()
