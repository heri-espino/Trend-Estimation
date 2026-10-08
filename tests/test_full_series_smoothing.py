"""The two CV treatments share a descriptive full-series smoother only.

The complete smoothing refit must never enter forecast validation or model
selection, especially when the user has enabled a final held-out test.
"""
from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import trend_estimation as td
from experiments.smoothness_cv.full_series import smooth_full_series
from experiments.smoothness_cv.article_simulations import make_article_synthetic

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("n", [50, 120])
@pytest.mark.parametrize("order", [1, 2, 3, 4])
@pytest.mark.parametrize("smoothness", [0.0, 0.35, 0.9, 1.0])
def test_complete_smoother_matches_original_penalized_least_squares(
    n, order, smoothness
):
    y = make_article_synthetic("linear", n=n, noise_sd=0.5, seed=13)[
        "observed"
    ].to_numpy(float)
    original = y.copy()
    full = smooth_full_series(y, order=order, smoothness=smoothness)
    expected = td.PurePenalizedTrend(
        order=order, smoothness=smoothness
    ).fit(y).trend_
    assert len(full) == n
    np.testing.assert_allclose(full, expected, rtol=1e-10, atol=1e-10)
    np.testing.assert_allclose(y, original)
    if smoothness == 0.0:
        np.testing.assert_allclose(full, y, atol=1e-10)


def test_complete_fit_uses_test_data_but_does_not_modify_pretest_selection():
    from experiments.smoothness_cv.pooled_lab import analyze_pooled

    y = make_article_synthetic(
        "beta_mixture", n=70, noise_sd=0.5, seed=23
    )["observed"].to_numpy(float)
    before = analyze_pooled(
        y, window=25, order=2, horizon=3, stride=3,
        max_folds=4, grid_points=21, refine=False, holdout=True,
        compare_one_step=False,
    )
    changed = y.copy()
    changed[-3:] += 5
    after = analyze_pooled(
        changed, window=25, order=2, horizon=3, stride=3,
        max_folds=4, grid_points=21, refine=False, holdout=True,
        compare_one_step=False,
    )
    assert before.pooled_s == after.pooled_s
    np.testing.assert_allclose(before.pooled_losses, after.pooled_losses)
    pooled_all = smooth_full_series(
        y, order=before.order, smoothness=before.pooled_s,
    )
    pooled_changed = smooth_full_series(
        changed, order=after.order, smoothness=after.pooled_s,
    )
    assert not np.allclose(pooled_all, pooled_changed)


@pytest.mark.parametrize("path", [
    "apps/pooled_forecast_cv.py",
    "apps/smoothness_lab.py",
    "apps/smoothness_lab_advanced.py",
    "apps/dynamic_branch_cv.py",
])
def test_labs_have_distinct_names_and_keep_valid_python(path):
    source = (ROOT / path).read_text(encoding="utf-8")
    ast.parse(source, filename=path)
    if path.endswith("pooled_forecast_cv.py"):
        assert "Laboratorio de CV · Promedio histórico de F(S)" in source
        assert "pooled_tendencia_completa" in source
        assert "make_article_synthetic" in source
    if path.endswith("/smoothness_lab.py"):
        assert "Laboratorio de CV dinámico · Seguimiento de ramas" in source
        assert "ramas_tendencia_completa" in source
    if path.endswith("/smoothness_lab_advanced.py"):
        assert "Versión histórica (legado)" in source
        assert "legado_tendencia_completa" in source
    if path.endswith("/dynamic_branch_cv.py"):
        assert "from apps.smoothness_lab import main" in source


def test_visualizations_of_complete_trend_are_distinct():
    pytest.importorskip("streamlit")
    pytest.importorskip("plotly")

    import apps.pooled_forecast_cv as pooled
    import apps.smoothness_lab as dynamic

    frame = make_article_synthetic("linear", n=50, noise_sd=0.5)
    trend = smooth_full_series(frame["observed"], order=2, smoothness=0.6)
    original = frame.copy()
    # Numeric axes and known true trend in a synthetic series.
    pooled_fig = pooled.complete_trend_plot(
        frame, trend, order=2, smoothness=0.6,
    )
    branch_fig = dynamic._full_series_figure(
        frame, trend, d=2, s=0.6, unidad="Unidades",
    )
    assert len(pooled_fig.data) == 3
    assert len(branch_fig.data) == 3
    np.testing.assert_allclose(pooled_fig.data[1].y, trend)
    np.testing.assert_allclose(branch_fig.data[1].y, trend)
    assert "Tendencia completa" in branch_fig.data[1].name
    assert "Tendencia completa" in pooled_fig.data[1].name
    pd.testing.assert_frame_equal(frame, original)
    # Date axes also work.
    frame["date"] = pd.date_range("2026-01-01", periods=50)
    assert pooled.complete_trend_plot(
        frame, trend, order=2, smoothness=0.6
    ).layout.xaxis.title.text == "Fecha"
    assert dynamic._full_series_figure(
        frame, trend, d=2, s=0.6, unidad="Unidades"
    ).layout.xaxis.title.text == "Fecha"


@pytest.mark.parametrize("kwargs", [
    {"order": 2, "smoothness": -0.01},
    {"order": 2, "smoothness": 1.01},
    {"order": 0, "smoothness": 0.5},
    {"order": 5, "smoothness": 0.5},
])
def test_reject_unusable_complete_smoothing_parameters(kwargs):
    with pytest.raises(ValueError):
        smooth_full_series([1.0, 2.0, 3.0], **kwargs)
    with pytest.raises(ValueError):
        smooth_full_series([float("nan")] * 50, **kwargs)
