from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


BOOTSTRAP_REPS = 5000
BOOTSTRAP_SEED = 20261007


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze CP05 frozen external financial panel."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_05/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("No completed Checkpoint 05 run was found.")
    return Path(latest.read_text(encoding="utf-8").strip())


def _geomean(values: np.ndarray) -> float:
    x = np.asarray(values, dtype=float)
    x = x[np.isfinite(x) & (x > 0.0)]
    if x.size == 0:
        return np.nan
    return float(np.exp(np.mean(np.log(x))))


def _paired(decisions: pd.DataFrame) -> pd.DataFrame:
    keys = [
        "series", "asset_class", "outer_number",
        "test_start_date", "test_end_date",
    ]
    dyn = decisions.loc[
        decisions["rule"].eq("recency_hl3"),
        keys + ["level_rmse", "fallback_used", "order", "window", "selected_s"],
    ].rename(
        columns={
            "level_rmse": "rmse_dynamic",
            "selected_s": "s_dynamic",
        }
    )
    last = decisions.loc[
        decisions["rule"].eq("last"),
        keys + ["level_rmse", "selected_s"],
    ].rename(
        columns={
            "level_rmse": "rmse_last",
            "selected_s": "s_last",
        }
    )
    pooled = decisions.loc[
        decisions["rule"].eq("pooled_cv_same_config"),
        keys + ["level_rmse", "selected_s"],
    ].rename(
        columns={
            "level_rmse": "rmse_pooled",
            "selected_s": "s_pooled",
        }
    )
    out = dyn.merge(last, on=keys, validate="one_to_one")
    out = out.merge(pooled, on=keys, validate="one_to_one")
    out["ratio_vs_last"] = out["rmse_dynamic"] / out["rmse_last"]
    out["ratio_vs_pooled"] = out["rmse_dynamic"] / out["rmse_pooled"]
    out["log_ratio_vs_last"] = np.log(out["ratio_vs_last"])
    out["log_ratio_vs_pooled"] = np.log(out["ratio_vs_pooled"])
    out["s_dynamic_minus_last"] = out["s_dynamic"] - out["s_last"]
    out["s_dynamic_minus_pooled"] = out["s_dynamic"] - out["s_pooled"]
    return out


def _series_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for (asset_class, series), group in paired.groupby(
        ["asset_class", "series"],
        sort=True,
    ):
        rows.append(
            {
                "asset_class": asset_class,
                "series": series,
                "n_outer": int(len(group)),
                "geometric_rmse_ratio_vs_last": _geomean(group["ratio_vs_last"]),
                "geometric_rmse_ratio_vs_pooled": _geomean(group["ratio_vs_pooled"]),
                "win_rate_vs_last": float(np.mean(group["ratio_vs_last"] < 1.0)),
                "win_rate_vs_pooled": float(np.mean(group["ratio_vs_pooled"] < 1.0)),
                "fallback_rate": float(np.mean(group["fallback_used"].astype(bool))),
                "mean_s_dynamic": float(group["s_dynamic"].mean()),
                "mean_abs_s_change_from_last": float(
                    np.mean(np.abs(group["s_dynamic_minus_last"]))
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["asset_class", "series"]
    ).reset_index(drop=True)


def _cluster_bootstrap(
    paired: pd.DataFrame,
    *,
    log_column: str,
    reps: int = BOOTSTRAP_REPS,
    seed: int = BOOTSTRAP_SEED,
) -> tuple[float, float, float]:
    series_logs = (
        paired.groupby("series", sort=True)[log_column]
        .mean()
        .dropna()
        .to_numpy(dtype=float)
    )
    if series_logs.size == 0:
        return np.nan, np.nan, np.nan
    point = float(np.exp(np.mean(series_logs)))
    rng = np.random.default_rng(seed)
    draws = np.empty(reps, dtype=float)
    n = series_logs.size
    for i in range(reps):
        sample = series_logs[rng.integers(0, n, size=n)]
        draws[i] = np.exp(np.mean(sample))
    lo, hi = np.quantile(draws, [0.025, 0.975])
    return point, float(lo), float(hi)


def _summary_row(paired: pd.DataFrame, label: str) -> dict:
    point_pool, lo_pool, hi_pool = _cluster_bootstrap(
        paired,
        log_column="log_ratio_vs_pooled",
    )
    point_last, lo_last, hi_last = _cluster_bootstrap(
        paired,
        log_column="log_ratio_vs_last",
    )
    series = _series_summary(paired)
    return {
        "group": label,
        "n_series": int(paired["series"].nunique()),
        "n_outer": int(len(paired)),
        "geometric_rmse_ratio_vs_pooled": point_pool,
        "cluster_ci95_lo_vs_pooled": lo_pool,
        "cluster_ci95_hi_vs_pooled": hi_pool,
        "outer_win_rate_vs_pooled": float(np.mean(paired["ratio_vs_pooled"] < 1.0)),
        "series_win_rate_vs_pooled": float(
            np.mean(series["geometric_rmse_ratio_vs_pooled"] < 1.0)
        ),
        "geometric_rmse_ratio_vs_last": point_last,
        "cluster_ci95_lo_vs_last": lo_last,
        "cluster_ci95_hi_vs_last": hi_last,
        "outer_win_rate_vs_last": float(np.mean(paired["ratio_vs_last"] < 1.0)),
        "series_win_rate_vs_last": float(
            np.mean(series["geometric_rmse_ratio_vs_last"] < 1.0)
        ),
        "fallback_rate": float(np.mean(paired["fallback_used"].astype(bool))),
    }


def _overall_and_class_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows = [_summary_row(paired, "all")]
    for asset_class, group in paired.groupby("asset_class", sort=True):
        rows.append(_summary_row(group, str(asset_class)))
    return pd.DataFrame(rows)


def _markdown_table(frame: pd.DataFrame, digits: int = 4) -> str:
    if frame.empty:
        return "_No rows._"
    clean = frame.copy()
    for col in clean.select_dtypes(include=[np.number]).columns:
        clean[col] = clean[col].map(
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
    divider = "| " + " | ".join(
        "-" * widths[j] for j in range(len(headers))
    ) + " |"
    body = [
        "| " + " | ".join(
            row[j].ljust(widths[j]) for j in range(len(headers))
        ) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    metadata = json.loads((run_dir / "run_metadata.json").read_text(encoding="utf-8"))
    decisions = pd.read_csv(run_dir / "decision_results.csv.gz")
    paired = _paired(decisions)
    series = _series_summary(paired)
    grouped = _overall_and_class_summary(paired)

    diagnostics = run_dir / "diagnostics"
    diagnostics.mkdir(parents=True, exist_ok=True)
    paired.to_csv(diagnostics / "paired_outer_results.csv", index=False)
    series.to_csv(diagnostics / "series_summary.csv", index=False)
    grouped.to_csv(diagnostics / "primary_summary.csv", index=False)

    overall = grouped.loc[grouped["group"].eq("all")].iloc[0]
    report = [
        "# Checkpoint 05 external financial panel",
        "",
        f"Source run: `{run_dir.as_posix()}`",
        "",
        "The dynamic rule was frozen before this panel was evaluated:",
        "`recency_hl3`. AAPL, SPY, and BTC-USD were excluded because they were",
        "used in CP04. No CP05 series was selected from forecast performance.",
        "",
        "## Primary result",
        "",
        f"Series-cluster geometric RMSE ratio versus pooled CV: **{overall['geometric_rmse_ratio_vs_pooled']:.4f}** ",
        f"(descriptive 95% series-cluster bootstrap interval ",
        f"[{overall['cluster_ci95_lo_vs_pooled']:.4f}, {overall['cluster_ci95_hi_vs_pooled']:.4f}]).",
        "",
        f"Series-cluster geometric RMSE ratio versus the newest tracked minimum: ",
        f"**{overall['geometric_rmse_ratio_vs_last']:.4f}** ",
        f"(descriptive 95% interval ",
        f"[{overall['cluster_ci95_lo_vs_last']:.4f}, {overall['cluster_ci95_hi_vs_last']:.4f}]).",
        "",
        "## Overall and by asset class",
        "",
        _markdown_table(grouped),
        "",
        "## Series-level results",
        "",
        _markdown_table(series),
        "",
        "## Interpretation rule",
        "",
        "This is an external validation stage, not a tuning stage. Do not change",
        "the half-life, branch selector, epsilon, spacing, orders, windows, or",
        "fallback rule based on these results. Financial series share common",
        "market shocks, so cluster intervals are sensitivity summaries rather",
        "than evidence of independent cross-sectional sampling.",
        "",
        f"Fallback rate: **{overall['fallback_rate']:.2%}**.",
        "",
        f"Frozen manifest timestamp: `{metadata['snapshot_manifest_updated_at']}`.",
        "",
    ]
    (run_dir / "checkpoint_report.md").write_text(
        "\n".join(report),
        encoding="utf-8",
    )
    print(f"Wrote {run_dir / 'checkpoint_report.md'}")
    print(f"Wrote diagnostics to {diagnostics}")


if __name__ == "__main__":
    main()
