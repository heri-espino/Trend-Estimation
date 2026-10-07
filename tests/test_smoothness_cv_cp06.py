from __future__ import annotations

from experiments.smoothness_cv.run_checkpoint_04 import _outer_stops
from experiments.smoothness_cv.run_checkpoint_06 import ORDER_SETS, PRESETS


def test_cp06_order_sets_are_nested_as_frozen():
    assert ORDER_SETS["d1234"] == (1, 2, 3, 4)
    assert ORDER_SETS["d123"] == (1, 2, 3)
    assert ORDER_SETS["d12"] == (1, 2)
    assert ORDER_SETS["d2"] == (2,)


def test_cp06_mechanism_blocks_end_before_cp05_region():
    preset = PRESETS["mechanism"]
    stops = _outer_stops(
        2060,
        horizon=60,
        development_blocks=preset.outer_blocks,
        holdout_blocks=preset.holdout_blocks,
    )
    assert stops == [1400, 1460, 1520, 1580, 1640, 1700, 1760, 1820]
    assert max(stops) == 1820
    assert 1880 not in stops


def test_cp06_full_panel_has_same_series_but_no_cp05_rescoring():
    preset = PRESETS["mechanism"]
    assert len(preset.series) == 64
    assert preset.holdout_blocks == 4
    assert preset.outer_blocks == 8
    assert preset.windows == (63, 126, 252, 504)
