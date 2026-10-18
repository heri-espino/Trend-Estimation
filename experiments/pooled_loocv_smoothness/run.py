"""Run standalone observed-series pooled LOOCV numerical experiments.

No forecasting or downloaded financial data. Heavy confirmatory runs
must be launched explicitly and are never part of CI.
"""

from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from .objective import PooledLOOCV
from .search import bounded_brent, dense_reference, multibracket_brent
from .simulate import Scenario, draw_pool, factorial_scenarios


def preset_design(preset: str):
    """Return scenarios, replicate counts, pool sizes, and solver budgets."""
    if preset == "smoke":
        return ([Scenario("linear", False, 0.5, 24),
                 Scenario("nonlinear", True, 2.0, 24)], 2, (1, 3), 121, 31, 0)
    if preset == "pilot":
        return (factorial_scenarios(), 5, (1, 3), 401, 101, 100_000)
    if preset == "confirmatory":
        return (factorial_scenarios(), 100, (1, 3), 801, 201, 900_000)
    raise ValueError(f"unknown preset: {preset}")


def git_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, timeout=3,
            stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def write_csv(path: Path, records: list[dict]):
    if not records:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def draw_case_figure(out: Path, scenario: Scenario, y: np.ndarray,
                     tau: np.ndarray, season: np.ndarray, selected_s: float):
    """A reproducible explanatory figure, never an empirical test."""
    obj = PooledLOOCV(y, order=2)
    logs = np.linspace(-20, 35, 251)
    lambdas = np.exp(logs)
    smoothness = [obj.smoothness(float(lam)) for lam in lambdas]
    loss = [obj.score(float(lam)) for lam in lambdas]
    s_idx = int(np.argmin(abs(np.asarray(smoothness) - selected_s)))
    lam_selected = float(lambdas[s_idx])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7))
    tt = np.arange(1, scenario.n + 1)
    ax1.plot(tt, tau, label="True latent trend")
    if scenario.seasonality:
        ax1.plot(tt, tau + season, label="Trend + seasonal component", alpha=0.6)
    ax1.plot(tt, y[0], label="Observed first series", alpha=0.65)
    ax1.plot(tt, obj.trend(lam_selected)[0], label="Approx. selected PLS trend")
    ax1.set_xlabel("Observation index")
    ax1.set_ylabel("Value")
    ax1.legend(loc="best", fontsize=8)
    ax2.plot(smoothness, loss, label="Pooled LOOCV MSE")
    ax2.axvline(selected_s, linestyle="--", label="Selected smoothness")
    ax2.scatter([0, 1], [obj.score(0), obj.score(float("inf"))],
                label="Exact endpoint scores", s=28)
    ax2.set_xlabel("Normalized smoothness S")
    ax2.set_ylabel("Pooled LOOCV MSE")
    ax2.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "example_signal_and_objective.png", dpi=150)
    plt.close(fig)
    write_csv(
        out / "example_loss_curve.csv",
        [{"lambda": float(lam), "s": float(s), "loocv_mse": float(v)}
         for lam, s, v in zip(lambdas, smoothness, loss)],
    )


def execute(preset: str, out: Path, dry_run: bool = False):
    scenarios, repeats, pool_sizes, n_grid, n_scan, seed_offset = preset_design(preset)
    runs = len(scenarios) * repeats * len(pool_sizes)
    manifest = {
        "protocol": "independent_pooled_observed_series_LOOCV_v1",
        "status": "planned" if dry_run else "executed",
        "preset": preset, "created_utc": datetime.now(timezone.utc).isoformat(),
        "factorial_scenarios": [s.as_dict() for s in scenarios],
        "independent_seed_repeats_per_cell": repeats,
        "pool_sizes": list(pool_sizes), "instance_count": runs,
        "difference_order": 2, "log_lambda_bounds": [-20, 35],
        "dense_grid_points": n_grid, "derivative_scan_points": n_scan,
        "seed_offset": seed_offset, "git_commit": git_sha(),
        "python": platform.python_version(),
        "numpy": np.__version__, "scipy": scipy.__version__,
        "method_caveat": "dense grid not certified; sign-scan Brent not complete",
    }
    if dry_run:
        print(json.dumps(manifest, indent=2))
        return
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    first_figure = False
    for idx, scenario in enumerate(scenarios):
        for replicate in range(repeats):
            # Within one cell, the first observation replicate is shared
            # between R=1 and R=3, producing a paired R contrast.
            seed = seed_offset + idx * 10_000 + replicate
            for r in pool_sizes:
                observed, tau, season = draw_pool(scenario, r, seed)
                objective = PooledLOOCV(observed, order=2)
                methods = (
                    bounded_brent(objective),
                    multibracket_brent(objective, n_scan=n_scan),
                    dense_reference(objective, n_grid=n_grid),
                )
                scores = {method.method: method.best.score for method in methods}
                for method in methods:
                    row = {
                        "scenario_id": idx, "replicate": replicate,
                        "seed": seed, "R": r,
                        **scenario.as_dict(),
                        **method.as_dict(),
                        "dense_grid_score": scores["dense_reference"],
                        "gap_vs_finite_grid": method.best.score - scores["dense_reference"],
                        "left_endpoint_mse": objective.score(0),
                        "right_endpoint_mse": objective.score(float("inf")),
                    }
                    rows.append(row)
                if not first_figure:
                    draw_case_figure(out, scenario, observed, tau, season,
                                     methods[1].best.s)
                    first_figure = True
    write_csv(out / "solver_comparison.csv", rows)
    manifest["rows_written"] = len(rows)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} method comparisons for {runs} pools to {out}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=("smoke", "pilot", "confirmatory"),
                        default="smoke")
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true",
                        help="Print all cells/solver budgets without generating data")
    args = parser.parse_args()
    out = args.out_dir or Path("results/pooled_loocv_smoothness") / args.preset
    execute(args.preset, out, args.dry_run)


if __name__ == "__main__":
    main()
