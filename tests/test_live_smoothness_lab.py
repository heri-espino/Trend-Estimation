"""Regression tests for the live smoothness app's pure computation layer."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from experiments.smoothness_cv.live_lab import (
    RULES,
    make_synthetic,
    run_lab,
    smoothing_matrix,
    synthetic_function,
    transform_observations,
)


def _small_run(y, **options):
    settings = dict(
        order=2, window=28, horizon=2, step=3,
        max_origins=4, test_size=3, grid_points=11,
        search_depth=3, rule="mean_k3",
    )
    settings.update(options)
    return run_lab(y, **settings)


def test_custom_expression_is_vectorized_and_safe():
    s = synthetic_function("0.02*t + where(t>15, 2, 0) + sin(t/3)", 35)
    assert s.shape == (35,)
    assert s[20] > s[15]
    for unsafe in ("__import__('os').system('echo bad')", "t.__class__",
                   "[t for t in range(5)]", "t[0]"):
        with pytest.raises(ValueError):
            synthetic_function(unsafe, 35)


def test_synthetic_noise_is_reproducible():
    a = make_synthetic("0.02*t + sin(t/10)", 85, 0.25, "Gaussian", 0.3, 12)
    b = make_synthetic("0.02*t + sin(t/10)", 85, 0.25, "Gaussian", 0.3, 12)
    pd.testing.assert_frame_equal(a, b)
    assert "latent" in a.columns
    assert not np.allclose(a["observed"], a["latent"])


def test_transform_return_alignment():
    frame = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=4),
        "observed": [10., 11., 12.1, 13.31],
    })
    result = transform_observations(frame, "Simple return")
    assert len(result) == 3
    assert result["date"].iloc[0] == frame["date"].iloc[1]
    assert np.allclose(result["observed"], 0.1)


def test_synthetic_latent_truth_is_available_in_matching_units():
    sample = make_synthetic("2 + 0.01*t", 60, 0.1)
    levels = transform_observations(sample, "Level")
    logs = transform_observations(sample, "Log level")
    returns = transform_observations(sample, "Log return")
    assert np.allclose(levels["latent"], sample["latent"])
    assert np.allclose(logs["latent"], np.log(sample["latent"]))
    assert np.allclose(returns["latent"], np.diff(np.log(sample["latent"])))


def test_smoothing_matrix_is_symmetric_and_has_correct_normalized_s():
    s = 0.72
    H = smoothing_matrix(28, 2, s)
    assert np.allclose(H, H.T, atol=1e-11)
    assert np.linalg.eigvalsh(H).min() >= -1e-10
    assert np.isclose((28 - np.trace(H))/(28 - 2), s, atol=1e-7)


def test_dynamic_branches_and_validation_mse_are_available():
    y = make_synthetic("0.015*t + sin(t/8)", 88, 0.2, seed=13)["observed"].to_numpy()
    result = _small_run(y)
    assert not result.tracks.empty
    assert len(result.surfaces) == result.tracks["origin"].nunique() * 11
    assert {"smoothness", "val1_mse", "val2_mse", "val2_rmse"}.issubset(result.tracks)
    matched = result.tracks.loc[result.tracks["status"].eq("matched")]
    assert np.all(matched["val1_mse"] >= 0)
    assert np.all(matched["val2_mse"] >= 0)
    assert np.allclose(matched["val2_mse"], matched["val2_rmse"]**2)
    assert 0 <= result.final_s <= 1
    assert result.trend.size == 28
    assert result.forecast.size == 3
    assert result.selected_branch == "none" or result.selected_branch in set(result.tracks["branch_id"])


def test_untouched_test_values_never_change_selected_s():
    y = make_synthetic("0.02*t + cos(t/7)", 88, 0.12, seed=17)["observed"].to_numpy()
    base = _small_run(y, rule="recency_hl3")
    altered = y.copy()
    altered[-3:] = [500, -500, 1000]
    changed = _small_run(altered, rule="recency_hl3")
    assert base.selected_branch == changed.selected_branch
    assert base.final_s == changed.final_s
    assert base.pooled_s == changed.pooled_s
    pd.testing.assert_frame_equal(base.tracks, changed.tracks)
    assert np.allclose(base.forecast, changed.forecast)


def test_rule_family_exposes_cp08_trajectory_options():
    assert {"last", "recency_hl3", "mean_k3", "val2_weighted",
            "linear_k5", "delta_hl3"}.issubset(RULES)
