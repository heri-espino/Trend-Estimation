"""Verify the *committed compact* 160k-draw confirmatory data.

No Monte Carlo, raw gzip or download in these tests.
"""

from pathlib import Path
import csv
import json

import pytest

from experiments.pooled_loocv_smoothness.audit_multorder_confirmatory import (
    ROOT, execute, read_and_verify, infer
)


def test_committed_multorder_campaign_and_paired_results():
    if not (ROOT / "campaign_manifest.json").is_file():
        pytest.skip("Aggregated campaign is not in this checkout")
    manifest,methods,contrasts=read_and_verify(ROOT)
    assert len(methods)==1280
    assert len(contrasts)==640
    assert manifest["source_git_sha"]=="070b363b7d8a8156f320c833539fa068b684fc7b"
    report=execute(ROOT)
    assert report["status"]=="independently_audited_complete_gaussian_confirmatory"
    assert report["independent_R3_base_shock_draws"]==160000
    assert report["primary_R3_mu_plus_1_cells"]==16
    assert report["primary_R3_mu_plus_1_cells_GLS_ML_lower_mean_MSE"]==15
    assert report["primary_R3_mu_plus_1_cells_CV_lower_mean_MSE"]==1
    assert (report[
        "primary_R3_mu_plus_1_cells_where_forced_zero_mu_Gaussian_penalty_exceeds_abs_ML_CV_gap"
    ]==16)
    assert (report[
        "primary_R3_mu_plus_1_cells_where_misspecification_cost_95CI_excludes_zero"
    ]==16)

    rows=infer(methods,contrasts,R=3)
    assert len(rows)==80
    d2n50high=next(x for x in rows
                   if x["d"]==2 and x["N"]==50
                   and x["sigma_eta"]==2. and x["mu_over_sigma_epsilon"]==1)
    assert d2n50high["estimated_mu_GLS_ML_MSE"]==pytest.approx(.6595339,abs=1e-6)
    assert d2n50high["estimated_mu_fold_clean_CV_MSE"]==pytest.approx(
        .6734682,abs=1e-6)
    exceptional=next(x for x in rows
                     if x["d"]==1 and x["N"]==50
                     and x["sigma_eta"]==2.
                     and x["mu_over_sigma_epsilon"]==1)
    assert exceptional["GLS_ML_minus_CV_ci95_low"]>0


def test_aggregate_audit_can_export_to_new_dir(tmp_path):
    if not ROOT.exists():
        pytest.skip("No committed confirmatory aggregates in this checkout")
    out=tmp_path/"independent_review"
    report=execute(ROOT,out)
    assert report["full_method_records_represented"]==12800000
    assert len(list(csv.DictReader(
        (out/"R3_with_paired_95pct_CIs.csv").open(newline=""))))==80
    assert len(list(csv.DictReader(
        (out/"R1_with_paired_95pct_CIs.csv").open(newline=""))))==80
    saved=json.loads((out/"audit_summary.json").read_text())
    assert saved["primary_R3_mu_plus_1_cells_GLS_ML_lower_mean_MSE"]==15
    with pytest.raises(FileExistsError):
        execute(ROOT,out)


def test_rejects_bad_incomplete_or_conflicting_manifest(tmp_path):
    if not ROOT.exists():
        pytest.skip("No committed confirmatory aggregates")
    original=json.loads((ROOT/"campaign_manifest.json").read_text())
    original["counts_by_cell"][0]["independent_seeds"]=9999
    import shutil
    out=tmp_path/"tampered"
    out.mkdir()
    (out/"campaign_manifest.json").write_text(json.dumps(original))
    for source in ("by_d_N_eta_R_mu_method.csv",
                   "paired_MSE_contrasts_by_d_N_eta_R_mu.csv"):
        shutil.copyfile(ROOT/source,out/source)
    with pytest.raises(ValueError,match="fewer than 10,000"):
        read_and_verify(out)
