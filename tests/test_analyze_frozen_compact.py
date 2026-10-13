"""Unit-test frozen postprocessing without invoking any DGP or simulation runner."""
from __future__ import annotations

import csv
import hashlib
import json
import sqlite3

import pytest

from experiments.smoothness_cv.analyze_frozen_compact import (
    Running, analyze, matched_comparators,
)


def fake_frozen_db(root):
    root.mkdir()
    config={
        "preset":"formal8h","backend":"cuda",
        "git_revision":"21bd563146e04eb545cae56b46393d93a9d98212",
        "scenario_keys":["A__linear__N50"],"seeds":5,
    }
    (root/"manifest.json").write_text(
        json.dumps({"configuration":config,"fingerprint":"frozen"}),
        encoding="utf-8",
    )
    db=root/"outcomes.sqlite"
    conn=sqlite3.connect(str(db))
    conn.executescript("""
        CREATE TABLE completed(
            task_key TEXT PRIMARY KEY,
            n_rows INTEGER NOT NULL,
            elapsed_sec REAL NOT NULL,
            completed_utc TEXT NOT NULL
        );
        CREATE TABLE failures(
            task_key TEXT PRIMARY KEY,message TEXT,occurred_utc TEXT
        );
        CREATE TABLE outcomes(
            task_key TEXT,
            scenario TEXT,study TEXT,shape TEXT,n_obs INTEGER,noise TEXT,
            sigma REAL,seasonal INTEGER,seed INTEGER,origin INTEGER,
            d INTEGER,h INTEGER,selector TEXT,is_oracle INTEGER,
            forecast_mse_obs REAL,forecast_mse_latent REAL,
            past_recovery_mse REAL,forecast_mse_conditional REAL,
            forecast_mae_obs REAL,selected_s REAL,edf REAL,
            branch_support INTEGER,n_local_minima INTEGER,
            PRIMARY KEY(task_key,origin,d,h,selector)
        ) WITHOUT ROWID;
        CREATE TABLE forecast_baselines(
            scenario TEXT,seed INTEGER,origin INTEGER,h INTEGER,
            baseline TEXT,payload TEXT,
            PRIMARY KEY(scenario,seed,origin,h,baseline)
        );
        CREATE TABLE numerical_diagnostics(
            scenario TEXT,seed INTEGER,d INTEGER,h INTEGER,
            method TEXT,payload TEXT,
            PRIMARY KEY(scenario,seed,d,h,method)
        );
    """)
    methods={
        "pooled_uniform_all":(2.,0),
        "classical_cv":(3.,0),
        "classical_gcv":(2.3,0),
        "classical_aicc":(2.6,0),
        "classical_bic":(2.9,0),
        "pooled_recent_exp_8":(2.5,0),
        "tracked_recent_exp_8":(1.5,0),
        "oracle_recovery":(.1,1),
    }
    for seed in (0,1):
        key=f"A__linear__N50__seed{seed:06d}"
        conn.execute(
            "INSERT INTO completed VALUES(?,?,?,?)",
            (key,2*len(methods),2.5,"2026-10-12T14:00Z")
        )
        for origin in (32,36):
            for selector,(mse,oracle) in methods.items():
                conn.execute(
                    "INSERT INTO outcomes VALUES("+
                    ",".join("?" for _ in range(23))+")",
                    (
                        key,"A__linear__N50","A","linear",50,
                        "iid",.5,0,seed,origin,2,3,selector,oracle,
                        mse+seed*.2,mse*.5,mse*.3,mse*.8,
                        mse*.4,.6,18.,3,2,
                    ),
                )
            for baseline in ("naive","drift","seasonal_naive","linear_ols"):
                obs={"naive":4.,"drift":2.,"seasonal_naive":5.,
                     "linear_ols":1.8}[baseline]
                payload={
                    "forecast_mse_obs":obs,
                    "forecast_mse_latent":obs/2,
                    "forecast_mae_obs":obs/3,
                }
                conn.execute(
                    "INSERT INTO forecast_baselines VALUES(?,?,?,?,?,?)",
                    ("A__linear__N50",seed,origin,3,baseline,json.dumps(payload)),
                )
        numeric={
            "study":"A","shape":"linear","d":2,"h":3,
            "method":"recent_exp_8",
            "grid_regret_to_dense":.2,
            "brent_regret_to_dense":.03,
            "adaptive_regret_to_dense":.01,
            "grid_s":.2,"brent_s":.31,
            "adaptive_s":.29,"dense_s":.3,
            "grid_outer_observed_mse":2.,
            "brent_outer_observed_mse":1.8,
            "adaptive_outer_observed_mse":1.7,
            "grid_past_recovery_mse":.9,
            "brent_past_recovery_mse":.8,
            "adaptive_past_recovery_mse":.7,
            "brent_objective_evaluations":7,
            "adaptive_objective_evaluations":50,
            "brent_seconds":.002,
            "adaptive_seconds":.01,
            "dense_seconds":.06,
        }
        conn.execute(
            "INSERT INTO numerical_diagnostics VALUES (?,?,?,?,?,?)",
            ("A__linear__N50",seed,2,3,"recent_exp_8",json.dumps(numeric)),
        )
    conn.commit()
    conn.close()
    return db


def load_csv(path):
    with path.open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))


def test_running_seed_only_uncertainty():
    s=Running()
    s.add(1)
    assert s.n==1
    assert s.se!=s.se  # undefined for single independent replication
    s.add(3)
    assert s.n==2 and s.mean==2.
    assert s.sd==pytest.approx(2**.5)


def test_matching_respects_same_weighting_and_excludes_oracles():
    assert matched_comparators("tracked_recent_exp_8")==("pooled_recent_exp_8",)
    assert matched_comparators("classical_cv")==("pooled_uniform_all",)
    assert matched_comparators("pooled_uniform_all")==()


def test_compact_analysis_no_raw_db_writes_and_true_paired_differences(tmp_path):
    run=tmp_path/"frozen"
    database=fake_frozen_db(run)
    before=hashlib.sha256(database.read_bytes()).hexdigest()
    report_dir=tmp_path/"reports"
    result=analyze(run,report_dir=report_dir,progress_every=500)
    after=hashlib.sha256(database.read_bytes()).hexdigest()
    assert before==after
    assert result["completed_scenario_seed_tasks"]==2
    assert result["method_rows_processed"]==32
    assert result["numerical_diagnostic_rows"]==2
    assert result["simulation_tasks_executed"]==0
    first=load_csv(report_dir/"paper1_forecast_cv_vs_classical.csv")
    cv=[r for r in first if r["selector"]=="classical_cv"]
    assert len(cv)==1
    assert float(cv[0]["paired_observed_msfe_diff"])==pytest.approx(1.)
    assert cv[0]["n_independent_seeds"]=="2"
    second=load_csv(report_dir/"paper2_tracking_vs_matched_pooled.csv")
    assert len(second)==1
    assert second[0]["comparator"]=="pooled_recent_exp_8"
    assert float(second[0]["paired_observed_msfe_diff"])==pytest.approx(-1.)
    assert float(second[0]["seed_win"])==pytest.approx(1.)
    with (report_dir/"paper1_2_paired_scenario.csv").open(
        encoding="utf-8",newline=""
    ) as f:
        selectors={r["selector"] for r in csv.DictReader(f)}
    assert "oracle_recovery" not in selectors
    baseline=load_csv(report_dir/"paired_vs_baselines_scenario.csv")
    naive=[r for r in baseline
           if r["selector"]=="pooled_uniform_all"
           and r["comparator"]=="naive"]
    assert len(naive)==1
    assert float(naive[0]["paired_observed_msfe_diff"])==pytest.approx(-1.9)
    coverage=load_csv(report_dir/"coverage_by_scenario.csv")
    assert len(coverage)==1
    assert coverage[0]["scenario"]=="A__linear__N50"
    assert coverage[0]["study"]=="A"
    assert coverage[0]["completed_seeds"]=="2"
    numeric=load_csv(report_dir/"paper3_numerical_summary_compact.csv")
    assert len(numeric)==1
    assert float(numeric[0]["brent_regret_to_dense"])==pytest.approx(.03)
    assert (report_dir/"README_RESULTS.md").is_file()


def test_guard_requires_completed_snapshot_not_incomplete(tmp_path):
    run=tmp_path/"no_database"
    run.mkdir()
    (run/"outcomes.sqlite.incomplete").write_bytes(b"temporary")
    with pytest.raises(FileNotFoundError,match="finalize"):
        analyze(run)


def test_frozen_compact_publication_figures_and_brief(tmp_path):
    pytest.importorskip("matplotlib")
    pytest.importorskip("pandas")
    from experiments.smoothness_cv.plot_frozen_compact import plot
    run=tmp_path/"frozen"
    fake_frozen_db(run)
    reports=tmp_path/"figures-and-tables"
    analyze(run,report_dir=reports,progress_every=999)
    actual=plot(reports)
    assert "paper1_classical_relative_rmse" in actual
    assert "paper2_matched_tracking_relative_rmse" in actual
    assert "paper3_numerical_regret" in actual
    assert "coverage_independent_seeds" in actual
    for name in actual:
        assert (reports/(name+".pdf")).stat().st_size>0
        assert (reports/(name+".png")).stat().st_size>0
    brief=(reports/"REPORT_BRIEF.md").read_text(encoding="utf-8")
    assert "Paper 1" in brief and "Paper 2" in brief and "Paper 3" in brief
    assert "EXPLORATORY" in brief and "No new Monte Carlo" in brief


def test_single_entrypoint_analyzes_existing_frozen_data_without_running_simulations(tmp_path):
    pytest.importorskip("matplotlib")
    pytest.importorskip("pandas")
    from experiments.smoothness_cv.finalize_frozen_study import finalize
    original=tmp_path/"missing-original"
    frozen=tmp_path/"frozen"
    source=fake_frozen_db(frozen)
    before=hashlib.sha256(source.read_bytes()).hexdigest()
    status=finalize(original,frozen,analyze_only=True)
    assert status["simulation_tasks_executed"]==0
    assert hashlib.sha256(source.read_bytes()).hexdigest()==before
    assert (frozen/"reports"/"frozen_compact"/"REPORT_BRIEF.md").exists()


def test_curated_github_share_excludes_all_sqlite_and_raw_rows(tmp_path):
    from experiments.smoothness_cv.publish_frozen_review import (
        EXPECTED, GRAPH_STEMS, review_paths,
    )
    root=tmp_path/"repo"
    report=root/"results"/"frozen"/"reports"/"frozen_compact"
    report.mkdir(parents=True)
    (report/"ANALYSIS_MANIFEST.json").write_text(json.dumps({
        "simulation_tasks_executed":0,
        "status":"PARTIAL — EXPLORATORY, nonconfirmatory",
    }),encoding="utf-8")
    for name in EXPECTED:
        if name=="ANALYSIS_MANIFEST.json":
            continue
        (report/name).write_text("report",encoding="utf-8")
    for stem in GRAPH_STEMS:
        for extension in (".pdf",".png"):
            (report/(stem+extension)).write_bytes(b"sample graphic")
    (root/"outcomes.sqlite").write_bytes(b"do not stage")
    selected=review_paths(report,root)
    assert all(path.startswith("results/frozen/reports/") for path in selected)
    assert all("sqlite" not in path.lower() for path in selected)
    assert len(selected)==len(EXPECTED)+2*len(GRAPH_STEMS)


def test_frozen_scientific_audit_no_new_simulations_or_sqlite_changes(tmp_path):
    from experiments.smoothness_cv.audit_frozen_evidence import audit
    run=tmp_path/"frozen"
    database=fake_frozen_db(run)
    before=hashlib.sha256(database.read_bytes()).hexdigest()
    reports=run/"reports"/"frozen_compact"
    analyze(run,report_dir=reports,progress_every=999)
    result=audit(reports,frozen_dir=run)
    assert result["no_new_simulations"] is True
    assert result["completed_tasks"]==2
    assert result["scenario_cells"]==1
    assert result["paper1_scenario_contrasts"]>0
    assert result["paper2_scenario_contrasts"]==1
    assert result["paper3"]["cases"]==2
    assert result["paper3"]["horizons"]==[3]
    assert result["paper3"]["fraction_adaptive_outer_msfe_below_grid"]==1.
    folder=reports/"audit"
    assert (folder/"AUDIT_OVERVIEW.md").exists()
    assert (folder/"PAPER1_AUDIT.md").exists()
    assert (folder/"PAPER2_AUDIT.md").exists()
    assert (folder/"PAPER3_AUDIT.md").exists()
    assert (folder/"smoothing_edf_diagnostics.csv").exists()
    tests=load_csv(folder/"comparison_tests.csv")
    assert not any(r["selector"]=="oracle_recovery" for r in tests)
    tracked=[r for r in tests if r["selector"]=="tracked_recent_exp_8"]
    assert len(tracked)==1
    assert tracked[0]["comparator"]=="pooled_recent_exp_8"
    assert float(tracked[0]["relative_rmse"])<1.
    assert float(tracked[0]["paired_observed_msfe_diff"])==pytest.approx(-1.)
    assert hashlib.sha256(database.read_bytes()).hexdigest()==before


def test_audit_rejects_tampered_ratio_or_pairing(tmp_path):
    from experiments.smoothness_cv.audit_frozen_evidence import audit
    run=tmp_path/"frozen"
    fake_frozen_db(run)
    reports=tmp_path/"reports"
    analyze(run,report_dir=reports,progress_every=999)
    file=reports/"paper1_forecast_cv_vs_classical.csv"
    lines=load_csv(file)
    lines[0]["relative_rmse"]="1234567"
    with file.open("w",encoding="utf-8",newline="") as dest:
        writer=csv.DictWriter(dest,fieldnames=list(lines[0]))
        writer.writeheader()
        writer.writerows(lines)
    with pytest.raises(ValueError,match="relative RMSE"):
        audit(reports,frozen_dir=run)


def test_audit_holm_adjust_monotonic_controls_family_error():
    import numpy as np
    from experiments.smoothness_cv.audit_frozen_evidence import holm_adjust
    p=np.array([.01,.04,.002,np.nan])
    adj=holm_adjust(p)
    assert adj[2]==pytest.approx(.006)
    assert adj[0]==pytest.approx(.02)
    assert adj[1]==pytest.approx(.04)
    assert np.isnan(adj[3])
