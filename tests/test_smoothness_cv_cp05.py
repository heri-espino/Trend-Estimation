from __future__ import annotations

import numpy as np

from experiments.smoothness_cv.run_checkpoint_05 import (
    PANEL_CRYPTOS,
    PANEL_ETFS,
    PANEL_SERIES,
    PANEL_STOCKS,
    PRESETS,
    _make_rule_rows,
)


def test_cp05_frozen_panel_counts_and_exclusions():
    assert len(PANEL_ETFS) == 20
    assert len(PANEL_STOCKS) == 36
    assert len(PANEL_CRYPTOS) == 8
    assert len(PANEL_SERIES) == 64
    assert len(set(PANEL_SERIES)) == 64
    assert {"AAPL", "SPY", "BTC-USD"}.isdisjoint(PANEL_SERIES)


def test_cp05_panel_preset_is_not_a_tuning_grid():
    preset = PRESETS["panel"]
    assert preset.outer_blocks == 4
    assert preset.max_origins == 30
    assert preset.windows == (63, 126, 252, 504)
    assert preset.series == PANEL_SERIES


def test_cp05_tracking_failure_falls_back_to_pooled_for_all_rules():
    rows = _make_rule_rows(
        branch_history=None,
        current_s=None,
        pooled_s=0.73,
        fallback_used=True,
    )
    assert set(rows["rule"]) == {
        "recency_hl3",
        "last",
        "pooled_cv_same_config",
    }
    assert np.allclose(rows["selected_s"], 0.73)
    assert set(rows["rule_family"]) == {"fallback_pooled", "pooled_cv"}
