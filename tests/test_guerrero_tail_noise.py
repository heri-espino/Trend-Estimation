"""Generator and score-contract tests for heavy-tail, skew and clustering study."""

import csv
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.run_tail_noise import (
    GAMMA_SHAPE, GARCH_ALPHA, GARCH_BETA, METHODS, REGIMES,
    TailScenario, design, draw_one, draw_pool, execute,
)


@pytest.mark.parametrize("regime", REGIMES)
def test_all_regimes_reproduce_nested_first_series(regime):
    sc = TailScenario(regime, 24, .5)
    y1, t1 = draw_pool(sc, 1, 427)
    y3, t3 = draw_pool(sc, 3, 427)
    np.testing.assert_array_equal(y1[0], y3[0])
    np.testing.assert_array_equal(t1[0], t3[0])
    assert y3.shape == t3.shape == (3, 24)
    assert np.all(np.isfinite(y3))


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
    assert len(smoke) == len(REGIMES) == 8
    assert rep == 1 and sizes == (1, 3)
    pilot, repeats, sizes, scan = design("pilot")
    assert len(pilot) == 32 and repeats == 5
    out = tmp_path / "does-not-exist"
    manifest = execute("pilot", out, dry_run=True)
    assert manifest["expected_pools"] == 320
    assert manifest["expected_method_rows"] == 960
    assert manifest["Cauchy_no_population_variance_or_expected_MSE"]
    assert not out.exists()


def test_smoke_outputs_all_methods_and_cauchy_warning(tmp_path):
    out = tmp_path / "smoke"
    report = execute("smoke", out)
    assert report["total_nested_pools"] == 16
    assert report["primary_R3_pools"] == 8
    assert (out / "manifest.json").stat().st_size > 0
    with (out / "method_comparison.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 48
    assert {r["method"] for r in rows} == set(METHODS)
    cauchy_rows = [r for r in rows if r["regime"] == "cauchy_observation"]
    assert len(cauchy_rows) == 6
    assert all(r["population_MSE_defined"] == "False" for r in cauchy_rows)
    assert all(r["noise_scale_semantics"] == "cauchy_scale_gamma"
               for r in cauchy_rows)
    assert all(np.isfinite(float(r["realized_median_absolute_trend_error"]))
               for r in rows)
    assert "Cauchy_warning" in json.loads((out / "summary.json").read_text())


def test_invalid_config_rejected():
    with pytest.raises(ValueError):
        TailScenario("unknown", 24, 1.)
    with pytest.raises(ValueError):
        TailScenario("gaussian_iid", 23, 1.)
    with pytest.raises(ValueError):
        draw_pool(TailScenario("gaussian_iid", 24, 1.), 0, seed=1)
