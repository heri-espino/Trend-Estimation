from __future__ import annotations

import json
import subprocess
import sys

import pandas as pd


def test_two_stage_order_validation_smoke_keeps_true_test_untouched(tmp_path):
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

    selection = pd.read_csv(
        tmp_path / "two_stage_order_selection.csv",
        parse_dates=[
            "inner_development_start_date",
            "inner_development_end_date",
            "validation2_start_date",
            "validation2_end_date",
            "true_test_start_date",
            "true_test_end_date",
        ],
    )
    paths = pd.read_csv(
        tmp_path / "two_stage_order_paths.csv",
        parse_dates=["date"],
    )
    metadata = json.loads(
        (tmp_path / "run_metadata.json").read_text(encoding="utf-8")
    )

    assert set(selection["series"]) == {"GDPC1"}
    assert set(selection["order"]) == {1, 2, 3, 4}
    assert int(selection["selected_order"].sum()) == 1
    assert set(selection["horizon"]) == {8}

    assert (
        selection["inner_development_end_date"]
        < selection["validation2_start_date"]
    ).all()
    assert (
        selection["validation2_end_date"]
        < selection["true_test_start_date"]
    ).all()

    assert {
        "inner_cv_error",
        "validation2_level_rmse",
        "validation2_log_rmse",
        "validation2_rank",
        "selected_order",
        "true_test_level_rmse",
        "true_test_log_rmse",
    } <= set(selection.columns)

    assert set(paths["segment"]) == {
        "inner_train",
        "validation2",
        "final_train",
        "true_test",
    }

    assert metadata["suite"] == "two_stage_order_validation"
    assert metadata["selection_uses_true_test"] is False
    assert metadata["selection_metric"] == "level_rmse"

    assert (tmp_path / "two_stage_order_validation.png").exists()
    assert (tmp_path / "two_stage_order_validation.pdf").exists()
