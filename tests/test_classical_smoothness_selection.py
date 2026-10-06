import numpy as np

from trend_estimation.selection.classical import (
    pure_smoother_score,
    select_classical_pure_smoothness,
)


def test_classical_scores_are_finite_away_from_unsmoothed_endpoint():
    y = np.array([0.0, 0.2, 0.1, 0.5, 0.9, 1.1, 1.0, 1.4], dtype=float)

    for criterion in ("cv", "gcv", "aicc", "bic"):
        result = pure_smoother_score(
            y,
            order=2,
            smoothness=0.7,
            criterion=criterion,
        )
        assert np.isfinite(result.score)
        assert 0.0 <= result.smoothness <= 1.0
        assert result.edf >= 2.0
        assert result.edf <= y.size


def test_cv_and_gcv_reject_exact_unsmoothed_endpoint_via_infinite_score():
    y = np.linspace(0.0, 1.0, 10)

    cv = pure_smoother_score(y, order=2, smoothness=0.0, criterion="cv")
    gcv = pure_smoother_score(y, order=2, smoothness=0.0, criterion="gcv")

    assert np.isinf(cv.score)
    assert np.isinf(gcv.score)


def test_aicc_rejects_effective_dimension_too_close_to_sample_size():
    y = np.linspace(0.0, 1.0, 10)

    result = pure_smoother_score(
        y,
        order=2,
        smoothness=0.0,
        criterion="aicc",
    )
    assert np.isinf(result.score)


def test_grid_selector_returns_one_of_supplied_smoothness_values():
    y = np.array([0.0, 0.1, 0.3, 0.25, 0.6, 0.8, 0.75, 1.1, 1.2, 1.4])
    grid = np.linspace(0.0, 1.0, 21)

    selection = select_classical_pure_smoothness(
        y,
        order=2,
        criterion="gcv",
        smoothness_grid=grid,
    )

    assert np.any(np.isclose(selection.smoothness_, grid))
    assert np.isfinite(selection.score_)
    assert len(selection.scores_) == len(grid)


def test_bic_rejects_exact_interpolating_endpoint():
    y = np.linspace(0.0, 1.0, 10)

    result = pure_smoother_score(
        y,
        order=2,
        smoothness=0.0,
        criterion="bic",
    )
    assert np.isinf(result.score)
