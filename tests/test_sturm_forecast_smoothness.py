"""Small exact rational cases; runs when SymPy is installed."""
import numpy as np
import pytest

sp = pytest.importorskip("sympy")

from trend_estimation.selection.sturm import sturm_forecast_smoothness


def test_multimodal_sturm_isolates_three_positive_roots():
    result = sturm_forecast_smoothness(
        [4, 0, -2, -1, 3, 1], [0, 1], order=2, max_window=6
    )
    assert result.certified_positive_root_count == 3
    assert result.constant_loss is False
    assert [p.kind for p in result.stationary_roots] == [
        "minimum", "maximum", "minimum"
    ]
    assert all(0.0 < p.smoothness < 1.0 for p in result.stationary_roots)
    assert result.sturm_variations[0] - result.sturm_variations[1] == 3
    assert all(p.rational_interval is not None for p in result.stationary_roots)
    assert np.allclose(
        [p.lambda_value for p in result.stationary_roots],
        [0.146706269970455, 1.10154279261145, 31.8088601118155],
        rtol=0.0, atol=2e-9,
    )
    assert np.allclose(
        [p.smoothness for p in result.stationary_roots],
        [0.380475254634, 0.718759058476, 0.976960746722],
        rtol=0.0, atol=2e-8,
    )
    assert 0.0 <= result.best_smoothness <= 1.0
    assert result.best_mse <= min(result.endpoint_mse) + 1e-9


def test_sturm_constant_forecast_loss_degeneracy():
    result = sturm_forecast_smoothness([1, 1, 1, 1], [1], order=1)
    assert result.certified_positive_root_count == 0
    assert result.stationary_roots == ()
    assert result.constant_loss is True
    assert result.best_smoothness == 0.0
    assert np.isclose(result.best_mse, 0.0)


def test_sturm_rejects_large_windows_before_symbolic_inversion():
    with pytest.raises(ValueError, match="max_window"):
        sturm_forecast_smoothness([0] * 9, [0], order=2)


def test_sturm_requires_consistent_validation_origin_counts():
    with pytest.raises(ValueError, match="origin counts"):
        sturm_forecast_smoothness([[0, 1, 2], [1, 2, 3]], [[1]], order=1)
