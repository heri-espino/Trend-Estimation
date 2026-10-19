"""Small, process-diverse illustrations for retrospective pooled trend reconstruction.

Purpose: compare existing feasible selectors on DIFFERENT generating
mechanisms, rather than increase the seed count of Study J/K.1.
Each case is one illustrative draw, never inferential proof of dominance.

Distinguish: latent trend changes, observation-error changes, and pooling
assumption failures. Cases use the same underlying innovations wherever
possible. R=1 is the first series of R=3. No oracle true-trend information
enters feasible lambda/mu selection; truth is only an evaluation target.

Run manually; no automatic heavy campaign and no changes to older data.
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

import numpy as np
import scipy

from .cortes_optimality_criteria import PenalizedCriteria, choose
from .mean_difference_methods import (
    estimate_contrast_gaussian_mean,
    fitted_affine_trend,
    particular_polynomial,
)
from .objective import PooledLOOCV
from .run_nonzero_difference_mean import _integrate_order
from .variance_estimation import estimate_gaussian_differences

DEFAULT_SEED = 20261019
ORDER = 2
SIGMA_EPSILON = 0.12
SIGMA_ETA = 0.80
MU = 0.04
METHODS = (
    "cv_zero", "gcv_zero", "aicc_zero",
    "cv_joint", "gcv_joint", "aicc_joint",
    "gls_mu_ml", "plugin_mu_ml", "zero_mu_ml",
    "controlled_s0.5_joint", "controlled_s0.8_joint",
)
PLOT_METHODS = (
    "cv_joint", "gcv_joint", "aicc_joint", "gls_mu_ml",
    "controlled_s0.8_joint",
)


@dataclass(frozen=True)
class Example:
    name: str
    mechanism: str
    y: np.ndarray  # (3, N)
    truth: np.ndarray  # simulated realized latent signal, (3, N)
    assumption: str


def _ar1(normal: np.ndarray, phi: float) -> np.ndarray:
    """Gaussian stationary AR(1) with unit marginal variance."""
    if not (-1.0 < phi < 1.0):
        raise ValueError("stationary AR(1) requires |phi| < 1")
    out = np.array(normal, dtype=float, copy=True)
    for i in range(1, len(out)):
        out[i] = phi * out[i - 1] + np.sqrt(1.0 - phi**2) * normal[i]
    return out


def make_examples(seed: int = DEFAULT_SEED, n: int = 80) -> dict[str, Example]:
    """Generate nine distinct cases from common normal innovations.

    Only the baseline satisfies independent homoskedastic Gaussian
    observation errors and a single constant mean in D_2 tau.
    All other cases change exactly one documented mechanism relative
    to the baseline (except the named pooled-heterogeneity case).
    """
    if n < 32:
        raise ValueError("n must be at least 32 for interpretable breaks")
    rng = np.random.default_rng(seed)
    eps = SIGMA_EPSILON * rng.standard_normal((3, n - ORDER))
    noise = rng.standard_normal((3, n))
    common = rng.standard_normal(n)
    time = np.arange(n, dtype=float)
    poly = particular_polynomial(n, ORDER)
    base_tau = np.stack([
        _integrate_order(eps[r], ORDER) + MU * poly for r in range(3)
    ])
    base_eta = SIGMA_ETA * noise

    cases: dict[str, Example] = {}

    def add(name: str, mechanism: str, tau: np.ndarray,
            eta: np.ndarray, assumption: str) -> None:
        if tau.shape != (3, n) or eta.shape != (3, n):
            raise ValueError("every case must contain 3 x N arrays")
        cases[name] = Example(
            name, mechanism, np.asarray(tau + eta, dtype=float).copy(),
            np.asarray(tau, dtype=float).copy(), assumption
        )

    add("gaussian_reference", "Correct d=2 Gaussian difference trend",
        base_tau, base_eta, "reference: iid Gaussian eta, iid Gaussian D2 tau")
    add("smooth_cycle", "Sinusoidal component in the latent trend",
        base_tau + 3.0 * np.sin(2 * np.pi * time / 24)[None, :],
        base_eta, "nonconstant mean structure in D2 tau")
    add("slope_break", "Single kink in the latent trend",
        base_tau + 0.75 * np.maximum(time - n // 2, 0)[None, :],
        base_eta, "non-Gaussian deterministic impulse in D2 tau")
    add("level_jump", "Sudden genuine trend level shift",
        base_tau + 7.0 * (time >= n // 2)[None, :],
        base_eta, "trend discontinuity incompatible with smooth difference prior")
    contaminated = base_eta.copy()
    for r, (location, sign) in enumerate(
        ((n // 2, 1), (n // 2 + 5, -1), (n // 2 - 7, 1))
    ):
        contaminated[r, location] += sign * 8.0
    add("observation_outliers", "Isolated measurement outliers, not trend jumps",
        base_tau, contaminated, "non-Gaussian contaminated measurement error")
    dependent = SIGMA_ETA * np.stack([_ar1(noise[r], 0.85) for r in range(3)])
    add("ar1_observation", "Serially correlated Gaussian observation errors",
        base_tau, dependent, "nondiagonal observation covariance (phi=0.85)")
    heteroskedastic = base_eta * np.where(time < n // 2, 0.45, 1.35)[None, :]
    add("variance_regime", "Observation variance changes halfway through",
        base_tau, heteroskedastic, "heteroskedastic measurement errors")
    pool_noise = np.array([0.25, 0.80, 1.50])[:, None] * noise
    add("heterogeneous_pool", "Three series with very different noise scales",
        base_tau, pool_noise, "no single observation variance/optimal lambda across R")
    correlated = SIGMA_ETA * (
        np.sqrt(0.70) * common[None, :] +
        np.sqrt(0.30) * noise
    )
    add("shared_observation_shock", "Common cross-series measurement factor",
        base_tau, correlated, "cross-series noise correlation of 0.70")
    return cases


def evaluate_example(case: Example, r: int = 3, scan_points: int = 31):
    """Fit eleven *feasible* policies on exactly the same observed pool."""
    if r not in (1, 3):
        raise ValueError("only nested R=1 and R=3 are predeclared")
    if scan_points < 5:
        raise ValueError("scan_points >= 5 required")
    y, truth = case.y[:r], case.truth[:r]
    base = PooledLOOCV(y, order=ORDER)
    rows: list[dict] = []
    fitted_curves: dict[str, np.ndarray] = {}

    def register(method: str, lam: float, mu: float,
                 fitted: np.ndarray, criterion: str, score,
                 mean_mode: str, edf=None, calls=None):
        fit = np.asarray(fitted, dtype=float)
        if fit.shape != truth.shape or not np.isfinite(fit).all():
            raise ArithmeticError("invalid reconstructed trend")
        rows.append({
            "case": case.name,
            "mechanism": case.mechanism,
            "assumption": case.assumption,
            "R": r, "N": y.shape[1], "d": ORDER,
            "method": method, "criterion": criterion,
            "mean_mode": mean_mode,
            "selected_lambda": float(lam),
            "selected_s_nominal": float(base.smoothness(float(lam))),
            "fitted_mu": float(mu),
            "edf_total": None if edf is None else float(edf),
            "criterion_score_NOT_COMPARABLE_ACROSS_TYPES": (
                None if score is None else float(score)
            ),
            "criterion_calls": calls,
            "latent_trend_mse_EX_POST": float(np.mean((fit - truth) ** 2)),
            "latent_trend_mae_EX_POST": float(np.mean(np.abs(fit - truth))),
        })
        fitted_curves[method] = fit

    for mode in ("zero", "joint"):
        obj = PenalizedCriteria(y, order=ORDER, mean_mode=mode)
        for criterion in ("cv", "gcv", "aicc"):
            sol = choose(obj, criterion, solver="multibracket",
                         scan_points=scan_points)
            register(f"{criterion}_{mode}", sol.lam, sol.mu_fit,
                     obj.trend(sol.lam), criterion, sol.score,
                     mode, sol.edf_total, sol.evaluated)
        if mode == "joint":
            for smooth in (0.5, 0.8):
                sol = obj.choose_fixed_smoothness(smooth)
                register(f"controlled_s{smooth:g}_joint", sol.lam,
                         sol.mu_fit, obj.trend(sol.lam),
                         "predeclared_smoothness", None, mode,
                         sol.edf_total, sol.evaluated)

    mu_fit = estimate_contrast_gaussian_mean(
        y, base.d, fixed_mu=None, scan_points=41)
    register("gls_mu_ml", mu_fit.variance.lambda_ratio, mu_fit.mu,
             fitted_affine_trend(base, mu_fit.variance.lambda_ratio,
                                 mu_fit.mu),
             "Gaussian contrast ML (quasi-ML if misspecified)", None,
             "GLS estimated")

    pooled_plugin_mu = float(np.mean(y @ base.d.T))
    pooled_plugin = estimate_contrast_gaussian_mean(
        y, base.d, fixed_mu=pooled_plugin_mu, scan_points=41)
    register("plugin_mu_ml", pooled_plugin.variance.lambda_ratio,
             pooled_plugin_mu,
             fitted_affine_trend(base, pooled_plugin.variance.lambda_ratio,
                                 pooled_plugin_mu),
             "observed-difference plug-in plus Gaussian contrast ML", None,
             "pooled plug-in")

    zero_var = estimate_gaussian_differences(
        y, base.d, scan_points=41)
    register("zero_mu_ml", zero_var.lambda_ratio, 0.0,
             fitted_affine_trend(base, zero_var.lambda_ratio, 0.0),
             "Gaussian contrast ML with mu fixed at zero", None, "zero")

    if {row["method"] for row in rows} != set(METHODS):
        raise AssertionError("missing or duplicate comparison methods")
    return rows, fitted_curves


def plot_example(case: Example, fitted: dict[str, np.ndarray],
                 output: Path, r: int) -> None:
    """Illustrative curves use fixed named selectors, not ex-post winner."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    t = np.arange(case.y.shape[1])
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.scatter(t, case.y[0], s=9, alpha=0.32, label="Observed y (series 1)")
    ax.plot(t, case.truth[0], linewidth=2.5, label="True simulated tau")
    for method in PLOT_METHODS:
        ax.plot(t, fitted[method][0], linewidth=1.3, alpha=0.8,
                label=method)
    ax.set(title=f"{case.name} — nested R={r}; one illustrative realization",
           xlabel="Observation index", ylabel="Simulated value")
    ax.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(output, dpi=130)
    plt.close(fig)


def _commit_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL, text=True
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def run(out_dir: Path, *, selected: tuple[str, ...] | None = None,
        seed: int = DEFAULT_SEED, n: int = 80,
        scan_points: int = 31, figures: bool = True) -> dict:
    cases = make_examples(seed, n)
    if selected is None:
        selected = tuple(cases)
    unknown = set(selected) - set(cases)
    if unknown or len(selected) != len(set(selected)) or not selected:
        raise ValueError(f"unknown/duplicate/empty selection: {sorted(unknown)}")
    if out_dir.exists() and any(out_dir.iterdir()):
        raise FileExistsError(f"refusing to overwrite nonempty {out_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)
    result_rows = []
    for name in selected:
        case = cases[name]
        for r in (1, 3):
            rows, fits = evaluate_example(case, r=r,
                                          scan_points=scan_points)
            result_rows.extend(rows)
            if figures:
                plot_example(case, fits, out_dir / f"{name}_R{r}.png", r)
    with (out_dir / "method_comparison.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=list(result_rows[0]))
        writer.writeheader()
        writer.writerows(result_rows)

    comparisons = []
    for name in selected:
        for r in (1, 3):
            subset = [row for row in result_rows
                      if row["case"] == name and row["R"] == r]
            winner = min(subset, key=lambda x: x["latent_trend_mse_EX_POST"])
            comparisons.append({
                "case": name, "R": r,
                "lowest_MSE_in_THIS_ONE_realization_NOT_DEPLOYABLE_SELECTOR": winner["method"],
                "lowest_MSE_EX_POST": winner["latent_trend_mse_EX_POST"],
                "gls_mu_ml_mse": next(x["latent_trend_mse_EX_POST"]
                                      for x in subset
                                      if x["method"] == "gls_mu_ml"),
                "cv_joint_mse": next(x["latent_trend_mse_EX_POST"]
                                     for x in subset
                                     if x["method"] == "cv_joint"),
                "aicc_joint_mse": next(x["latent_trend_mse_EX_POST"]
                                       for x in subset
                                       if x["method"] == "aicc_joint"),
            })
    with (out_dir / "illustrative_winners.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=list(comparisons[0]))
        writer.writeheader()
        writer.writerows(comparisons)
    manifest = {
        "status": "ILLUSTRATIONS_ONLY_NO_MONTE_CARLO_INFERENCE",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_git_sha": _commit_sha(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "seed": seed, "n": n, "d": ORDER, "series_generated": 3,
        "nested_pool_sizes": [1, 3], "sigma_epsilon_reference": SIGMA_EPSILON,
        "sigma_eta_reference": SIGMA_ETA, "mu_reference": MU,
        "same_base_innovations_across_cases": True,
        "methods": list(METHODS), "cases": list(selected),
        "score_grid_points": scan_points, "solver": "score_multibracket",
        "number_of_rows": len(result_rows),
        "warnings": [
            "One fixed realization per mechanism: no winner-frequency or significance claim.",
            "Latent true tau is ONLY available for retrospective ex-post metrics.",
            "All statistical criteria have different score scales; never compare raw CV, GCV, AICc scores directly.",
            "All changes to noise dynamics, mean dynamics and pooling affect fitted-model validity.",
            "Known sigma parameters apply only to Gaussian reference and are NOT treated as true oracles elsewhere.",
            "R1 is nested in R3 and shares the first observation series.",
            "Actual financial data contain no observed true latent tau.",
        ],
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path,
        default=Path("results/pooled_loocv_smoothness/process_examples/v1"))
    parser.add_argument("--cases", default="all",
                        help="comma-separated scenario names or 'all'")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--n", type=int, default=80)
    parser.add_argument("--scan-points", type=int, default=31)
    parser.add_argument("--no-figures", action="store_true")
    args = parser.parse_args()
    all_names = tuple(make_examples(args.seed, args.n))
    chosen = all_names if args.cases == "all" else tuple(
        s.strip() for s in args.cases.split(",")
    )
    manifest = run(args.out_dir, selected=chosen,
                   seed=args.seed, n=args.n,
                   scan_points=args.scan_points,
                   figures=not args.no_figures)
    print(json.dumps({
        "status": manifest["status"], "cases": manifest["cases"],
        "method_rows": manifest["number_of_rows"],
        "output": str(args.out_dir),
    }, indent=2))


if __name__ == "__main__":
    main()
