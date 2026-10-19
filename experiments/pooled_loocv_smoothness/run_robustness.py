"""Misspecified-noise robustness study for Guerrero-model trend smoothing.

Comparison of observed-data Gaussian difference-likelihood estimation,
pooled LOOCV (single-start and multibracket), nonnegative moments, and
a *nominal* true-marginal-variance ratio. Only in iid Gaussian regime
is the ratio the model-informed Guerrero variance-ratio benchmark.

This is retrospective latent trend reconstruction, NOT forecasting.
Heavy-tailed shocks, AR(1) observation errors, and time-changing
observation variance violate some assumptions of the fitted likelihood.
All methods use identical observed pools; true latent tau is used only
in evaluating reconstruction errors. R=1 is nested in R=3.

Heavy-tailed Student t uses df=5 with finite variance and variance-one
standardization. AR(1) phi=0.65 is initialized at stationarity.
The heteroskedastic design sets first-half marginal noise variance
to 0.25 * sigma_eta^2 and last-half to 1.75 * sigma_eta^2, so
average marginal observation variance is sigma_eta^2.
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

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy

from .guerrero_ratio import GuerreroScenario, integrated_trend, reconstruction_mse
from .objective import PooledLOOCV
from .search import bounded_brent, multibracket_brent
from .variance_estimation import estimate_gaussian_differences, estimate_moments


REGIMES = (
    "gaussian_iid",
    "student_t_observation",
    "student_t_innovation",
    "ar1_observation",
    "heteroskedastic_observation",
)
METHODS = (
    "nominal_known_ratio",
    "estimated_gaussian_difference_ml",
    "pooled_loocv_bounded_brent",
    "pooled_loocv_multibracket_brent",
    "estimated_moments_nnls",
)
T_DF = 5
AR1_PHI = 0.65
# This seed offset is disjoint from prior variance-estimation campaign.
SEED_BASE = 30610000


@dataclass(frozen=True)
class RobustScenario:
    regime: str
    n: int
    sigma_eta: float
    sigma_epsilon: float = 0.3
    order: int = 2

    def __post_init__(self):
        if self.regime not in REGIMES:
            raise ValueError("Unknown noise regime")
        if self.order != 2 or self.n < 12 or self.n % 2:
            raise ValueError("This protocol uses d=2 and even N >= 12")
        if self.sigma_eta <= 0 or self.sigma_epsilon <= 0:
            raise ValueError("Both marginal standard deviations must be positive")

    @property
    def nominal_lambda(self) -> float:
        return (self.sigma_eta / self.sigma_epsilon) ** 2


def _unit_t(rng: np.random.Generator, n: int) -> np.ndarray:
    """Student-t(df=5) shocks rescaled to population variance 1."""
    return rng.standard_t(T_DF, size=n) * np.sqrt((T_DF - 2) / T_DF)


def draw_one(scenario: RobustScenario,
             rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return observed y, latent tau, and observation noise eta."""
    n, d = scenario.n, scenario.order
    if scenario.regime == "student_t_innovation":
        eps = scenario.sigma_epsilon * _unit_t(rng, n - d)
    else:
        eps = scenario.sigma_epsilon * rng.standard_normal(n - d)
    tau = integrated_trend(eps, order=d, intercept=0.0, slope=0.02)

    if scenario.regime == "student_t_observation":
        eta = scenario.sigma_eta * _unit_t(rng, n)
    elif scenario.regime == "ar1_observation":
        # Stationary variance = sigma_eta^2 at every t.
        u = rng.standard_normal(n)
        eta = np.empty(n, dtype=float)
        eta[0] = scenario.sigma_eta * u[0]
        innovation_sd = scenario.sigma_eta * np.sqrt(1.0 - AR1_PHI**2)
        for t in range(1, n):
            eta[t] = AR1_PHI * eta[t - 1] + innovation_sd * u[t]
    elif scenario.regime == "heteroskedastic_observation":
        scales = np.concatenate((
            np.full(n // 2, np.sqrt(0.25)),
            np.full(n - n // 2, np.sqrt(1.75)),
        ))
        eta = scenario.sigma_eta * scales * rng.standard_normal(n)
    else:
        eta = scenario.sigma_eta * rng.standard_normal(n)
    return tau + eta, tau, eta


def draw_pool(scenario: RobustScenario, r: int,
              seed: int) -> tuple[np.ndarray, np.ndarray]:
    """One seed deterministically generates independent series within pool.

    R=1 and R=3 at the same seed share exactly the first series.
    """
    if r < 1:
        raise ValueError("pool must have at least one observed series")
    rng = np.random.default_rng(seed)
    ys, trends = [], []
    for _ in range(r):
        y, tau, _ = draw_one(scenario, rng)
        ys.append(y)
        trends.append(tau)
    return np.asarray(ys), np.asarray(trends)


def design(preset: str):
    if preset == "smoke":
        cells = [RobustScenario(regime, 24, 0.5) for regime in REGIMES]
        return cells, 1, (1, 3), 31
    if preset in ("pilot", "confirmatory"):
        cells = [RobustScenario(regime, n, eta)
                 for regime in REGIMES for n in (50, 200)
                 for eta in (0.5, 2.0)]
        repetitions = 5 if preset == "pilot" else 100
        return cells, repetitions, (1, 3), 81
    raise ValueError("Unknown preset")


def _git_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, timeout=3,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _write_csv(path: Path, rows: list[dict]):
    if not rows:
        raise ValueError("No rows to write")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def compare_pool(scenario: RobustScenario, y: np.ndarray,
                 truth: np.ndarray, n_scan: int = 81) -> list[dict]:
    """Fit all five selection procedures on exactly the same observed y."""
    obj = PooledLOOCV(y, order=scenario.order)
    ml = estimate_gaussian_differences(y, obj.d, scan_points=n_scan)
    mom = estimate_moments(y, obj.d)
    single = bounded_brent(obj)
    multi = multibracket_brent(obj, n_scan=n_scan)
    options = {
        METHODS[0]: (scenario.nominal_lambda, None),
        METHODS[1]: (ml.lambda_ratio, ml),
        METHODS[2]: (single.best.lam, None),
        METHODS[3]: (multi.best.lam, None),
        METHODS[4]: (mom.lambda_ratio, mom),
    }
    return [{
        "regime": scenario.regime, "N": scenario.n, "d": scenario.order,
        "R": obj.r, "sigma_eta_nominal": scenario.sigma_eta,
        "sigma_epsilon_nominal": scenario.sigma_epsilon,
        "nominal_variance_ratio_lambda": scenario.nominal_lambda,
        "nominal_ratio_is_valid_model_benchmark":
            scenario.regime == "gaussian_iid",
        "method": method,
        "selected_lambda": lam,
        "selected_S": obj.smoothness(lam),
        "observed_loocv_mse": obj.score(lam),
        "true_trend_mse": reconstruction_mse(obj, truth, lam),
        "estimated_sigma_eta2": (
            estimate.sigma_eta2 if estimate is not None else float("nan")),
        "estimated_sigma_epsilon2": (
            estimate.sigma_epsilon2 if estimate is not None else float("nan")),
        "zero_innovation_variance_estimated": bool(
            estimate is not None and estimate.sigma_epsilon2 == 0.0),
        "stationary_candidates_multibracket": sum(
            c.kind == "stationary" for c in multi.candidates),
    } for method, (lam, estimate) in options.items()]


def summarize(rows: list[dict]) -> dict:
    pools: dict[tuple[str, int, float, int, int], dict[str, dict]] = {}
    for x in rows:
        key = (x["regime"], x["N"], x["sigma_eta_nominal"],
               x["replicate"], x["R"])
        slot = pools.setdefault(key, {})
        if x["method"] in slot:
            raise ValueError("Duplicate paired method row")
        slot[x["method"]] = x
    if not pools or any(set(p) != set(METHODS) for p in pools.values()):
        raise ValueError("Incomplete paired-method pool")

    def group_results(sub: list[dict[str, dict]]) -> dict:
        return {
            "pool_count": len(sub),
            "methods": {
                m: {
                    "mean_true_trend_mse": float(np.mean([
                        x[m]["true_trend_mse"] for x in sub])),
                    "median_true_trend_mse": float(np.median([
                        x[m]["true_trend_mse"] for x in sub])),
                    "mean_observed_loocv_mse": float(np.mean([
                        x[m]["observed_loocv_mse"] for x in sub])),
                    "infinite_lambda_count": sum(
                        bool(np.isinf(x[m]["selected_lambda"])) for x in sub),
                } for m in METHODS
            },
            "ml_true_mse_beats_single_cv": sum(
                x[METHODS[1]]["true_trend_mse"] <
                x[METHODS[2]]["true_trend_mse"] for x in sub),
            "single_cv_misses_multibracket_more_than_1e-7": sum(
                x[METHODS[2]]["observed_loocv_mse"] >
                x[METHODS[3]]["observed_loocv_mse"] + 1e-7
                for x in sub),
            "mean_paired_true_mse_single_cv_minus_ml": float(np.mean([
                x[METHODS[2]]["true_trend_mse"] -
                x[METHODS[1]]["true_trend_mse"] for x in sub])),
        }

    primary = [p for key, p in pools.items() if key[-1] == 3]
    by_regime = {}
    for regime in REGIMES:
        regime_groups = [p for p in primary
                         if p[METHODS[0]]["regime"] == regime]
        if regime_groups:
            by_regime[regime] = group_results(regime_groups)
    by_cell = []
    for regime, n, eta in sorted(set((k[0], k[1], k[2]) for k in pools)):
        sub = [p for key, p in pools.items()
               if key[0] == regime and key[1] == n
               and key[2] == eta and key[-1] == 3]
        if sub:
            by_cell.append({
                "regime": regime, "N": n, "sigma_eta": eta,
                "sigma_epsilon": sub[0][METHODS[0]]["sigma_epsilon_nominal"],
                "nominal_lambda": sub[0][METHODS[0]][
                    "nominal_variance_ratio_lambda"],
                **group_results(sub),
            })
    return {
        "protocol": "misspecified_guerrero_noise_robustness_v1",
        "status": "descriptive_simulation_not_confirmatory",
        "total_pools": len(pools),
        "nested_R_warning": "R=1 and R=3 at same seed share the first series",
        "primary_R3": group_results(primary),
        "by_regime_R3": by_regime,
        "by_cell_R3": by_cell,
        "interpretation_warnings": [
            "The nominal variance ratio is not the correct oracle under AR1 or time-varying noise.",
            "For Student-t shocks finite second moments exist (df=5) but Gaussian likelihood is misspecified.",
            "Ordinary LOOCV also assumes a meaningful held-out conditional prediction target; autocorrelated observations can invalidate its interpretation.",
            "True tau appears only in evaluation, never in any fitted selector.",
            "Small exploratory pilot seeds cannot support publication-ready superiority claims.",
            "Multibracket derivative scans are finite, without global completeness guarantees.",
        ],
    }


def _figure(summary: dict, out: Path):
    by = summary["by_regime_R3"]
    regimes = [x for x in REGIMES if x in by]
    fig, ax = plt.subplots(figsize=(10, 5))
    xx = np.arange(len(regimes))
    for method, label in ((METHODS[1], "Fitted Gaussian difference ML"),
                          (METHODS[2], "Pooled LOOCV (Brent)"),
                          (METHODS[0], "Nominal variance ratio")):
        ax.plot(xx, [by[x]["methods"][method]["mean_true_trend_mse"]
                     for x in regimes], marker="o", label=label)
    ax.set_xticks(xx, [r.replace("_", " ") for r in regimes],
                  rotation=28, ha="right")
    ax.set_ylabel("Mean realized true trend MSE, R=3")
    ax.set_xlabel("Simulated observation/innovation noise mechanism")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "robustness_true_trend_mse_R3.png", dpi=160)
    plt.close(fig)


def execute(preset: str, out: Path, dry_run: bool = False) -> dict:
    scenarios, repeats, r_values, scan = design(preset)
    base = SEED_BASE if preset != "confirmatory" else SEED_BASE + 1000000
    manifest = {
        "protocol": "misspecified_guerrero_noise_robustness_v1",
        "status": "planned" if dry_run else "executed",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "preset": preset, "seed_base": base,
        "seed_formula": "seed_base + scenario_id*10000 + replicate",
        "random_generator": "numpy.random.default_rng",
        "regimes": list(REGIMES),
        "scenario_count": len(scenarios),
        "scenarios": [
            {"regime": s.regime, "n": s.n, "d": s.order,
             "sigma_eta": s.sigma_eta, "sigma_epsilon": s.sigma_epsilon,
             "nominal_lambda": s.nominal_lambda}
            for s in scenarios
        ],
        "seed_repetitions_per_scenario": repeats,
        "pool_sizes": list(r_values),
        "nested_pool_first_series_reused": True,
        "expected_pools": len(scenarios) * repeats * len(r_values),
        "expected_method_rows": len(scenarios) * repeats * len(r_values) * len(METHODS),
        "methods": list(METHODS),
        "difference_order": 2, "student_t_df": T_DF,
        "t_variance_normalization": "(df-2)/df",
        "ar1_phi": AR1_PHI,
        "heteroskedastic_first_half_variance_factor": 0.25,
        "heteroskedastic_second_half_variance_factor": 1.75,
        "reference_variance_ratio": "sigma_eta_nominal**2/sigma_epsilon_nominal**2",
        "reference_ratio_warning":
            "Model-informed Guerrero ratio only for iid Gaussian; under other regimes a NOMINAL reference, not an oracle.",
        "cv_log_lambda_bounds": [-20, 35],
        "ml_profile_scan_points": scan,
        "multibracket_derivative_scan_points": scan,
        "git_sha": _git_sha(),
        "python": platform.python_version(),
        "numpy": np.__version__, "scipy": scipy.__version__,
        "truth_used_for_tuning": False,
    }
    if dry_run:
        print(json.dumps(manifest, indent=2))
        return manifest
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for scenario_id, sc in enumerate(scenarios):
        for rep in range(repeats):
            seed = base + scenario_id * 10000 + rep
            for r in r_values:
                y, tau = draw_pool(sc, r=r, seed=seed)
                for record in compare_pool(sc, y, tau, n_scan=scan):
                    rows.append({
                        "scenario_id": scenario_id,
                        "replicate": rep, "seed": seed, **record,
                    })
    _write_csv(out / "method_comparison.csv", rows)
    summary = summarize(rows)
    (out / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    _figure(summary, out)
    manifest["actual_rows"] = len(rows)
    (out / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": manifest["status"],
        "scenarios": len(scenarios),
        "pools": summary["total_pools"],
        "rows": len(rows),
        "primary_R3": summary["primary_R3"],
        "outputs": str(out),
    }, indent=2))
    return summary


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--preset", choices=("smoke", "pilot", "confirmatory"),
                   default="smoke")
    p.add_argument("--out-dir", type=Path, default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    out = args.out_dir or (Path("results/pooled_loocv_smoothness/guerrero") /
                            "robustness" / args.preset)
    execute(args.preset, out, args.dry_run)


if __name__ == "__main__":
    main()
