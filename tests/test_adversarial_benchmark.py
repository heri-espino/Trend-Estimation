from __future__ import annotations

import json
import subprocess
import sys

import numpy as np
import pandas as pd

from trend_estimation.benchmarks.adversarial import (
    adversarial_smoothness_cases,
)


def test_adversarial_suite_contains_boundary_close_and_flat_cases():
    cases = {case.name: case for case in adversarial_smoothness_cases()}

    assert {"near_zero", "near_one", "close_pair", "flat_minimum", "five_minima"} <= set(cases)
    assert cases["near_zero"].true_minima == (0.001,)
    assert cases["near_one"].true_minima == (0.999,)
    assert len(cases["five_minima"].true_minima) == 5
    assert cases["flat_minimum"].true_flat_minima


def test_adversarial_lambda_callback_matches_chain_rule():
    case = {
        item.name: item for item in adversarial_smoothness_cases()
    }["close_pair"]
    n_obs = 63
    order = 4
    callback = case.lambda_callback(n_obs=n_obs, order=order)

    for smoothness in (0.2, 0.46, 0.8):
        from trend_estimation.core.smoothness import (
            smoothness_derivatives,
            smoothness_to_lambda,
        )

        lambda_ = smoothness_to_lambda(smoothness, n_obs, order)
        recovered_s = td.lambda_to_smoothness(lambda_, n_obs, order)
        value, grad_lambda, hess_lambda = callback(lambda_)
        ds, d2s = smoothness_derivatives(lambda_, n_obs, order)

        assert np.isclose(value, case.value(recovered_s), rtol=1e-12, atol=1e-12)
        assert np.isclose(grad_lambda, case.first(recovered_s) * ds, rtol=1e-9, atol=1e-12)
        expected_hess = case.second(recovered_s) * ds**2 + case.first(recovered_s) * d2s
        assert np.isclose(hess_lambda, expected_hess, rtol=1e-8, atol=1e-12)


def test_adversarial_benchmark_smoke_writes_method_comparison(tmp_path):
    script = (
        "experiments/numerical_smoothness_selection/"
        "run_adversarial_benchmark.py"
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

    summary = pd.read_csv(tmp_path / "method_summary.csv")
    detections = pd.read_csv(tmp_path / "stationary_detection.csv")
    metadata = json.loads(
        (tmp_path / "run_metadata.json").read_text(encoding="utf-8")
    )

    assert set(summary["method"]) == {"adaptive_s", "log_lambda", "dense"}
    assert {"case", "n_obs", "order", "method", "best_s", "objective_regret", "n_evaluations"} <= set(summary)
    assert {"truth_s", "truth_kind", "detected", "abs_error"} <= set(detections)
    assert metadata["suite"] == "adversarial_smoothness"
    assert metadata["preset"] == "smoke"
    assert metadata["endpoint_policy"] == "exact"
