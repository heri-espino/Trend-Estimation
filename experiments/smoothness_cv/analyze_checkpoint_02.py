from __future__ import annotations

import argparse
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
        description="Analyze Checkpoint 02 and produce design-freezing diagnostics."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_02/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError(
            "No completed Checkpoint 02 run was found. "
            "run_checkpoint_02.py must finish successfully first."
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


def selector_summary(results: pd.DataFrame) -> pd.DataFrame:
    return (
        results.groupby(["selector", "window", "horizon"], dropna=False)
        .agg(
            n=("selected_s", "size"),
            mean_s=("selected_s", "mean"),
            median_s=("selected_s", "median"),
            endpoint_one_rate=("selected_s", lambda x: np.mean(np.isclose(x, 1.0))),
            mean_mse=("forecast_mse_observed", "mean"),
            median_rel_rmsfe_gcv=("relative_rmsfe_to_gcv", "median"),
            median_latent_regret_ratio=("latent_regret_ratio", "median"),
        )
        .reset_index()
    )


def horizon_window_summary(paired: pd.DataFrame) -> pd.DataFrame:
    frame = paired.copy()
    frame["abs_s_gap_cvh_cv1"] = np.abs(frame["s_gap_cvh_minus_cv1"])
    return (
        frame.groupby(["window", "horizon"], dropna=False)
        .agg(
            n=("mse_ratio_cvh_to_cv1", "size"),
            median_mse_ratio=("mse_ratio_cvh_to_cv1", "median"),
            mean_mse_ratio=("mse_ratio_cvh_to_cv1", "mean"),
            matched_win_rate=("mse_ratio_cvh_to_cv1", lambda x: np.mean(x < 1.0)),
            median_abs_s_gap=("abs_s_gap_cvh_cv1", "median"),
            mean_s_cvh=("s_cvh", "mean"),
            mean_s_cv1=("s_cv1", "mean"),
        )
        .reset_index()
    )


def mechanism_summary(paired: pd.DataFrame) -> pd.DataFrame:
    frame = paired.copy()
    frame["abs_gap_cvh_oracle"] = np.abs(frame["s_gap_cvh_minus_forecast_oracle"])
    frame["abs_gap_recovery_oracle"] = np.abs(
        frame["s_gap_recovery_minus_forecast_oracle"]
    )
    frame["oracle_interior"] = (
        (frame["s_forecast_oracle"] > 0.01)
        & (frame["s_forecast_oracle"] < 0.99)
    )
    return (
        frame.groupby(["trend_kind", "noise_model", "window", "horizon"], dropna=False)
        .agg(
            n=("s_cvh", "size"),
            mean_s_cvh=("s_cvh", "mean"),
            mean_s_oracle=("s_forecast_oracle", "mean"),
            oracle_interior_rate=("oracle_interior", "mean"),
            median_abs_gap_cvh_oracle=("abs_gap_cvh_oracle", "median"),
            median_abs_gap_recovery_oracle=("abs_gap_recovery_oracle", "median"),
            median_mse_ratio_cvh_cv1=("mse_ratio_cvh_to_cv1", "median"),
            matched_win_rate=("mse_ratio_cvh_to_cv1", lambda x: np.mean(x < 1.0)),
        )
        .reset_index()
    )


def trend_screen(paired: pd.DataFrame) -> pd.DataFrame:
    frame = paired.copy()
    frame["abs_gap_recovery_oracle"] = np.abs(
        frame["s_gap_recovery_minus_forecast_oracle"]
    )
    frame["abs_gap_cvh_oracle"] = np.abs(frame["s_gap_cvh_minus_forecast_oracle"])
    frame["oracle_interior"] = (
        (frame["s_forecast_oracle"] > 0.01)
        & (frame["s_forecast_oracle"] < 0.99)
    )
    frame["matched_win"] = frame["mse_ratio_cvh_to_cv1"] < 1.0

    out = (
        frame.groupby("trend_kind", dropna=False)
        .agg(
            n=("s_cvh", "size"),
            oracle_interior_rate=("oracle_interior", "mean"),
            mean_oracle_s=("s_forecast_oracle", "mean"),
            sd_oracle_s=("s_forecast_oracle", "std"),
            median_abs_recovery_oracle_gap=("abs_gap_recovery_oracle", "median"),
            median_abs_cvh_oracle_gap=("abs_gap_cvh_oracle", "median"),
            matched_win_rate=("matched_win", "mean"),
            median_matched_mse_ratio=("mse_ratio_cvh_to_cv1", "median"),
        )
        .reset_index()
    )
    return out.sort_values(
        ["oracle_interior_rate", "median_abs_recovery_oracle_gap"],
        ascending=[False, False],
    )


def method_wins(results: pd.DataFrame) -> pd.DataFrame:
    feasible = results[results["selector"].isin(FEASIBLE_SELECTORS)].copy()
    keys = [
        "scenario_id",
        "seed",
        "trend_kind",
        "noise_model",
        "noise_std",
        "window",
        "outer_origin",
        "horizon",
    ]
    idx = feasible.groupby(keys)["forecast_mse_observed"].idxmin()
    wins = feasible.loc[idx, ["selector", "window", "horizon"]]
    out = (
        wins.groupby(["selector", "window", "horizon"])
        .size()
        .rename("wins")
        .reset_index()
    )
    totals = (
        wins.groupby(["window", "horizon"])
        .size()
        .rename("total_blocks")
        .reset_index()
    )
    out = out.merge(totals, on=["window", "horizon"], validate="many_to_one")
    out["win_rate"] = out["wins"] / out["total_blocks"]
    return out.sort_values(
        ["window", "horizon", "win_rate"],
        ascending=[True, True, False],
    )


def criterion_audit(audit: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows: list[dict] = []
    group_keys = [
        "scenario_id",
        "trend_kind",
        "noise_model",
        "noise_std",
        "window",
        "outer_origin",
        "criterion",
    ]
    for key, group in audit.groupby(group_keys, dropna=False):
        group = group.sort_values("smoothness")
        values = group["score"].to_numpy(dtype=float)
        finite = np.isfinite(values)
        if not np.any(finite):
            continue
        finite_idx = np.flatnonzero(finite)
        best_local = finite_idx[int(np.argmin(values[finite]))]
        best_s = float(group.iloc[best_local]["smoothness"])
        first_finite_s = float(group.iloc[finite_idx[0]]["smoothness"])
        last_finite_s = float(group.iloc[finite_idx[-1]]["smoothness"])
        rows.append(
            {
                **dict(zip(group_keys, key)),
                "best_s": best_s,
                "first_finite_s": first_finite_s,
                "last_finite_s": last_finite_s,
                "at_left_finite_boundary": bool(np.isclose(best_s, first_finite_s)),
                "at_right_finite_boundary": bool(np.isclose(best_s, last_finite_s)),
            }
        )
    detailed = pd.DataFrame(rows)
    summary = (
        detailed.groupby("criterion", dropna=False)
        .agg(
            n_curves=("best_s", "size"),
            mean_best_s=("best_s", "mean"),
            median_best_s=("best_s", "median"),
            left_boundary_rate=("at_left_finite_boundary", "mean"),
            right_boundary_rate=("at_right_finite_boundary", "mean"),
        )
        .reset_index()
    )
    return detailed, summary


def main() -> None:
    args = parse_args()
    run_dir = resolve_run_dir(args.run_dir)

    results = pd.read_csv(run_dir / "results.csv")
    paired = pd.read_csv(run_dir / "paired_comparisons.csv")
    audit = pd.read_csv(run_dir / "classical_score_audit.csv")

    diagnostics = run_dir / "diagnostics"
    diagnostics.mkdir(parents=True, exist_ok=True)

    selector = selector_summary(results)
    horizon_window = horizon_window_summary(paired)
    mechanisms = mechanism_summary(paired)
    trends = trend_screen(paired)
    wins = method_wins(results)
    audit_detail, audit_summary = criterion_audit(audit)

    outputs = {
        "selector_summary.csv": selector,
        "horizon_window_summary.csv": horizon_window,
        "mechanism_summary.csv": mechanisms,
        "trend_screen.csv": trends,
        "method_wins.csv": wins,
        "criterion_audit_detail.csv": audit_detail,
        "criterion_audit_summary.csv": audit_summary,
    }
    for name, frame in outputs.items():
        frame.to_csv(diagnostics / name, index=False)

    report = [
        "# Checkpoint 02 diagnostic report",
        "",
        f"Source run: {run_dir.as_posix()}",
        "",
        "CP02 is a design-refinement checkpoint. These summaries determine which",
        "mechanisms and window lengths should survive into the frozen paper-scale",
        "simulation; they are not final paper estimates.",
        "",
        "## Trend-mechanism screen",
        "",
        markdown_table(trends),
        "",
        "## Horizon matching by window",
        "",
        markdown_table(horizon_window),
        "",
        "## Classical criterion audit",
        "",
        markdown_table(audit_summary),
        "",
        "## Selector summary",
        "",
        markdown_table(selector),
        "",
        "## Per-block feasible-method wins",
        "",
        markdown_table(wins),
        "",
        "## Decision rules for freezing CP03",
        "",
        "- retain at least one nearly linear mechanism as a sanity/control case;",
        "- retain nonlinear mechanisms where the latent forecast oracle is not almost always S=1;",
        "- prioritize mechanisms with a visible recovery-optimal versus forecast-oracle gap;",
        "- retain window lengths only if they materially change the smoothness/forecast trade-off;",
        "- treat BIC as diagnostic-only if its global optimum remains pinned to the left finite boundary;",
        "- do not select mechanisms solely because forecast-CV happens to win on this exploratory run;",
        "- freeze CP03 seeds and final test origins before running the paper-scale experiment.",
        "",
    ]
    (run_dir / "checkpoint_report.md").write_text("\n".join(report), encoding="utf-8")

    print(f"Wrote {run_dir / 'checkpoint_report.md'}")
    print(f"Wrote diagnostics to {diagnostics}")


if __name__ == "__main__":
    main()
