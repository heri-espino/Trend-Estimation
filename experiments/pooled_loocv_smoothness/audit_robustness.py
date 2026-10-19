"""Audit committed robustness-pilot CSV without regenerating simulated data.

The main statistical unit is a scenario/seed/R pool. Methods within a pool
are paired; R=1 reuses the first series in R=3, so do not combine these as
independent replications. Figures are MANUAL (--figures), not CI outputs.
This audit is descriptive with only five independent seeds per DGP cell.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from .run_robustness import METHODS, REGIMES


ML = "estimated_gaussian_difference_ml"
CV = "pooled_loocv_bounded_brent"
MULTI = "pooled_loocv_multibracket_brent"
MOM = "estimated_moments_nnls"
NOMINAL = "nominal_known_ratio"


def load_paired(input_csv: Path) -> list[dict]:
    with input_csv.open(newline="", encoding="utf-8") as handle:
        raw = list(csv.DictReader(handle))
    pools: dict[tuple[int, int, int], dict[str, dict]] = defaultdict(dict)
    for row in raw:
        key = (int(row["scenario_id"]), int(row["replicate"]), int(row["R"]))
        method = row["method"]
        if method not in METHODS or method in pools[key]:
            raise ValueError(f"Duplicate/unknown method in pool {key}: {method}")
        pools[key][method] = row
    if not pools or any(set(p) != set(METHODS) for p in pools.values()):
        raise ValueError("Each pool must have exactly five declared methods")
    output = []
    for key, methods in sorted(pools.items()):
        first = methods[NOMINAL]
        for field in ("seed", "regime", "N", "d", "R",
                      "sigma_eta_nominal", "sigma_epsilon_nominal"):
            if any(row[field] != first[field] for row in methods.values()):
                raise ValueError(f"Inconsistent {field} in {key}")
        mle, cv, multi, mom = (methods[m] for m in (ML, CV, MULTI, MOM))
        score = lambda rec, field: float(rec[field])
        record = {
            "scenario_id": key[0], "replicate": key[1],
            "R": key[2], "seed": int(first["seed"]),
            "regime": first["regime"], "N": int(first["N"]),
            "sigma_eta": float(first["sigma_eta_nominal"]),
            "sigma_epsilon": float(first["sigma_epsilon_nominal"]),
            "nominal_lambda": score(first, "nominal_variance_ratio_lambda"),
            "nominal_ratio_model_valid": first[
                "nominal_ratio_is_valid_model_benchmark"].lower() == "true",
            "true_mse_nominal": score(first, "true_trend_mse"),
            "true_mse_ml": score(mle, "true_trend_mse"),
            "true_mse_cv": score(cv, "true_trend_mse"),
            "true_mse_multibracket": score(multi, "true_trend_mse"),
            "true_mse_moments": score(mom, "true_trend_mse"),
            "loocv_ml": score(mle, "observed_loocv_mse"),
            "loocv_cv": score(cv, "observed_loocv_mse"),
            "loocv_multibracket": score(multi, "observed_loocv_mse"),
            "delta_true_mse_cv_minus_ml": (
                score(cv, "true_trend_mse") - score(mle, "true_trend_mse")),
            "delta_loocv_ml_minus_cv": (
                score(mle, "observed_loocv_mse") -
                score(cv, "observed_loocv_mse")),
            "delta_loocv_cv_minus_multibracket": (
                score(cv, "observed_loocv_mse") -
                score(multi, "observed_loocv_mse")),
            "ml_selected_lambda": score(mle, "selected_lambda"),
            "cv_selected_lambda": score(cv, "selected_lambda"),
            "moments_selected_lambda": score(mom, "selected_lambda"),
            "ml_infinite_lambda": bool(np.isinf(score(mle, "selected_lambda"))),
            "moments_infinite_lambda": bool(np.isinf(score(mom, "selected_lambda"))),
            "numerically_detected_stationary_candidates": int(
                float(cv["stationary_candidates_multibracket"])),
        }
        if record["regime"] not in REGIMES:
            raise ValueError("Unrecognized regime in saved CSV")
        output.append(record)

    # Verify each nested single-series and three-series run used a common seed.
    nested: dict[tuple[int, int], dict[int, dict]] = defaultdict(dict)
    for rec in output:
        nested[(rec["scenario_id"], rec["replicate"])][rec["R"]] = rec
    for key, by_r in nested.items():
        if set(by_r) != {1, 3} or by_r[1]["seed"] != by_r[3]["seed"]:
            raise ValueError(f"Missing/inconsistent nested R=1/R=3: {key}")
    return output


def metrics(rows: list[dict]) -> dict:
    if not rows:
        raise ValueError("Cannot summarize empty subset")
    med = lambda field: float(np.median([x[field] for x in rows]))
    mean = lambda field: float(np.mean([x[field] for x in rows]))
    return {
        "pool_count": len(rows),
        "mean_true_mse_ml": mean("true_mse_ml"),
        "mean_true_mse_cv": mean("true_mse_cv"),
        "mean_true_mse_nominal": mean("true_mse_nominal"),
        "mean_true_mse_moments": mean("true_mse_moments"),
        "median_true_mse_ml": med("true_mse_ml"),
        "median_true_mse_cv": med("true_mse_cv"),
        "mean_paired_cv_minus_ml_true_mse": mean("delta_true_mse_cv_minus_ml"),
        "median_paired_cv_minus_ml_true_mse": med("delta_true_mse_cv_minus_ml"),
        "ml_lower_true_mse_than_cv": sum(
            x["delta_true_mse_cv_minus_ml"] > 0 for x in rows),
        "mean_cv_mse_ml": mean("loocv_ml"),
        "mean_cv_mse_cv": mean("loocv_cv"),
        "single_brent_worse_loocv_than_multibracket_1e7": sum(
            x["delta_loocv_cv_minus_multibracket"] > 1e-7 for x in rows),
        "moments_infinite_lambda_count": sum(
            x["moments_infinite_lambda"] for x in rows),
        "ml_infinite_lambda_count": sum(x["ml_infinite_lambda"] for x in rows),
        "stationary_candidate_histogram": dict(sorted(Counter(
            x["numerically_detected_stationary_candidates"]
            for x in rows).items())),
    }


def audit(paired: list[dict]) -> dict:
    by_r = {
        str(r): metrics([row for row in paired if row["R"] == r])
        for r in (1, 3)
    }
    by_regime = {
        regime: metrics([
            row for row in paired if row["R"] == 3 and row["regime"] == regime
        ]) for regime in REGIMES
    }
    cells = []
    for scenario_id in sorted({x["scenario_id"] for x in paired}):
        subset = [x for x in paired
                  if x["scenario_id"] == scenario_id and x["R"] == 3]
        if len(subset) != len({x["seed"] for x in subset}):
            raise ValueError("A scenario has duplicate independent seed")
        exemplar = subset[0]
        cells.append({
            "scenario_id": scenario_id, "regime": exemplar["regime"],
            "N": exemplar["N"], "sigma_eta": exemplar["sigma_eta"],
            **metrics(subset),
        })
    return {
        "status": "descriptive_committed_pilot_not_confirmatory",
        "protocol": "robustness_pilot_independent_csv_audit_v1",
        "method_rows_expected": len(paired) * len(METHODS),
        "paired_pools": len(paired),
        "primary_R3": by_r["3"],
        "R1_sensitivity": by_r["1"],
        "by_regime_R3": by_regime,
        "by_scenario_R3": cells,
        "warnings": [
            "R=1 is a nested copy of the first series of R=3, not independent.",
            "Five seed repetitions per scenario; don't compute naive confidence intervals from 1000 method rows.",
            "Nominal variance ratio is not a covariance-correct oracle under AR1/heteroskedastic measurement errors.",
            "Observed LOOCV MSE and latent truth reconstruction MSE are different estimands.",
            "Finite derivative scans count candidates, not certified stationary points or local minima.",
            "Gaussian likelihood models differenced observations; this is our extension, not an MLE claimed by Guerrero (2007).",
        ],
    }


def _write_csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def figures(summary: dict, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    regimes = list(REGIMES)
    values = [summary["by_regime_R3"][name] for name in regimes]
    fig, ax = plt.subplots(figsize=(11, 5))
    xx = np.arange(len(regimes))
    bar = .38
    ax.bar(xx - bar/2, [v["mean_true_mse_ml"] for v in values],
           bar, label="Fitted Gaussian difference likelihood")
    ax.bar(xx + bar/2, [v["mean_true_mse_cv"] for v in values],
           bar, label="Pooled observed LOOCV (Brent)")
    ax.set_xticks(xx, [r.replace("_", " ") for r in regimes],
                  rotation=28, ha="right")
    ax.set_ylabel("Mean true latent trend MSE (R=3)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "R3_MLE_vs_LOOCV_by_noise_regime.png", dpi=160)
    plt.close(fig)

    cells = summary["by_scenario_R3"]
    fig, ax = plt.subplots(figsize=(11, 4.5))
    xx = np.arange(len(cells))
    ax.bar(xx, [v["mean_paired_cv_minus_ml_true_mse"] for v in cells])
    ax.axhline(0, linestyle="--", linewidth=1)
    ax.set_xticks(xx, [f'{v["scenario_id"]} / N{v["N"]}' for v in cells],
                  rotation=50, ha="right")
    ax.set_ylabel("Mean paired trend MSE (CV minus MLE)")
    ax.set_xlabel("Scenario ID / observation length (5 seeds each, R=3)")
    fig.tight_layout()
    fig.savefig(out / "R3_paired_true_MSE_by_scenario.png", dpi=160)
    plt.close(fig)


def execute(input_csv: Path, out: Path, render_figures: bool = False):
    paired = load_paired(input_csv)
    summary = audit(paired)
    out.mkdir(parents=True, exist_ok=True)
    _write_csv(out / "paired_pool_differences.csv", paired)
    cell_rows = summary["by_scenario_R3"]
    _write_csv(out / "R3_scenario_summary.csv", [
        {k: v for k, v in cell.items() if k != "stationary_candidate_histogram"}
        for cell in cell_rows])
    (out / "audit_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    if render_figures:
        figures(summary, out)
    return summary


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--csv", type=Path, default=Path(
        "results/pooled_loocv_smoothness/guerrero/robustness/pilot/method_comparison.csv"))
    p.add_argument("--out-dir", type=Path, default=Path(
        "results/pooled_loocv_smoothness/guerrero/robustness/pilot/audit"))
    p.add_argument("--figures", action="store_true",
                   help="Manually generate two audit figures")
    args = p.parse_args()
    summary = execute(args.csv, args.out_dir, args.figures)
    print(json.dumps({"pools": summary["paired_pools"],
                      "R3": summary["primary_R3"],
                      "by_regime_R3": summary["by_regime_R3"]}, indent=2))


if __name__ == "__main__":
    main()
