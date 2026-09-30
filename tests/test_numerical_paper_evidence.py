from __future__ import annotations

import subprocess
import sys

import pandas as pd


def test_generate_numerical_paper_evidence(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "generate_paper_evidence.py"
    )
    subprocess.run(
        [
            sys.executable,
            script,
            "--output-dir",
            str(tmp_path),
        ],
        check=True,
    )

    summary = pd.read_csv(tmp_path / "tables" / "benchmark_summary.csv")
    assert set(summary["benchmark"]) == {
        "adversarial",
        "synthetic",
        "financial",
    }
    assert int(
        summary.loc[
            summary["benchmark"].eq("synthetic"),
            "missed_minima",
        ].iloc[0]
    ) == 0
    assert int(
        summary.loc[
            summary["benchmark"].eq("financial"),
            "missed_minima",
        ].iloc[0]
    ) == 0

    expected = [
        tmp_path / "tables" / "benchmark_summary.tex",
        tmp_path / "tables" / "sensitivity_summary.tex",
        tmp_path / "figures" / "evaluation_efficiency.pdf",
        tmp_path / "figures" / "optimum_agreement.pdf",
        tmp_path / "figures" / "sensitivity_tradeoff.pdf",
    ]
    for path in expected:
        assert path.exists()
        assert path.stat().st_size > 0
