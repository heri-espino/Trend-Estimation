"""Verify five-regime robustness evidence and protected paired-sample analysis."""

from pathlib import Path

import pytest

from experiments.pooled_loocv_smoothness.audit_robustness import (
    ML, MOM, REGIMES, CV, audit, load_paired,
)


PILOT = Path(
    "results/pooled_loocv_smoothness/guerrero/"
    "robustness/pilot/method_comparison.csv"
)


def test_committed_robustness_protocol_and_per_method_completeness():
    if not PILOT.exists():
        pytest.skip("Pilot CSV not present in this checkout")
    data = load_paired(PILOT)
    report = audit(data)
    assert report["paired_pools"] == 200
    assert report["method_rows_expected"] == 1000
    assert report["primary_R3"]["pool_count"] == 100
    assert report["R1_sensitivity"]["pool_count"] == 100
    assert set(report["by_regime_R3"]) == set(REGIMES)
    assert len(report["by_scenario_R3"]) == 20
    assert all(x["pool_count"] == 5 for x in report["by_scenario_R3"])
    assert report["primary_R3"]["ml_lower_true_mse_than_cv"] == 76
    assert report["primary_R3"]["mean_true_mse_ml"] == pytest.approx(
        0.5429075862902357)
    assert report["primary_R3"]["mean_true_mse_cv"] == pytest.approx(
        0.6207456553951402)
    assert report["primary_R3"]["moments_infinite_lambda_count"] == 30
    assert report["by_regime_R3"]["ar1_observation"][
        "ml_lower_true_mse_than_cv"] == 20
    assert report["primary_R3"][
        "single_brent_worse_loocv_than_multibracket_1e7"] == 0
    assert set(report["primary_R3"]["stationary_candidate_histogram"]) == {1}


def test_audit_rejects_duplicate_method_and_missing_groups(tmp_path):
    missing = tmp_path / "missing.csv"
    missing.write_text(
        "scenario_id,replicate,R,method\n"
        "0,0,3,nominal_known_ratio\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="exactly five"):
        load_paired(missing)

    duplicate = tmp_path / "duplicate.csv"
    duplicate.write_text(
        "scenario_id,replicate,R,method\n"
        "0,0,3,nominal_known_ratio\n"
        "0,0,3,nominal_known_ratio\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Duplicate/unknown"):
        load_paired(duplicate)
