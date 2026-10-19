"""Analyze SAVED estimated-variance pilot data without re-running simulation.

Each (scenario, seed, R) is a matched comparison of four methods.
The primary R=3 analysis is kept separate from nested R=1.
Numbers describe Monte Carlo pilot realizations, not independent
statistical significance tests, Bayesian guarantees, or global roots.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ORACLE = "guerrero_known_ratio"
ML = "estimated_gaussian_difference_ml"
MOM = "estimated_moments_nnls"
CV = "pooled_loocv_bounded_brent"
METHODS = {ORACLE, ML, MOM, CV}


def load_paired(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out: dict[tuple[int, int, int], dict] = defaultdict(dict)
    for x in rows:
        key = (int(x["scenario_id"]), int(x["replicate"]), int(x["R"]))
        method = x["method"]
        if method not in METHODS or method in out[key]:
            raise ValueError(f"unknown or repeated method {method} for {key}")
        out[key][method] = x
    if not out or any(set(g) != METHODS for g in out.values()):
        raise ValueError("all four methods must exist for each paired pool")
    return [out[key] for key in sorted(out)]


def _mean(g: list[dict], method: str, key: str) -> float:
    return float(np.mean([float(x[method][key]) for x in g]))


def _metric(g: list[dict]) -> dict:
    def wins(left, right, field="true_trend_mse"):
        return sum(float(x[left][field]) < float(x[right][field]) for x in g)
    def boundaries(m):
        return sum(np.isinf(float(x[m]["selected_lambda"])) for x in g)
    def mean_abs_relative(estimated_field: str, true_field: str):
        return float(np.mean([
            abs(float(x[ML][estimated_field]) / float(x[ORACLE][true_field]) - 1.)
            for x in g
        ]))
    finite_log_errors = [
        abs(np.log(float(x[ML]["selected_lambda"]) / float(x[ORACLE]["true_lambda"])))
        for x in g if 0 < float(x[ML]["selected_lambda"]) < np.inf
    ]
    result = {
        "pool_count": len(g),
        "methods": {
            name: {
                "mean_true_trend_mse": _mean(g, name, "true_trend_mse"),
                "mean_observed_loocv_mse": _mean(g, name, "loocv_mse"),
                "median_true_trend_mse": float(np.median([
                    float(x[name]["true_trend_mse"]) for x in g
                ])),
                "infinite_lambda": boundaries(name),
            } for name in (ORACLE, ML, CV, MOM)
        },
        "ml_true_mse_better_than_cv": wins(ML, CV),
        "ml_true_mse_better_than_known_ratio": wins(ML, ORACLE),
        "known_ratio_true_mse_better_than_cv": wins(ORACLE, CV),
        "mom_true_mse_better_than_cv": wins(MOM, CV),
        "ml_mean_abs_relative_error_sigma_eta_squared": mean_abs_relative(
            "estimated_sigma_eta2", "true_sigma_eta2"),
        "ml_mean_abs_relative_error_sigma_epsilon_squared": mean_abs_relative(
            "estimated_sigma_epsilon2", "true_sigma_epsilon2"),
        "ml_median_abs_log_lambda_ratio": (
            float(np.median(finite_log_errors)) if finite_log_errors else None
        ),
        "ml_nonfinite_lambda_count": len(g) - len(finite_log_errors),
    }
    return result


def summarize(paired: list[dict]) -> dict:
    by_r = {
        str(r): _metric([x for x in paired if int(x[ORACLE]["R"]) == r])
        for r in sorted(set(int(x[ORACLE]["R"]) for x in paired))
    }
    primary = [x for x in paired if int(x[ORACLE]["R"]) == 3]
    if not primary:
        raise ValueError("expected R=3 primary pools")
    by_n = {
        str(n): _metric([x for x in primary if int(x[ORACLE]["n"]) == n])
        for n in sorted(set(int(x[ORACLE]["n"]) for x in primary))
    }
    by_ratio = {
        str(ratio): _metric([
            x for x in primary if float(x[ORACLE]["true_lambda"]) == ratio
        ]) for ratio in sorted(set(float(x[ORACLE]["true_lambda"]) for x in primary))
    }
    by_scenario = []
    for sid in sorted(set(int(x[ORACLE]["scenario_id"]) for x in primary)):
        g = [x for x in primary if int(x[ORACLE]["scenario_id"]) == sid]
        first = g[0][ORACLE]
        metrics = _metric(g)
        by_scenario.append({
            "scenario_id": sid, "n": int(first["n"]),
            "sigma_eta": float(first["sigma_eta"]),
            "sigma_epsilon": float(first["sigma_epsilon"]),
            "known_lambda": float(first["true_lambda"]), **metrics,
        })
    return {
        "protocol": "estimated_variance_pilot_descriptive_audit_v1",
        "source_pool_count": len(paired),
        "nested_design": "R1 shares first observed series with corresponding R3 at same seed",
        "by_R": by_r,
        "primary_R3_by_n": by_n,
        "primary_R3_by_known_ratio": by_ratio,
        "primary_R3_by_scenario": by_scenario,
        "warnings": [
            "The known-ratio comparator receives true DGP variances.",
            "Difference-Gaussian ML and moments/NNLS are extensions, not Guerrero's proposed ML procedure.",
            "Five independent seed replicates per scenario: exploratory only.",
            "Method-of-moments boundary cases can dominate mean true trend MSE.",
            "Different DGP cells have different scales; keep per-scenario results.",
            "No global optimization guarantee or future-data forecasting result.",
        ],
    }


def _save_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def figures(summary: dict, out: Path) -> None:
    cells = summary["primary_R3_by_scenario"]
    xx = np.arange(len(cells))
    labels = [f"{c['scenario_id']}:N{c['n']}" for c in cells]
    fig, ax = plt.subplots(figsize=(11, 5))
    for name, label in [
        (ORACLE, "Known variance ratio (oracle)"),
        (ML, "Estimated Gaussian likelihood"),
        (CV, "Pooled LOOCV / Brent"),
    ]:
        ax.plot(xx, [c["methods"][name]["mean_true_trend_mse"] for c in cells],
                marker="o", linewidth=1.5, label=label)
    ax.set_xticks(xx, labels, rotation=45, ha="right")
    ax.set_xlabel("Scenario ID and observed series length (R=3)")
    ax.set_ylabel("Mean true latent trend MSE, 5 seeds per scenario")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "R3_true_trend_mse_by_variance_scenario.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.bar(xx, [c["methods"][MOM]["infinite_lambda"] for c in cells],
           label="Moment estimator selected infinite lambda")
    ax.set_xticks(xx, labels, rotation=45, ha="right")
    ax.set_yticks(range(6))
    ax.set_ylim(0, 5.3)
    ax.set_ylabel("Failures among 5 seeds")
    ax.set_xlabel("Scenario ID and observed series length (R=3)")
    fig.tight_layout()
    fig.savefig(out / "R3_moment_boundary_failures.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    outcomes = [
        summary["by_R"]["1"], summary["by_R"]["3"],
        summary["primary_R3_by_n"]["50"], summary["primary_R3_by_n"]["200"],
    ]
    labels = ["R=1 (all N)", "R=3 (all N)", "R=3, N=50", "R=3, N=200"]
    xx = np.arange(4)
    width = .38
    ax.bar(xx - width / 2,
           [o["ml_mean_abs_relative_error_sigma_eta_squared"] for o in outcomes],
           width, label="Observation noise variance")
    ax.bar(xx + width / 2,
           [o["ml_mean_abs_relative_error_sigma_epsilon_squared"] for o in outcomes],
           width, label="Trend innovation variance")
    ax.set_xticks(xx, labels)
    ax.set_ylabel("Mean absolute relative component error")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "ML_variance_component_error_by_sample_size.png", dpi=160)
    plt.close(fig)


def run(csv_path: Path, out: Path) -> dict:
    paired = load_paired(csv_path)
    report = summarize(paired)
    out.mkdir(parents=True, exist_ok=True)
    summary_rows = []
    for x in report["primary_R3_by_scenario"]:
        row = {k: x[k] for k in ("scenario_id", "n", "sigma_eta",
                                "sigma_epsilon", "known_lambda", "pool_count")}
        for name in (ORACLE, ML, CV, MOM):
            row[f"true_mse_{name}"] = x["methods"][name]["mean_true_trend_mse"]
            row[f"loocv_{name}"] = x["methods"][name]["mean_observed_loocv_mse"]
        row["ml_wins_vs_loocv"] = x["ml_true_mse_better_than_cv"]
        row["mom_infinite_lambda"] = x["methods"][MOM]["infinite_lambda"]
        row["ml_abs_relative_error_eta2"] = x[
            "ml_mean_abs_relative_error_sigma_eta_squared"]
        row["ml_abs_relative_error_epsilon2"] = x[
            "ml_mean_abs_relative_error_sigma_epsilon_squared"]
        summary_rows.append(row)
    _save_csv(out / "R3_scenario_diagnostics.csv", summary_rows)
    (out / "variance_pilot_audit.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    figures(report, out)
    return report


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--csv", type=Path, default=Path(
        "results/pooled_loocv_smoothness/guerrero/"
        "estimated_variances/pilot/variance_estimator_comparison.csv"
    ))
    p.add_argument("--out-dir", type=Path, default=Path(
        "results/pooled_loocv_smoothness/guerrero/"
        "estimated_variances/pilot/audit"
    ))
    args = p.parse_args()
    report = run(args.csv, args.out_dir)
    print(json.dumps({
        "primary_R3": report["by_R"]["3"],
        "first_scenario": report["primary_R3_by_scenario"][0]["scenario_id"],
        "outputs": str(args.out_dir),
    }, indent=2))


if __name__ == "__main__":
    main()
