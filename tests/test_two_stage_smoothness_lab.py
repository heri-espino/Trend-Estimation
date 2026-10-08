"""Pruebas del laboratorio de selección directa con dos validaciones."""
from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.smoothness_cv.live_lab import make_synthetic
from experiments.smoothness_cv.two_stage_lab import run_two_stage_lab


APP = Path(__file__).resolve().parents[1] / "apps" / "smoothness_lab.py"


def _sample(n=88, seed=18):
    return make_synthetic(
        "10 + 0.03*t + 0.6*sin(t/8)", n, 0.16, seed=seed
    )["observed"].to_numpy(dtype=float)


def _run(y, *, orders=(1, 2)):
    return run_two_stage_lab(
        y, orders=orders, window=26, horizon=3,
        test_size=4, future_horizon=4, search_depth=3, grid_points=15,
    )


def test_main_ui_is_valid_python_and_identifies_three_stages():
    source = APP.read_text(encoding="utf-8")
    ast.parse(source, filename=str(APP))
    for label in (
        "Validación 1: mínimos de S",
        "Validación 2: elección de d y S",
        "Tendencia y pronóstico",
        "División cronológica",
        "Matriz de comparación de candidatos",
    ):
        assert label in source


def test_val1_minima_are_all_evaluated_on_val2_for_each_order():
    result = _run(_sample())
    assert set(result.candidates["d"]) == {1, 2}
    assert len(result.candidates) >= 2
    assert set(["d", "smoothness", "val1_mse", "val2_mse", "val2_rmse"]).issubset(
        result.candidates.columns
    )
    assert (result.candidates["smoothness"].between(0, 1)).all()
    assert np.isclose(result.selected_s, result.candidates.iloc[0]["smoothness"])
    assert result.selected_order == int(result.candidates.iloc[0]["d"])
    assert np.isclose(
        result.selected_val2_mse,
        result.candidates["val2_mse"].min(),
    )
    assert result.candidates["rank"].tolist() == list(
        range(1, len(result.candidates) + 1)
    )
    assert result.surfaces.groupby("d").size().to_dict() == {1: 15, 2: 15}


def test_fit_val1_val2_and_final_forecast_are_chronologically_disjoint():
    data = _sample()
    result = _run(data)
    assert result.train_start == len(data) - result.window
    assert result.val1_end == result.val1_start + result.horizon
    assert result.val2_end == result.val1_end + result.horizon
    assert result.pretest_end == result.val2_end
    assert result.test_end == len(data)
    assert result.test_end - result.pretest_end == 4
    assert result.trend.shape == (26,)
    assert result.forecast.shape == (4,)
    assert result.evaluation_trend.shape == (26,)
    assert result.evaluation_forecast.shape == (4,)
    assert result.forecast_start == len(data)
    assert result.forecast_end == len(data) + 4
    assert np.all(np.isfinite(result.trend))


def test_changing_test_targets_never_changes_model_selection_or_forecasts():
    data = _sample()
    original = _run(data)
    changed = data.copy()
    changed[-4:] = np.array([10_000.0, -2000., -1000., 8000.])
    altered = _run(changed)
    assert original.selected_order == altered.selected_order
    assert original.selected_s == altered.selected_s
    pd.testing.assert_frame_equal(original.candidates, altered.candidates)
    pd.testing.assert_frame_equal(original.surfaces, altered.surfaces)
    np.testing.assert_allclose(
        original.evaluation_trend, altered.evaluation_trend
    )
    np.testing.assert_allclose(
        original.evaluation_forecast, altered.evaluation_forecast
    )
    # Las observaciones de prueba sí pasan al nuevo reajuste operativo:
    # cambiar esos datos debe alterar normalmente el pronóstico futuro.
    assert not np.allclose(original.forecast, altered.forecast)


def test_smoothing_parameters_are_reused_without_val2_reoptimization():
    import trend_estimation as td

    data = _sample()
    result = _run(data)
    final = td.PurePenalizedTrend(
        order=result.selected_order, smoothness=result.selected_s
    ).fit(data[-26:])
    np.testing.assert_allclose(final.trend_, result.trend)
    np.testing.assert_allclose(final.forecast(4), result.forecast)
    evaluation = td.PurePenalizedTrend(
        order=result.selected_order, smoothness=result.selected_s
    ).fit(data[result.pretest_end-26:result.pretest_end])
    np.testing.assert_allclose(
        evaluation.forecast(4), result.evaluation_forecast
    )


def test_missing_orders_and_insufficient_data_are_rejected():
    with pytest.raises(ValueError):
        _run(_sample(), orders=())
    with pytest.raises(ValueError):
        run_two_stage_lab(
            _sample(40), window=35, horizon=3, test_size=4
        )


@pytest.fixture(scope="module")
def app():
    pytest.importorskip("plotly")
    pytest.importorskip("streamlit")
    import apps.smoothness_lab as module

    return module


def test_candidate_plot_highlights_minimum_val2_error(app):
    result = _run(_sample(), orders=(1,))
    fig = app._val2_figure(result)
    assert "validación 2" in fig.layout.title.text
    assert "Modelo seleccionado" in [trace.name for trace in fig.data]


def test_forecast_graph_supports_dates_and_integer_indices(app):
    result = _run(_sample(), orders=(1,))
    values = _sample()
    for dated in (False, True):
        frame = pd.DataFrame({"observed": values})
        if dated:
            frame["date"] = pd.date_range("2024-01-01", periods=len(values))
        fig = app._forecast_figure(
            frame, result, "Valor observado", reveal=False, truth=False
        )
        assert fig.layout.xaxis.title.text == (
            "Fecha" if dated else "Número de observación"
        )
        assert any("Pronóstico futuro con S" in trace.name for trace in fig.data)
