"""Contracts for the NEW shared weighted-F / branch-tracking protocol.

Separate from historical CP04--CP08 and the earlier Val1/Val2 lab.
"""
import numpy as np
import pytest

from experiments.smoothness_cv.weighted_surface_study import (
    LossWeighting,
    grid_local_minima,
    run_weighted_surface_study,
    track_grid_branches,
    weighted_surface_history,
)


def test_weighted_surface_uses_only_current_and_earlier_losses():
    folds = np.array([[1., 10.], [2., 20.], [3., 30.], [4., 40.]])
    uniform = weighted_surface_history(folds, LossWeighting("all", "uniform"))
    recent = weighted_surface_history(
        folds, LossWeighting("last2", "uniform", lookback=2)
    )
    exp = weighted_surface_history(
        folds, LossWeighting("exp", "exponential", lookback=2, decay=0.5)
    )
    assert np.allclose(uniform[:, 0], [1., 1.5, 2., 2.5])
    assert np.allclose(recent[-1], [3.5, 35.])
    assert np.allclose(exp[-1], [11. / 3., 110. / 3.])
    changed = folds.copy()
    changed[-1] = [1_000., 1_000.]
    assert np.array_equal(
        weighted_surface_history(changed, LossWeighting("all"))[:-1],
        uniform[:-1],
    )


def test_bad_weights_and_loss_matrices_rejected():
    with pytest.raises(ValueError):
        LossWeighting("negative", "exponential", decay=-0.4).weights(3)
    with pytest.raises(ValueError):
        LossWeighting("bad", "uniform", lookback=0).weights(3)
    with pytest.raises(ValueError):
        weighted_surface_history(np.array([1., 2.]), LossWeighting("all"))
    with pytest.raises(ValueError):
        weighted_surface_history(np.array([[-1., 2.]]), LossWeighting("all"))


def test_grid_minima_include_boundaries_and_multiple_valleys():
    s = np.linspace(0, 1, 11)
    f = np.full(len(s), 10.)
    f[[0, 4, 8, 10]] = [1., 0.4, 0.2, 0.1]
    minima = grid_local_minima(s, f)
    assert np.allclose([m[0] for m in minima], [0., 0.4, 0.8, 1.0])


def test_correspondence_maximizes_matches_before_distance():
    # Greedy nearest-first could match .40 -> .43 and lose the other match.
    # Correct maximum-cardinality links are .40 -> .34, .48 -> .43.
    s = np.linspace(0, 1, 101)
    curves = np.full((2, len(s)), 3.0)
    for value in [0.40, 0.48]:
        curves[0, np.argmin(abs(s - value))] = 0.
    for value in [0.34, 0.43]:
        curves[1, np.argmin(abs(s - value))] = 0.
    branches = track_grid_branches(s, curves, radius=0.10)
    assert len(branches) == 4
    origins = branches[branches.step == 0].sort_values("s_local")
    nexts = branches[branches.step == 1].sort_values("s_local")
    assert origins.branch.tolist() == nexts.branch.tolist()


@pytest.fixture(scope="module")
def series():
    t = np.arange(91, dtype=float)
    return 10 + 0.02 * t + np.sin(t / 9) + .10 * np.random.default_rng(18).normal(size=t.size)


def _analyze(y):
    return run_weighted_surface_study(
        y, methods=(
            LossWeighting("all", "uniform"),
            LossWeighting("exponential", "exponential", lookback=4, decay=.6),
        ),
        orders=(1, 2), window=23, horizon=3, stride=4,
        max_folds=6, grid_points=21, refine_pooled=False,
        branch_min_support=2, holdout=True,
    )


def test_both_papers_use_identical_inputs_but_distinct_decision_rules(series):
    result = _analyze(series)
    assert len(result.summary) == 4
    assert result.surfaces.keys() == {
        ("all", 1), ("all", 2), ("exponential", 1), ("exponential", 2)
    }
    for row in result.summary.itertuples():
        assert 0 <= row.pooled_s <= 1
        assert 0 <= row.tracked_s <= 1
        assert np.isfinite(row.pooled_historical_mse)
        assert np.isfinite(row.tracked_historical_score)
        assert row.h == 3 and row.L == 23
        assert row.n_folds == len(result.origins)
        assert np.isfinite(row.pooled_test_mse)
        assert np.isfinite(row.tracked_test_mse)
    assert {"step", "branch", "s_local", "F_local", "method", "d"}.issubset(result.branches)
    assert not any("val2" in str(col).lower() for col in result.branches.columns)


def test_untouched_test_values_cannot_change_either_selector(series):
    original = _analyze(series)
    tampered = series.copy()
    tampered[-3:] = [1e3, -1e3, 2e3]
    altered = _analyze(tampered)
    keys = [
        "method", "d", "pooled_s", "pooled_historical_mse",
        "tracked_s", "tracked_branch", "tracked_support", "tracked_historical_score",
    ]
    assert original.summary[keys].equals(altered.summary[keys])
    for key in original.surfaces:
        assert np.array_equal(original.surfaces[key], altered.surfaces[key])
    assert original.branches.equals(altered.branches)
    assert np.any(original.summary["pooled_test_mse"] != altered.summary["pooled_test_mse"])


def test_no_holdout_outputs_predictions_but_no_test_scores(series):
    r = run_weighted_surface_study(
        series, methods=(LossWeighting("all"),),
        orders=(2,), window=24, horizon=3, stride=4,
        max_folds=4, grid_points=21, refine_pooled=False, holdout=False,
    )
    assert len(r.summary) == 1
    assert r.selected_origin == series.size
    assert np.isnan(r.summary.iloc[0].pooled_test_mse)
    assert np.isnan(r.summary.iloc[0].tracked_test_mse)
