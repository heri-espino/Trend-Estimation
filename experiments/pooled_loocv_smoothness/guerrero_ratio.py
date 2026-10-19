"""Guerrero (2007) known-variance-ratio benchmark for observed-series smoothing.

This independent experiment generates d=2 integrated stochastic trends
    D_2 tau = epsilon, epsilon ~ N(0, sigma_epsilon^2 I)
    y = tau + eta,       eta ~ N(0, sigma_eta^2 I)
and compares lambda_G = sigma_eta^2 / sigma_epsilon^2 to the
single-start and multi-bracket optimizers of *pooled observed LOOCV*.

Guerrero is supplied the TRUE DGP variances. That is a model-informed
oracle benchmark, not a variance estimator applicable to unknown market
noise. True trend MSE is evaluated AFTER selecting lambda; latent tau
never enters LOOCV selection. No forecasting is involved.
"""

from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from .objective import PooledLOOCV
from .search import bounded_brent, dense_reference, multibracket_brent


@dataclass(frozen=True)
class GuerreroScenario:
    n: int
    sigma_eta: float
    sigma_epsilon: float
    order: int = 2

    def __post_init__(self):
        if self.n < self.order + 3 or self.order not in (1, 2):
            raise ValueError("requires n >= d+3, and d in {1,2}")
        if not np.isfinite(self.sigma_eta) or not np.isfinite(self.sigma_epsilon):
            raise ValueError("finite standard deviations required")
        if self.sigma_eta <= 0 or self.sigma_epsilon <= 0:
            raise ValueError("standard deviations must be positive")

    @property
    def lambda_guerrero(self) -> float:
        """Known-variance ratio, not an estimated hyperparameter."""
        return (self.sigma_eta / self.sigma_epsilon) ** 2


def integrated_trend(innovations: np.ndarray, order: int = 2,
                     intercept: float = 0.0, slope: float = 0.02) -> np.ndarray:
    """Integrate forward differences with an unpenalized polynomial start."""
    innovations = np.asarray(innovations, dtype=float)
    if innovations.ndim != 1:
        raise ValueError("innovations must be one-dimensional")
    n = innovations.size + order
    tau = np.empty(n, dtype=float)
    if order == 1:
        tau[0] = intercept
        for i in range(1, n):
            tau[i] = tau[i - 1] + innovations[i - 1]
    elif order == 2:
        tau[0] = intercept
        tau[1] = intercept + slope
        for i in range(2, n):
            tau[i] = 2.0 * tau[i - 1] - tau[i - 2] + innovations[i - 2]
    else:
        raise ValueError("only orders 1 and 2 are included in this experiment")
    return tau


def draw_observed_pool(scenario: GuerreroScenario, r: int, seed: int):
    """Draw R independent latent stochastic trends and observation noises.

    The first member of R=1 and R=3 pools is exactly the same at the
    same seed; this creates an interpretable *nested paired* comparison.
    """
    if r < 1:
        raise ValueError("r must be >=1")
    rng = np.random.default_rng(seed)
    trends, observed = [], []
    for _ in range(r):
        increments = rng.normal(0.0, scenario.sigma_epsilon,
                                scenario.n - scenario.order)
        trend = integrated_trend(increments, scenario.order)
        obs = trend + rng.normal(0.0, scenario.sigma_eta, scenario.n)
        trends.append(trend)
        observed.append(obs)
    return np.asarray(observed), np.asarray(trends)


def reconstruction_mse(obj: PooledLOOCV, true_trends: np.ndarray, lam: float) -> float:
    """Pooled true latent trend MSE (diagnostic only, never tune using it)."""
    if true_trends.shape != obj.y.shape:
        raise ValueError("true trend/observed array shape mismatch")
    return float(np.mean((obj.trend(lam) - true_trends) ** 2))


def preset_design(preset: str):
    if preset == "smoke":
        scenarios = [
            GuerreroScenario(24, 0.5, 0.25),
            GuerreroScenario(24, 2.0, 0.25),
        ]
        return scenarios, 2, (1, 3), 121, 31, 20261018
    if preset in ("pilot", "confirmatory"):
        scenarios = [
            GuerreroScenario(n, eta, eps)
            for n, eta, eps in product((50, 200), (0.5, 2.0), (0.1, 0.3, 1.0))
        ]
        return (scenarios, 5 if preset == "pilot" else 100, (1, 3),
                401 if preset == "pilot" else 801,
                101 if preset == "pilot" else 201,
                20262000 if preset == "pilot" else 20269000)
    raise ValueError(f"unknown preset: {preset}")


def _git_sha() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], timeout=3, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _write_csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _example_plot(out: Path, obj: PooledLOOCV, truth: np.ndarray,
                  picks: dict[str, float], scenario: GuerreroScenario):
    """Plot full-series reconstruction and loss with oracle-ratio marker."""
    grid = np.exp(np.linspace(-18, 30, 301))
    ss = np.array([obj.smoothness(float(lam)) for lam in grid])
    loss = np.array([obj.score(float(lam)) for lam in grid])
    trend_error = np.array([reconstruction_mse(obj, truth, float(lam))
                            for lam in grid])
    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(9, 10))
    x = np.arange(obj.n)
    ax0.plot(x, obj.y[0], label="Observed y", alpha=0.5)
    ax0.plot(x, truth[0], label="True latent trend", linewidth=2)
    for label in ("guerrero_known_ratio", "multibracket_brent"):
        lam = picks[label]
        ax0.plot(x, obj.trend(lam)[0], label=f"{label} fit", linestyle="--")
    ax0.set_ylabel("Value")
    ax0.set_xlabel("Observation index")
    ax0.legend(fontsize=8)
    ax1.plot(ss, loss, label="Pooled observed LOOCV MSE")
    ax2.plot(ss, trend_error, label="Realized latent trend MSE")
    for ax in (ax1, ax2):
        for label in ("guerrero_known_ratio", "bounded_brent", "multibracket_brent"):
            lam = picks[label]
            ax.axvline(obj.smoothness(lam), linestyle="--", linewidth=1, label=label)
        ax.set_xlabel("Normalized smoothness S")
        ax.legend(fontsize=8)
    ax1.set_ylabel("LOOCV MSE")
    ax2.set_ylabel("Latent trend MSE")
    fig.suptitle(
        f"Guerrero d={scenario.order}, N={scenario.n}, "
        f"sigma_eta={scenario.sigma_eta}, sigma_epsilon={scenario.sigma_epsilon}; "
        f"R={obj.r}"
    )
    fig.tight_layout()
    fig.savefig(out / "guerrero_example.png", dpi=160)
    plt.close(fig)
    _write_csv(out / "guerrero_example_curves.csv", [
        {"lambda": float(lam), "S": float(s),
         "pooled_loocv_mse": float(cv), "true_trend_mse_diagnostic": float(mse)}
        for lam, s, cv, mse in zip(grid, ss, loss, trend_error)
    ])


def execute(preset: str, out: Path, dry_run: bool = False) -> dict:
    scenarios, repeats, r_values, n_grid, n_scan, seed_base = preset_design(preset)
    manifest = {
        "protocol": "guerrero_known_variance_ratio_pooled_loocv_v1",
        "status": "planned" if dry_run else "executed",
        "preset": preset, "created_utc": datetime.now(timezone.utc).isoformat(),
        "DGP": "D_d tau = epsilon; y = tau + eta; independent Gaussian noises",
        "true_lambda_definition": "sigma_eta**2 / sigma_epsilon**2",
        "true_lambda_is_known_parameter_oracle": True,
        "model": "V=I, mu=0, fixed initial trend values",
        "scenario_count": len(scenarios),
        "scenarios": [{"n": s.n, "d": s.order,
                       "sigma_eta": s.sigma_eta,
                       "sigma_epsilon": s.sigma_epsilon,
                       "guerrero_lambda": s.lambda_guerrero} for s in scenarios],
        "independent_seed_repeats_per_cell": repeats,
        "pool_sizes": list(r_values),
        "nested_pools": True,
        "total_pool_cases": len(scenarios) * repeats * len(r_values),
        "solver_methods": ["guerrero_known_ratio", "bounded_brent",
                           "multibracket_brent", "dense_reference"],
        "dense_grid_points": n_grid,
        "derivative_scan_points": n_scan,
        "log_lambda_bounds": [-20, 35],
        "seed_base": seed_base,
        "git_sha": _git_sha(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "caveats": [
            "Guerrero uses known true simulation variances, not estimated real-data variances.",
            "The deterministic initialization of each integrated trend is not the diffuse prior formulation.",
            "Results for R=1 and R=3 at the same seed share their first generated series.",
            "The observed LOOCV target and latent trend MSE have different estimands.",
            "Numerical root-search candidates and finite grids are not global certificates.",
        ],
    }
    if dry_run:
        print(json.dumps(manifest, indent=2))
        return manifest
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    first_plot = False
    for case_id, scenario in enumerate(scenarios):
        for replicate in range(repeats):
            seed = seed_base + case_id * 10000 + replicate
            for r in r_values:
                y, tau = draw_observed_pool(scenario, r, seed)
                obj = PooledLOOCV(y, order=scenario.order)
                bounded = bounded_brent(obj)
                multibracket = multibracket_brent(obj, n_scan=n_scan)
                dense = dense_reference(obj, n_grid=n_grid)
                selected = {
                    "guerrero_known_ratio": scenario.lambda_guerrero,
                    "bounded_brent": bounded.best.lam,
                    "multibracket_brent": multibracket.best.lam,
                    "dense_reference": dense.best.lam,
                }
                for method, lam in selected.items():
                    rows.append({
                        "scenario_id": case_id, "replicate": replicate,
                        "seed": seed, "R": r, "n": scenario.n, "d": scenario.order,
                        "sigma_eta": scenario.sigma_eta,
                        "sigma_epsilon": scenario.sigma_epsilon,
                        "known_variance_ratio_lambda": scenario.lambda_guerrero,
                        "method": method,
                        "selected_lambda": lam,
                        "selected_s": obj.smoothness(lam),
                        "pooled_loocv_mse": obj.score(lam),
                        "true_trend_mse": reconstruction_mse(obj, tau, lam),
                        "selected_exact_endpoint": bool(lam == 0 or np.isinf(lam)),
                        "stationary_candidates_detected":
                            multibracket.as_dict()["stationary_count"],
                    })
                if not first_plot:
                    _example_plot(out, obj, tau, selected, scenario)
                    first_plot = True
    _write_csv(out / "guerrero_solver_comparison.csv", rows)
    manifest["rows_written"] = len(rows)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n",
                                       encoding="utf-8")
    summary = paired_summary(rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n",
                                      encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def paired_summary(rows: list[dict]) -> dict:
    """Aggregate paired pool-level metrics without treating methods as replicates."""
    groups = {}
    for row in rows:
        key = (row["scenario_id"], row["replicate"], row["R"])
        group = groups.setdefault(key, {})
        method = row["method"]
        if method in group:
            raise ValueError(f"duplicate row for {key}/{method}")
        group[method] = row
    expected = {"guerrero_known_ratio", "bounded_brent",
                "multibracket_brent", "dense_reference"}
    if any(set(g) != expected for g in groups.values()):
        raise ValueError("missing solver method in at least one paired pool")

    def aggregate(gs: list[dict]):
        return {
            name: {
                "mean_LOOCV_MSE": float(np.mean([g[name]["pooled_loocv_mse"] for g in gs])),
                "mean_true_trend_MSE": float(np.mean([g[name]["true_trend_mse"] for g in gs])),
                "mean_S": float(np.mean([g[name]["selected_s"] for g in gs])),
            }
            for name in sorted(expected)
        }

    groups_list = list(groups.values())
    by_r = {}
    for r in sorted({key[2] for key in groups}):
        gs = [g for key, g in groups.items() if key[2] == r]
        by_r[str(r)] = {
            "pool_count": len(gs),
            "metrics": aggregate(gs),
            "guerrero_lower_true_mse_than_multibracket_count": sum(
                g["guerrero_known_ratio"]["true_trend_mse"] <
                g["multibracket_brent"]["true_trend_mse"] for g in gs
            ),
            "multibracket_lower_LOOCV_than_guerrero_count": sum(
                g["multibracket_brent"]["pooled_loocv_mse"] + 1e-8 <
                g["guerrero_known_ratio"]["pooled_loocv_mse"] for g in gs
            ),
        }
    return {
        "pool_count": len(groups),
        "method_count": len(expected),
        "row_count": len(rows),
        "overall": aggregate(groups_list),
        "by_R": by_r,
        "multibracket_lower_LOOCV_than_guerrero_count": sum(
            g["multibracket_brent"]["pooled_loocv_mse"] + 1e-8 <
            g["guerrero_known_ratio"]["pooled_loocv_mse"] for g in groups_list
        ),
        "guerrero_lower_true_MSE_than_multibracket_count": sum(
            g["guerrero_known_ratio"]["true_trend_mse"] <
            g["multibracket_brent"]["true_trend_mse"] for g in groups_list
        ),
        "multibracket_lower_true_MSE_than_guerrero_count": sum(
            g["multibracket_brent"]["true_trend_mse"] <
            g["guerrero_known_ratio"]["true_trend_mse"] for g in groups_list
        ),
        "bounded_worse_LOOCV_than_multibracket_count": sum(
            g["bounded_brent"]["pooled_loocv_mse"] >
            g["multibracket_brent"]["pooled_loocv_mse"] + 1e-7
            for g in groups_list
        ),
        "interpretation": (
            "A smaller observed LOOCV score does not imply lower true latent-trend MSE. "
            "Guerrero is given actual DGP variances; pooled rows at R=1 and R=3 "
            "are nested. Report paired by-seed uncertainty before scientific claims."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=("smoke", "pilot", "confirmatory"),
                        default="smoke")
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    out = args.out_dir or Path("results/pooled_loocv_smoothness/guerrero") / args.preset
    execute(args.preset, out, args.dry_run)


if __name__ == "__main__":
    main()
