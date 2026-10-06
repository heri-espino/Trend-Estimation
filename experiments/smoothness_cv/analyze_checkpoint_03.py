from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


FEASIBLE_SELECTORS = (
    "forecast_cv_h",
    "forecast_cv_1",
    "cv",
    "gcv",
    "aicc",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Analyze frozen Checkpoint 03 simulations with paired, seed-clustered "
            "summaries. Common random numbers across mechanisms make seed the "
            "resampling unit."
        )
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    parser.add_argument("--bootstrap-reps", type=int, default=5000)
    parser.add_argument("--bootstrap-seed", type=int, default=20261005)
    return parser.parse_args()


def resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_03/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError(
            "No completed Checkpoint 03 run was found. "
            "run_checkpoint_03.py must finish successfully first."
        )
    return Path(latest.read_text(encoding="utf-8").strip())


def markdown_table(frame: pd.DataFrame, digits: int = 4) -> str:
    if frame.empty:
        return "_No rows._"
    clean = frame.copy()
    for column in clean.select_dtypes(include=[np.number]).columns:
        clean[column] = clean[column].map(
            lambda x: "" if pd.isna(x) else f"{float(x):.{digits}g}"
        )
    headers = [str(c) for c in clean.columns]
    rows = [[str(v) for v in row] for row in clean.to_numpy()]
    widths = [
        max(len(headers[j]), *(len(row[j]) for row in rows))
        for j in range(len(headers))
    ]
    header = "| " + " | ".join(
        headers[j].ljust(widths[j]) for j in range(len(headers))
    ) + " |"
    divider = "| " + " | ".join("-" * widths[j] for j in range(len(headers))) + " |"
    body = [
        "| " + " | ".join(row[j].ljust(widths[j]) for j in range(len(headers))) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def bootstrap_mean_ci(
    seed_values: np.ndarray,
    *,
    reps: int,
    rng: np.random.Generator,
) -> tuple[float, float, float]:
    seed_values = np.asarray(seed_values, dtype=float)
    seed_values = seed_values[np.isfinite(seed_values)]
    if seed_values.size == 0:
        return np.nan, np.nan, np.nan
    point = float(np.mean(seed_values))
    if seed_values.size == 1:
        return point, point, point
    draw = rng.integers(0, seed_values.size, size=(reps, seed_values.size))
    boot = np.mean(seed_values[draw], axis=1)
    lo, hi = np.quantile(boot, [0.025, 0.975])
    return point, float(lo), float(hi)


def ratio_summary(
    paired: pd.DataFrame,
    *,
    reps: int,
    rng: np.random.Generator,
) -> pd.DataFrame:
    rows: list[dict] = []

    scopes: list[tuple[str, pd.DataFrame]] = [("all", paired)]
    scopes.extend(
        (str(noise), group.copy())
        for noise, group in paired.groupby("noise_model", dropna=False)
    )

    for scope_name, scope in scopes:
        for (comparator, horizon), group in scope.groupby(
            ["comparator", "horizon"],
            dropna=False,
        ):
            by_seed = (
                group.groupby("seed", dropna=False)["log_mse_ratio"]
                .mean()
                .to_numpy(dtype=float)
            )
            point_log, lo_log, hi_log = bootstrap_mean_ci(
                by_seed,
                reps=reps,
                rng=rng,
            )
            rows.append(
                {
                    "noise_scope": scope_name,
                    "comparator": comparator,
                    "horizon": int(horizon),
                    "n_series": int(len(group)),
                    "n_seeds": int(group["seed"].nunique()),
                    "geometric_rmsfe_ratio": float(np.exp(0.5 * point_log)),
                    "ci95_low": float(np.exp(0.5 * lo_log)),
                    "ci95_high": float(np.exp(0.5 * hi_log)),
                    "series_win_rate": float(np.mean(group["mse_ratio"] < 1.0)),
                    "series_tie_rate": float(np.mean(np.isclose(group["mse_ratio"], 1.0))),
                    "median_rmsfe_ratio": float(np.median(group["rmsfe_ratio"])),
                    "median_s_difference": float(np.median(group["s_difference"])),
                }
            )
    return pd.DataFrame(rows)


def selected_s_summary(series_results: pd.DataFrame) -> pd.DataFrame:
    frame = series_results[
        series_results["selector"].isin(
            ["forecast_cv_h", "forecast_cv_1", "cv", "gcv", "aicc"]
        )
    ].copy()
    return (
        frame.groupby(["selector", "noise_model", "horizon"], dropna=False)
        .agg(
            n_series=("mean_selected_s", "size"),
            mean_s=("mean_selected_s", "mean"),
            median_s=("mean_selected_s", "median"),
            q25_s=("mean_selected_s", lambda x: np.quantile(x, 0.25)),
            q75_s=("mean_selected_s", lambda x: np.quantile(x, 0.75)),
            endpoint_one_rate=(
                "endpoint_one_rate",
                lambda x: np.mean(np.asarray(x) > 0.5),
            ),
            mean_edf=("mean_edf", "mean"),
        )
        .reset_index()
    )


def oracle_summary(oracle: pd.DataFrame) -> pd.DataFrame:
    frame = oracle.copy()
    frame["abs_gap_proposed_oracle"] = np.abs(frame["s_gap_proposed_oracle"])
    frame["abs_gap_recovery_oracle"] = np.abs(frame["s_gap_recovery_oracle"])
    frame["oracle_interior"] = (
        (frame["s_forecast_oracle"] > 0.01)
        & (frame["s_forecast_oracle"] < 0.99)
    )
    return (
        frame.groupby(["noise_model", "horizon"], dropna=False)
        .agg(
            n_series=("s_proposed", "size"),
            mean_s_proposed=("s_proposed", "mean"),
            mean_s_recovery=("s_recovery", "mean"),
            mean_s_forecast_oracle=("s_forecast_oracle", "mean"),
            oracle_interior_rate=("oracle_interior", "mean"),
            median_abs_gap_proposed_oracle=("abs_gap_proposed_oracle", "median"),
            median_abs_gap_recovery_oracle=("abs_gap_recovery_oracle", "median"),
            median_scaled_latent_excess=(
                "latent_excess_scaled_by_noise_var",
                "median",
            ),
        )
        .reset_index()
    )


def mechanism_summary(oracle: pd.DataFrame) -> pd.DataFrame:
    frame = oracle.copy()
    frame["oracle_interior"] = (
        (frame["s_forecast_oracle"] > 0.01)
        & (frame["s_forecast_oracle"] < 0.99)
    )
    frame["abs_gap_recovery_oracle"] = np.abs(frame["s_gap_recovery_oracle"])
    frame["abs_gap_proposed_oracle"] = np.abs(frame["s_gap_proposed_oracle"])
    return (
        frame.groupby(["trend_kind", "horizon"], dropna=False)
        .agg(
            n_series=("s_proposed", "size"),
            oracle_interior_rate=("oracle_interior", "mean"),
            mean_s_oracle=("s_forecast_oracle", "mean"),
            median_abs_recovery_oracle_gap=("abs_gap_recovery_oracle", "median"),
            median_abs_proposed_oracle_gap=("abs_gap_proposed_oracle", "median"),
            median_scaled_latent_excess=(
                "latent_excess_scaled_by_noise_var",
                "median",
            ),
        )
        .reset_index()
    )


def fractional_method_wins(series_results: pd.DataFrame) -> pd.DataFrame:
    frame = series_results[series_results["selector"].isin(FEASIBLE_SELECTORS)].copy()
    keys = [
        "seed",
        "scenario_id",
        "trend_kind",
        "noise_model",
        "noise_std",
        "horizon",
    ]
    group_min = frame.groupby(keys, dropna=False)["msfe"].transform("min")
    frame["is_winner"] = np.isclose(frame["msfe"], group_min, rtol=1e-10, atol=1e-12)
    n_winners = frame.groupby(keys, dropna=False)["is_winner"].transform("sum")
    frame["win_share"] = np.where(frame["is_winner"], 1.0 / n_winners, 0.0)
    return (
        frame.groupby(["selector", "horizon"], dropna=False)
        .agg(
            total_win_share=("win_share", "sum"),
            n_series=("scenario_id", "size"),
        )
        .reset_index()
        .assign(win_share_rate=lambda x: x["total_win_share"] / x["n_series"])
    )


def main() -> None:
    args = parse_args()
    run_dir = resolve_run_dir(args.run_dir)
    rng = np.random.default_rng(args.bootstrap_seed)

    series_results = pd.read_csv(run_dir / "series_results.csv")
    paired = pd.read_csv(run_dir / "paired_method_comparisons.csv")
    oracle = pd.read_csv(run_dir / "oracle_comparisons.csv")

    diagnostics = run_dir / "diagnostics"
    diagnostics.mkdir(parents=True, exist_ok=True)

    ratios = ratio_summary(
        paired,
        reps=args.bootstrap_reps,
        rng=rng,
    )
    selected = selected_s_summary(series_results)
    oracle_s = oracle_summary(oracle)
    mechanisms = mechanism_summary(oracle)
    wins = fractional_method_wins(series_results)

    outputs = {
        "paired_rmsfe_summary.csv": ratios,
        "selected_s_summary.csv": selected,
        "oracle_summary.csv": oracle_s,
        "mechanism_summary.csv": mechanisms,
        "method_win_shares.csv": wins,
    }
    for name, frame in outputs.items():
        frame.to_csv(diagnostics / name, index=False)

    main_ratios = ratios[ratios["noise_scope"] == "all"].copy()
    by_noise = ratios[
        (ratios["comparator"] == "forecast_cv_1")
        & (ratios["horizon"] > 1)
    ].copy()

    metadata = json.loads((run_dir / "run_metadata.json").read_text(encoding="utf-8"))

    report = [
        "# Checkpoint 03 paper-scale simulation report",
        "",
        f"Source run: {run_dir.as_posix()}",
        "",
        f"Preset: {metadata['preset']}",
        "",
        "Inference note: common random numbers are reused across trend mechanisms",
        "within each seed. Confidence intervals therefore resample seeds, not",
        "individual scenario rows.",
        "",
        "## Primary paired forecast comparison",
        "",
        "Geometric RMSFE ratio < 1 favors horizon-matched forecast-CV.",
        "",
        markdown_table(main_ratios),
        "",
        "## Horizon matching by noise model",
        "",
        markdown_table(by_noise),
        "",
        "## Smoothness and oracle targets",
        "",
        markdown_table(oracle_s),
        "",
        "## Mechanism diagnostics",
        "",
        markdown_table(mechanisms),
        "",
        "## Fractional method win shares",
        "",
        markdown_table(wins),
        "",
        "## Interpretation rules",
        "",
        "- treat h=1 forecast_cv_h versus forecast_cv_1 as an identity check;",
        "- emphasize paired ratios and seed-clustered intervals, not raw block counts;",
        "- do not use the latent oracle as a feasible forecasting competitor;",
        "- report iid, AR(1), and Student-t conditions separately when their conclusions differ;",
        "- do not add or remove DGPs after seeing this paper-preset result;",
        "- BIC remains outside the primary comparison because CP02 showed boundary degeneracy.",
        "",
    ]
    (run_dir / "checkpoint_report.md").write_text("\n".join(report), encoding="utf-8")

    print(f"Wrote {run_dir / 'checkpoint_report.md'}")
    print(f"Wrote diagnostics to {diagnostics}")


if __name__ == "__main__":
    main()
