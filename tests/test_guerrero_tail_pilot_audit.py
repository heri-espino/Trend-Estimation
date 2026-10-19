"""Independent audit regression tests for uploaded 13-regime x 3-order pilot."""

from pathlib import Path
import json

import pytest

from experiments.pooled_loocv_smoothness.audit_tail_noise import execute, read_pools, summarize


BASE = Path("results/pooled_loocv_smoothness/guerrero/tail_stress/pilot")


def test_committed_pilot_integrity_and_recomputed_results():
    csv_file = BASE / "method_comparison.csv"
    manifest_file = BASE / "manifest.json"
    if not csv_file.is_file() or not manifest_file.is_file():
        pytest.skip("Uploaded pilot is not available in this checkout")
    pools, manifest = read_pools(csv_file, manifest_file)
    report = summarize(pools)
    assert manifest["scenario_count"] == 156
    assert manifest["expected_method_rows"] == 4680
    assert len(pools) == 1560
    assert report["primary_R3_pools"] == 780
    assert report["nested_R1_pools"] == 780
    assert report["method_rows_checked"] == 4680
    assert len(report["by_d_and_regime_R3"]) == 39
    assert len(report["by_scenario_R3"]) == 156

    finite = report["finite_variance_primary_R3"]
    assert finite["n_primary_R3_pools"] == 720
    assert finite["gaussian_ML_lower_realized_MSE_count"] == 427
    assert finite["mean_realized_trend_MSE_ML"] == pytest.approx(
        0.3225731665255932, abs=1e-12)
    assert finite["mean_realized_trend_MSE_LOOCV"] == pytest.approx(
        0.3293217318531668, abs=1e-12)
    assert finite["bounded_Brent_LOOCV_loss_worse_than_multibracket_gt_1e7"] == 0

    for order, n, mle_mse, cv_mse, wins in (
        ("1", 240, .20768664158102543, .20883861128823983, 122),
        ("2", 240, .33830952891578925, .34831319462775073, 149),
        ("3", 240, .4217233290799649, .4308133896435104, 156),
    ):
        group = report["by_d_finite_variance_R3"][order]
        assert group["n_primary_R3_pools"] == n
        assert group["mean_realized_trend_MSE_ML"] == pytest.approx(
            mle_mse, abs=1e-12)
        assert group["mean_realized_trend_MSE_LOOCV"] == pytest.approx(
            cv_mse, abs=1e-12)
        assert group["gaussian_ML_lower_realized_MSE_count"] == wins

    cauchy = report["Cauchy_primary_R3"]
    assert cauchy["n_primary_R3_pools"] == 60
    assert cauchy["population_expected_trend_MSE_defined"] is False
    assert cauchy["mean_MSE_omitted_due_to_infinite_Cauchy_risk"] is True
    assert "mean_realized_trend_MSE_ML" not in cauchy
    assert cauchy["gaussian_ML_lower_realized_MSE_count"] == 18
    assert cauchy["ML_infinite_lambda_count"] == 27
    assert cauchy["LOOCV_infinite_lambda_count"] == 8

    assert len(report["multiple_stationary_candidate_R3_cases"]) == 7
    assert len(report["by_skew_normal_alpha_R3"]) == 5


def test_rejects_corrupted_csv_without_all_three_methods(tmp_path):
    data = tmp_path / "methods.csv"
    data.write_text(
        "scenario_id,replicate,R,method\n"
        "0,0,3,estimated_gaussian_difference_ml\n",
        encoding="utf-8",
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        '{"status":"executed","expected_method_rows":1,'
        '"expected_pools":1}', encoding="utf-8")
    with pytest.raises(ValueError, match="all three"):
        read_pools(data, manifest)



def test_uploaded_pilot_full_audit_json_csv_export(tmp_path):
    """Exercise actual artifact writer, not just intermediate dictionaries."""
    csv_path = BASE / "method_comparison.csv"
    manifest_path = BASE / "manifest.json"
    if not csv_path.is_file() or not manifest_path.is_file():
        pytest.skip("Uploaded pilot is not available in this checkout")
    summary = execute(csv_path, manifest_path, tmp_path, figures=False)
    saved = json.loads((tmp_path / "audit_summary.json").read_text())
    assert summary["primary_R3_pools"] == 780
    assert saved["primary_R3_pools"] == 780
    assert (tmp_path / "R3_by_d_distribution.csv").is_file()
    assert (tmp_path / "R3_by_scenario.csv").is_file()
    assert (tmp_path / "paired_pool_diagnostics.csv").is_file()
    assert saved["Cauchy_primary_R3"]["ML_infinite_lambda_count"] == 27
    assert saved["Cauchy_primary_R3"]["LOOCV_infinite_lambda_count"] == 8
