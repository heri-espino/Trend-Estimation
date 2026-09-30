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


def _quick_regression_search(*, seed: int, ar1_phi: float, window: int, horizon: int):
    data = td.make_local_linear_ar1_series(
        n_obs=800,
        slope_noise_std=0.01,
        observation_noise_std=0.5,
        ar1_phi=ar1_phi,
        random_state=seed,
    )
    splits = td.rolling_origin_splits(
        800,
        initial_train=window,
        horizon=horizon,
        step=5,
        expanding=False,
        train_window=window,
    )[-30:]
    prepared = td.prepare_rolling_pure_forecast_objective(
        data.y,
        splits,
        order=4,
    )

    def value_grad_hess(lambda_: float):
        evaluated = prepared.evaluate(lambda_)
        return evaluated.value, evaluated.first, evaluated.second

    return td.find_stationary_points_smoothness(
        value_grad_hess,
        n_obs=window,
        order=4,
        initial_grid_size=9,
        max_depth=8,
        min_interval=1e-3,
    )


def test_search_recovers_quick_case_minimum_near_upper_boundary():
    result = _quick_regression_search(
        seed=1,
        ar1_phi=0.3,
        window=63,
        horizon=1,
    )

    minima = [
        point.smoothness_
        for point in result.points_
        if point.kind_ == "minimum"
    ]

    assert any(abs(smoothness - 0.988) < 0.003 for smoothness in minima)


def test_search_recovers_persistent_quick_case_minimum_near_upper_boundary():
    result = _quick_regression_search(
        seed=1,
        ar1_phi=0.8,
        window=252,
        horizon=20,
    )

    minima = [
        point.smoothness_
        for point in result.points_
        if point.kind_ == "minimum"
    ]

    assert any(abs(smoothness - 0.995) < 0.003 for smoothness in minima)
