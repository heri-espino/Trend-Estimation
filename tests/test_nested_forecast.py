import numpy as np

import trend_estimation as td


def test_no_change_forecast_repeats_last_observation():
    y = np.array([1.0, 1.5, 2.25])
    assert np.allclose(td.no_change_forecast(y, 4), [2.25, 2.25, 2.25, 2.25])


def test_nested_outer_forecast_is_invariant_to_untouched_future_values():
    # Exactly one outer origin: 24 observations available, 2 future values.
    x = np.arange(26, dtype=float)
    prefix = 0.03 * x[:24] ** 2 + 0.1 * np.sin(x[:24])

    y_a = np.concatenate([prefix, [18.0, 19.0]])
    y_b = np.concatenate([prefix, [-100.0, 250.0]])

    kwargs = dict(
        outer_initial_train=24,
        horizon=2,
        outer_step=2,
        orders=(1, 2),
        windows=(8, 12),
        inner_step=4,
        min_inner_origins=2,
        log_bounds=(-5.0, 7.0),
        n_grid=31,
    )

    result_a = td.nested_rolling_pure_forecast(y_a, **kwargs)
    result_b = td.nested_rolling_pure_forecast(y_b, **kwargs)

    assert len(result_a.records) == len(result_b.records) == 1
    record_a = result_a.records[0]
    record_b = result_b.records[0]

    assert record_a.origin == record_b.origin == 24
    assert record_a.selected_order == record_b.selected_order
    assert record_a.selected_window == record_b.selected_window
    assert np.isclose(record_a.selected_lambda, record_b.selected_lambda)
    assert np.isclose(record_a.selected_smoothness, record_b.selected_smoothness)
    assert np.allclose(record_a.prediction, record_b.prediction)
    assert np.allclose(record_a.benchmark_prediction, record_b.benchmark_prediction)

    # The targets differ, proving they were not part of selection/fitting.
    assert not np.allclose(record_a.observed, record_b.observed)


def test_nested_result_reports_relative_rmsfe():
    x = np.arange(30, dtype=float)
    y = 0.015 * x**2 + 0.2 * np.cos(x / 3.0)

    result = td.nested_rolling_pure_forecast(
        y,
        outer_initial_train=24,
        horizon=2,
        outer_step=2,
        orders=(2,),
        windows=(10,),
        inner_step=4,
        min_inner_origins=2,
        log_bounds=(-5.0, 7.0),
        n_grid=31,
    )

    assert len(result.records) == 3
    assert result.observed.shape == result.prediction.shape
    assert result.observed.shape == result.benchmark_prediction.shape
    assert result.rmse >= 0.0
    assert result.benchmark_rmse >= 0.0
    assert result.relative_rmsfe >= 0.0
