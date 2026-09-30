from __future__ import annotations

import json
import subprocess
import sys

import pandas as pd


def test_real_financial_stress_smoke_writes_comparison_outputs(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "run_financial_stress_test.py"
    )
    subprocess.run(
        [
            sys.executable,
            script,
            "--preset",
            "smoke",
            "--max-cases",
            "1",
            "--dense-grid-size",
            "51",
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    summary = pd.read_csv(tmp_path / "search_summary.csv")
    metadata = json.loads(
        (tmp_path / "run_metadata.json").read_text(encoding="utf-8")
    )

    assert len(summary) == 1
    assert {
        "series",
        "asset_class",
        "order",
        "window",
        "horizon",
        "dense_best_s",
        "adaptive_best_s",
        "best_s_abs_error",
        "objective_regret",
        "n_dense_interior_minima_missed",
        "adaptive_evaluations",
        "dense_evaluations",
    } <= set(summary.columns)

    assert metadata["suite"] == "financial_geometry_stress"
    assert metadata["transform"] == "natural_log_price"
    assert metadata["data_policy"] == "tracked_snapshot_only"
    assert metadata["endpoint_policy"] == "exact"
