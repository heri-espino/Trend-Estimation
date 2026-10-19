"""Estimated Guerrero variance-ratio methodology and end-to-end smoke tests."""

import csv
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.guerrero_ratio import (
    GuerreroScenario, draw_observed_pool,
)
from experiments.pooled_loocv_smoothness.objective import (
    PooledLOOCV, difference_matrix,
)
from experiments.pooled_loocv_smoothness.variance_estimation import (
    estimate_gaussian_differences, estimate_moments,
)
from experiments.pooled_loocv_smoothness.run_variance_estimation import (
    execute, summarize,
)


def test_theoretical_differenced_covariance_is_not_white_noise():
    d = difference_matrix(20, 2)
    a, b = 0.3**2, 1.5**2
    cov = a * np.eye(d.shape[0]) + b * (d @ d.T)
    assert np.all(np.linalg.eigvalsh(cov) > 0)
    assert cov[0, 1] == pytest.approx(-4. * b)
    assert cov[0, 2] == pytest.approx(1. * b)
    assert cov[0, 3] == pytest.approx(0.)


@pytest.mark.parametrize("r", [1, 3])
def test_estimation_returns_nonnegative_components_and_finite_score(r):
    s = GuerreroScenario(n=50, sigma_eta=0.5, sigma_epsilon=0.3)
    y, _ = draw_observed_pool(s, r=r, seed=100)
    obj = PooledLOOCV(y, order=2)
    for f in (estimate_moments, estimate_gaussian_differences):
        result = f(y, obj.d)
        assert result.sigma_epsilon2 >= 0
        assert result.sigma_eta2 >= 0
        assert result.lambda_ratio >= 0
        assert np.isfinite(obj.score(result.lambda_ratio))


def test_scale_equivariance_of_variance_estimators_and_reconstruction():
    s = GuerreroScenario(n=50, sigma_eta=2.0, sigma_epsilon=0.3)
    y, tau = draw_observed_pool(s, r=3, seed=111)
    d = difference_matrix(s.n, 2)
    for estimate in (estimate_moments, estimate_gaussian_differences):
        original = estimate(y, d)
        scaled = estimate(3 * y, d)
        assert scaled.sigma_eta2 == pytest.approx(9 * original.sigma_eta2, rel=1e-7, abs=1e-6)
        assert scaled.sigma_epsilon2 == pytest.approx(9 * original.sigma_epsilon2, rel=1e-7, abs=1e-6)
        assert scaled.lambda_ratio == pytest.approx(original.lambda_ratio, rel=1e-7)
        original_obj = PooledLOOCV(y)
        scaled_obj = PooledLOOCV(3 * y)
        assert scaled_obj.score(original.lambda_ratio) == pytest.approx(
            9 * original_obj.score(original.lambda_ratio), rel=1e-9
        )
        assert np.mean((scaled_obj.trend(original.lambda_ratio) - 3 * tau) ** 2) == pytest.approx(
            9 * np.mean((original_obj.trend(original.lambda_ratio) - tau) ** 2), rel=1e-9
        )


def test_estimate_from_known_stochastic_model_has_correct_order_of_magnitude():
    scenario = GuerreroScenario(n=200, sigma_eta=2.0, sigma_epsilon=0.3)
    y, _ = draw_observed_pool(scenario, r=3, seed=2026)
    estimate = estimate_gaussian_differences(y, difference_matrix(200, 2))
    assert 1. < estimate.sigma_eta2 < 8.
    assert 0.01 < estimate.sigma_epsilon2 < 1.
    assert estimate.lambda_ratio > 0.


def test_dry_run_has_no_files_and_reports_all_scenarios(tmp_path):
    path = tmp_path / "dry"
    report = execute("pilot", path, dry_run=True)
    assert report["total_pools"] == 120
    assert len(report["scenarios"]) == 12
    assert not path.exists()


def test_smoke_persists_four_estimators_and_two_loss_metrics(tmp_path):
    out = tmp_path / "results"
    summary = execute("smoke", out)
    manifest = json.loads((out / "manifest.json").read_text())
    assert manifest["total_pools"] == 8
    assert manifest["rows_written"] == 32
    assert summary["rows"] == 32
    for name in (
        "variance_estimator_comparison.csv",
        "scenario_summary.csv",
        "summary.json",
        "true_mse_by_noise_level.png",
        "common_noise_scale_invariance.csv",
    ):
        assert (out / name).stat().st_size > 0
    with (out / "variance_estimator_comparison.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 32
    assert {row["method"] for row in rows} == {
        "guerrero_known_ratio", "estimated_moments_nnls",
        "estimated_gaussian_difference_ml", "pooled_loocv_bounded_brent",
    }
    assert all(float(row["loocv_mse"]) >= 0 for row in rows)


def test_malformed_summary_empty_fails():
    with pytest.raises(KeyError):
        summarize([{"R": 1, "method": "known"}])
