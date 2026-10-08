"""Invariants of the new standalone pooled F Streamlit lab.

No Streamlit import required: all scientific code is in pooled_lab.
"""
from __future__ import annotations

import numpy as np
import pytest

from experiments.smoothness_cv.pooled_lab import (
    all_grid_fold_losses,
    analyze_pooled,
    chronological_origins,
    fit_window_forecast,
    fold_loss_at_lambda,
)
from trend_estimation.core.smoothness import smoothness_to_lambda
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.validation.rolling_origin import RollingOriginSplit


@pytest.fixture(scope="module")
def observed():
    t = np.arange(91, dtype=float)
    return 8 + 0.03 * t + np.sin(t / 7) + 0.09 * np.random.default_rng(13).normal(size=len(t))


def _run(y, **options):
    kw = dict(
        window=22, order=2, horizon=3, stride=4, max_folds=7,
        grid_points=31, refine=True, holdout=True, compare_one_step=True,
    )
    kw.update(options)
    return analyze_pooled(y, **kw)



def test_origin_spacing_and_latest_completed_block():
    # Backward from 80-6=74; 74,65,56,47,38; keep four recent, then chronological.
    assert chronological_origins(80, 20, 6, 9, 4).tolist() == [47, 56, 65, 74]
    assert chronological_origins(50, 20, 5, 5, 1).tolist() == [45]
    with pytest.raises(ValueError):
        chronological_origins(23, 20, 6, 1, 3)


def test_curve_pooling_is_arithmetic_mean_of_same_s(observed):
    result = _run(observed)
    assert result.fold_losses.shape == (len(result.origins), 31)
    assert np.allclose(result.pooled_losses, result.fold_losses.mean(axis=0), atol=1e-10)
    assert np.isclose(result.pooled_mse, result.losses_at_pooled.mean(), atol=1e-7)
    assert np.isclose(
        result.last_validation_mse,
        result.losses_at_last[-1],
        atol=1e-7,
    )
    assert 0 <= result.pooled_s <= 1
    assert 0 <= result.last_s <= 1
    assert result.one_step_s is not None and 0 <= result.one_step_s <= 1


def test_held_out_truth_cannot_change_selector_or_forecast(observed):
    original = _run(observed)
    tampered = observed.copy()
    tampered[-3:] = [1500., -500., 750.]
    altered = _run(tampered)
    assert np.array_equal(original.origins, altered.origins)
    assert np.array_equal(original.fold_losses, altered.fold_losses)
    assert original.pooled_s == altered.pooled_s
    assert original.last_s == altered.last_s
    assert original.one_step_s == altered.one_step_s
    for method in original.final_trends:
        assert np.allclose(original.final_trends[method], altered.final_trends[method])
        assert np.allclose(original.future_forecasts[method], altered.future_forecasts[method])
    assert original.test_mse["Pooled CV"] != altered.test_mse["Pooled CV"]


def test_spectral_batch_matches_existing_objective(observed):
    T = len(observed) - 3
    splits = [
        RollingOriginSplit(
            train=slice(t - 22, t),
            validation=slice(t, t + 3),
        )
        for t in [59, 67, 80]
    ]
    prep = prepare_rolling_pure_forecast_objective(observed[:T], splits, order=2)
    grid = np.array([0.0, 0.15, 0.50, 0.88, 1.0])
    losses = all_grid_fold_losses(prep, grid, 22, 2)
    for j, s in enumerate(grid):
        lam = smoothness_to_lambda(float(s), 22, 2)
        assert np.allclose(losses[:, j], fold_loss_at_lambda(prep, lam), rtol=1e-10, atol=1e-10)
        assert np.isclose(np.mean(losses[:, j]), prep.evaluate(lam).value, rtol=1e-10, atol=1e-10)


def test_last_fold_only_is_one_curve(observed):
    r = _run(observed, max_folds=1, compare_one_step=False)
    assert len(r.origins) == 1
    assert np.allclose(r.pooled_losses, r.fold_losses[0])
    assert np.isclose(r.pooled_s, r.last_s, atol=1e-8)
    assert r.one_step_s is None


def test_holdout_disabled_predicts_beyond_last_observation(observed):
    r = _run(observed, holdout=False, compare_one_step=False)
    assert r.selected_origin == len(observed)
    assert r.test_mse == {}
    assert r.origins[-1] + r.horizon <= len(observed)
    assert all(len(f) == 3 and np.all(np.isfinite(f)) for f in r.future_forecasts.values())


def test_native_polynomial_forecast_is_consistent(observed):
    for order in (1, 2, 3):
        trend, forecast = fit_window_forecast(
            observed, origin=70, window=24,
            order=order, horizon=4, smoothness=0.73,
        )
        assert trend.size == 24 and forecast.size == 4
        if order == 1:
            assert np.allclose(forecast, trend[-1])
        if order == 2:
            assert np.allclose(forecast, trend[-1] + np.arange(1, 5) * (trend[-1] - trend[-2]))


def test_export_tables_have_consistent_shape(observed):
    r = _run(observed, grid_points=21, max_folds=4)
    matrix = r.loss_table()
    minima = r.minima_table()
    assert len(matrix) == len(minima) == 4
    assert len([c for c in matrix if c.startswith("S=")]) == 21
    assert np.all(minima["validation_end_1based"] <= r.selected_origin) if (
        "validation_end_1based" in minima.columns
    ) else np.all(matrix["validation_end_1based"] <= r.selected_origin)
    assert np.all(np.isfinite(minima["mse_at_pooled_s"]))


def test_invalid_inputs_raise_clear_error(observed):
    with pytest.raises(ValueError):
        _run(observed, order=5)
    with pytest.raises(ValueError):
        _run(observed[:24], window=22, horizon=3)
    with pytest.raises(ValueError):
        _run(np.r_[observed[:-1], np.nan])
