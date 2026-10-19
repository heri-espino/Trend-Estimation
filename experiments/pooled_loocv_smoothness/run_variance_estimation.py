"""Feasible variance-ratio comparison at different noise levels.

Compares known Guerrero population ratio, *estimated* ratios from
nonnegative moments / Gaussian covariance likelihood of differences,
and pooled observed-series LOOCV. Two losses are reported separately:
observed pooled LOOCV MSE and true latent-trend reconstruction MSE.

Results are exploratory simulations, NOT a forecasting study.
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

from .guerrero_ratio import draw_observed_pool, preset_design, reconstruction_mse
from .objective import PooledLOOCV
from .search import bounded_brent
from .variance_estimation import estimate_gaussian_differences, estimate_moments


def _git_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL,
            timeout=3, text=True,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _write_csv(path, rows):
    if not rows:
        raise ValueError("expected nonempty comparison rows")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows):
    """Equal cell/seed weighting, but R=1 and R=3 results are nested."""
    methods = sorted(set(r["method"] for r in rows))
    result = {
        "rows": len(rows),
        "methods": methods,
        "method_labels": {
            "guerrero_known_ratio": "oracle_true_simulation_variances",
            "estimated_gaussian_difference_ml": "feasible_difference_covariance_mle",
            "estimated_moments_nnls": "feasible_nonnegative_two_moment_method",
            "pooled_loocv_bounded_brent": "feasible_observed_loocv_optimizer",
        },
        "by_R": {},
        "warning": (
            "R=1 is nested in R=3 for same seed; 5 seeds/cell are exploratory. "
            "Moment estimates can set epsilon variance to zero and cause "
            "extreme oversmoothing and huge mean errors. Known ratio is an oracle."
        ),
    }
    for R in sorted({r["R"] for r in rows}):
        part = [r for r in rows if r["R"] == R]
        summary = {"number_pools": len(part) // len(methods), "by_method": {}}
        for method in methods:
            mm = [r for r in part if r["method"] == method]
            summary["by_method"][method] = {
                "mean_observed_loocv_mse": float(np.mean([r["loocv_mse"] for r in mm])),
                "mean_true_trend_mse": float(np.mean([r["true_trend_mse"] for r in mm])),
                "median_true_trend_mse": float(np.median([r["true_trend_mse"] for r in mm])),
                "mean_absolute_error_sigma_eta2": (
                    float(np.mean([abs(r["estimated_sigma_eta2"] - r["true_sigma_eta2"])
                                   for r in mm]))
                    if method != "pooled_loocv_bounded_brent" else None
                ),
                "mean_absolute_error_sigma_epsilon2": (
                    float(np.mean([abs(r["estimated_sigma_epsilon2"] - r["true_sigma_epsilon2"])
                                   for r in mm]))
                    if method != "pooled_loocv_bounded_brent" else None
                ),
                "infinite_lambda_count": sum(bool(np.isinf(r["selected_lambda"])) for r in mm),
                "zero_lambda_count": sum(r["selected_lambda"] == 0 for r in mm),
                "negative_unconstrained_moment_count": sum(
                    bool(r["negative_unconstrained_moments"]) for r in mm
                ),
            }
        result["by_R"][str(R)] = summary
    return result


def _scenario_table(rows):
    result = []
    for R in (1, 3):
        for scenario_id in sorted({r["scenario_id"] for r in rows}):
            for method in sorted({r["method"] for r in rows}):
                part = [
                    r for r in rows
                    if r["R"] == R and r["scenario_id"] == scenario_id
                    and r["method"] == method
                ]
                if not part:
                    continue
                first = part[0]
                result.append({
                    "R": R, "scenario_id": scenario_id, "n": first["n"],
                    "sigma_eta": first["sigma_eta"], "sigma_epsilon": first["sigma_epsilon"],
                    "true_lambda": first["true_lambda"], "method": method,
                    "seed_count": len(part),
                    "mean_true_trend_mse": float(np.mean(
                        [p["true_trend_mse"] for p in part])),
                    "mean_loocv_mse": float(np.mean([p["loocv_mse"] for p in part])),
                    "median_true_trend_mse": float(np.median(
                        [p["true_trend_mse"] for p in part])),
                })
    return result


def _figure(out, rows):
    cell = _scenario_table(rows)
    methods = ("guerrero_known_ratio", "estimated_gaussian_difference_ml",
               "pooled_loocv_bounded_brent", "estimated_moments_nnls")
    prim = [p for p in cell if p["R"] == 3]
    fig, ax = plt.subplots(figsize=(11, 6))
    xx = np.arange(len({p["scenario_id"] for p in prim}))
    for method in methods:
        a = sorted((p for p in prim if p["method"] == method),
                   key=lambda p: p["scenario_id"])
        ax.plot(xx, [p["mean_true_trend_mse"] for p in a], marker="o",
                label=method)
    ax.set_xticks(xx, [str(int(p)) for p in xx])
    ax.set_yscale("symlog", linthresh=.01)
    ax.set_xlabel("Scenario (noise levels listed in scenario_summary.csv)")
    ax.set_ylabel("Mean realized true trend MSE (symlog)")
    ax.set_title("Known versus estimated variance ratios and pooled LOOCV (R=3)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "true_mse_by_noise_level.png", dpi=160)
    plt.close(fig)


def _scale_check(out, scenario, seed):
    """Multiplying y,tau by c should preserve estimated lambda and multiply
    estimated variances/MSE by c^2. Not a new independent sample.
    """
    y, tau = draw_observed_pool(scenario, r=3, seed=seed)
    result = []
    for scale in (.5, 1., 2.):
        yy, tt = y * scale, tau * scale
        obj = PooledLOOCV(yy, order=scenario.order)
        methods = {
            "guerrero_known_ratio": (scenario.lambda_guerrero, None),
            "estimated_moments_nnls": (None, estimate_moments(yy, obj.d)),
            "estimated_gaussian_difference_ml":
                (None, estimate_gaussian_differences(yy, obj.d)),
            "pooled_loocv_bounded_brent": (bounded_brent(obj).best.lam, None),
        }
        for name, (known, estimate) in methods.items():
            lam = known if estimate is None else estimate.lambda_ratio
            result.append({
                "scale": scale, "scale_squared": scale ** 2, "method": name,
                "selected_lambda": lam, "loocv_mse": obj.score(lam),
                "true_trend_mse": reconstruction_mse(obj, tt, lam),
                "sigma_eta2_hat": (
                    estimate.sigma_eta2 if estimate is not None else
                    scenario.sigma_eta ** 2 * scale ** 2
                ),
                "sigma_epsilon2_hat": (
                    estimate.sigma_epsilon2 if estimate is not None else
                    scenario.sigma_epsilon ** 2 * scale ** 2
                ),
            })
    _write_csv(out / "common_noise_scale_invariance.csv", result)


def execute(preset: str, out: Path, dry_run: bool = False):
    scenarios, repeats, pool_sizes, _, _, seed_base = preset_design(preset)
    methods = ("guerrero_known_ratio", "estimated_gaussian_difference_ml",
               "estimated_moments_nnls", "pooled_loocv_bounded_brent")
    manifest = {
        "protocol": "guerrero_feasible_estimated_variance_ratio_v1",
        "status": "planned" if dry_run else "executed",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "preset": preset,
        "DGP": "independent Gaussian D_d tau=epsilon and y=tau+eta",
        "scenarios": [{"n": s.n, "sigma_eta": s.sigma_eta,
                       "sigma_epsilon": s.sigma_epsilon,
                       "true_lambda": s.lambda_guerrero} for s in scenarios],
        "seeds_per_cell": repeats,
        "pool_sizes": list(pool_sizes),
        "total_pools": len(scenarios) * repeats * len(pool_sizes),
        "methods": methods,
        "seed_base": seed_base,
        "git_sha": _git_sha(),
        "python": platform.python_version(),
        "numpy": np.__version__, "scipy": scipy.__version__,
        "interpretive_limits": [
            "Known Guerrero ratio is an oracle using true DGP variances.",
            "Gaussian variance components maximize marginal likelihood of D_d y, not y.",
            "Moment NNLS estimate may lie on boundary, causing catastrophic over-smoothing.",
            "One-shot Brent is local; does not guarantee global LOOCV minimum.",
            "R=1 and R=3 at matching seed are nested and not independent.",
            "Scale experiment rescales the same path, not independent draws.",
            "No financial data, predictions or future values are used.",
        ],
    }
    if dry_run:
        print(json.dumps(manifest, indent=2))
        return manifest

    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for scenario_id, scenario in enumerate(scenarios):
        for replicate in range(repeats):
            seed = seed_base + scenario_id * 10000 + replicate
            for R in pool_sizes:
                y, tau = draw_observed_pool(scenario, R, seed)
                obj = PooledLOOCV(y, order=scenario.order)
                mom = estimate_moments(y, obj.d)
                ml = estimate_gaussian_differences(y, obj.d)
                estimates = {
                    "guerrero_known_ratio": scenario.lambda_guerrero,
                    "pooled_loocv_bounded_brent": bounded_brent(obj).best.lam,
                    "estimated_moments_nnls": mom.lambda_ratio,
                    "estimated_gaussian_difference_ml": ml.lambda_ratio,
                }
                for method, lam in estimates.items():
                    fit = (mom if method == "estimated_moments_nnls" else
                           ml if method == "estimated_gaussian_difference_ml" else None)
                    rows.append({
                        "scenario_id": scenario_id, "replicate": replicate,
                        "seed": seed, "R": R, "n": scenario.n,
                        "sigma_eta": scenario.sigma_eta,
                        "sigma_epsilon": scenario.sigma_epsilon,
                        "true_sigma_eta2": scenario.sigma_eta ** 2,
                        "true_sigma_epsilon2": scenario.sigma_epsilon ** 2,
                        "true_lambda": scenario.lambda_guerrero,
                        "method": method, "selected_lambda": lam,
                        "selected_s": obj.smoothness(lam),
                        "loocv_mse": obj.score(lam),
                        "true_trend_mse": reconstruction_mse(obj, tau, lam),
                        "estimated_sigma_eta2": (
                            fit.sigma_eta2 if fit is not None else
                            (scenario.sigma_eta ** 2 if method == "guerrero_known_ratio"
                             else float("nan"))
                        ),
                        "estimated_sigma_epsilon2": (
                            fit.sigma_epsilon2 if fit is not None else
                            (scenario.sigma_epsilon ** 2 if method == "guerrero_known_ratio"
                             else float("nan"))
                        ),
                        "negative_unconstrained_moments": (
                            fit.negative_unconstrained_moments if fit else False
                        ),
                    })
    _write_csv(out / "variance_estimator_comparison.csv", rows)
    _write_csv(out / "scenario_summary.csv", _scenario_table(rows))
    _figure(out, rows)
    _scale_check(out, scenarios[0], seed_base)
    summary = summarize(rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n",
                                       encoding="utf-8")
    manifest["rows_written"] = len(rows)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n",
                                        encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--preset", choices=("smoke", "pilot", "confirmatory"),
                   default="smoke")
    p.add_argument("--out-dir", type=Path, default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    out = args.out_dir or Path(
        "results/pooled_loocv_smoothness/guerrero/estimated_variances") / args.preset
    execute(args.preset, out, args.dry_run)


if __name__ == "__main__":
    main()
