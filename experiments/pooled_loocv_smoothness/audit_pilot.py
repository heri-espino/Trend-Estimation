"""Audit an executed pooled LOOCV solver_comparison.csv.

This is a *descriptive numerical audit*, not a global-optimality
certificate or independent statistical replication. Uses the paired
pool/scenario/replicate observations, never merges independent pools.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def summarize(path: Path, tolerance: float = 1e-7) -> dict:
    """Return reproducible paired numerical comparisons across methods."""
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    required = {"bounded_brent", "multibracket_brent", "dense_reference"}
    groups = {}
    for row in rows:
        key = (int(row["scenario_id"]), int(row["replicate"]), int(row["R"]))
        d = groups.setdefault(key, {})
        if row["method"] in d:
            raise ValueError(f"duplicated result: {key}, {row['method']}")
        d[row["method"]] = row
    if not groups or any(set(group) != required for group in groups.values()):
        raise ValueError("every pool needs exactly the same three methods")

    def score(row):
        return float(row["best_loocv_mse"])

    def count(condition):
        return sum(bool(condition(g)) for g in groups.values())

    records = []
    for (scenario_id, replicate, r), g in sorted(groups.items()):
        b = g["bounded_brent"]
        m = g["multibracket_brent"]
        reference = g["dense_reference"]
        delta = score(b) - score(m)
        records.append({
            "scenario_id": scenario_id, "replicate": replicate, "R": r,
            "trend": m["trend"], "seasonality": m["seasonality"],
            "sigma": float(m["sigma"]), "n": int(m["n"]),
            "bounded_score": score(b), "multibracket_score": score(m),
            "dense_score": score(reference),
            "bounded_s": float(b["selected_s"]),
            "multibracket_s": float(m["selected_s"]),
            "bounded_regret": delta,
            "bounded_relative_regret_percent": 100 * delta / score(m),
            "detected_stationary_roots": int(m["stationary_count"]),
        })

    summary = {
        "source_csv": str(path),
        "source_row_count": len(rows),
        "paired_pool_count": len(groups),
        "method_names": sorted(required),
        "tolerance": tolerance,
        "bounded_worse_than_multibracket": count(
            lambda g: score(g["bounded_brent"]) >
            score(g["multibracket_brent"]) + tolerance
        ),
        "multibracket_worse_than_bounded": count(
            lambda g: score(g["multibracket_brent"]) >
            score(g["bounded_brent"]) + tolerance
        ),
        "bounded_better_than_finite_grid": count(
            lambda g: score(g["bounded_brent"]) <
            score(g["dense_reference"]) - tolerance
        ),
        "multibracket_better_than_finite_grid": count(
            lambda g: score(g["multibracket_brent"]) <
            score(g["dense_reference"]) - tolerance
        ),
        "multibracket_stationary_count_histogram": dict(sorted(Counter(
            int(g["multibracket_brent"]["stationary_count"])
            for g in groups.values()
        ).items())),
        "at_least_three_detected_stationary_roots": count(
            lambda g: int(g["multibracket_brent"]["stationary_count"]) >= 3
        ),
        "selected_right_endpoint_multibracket": count(
            lambda g: float(g["multibracket_brent"]["selected_s"]) == 1.0
        ),
        "selected_left_endpoint_multibracket": count(
            lambda g: float(g["multibracket_brent"]["selected_s"]) == 0.0
        ),
        "by_pool_size": {},
        "max_bounded_absolute_regret": max(x["bounded_regret"] for x in records),
        "max_bounded_relative_regret_percent": max(
            x["bounded_relative_regret_percent"] for x in records
        ),
        "cases_bounded_worse": [
            x for x in records if x["bounded_regret"] > tolerance
        ],
        "interpretation": (
            "All minima and root counts are numerically detected, NOT "
            "globally certified. 3+ stationary roots do not prove 2+ "
            "distinct minima; near-infinite lambda needs special checks."
        ),
    }
    for r in sorted({x["R"] for x in records}):
        subset = [x for x in records if x["R"] == r]
        summary["by_pool_size"][str(r)] = {
            "n_pools": len(subset),
            "at_least_three_detected_stationary_roots": sum(
                x["detected_stationary_roots"] >= 3 for x in subset
            ),
            "bounded_worse_than_multibracket": sum(
                x["bounded_regret"] > tolerance for x in subset
            ),
            "mean_selected_multibracket_s": sum(
                x["multibracket_s"] for x in subset
            ) / len(subset),
        }
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=Path(
        "results/pooled_loocv_smoothness/pilot/solver_comparison.csv"
    ))
    parser.add_argument("--out", type=Path, default=None,
                        help="Optional JSON audit destination")
    args = parser.parse_args()
    summary = summarize(args.csv)
    result = json.dumps(summary, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result + "\n", encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
