"""Lightweight repo-CI smoke test for the separate published-methods package."""
from pathlib import Path
import sys

import numpy as np


def test_standalone_release_has_published_only_api():
    package_source = (Path(__file__).resolve().parents[1]
                      / "packages" / "trendestimation" / "src")
    sys.path.insert(0, str(package_source))
    try:
        import trendestimation as te
        assert not hasattr(te, "forecast_trend")
        assert not hasattr(te, "nested_rolling_pure_forecast")
        y = np.linspace(0, 1, 20)
        smoother = te.TrendSmoother(len(y), order=2)
        assert np.all(np.isfinite(smoother.fit(y, lambda_=10).trend))
    finally:
        sys.path.remove(str(package_source))
