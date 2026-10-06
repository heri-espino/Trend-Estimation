from __future__ import annotations

import numpy as np
import pandas as pd

from experiments.smoothness_cv.dynamic_branch_rules import (
    DynamicRuleSpec,
    apply_rule,
    evaluate_rule_set,
)
from experiments.smoothness_cv.run_checkpoint_04 import _outer_stops


def test_recent_mean_and_median_include_current_s():
    history_s = np.array([0.2, 0.3, 0.4, 0.5])
    losses = np.ones(4)

    mean_s, _ = apply_rule(
        DynamicRuleSpec("mean_k3", "recent_mean", k=3),
        history_s=history_s,
        history_val2_loss=losses,
        current_s=0.8,
    )
    median_s, _ = apply_rule(
        DynamicRuleSpec("median_k3", "recent_median", k=3),
        history_s=history_s,
        history_val2_loss=losses,
        current_s=0.8,
    )

    assert np.isclose(mean_s, np.mean([0.4, 0.5, 0.8]))
    assert np.isclose(median_s, 0.5)


def test_recency_weighted_mean_favors_newer_smoothness():
    selected, meta = apply_rule(
        DynamicRuleSpec("recency", "recency_weighted", half_life=1.0),
        history_s=np.array([0.0, 0.0]),
        history_val2_loss=np.ones(2),
        current_s=1.0,
    )

    simple_mean = np.mean([0.0, 0.0, 1.0])
    assert selected > simple_mean
    assert selected < 1.0
    assert meta["includes_current_s"] is True
    assert np.isclose(meta["rho"], 0.5)


def test_val2_weighting_prefers_low_loss_historical_smoothness():
    selected, meta = apply_rule(
        DynamicRuleSpec("weighted", "val2_weighted"),
        history_s=np.array([0.2, 0.9]),
        history_val2_loss=np.array([10.0, 1.0]),
        current_s=0.5,
    )
    assert selected > 0.8
    assert meta["includes_current_s"] is False
    assert meta["n_history_used"] == 2


def test_evaluate_rule_set_uses_only_matched_rows():
    branch = pd.DataFrame(
        {
            "status": ["matched", "missing_local_minimum", "matched"],
            "origin_number": [1, 2, 3],
            "smoothness": [0.2, np.nan, 0.6],
            "val2_level_rmse": [2.0, np.nan, 1.0],
        }
    )
    result = evaluate_rule_set(
        branch,
        current_s=0.8,
        val2_loss_column="val2_level_rmse",
    )
    last = result.loc[result["rule"].eq("last")].iloc[0]
    assert np.isclose(last["selected_s"], 0.8)
    assert result["selected_s"].between(0.0, 1.0).all()


def test_outer_stops_reserve_confirmation_blocks():
    stops = _outer_stops(
        1000,
        horizon=20,
        development_blocks=3,
        holdout_blocks=4,
    )
    assert stops == [880, 900, 920]
    assert max(stops) == 1000 - 4 * 20
