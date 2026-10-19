"""Checks for the independently simulated known-variance Guerrero benchmark."""

from __future__ import annotations

import csv
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.guerrero_ratio import (
    GuerreroScenario, draw_observed_pool, execute, integrated_trend,
    paired_summary, preset_design, reconstruction_mse,
)
from experiments.pooled_loocv_smoothness.objective import (
    PooledLOOCV, difference_matrix,
)


def test_known_variance_ratio_and_smoothness_coordinate():
    scenario = GuerreroScenario(n=30, sigma_eta=2.0, sigma_epsilon=0.5)
    assert scenario.lambda_guerrero == pytest.approx(16.0)
    y, tau = draw_observed_pool(scenario, r=2, seed=11)
    obj = PooledLOOCV(y)
    assert 0 < obj.smoothness(scenario.lambda_guerrero) < 1
    assert reconstruction_mse(obj, tau, scenario.lambda_guerrero) >= 0


@pytest.mark.parametrize("order", [1, 2])
def test_integrated_trend_exactly_has_declared_difference_innovations(order):
    eps = np.array([0.5, -1.0, 0.2, 0.9, -0.4])
    tau = integrated_trend(eps, order=order, intercept=1.5, slope=0.1)
    np.testing.assert_allclose(difference_matrix(tau.size, order) @ tau,
                               eps, atol=1e-12)


def test_first_replication_is_identical_when_pool_size_grows():
    scenario = GuerreroScenario(n=25, sigma_eta=0.5, sigma_epsilon=0.1)
    y1, tau1 = draw_observed_pool(scenario, r=1, seed=730)
    y3, tau3 = draw_observed_pool(scenario, r=3, seed=730)
    np.testing.assert_array_equal(y1[0], y3[0])
    np.testing.assert_array_equal(tau1[0], tau3[0])
    assert not np.array_equal(tau3[0], tau3[1])


def test_manual_true_trend_mse_is_pooled_mean_of_squared_errors():
    scenario = GuerreroScenario(n=18, sigma_eta=1.2, sigma_epsilon=0.4)
    y, tau = draw_observed_pool(scenario, r=3, seed=777)
    obj = PooledLOOCV(y, order=2)
    lam = scenario.lambda_guerrero
    direct = float(np.mean((obj.trend(lam) - tau) ** 2))
    assert reconstruction_mse(obj, tau, lam) == pytest.approx(direct)
    individual = [PooledLOOCV(v, order=2) for v in y]
    assert direct == pytest.approx(float(np.mean([
        reconstruction_mse(x, tau[i:i+1], lam) for i, x in enumerate(individual)
    ])))


def test_invalid_scenarios_rejected():
    with pytest.raises(ValueError):
        GuerreroScenario(n=20, sigma_eta=0, sigma_epsilon=1)
    with pytest.raises(ValueError):
        GuerreroScenario(n=20, sigma_eta=1, sigma_epsilon=0)
    with pytest.raises(ValueError):
        GuerreroScenario(n=4, sigma_eta=1, sigma_epsilon=0.5)


def test_presets_have_disjoint_seeds_and_pilot_12_cells():
    sm = preset_design("smoke")
    pilot = preset_design("pilot")
    confirm = preset_design("confirmatory")
    assert len(sm[0]) == 2
    assert len(pilot[0]) == 12  # 2 lengths × 2 obs SD × 3 trend SD
    assert sm[-1] != pilot[-1] != confirm[-1]
    assert pilot[1] == 5 and confirm[1] == 100
    assert pilot[2] == (1, 3)


def test_smoke_creates_manifest_comparison_curve_and_plot(tmp_path):
    output = tmp_path / "guerrero_smoke"
    summary = execute("smoke", output)
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["total_pool_cases"] == 8
    assert manifest["rows_written"] == 32
    assert manifest["true_lambda_is_known_parameter_oracle"] is True
    assert summary["pool_count"] == 8
    assert summary["row_count"] == 32
    assert (output / "guerrero_example.png").stat().st_size > 0
    assert (output / "guerrero_example_curves.csv").stat().st_size > 0
    with (output / "guerrero_solver_comparison.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 32
    assert {r["method"] for r in rows} == {
        "guerrero_known_ratio", "bounded_brent", "multibracket_brent",
        "dense_reference",
    }
    assert all(float(x["true_trend_mse"]) >= 0 for x in rows)


def test_summary_rejects_missing_methods():
    with pytest.raises(ValueError, match="missing solver"):
        paired_summary([{
            "scenario_id": 0, "replicate": 0, "R": 1,
            "method": "guerrero_known_ratio",
        }])
