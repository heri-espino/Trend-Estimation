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




def test_empty_v_history_is_valid_for_first_origin():
    """An empty V must expose the same columns as completed V records."""
    from experiments.smoothness_cv.branch_rule_lab import _safe_rule

    empty_v = pd.DataFrame(columns=[
        "origin", "val2_end", "s_minimo", "val2_mse"
    ])
    for name in ("last", "mean_k3", "val2_weighted"):
        applied, raw, metadata, n = _safe_rule(
            RULE_SPECS[name], current_s=0.9,
            prior=empty_v, observed_at=10,
        )
        assert n == 0
        assert np.isclose(applied, 0.9)
        assert np.isclose(raw, 0.9)


def test_v_matrix_has_consistent_schema_with_completed_errors():
    result = _run(_sample())
    frame = result.evaluations
    assert {"val2_mse", "val2_rmse", "val1_mse"}.issubset(frame)
    assert np.isfinite(frame["val2_mse"]).all()
    assert np.isfinite(frame["val2_rmse"]).all()

def test_tracks_methods_v_matrices_and_all_orders():
    result = _run(_sample())
    assert set(result.evaluations["d"]) == {1, 2}
    assert set(result.evaluations["regla"]) == {
        "last", "mean_k3", "val2_weighted"
    }
    assert set(result.branches["d"]) == {1, 2}
    assert set(result.branches["regla"]) == set(result.evaluations["regla"])
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
                "val2_mse"
            ].to_numpy(float),
            current_s=float(row.s_minimo),
        )
        assert np.isclose(
            float(np.clip(raw_s, 0, 1)), row.s_aplicado,
        )


def test_each_rule_has_own_v1_minima_and_independent_branch_history():
    data = _sample()
    result = _run(data, step=3, max_origins=6, track_epsilon=0.29)
    v = result.evaluations
    b = result.branches
    # A branch label is meaningful only together with its order AND its rule.
    pd.testing.assert_frame_equal(
        b[["d", "regla", "rama", "origin", "s_aplicado"]]
        .sort_values(["d", "regla", "rama", "origin"])
        .reset_index(drop=True),
        v[["d", "regla", "rama", "origin", "s_aplicado"]]
        .sort_values(["d", "regla", "rama", "origin"])
        .reset_index(drop=True),
    )
    for row in b.itertuples():
        assert row.regla in RULE_SPECS
        assert np.isfinite(row.s_aplicado)
        if row.regla == "last":
            assert np.isclose(row.s_minimo, row.s_aplicado)
    # Method-specific V1 objective equals E1(phi_r(history, s_input)).
    # We test this directly using a fully completed, causally available history.
    candidate = v.loc[
        v["regla"].eq("mean_k3")
        & v["n_historial_disponible"].gt(0)
    ].iloc[0]
    past = v.loc[
        v["d"].eq(candidate["d"])
        & v["rama"].eq(candidate["rama"])
        & v["regla"].eq(candidate["regla"])
        & v["origin"].lt(candidate["origin"])
        & v["val2_end"].le(candidate["val1_end"])
    ].sort_values("origin")
    applied, _ = apply_rule(
        RULE_SPECS["mean_k3"],
        history_s=past["s_minimo"].to_numpy(float),
        history_val2_loss=past["val2_mse"].to_numpy(float),
        current_s=float(candidate["s_minimo"]),
    )
    assert np.isclose(float(np.clip(applied, 0, 1)), candidate["s_aplicado"])


def test_loss_weighted_rule_identifies_flat_v1_objective():
    from experiments.smoothness_cv.branch_rule_lab import _method_minima

    data = _sample()
    a, b = 26, 28
    split = td.RollingOriginSplit(
        train=slice(a-26, a), validation=slice(a, b)
    )
    prepared = td.prepare_rolling_pure_forecast_objective(
        data[:b], [split], order=2
    )
    history = pd.DataFrame({
        "origin": [1, 2], "val2_end": [15, 20],
        "s_minimo": [0.25, 0.8],
        "val2_mse": [1.0, 0.1],
    })
    candidates = _method_minima(
        prepared, order=2, window=26,
        rule=RULE_SPECS["val2_weighted"],
        history=history, observed_at=b,
        spacing=0.02, depth=2, last_input=0.4,
    )
    assert len(candidates) == 1
    assert candidates[0]["objetivo_plano"]
    assert candidates[0]["source"] == "objetivo_plano"
    assert np.isclose(candidates[0]["s_minimo"], 0.4)


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
    assert app._branch_figure(r, d, r.selected_rule).layout.yaxis.title.text
    assert app._historical_loss_figure(r, d, r.selected_rule).data
    assert app._branch_rank_figure(r).data
    assert app._v_figure(
        subset, d, str(first["rama"]), str(first["regla"])
    ).data
    assert app._v_losses(
        subset, d, str(first["rama"]), str(first["regla"])
    ).data
    assert app._branch_timeline(r).data
