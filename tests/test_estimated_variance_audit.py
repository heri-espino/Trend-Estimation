"""Lightweight, figure-free checks of committed estimated-variance pilot audit."""

from pathlib import Path

import pytest

from experiments.pooled_loocv_smoothness.audit_variance_estimation import (
    CV, ML, MOM, ORACLE, load_paired, summarize,
)


PILOT = Path(
    "results/pooled_loocv_smoothness/guerrero/"
    "estimated_variances/pilot/variance_estimator_comparison.csv"
)


def test_uploaded_pilot_has_complete_methods_and_correct_nested_counts():
    if not PILOT.exists():
        pytest.skip("committed exploratory pilot not available in this checkout")
    pairs = load_paired(PILOT)
    result = summarize(pairs)
    assert len(pairs) == 120
    assert set(result["by_R"]) == {"1", "3"}
    assert result["by_R"]["1"]["pool_count"] == 60
    assert result["by_R"]["3"]["pool_count"] == 60
    assert len(result["primary_R3_by_scenario"]) == 12
    assert result["primary_R3_by_n"]["50"]["pool_count"] == 30
    assert result["primary_R3_by_n"]["200"]["pool_count"] == 30
    for size in ("1", "3"):
        assert set(result["by_R"][size]["methods"]) == {CV, ML, MOM, ORACLE}
    assert result["by_R"]["3"]["methods"][MOM]["infinite_lambda"] == 16
    assert result["by_R"]["3"]["ml_true_mse_better_than_cv"] == 37
    assert result["by_R"]["3"]["methods"][ML][
        "mean_true_trend_mse"] == pytest.approx(0.3879155661026364)


def test_audit_rejects_missing_method_with_lineage(tmp_path):
    csv_file = tmp_path / "incomplete.csv"
    csv_file.write_text(
        "scenario_id,replicate,R,method\n"
        "0,0,3,guerrero_known_ratio\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="all four methods"):
        load_paired(csv_file)


def test_audit_rejects_duplicate_method(tmp_path):
    csv_file = tmp_path / "duplicate.csv"
    csv_file.write_text(
        "scenario_id,replicate,R,method\n"
        "0,0,3,guerrero_known_ratio\n"
        "0,0,3,guerrero_known_ratio\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="repeated method"):
        load_paired(csv_file)
