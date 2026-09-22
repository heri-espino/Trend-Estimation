from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

import trend_estimation as td


SMOKE_GRID = {
    "ar1_phi": (0.0, 0.8),
    "horizon": (1, 6),
}

EXPLORE_GRID = {
    "ar1_phi": (-0.8, -0.4, 0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95),
    "horizon": (1, 2, 3, 6, 12),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Mechanism study for persistence and forecast horizon. "
            "Compares four lambda objectives conditional on the same selected "
            "difference order and window length."
        )
    )
    parser.add_argument(
        "--preset",
        choices=("smoke", "explore", "boundary"),
        default="explore",
        help=(
            "boundary repeats the full explore grid with a wider log-lambda "
            "domain and denser root-discovery grid."
        ),
    )
    parser.add_argument("--n-seeds", type=int, default=None)
    parser.add_argument("--n-obs", type=int, default=240)
    parser.add_argument("--slope-noise-std", type=float, default=0.01)
    parser.add_argument("--observation-noise-std", type=float, default=0.5)
    parser.add_argument("--outer-initial-train", type=int, default=120)
    parser.add_argument("--outer-step", type=int, default=6)
    parser.add_argument("--inner-step", type=int, default=3)
    parser.add_argument("--max-inner-origins", type=int, default=30)
    parser.add_argument("--orders", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--windows", type=int, nargs="+", default=[24, 48, 72])
    parser.add_argument("--n-grid", type=int, default=None)
    parser.add_argument("--log-lambda-min", type=float, default=None)
    parser.add_argument("--log-lambda-max", type=float, default=None)
    return parser.parse_args()


def git_short_sha() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def optimize_prepared(prepared, *, log_bounds, n_grid):
    def value_grad_hess(lambda_value: float):
        result = prepared.evaluate(lambda_value)
        return result.value, result.first, result.second

    return td.find_stationary_points_log_lambda(
        value_grad_hess,
        log_bounds=log_bounds,
        n_grid=n_grid,
    )


def selected_inner_splits(record, horizon: int):
    window = int(record.selected_window)
    return [
        td.RollingOriginSplit(
            train=slice(origin - window, origin),
            validation=slice(origin, origin + int(horizon)),
        )
        for origin in record.inner_selection.common_inner_origins_
    ]


def forecast_from_lambda(history, *, order, window, lambda_, horizon):
    fit_history = np.asarray(history[-window:], dtype=float)
    model = td.PurePenalizedTrend(
        order=order,
        smoothness=None,
        lambda_=lambda_,
    ).fit(fit_history)
    return model.forecast(horizon), model


def oracle_ar_forecast(history, *, order, window, lambda_, horizon, phi):
    trend_prediction, model = forecast_from_lambda(
        history,
        order=order,
        window=window,
        lambda_=lambda_,
        horizon=horizon,
    )
    fit_history = np.asarray(history[-window:], dtype=float)
    last_residual = float(fit_history[-1] - model.trend_[-1])
    powers = float(phi) ** np.arange(1, horizon + 1, dtype=float)
    return trend_prediction + powers * last_residual


def run_configuration(*, seed, phi, horizon, args):
    data = td.make_local_linear_ar1_series(
        n_obs=args.n_obs,
        slope_noise_std=args.slope_noise_std,
        observation_noise_std=args.observation_noise_std,
        ar1_phi=phi,
        random_state=seed,
    )

    nested = td.nested_rolling_pure_forecast(
        data.y,
        outer_initial_train=args.outer_initial_train,
        horizon=horizon,
        outer_step=args.outer_step,
        orders=tuple(args.orders),
        windows=tuple(args.windows),
        inner_step=args.inner_step,
        max_inner_origins=args.max_inner_origins,
        min_inner_origins=2,
        log_bounds=(args.log_lambda_min, args.log_lambda_max),
        n_grid=args.n_grid,
    )

    rows = []
    log_bounds = (args.log_lambda_min, args.log_lambda_max)

    for record in nested.records:
        origin = int(record.origin)
        history = data.y[:origin]
        latent_history = data.true_trend[:origin]
        latent_future = data.true_trend[
            record.validation_start:record.validation_stop
        ]
        observed_future = record.observed
        order = int(record.selected_order)
        window = int(record.selected_window)
        splits = selected_inner_splits(record, horizon)

        observed_search = record.inner_selection.best_.search_

        latent_search = optimize_prepared(
            td.prepare_rolling_pure_forecast_objective(
                history,
                splits,
                order=order,
                target_series=latent_history,
            ),
            log_bounds=log_bounds,
            n_grid=args.n_grid,
        )
        ar_search = optimize_prepared(
            td.prepare_rolling_pure_forecast_objective(
                history,
                splits,
                order=order,
                residual_ar_phi=phi,
            ),
            log_bounds=log_bounds,
            n_grid=args.n_grid,
        )
        recovery_search = optimize_prepared(
            td.prepare_rolling_pure_recovery_objective(
                history,
                latent_history,
                splits,
                order=order,
            ),
            log_bounds=log_bounds,
            n_grid=args.n_grid,
        )

        smoothness = {}
        for name, search in (
            ("observed", observed_search),
            ("latent", latent_search),
            ("ar", ar_search),
            ("recovery", recovery_search),
        ):
            smoothness[name] = td.lambda_to_smoothness(
                search.best_lambda_,
                n_obs=window,
                order=order,
            )

        pred_observed = record.prediction
        pred_latent_lambda, _ = forecast_from_lambda(
            history,
            order=order,
            window=window,
            lambda_=latent_search.best_lambda_,
            horizon=horizon,
        )
        pred_recovery_lambda, _ = forecast_from_lambda(
            history,
            order=order,
            window=window,
            lambda_=recovery_search.best_lambda_,
            horizon=horizon,
        )
        pred_ar = oracle_ar_forecast(
            history,
            order=order,
            window=window,
            lambda_=ar_search.best_lambda_,
            horizon=horizon,
            phi=phi,
        )

        rows.append(
            {
                "seed": seed,
                "ar1_phi": phi,
                "horizon": horizon,
                "outer_origin": origin,
                "selected_order": order,
                "selected_window": window,
                "lambda_observed_forecast": float(observed_search.best_lambda_),
                "lambda_latent_forecast_oracle": float(latent_search.best_lambda_),
                "lambda_ar_residual_oracle": float(ar_search.best_lambda_),
                "lambda_recovery_oracle": float(recovery_search.best_lambda_),
                "smoothness_observed_forecast": smoothness["observed"],
                "smoothness_latent_forecast_oracle": smoothness["latent"],
                "smoothness_ar_residual_oracle": smoothness["ar"],
                "smoothness_recovery_oracle": smoothness["recovery"],
                "gap_observed_minus_latent": smoothness["observed"] - smoothness["latent"],
                "gap_observed_minus_ar": smoothness["observed"] - smoothness["ar"],
                "gap_observed_minus_recovery": smoothness["observed"] - smoothness["recovery"],
                "observed_mse_observed_lambda": float(
                    np.mean((observed_future - pred_observed) ** 2)
                ),
                "observed_mse_latent_lambda": float(
                    np.mean((observed_future - pred_latent_lambda) ** 2)
                ),
                "observed_mse_recovery_lambda": float(
                    np.mean((observed_future - pred_recovery_lambda) ** 2)
                ),
                "observed_mse_ar_oracle": float(
                    np.mean((observed_future - pred_ar) ** 2)
                ),
                "latent_mse_observed_lambda": float(
                    np.mean((latent_future - pred_observed) ** 2)
                ),
                "latent_mse_latent_lambda": float(
                    np.mean((latent_future - pred_latent_lambda) ** 2)
                ),
                "latent_mse_recovery_lambda": float(
                    np.mean((latent_future - pred_recovery_lambda) ** 2)
                ),
                "search_source_observed": observed_search.best_source_,
                "search_source_latent": latent_search.best_source_,
                "search_source_ar": ar_search.best_source_,
                "search_source_recovery": recovery_search.best_source_,
                "n_stationary_observed": len(observed_search.points_),
                "n_stationary_latent": len(latent_search.points_),
                "n_stationary_ar": len(ar_search.points_),
                "n_stationary_recovery": len(recovery_search.points_),
            }
        )

    return rows


def write_summary(frame: pd.DataFrame, path: Path) -> None:
    summary_frame = frame.copy()
    for objective in ("observed", "latent", "ar", "recovery"):
        source = summary_frame[f"search_source_{objective}"]
        summary_frame[f"lower_boundary_{objective}"] = (
            source.eq("lower_boundary").astype(float)
        )
        summary_frame[f"upper_boundary_{objective}"] = (
            source.eq("upper_boundary").astype(float)
        )

    summary = (
        summary_frame.groupby(["seed", "ar1_phi", "horizon"], dropna=False)
        .agg(
            n_outer_origins=("outer_origin", "size"),
            mean_order=("selected_order", "mean"),
            mean_window=("selected_window", "mean"),
            s_observed=("smoothness_observed_forecast", "mean"),
            s_latent=("smoothness_latent_forecast_oracle", "mean"),
            s_ar=("smoothness_ar_residual_oracle", "mean"),
            s_recovery=("smoothness_recovery_oracle", "mean"),
            gap_observed_minus_latent=("gap_observed_minus_latent", "mean"),
            gap_observed_minus_ar=("gap_observed_minus_ar", "mean"),
            gap_observed_minus_recovery=("gap_observed_minus_recovery", "mean"),
            mse_observed=("observed_mse_observed_lambda", "mean"),
            mse_latent_lambda=("observed_mse_latent_lambda", "mean"),
            mse_recovery_lambda=("observed_mse_recovery_lambda", "mean"),
            mse_ar_oracle=("observed_mse_ar_oracle", "mean"),
            latent_mse_observed=("latent_mse_observed_lambda", "mean"),
            latent_mse_latent=("latent_mse_latent_lambda", "mean"),
            latent_mse_recovery=("latent_mse_recovery_lambda", "mean"),
            frac_lower_observed=("lower_boundary_observed", "mean"),
            frac_upper_observed=("upper_boundary_observed", "mean"),
            frac_lower_latent=("lower_boundary_latent", "mean"),
            frac_upper_latent=("upper_boundary_latent", "mean"),
            frac_lower_ar=("lower_boundary_ar", "mean"),
            frac_upper_ar=("upper_boundary_ar", "mean"),
            frac_lower_recovery=("lower_boundary_recovery", "mean"),
            frac_upper_recovery=("upper_boundary_recovery", "mean"),
        )
        .reset_index()
    )
    summary["rmse_ar_vs_trend_only"] = np.sqrt(
        summary["mse_ar_oracle"] / summary["mse_observed"]
    )
    summary.to_csv(path, index=False)


def main() -> None:
    args = parse_args()

    if args.preset == "smoke":
        grid = SMOKE_GRID
        default_seeds = 1
        default_n_grid = 161
        default_log_bounds = (-10.0, 16.0)
    elif args.preset == "boundary":
        grid = EXPLORE_GRID
        default_seeds = 30
        default_n_grid = 321
        default_log_bounds = (-18.0, 24.0)
    else:
        grid = EXPLORE_GRID
        default_seeds = 30
        default_n_grid = 161
        default_log_bounds = (-10.0, 16.0)

    n_seeds = default_seeds if args.n_seeds is None else int(args.n_seeds)
    args.n_grid = default_n_grid if args.n_grid is None else int(args.n_grid)
    args.log_lambda_min = (
        default_log_bounds[0]
        if args.log_lambda_min is None
        else float(args.log_lambda_min)
    )
    args.log_lambda_max = (
        default_log_bounds[1]
        if args.log_lambda_max is None
        else float(args.log_lambda_max)
    )
    configs = list(product(range(n_seeds), grid["ar1_phi"], grid["horizon"]))

    rows = []
    total_start = time.perf_counter()
    for i, (seed, phi, horizon) in enumerate(configs, start=1):
        start = time.perf_counter()
        print(
            f"[{i}/{len(configs)}] seed={seed} phi={phi} h={horizon}",
            flush=True,
        )
        new_rows = run_configuration(
            seed=int(seed),
            phi=float(phi),
            horizon=int(horizon),
            args=args,
        )
        rows.extend(new_rows)
        print(
            f"    completed in {time.perf_counter() - start:.2f}s; "
            f"outer rows={len(new_rows)}",
            flush=True,
        )

    frame = pd.DataFrame(rows)
    elapsed = time.perf_counter() - total_start
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = (
        Path("results")
        / "forecast_optimal_smoothing"
        / f"{stamp}_persistence-mechanism_{args.preset}_{git_short_sha()}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)
    frame.to_csv(run_dir / "mechanism_grid.csv", index=False)
    write_summary(frame, run_dir / "summary.csv")

    metadata = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_short_sha(),
        "experiment": "persistence_horizon_mechanism",
        "preset": args.preset,
        "n_seeds": n_seeds,
        "n_obs": args.n_obs,
        "slope_noise_std": args.slope_noise_std,
        "observation_noise_std": args.observation_noise_std,
        "outer_initial_train": args.outer_initial_train,
        "outer_step": args.outer_step,
        "inner_step": args.inner_step,
        "max_inner_origins": args.max_inner_origins,
        "orders": list(args.orders),
        "windows": list(args.windows),
        "n_grid": args.n_grid,
        "log_lambda_bounds": [args.log_lambda_min, args.log_lambda_max],
        "grid": {key: list(values) for key, values in grid.items()},
        "n_configurations": len(configs),
        "n_output_rows": len(frame),
        "elapsed_seconds": elapsed,
    }
    with (run_dir / "run_metadata.json").open("w", encoding="utf-8") as handle:
        json.dump(metadata, handle, indent=2)

    print(f"Wrote results to {run_dir} in {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
