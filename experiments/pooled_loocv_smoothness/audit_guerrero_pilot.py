"""Reproducible, descriptive audit of Guerrero's saved variance-ratio pilot.

Computes paired method comparisons from the SAVED CSV, never reruns the
stochastic DGP or treats R=1 and R=3 pools as independent. Generates
tables and interpretable figures (no inferential CI with five seeds/cell).
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


METHODS = {"guerrero_known_ratio", "bounded_brent",
           "multibracket_brent", "dense_reference"}


def load_comparisons(path: Path) -> list[dict]:
    """Return one paired record per (scenario, replicate, R)."""
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    groups: dict[tuple[int, int, int], dict[str, dict]] = defaultdict(dict)
    for row in rows:
        key = (int(row["scenario_id"]), int(row["replicate"]), int(row["R"]))
        if row["method"] in groups[key]:
            raise ValueError(f"Duplicate method in {key}: {row['method']}")
        groups[key][row["method"]] = row
    if not groups or any(set(g) != METHODS for g in groups.values()):
        raise ValueError("Every group must contain exactly the 4 declared methods")
    paired = []
    for (case_id, replicate, pool_size), methods in sorted(groups.items()):
        g = methods["guerrero_known_ratio"]
        m = methods["multibracket_brent"]
        b = methods["bounded_brent"]
        d = methods["dense_reference"]
        cv_g, cv_m = float(g["pooled_loocv_mse"]), float(m["pooled_loocv_mse"])
        true_g, true_m = float(g["true_trend_mse"]), float(m["true_trend_mse"])
        paired.append({
            "scenario_id": case_id, "replicate": replicate, "seed": int(g["seed"]),
            "R": pool_size, "n": int(g["n"]),
            "sigma_eta": float(g["sigma_eta"]),
            "sigma_epsilon": float(g["sigma_epsilon"]),
            "lambda_guerrero": float(g["known_variance_ratio_lambda"]),
            "S_guerrero": float(g["selected_s"]), "S_multibracket": float(m["selected_s"]),
            "cv_guerrero": cv_g, "cv_multibracket": cv_m,
            "true_mse_guerrero": true_g, "true_mse_multibracket": true_m,
            "delta_cv_guerrero_minus_multibracket": cv_g - cv_m,
            "delta_true_mse_multibracket_minus_guerrero": true_m - true_g,
            "single_start_minus_multibracket_cv":
                float(b["pooled_loocv_mse"]) - cv_m,
            "grid_minus_multibracket_cv": float(d["pooled_loocv_mse"]) - cv_m,
            "stationary_candidates_detected": int(m["stationary_candidates_detected"]),
            "multibracket_endpoint": str(m["selected_exact_endpoint"]).lower() == "true",
        })
    return paired


def _write_csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def summarize(paired: list[dict]):
    """Return per-cell summaries and a nested-pool-aware descriptive summary."""
    by_cell: dict[tuple[int, int], list[dict]] = defaultdict(list)
    for row in paired:
        by_cell[(row["scenario_id"], row["R"])].append(row)
    cells = []
    for (case_id, pool_size), records in sorted(by_cell.items()):
        first = records[0]
        for key in ("n", "sigma_eta", "sigma_epsilon", "lambda_guerrero"):
            if any(rec[key] != first[key] for rec in records):
                raise ValueError(f"Scenario {case_id} has inconsistent {key}")
        cells.append({
            "scenario_id": case_id, "R": pool_size,
            "n": first["n"], "sigma_eta": first["sigma_eta"],
            "sigma_epsilon": first["sigma_epsilon"],
            "lambda_guerrero": first["lambda_guerrero"],
            "n_seeds": len(records),
            "mean_cv_guerrero": float(np.mean([r["cv_guerrero"] for r in records])),
            "mean_cv_multibracket": float(np.mean([r["cv_multibracket"] for r in records])),
            "mean_true_mse_guerrero": float(np.mean(
                [r["true_mse_guerrero"] for r in records])),
            "mean_true_mse_multibracket": float(np.mean(
                [r["true_mse_multibracket"] for r in records])),
            "mean_delta_true_mse_multibracket_minus_guerrero": float(np.mean(
                [r["delta_true_mse_multibracket_minus_guerrero"] for r in records])),
            "guerrero_true_mse_wins": sum(
                r["delta_true_mse_multibracket_minus_guerrero"] > 0 for r in records),
            "multibracket_cv_wins": sum(
                r["delta_cv_guerrero_minus_multibracket"] > 1e-8 for r in records),
        })

    by_r = {}
    for pool_size in sorted({r["R"] for r in paired}):
        records = [r for r in paired if r["R"] == pool_size]
        by_r[str(pool_size)] = {
            "pool_count": len(records),
            "mean_true_mse_guerrero": float(np.mean(
                [r["true_mse_guerrero"] for r in records])),
            "mean_true_mse_multibracket": float(np.mean(
                [r["true_mse_multibracket"] for r in records])),
            "mean_cv_guerrero": float(np.mean([r["cv_guerrero"] for r in records])),
            "mean_cv_multibracket": float(np.mean(
                [r["cv_multibracket"] for r in records])),
            "guerrero_true_mse_wins": sum(
                r["delta_true_mse_multibracket_minus_guerrero"] > 0 for r in records),
            "multibracket_cv_wins": sum(
                r["delta_cv_guerrero_minus_multibracket"] > 1e-8 for r in records),
            "single_start_cv_worse_than_multibracket": sum(
                r["single_start_minus_multibracket_cv"] > 1e-7 for r in records),
            "numerically_detected_stationary_candidate_counts": dict(sorted(
                Counter(r["stationary_candidates_detected"] for r in records).items()
            )),
        }
    return cells, {
        "status": "descriptive pilot evidence, no certified global optimization",
        "paired_pools_total": len(paired),
        "nested_R_warning": "R=1 reuses first series in corresponding R=3 pool",
        "by_R": by_r,
        "primary_R3_scenario_count": sum(c["R"] == 3 for c in cells),
        "primary_R3_cells_mean_trend_mse_favors_guerrero": sum(
            c["R"] == 3 and c["mean_delta_true_mse_multibracket_minus_guerrero"] > 0
            for c in cells
        ),
        "uncertainty_warning": "only five independent seeds per DGP cell",
    }


def make_plots(paired: list[dict], cells: list[dict], out: Path):
    """Plot R=3 scenario paired true-MSE contrasts and both-loss scatter."""
    prim = [c for c in cells if c["R"] == 3]
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(prim))
    w = 0.39
    ax.bar(x - w / 2, [c["mean_true_mse_guerrero"] for c in prim],
           w, label="Guerrero known ratio")
    ax.bar(x + w / 2, [c["mean_true_mse_multibracket"] for c in prim],
           w, label="Pooled LOOCV / multibracket")
    ax.set_xticks(x, [str(c["scenario_id"]) for c in prim])
    ax.set_xlabel("Scenario ID (R=3, five seeds per scenario)")
    ax.set_ylabel("Mean true latent-trend MSE")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "guerrero_vs_loocv_true_mse_by_scenario.png", dpi=160)
    plt.close(fig)

    records = [r for r in paired if r["R"] == 3]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter([r["delta_cv_guerrero_minus_multibracket"] for r in records],
               [r["delta_true_mse_multibracket_minus_guerrero"] for r in records],
               alpha=0.75)
    ax.axhline(0, linestyle="--", linewidth=1)
    ax.axvline(0, linestyle="--", linewidth=1)
    ax.set_xlabel("LOOCV MSE: Guerrero minus multibracket (positive favors LOOCV)")
    ax.set_ylabel("Trend MSE: multibracket minus Guerrero (positive favors Guerrero)")
    ax.set_title("Paired R=3 pool contrasts; 12 scenarios × 5 seeds")
    fig.tight_layout()
    fig.savefig(out / "guerrero_paired_two_loss_contrasts.png", dpi=160)
    plt.close(fig)


def run(input_csv: Path, out: Path) -> dict:
    paired = load_comparisons(input_csv)
    cells, summary = summarize(paired)
    out.mkdir(parents=True, exist_ok=True)
    _write_csv(out / "paired_pool_contrasts.csv", paired)
    _write_csv(out / "scenario_by_R_summary.csv", cells)
    (out / "audit_summary.json").write_text(json.dumps(summary, indent=2) + "\n",
                                             encoding="utf-8")
    make_plots(paired, cells, out)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=Path(
        "results/pooled_loocv_smoothness/guerrero/pilot/guerrero_solver_comparison.csv"
    ))
    parser.add_argument("--out-dir", type=Path, default=Path(
        "results/pooled_loocv_smoothness/guerrero/pilot/audit"
    ))
    args = parser.parse_args()
    print(json.dumps(run(args.csv, args.out_dir), indent=2))


if __name__ == "__main__":
    main()
