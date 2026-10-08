from __future__ import annotations

from types import SimpleNamespace

import pytest

from experiments.smoothness_cv.make_workflow_tutorial_figure import (
    HORIZON, NAME, OUTER_NUMBER, RULES, SEED, WINDOW, _positions,
)


def test_workflow_uses_fixed_ex_ante_example():
    assert NAME == "fig_workflow_tutorial"
    assert SEED == 100
    assert OUTER_NUMBER == 8
    assert WINDOW == 120
    assert HORIZON == 20
    assert set(RULES) == {"pooled_cv_same_config", "last", "recency_hl3"}


def test_workflow_chronology_is_half_open_and_non_overlapping():
    # Historical train: 40..160; historical Val1: 160..180;
    # historical Val2: 180..200; current Val1: 240..260; test: 260..280.
    split = SimpleNamespace(validation=slice(160, 180))
    ranges = _positions(280, split)
    assert ranges == {
        "train": (40, 160),
        "val1": (160, 180),
        "val2": (180, 200),
        "current": (240, 260),
        "test": (260, 280),
    }


def test_workflow_rejects_validation_overlap_with_current_val1():
    split = SimpleNamespace(validation=slice(230, 250))
    with pytest.raises(ValueError, match="overlap"):
        _positions(280, split)


def test_workflow_rejects_impossible_training_window():
    split = SimpleNamespace(validation=slice(80, 100))
    with pytest.raises(ValueError, match="Invalid chronological region"):
        _positions(280, split)
