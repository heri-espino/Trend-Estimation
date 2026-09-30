from __future__ import annotations

import json
import subprocess
import sys

import pandas as pd


def test_search_sensitivity_smoke_writes_ofat_results(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "run_search_sensitivity.py"
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

    summary_path = tmp_path / "sensitivity_summary.csv"
    metadata_path = tmp_path / "run_metadata.json"

    assert summary_path.exists()
    assert metadata_path.exists()

    summary = pd.read_csv(summary_path)
    assert {
        "parameter",
        "setting",
        "is_primary",
        "n_cases",
        "missed_minima",
        "positive_regret_cases",
        "mean_evaluations",
    } <= set(summary.columns)

    assert summary["is_primary"].sum() == 1
    assert set(summary["parameter"]) >= {
        "primary",
        "initial_grid_size",
        "max_depth",
        "endpoint_refinement_levels",
        "min_interval",
    }

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["suite"] == "search_design_sensitivity"
    assert metadata["preset"] == "smoke"
    assert metadata["primary_spec"]["initial_grid_size"] == 9
    assert metadata["primary_spec"]["endpoint_refinement_levels"] == 6
