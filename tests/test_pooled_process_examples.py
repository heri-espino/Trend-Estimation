"""Lightweight, no-Monte-Carlo tests for the process illustration gallery."""
import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.run_process_examples import (
    DEFAULT_SEED, METHODS, SIGMA_ETA, _ar1,
    make_examples, evaluate_example,
)


def test_illustrations_are_deterministic_distinct_and_finite():
    a = make_examples(seed=DEFAULT_SEED, n=40)
    b = make_examples(seed=DEFAULT_SEED, n=40)
    assert len(a) == 9
    assert list(a) == list(b)
    for name in a:
        assert a[name].y.shape == (3, 40)
        assert a[name].truth.shape == (3, 40)
        assert np.isfinite(a[name].y).all()
        assert np.isfinite(a[name].truth).all()
        np.testing.assert_array_equal(a[name].y, b[name].y)
        np.testing.assert_array_equal(a[name].truth, b[name].truth)


def test_single_mechanism_contrasts_reuse_same_underlying_shocks():
    cases = make_examples(n=40)
    ref = cases["gaussian_reference"]
    for name in ("smooth_cycle", "slope_break", "level_jump"):
        # Structural examples perturb true tau while keeping eta identical.
        np.testing.assert_allclose(
            cases[name].y - cases[name].truth,
            ref.y - ref.truth, rtol=0, atol=2e-14
        )
    for name in ("observation_outliers", "ar1_observation",
                 "variance_regime", "heterogeneous_pool",
                 "shared_observation_shock"):
        # These scenarios perturb eta only; latent trends remain identical.
        np.testing.assert_array_equal(cases[name].truth, ref.truth)
    assert not np.array_equal(
        cases["slope_break"].truth, ref.truth
    )
    assert not np.array_equal(
        cases["observation_outliers"].y, ref.y
    )
    # The R=1 first series is exactly nested in the R=3 input.
    np.testing.assert_array_equal(
        cases["heterogeneous_pool"].truth[0], ref.truth[0]
    )
    np.testing.assert_allclose(
        (cases["heterogeneous_pool"].y[0] -
         cases["heterogeneous_pool"].truth[0]),
        (ref.y[0] - ref.truth[0]) * (0.25 / SIGMA_ETA),
        rtol=0, atol=2e-14,
    )


def test_ar1_constructor_rejects_explosive_coefficient():
    with pytest.raises(ValueError):
        _ar1(np.ones(8), 1.0)
    with pytest.raises(ValueError):
        _ar1(np.ones(8), -1.2)


def test_invalid_examples_and_pool_sizes():
    with pytest.raises(ValueError):
        make_examples(n=24)
    with pytest.raises(ValueError):
        evaluate_example(make_examples(n=32)["gaussian_reference"], r=2)


def test_single_case_all_feasible_methods_and_ex_post_metrics():
    # One SMALL fixed numerical fixture, not a campaign.
    case = make_examples(n=32)["gaussian_reference"]
    rows, fits = evaluate_example(case, r=1, scan_points=7)
    assert len(rows) == len(METHODS)
    assert {r["method"] for r in rows} == set(METHODS)
    assert set(fits) == set(METHODS)
    assert all(x["R"] == 1 and x["d"] == 2 for x in rows)
    assert all(np.isfinite(x["latent_trend_mse_EX_POST"])
               for x in rows)
    assert all(np.isfinite(x["latent_trend_mae_EX_POST"])
               for x in rows)
    assert all(np.isfinite(fits[x][0]).all() for x in fits)
    # Penalized smoother explicitly includes the held-out-aware joint mean;
    # none of the eleven examples uses the known realized tau as a selector.
    assert not any("oracle" in row["method"] for row in rows)
