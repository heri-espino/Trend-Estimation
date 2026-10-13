"""Audit the EXISTING frozen 100,848-task mu=0 campaign. NO MONTE CARLO.

Read only already-saved scenario-level CSVs, recovery inventory, and
(optionally) the 50,424 existing numerical-diagnostic JSON records using
SQLite mode=ro. No simulation imports, GPU, y generation, fits or new seeds.

Outputs small, reproducible files under reports/frozen_compact/audit:
  AUDIT_OVERVIEW.md
  PAPER1_AUDIT.md, PAPER2_AUDIT.md, PAPER3_AUDIT.md
  comparison_tests.csv (scenario-level paired t-tests + Holm adjustment)
  group_heterogeneity.csv (study/noise/shape/sigma/seasonal grouped cells)
  extreme_cases.csv (predeclared largest/smallest paired risk ratios)
  numerical_paired_summary.csv (per-case numerical paired contrasts)
  AUDIT_MANIFEST.json

This is a retrospective exploratory audit, NOT new confirmation.
"""
from __future__ import annotations

import argparse
from contextlib import closing
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import t as student_t

from .recover_campaign import inspect, ro_connect


META=("study","scenario","shape","noise","n_obs","sigma","seasonal","d","h")
MATCH=("study","scenario","d","h")


def needed(folder:Path,name:str)->Path:
    file=folder/name
    if not file.is_file():
        raise FileNotFoundError(
            f"Frozen compact result missing: {file}. "
            "Run the completed frozen-only report pipeline first; "
            "do NOT restart the Monte Carlo campaign."
        )
    return file


def holm_adjust(pvalues:np.ndarray)->np.ndarray:
    """Holm FWER adjustment, valid under arbitrary dependence.

    Families are specified BEFORE reading losses: each full paper's
    predeclared deployable scenario-level pairwise comparisons.
    """
    p=np.asarray(pvalues,dtype=float)
    adjusted=np.full_like(p,np.nan)
    valid=np.flatnonzero(np.isfinite(p) & (p>=0) & (p<=1))
    n=len(valid)
    if n==0:
        return adjusted
    order=valid[np.argsort(p[valid],kind="mergesort")]
    increments=p[order]*(n-np.arange(n))
    adjusted[order]=np.minimum(1.,np.maximum.accumulate(increments))
    return adjusted


def _checked_pairing(frame:pd.DataFrame,label:str)->pd.DataFrame:
    required={
        *META,"selector","comparator","n_independent_seeds",
        "paired_observed_msfe_diff","se_paired_observed_msfe_diff",
        "method_msfe","comparator_msfe","relative_rmse",
        "n_matched_origins",
    }
    # The compact exporter records n_matched_origins and provides an SE
    # for each scenario/selector/comparator from independent seeds.
    missing=required-set(frame.columns)
    if missing:
        raise ValueError(f"{label}: missing expected paired columns: {sorted(missing)}")
    if frame.duplicated(list(META)+["selector","comparator"]).any():
        raise ValueError(f"{label}: duplicate scenario/order/horizon/method pairs")
    frame=frame.copy()
    frame["n_independent_seeds"]=pd.to_numeric(
        frame["n_independent_seeds"],errors="raise"
    )
    for field in ("paired_observed_msfe_diff","method_msfe",
                  "comparator_msfe","relative_rmse",
                  "se_paired_observed_msfe_diff"):
        frame[field]=pd.to_numeric(frame[field],errors="coerce")
    positive=(frame["method_msfe"]>=0)&(frame["comparator_msfe"]>0)
    if not positive.all():
        raise ValueError(f"{label}: nonpositive denominator or negative observed MSFE")
    expected_ratio=np.sqrt(frame.method_msfe/frame.comparator_msfe)
    if not np.allclose(
        frame.relative_rmse.to_numpy(float),
        expected_ratio.to_numpy(float),
        rtol=2e-8,atol=1e-10,equal_nan=False,
    ):
        raise ValueError(f"{label}: relative RMSE contradicts its stored mean MSE")
    if (frame.n_independent_seeds<2).any():
        raise ValueError(f"{label}: fewer than two independent seeds in a CI cell")
    # Each group is already a within-scenario matched comparison.
    return frame


def _paper_tests(frame:pd.DataFrame,paper:str)->pd.DataFrame:
    data=_checked_pairing(frame,paper)
    # Mean paired MSFE differences are computed across independent seeds.
    # Student-t approximations are post-hoc exploratory, not a new test
    # sample; Holm is applied jointly across the predeclared paper family.
    effect=data["paired_observed_msfe_diff"].to_numpy(float)
    se=data["se_paired_observed_msfe_diff"].to_numpy(float)
    n=data["n_independent_seeds"].to_numpy(int)
    df=np.maximum(n-1,1)
    t_stat=np.divide(
        effect,se,out=np.full_like(effect,np.nan),
        where=np.isfinite(se)&(se>0),
    )
    p=2.*student_t.sf(np.abs(t_stat),df=df)
    zeros=(se==0)&np.isfinite(effect)
    p[zeros & (effect==0)]=1.
    p[zeros & (effect!=0)]=0.
    data["paper"]=paper
    data["p_two_sided_t"]=p
    data["holm_p_family"]=holm_adjust(p)
    data["nominal_p_below_005"]=data.p_two_sided_t<.05
    data["holm_p_below_005"]=data.holm_p_family<.05
    data["smaller_method_msfe"]=effect<0
    data["smaller_comparator_msfe"]=effect>0
    # Distinguish SIGN from SIGNIFICANCE: a small but systematic
    # reduction in error is not automatically statistically resolved.
    data["directional_holm_method"]=(
        (effect<0)&(data.holm_p_family<.05)
    )
    data["directional_holm_comparator"]=(
        (effect>0)&(data.holm_p_family<.05)
    )
    return data


def _summarize_by(groups:pd.DataFrame,facets:list[str])->pd.DataFrame:
    vals=[]
    for keys,part in groups.groupby(facets,dropna=False,sort=True):
        if not isinstance(keys,tuple):keys=(keys,)
        r=dict(zip(facets,keys))
        ratio=part.relative_rmse.to_numpy(float)
        r.update({
            "n_scenario_contrasts":len(part),
            "median_relative_rmse":float(np.median(ratio)),
            "q10_relative_rmse":float(np.quantile(ratio,.1)),
            "q90_relative_rmse":float(np.quantile(ratio,.9)),
            "share_method_lower_rmse":float(np.mean(ratio<1)),
            "share_method_holm_significant":float(
                np.mean(part.directional_holm_method)
            ),
            "share_comparator_holm_significant":float(
                np.mean(part.directional_holm_comparator)
            ),
            "min_independent_seeds":int(part.n_independent_seeds.min()),
            "max_independent_seeds":int(part.n_independent_seeds.max()),
        })
        vals.append(r)
    return pd.DataFrame(vals)


def _finite_fmt(value,ndigits=4):
    return f"{float(value):.{ndigits}f}" if np.isfinite(value) else "NA"


def summarize_paper(frame:pd.DataFrame,*,paper:str,report_dir:Path)->pd.DataFrame:
    # Group by all predeclared methods, d,h; do not select a winning
    # method by inspecting the common held-out panel.
    by=_summarize_by(frame,["selector","comparator","d","h"])
    lines=[
        f"# Paper {paper} — retrospective evidence audit",
        "",
        "**Exploratory; source: existing frozen mu=0 Monte Carlo only.**",
        "Ratios are sqrt(mean method MSE / mean comparator MSE) "
        "inside a DGP scenario. Significance uses seed-level paired "
        "MSFE contrasts (Student t), Holm-corrected across every "
        f"tested {paper} scenario/method/order/horizon contrast; "
        "one outer origin is NOT an independent experiment.",
        "",
        "| d | h | Method | Comparator | Cells | Median ratio | "
        "Share ratio <1 | Share Holm significant (method) |",
        "|---:|---:|---|---|---:|---:|---:|---:|",
    ]
    for _,row in by.sort_values(["d","h","selector"]).iterrows():
        lines.append(
            f"| {int(row.d)} | {int(row.h)} | {row.selector} | "
            f"{row.comparator} | {int(row.n_scenario_contrasts)} | "
            f"{_finite_fmt(row.median_relative_rmse)} | "
            f"{row.share_method_lower_rmse:.1%} | "
            f"{row.share_method_holm_significant:.1%} |"
        )
    lines+=["","## Heterogeneity and failures","","The median may hide large "
        "outliers. Inspect `group_heterogeneity.csv` and "
        "`extreme_cases.csv` for the negative cases, noise families, "
        "trend shapes and horizons; no scenario outcomes are removed."]
    if paper=="1":
        lines += [
            "",
            "## BIC anomaly: mechanistic audit, NOT an automatic bug verdict",
            "",
            "BIC in the original CUDA campaign revision chooses S using",
            "`log(RSS/L) + EDF*log(L)/L` on the LAST L observed values. "
            "It is a reconstruction information criterion, not a "
            "horizon-h out-of-sample forecast criterion. Very small "
            "in-sample residuals can coexist with unstable order-d "
            "polynomial continuation, especially d=3 and h=12.",
            "",
            "The published example d=3,h=12 has BIC/pooled median "
            "relative RMSE 83.9803. This statistic is a scenario "
            "median ratio, not a factor of 84 across every observation.",
            "Use the local `paper1_2_method_scenario.csv`"
            " diagnostics (selected_s, edf, n_independent_seeds) and "
            "the original SHA 21bd563... before attributing the "
            "anomaly to overfitting, low S, boundary behavior or a "
            "specific implementation error.",
        ]
    elif paper=="2":
        lines += [
            "",
            "## Mechanism warning: branch selection versus S averaging",
            "",
            "Operational tracking chooses a persistent historical "
            "local-minimum branch and **averages its latest K S "
            "positions**. This experiment does not include a "
            "moving-average-of-global-S control. Significant gains "
            "against matched pooled do NOT isolate the contribution "
            "of branch identity from temporal variance reduction.",
            "The local-minimum/EDF diagnostics below can identify "
            "whether competing branches are generally present but "
            "cannot substitute for the missing ablation.",
        ]
    (report_dir/f"PAPER{paper}_AUDIT.md").write_text(
        "\n".join(lines)+"\n",encoding="utf-8"
    )
    return by


def _method_diagnostics(local_folder:Path, audit:Path)->str:
    path=local_folder/"paper1_2_method_scenario.csv"
    if not path.is_file():
        return (
            "The uncurated paper1_2_method_scenario.csv was not found. "
            "S/EDF boundary and branch-support diagnostics are not "
            "auditable from public paired-only tables."
        )
    df=pd.read_csv(path)
    needed_fields={
        "study","scenario","d","h","selector",
        "selected_s","edf","local_minima",
        "branch_support","n_independent_seeds",
    }
    missing=needed_fields-set(df)
    if missing:
        return f"S/EDF table exists but lacks columns: {sorted(missing)}"
    selectors=("classical_bic","classical_aicc",
               "classical_cv","pooled_uniform_all",
               "pooled_recent_exp_8","tracked_recent_exp_8")
    chosen=df[df.selector.isin(selectors)].copy()
    fields=[
        "selected_s","edf","local_minima",
        "branch_support",
    ]
    summaries=[]
    for (d,h,selector),group in chosen.groupby(
        ["d","h","selector"],sort=True
    ):
        row={"d":d,"h":h,"selector":selector,
             "scenario_cells":group.scenario.nunique()}
        for field in fields:
            x=pd.to_numeric(group[field],errors="coerce").dropna()
            row[f"median_{field}"]=x.median() if len(x) else np.nan
            row[f"share_{field}_near_zero"]=(
                (x<.01).mean() if len(x) else np.nan
            )
            if field=="selected_s":
                row["share_S_near_one"]=(
                    (x>.99).mean() if len(x) else np.nan
                )
        summaries.append(row)
    out=pd.DataFrame(summaries)
    out.to_csv(audit/"smoothing_edf_diagnostics.csv",index=False)
    return (
        "The local scenario/method table was found and "
        f"{len(out)} summaries of S, EDF, local-minimum count and "
        "branch support were written to smoothing_edf_diagnostics.csv. "
        "These are scenario-level medians of values already averaged "
        "over seeds and origins; they cannot measure single-origin "
        "boundary hit rates."
    )


P3_METRICS=(
    "grid_regret_to_dense","brent_regret_to_dense",
    "adaptive_regret_to_dense",
    "grid_outer_observed_mse","brent_outer_observed_mse",
    "adaptive_outer_observed_mse",
    "grid_past_recovery_mse","brent_past_recovery_mse",
    "adaptive_past_recovery_mse",
    "brent_objective_evaluations","adaptive_objective_evaluations",
    "brent_seconds","adaptive_seconds","dense_seconds",
)


def _audit_numerical(db_path:Path,report_dir:Path,expected_count:int)->dict:
    """Stream archived Paper 3 JSON rows; do not regenerate objectives."""
    grouped={}
    n_cases=0
    negative=0
    better_adaptive=0
    methods=set()
    horizons=set()
    with closing(ro_connect(db_path)) as conn:
        tables={r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )}
        if "numerical_diagnostics" not in tables:
            return {"cases":0,"reason":"No numerical_diagnostics table"}
        for (payload,) in conn.execute(
            "SELECT payload FROM numerical_diagnostics "
            "ORDER BY scenario,seed,d,h,method"
        ):
            v=json.loads(payload)
            missing=set(P3_METRICS)-set(v)
            if missing:
                raise ValueError(
                    f"Stored numerical JSON missing keys {sorted(missing)}"
                )
            key=(v["study"],v["shape"],int(v["d"]),
                 int(v["h"]),v["method"])
            metrics={
                "brent_minus_grid_outer_msfe":(
                    v["brent_outer_observed_mse"]-v["grid_outer_observed_mse"]
                ),
                "adaptive_minus_grid_outer_msfe":(
                    v["adaptive_outer_observed_mse"]-v["grid_outer_observed_mse"]
                ),
                "adaptive_minus_brent_outer_msfe":(
                    v["adaptive_outer_observed_mse"]-v["brent_outer_observed_mse"]
                ),
                "brent_minus_grid_F_regret":(
                    v["brent_regret_to_dense"]-v["grid_regret_to_dense"]
                ),
                "adaptive_minus_brent_F_regret":(
                    v["adaptive_regret_to_dense"]-v["brent_regret_to_dense"]
                ),
                "grid_regret_to_dense":v["grid_regret_to_dense"],
                "brent_regret_to_dense":v["brent_regret_to_dense"],
                "adaptive_regret_to_dense":v["adaptive_regret_to_dense"],
                "brent_objective_evaluations":v["brent_objective_evaluations"],
                "adaptive_objective_evaluations":v["adaptive_objective_evaluations"],
                "brent_seconds":v["brent_seconds"],
                "adaptive_seconds":v["adaptive_seconds"],
                "dense_seconds":v["dense_seconds"],
            }
            row=grouped.setdefault(key,{"n":0,"sum":{},"sum2":{}})
            row["n"]+=1
            for m,x in metrics.items():
                x=float(x)
                if not np.isfinite(x):
                    raise ValueError(f"Non-finite numerical case {m}")
                row["sum"][m]=row["sum"].get(m,0.)+x
                row["sum2"][m]=row["sum2"].get(m,0.)+x*x
            negative+=int(float(v["adaptive_regret_to_dense"])<0)
            better_adaptive+=int(
                float(v["adaptive_outer_observed_mse"])<
                float(v["grid_outer_observed_mse"])
            )
            n_cases+=1
            horizons.add(int(v["h"]))
            methods.add(v["method"])
    if n_cases!=expected_count:
        raise RuntimeError(
            f"Paper3 saved records {n_cases} != analysis manifest "
            f"expected {expected_count}; freeze may be mismatched"
        )
    rows=[]
    for key,v in sorted(grouped.items()):
        r=dict(zip(("study","shape","d","h","method"),key))
        r["n_cases"]=v["n"]
        for name,total in v["sum"].items():
            r["mean_"+name]=total/v["n"]
            r["se_"+name]=(
                float(np.sqrt(max(
                    0.,(v["sum2"][name]-total**2/v["n"])/(v["n"]-1)
                )/v["n"])) if v["n"]>1 else np.nan
            )
        rows.append(r)
    pd.DataFrame(rows).to_csv(
        report_dir/"numerical_paired_summary.csv",index=False
    )
    return {
        "cases":n_cases,"groups":len(rows),
        "horizons":sorted(horizons),
        "weighting_methods":sorted(methods),
        "fraction_adaptive_F_below_dense_grid":negative/n_cases,
        "fraction_adaptive_outer_msfe_below_grid":better_adaptive/n_cases,
    }


def audit(report_dir:Path,*,frozen_dir:Path|None=None)->dict:
    report_dir=Path(report_dir)
    audit_dir=report_dir/"audit"
    manifest=json.loads(
        needed(report_dir,"ANALYSIS_MANIFEST.json").read_text(
            encoding="utf-8"
        )
    )
    if manifest.get("simulation_tasks_executed")!=0:
        raise ValueError("Refusing an audit without 0 new simulation tasks")
    original_rev=manifest.get("original_git_revision")
    if original_rev!="21bd563146e04eb545cae56b46393d93a9d98212":
        raise ValueError(
            "This audit is limited to the verified archived formal8h "
            f"revision, not {original_rev}."
        )
    coverage=pd.read_csv(needed(report_dir,"coverage_by_scenario.csv"))
    for name in ("scenario","study","completed_seeds"):
        if name not in coverage:
            raise ValueError(f"Coverage missing {name}")
    n_tasks=int(coverage.completed_seeds.sum())
    n_scenarios=int(coverage.scenario.nunique())
    if n_tasks!=int(manifest["completed_scenario_seed_tasks"]):
        raise ValueError("Coverage total conflicts with completed replications")
    if n_scenarios!=int(manifest["scenario_cells_present"]):
        raise ValueError("Coverage scenarios conflict with analyzed manifest")
    if coverage.scenario.duplicated().any():
        raise ValueError("Duplicate scenario coverage row")
    if not coverage.study.eq(
        coverage.scenario.astype(str).str.split("__").str[0]
    ).all():
        raise ValueError("Coverage study label disagrees with scenario key")
    if frozen_dir is not None:
        actual=inspect(Path(frozen_dir))
        if actual["completed_scenario_seed_tasks"]!=n_tasks:
            raise ValueError("Frozen SQLite and published analysis disagree")
        if actual["original_git_revision"]!=original_rev:
            raise ValueError("Original Git revision mismatch")
        if actual["saved_method_rows_from_atomic_completed"]!=int(
            manifest["method_rows_processed"]
        ):
            raise ValueError("Method row count mismatch")
    # Validation is done before writing any audit files.
    source1=pd.read_csv(
        needed(report_dir,"paper1_forecast_cv_vs_classical.csv")
    )
    source2=pd.read_csv(
        needed(report_dir,"paper2_tracking_vs_matched_pooled.csv")
    )
    if not source1.selector.astype(str).str.startswith(
        ("classical_","fixed_")
    ).all() or not source1.comparator.eq("pooled_uniform_all").all():
        raise ValueError("P1 has incorrect or unrecognized method pairing")
    if not source2.selector.astype(str).str.startswith("tracked_").all():
        raise ValueError("P2 contains a non-tracking selector")
    expected_comp="pooled_"+source2.selector.str[len("tracked_"):]
    if not (source2.comparator==expected_comp).all():
        raise ValueError("P2 tracking is not paired to the SAME weighting")
    audit_dir.mkdir(parents=True,exist_ok=True)
    one=_paper_tests(source1,"1")
    two=_paper_tests(source2,"2")
    comparisons=pd.concat([one,two],ignore_index=True)
    # Export ONLY the actual inferential fields, not the entire already-
    # published multi-megabyte source CSVs again. Compact enough for
    # ordinary Git review and includes every predeclared paired contrast.
    public_columns=[
        "paper",*META,"selector","comparator","n_independent_seeds",
        "paired_observed_msfe_diff","se_paired_observed_msfe_diff",
        "method_msfe","comparator_msfe","relative_rmse",
        "p_two_sided_t","holm_p_family",
        "nominal_p_below_005","holm_p_below_005",
        "smaller_method_msfe","directional_holm_method",
        "directional_holm_comparator",
    ]
    comparisons[public_columns].to_csv(
        audit_dir/"comparison_tests.csv",index=False
    )
    g1=summarize_paper(one,paper="1",report_dir=audit_dir)
    g2=summarize_paper(two,paper="2",report_dir=audit_dir)
    heterogeneity=[]
    for paper,frame in (("1",one),("2",two)):
        for facet in ("study","shape","noise","sigma","seasonal"):
            h=_summarize_by(
                frame,["d","h","selector","comparator",facet]
            )
            h.insert(0,"facet",facet)
            h.insert(1,"paper",paper)
            heterogeneity.append(h)
    pd.concat(heterogeneity,ignore_index=True).to_csv(
        audit_dir/"group_heterogeneity.csv",index=False
    )
    extreme=[]
    for paper,data in (("1",one),("2",two)):
        for (d,h,selector,comparator),subset in data.groupby(
            ["d","h","selector","comparator"],sort=True
        ):
            ordered=subset.sort_values("relative_rmse")
            # Equal-sized representation of both tails per predeclared
            # method/horizon, not cherry-picked only best cases.
            for label,part in (
                ("lowest_five",ordered.head(5)),
                ("highest_five",ordered.tail(5)),
            ):
                for _,v in part.iterrows():
                    extreme.append({
                        "paper":paper,"tail":label,
                        **{k:v[k] for k in META},
                        "selector":selector,"comparator":comparator,
                        "relative_rmse":v.relative_rmse,
                        "paired_observed_msfe_diff":
                            v.paired_observed_msfe_diff,
                        "holm_p_family":v.holm_p_family,
                        "n_independent_seeds":v.n_independent_seeds,
                    })
    pd.DataFrame(extreme).to_csv(
        audit_dir/"extreme_cases.csv",index=False
    )
    diagnostics=_method_diagnostics(report_dir,audit_dir)
    numeric={"cases":0,"reason":"frozen database path not supplied"}
    if frozen_dir is not None:
        numeric=_audit_numerical(
            Path(frozen_dir)/"outcomes.sqlite",
            audit_dir,int(manifest["numerical_diagnostic_rows"]),
        )
    lines=[
        "# Frozen formal8h audit — three papers",
        "",
        f"- Original Git revision: `{original_rev}`.",
        f"- Completed independent scenario/seed tasks: "
        f"**{n_tasks:,}** / {manifest['expected_scenario_seed_tasks']:,}.",
        f"- Distinct DGP cells: **{n_scenarios:,}**; "
        f"min/max complete seeds per cell: "
        f"{int(coverage.completed_seeds.min()):,}/"
        f"{int(coverage.completed_seeds.max()):,}.",
        "- No new generated observations, Monte Carlo, CUDA or refits.",
        "- All inference is **exploratory** after a truncated run; "
        "multiple methods compared on one common external test panel.",
        "",
        "## Integrity",
        "",
        "- Every scenario cell has one coverage row; summed seeds equal "
        "the completed-task manifest.",
        "- Method/comparator pairs are the expected predeclared "
        "matching rules; stored relative RMSE equals "
        "sqrt(method MSFE / comparator MSFE).",
        "- Underlying comparisons use within-seed matched outer "
        "origins, and independent Monte Carlo seeds within a DGP "
        "form each standard-error sample.",
        f"- Statistical cells: P1={len(one):,}; P2={len(two):,}. "
        "Holm FWER corrections applied separately over ALL "
        "predeclared scenario contrasts within each paper.",
        "",
        "## Key caveats",
        "",
        "- The tests audit consistency of stored aggregated values; "
        "they do **not** independently regenerate raw forecast errors "
        "from the original time series.",
        "- Holm-adjusted p-values on a post hoc explored dataset "
        "do not turn this into an independent confirmation study.",
        "- The strong BIC anomalies may reflect horizon-amplified "
        "polynomial extrapolation, score normalization or "
        "boundary selection; inspect existing S/EDF tables, "
        "not only the RMSE ratio.",
        "- Tracking includes temporal mean-K of branch S, so "
        "the unrun global-S moving-average control remains necessary "
        "to attribute the gains uniquely to branch identities.",
        "- P3 diagnostics compare with a **finite dense numerical grid**, "
        "not an exact global minimum. Negative regret is permitted.",
        "",
        "## Existing S and EDF diagnostics",
        "",
        diagnostics,
        "",
        "## Numerical audit",
        "",
        json.dumps(numeric,ensure_ascii=False,indent=2),
        "",
        "## Details",
        "",
        "Read `PAPER1_AUDIT.md`, `PAPER2_AUDIT.md` and "
        "`PAPER3_AUDIT.md`, plus `comparison_tests.csv`, "
        "`group_heterogeneity.csv`, `extreme_cases.csv`, "
        "`smoothing_edf_diagnostics.csv` if available, "
        "and `numerical_paired_summary.csv` if the local frozen "
        "SQLite snapshot was supplied.",
    ]
    if numeric["cases"]:
        info=[
            "# Paper 3 — numerical evidence audit",
            "",
            f"Paired recorded numerical cases: **{numeric['cases']:,}** "
            f"across {numeric['groups']:,} predeclared groups.",
            f"Horizons actually tested: {numeric['horizons']} "
            "(do not attribute P3 evidence to other h).",
            f"Fraction of cases with adaptive F BELOW the dense "
            f"grid's minimum: "
            f"**{numeric['fraction_adaptive_F_below_dense_grid']:.1%}**. "
            "This indicates the dense grid is approximate, not "
            "that a known exact global optimum was beaten.",
            f"Fraction of cases with adaptive lower held-out observed "
            f"MSE than the coarse grid: "
            f"**{numeric['fraction_adaptive_outer_msfe_below_grid']:.1%}**.",
            "Interpret the archived per-case paired MSFE and timings "
            "rather than comparing unpaired method averages.",
            "",
            "These are exploratory comparisons of known optimization "
            "algorithms, NOT a proof of global convergence and NOT "
            "an independent sample.",
        ]
    else:
        info=["# Paper 3 — numerical evidence audit","",
              "The case-level archived diagnostics were not supplied. "
              "Numerical case-level P3 audit remains unavailable."]
    (audit_dir/"PAPER3_AUDIT.md").write_text(
        "\n".join(info)+"\n",encoding="utf-8"
    )
    (audit_dir/"AUDIT_OVERVIEW.md").write_text(
        "\n".join(lines)+"\n",encoding="utf-8"
    )
    summary={
        "source_original_git_revision":original_rev,
        "status":"RETROSPECTIVE_EXPLORATORY_AUDIT",
        "completed_tasks":n_tasks,
        "scenario_cells":n_scenarios,
        "paper1_scenario_contrasts":len(one),
        "paper2_scenario_contrasts":len(two),
        "paper1_holm_method_favorable":int(
            one.directional_holm_method.sum()
        ),
        "paper1_holm_comparator_favorable":int(
            one.directional_holm_comparator.sum()
        ),
        "paper2_holm_method_favorable":int(
            two.directional_holm_method.sum()
        ),
        "paper2_holm_comparator_favorable":int(
            two.directional_holm_comparator.sum()
        ),
        "paper3":numeric,
        "no_new_simulations":True,
        "notes":"Audit of historic mu=0 experiment; does not establish novelty or confirmatory winner",
    }
    (audit_dir/"AUDIT_MANIFEST.json").write_text(
        json.dumps(summary,indent=2,ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(summary,indent=2,ensure_ascii=False),flush=True)
    return summary


def main(argv=None)->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report-dir",type=Path,required=True)
    p.add_argument("--frozen-dir",type=Path,
                   help="Read-only frozen SQLite: counts and Paper 3 recorded cases")
    a=p.parse_args(argv)
    audit(a.report_dir,frozen_dir=a.frozen_dir)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
