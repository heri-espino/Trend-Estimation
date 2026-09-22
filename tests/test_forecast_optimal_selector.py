import numpy as np

import trend_estimation as td


def test_fixed_window_selector_returns_valid_candidate():
    x = np.arange(48, dtype=float)
    y = 0.02 * x * x + 0.3 * np.sin(x / 3.0)

    result = td.select_fixed_window_pure_smoothness(
        y,
        orders=(1, 2),
        windows=(10, 14),
        horizon=2,
        step=3,
        min_origins=2,
        log_bounds=(-6.0, 8.0),
        n_grid=61,
    )

    assert result.best_ in result.candidates_
    assert result.best_.order in (1, 2)
    assert result.best_.window in (10, 14)
    assert result.best_.lambda_ > 0.0
    assert 0.0 <= result.best_.smoothness_ < 1.0
    assert result.best_.n_origins_ >= 2
    assert len(result.candidates_) == 4


def test_selector_requires_only_history_available_at_outer_origin():
    x = np.arange(42, dtype=float)
    history = 0.01 * x * x + np.cos(x / 5.0)

    first = td.select_fixed_window_pure_smoothness(
        history,
        orders=(2,),
        windows=(12,),
        horizon=2,
        step=4,
        min_origins=2,
        log_bounds=(-5.0, 7.0),
        n_grid=41,
    )

    # Data after the outer origin are not an argument to the selector. Reusing
    # the same available history must reproduce the same selection exactly.
    second = td.select_fixed_window_pure_smoothness(
        history.copy(),
        orders=(2,),
        windows=(12,),
        horizon=2,
        step=4,
        min_origins=2,
        log_bounds=(-5.0, 7.0),
        n_grid=41,
    )

    assert np.isclose(first.best_.lambda_, second.best_.lambda_)
    assert np.isclose(first.best_.objective_, second.best_.objective_)



def test_candidate_windows_are_compared_on_identical_inner_origins():
    x = np.arange(50, dtype=float)
    y = 0.01 * x**2 + 0.15 * np.sin(x / 4.0)

    result = td.select_fixed_window_pure_smoothness(
        y,
        orders=(2,),
        windows=(10, 18, 24),
        horizon=3,
        step=4,
        min_origins=2,
        log_bounds=(-5.0, 7.0),
        n_grid=41,
    )

    origin_sets = {candidate.inner_origins_ for candidate in result.candidates_}
    assert len(origin_sets) == 1
    assert next(iter(origin_sets)) == result.common_inner_origins_

    n_origins = {candidate.n_origins_ for candidate in result.candidates_}
    n_scored = {candidate.n_scored_ for candidate in result.candidates_}
    assert len(n_origins) == 1
    assert len(n_scored) == 1
