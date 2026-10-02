from __future__ import annotations

import json
import subprocess
import sys

import pandas as pd


def test_tracked_minima_smoke_keeps_true_test_untouched(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "run_two_stage_order_validation.py"
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

    windows = pd.read_csv(tmp_path / "order_window_selection.csv")
    tracks = pd.read_csv(
        tmp_path / "rolling_minimum_tracks.csv",
        parse_dates=[
            "val1_start_date",
            "val1_end_date",
            "val2_start_date",
            "val2_end_date",
        ],
    )
    validation_paths = pd.read_csv(
        tmp_path / "rolling_validation_paths.csv",
        parse_dates=["date"],
    )
    selection = pd.read_csv(tmp_path / "tracked_branch_selection.csv")
    test_paths = pd.read_csv(
        tmp_path / "tracked_branch_test_paths.csv",
        parse_dates=["date"],
    )
    metadata = json.loads(
        (tmp_path / "run_metadata.json").read_text(encoding="utf-8")
    )

    assert set(windows["series"]) == {"GDPC1"}
    assert set(windows["order"]) == {1, 2, 3, 4}
    assert set(windows["horizon"]) == {8}

    assert set(tracks["series"]) == {"GDPC1"}
    assert set(tracks["order"]) == {1, 2, 3, 4}
    assert {
        "branch_id",
        "origin_number",
        "status",
        "smoothness",
        "val1_loss",
        "val2_level_rmse",
        "val2_log_rmse",
        "delta_s",
        "surface_minima_count",
        "matched_branch_count",
    } <= set(tracks.columns)

    matched = tracks.loc[tracks["status"].eq("matched")]
    assert not matched.empty
    assert matched["smoothness"].between(0.0, 1.0).all()
    assert (
        matched["val1_end_date"] < matched["val2_start_date"]
    ).all()

    assert not validation_paths.empty
    assert {
        "series",
        "order",
        "branch_id",
        "origin_number",
        "smoothness",
        "date",
        "observed",
        "candidate_path",
        "val2_level_rmse",
        "val2_log_rmse",
    } <= set(validation_paths.columns)

    assert set(selection["series"]) == {"GDPC1"}
    assert int(selection["selected_branch"].sum()) == 1
    assert {
        "branch_id",
        "order",
        "window",
        "n_possible_origins",
        "n_matched_origins",
        "support_fraction",
        "selection_score",
        "smoothness_first",
        "smoothness_last",
        "smoothness_recent5_mean",
        "final_continuation",
        "final_smoothness",
        "true_test_level_rmse",
        "true_test_log_rmse",
        "selected_branch",
    } <= set(selection.columns)

    assert not test_paths.empty
    assert {
        "series",
        "branch_id",
        "order",
        "smoothness",
        "date",
        "observed",
        "candidate_path",
    } <= set(test_paths.columns)

    assert metadata["suite"] == "tracked_local_minima_two_validation"
    assert metadata["selection_uses_true_test"] is False
    assert metadata["max_minima"] == 5
    assert metadata["track_epsilon"] == 0.10
    assert metadata["candidate_spacing"] == 0.02

    assert (tmp_path / "rolling_validation_paths.csv").exists()
    assert (tmp_path / "tracked_minima_validation.png").exists()
    assert (tmp_path / "tracked_minima_validation.pdf").exists()
