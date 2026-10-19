"""Estimate both Guerrero-model noise variances from observed series.

This is a NEW Gaussian contrast-likelihood (restricted-likelihood) plug-in
extension, not a procedure attributed to Guerrero (2007). Under d=2:
 D y = epsilon + D eta, Cov(D y) = sigma_epsilon^2 I
                                      + sigma_eta^2 D D^T.
The unobserved trend is NEVER used in estimating either variance.
The true DGP variances are available only as simulation evaluation data.

For R independently generated series with common variances and order,
we maximize the Gaussian likelihood of their *difference contrasts*,
profiling the common scale over lambda=sigma_eta^2/sigma_epsilon^2.
Finite lambda=0 and the lambda=infinity boundary are compared exactly.

A finite adaptive multi-basin numerical search is NOT a certificate of
global likelihood optimality. The dimension order and likelihood
assumptions must be checked before financial-data applications.
"""

from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.optimize import minimize_scalar
from scipy.special import logsumexp

from .guerrero_ratio import (
    GuerreroScenario, draw_observed_pool, paired_summary, preset_design,
    reconstruction_mse,
)
from .objective import PooledLOOCV, difference_matrix
from .search import bounded_brent, multibracket_brent


@dataclass(frozen=True)
class ContrastMLE:
    """Maximized likelihood based on observed trend-difference contrasts."""
    sigma_eta2: float
    sigma_epsilon2: float
    lam: float
    neg2_loglike_excluding_constant: float
    candidate_count: int
    seconds: float

    def as_dict(self) -> dict:
        return {
            "estimated_sigma_eta2": self.sigma_eta2,
            "estimated_sigma_epsilon2": self.sigma_epsilon2,
            "estimated_lambda": self.lam,
            "profile_objective": self.neg2_loglike_excluding_constant,
            "profile_candidate_count": self.candidate_count,
            "estimation_seconds": self.seconds,
        }


class VarianceContrastLikelihood:
    """Gaussian likelihood of D y, shared independent variance components.

    With d=2: gamma_0 = sigma_eps2+6 sigma_eta2,
    gamma_1 = -4 sigma_eta2, gamma_2 = sigma_eta2.
    We use the entire covariance, not noisy moment estimates.
    """

    def __init__(self, observed: np.ndarray, order: int = 2):
        y = np.asarray(observed, dtype=float)
        if y.ndim == 1:
            y = y[None, :]
        if y.ndim != 2 or y.shape[1] < order + 3 or y.shape[0] < 1:
            raise ValueError("expected (R,N) with N >= order+3")
        if not np.all(np.isfinite(y)):
            raise ValueError("all observations must be finite")
        self.y = y.copy()
        self.r, self.n = y.shape
        self.d = difference_matrix(self.n, order)
        self.m = self.n - order
        self.z = (self.d @ self.y.T).T
        a = self.d @ self.d.T
        eig, u = np.linalg.eigh(a)
        if np.min(eig) <= 0:
            raise ArithmeticError("difference contrast covariance must be positive definite")
        self.eig = eig
        self.nu2 = (self.z @ u) ** 2  # R by m
        self.squares = np.sum(self.nu2, axis=0)
        self.mean_square = float(np.mean(self.z**2))
        if self.mean_square <= 0:
            raise ValueError("all differences are exactly zero: variance components unidentified")

    def profile(self, lam: float) -> tuple[float, float, float]:
        """Return (negative twice log likelihood up to constant, var_eps, var_eta)."""
        if np.isnan(lam) or lam < 0:
            raise ValueError("lambda must be nonnegative")
        if np.isinf(lam):
            eta2 = float(np.sum(self.squares / self.eig) / (self.r * self.m))
            obj = self.r * self.m * np.log(eta2) + self.r * np.sum(np.log(self.eig))
            return float(obj), 0.0, eta2
        a = 1 + lam * self.eig
        eps2 = float(np.sum(self.squares / a) / (self.r * self.m))
        eta2 = float(lam * eps2)
        obj = self.r * self.m * np.log(eps2) + self.r * np.sum(np.log(a))
        return float(obj), eps2, eta2

    def fit(self, n_scan: int = 121, log_bounds=(-18.0, 25.0)) -> ContrastMLE:
        """Profile both variances, compare finite local basins and boundaries."""
        if n_scan < 5:
            raise ValueError("n_scan must be >= 5")
        start = perf_counter()
        grid = np.linspace(*log_bounds, n_scan)
        scores = np.array([self.profile(float(np.exp(x)))[0] for x in grid])
        candidates: list[float] = [0.0, float("inf"),
                                   float(np.exp(grid[0])), float(np.exp(grid[-1]))]
        for i in range(1, n_scan - 1):
            if scores[i] <= scores[i - 1] and scores[i] <= scores[i + 1]:
                best = minimize_scalar(
                    lambda x: self.profile(float(np.exp(x)))[0],
                    method="bounded",
                    bounds=(float(grid[i - 1]), float(grid[i + 1])),
                    options={"xatol": 1e-10},
                )
                if best.success:
                    candidates.append(float(np.exp(best.x)))
        best_lam = min(candidates, key=lambda lam: self.profile(lam)[0])
        objective, eps2, eta2 = self.profile(best_lam)
        return ContrastMLE(
            sigma_eta2=eta2, sigma_epsilon2=eps2, lam=best_lam,
            neg2_loglike_excluding_constant=objective,
            candidate_count=len(candidates), seconds=perf_counter() - start,
        )

    def lag_covariance_diagnostics(self) -> dict:
        """Simple unchecked moment diagnostics, NOT positive-variance estimates."""
        z = self.z
        mean = float(np.mean(z))
        gammas = [float(np.mean(z[:, :self.m - lag] *
                                     z[:, lag:])) for lag in range(min(self.m, 3))]
        return {"observed_mean_Dy": mean, "raw_autocov_lags_0_to_2": gammas}


def _get_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True,
            stderr=subprocess.DEVNULL, timeout=3,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _csv(path: Path, rows: list[dict]):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def compare_one(scenario: GuerreroScenario, observed: np.ndarray,
                true_tau: np.ndarray, n_scan: int = 121,
                include_brent: bool = True) -> tuple[list[dict], dict]:
    """Compare estimated-vs-known ratio and selected observed-series LOOCV."""
    model = VarianceContrastLikelihood(observed, scenario.order)
    mle = model.fit(n_scan=n_scan)
    obj = PooledLOOCV(observed, order=scenario.order)
    b = bounded_brent(obj) if include_brent else None
    mb = multibracket_brent(obj, n_scan=n_scan) if include_brent else None
    candidates = {
        "guerrero_known_true_ratio": scenario.lambda_guerrero,
        "guerrero_estimated_contrast_MLE": mle.lam,
    }
    if include_brent:
        candidates["bounded_brent_LOOCV"] = b.best.lam
        candidates["multibracket_brent_LOOCV"] = mb.best.lam
    common = {
        "n": scenario.n, "d": scenario.order, "R": observed.shape[0],
        "sigma_eta2_true": scenario.sigma_eta**2,
        "sigma_epsilon2_true": scenario.sigma_epsilon**2,
        "lambda_guerrero_true": scenario.lambda_guerrero,
        "sigma_eta2_estimated": mle.sigma_eta2,
        "sigma_epsilon2_estimated": mle.sigma_epsilon2,
        "lambda_estimated": mle.lam,
        "lambda_estimate_hits_boundary": bool(mle.lam == 0 or np.isinf(mle.lam)),
        "profile_likelihood_candidate_count": mle.candidate_count,
        "variance_estimation_seconds": mle.seconds,
        "variance_logratio_error": float(
            np.log(mle.lam / scenario.lambda_guerrero))
            if np.isfinite(mle.lam) and mle.lam > 0 else float("nan"),
    }
    records = [{
        **common, "method": method, "selected_lambda": lam,
        "selected_s": obj.smoothness(lam),
        "pooled_LOOCV_MSE": obj.score(lam),
        "true_trend_MSE": reconstruction_mse(obj, true_tau, lam),
    } for method, lam in candidates.items()]
    return records, model.lag_covariance_diagnostics()


def aggregate(rows: list[dict]) -> dict:
    groups: dict[tuple[int, int, int], dict[str, dict]] = {}
    for row in rows:
        key = (row["scenario_id"], row["replicate"], row["R"])
        groups.setdefault(key, {})[row["method"]] = row

    def by_group(sub):
        names = list(next(iter(sub.values())).keys())
        means = {
            name: {
                "mean_LOOCV_MSE": float(np.mean([g[name]["pooled_LOOCV_MSE"] for g in sub.values()])),
                "mean_true_trend_MSE": float(np.mean([g[name]["true_trend_MSE"] for g in sub.values()])),
                "mean_S": float(np.mean([g[name]["selected_s"] for g in sub.values()])),
            } for name in names
        }
        reference = "guerrero_known_true_ratio"
        estimated = "guerrero_estimated_contrast_MLE"
        return {
            "paired_pool_count": len(sub),
            "methods": means,
            "estimated_vs_true_log_lambda_abs_median": float(np.nanmedian([
                abs(next(iter(g.values()))["variance_logratio_error"])
                for g in sub.values()])),
            "variance_estimation_boundary_count": sum(
                next(iter(g.values()))["lambda_estimate_hits_boundary"]
                for g in sub.values()
            ),
            "known_ratio_true_MSE_lower_than_estimated_count": sum(
                g[reference]["true_trend_MSE"] < g[estimated]["true_trend_MSE"]
                for g in sub.values()),
            "estimated_ratio_true_MSE_lower_than_LOOCV_multibracket_count": sum(
                g[estimated]["true_trend_MSE"] < g["multibracket_brent_LOOCV"]["true_trend_MSE"]
                for g in sub.values()),
        }

    if not groups:
        raise ValueError("no comparison data")
    expected = {"guerrero_known_true_ratio", "guerrero_estimated_contrast_MLE",
                "bounded_brent_LOOCV", "multibracket_brent_LOOCV"}
    if any(set(g) != expected for g in groups.values()):
        raise ValueError("missing or duplicate method for at least one pool")
    return {
        "overall": by_group(groups),
        "by_R": {str(r): by_group({k: v for k, v in groups.items() if k[2] == r})
                 for r in sorted(set(k[2] for k in groups))},
        "interpretation": [
            "The known-variance ratio is an oracle baseline, not a feasible estimator.",
            "MLE is Gaussian contrast/restricted likelihood fitted only to D y.",
            "R=1 and R=3 at a given seed are nested, not independent draws.",
            "Potential boundary estimates and log-ratio errors are reported.",
            "Observed CV and actual latent trend reconstruction MSE are different criteria.",
        ],
    }


def _plot_example(out: Path, scenario: GuerreroScenario,
                  observed: np.ndarray, true_tau: np.ndarray,
                  rows: list[dict], mle: ContrastMLE):
    obj = PooledLOOCV(observed, order=scenario.order)
    xx = np.exp(np.linspace(-14, 22, 300))
    fig, axs = plt.subplots(2, 1, figsize=(9, 8))
    x = np.arange(obj.n)
    axs[0].plot(x, observed[0], alpha=0.4, label="Observed y")
    axs[0].plot(x, true_tau[0], label="True trend", linewidth=2)
    for row in rows[:3]:
        axs[0].plot(x, obj.trend(row["selected_lambda"])[0],
                    label=row["method"], linestyle="--", linewidth=1)
    axs[0].legend(fontsize=8)
    axs[0].set_ylabel("Series level")
    axs[1].plot([obj.smoothness(float(q)) for q in xx],
                [obj.score(float(q)) for q in xx], label="Pooled observed LOOCV MSE")
    for row in rows:
        axs[1].axvline(row["selected_s"], linestyle="--",
                       label=row["method"], linewidth=1)
    axs[1].set_xlabel("Normalized smoothness S")
    axs[1].set_ylabel("LOOCV MSE")
    axs[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "estimated_variance_example.png", dpi=150)
    plt.close(fig)


def execute(preset: str, out: Path, dry_run: bool = False) -> dict:
    scenarios, n_reps, r_values, _, _, seed_base = preset_design(preset)
    seed_base += 50000000  # disjoint from the previous known-ratio campaign
    n_scan = 51 if preset == "smoke" else (101 if preset == "pilot" else 161)
    manifest = {
        "status": "planned" if dry_run else "executed",
        "protocol": "guerrero_feasible_contrast_MLE_d2_v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "preset": preset, "scenario_count": len(scenarios),
        "independent_seed_repeats_per_cell": n_reps,
        "pool_sizes": list(r_values),
        "pool_count": len(scenarios) * n_reps * len(r_values),
        "method_count": 4,
        "log_lambda_scan_bounds": [-18, 25],
        "profile_grid_size": n_scan, "seed_base": seed_base,
        "stochastic_DGP": "D_2 tau = epsilon, y = tau + eta",
        "variance_likelihood": "zero-mean Gaussian contrasts z=D_2 y",
        "variance_estimator_is_NOT_from_Guerrero_2007": True,
        "true_variances_used_only_for_simulation_and_evaluation": True,
        "nested_R": True,
        "git_commit": _get_sha(),
        "python": platform.python_version(),
        "numpy": np.__version__, "scipy": scipy.__version__,
        "scenarios": [{"n": s.n, "d": s.order, "sigma_eta": s.sigma_eta,
                       "sigma_epsilon": s.sigma_epsilon,
                       "lambda_G": s.lambda_guerrero} for s in scenarios],
    }
    if dry_run:
        print(json.dumps(manifest, indent=2))
        return manifest
    out.mkdir(parents=True, exist_ok=True)
    rows, diagnostics = [], []
    plotted = False
    for case_id, scenario in enumerate(scenarios):
        for rep in range(n_reps):
            seed = seed_base + case_id * 10000 + rep
            for r in r_values:
                y, tau = draw_observed_pool(scenario, r, seed)
                group, diag = compare_one(scenario, y, tau, n_scan=n_scan)
                for record in group:
                    rows.append({"scenario_id": case_id, "replicate": rep,
                                 "seed": seed, **record})
                diagnostics.append({"scenario_id": case_id, "replicate": rep,
                                    "seed": seed, "R": r, **diag})
                if not plotted:
                    likelihood = VarianceContrastLikelihood(y, scenario.order)
                    _plot_example(out, scenario, y, tau, group,
                                  likelihood.fit(n_scan=n_scan))
                    plotted = True
    _csv(out / "variance_estimation_method_comparison.csv", rows)
    _csv(out / "contrast_autocovariance_diagnostics.csv", [{
        "scenario_id": d["scenario_id"], "replicate": d["replicate"],
        "seed": d["seed"], "R": d["R"], "mean_Dy": d["observed_mean_Dy"],
        "lag0": d["raw_autocov_lags_0_to_2"][0],
        "lag1": d["raw_autocov_lags_0_to_2"][1],
        "lag2": d["raw_autocov_lags_0_to_2"][2],
    } for d in diagnostics])
    summary = aggregate(rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n",
                                       encoding="utf-8")
    manifest["rows_written"] = len(rows)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n",
                                        encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preset", choices=("smoke", "pilot", "confirmatory"),
                        default="smoke")
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    out = args.out_dir or (Path("results/pooled_loocv_smoothness/guerrero") /
                           "estimated_variances" / args.preset)
    execute(args.preset, out, args.dry_run)


if __name__ == "__main__":
    main()
