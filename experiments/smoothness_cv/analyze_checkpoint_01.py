from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize Checkpoint 01 without changing any experiment design."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_01/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("Checkpoint 01 LATEST.txt was not found.")
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
    header = "| " + " | ".join(headers[j].ljust(widths[j]) for j in range(len(headers))) + " |"
    divider = "| " + " | ".join("-" * widths[j] for j in range(len(headers))) + " |"
    body = [
        "| " + " | ".join(row[j].ljust(widths[j]) for j in range(len(headers))) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def selector_summary(results: pd.DataFrame) -> pd.DataFrame:
    return (
        results.groupby(["selector", "horizon"], dropna=False)
        .agg(
            n=("forecast_mse_observed", "size"),
            mean_s=("selected_s", "mean"),
            median_s=("selected_s", "median"),
            endpoint_zero_rate=("selected_s", lambda x: np.mean(np.isclose(x, 0.0))),
            endpoint_one_rate=("selected_s", lambda x: np.mean(np.isclose(x, 1.0))),
            mean_mse=("forecast_mse_observed", "mean"),
            median_rel_rmsfe_gcv=("relative_rmsfe_to_gcv", "median"),
        )
        .reset_index()
    )


def horizon_summary(horizon_matching: pd.DataFrame) -> pd.DataFrame:
    return (
        horizon_matching.groupby("horizon", dropna=False)
        .agg(
            n=("mse_ratio_h_over_1", "size"),
            median_mse_ratio=("mse_ratio_h_over_1", "median"),
            mean_mse_ratio=("mse_ratio_h_over_1", "mean"),
            win_rate_h=("mse_ratio_h_over_1", lambda x: np.mean(x < 1.0)),
            tie_rate=("mse_ratio_h_over_1", lambda x: np.mean(np.isclose(x, 1.0))),
            mean_s_difference=("smoothness_difference_h_minus_1", "mean"),
            median_abs_s_difference=(
                "smoothness_difference_h_minus_1",
                lambda x: np.median(np.abs(x)),
            ),
        )
        .reset_index()
    )


def recovery_summary(results: pd.DataFrame) -> pd.DataFrame:
    keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "outer_origin",
        "horizon",
    ]
    f = results.loc[
        results["selector"] == "forecast_cv_h",
        keys + ["selected_s", "forecast_mse_observed", "train_recovery_mse"],
    ].rename(
        columns={
            "selected_s": "s_forecast",
            "forecast_mse_observed": "mse_forecast_selector",
            "train_recovery_mse": "recovery_mse_forecast_selector",
        }
    )
    r = results.loc[
        results["selector"] == "recovery_oracle_train",
        keys + ["selected_s", "forecast_mse_observed", "train_recovery_mse"],
    ].rename(
        columns={
            "selected_s": "s_recovery",
            "forecast_mse_observed": "mse_recovery_selector",
            "train_recovery_mse": "recovery_mse_oracle",
        }
    )
    paired = f.merge(r, on=keys, validate="one_to_one")
    paired["s_gap"] = paired["s_forecast"] - paired["s_recovery"]
    paired["abs_s_gap"] = np.abs(paired["s_gap"])
    paired["forecast_mse_ratio_to_recovery_oracle"] = (
        paired["mse_forecast_selector"] / paired["mse_recovery_selector"]
    )

    return (
        paired.groupby("horizon", dropna=False)
        .agg(
            n=("abs_s_gap", "size"),
            mean_s_forecast=("s_forecast", "mean"),
            mean_s_recovery=("s_recovery", "mean"),
            median_abs_s_gap=("abs_s_gap", "median"),
            rate_abs_gap_gt_010=("abs_s_gap", lambda x: np.mean(x > 0.10)),
            median_forecast_mse_ratio_to_recovery=(
                "forecast_mse_ratio_to_recovery_oracle",
                "median",
            ),
        )
        .reset_index()
    )


def method_win_table(results: pd.DataFrame) -> pd.DataFrame:
    feasible = results[
        results["selector"].isin(
            ["forecast_cv_h", "forecast_cv_1", "cv", "gcv", "aicc", "bic"]
        )
    ].copy()
    keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "outer_origin",
        "horizon",
    ]
    idx = feasible.groupby(keys)["forecast_mse_observed"].idxmin()
    wins = feasible.loc[idx, ["selector", "horizon"]]
    out = (
        wins.groupby(["selector", "horizon"])
        .size()
        .rename("wins")
        .reset_index()
    )
    totals = wins.groupby("horizon").size().rename("total_blocks").reset_index()
    out = out.merge(totals, on="horizon")
    out["win_rate"] = out["wins"] / out["total_blocks"]
    return out.sort_values(["horizon", "win_rate"], ascending=[True, False])


def mechanism_summary(results: pd.DataFrame) -> pd.DataFrame:
    frame = results[results["selector"] == "forecast_cv_h"].copy()
    return (
        frame.groupby(["trend_kind", "noise_model", "horizon"], dropna=False)
        .agg(
            n=("selected_s", "size"),
            mean_s=("selected_s", "mean"),
            median_s=("selected_s", "median"),
            mean_mse=("forecast_mse_observed", "mean"),
        )
        .reset_index()
    )


def main() -> None:
    args = parse_args()
    run_dir = resolve_run_dir(args.run_dir)

    results = pd.read_csv(run_dir / "results.csv")
    horizon_matching = pd.read_csv(run_dir / "horizon_matching.csv")

    s_summary = selector_summary(results)
    h_summary = horizon_summary(horizon_matching)
    r_summary = recovery_summary(results)
    wins = method_win_table(results)
    mechanisms = mechanism_summary(results)

    diagnostics_dir = run_dir / "diagnostics"
    diagnostics_dir.mkdir(parents=True, exist_ok=True)
    s_summary.to_csv(diagnostics_dir / "selector_summary.csv", index=False)
    h_summary.to_csv(diagnostics_dir / "horizon_matching_summary.csv", index=False)
    r_summary.to_csv(diagnostics_dir / "forecast_vs_recovery_summary.csv", index=False)
    wins.to_csv(diagnostics_dir / "method_wins.csv", index=False)
    mechanisms.to_csv(diagnostics_dir / "mechanism_summary.csv", index=False)

    report = [
        "# Checkpoint 01 diagnostic report",
        "",
        f"Source run: {run_dir.as_posix()}",
        "",
        "This report is descriptive only. It does not freeze CP02 or assert that",
        "the proposed selector is superior.",
        "",
        "## Selector summary",
        "",
        markdown_table(s_summary),
        "",
        "## Horizon-matched versus one-step tuning",
        "",
        markdown_table(h_summary),
        "",
        "## Forecast-optimal versus recovery-optimal smoothness",
        "",
        markdown_table(r_summary),
        "",
        "## Per-block method wins",
        "",
        markdown_table(wins),
        "",
        "## Forecast-CV smoothness by mechanism",
        "",
        markdown_table(mechanisms),
        "",
        "## Required human/agent review before CP02",
        "",
        "- inspect endpoint selection rates;",
        "- inspect objective curves rather than only aggregate scores;",
        "- inspect results by trend mechanism and noise dependence;",
        "- verify whether horizon-matched gains, if any, are broad or driven by a few cases;",
        "- verify whether the recovery-versus-forecast gap is scientifically interpretable;",
        "- do not run the paper preset until those checks are complete.",
        "",
    ]
    (run_dir / "checkpoint_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {run_dir / 'checkpoint_report.md'}")
    print(f"Wrote diagnostics to {diagnostics_dir}")


if __name__ == "__main__":
    main()
