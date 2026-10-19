"""Independent tail-shape, skewness and volatility-clustering stress experiment.

This is NOT a financial-return backtest. Data are artificial
y = tau + eta, Delta^2 tau = epsilon, with precisely known latent tau.
All feasible methods see only y, never tau, when selecting lambda.

Cauchy has undefined mean AND variance. Its scale gamma is not SD;
there is no Guerrero variance-ratio target or population MSE. The
empirical squared errors produced for one finite sample are recorded
for diagnostic completeness ONLY. Compare across repetitions using
quantiles and robust absolute-error summaries, not expected MSE.
"""

from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
from math import comb
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from .objective import PooledLOOCV
from .search import bounded_brent, multibracket_brent
from .variance_estimation import estimate_gaussian_differences


REGIMES = (
    "gaussian_iid",
    "student_t3_observation",
    "student_t3_innovation",
    "centered_gamma_right",
    "centered_gamma_left",
    "gaussian_jump_mixture",
    "garch_t5_observation",
    "cauchy_observation",
    "skew_normal_m6",
    "skew_normal_m3",
    "skew_normal_0",
    "skew_normal_p3",
    "skew_normal_p6",
)
METHODS = (
    "estimated_gaussian_difference_ml",
    "pooled_loocv_bounded_brent",
    "pooled_loocv_multibracket_brent",
)
SKEW_NORMAL_ALPHAS = {
    "skew_normal_m6": -6.0,
    "skew_normal_m3": -3.0,
    "skew_normal_0": 0.0,
    "skew_normal_p3": 3.0,
    "skew_normal_p6": 6.0,
}
DIFFERENCE_ORDERS = (1, 2, 3)
T3_DF = 3
T5_DF = 5
GAMMA_SHAPE = 0.5
JUMP_PROBABILITY = 0.02
JUMP_SD_MULTIPLIER = 8.0
GARCH_ALPHA = 0.10
GARCH_BETA = 0.85
SEED_BASE = 47800000  # entirely separate from previous research pilots


@dataclass(frozen=True)
class TailScenario:
    regime: str
    n: int
    noise_scale: float
    sigma_epsilon: float = 0.3
    order: int = 2

    def __post_init__(self):
        if self.regime not in REGIMES:
            raise ValueError("unknown tail-noise regime")
        if self.n < 12 or self.n % 2 or self.order not in DIFFERENCE_ORDERS:
            raise ValueError("require even N >= 12 and d in {1,2,3}")
        if not np.isfinite(self.noise_scale) or self.noise_scale <= 0:
            raise ValueError("noise scale must be positive and finite")
        if not np.isfinite(self.sigma_epsilon) or self.sigma_epsilon <= 0:
            raise ValueError("trend innovation SD must be positive")

    @property
    def observation_variance_exists(self):
        return self.regime != "cauchy_observation"


def _standard_t(rng: np.random.Generator, df: int, n: int):
    """Student-t shocks standardized to have population SD exactly 1."""
    return rng.standard_t(df, size=n) * np.sqrt((df - 2.0) / df)


def integrate_differences(innovations: np.ndarray, order: int) -> np.ndarray:
    """Integrate D_d tau = eps exactly, with deterministic polynomial start.

    d=1 has a fixed initial level, d=2 a fixed level and slope, and
    d=3 three initial polynomial values (zero initial curvature).
    The method uses integer binomial coefficients, not numerical
    inverse differencing. Verify D_d @ tau == eps in tests.
    """
    if order not in DIFFERENCE_ORDERS:
        raise ValueError("unsupported difference order")
    eps = np.asarray(innovations, dtype=float)
    if eps.ndim != 1 or not np.isfinite(eps).all():
        raise ValueError("innovations must be a finite vector")
    n = eps.size + order
    tau = np.empty(n, dtype=float)
    tau[:order] = 0.02 * np.arange(order)
    earlier = np.array([
        (-1) ** (order - k) * comb(order, k) for k in range(order)
    ], dtype=float)
    for j, innovation in enumerate(eps):
        tau[j + order] = innovation - float(
            earlier @ tau[j:j + order])
    return tau


def centered_skew_normal(rng: np.random.Generator, n: int,
                         alpha: float) -> np.ndarray:
    """Azzalini skew-normal, population-centered and variance-standardized.

    Z = delta |U| + sqrt(1-delta^2) V, delta=alpha/sqrt(1+alpha^2).
    Subtract E[Z] and divide by sqrt(Var(Z)) analytically; never
    center/scale each realized sample using its own sample moments.
    For alpha=0, Z is standard Gaussian in distribution.
    """
    delta = alpha / np.sqrt(1.0 + alpha**2)
    z = (delta * np.abs(rng.standard_normal(n)) +
         np.sqrt(1.0 - delta**2) * rng.standard_normal(n))
    mu = delta * np.sqrt(2.0 / np.pi)
    variance = 1.0 - 2.0 * delta**2 / np.pi
    return (z - mu) / np.sqrt(variance)


def draw_one(sc: TailScenario, rng: np.random.Generator):
    """Independent trend/observation-noise mechanisms, returns y,tau,eta."""
    n = sc.n
    if sc.regime == "student_t3_innovation":
        eps = sc.sigma_epsilon * _standard_t(rng, T3_DF, n - sc.order)
    else:
        eps = sc.sigma_epsilon * rng.standard_normal(n - sc.order)
    tau = integrate_differences(eps, sc.order)

    if sc.regime == "student_t3_observation":
        eta = sc.noise_scale * _standard_t(rng, T3_DF, n)
    elif sc.regime in ("centered_gamma_right", "centered_gamma_left"):
        u = (rng.gamma(shape=GAMMA_SHAPE, scale=1., size=n) -
             GAMMA_SHAPE) / np.sqrt(GAMMA_SHAPE)
        eta = sc.noise_scale * (u if sc.regime.endswith("right") else -u)
    elif sc.regime == "gaussian_jump_mixture":
        jumps = rng.uniform(size=n) < JUMP_PROBABILITY
        multiplier = np.where(jumps, JUMP_SD_MULTIPLIER, 1.)
        second_moment = (1. - JUMP_PROBABILITY) + (
            JUMP_PROBABILITY * JUMP_SD_MULTIPLIER**2)
        eta = (sc.noise_scale * multiplier * rng.standard_normal(n) /
               np.sqrt(second_moment))
    elif sc.regime == "garch_t5_observation":
        # h_0=1, not a random draw from the stationary volatility distribution.
        # omega=1-alpha-beta>0 ensures unconditional target Var(eta)=scale^2.
        standardized = _standard_t(rng, T5_DF, n)
        h = np.ones(n, dtype=float)
        eta = np.empty(n, dtype=float)
        omega = 1. - GARCH_ALPHA - GARCH_BETA
        for t in range(n):
            if t:
                h[t] = (omega + GARCH_ALPHA *
                        (eta[t-1] / sc.noise_scale)**2 +
                        GARCH_BETA * h[t-1])
            eta[t] = sc.noise_scale * np.sqrt(h[t]) * standardized[t]
    elif sc.regime in SKEW_NORMAL_ALPHAS:
        eta = sc.noise_scale * centered_skew_normal(
            rng, n, SKEW_NORMAL_ALPHAS[sc.regime])
    elif sc.regime == "cauchy_observation":
        # noise_scale = CAUCHY SCALE gamma; it is *not* a SD.
        eta = sc.noise_scale * rng.standard_cauchy(n)
    else:
        eta = sc.noise_scale * rng.standard_normal(n)
    return tau + eta, tau, eta


def draw_pool(sc: TailScenario, r: int, seed: int):
    """Nested R=1/R=3: first pair is exactly identical by construction."""
    if r < 1:
        raise ValueError("R must be positive")
    rng = np.random.default_rng(seed)
    ys, taus = [], []
    for _ in range(r):
        y, tau, _ = draw_one(sc, rng)
        ys.append(y)
        taus.append(tau)
    return np.asarray(ys), np.asarray(taus)


def design(preset: str):
    if preset == "smoke":
        return [TailScenario(regime, 24, 0.5, order=d)
                for regime in REGIMES for d in DIFFERENCE_ORDERS], 1, (1, 3), 31
    if preset in ("pilot", "confirmatory"):
        cells = [TailScenario(regime, n, scale, order=d)
                 for regime in REGIMES for d in DIFFERENCE_ORDERS
                 for n in (50, 200) for scale in (0.5, 2.0)]
        return cells, (5 if preset == "pilot" else 100), (1, 3), 81
    raise ValueError("unknown preset")


def _git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True,
                                       stderr=subprocess.DEVNULL, timeout=3).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _write_csv(path: Path, rows: list[dict]):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def compare_pool(sc: TailScenario, y: np.ndarray, truth: np.ndarray,
                 n_scan: int = 81):
    obj = PooledLOOCV(y, order=sc.order)
    ml = estimate_gaussian_differences(y, obj.d, scan_points=n_scan)
    bounded = bounded_brent(obj)
    multibracket = multibracket_brent(obj, n_scan=n_scan)
    choices = {
        METHODS[0]: (ml.lambda_ratio, ml),
        METHODS[1]: (bounded.best.lam, None),
        METHODS[2]: (multibracket.best.lam, None),
    }
    rows = []
    for method, (lam, estimator) in choices.items():
        residual = obj.trend(lam) - truth
        abs_err = np.abs(residual)
        rows.append({
            "regime": sc.regime, "N": sc.n, "d": sc.order, "R": obj.r,
            "skew_normal_alpha": SKEW_NORMAL_ALPHAS.get(sc.regime, float("nan")),
            "noise_scale": sc.noise_scale,
            "noise_scale_semantics": (
                "cauchy_scale_gamma" if not sc.observation_variance_exists
                else "observation_population_sd"),
            "observation_variance_exists": sc.observation_variance_exists,
            "sigma_epsilon": sc.sigma_epsilon,
            "method": method,
            "selected_lambda": lam,
            "selected_s": obj.smoothness(lam),
            "observed_LOOCV_MSE": obj.score(lam),
            "realized_true_trend_MSE": float(np.mean(residual**2)),
            "realized_mean_absolute_trend_error": float(np.mean(abs_err)),
            "realized_median_absolute_trend_error": float(np.median(abs_err)),
            "realized_p90_absolute_trend_error": float(np.quantile(abs_err, .9)),
            "estimated_sigma_eta2": (
                estimator.sigma_eta2 if estimator is not None else float("nan")),
            "estimated_sigma_epsilon2": (
                estimator.sigma_epsilon2 if estimator is not None else float("nan")),
            "number_stationary_sign_change_candidates": sum(
                c.kind == "stationary" for c in multibracket.candidates),
            "population_MSE_defined": sc.observation_variance_exists,
        })
    return rows


def summarize(rows: list[dict]):
    pools = {}
    for x in rows:
        key = (x["scenario_id"], x["replicate"], x["R"])
        slot = pools.setdefault(key, {})
        if x["method"] in slot:
            raise ValueError("duplicate method")
        slot[x["method"]] = x
    if not pools or any(set(p) != set(METHODS) for p in pools.values()):
        raise ValueError("incomplete methods")
    results = {}
    for regime in REGIMES:
        rr = [p for p in pools.values() if p[METHODS[0]]["R"] == 3 and
              p[METHODS[0]]["regime"] == regime]
        if not rr:
            continue
        results[regime] = {
            "pool_count": len(rr),
            "population_squared_error_risk_is_defined":
                regime != "cauchy_observation",
            "mle_lower_realized_trend_mse_than_bounded": sum(
                p[METHODS[0]]["realized_true_trend_MSE"] <
                p[METHODS[1]]["realized_true_trend_MSE"] for p in rr),
            "by_method": {
                m: {
                    "median_pool_realized_trend_MSE": float(np.median([
                        p[m]["realized_true_trend_MSE"] for p in rr])),
                    "median_pool_median_absolute_trend_error": float(np.median([
                        p[m]["realized_median_absolute_trend_error"] for p in rr])),
                    "median_pool_p90_absolute_trend_error": float(np.median([
                        p[m]["realized_p90_absolute_trend_error"] for p in rr])),
                    "mean_pool_realized_trend_MSE_diagnostic_only": float(np.mean([
                        p[m]["realized_true_trend_MSE"] for p in rr])),
                } for m in METHODS
            },
        }
    by_d = {}
    for order in DIFFERENCE_ORDERS:
        subset = [p for p in pools.values()
                  if p[METHODS[0]]["R"] == 3 and p[METHODS[0]]["d"] == order]
        by_d[str(order)] = {
            "pool_count": len(subset),
            "by_regime": {
                regime: {
                    "pool_count": len([
                        p for p in subset if p[METHODS[0]]["regime"] == regime]),
                    "median_realized_MSE_by_method": {
                        method: float(np.median([
                            p[method]["realized_true_trend_MSE"]
                            for p in subset if p[METHODS[0]]["regime"] == regime]))
                        for method in METHODS
                    },
                    "median_absolute_error_by_method": {
                        method: float(np.median([
                            p[method]["realized_median_absolute_trend_error"]
                            for p in subset if p[METHODS[0]]["regime"] == regime]))
                        for method in METHODS
                    },
                }
                for regime in REGIMES
            },
        }
    return {
        "status": "descriptive_only_no_independent_confirmation",
        "total_nested_pools": len(pools),
        "primary_R3_pools": sum(p[METHODS[0]]["R"] == 3 for p in pools.values()),
        "by_regime_R3": results,
        "by_difference_order_R3": by_d,
        "Cauchy_warning": (
            "Cauchy scale is not a standard deviation: no finite "
            "population noise variance, no Guerrero variance ratio, "
            "and no population expected squared-error risk for "
            "ordinary nontrivial linear reconstructions. "
            "Its mean empirical sample MSE is not comparable as expected risk."
        ),
        "nested_R_warning": "R=1 shares first generated series with R=3 at matching seed",
    }


def execute(preset: str, out: Path, dry_run: bool = False):
    scenarios, repeats, sizes, scan = design(preset)
    base = SEED_BASE if preset != "confirmatory" else SEED_BASE + 1000000
    manifest = {
        "protocol": "guerrero_tail_and_skew_stress_v1",
        "preset": preset,
        "status": "planned" if dry_run else "executed",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_sha": _git_sha(), "python": platform.python_version(),
        "numpy": np.__version__, "scipy": scipy.__version__,
        "rng": "numpy.random.default_rng", "base_seed": base,
        "seed_formula": "base_seed + scenario_id*10000 + replicate",
        "scenario_count": len(scenarios),
        "scenario_grid": [{"regime": s.regime, "N": s.n, "d": s.order,
                           "skew_normal_alpha": SKEW_NORMAL_ALPHAS.get(s.regime),
                           "noise_scale": s.noise_scale,
                           "scale_is_population_SD": s.observation_variance_exists,
                           "sigma_epsilon": s.sigma_epsilon} for s in scenarios],
        "replicates_per_scenario": repeats, "R_values": list(sizes),
        "nested_R1_in_R3": True, "difference_orders": list(DIFFERENCE_ORDERS),
        "difference_order_matches_trend_generator": True,
        "skew_normal_alphas": SKEW_NORMAL_ALPHAS,
        "methods": list(METHODS), "ml_profile_scan_points": scan,
        "Student_t3_df": T3_DF, "Student_t5_df": T5_DF,
        "skew_normal_centered_by_population_formula": True,
        "Gamma_shape": GAMMA_SHAPE, "Gamma_center_scale":
            "(X-shape)/sqrt(shape), sign flipped for left skew",
        "jump_probability": JUMP_PROBABILITY,
        "jump_SD_multiplier": JUMP_SD_MULTIPLIER,
        "GARCH_alpha": GARCH_ALPHA, "GARCH_beta": GARCH_BETA,
        "GARCH_initial_h": 1.,
        "GARCH_omega": 1-GARCH_ALPHA-GARCH_BETA,
        "Cauchy_gamma_scale_not_SD": True,
        "Cauchy_no_population_variance_or_expected_MSE": True,
        "latent_truth_is_evaluation_only": True,
        "expected_pools": len(scenarios)*repeats*len(sizes),
        "expected_method_rows": len(scenarios)*repeats*len(sizes)*len(METHODS),
        "no_original_campaign_modified": True,
    }
    if dry_run:
        print(json.dumps(manifest, indent=2))
        return manifest
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for scenario_id, sc in enumerate(scenarios):
        for replicate in range(repeats):
            seed = base + 10000*scenario_id + replicate
            for size in sizes:
                observed, truth = draw_pool(sc, r=size, seed=seed)
                records = compare_pool(sc, observed, truth, n_scan=scan)
                for rec in records:
                    rows.append({"scenario_id": scenario_id,
                                 "replicate": replicate, "seed": seed, **rec})
    _write_csv(out / "method_comparison.csv", rows)
    summary = summarize(rows)
    manifest["actual_rows"] = len(rows)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n",
                                       encoding="utf-8")
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n",
                                      encoding="utf-8")
    print(json.dumps({
        "status": manifest["status"], "scenarios": len(scenarios),
        "pools": summary["total_nested_pools"], "method_rows": len(rows),
        "by_regime_R3": summary["by_regime_R3"],
        "by_difference_order_R3": summary["by_difference_order_R3"],
        "output": str(out),
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
                           "tail_stress" / args.preset)
    execute(args.preset, out, args.dry_run)


if __name__ == "__main__":
    main()
