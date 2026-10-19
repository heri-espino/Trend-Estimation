"""Generator and score-contract tests for heavy-tail, skew and clustering study."""

import csv
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.run_tail_noise import (
    DIFFERENCE_ORDERS, GAMMA_SHAPE, GARCH_ALPHA, GARCH_BETA,
    METHODS, REGIMES, SKEW_NORMAL_ALPHAS, TailScenario,
    centered_skew_normal, design, draw_one, draw_pool, execute,
    integrate_differences,
)
from experiments.pooled_loocv_smoothness.objective import difference_matrix


@pytest.mark.parametrize("regime", REGIMES)
def test_all_regimes_reproduce_nested_first_series(regime):
    sc = TailScenario(regime, 24, .5)
    y1, t1 = draw_pool(sc, 1, 427)
    y3, t3 = draw_pool(sc, 3, 427)
    np.testing.assert_array_equal(y1[0], y3[0])
    np.testing.assert_array_equal(t1[0], t3[0])
    assert y3.shape == t3.shape == (3, 24)
    assert np.all(np.isfinite(y3))


@pytest.mark.parametrize("d", DIFFERENCE_ORDERS)
def test_stochastic_generator_exact_dth_difference(d):
    rng = np.random.default_rng(640+d)
    innovations = rng.normal(size=42-d)
    trend = integrate_differences(innovations, d)
    np.testing.assert_allclose(
        difference_matrix(len(trend), d) @ trend,
        innovations, rtol=2e-7, atol=2e-7
    )


@pytest.mark.parametrize("alpha", [-6., -3., 0., 3., 6.])
def test_skew_normal_population_center_and_unit_variance(alpha):
    rng = np.random.default_rng(1470)
    z = centered_skew_normal(rng, 100000, alpha)
    assert abs(float(np.mean(z))) < .025
    assert float(np.var(z)) == pytest.approx(1., rel=.025)
    standardized_skew = float(np.mean((z - z.mean())**3))
    if alpha >= 3:
        assert standardized_skew > .4
    elif alpha <= -3:
        assert standardized_skew < -.4
    else:
        assert abs(standardized_skew) < .06


def test_skew_normal_distribution_is_exposed_at_all_orders():
    for d in DIFFERENCE_ORDERS:
        for regime, alpha in SKEW_NORMAL_ALPHAS.items():
            sc = TailScenario(regime, 24, 1.5, order=d)
            y, tau, eta = draw_one(sc, np.random.default_rng(20000 + d))
            np.testing.assert_allclose(y - tau, eta, atol=1e-7)
            assert sc.order == d
            assert float(np.isfinite(eta).mean()) == 1.0


def test_gamma_centered_sd_and_opposite_skewness():
    rng = np.random.default_rng(100)
    sh = GAMMA_SHAPE
    right = (rng.gamma(sh, 1., 50000) - sh) / np.sqrt(sh)
    assert abs(float(right.mean())) < .025
    assert float(np.var(right)) == pytest.approx(1., rel=.04)
    assert float(np.mean(right**3)) > 1.
    assert float(np.mean((-right)**3)) < -1.


def test_t3_has_finite_population_variance_and_very_heavy_tails():
    sc = TailScenario("student_t3_observation", 24, 2.)
    rng = np.random.default_rng(1)
    data = np.concatenate([draw_one(sc, rng)[2] for _ in range(3000)])
    assert float(np.var(data)) == pytest.approx(4., rel=.16)
    assert float(np.mean(np.abs(data)>10.)) > 0.


def test_cauchy_scale_is_not_standard_deviation():
    sc = TailScenario("cauchy_observation", 24, .5)
    assert not sc.observation_variance_exists
    rng = np.random.default_rng(1111)
    noise = np.concatenate([draw_one(sc, rng)[2] for _ in range(300)])
    assert float(np.median(np.abs(noise))) == pytest.approx(.5, rel=.08)


def test_garch_variance_cluster_recurrence_and_unconditional_mean():
    sc = TailScenario("garch_t5_observation", 200, 1.)
    rng = np.random.default_rng(101)
    noise = np.concatenate([draw_one(sc, rng)[2] for _ in range(400)])
    assert float(np.mean(noise**2)) == pytest.approx(1., rel=.18)
    assert GARCH_ALPHA+GARCH_BETA < 1
    # Dependence in magnitudes, not necessarily signed returns:
    x = noise[:40000]
    corr = np.corrcoef(x[:-1]**2, x[1:]**2)[0, 1]
    assert corr > .02


def test_separate_seed_and_pilot_are_locked(tmp_path):
    smoke, rep, sizes, scan = design("smoke")
    assert len(smoke) == len(REGIMES) * len(DIFFERENCE_ORDERS) == 39
    assert rep == 1 and sizes == (1, 3)
    pilot, repeats, sizes, scan = design("pilot")
    assert len(pilot) == 156 and repeats == 5
    assert {s.order for s in pilot} == set(DIFFERENCE_ORDERS)
    out = tmp_path / "does-not-exist"
    manifest = execute("pilot", out, dry_run=True)
    assert manifest["expected_pools"] == 1560
    assert manifest["expected_method_rows"] == 4680
    assert manifest["difference_orders"] == [1, 2, 3]
    assert len(manifest["skew_normal_alphas"]) == 5
    assert manifest["Cauchy_no_population_variance_or_expected_MSE"]
    assert not out.exists()


def test_smoke_outputs_all_methods_and_cauchy_warning(tmp_path):
    out = tmp_path / "smoke"
    report = execute("smoke", out)
    assert report["total_nested_pools"] == 78
    assert report["primary_R3_pools"] == 39
    assert set(report["by_difference_order_R3"]) == {"1", "2", "3"}
    assert (out / "manifest.json").stat().st_size > 0
    with (out / "method_comparison.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 234
    assert {r["method"] for r in rows} == set(METHODS)
    cauchy_rows = [r for r in rows if r["regime"] == "cauchy_observation"]
    assert len(cauchy_rows) == 18
    assert all(r["population_MSE_defined"] == "False" for r in cauchy_rows)
    assert all(r["noise_scale_semantics"] == "cauchy_scale_gamma"
               for r in cauchy_rows)
    assert all(np.isfinite(float(r["realized_median_absolute_trend_error"]))
               for r in rows)
    manifest = json.loads((out / "manifest.json").read_text())
    assert manifest["actual_rows"] == 234
    assert manifest["difference_order_matches_trend_generator"]
    assert set(float(row["d"]) for row in rows) == set(DIFFERENCE_ORDERS)
    assert "Cauchy_warning" in json.loads((out / "summary.json").read_text())


def test_invalid_config_rejected():
    with pytest.raises(ValueError):
        TailScenario("unknown", 24, 1.)
    with pytest.raises(ValueError):
        TailScenario("gaussian_iid", 23, 1.)
    with pytest.raises(ValueError):
        TailScenario("gaussian_iid", 24, 1., order=4)
    with pytest.raises(ValueError):
        draw_pool(TailScenario("gaussian_iid", 24, 1.), 0, seed=1)
