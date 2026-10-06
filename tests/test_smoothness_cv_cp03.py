import numpy as np
import pandas as pd

from experiments.smoothness_cv.run_checkpoint_03 import (
    paired_series_comparisons,
    series_aggregate,
)


def _block_rows():
    rows = []
    for selector, base in (("forecast_cv_h", 1.0), ("gcv", 2.0)):
        for origin in (100, 120):
            rows.append(
                {
                    "seed": 0,
                    "scenario_id": "linear__iid__sd0.3",
                    "trend_kind": "linear",
                    "noise_model": "iid",
                    "noise_std": 0.3,
                    "order": 2,
                    "window": 60,
                    "outer_origin": origin,
                    "horizon": 3,
                    "selector": selector,
                    "selected_s": 0.9 if selector == "forecast_cv_h" else 0.8,
                    "edf": 7.8,
                    "forecast_mse_observed": base,
                    "forecast_mae_observed": np.sqrt(base),
                    "forecast_mse_latent": base / 2.0,
                    "train_recovery_mse": 0.1,
                    "latent_oracle_mse": 0.05,
                    "latent_excess_mse": base / 2.0 - 0.05,
                }
            )
    return pd.DataFrame(rows)


def test_series_aggregate_averages_outer_origins():
    series = series_aggregate(_block_rows())
    assert len(series) == 2
    proposed = series[series["selector"] == "forecast_cv_h"].iloc[0]
    assert proposed["n_outer_origins"] == 2
    assert np.isclose(proposed["msfe"], 1.0)
    assert np.isclose(proposed["mean_selected_s"], 0.9)


def test_paired_series_comparison_returns_expected_ratio_when_comparator_present():
    series = series_aggregate(_block_rows())
    paired = paired_series_comparisons(series)
    paired = paired[paired["comparator"] == "gcv"]
    assert len(paired) == 1
    assert np.isclose(paired.iloc[0]["mse_ratio"], 0.5)
    assert np.isclose(paired.iloc[0]["rmsfe_ratio"], np.sqrt(0.5))
