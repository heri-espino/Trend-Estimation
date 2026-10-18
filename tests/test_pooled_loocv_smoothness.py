"""Independent mathematical and numerical checks for the new LOOCV paper."""

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.objective import PooledLOOCV, difference_matrix
from experiments.pooled_loocv_smoothness.search import (
    bounded_brent, dense_reference, multibracket_brent,
)
from experiments.pooled_loocv_smoothness.simulate import (
    Scenario, draw_pool, factorial_scenarios,
)


def example():
    tt = np.arange(9, dtype=float)
    return np.stack([0.1 * tt ** 2 + np.sin(tt),
                     0.08 * tt ** 2 + np.cos(tt * 1.3)])


def test_forward_difference_nullspace():
    d = difference_matrix(9, 2)
    t = np.arange(9, dtype=float)
    np.testing.assert_allclose(d @ np.ones(9), 0.0, atol=1e-13)
    np.testing.assert_allclose(d @ t, 0.0, atol=1e-13)
    np.testing.assert_allclose(d @ (t ** 2), 2.0 * np.ones(7), atol=1e-13)


@pytest.mark.parametrize("lam", [0.01, 0.6, 25.0])
def test_exact_loocv_matches_refitting_each_left_out_value(lam):
    y = example()[0]
    obj = PooledLOOCV(y, order=2)
    expected = []
    for i in range(len(y)):
        w = np.eye(len(y))
        w[i, i] = 0.0
        fit_without_i = np.linalg.solve(w + lam * obj.q, w @ y)
        expected.append((y[i] - fit_without_i[i]) ** 2)
    assert obj.score(lam) == pytest.approx(float(np.mean(expected)), rel=2e-9)


def test_pooled_loss_is_mean_of_component_losses():
    y = example()
    obj = PooledLOOCV(y, order=2)
    for lam in (0.0, 0.2, 10.0, float("inf")):
        individual = [PooledLOOCV(one, order=2).score(lam) for one in y]
        assert obj.score(lam) == pytest.approx(float(np.mean(individual)), rel=1e-9)


def test_endpoint_limits_and_monotone_normalization():
    obj = PooledLOOCV(example())
    assert obj.smoothness(0) == 0.0
    assert obj.smoothness(float("inf")) == 1.0
    xx = [obj.smoothness(lam) for lam in (1e-5, 0.1, 10.0, 1e5)]
    assert all(0.0 < x < 1.0 for x in xx)
    assert all(a < b for a, b in zip(xx[:-1], xx[1:]))
    assert obj.score(0) == pytest.approx(obj.score(1e-8), abs=1e-6)
    assert obj.score(float("inf")) == pytest.approx(obj.score(1e12), abs=1e-6)
    np.testing.assert_allclose(
        obj.trend(float("inf"))[:, 2:-2],
        obj.trend(1e12)[:, 2:-2], atol=1e-6,
    )


@pytest.mark.parametrize("lam", [0.04, 0.5, 4.0, 100.0])
def test_analytic_derivative_agrees_with_centered_difference(lam):
    obj = PooledLOOCV(example())
    h = lam * 1e-5
    numeric = (obj.score(lam + h) - obj.score(lam - h)) / (2.0 * h)
    assert obj.derivative(lam) == pytest.approx(numeric, rel=2e-4, abs=1e-7)


def test_candidate_score_is_no_worse_than_exact_endpoints():
    obj = PooledLOOCV(example())
    for method in (
        bounded_brent(obj), multibracket_brent(obj, n_scan=81),
        dense_reference(obj, n_grid=201),
    ):
        assert method.best.score <= obj.score(0) + 1e-13
        assert method.best.score <= obj.score(float("inf")) + 1e-13
        assert method.best.s >= 0 and method.best.s <= 1


def test_source_factorial_and_shared_signal_replicates():
    cells = factorial_scenarios()
    assert len(cells) == 16
    y1, tau1, season1 = draw_pool(Scenario("nonlinear", True, 0.5, 50), 1, 81)
    y3, tau3, season3 = draw_pool(Scenario("nonlinear", True, 0.5, 50), 3, 81)
    np.testing.assert_array_equal(y1[0], y3[0])
    np.testing.assert_array_equal(tau1, tau3)
    np.testing.assert_array_equal(season1, season3)


def test_sturm_rejects_floating_point_certificate_inputs():
    pytest.importorskip("sympy")
    from experiments.pooled_loocv_smoothness.sturm_exact import exact_sturm

    with pytest.raises(TypeError):
        exact_sturm([[0, 1, 0.5, 1, 0]], order=2)


def test_sturm_counts_tiny_exact_stationary_polynomial():
    pytest.importorskip("sympy")
    from experiments.pooled_loocv_smoothness.sturm_exact import exact_sturm

    result = exact_sturm([[0, 3, -1, 5, 1]], order=2)
    assert result["constant_objective"] is False
    assert result["polynomial_degree"] >= 0
    assert result["positive_stationary_roots"] >= 0
