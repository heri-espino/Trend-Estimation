import numpy as np

import trend_estimation as td


def _known_multimodal_objective(n_obs: int, order: int):
    polynomial = np.poly1d([1.0])
    for root in (0.15, 0.45, 0.80):
        factor = np.poly1d([1.0, -root])
        polynomial = polynomial * factor * factor

    first = polynomial.deriv()
    second = first.deriv()

    def value_grad_hess(lambda_: float):
        smoothness = td.lambda_to_smoothness(lambda_, n_obs, order)
        ds, d2s = td.smoothness_derivatives(lambda_, n_obs, order)
        value = float(polynomial(smoothness))
        gradient_s = float(first(smoothness))
        curvature_s = float(second(smoothness))
        gradient_lambda = gradient_s * ds
        curvature_lambda = curvature_s * ds * ds + gradient_s * d2s
        return value, gradient_lambda, curvature_lambda

    return value_grad_hess


def test_smoothness_stationary_search_finds_multiple_local_minima():
    n_obs = 40
    order = 2
    result = td.find_stationary_points_smoothness(
        _known_multimodal_objective(n_obs, order),
        n_obs=n_obs,
        order=order,
        initial_grid_size=9,
        max_depth=8,
    )

    minima = [
        point.smoothness_
        for point in result.points_
        if point.kind_ == "minimum"
    ]
    maxima = [
        point.smoothness_
        for point in result.points_
        if point.kind_ == "maximum"
    ]

    assert np.allclose(minima, [0.15, 0.45, 0.80], atol=2e-6)
    assert len(maxima) == 2
    assert result.n_evaluations_ < 500


def test_spaced_minima_keep_best_inside_epsilon_radius():
    def point(smoothness, objective):
        return td.SmoothnessStationaryPoint(
            smoothness_=smoothness,
            lambda_=1.0,
            objective_=objective,
            gradient_smoothness_=0.0,
            curvature_smoothness_=1.0,
            gradient_lambda_=0.0,
            curvature_lambda_=1.0,
            kind_="minimum",
        )

    points = (
        point(0.10, 0.20),
        point(0.16, 0.10),
        point(0.40, 0.30),
        point(0.46, 0.05),
        point(0.80, 0.20),
        point(0.95, 0.40),
    )
    selected = td.select_spaced_smoothness_minima(
        points,
        epsilon=0.10,
        max_candidates=5,
    )

    smoothness = [candidate.smoothness_ for candidate in selected.candidates_]
    assert np.allclose(smoothness, [0.46, 0.16, 0.80, 0.95])
    assert 0.40 not in smoothness
    assert 0.10 not in smoothness
    for i, first in enumerate(smoothness):
        for second in smoothness[i + 1 :]:
            assert abs(first - second) > 0.10


def test_epsilon_sweep_caps_candidate_count():
    points = tuple(
        td.SmoothnessStationaryPoint(
            smoothness_=smoothness,
            lambda_=1.0,
            objective_=objective,
            gradient_smoothness_=0.0,
            curvature_smoothness_=1.0,
            gradient_lambda_=0.0,
            curvature_lambda_=1.0,
            kind_="minimum",
        )
        for smoothness, objective in [
            (0.05, 0.6),
            (0.15, 0.5),
            (0.25, 0.4),
            (0.35, 0.3),
            (0.45, 0.2),
            (0.55, 0.1),
        ]
    )

    sweep = td.sweep_spaced_smoothness_minima(
        points,
        epsilons=(0.0, 0.05, 0.10, 0.15),
        max_candidates=5,
    )

    assert [item.epsilon_ for item in sweep] == [0.0, 0.05, 0.10, 0.15]
    assert all(len(item.candidates_) <= 5 for item in sweep)
