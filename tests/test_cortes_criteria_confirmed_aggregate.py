"""Validate uploaded 26-method 25-seed Cortes-Toto aggregate (NO Monte Carlo)."""
import csv
import json
import shutil

import pytest

from experiments.pooled_loocv_smoothness.audit_cortes_criteria_confirmed_pilot import (
    ROOT, verify, descriptive, execute
)


def test_exact_pilot_26_methods_192_strata_and_existing_J_parity():
    if not (ROOT/"campaign_manifest.json").is_file():
        pytest.skip("Uploaded compact Study K pilot missing in checkout")
    manifest,index,paired,maximum=verify(ROOT)
    assert len(index)==49920
    assert len(paired)==80640
    assert maximum < 1e-8
    assert manifest["source_git_sha"]=="1785889d7d64a77f548d8746d41a9ea786e3e588"
    assert manifest["original_eight_method_parity"]["maximum_mean_true_MSE_difference"]==0.0

    report,cells,by_law=descriptive(ROOT)
    assert len(cells)==384
    assert len(by_law)==24
    assert report["R3_GLS_better_than_CV_multibracket"]==179
    assert report["R3_GLS_better_than_GCV"]==180
    assert report["R3_GLS_better_than_AICc"]==178
    assert report["BIC_joint_at_lower_search_limit_in_R3"]==4800
    assert report["BIC_joint_at_lower_search_limit_in_R1"]==4800
    assert all(row["independent_reused_J_shocks"]==25 for row in cells)
    assert all(row["mu_factor"]==1.0 for row in cells)
    assert set(row["R"] for row in cells)=={1,3}


def test_read_only_audit_exports_disaggregated_summary_once(tmp_path):
    if not ROOT.exists():
        pytest.skip("Study K compact data not mounted")
    out=tmp_path/"audit"
    result=execute(ROOT,out)
    assert result["original_reused_independent_shocks"]==4800
    with (out/"R1_R3_mu_plus1_26_methods_per_scenario.csv").open(
        newline="",encoding="utf-8") as f:
        assert len(list(csv.DictReader(f)))==384
    with (out/"by_regime_R_mu_plus1_key_methods.csv").open(
        newline="",encoding="utf-8") as f:
        assert len(list(csv.DictReader(f)))==24
    assert json.loads((out/"audit_summary.json").read_text())[
        "R3_GLS_better_than_GCV"]==180
    with pytest.raises(FileExistsError):
        execute(ROOT,out)


def test_bad_reference_parity_is_rejected(tmp_path):
    if not ROOT.exists():pytest.skip("Study K compact data not mounted")
    folder=tmp_path/"bad"
    folder.mkdir()
    man=json.loads((ROOT/"campaign_manifest.json").read_text())
    man["original_eight_method_parity"]["saved_J_baseline_cells_matched"]=15359
    (folder/"campaign_manifest.json").write_text(json.dumps(man))
    for name in ("by_regime_d_N_eta_R_mu_26_methods.csv",
                 "paired_criterion_vs_original_MLE_LOOCV_plugin.csv"):
        shutil.copyfile(ROOT/name,folder/name)
    with pytest.raises(ValueError,match="parity"):
        verify(folder)


def test_bad_moment_warning_is_rejected(tmp_path):
    if not ROOT.exists():pytest.skip("Study K compact data not mounted")
    folder=tmp_path/"moments"
    folder.mkdir()
    shutil.copyfile(ROOT/"campaign_manifest.json",folder/"campaign_manifest.json")
    shutil.copyfile(ROOT/"paired_criterion_vs_original_MLE_LOOCV_plugin.csv",
                    folder/"paired_criterion_vs_original_MLE_LOOCV_plugin.csv")
    source=ROOT/"by_regime_d_N_eta_R_mu_26_methods.csv"
    data=source.read_text(encoding="utf-8")
    # Flip exactly one moment warning field in Student-t3 data without
    # altering the CSV shape or any numerical experiment records.
    records=data.splitlines()
    header=records[0].split(",")
    reg=header.index("regime")
    flag=header.index("fourth_moment_infinite_normal_CI_not_valid")
    for i in range(1,len(records)):
        values=records[i].split(",")
        if values[reg]=="student_t3_observation":
            values[flag]="False"
            records[i]=",".join(values)
            break
    (folder/"by_regime_d_N_eta_R_mu_26_methods.csv").write_text(
        "\n".join(records)+"\n",encoding="utf-8")
    with pytest.raises(ValueError,match="moment"):
        verify(folder)
