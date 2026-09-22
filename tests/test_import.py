def test_public_api_imports():
    import trend_estimation as td

    expected = (
        "PurePenalizedTrend",
        "GuerreroTrend",
        "select_fixed_window_pure_smoothness",
        "nested_rolling_pure_forecast",
        "find_stationary_points_log_lambda",
    )
    for name in expected:
        assert hasattr(td, name)

    assert not hasattr(td, "PenalizedTrend")
    assert td.__version__ != "0+unknown"
