from __future__ import annotations

import json
import subprocess
import sys

import pandas as pd


def test_synthetic_numerical_benchmark_smoke_writes_outputs(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "run_synthetic_benchmark.py"
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

    summary_path = tmp_path / "search_summary.csv"
    candidates_path = tmp_path / "candidate_sweep.csv"
    metadata_path = tmp_path / "run_metadata.json"

    assert summary_path.exists()
    assert candidates_path.exists()
    assert metadata_path.exists()

    summary = pd.read_csv(summary_path)
    assert len(summary) == 1
    assert summary.loc[0, "dense_best_s"] >= 0.0
    assert summary.loc[0, "dense_best_s"] <= 1.0
    assert summary.loc[0, "adaptive_best_s"] >= 0.0
    assert summary.loc[0, "adaptive_best_s"] <= 1.0
    assert summary.loc[0, "adaptive_best_source"] in {
        "interior",
        "S=0",
        "S=1",
    }

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["n_cases"] == 1
    assert metadata["endpoint_policy"] == "exact"
