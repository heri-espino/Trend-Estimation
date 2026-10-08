"""The two article trend designs are shared by both Streamlit applications."""
from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from scipy.stats import beta

from experiments.smoothness_cv.article_simulations import (
    ARTICLE_TRENDS, article_trend, make_article_synthetic,
    quarterly_seasonality,
)
from experiments.smoothness_cv.live_lab import make_synthetic

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("n", [50, 200])
def test_linear_trend_is_exact_four_t_over_n(n):
    t = np.arange(1, n+1, dtype=float)
    actual = article_trend("linear", n)
    np.testing.assert_allclose(actual, 4*t/n, rtol=0, atol=1e-14)
    assert actual[0] == pytest.approx(4/n)
    assert actual[-1] == pytest.approx(4.0)


@pytest.mark.parametrize("n", [50, 200])
def test_nonlinear_trend_uses_correct_two_beta_pdfs(n):
    u = np.arange(1, n+1, dtype=float)/n
    actual = article_trend("beta_mixture", n)
    reference = 0.6*beta.pdf(u, 30, 17) + 0.4*beta.pdf(u, 3, 11)
    np.testing.assert_allclose(actual, reference, rtol=1e-14, atol=1e-14)
    assert np.all(np.isfinite(actual))
    assert actual[-1] == pytest.approx(0.0, abs=1e-14)


def test_article_quarterly_effects_repeat_every_four_observations():
    seasonal = quarterly_seasonality(13)
    np.testing.assert_array_equal(
        seasonal,
        [1, -0.5, -2.5, 2] * 3 + [1],
    )
    for q in range(0, 12, 4):
        assert seasonal[q:q+4].sum() == pytest.approx(0)


@pytest.mark.parametrize("kind", ["linear", "beta_mixture"])
@pytest.mark.parametrize("n", [50, 200])
@pytest.mark.parametrize("sigma", [0.5, 2.0])
def test_article_noise_and_seasonality_preserve_latent_trend(kind, n, sigma):
    base = make_article_synthetic(
        kind, n=n, noise_sd=sigma, seasonality=False, seed=82
    )
    season = make_article_synthetic(
        kind, n=n, noise_sd=sigma, seasonality=True, seed=82
    )
    same = make_article_synthetic(
        kind, n=n, noise_sd=sigma, seasonality=True, seed=82
    )
    pd.testing.assert_frame_equal(season, same)
    np.testing.assert_allclose(base["latent"], article_trend(kind, n))
    np.testing.assert_allclose(season["latent"], base["latent"])
    np.testing.assert_allclose(
        season["observed"]-base["observed"], quarterly_seasonality(n),
        atol=1e-13,
    )
    residual = (base["observed"]-base["latent"]).to_numpy()
    noise_reference = make_synthetic(
        "0", n, sigma, "Gaussian", 0.0, 82
    )["observed"].to_numpy()
    np.testing.assert_allclose(residual, noise_reference, atol=1e-13)
    assert len(season) == n
    np.testing.assert_array_equal(season["t"], np.arange(1, n+1))


def test_zero_noise_splits_trend_from_quarterly_component():
    y = make_article_synthetic(
        "beta_mixture", 50, noise_sd=0.0, seasonality=True
    )
    np.testing.assert_allclose(
        y["observed"], y["latent"]+y["seasonal"], atol=1e-14
    )


@pytest.mark.parametrize("path", [
    "apps/pooled_forecast_cv.py",
    "apps/smoothness_lab.py",
    "apps/smoothness_lab_advanced.py",
])
def test_both_streamlits_expose_identical_article_presets(path):
    source = (ROOT/path).read_text(encoding="utf-8")
    ast.parse(source, filename=path)
    for snippet in (
        "ARTICLE_TRENDS", "make_article_synthetic",
        "estacionalidad", "Desviación estándar del ruido gaussiano",
        "Número de observaciones, N", "min_value=50", "max_value=200",
        "Desviación estándar del ruido gaussiano, σ",
        "min_value=0.5", "max_value=2.0", "st.slider(",
    ):
        assert snippet in source
    assert set(ARTICLE_TRENDS.values()) == {"linear", "beta_mixture"}



def test_article_n50_works_with_short_chronological_cv():
    from experiments.smoothness_cv.branch_rule_lab import run_branch_lab
    from experiments.smoothness_cv.live_lab import run_lab

    frame = make_article_synthetic("linear", n=50, seed=32)
    observed = frame["observed"].to_numpy()
    direct = run_lab(
        observed, order=2, window=25, horizon=3,
        step=3, max_origins=3, test_size=3,
        rule="last", grid_points=11, search_depth=2,
    )
    assert 0 <= direct.final_s <= 1
    branches = run_branch_lab(
        observed, orders=(2,), rules=("last",),
        window=25, horizon=3, step=3, max_origins=3,
        test_size=3, min_support=0.25,
        grid_points=11, search_depth=2,
    )
    assert 0 <= branches.selected_s <= 1
    assert len(branches.evaluation_forecast) == 3


def test_reject_invalid_trend_and_noise_inputs():
    for kind, n in [("other", 200), ("linear", 29), ("linear", 3001)]:
        with pytest.raises(ValueError):
            article_trend(kind, n)
    with pytest.raises(ValueError):
        make_article_synthetic("linear", 50, noise_sd=-0.5)
