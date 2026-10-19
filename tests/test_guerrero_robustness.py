"""Deterministic generator and minimal robustness campaign tests."""

import csv
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.run_robustness import (
    AR1_PHI, METHODS, REGIMES, RobustScenario, design, draw_one, draw_pool, execute,
    summarize,
)


def test_nested_r1_r3_reuse_first_series_in_every_regime():
    for regime in REGIMES:
        scenario = RobustScenario(regime, n=24, sigma_eta=2.0)
        one_y, one_tau = draw_pool(scenario, r=1, seed=903)
        three_y, three_tau = draw_pool(scenario, r=3, seed=903)
        np.testing.assert_array_equal(one_y[0], three_y[0])
        np.testing.assert_array_equal(one_tau[0], three_tau[0])
        assert not np.array_equal(three_tau[0], three_tau[1])


@pytest.mark.parametrize("regime", REGIMES)
def test_finite_dgp_and_nominal_variance_ratio(regime):
    sc = RobustScenario(regime, 50, 2.0, 0.3)
    assert sc.nominal_lambda == pytest.approx((2.0 / 0.3) ** 2)
    y, tau, eta = draw_one(sc, np.random.default_rng(2026))
    assert y.shape == tau.shape == eta.shape == (50,)
    np.testing.assert_allclose(y - tau, eta)
    assert np.all(np.isfinite(y))
    assert np.all(np.isfinite(tau))


def test_ar1_is_stationary_and_correlated_in_monte_carlo():
    sc = RobustScenario("ar1_observation", 24, 1.5, .3)
    rng = np.random.default_rng(2026)
    replicates = np.stack([draw_one(sc, rng)[2] for _ in range(2000)])
    assert np.var(replicates[:, 0]) == pytest.approx(1.5 ** 2, rel=.08)
    rho = np.mean(replicates[:, 0] * replicates[:, 1]) / (1.5 ** 2)
    assert rho == pytest.approx(AR1_PHI, abs=.06)


def test_heteroskedastic_variance_changes_but_average_is_preserved():
    sc = RobustScenario("heteroskedastic_observation", 24, 2.0, .3)
    rng = np.random.default_rng(301)
    samples = np.stack([draw_one(sc, rng)[2] for _ in range(2000)])
    first = np.mean(samples[:, :12] ** 2)
    second = np.mean(samples[:, 12:] ** 2)
    assert first == pytest.approx(0.25 * 4.0, rel=.06)
    assert second == pytest.approx(1.75 * 4.0, rel=.06)
    assert (first + second) / 2 == pytest.approx(4.0, rel=.06)


@pytest.mark.parametrize("regime", ["student_t_observation", "student_t_innovation"])
def test_t5_marginal_second_moment_standardized(regime):
    sc = RobustScenario(regime, 24, 1.0, .3)
    rng = np.random.default_rng(42)
    chunks = []
    for _ in range(1500):
        y, tau, eta = draw_one(sc, rng)
        v = eta if regime == "student_t_observation" else np.diff(tau, n=2) / .3
        chunks.append(v)
    m2 = np.mean(np.concatenate(chunks) ** 2)
    assert m2 == pytest.approx(1.0, rel=.10)


def test_smoke_and_pilot_preset_sizes_and_no_side_effect_dryrun(tmp_path):
    smoke, repeats, pools, _ = design("smoke")
    assert len(smoke) == 5 and repeats == 1 and pools == (1, 3)
    pilot, repeats, pools, _ = design("pilot")
    assert len(pilot) == 20 and repeats == 5 and pools == (1, 3)
    target = tmp_path / "dry"
    info = execute("pilot", target, dry_run=True)
    assert info["expected_pools"] == 200
    assert info["expected_method_rows"] == 1000
    assert not target.exists()


def test_smoke_artifacts_five_regimes_and_nested_methods(tmp_path):
    out = tmp_path / "robustness_smoke"
    s = execute("smoke", out)
    assert s["total_pools"] == 10
    assert s["primary_R3"]["pool_count"] == 5
    assert set(s["by_regime_R3"]) == set(REGIMES)
    assert (out / "robustness_true_trend_mse_R3.png").stat().st_size > 0
    manifest = json.loads((out / "manifest.json").read_text())
    assert manifest["actual_rows"] == 50
    assert manifest["truth_used_for_tuning"] is False
    with (out / "method_comparison.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 50
    assert {r["method"] for r in rows} == set(METHODS)
    assert all(float(r["true_trend_mse"]) >= 0 for r in rows)
    assert all(r["nominal_ratio_is_valid_model_benchmark"] ==
               ("True" if r["regime"] == "gaussian_iid" else "False")
               for r in rows)


def test_bad_regime_and_missing_method_rejected():
    with pytest.raises(ValueError):
        RobustScenario("nonexistent", 24, .5)
    with pytest.raises(ValueError):
        summarize([{"regime": "gaussian_iid", "N": 24,
                    "sigma_eta_nominal": .5, "replicate": 0,
                    "R": 3, "method": METHODS[0]}])
