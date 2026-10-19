"""No Monte Carlo: validate the 2026-10-19 25-seed non-Gaussian pilot upload."""
from pathlib import Path
import csv
import json
import shutil

import pytest

from experiments.pooled_loocv_smoothness.audit_nonzero_mu_nongaussian_pilot import (
    ROOT, verify, summarize, execute,
)


def test_committed_pilot_has_all_distributions_and_consistent_pairs():
    if not (ROOT/"campaign_manifest.json").exists():
        pytest.skip("User's compact GitHub pilot not available in this checkout")
    manifest, methods, pairs, discrepancy=verify(ROOT)
    assert manifest["source_git_sha"]=="33c8eef425e56c6e17b9a5f3d331869e2af99c30"
    assert len(methods)==15360
    assert len(pairs)==7680
    assert discrepancy < 1e-8
    report, detail=summarize(ROOT)
    assert report["independent_R3_shock_pools"]==4800
    assert len(detail)==384
    assert report["R3_mu_plus1_cells"]==192
    assert report["R3_cells_quasi_ML_better_than_CV"]==179
    assert report["R1_cells_quasi_ML_better_than_CV"]==158
    assert report["R3_cells_wrong_zero_mu_ML_more_costly_than_ML_CV_gap"]==190
    assert len(report["R3_by_distribution"])==12
    assert len(report["R1_by_distribution"])==12
    assert all(x["independent_base_shock_draws"]==25 for x in detail)
    assert all(x["mu_over_sigma_epsilon"]==1 for x in detail)
    assert not any(x["regime"].startswith("cauchy") for x in detail)


def test_export_requires_new_directory_and_has_detailed_MSE(tmp_path):
    if not (ROOT/"campaign_manifest.json").exists():
        pytest.skip("No pilot aggregates")
    out=tmp_path/"pilot_qa"
    r=execute(ROOT,out)
    assert r["saved_paired_comparison_cells"]==7680
    saved=json.loads((out/"audit_summary.json").read_text())
    assert saved["R3_cells_quasi_ML_better_than_CV"]==179
    with (out/"R1_R3_mu_plus1_all_8_methods.csv").open(newline="") as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==384
    assert len({tuple((x["regime"],x["d"],x["N"],x["sigma_eta"],x["R"]))
                for x in rows})==384
    assert all(float(x["forced_zero_mu_ML_MSE"])>=0 for x in rows)
    with pytest.raises(FileExistsError):
        execute(ROOT,out)


def test_missing_seed_rejected_before_inference(tmp_path):
    if not ROOT.exists():
        pytest.skip("No pilot aggregates")
    bad=tmp_path/"invalid"
    bad.mkdir()
    man=json.loads((ROOT/"campaign_manifest.json").read_text())
    man["by_cell"][0]["independent_shock_draws"]=24
    (bad/"campaign_manifest.json").write_text(json.dumps(man))
    for f in ("by_regime_d_N_eta_R_mu_method.csv",
              "paired_by_regime_d_N_eta_R_mu.csv"):
        shutil.copyfile(ROOT/f,bad/f)
    with pytest.raises(ValueError,match="25 independent shock"):
        verify(bad)
