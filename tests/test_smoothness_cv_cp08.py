from __future__ import annotations

import numpy as np
import pandas as pd

from experiments.smoothness_cv.dynamic_branch_rules import (
    DynamicRuleSpec,
    TRAJECTORY_RULES,
    apply_rule,
    evaluate_rule_set,
)


def test_linear_k3_extrapolates_branch_trend_one_step():
    selected, meta = apply_rule(
        DynamicRuleSpec('linear_k3', 'linear_extrapolation', k=3),
        history_s=np.array([0.2, 0.3]),
        history_val2_loss=np.ones(2),
        current_s=0.4,
    )
    assert np.isclose(selected, 0.5)
    assert meta['includes_current_s'] is True


def test_delta_rule_continues_positive_recent_drift():
    selected, meta = apply_rule(
        DynamicRuleSpec('delta_hl3', 'recency_delta_extrapolation', half_life=3.0),
        history_s=np.array([0.2, 0.25, 0.32]),
        history_val2_loss=np.ones(3),
        current_s=0.4,
    )
    assert selected > 0.4
    assert meta['rho'] > 0.0


def test_trajectory_rule_output_is_clipped_but_raw_value_is_saved():
    branch = pd.DataFrame({
        'status': ['matched', 'matched'],
        'origin_number': [1, 2],
        'smoothness': [0.8, 0.9],
        'val2_log_rmse': [1.0, 1.0],
    })
    rules = (DynamicRuleSpec('linear_k3', 'linear_extrapolation', k=3),)
    result = evaluate_rule_set(
        branch, current_s=1.0, val2_loss_column='val2_log_rmse', rules=rules
    )
    row = result.iloc[0]
    assert row['raw_selected_s'] > 1.0
    assert np.isclose(row['selected_s'], 1.0)
    assert bool(row['clipped']) is True


def test_cp08_trajectory_rule_names_are_unique():
    names = [rule.name for rule in TRAJECTORY_RULES]
    assert len(names) == len(set(names))
    assert {'linear_k3','linear_k5','linear_k10','ew_linear_hl3','ew_linear_hl5','delta_hl3','delta_hl5'} == set(names)
