"""Chronological contracts for the multi-order, branch-and-rule smoothness lab."""
from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import trend_estimation as td
from experiments.smoothness_cv.dynamic_branch_rules import apply_rule
from experiments.smoothness_cv.branch_rule_lab import (
    RULE_SPECS, run_branch_lab,
)
from experiments.smoothness_cv.live_lab import make_synthetic


APP_PATH = Path(__file__).resolve().parents[1] / "apps" / "smoothness_lab.py"


def _sample():
    return make_synthetic(
        "12 + 0.025*t + sin(t/13)", 96, 0.25, seed=19
    )["observed"].to_numpy(float)


def _run(series, **overrides):
    params = dict(
        orders=(1, 2),
        rules=("last", "mean_k3", "val2_weighted"),
        window=26, horizon=2, step=3, max_origins=4, test_size=3,
        future_horizon=4, grid_points=11, max_branches=3,
        min_support=0.25, search_depth=2,
    )
    params.update(overrides)
    return run_branch_lab(series, **params)


def test_main_app_contains_branch_sections_and_spanish_labels():
    source = APP_PATH.read_text(encoding="utf-8")
    ast.parse(source, filename=str(APP_PATH))
    for phrase in (
        "Seguimiento histórico de ramas (general)",
        "Selección directa en dos bloques (caso particular)",
        "Validación 1: ECM y mínimos por d",
        "Trayectorias de ramas",
        "Matrices V: suavidades y errores",
        "Validación 2: reglas y comparación",
        "Tendencia, prueba y pronóstico",
        "Mostrar evaluación retrospectiva y los valores de prueba",
    ):
        assert phrase in source


def test_tracks_methods_v_matrices_and_all_orders():
    result = _run(_sample())
    assert set(result.evaluations["d"]) == {1, 2}
    assert set(result.evaluations["regla"]) == {
        "last", "mean_k3", "val2_weighted"
    }
    assert set(result.branches["d"]) == {1, 2}
    assert result.summary.shape[0] >= 2
    assert result.selected_rule in set(result.evaluations["regla"])
    assert result.selected_branch in set(result.branches["rama"])
    assert 0 <= result.selected_s <= 1
    assert np.all(result.evaluations["s_aplicado"].between(0, 1))
    assert np.all(result.evaluations["s_minimo"].between(0, 1))
    assert set([
        "s_minimo", "s_aplicado", "val1_mse", "val2_mse",
        "val1_end", "val2_end", "n_historial_disponible",
    ]).issubset(result.evaluations.columns)
    assert (
        result.historical_surfaces.groupby(["d", "origin"]).size() == 11
    ).all()


def test_last_rule_keeps_original_local_minimum_and_polynomial_forecast():
    y = _sample()
    result = _run(y)
    v = result.evaluations
    rows = v.loc[v["regla"].eq("last")]
    np.testing.assert_allclose(rows["s_aplicado"], rows["s_minimo"])
    for row in rows.head(6).itertuples():
        fit = td.PurePenalizedTrend(
            order=int(row.d), smoothness=float(row.s_aplicado)
        ).fit(y[int(row.val1_end)-26:int(row.val1_end)])
        forecast = fit.forecast(2)
        actual = y[int(row.val1_end):int(row.val2_end)]
        assert np.isclose(float(np.mean((forecast-actual)**2)), row.val2_mse)


def test_all_rules_apply_same_s_on_val1_and_val2():
    y = _sample()
    result = _run(y)
    for row in result.evaluations.head(6).itertuples():
        d = int(row.d)
        b = int(row.val1_end)
        a = int(row.val1_start)
        prepared = td.prepare_rolling_pure_forecast_objective(
            y[:b],
            [td.RollingOriginSplit(
                train=slice(a-26, a), validation=slice(a, b)
            )],
            order=d,
        )
        lam = td.smoothness_to_lambda(float(row.s_aplicado), 26, d)
        assert np.isclose(
            float(prepared.evaluate(lam).value), row.val1_mse
        )
        fit = td.PurePenalizedTrend(
            order=d, smoothness=float(row.s_aplicado)
        ).fit(y[b-26:b])
        target = y[b:int(row.val2_end)]
        assert np.isclose(
            float(np.mean((fit.forecast(2)-target)**2)), row.val2_mse,
        )


def test_late_validation_losses_are_not_known_to_past_rules():
    result = _run(_sample(), step=1, horizon=3)
    v = result.evaluations
    for row in v.itertuples():
        group = v.loc[
            v["d"].eq(row.d)
            & v["rama"].eq(row.rama)
            & v["regla"].eq(row.regla)
            & v["origin"].lt(row.origin)
            & v["val2_end"].le(row.val1_end)
        ]
        assert row.n_historial_disponible == len(group)
        spec = RULE_SPECS[row.regla]
        raw_s, _ = apply_rule(
            spec,
            history_s=group.sort_values("origin")[
                "s_minimo"
            ].to_numpy(float),
            history_val2_loss=group.sort_values("origin")[
                "val2_rmse"
            ].to_numpy(float),
            current_s=float(row.s_minimo),
        )
        assert np.isclose(
            float(np.clip(raw_s, 0, 1)), row.s_aplicado,
        )


def test_polynomial_last_baseline_is_always_included():
    result = _run(_sample(), rules=("mean_k3",))
    assert set(result.evaluations["regla"]) == {"last", "mean_k3"}


def test_reserved_test_does_not_affect_branch_selection_or_backtest():
    y = _sample()
    result = _run(y)
    changed = y.copy()
    changed[-3:] = [1000., -800., 600.]
    other = _run(changed)
    pd.testing.assert_frame_equal(result.branches, other.branches)
    pd.testing.assert_frame_equal(result.evaluations, other.evaluations)
    pd.testing.assert_frame_equal(result.summary, other.summary)
    assert (result.selected_order, result.selected_branch, result.selected_rule) == (
        other.selected_order, other.selected_branch, other.selected_rule
    )
    assert result.selected_s == other.selected_s
    np.testing.assert_allclose(
        result.evaluation_forecast, other.evaluation_forecast
    )
    assert result.forecast_start == len(y)
    assert result.forecast.shape == (4,)
    assert result.evaluation_forecast.shape == (3,)
    assert not np.allclose(result.forecast, other.forecast)


def test_selection_minimizes_mean_val2_loss_with_support_constraint():
    result = _run(_sample())
    feasible = result.summary.loc[result.summary["elegible"]]
    assert not feasible.empty
    chosen = feasible.loc[
        feasible["d"].eq(result.selected_order)
        & feasible["rama"].eq(result.selected_branch)
        & feasible["regla"].eq(result.selected_rule)
    ].iloc[0]
    assert np.isclose(
        chosen["ec_medio_val2"], feasible["ec_medio_val2"].min()
    )
    assert np.isclose(
        result.selected_val2_rmse**2, result.selected_val2_mse
    )


def test_validation_rejects_unknown_rules_and_short_data():
    with pytest.raises(ValueError):
        _run(_sample(), rules=("not_a_rule",))
    with pytest.raises(ValueError):
        _run(_sample(), orders=())
    with pytest.raises(ValueError):
        _run(_sample()[:30])


@pytest.fixture(scope="module")
def app():
    pytest.importorskip("plotly")
    pytest.importorskip("streamlit")
    import apps.smoothness_lab as dashboard

    return dashboard


def test_branch_figures_and_v_matrices_render(app):
    r = _run(_sample())
    d = r.selected_order
    df = r.evaluations
    first = df[df["d"].eq(d)].iloc[0]
    subset = df[
        df["d"].eq(d) & df["rama"].eq(first["rama"])
        & df["regla"].eq(first["regla"])
    ]
    assert app._branch_figure(r, d).layout.yaxis.title.text
    assert app._historical_loss_figure(r, d).data
    assert app._branch_rank_figure(r).data
    assert app._v_figure(
        subset, d, str(first["rama"]), str(first["regla"])
    ).data
    assert app._v_losses(
        subset, d, str(first["rama"]), str(first["regla"])
    ).data
    assert app._branch_timeline(r).data
