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
        description="Analyze CP06 order-stability mechanism results."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_06/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("No completed CP06 run found.")
    return Path(latest.read_text(encoding="utf-8").strip())


def _geomean(x: pd.Series) -> float:
    values = x.to_numpy(dtype=float)
    values = values[np.isfinite(values) & (values > 0.0)]
    if values.size == 0:
        return np.nan
    return float(np.exp(np.mean(np.log(values))))


def _paired(decisions: pd.DataFrame) -> pd.DataFrame:
    keys = [
        "series", "asset_class", "order_set", "outer_number",
        "test_start_date", "test_end_date",
    ]
    dynamic = decisions.loc[
        decisions["rule"].eq("recency_hl3"),
        keys + ["level_rmse", "fallback_used", "order", "window", "selected_s"],
    ].rename(columns={"level_rmse": "rmse_dynamic", "selected_s": "s_dynamic"})
    last = decisions.loc[
        decisions["rule"].eq("last"),
        keys + ["level_rmse", "selected_s"],
    ].rename(columns={"level_rmse": "rmse_last", "selected_s": "s_last"})
    pooled = decisions.loc[
        decisions["rule"].eq("pooled_cv_same_config"),
        keys + ["level_rmse", "selected_s"],
    ].rename(columns={"level_rmse": "rmse_pooled", "selected_s": "s_pooled"})
    out = dynamic.merge(last, on=keys, validate="one_to_one")
    out = out.merge(pooled, on=keys, validate="one_to_one")
    out["ratio_vs_last"] = out["rmse_dynamic"] / out["rmse_last"]
    out["ratio_vs_pooled"] = out["rmse_dynamic"] / out["rmse_pooled"]
    out["log_ratio_vs_last"] = np.log(out["ratio_vs_last"])
    out["log_ratio_vs_pooled"] = np.log(out["ratio_vs_pooled"])
    return out


def _cluster_ci(frame: pd.DataFrame, column: str) -> tuple[float, float, float]:
    per_series = (
        frame.groupby("series", sort=True)[column]
        .mean()
        .dropna()
        .to_numpy(dtype=float)
    )
    if per_series.size == 0:
        return np.nan, np.nan, np.nan
    point = float(np.exp(np.mean(per_series)))
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    draws = np.empty(BOOTSTRAP_REPS, dtype=float)
    n = len(per_series)
    for i in range(BOOTSTRAP_REPS):
        sample = per_series[rng.integers(0, n, size=n)]
        draws[i] = np.exp(np.mean(sample))
    lo, hi = np.quantile(draws, [0.025, 0.975])
    return point, float(lo), float(hi)


def _series_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for (asset_class, series, order_set), group in paired.groupby(
        ["asset_class", "series", "order_set"],
        sort=True,
    ):
        rows.append(
            {
                "asset_class": asset_class,
                "series": series,
                "order_set": order_set,
                "n_outer": int(len(group)),
                "geometric_ratio_vs_pooled": _geomean(group["ratio_vs_pooled"]),
                "geometric_ratio_vs_last": _geomean(group["ratio_vs_last"]),
                "win_rate_vs_pooled": float(np.mean(group["ratio_vs_pooled"] < 1.0)),
                "win_rate_vs_last": float(np.mean(group["ratio_vs_last"] < 1.0)),
                "fallback_rate": float(np.mean(group["fallback_used"].astype(bool))),
            }
        )
    return pd.DataFrame(rows)


def _order_set_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for order_set, group in paired.groupby("order_set", sort=False):
        point_pool, lo_pool, hi_pool = _cluster_ci(group, "log_ratio_vs_pooled")
        point_last, lo_last, hi_last = _cluster_ci(group, "log_ratio_vs_last")
        series = _series_summary(group)
        rows.append(
            {
                "order_set": order_set,
                "n_series": int(group["series"].nunique()),
                "n_outer": int(len(group)),
                "geometric_ratio_vs_pooled": point_pool,
                "ci95_lo_vs_pooled": lo_pool,
                "ci95_hi_vs_pooled": hi_pool,
                "outer_win_rate_vs_pooled": float(np.mean(group["ratio_vs_pooled"] < 1.0)),
                "series_win_rate_vs_pooled": float(
                    np.mean(series["geometric_ratio_vs_pooled"] < 1.0)
                ),
                "ratio_gt_5_rate": float(np.mean(group["ratio_vs_pooled"] > 5.0)),
                "ratio_gt_10_rate": float(np.mean(group["ratio_vs_pooled"] > 10.0)),
                "ratio_gt_100_rate": float(np.mean(group["ratio_vs_pooled"] > 100.0)),
                "max_ratio_vs_pooled": float(group["ratio_vs_pooled"].max()),
                "geometric_ratio_vs_last": point_last,
                "ci95_lo_vs_last": lo_last,
                "ci95_hi_vs_last": hi_last,
                "outer_win_rate_vs_last": float(np.mean(group["ratio_vs_last"] < 1.0)),
                "series_win_rate_vs_last": float(
                    np.mean(series["geometric_ratio_vs_last"] < 1.0)
                ),
                "fallback_rate": float(np.mean(group["fallback_used"].astype(bool))),
            }
        )
    return pd.DataFrame(rows)


def _asset_class_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for (order_set, asset_class), group in paired.groupby(
        ["order_set", "asset_class"],
        sort=True,
    ):
        rows.append(
            {
                "order_set": order_set,
                "asset_class": asset_class,
                "n_series": int(group["series"].nunique()),
                "n_outer": int(len(group)),
                "geometric_ratio_vs_pooled": float(
                    np.exp(group["log_ratio_vs_pooled"].mean())
                ),
                "geometric_ratio_vs_last": float(
                    np.exp(group["log_ratio_vs_last"].mean())
                ),
                "win_rate_vs_pooled": float(np.mean(group["ratio_vs_pooled"] < 1.0)),
                "win_rate_vs_last": float(np.mean(group["ratio_vs_last"] < 1.0)),
                "ratio_gt_10_rate": float(np.mean(group["ratio_vs_pooled"] > 10.0)),
            }
        )
    return pd.DataFrame(rows)


def _selected_order_summary(paired: pd.DataFrame) -> pd.DataFrame:
    out = (
        paired.groupby(["order_set", "order"], dropna=False)
        .size()
        .rename("n_outer")
        .reset_index()
    )
    totals = out.groupby("order_set")["n_outer"].transform("sum")
    out["selection_rate"] = out["n_outer"] / totals
    return out


def _restriction_comparison(paired: pd.DataFrame) -> pd.DataFrame:
    keys = ["series", "asset_class", "outer_number", "test_start_date", "test_end_date"]
    baseline = paired.loc[
        paired["order_set"].eq("d1234"),
        keys + ["rmse_dynamic"],
    ].rename(columns={"rmse_dynamic": "rmse_dynamic_d1234"})
    rows: list[pd.DataFrame] = []
    for order_set in ("d123", "d12", "d2"):
        if order_set not in set(paired["order_set"]):
            continue
        current = paired.loc[
            paired["order_set"].eq(order_set),
            keys + ["rmse_dynamic"],
        ].merge(baseline, on=keys, validate="one_to_one")
        current["order_set"] = order_set
        current["dynamic_rmse_ratio_vs_d1234"] = (
            current["rmse_dynamic"] / current["rmse_dynamic_d1234"]
        )
        rows.append(current)
    if not rows:
        return pd.DataFrame()
    combined = pd.concat(rows, ignore_index=True)
    summary_rows: list[dict] = []
    for order_set, group in combined.groupby("order_set", sort=False):
        summary_rows.append(
            {
                "order_set": order_set,
                "n_outer": int(len(group)),
                "geometric_dynamic_rmse_ratio_vs_d1234": _geomean(
                    group["dynamic_rmse_ratio_vs_d1234"]
                ),
                "win_rate_vs_d1234_dynamic": float(
                    np.mean(group["dynamic_rmse_ratio_vs_d1234"] < 1.0)
                ),
            }
        )
    return pd.DataFrame(summary_rows)


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
    widths = [max(len(headers[j]), *(len(row[j]) for row in rows)) for j in range(len(headers))]
    header = "| " + " | ".join(headers[j].ljust(widths[j]) for j in range(len(headers))) + " |"
    divider = "| " + " | ".join("-" * widths[j] for j in range(len(headers))) + " |"
    body = [
        "| " + " | ".join(row[j].ljust(widths[j]) for j in range(len(headers))) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    metadata = json.loads((run_dir / "run_metadata.json").read_text(encoding="utf-8"))
    if metadata.get("study_type") != "post_hoc_mechanism_not_confirmation":
        raise RuntimeError("Unexpected CP06 study type.")
    if metadata.get("cp05_external_test_blocks_rescored", True):
        raise RuntimeError("CP06 must not rescore the CP05 external test blocks.")

    decisions = pd.read_csv(run_dir / "decision_results.csv.gz")
    paired = _paired(decisions)
    order_sets = _order_set_summary(paired)
    asset_classes = _asset_class_summary(paired)
    selected_orders = _selected_order_summary(paired)
    restrictions = _restriction_comparison(paired)
    series = _series_summary(paired)

    diagnostics = run_dir / "diagnostics"
    diagnostics.mkdir(parents=True, exist_ok=True)
    paired.to_csv(diagnostics / "paired_outer_results.csv", index=False)
    order_sets.to_csv(diagnostics / "order_set_summary.csv", index=False)
    asset_classes.to_csv(diagnostics / "asset_class_summary.csv", index=False)
    selected_orders.to_csv(diagnostics / "selected_order_summary.csv", index=False)
    restrictions.to_csv(diagnostics / "restriction_vs_d1234.csv", index=False)
    series.to_csv(diagnostics / "series_summary.csv", index=False)

    report = [
        "# Checkpoint 06 order-stability mechanism report",
        "",
        f"Source run: `{run_dir.as_posix()}`",
        "",
        "CP06 is explicitly post-hoc and explanatory. It uses earlier historical",
        "outer blocks and does not rescore the four CP05 external-test blocks.",
        "",
        "## Order-set comparison",
        "",
        _markdown_table(order_sets),
        "",
        "## Direct effect of restricting orders on the dynamic forecast",
        "",
        _markdown_table(restrictions),
        "",
        "## Selected-order frequencies",
        "",
        _markdown_table(selected_orders),
        "",
        "## By asset class",
        "",
        _markdown_table(asset_classes),
        "",
        "## Interpretation boundary",
        "",
        "Use this checkpoint to identify whether high-order polynomial",
        "continuation is the mechanism behind the CP05 tail failures. Do not",
        "present a better-performing post-hoc order set as independently",
        "validated. Any revised forecasting specification must next be frozen",
        "and tested prospectively in controlled simulations or new data.",
        "",
    ]
    (run_dir / "checkpoint_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {run_dir / 'checkpoint_report.md'}")
    print(f"Wrote diagnostics to {diagnostics}")


if __name__ == "__main__":
    main()
