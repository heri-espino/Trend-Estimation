from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Post-hoc mechanism diagnostics for CP05. This script explains "
            "where the external-panel failures come from; it does not retune "
            "or redefine the frozen CP05 test."
        )
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_05/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("No completed CP05 run found.")
    return Path(latest.read_text(encoding="utf-8").strip())


def _geomean(values: pd.Series) -> float:
    x = values.to_numpy(dtype=float)
    x = x[np.isfinite(x) & (x > 0.0)]
    if x.size == 0:
        return np.nan
    return float(np.exp(np.mean(np.log(x))))


def _order_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for order, group in paired.groupby("order", sort=True):
        rows.append(
            {
                "order": int(order),
                "n_outer": int(len(group)),
                "geometric_rmse_ratio_vs_pooled": _geomean(group["ratio_vs_pooled"]),
                "geometric_rmse_ratio_vs_last": _geomean(group["ratio_vs_last"]),
                "win_rate_vs_pooled": float(np.mean(group["ratio_vs_pooled"] < 1.0)),
                "win_rate_vs_last": float(np.mean(group["ratio_vs_last"] < 1.0)),
                "ratio_gt_5_rate": float(np.mean(group["ratio_vs_pooled"] > 5.0)),
                "ratio_gt_10_rate": float(np.mean(group["ratio_vs_pooled"] > 10.0)),
                "ratio_gt_100_rate": float(np.mean(group["ratio_vs_pooled"] > 100.0)),
                "median_abs_s_dynamic_minus_pooled": float(
                    np.median(np.abs(group["s_dynamic_minus_pooled"]))
                ),
                "max_dynamic_rmse": float(group["rmse_dynamic"].max()),
            }
        )
    return pd.DataFrame(rows)


def _tail_sensitivity(paired: pd.DataFrame) -> pd.DataFrame:
    ordered = paired.sort_values("log_ratio_vs_pooled", ascending=False).reset_index(drop=True)
    rows: list[dict] = []
    for remove_n in (0, 1, 3, 5, 10):
        kept = ordered.iloc[remove_n:].copy()
        rows.append(
            {
                "removed_worst_outer_blocks": remove_n,
                "n_outer_remaining": int(len(kept)),
                "geometric_rmse_ratio_vs_pooled": float(
                    np.exp(kept["log_ratio_vs_pooled"].mean())
                ),
                "geometric_rmse_ratio_vs_last": float(
                    np.exp(kept["log_ratio_vs_last"].mean())
                ),
            }
        )
    return pd.DataFrame(rows)


def _tail_concentration(paired: pd.DataFrame) -> pd.DataFrame:
    ordered = paired.sort_values("log_ratio_vs_pooled", ascending=False).reset_index(drop=True)
    positive_total = float(ordered.loc[ordered["log_ratio_vs_pooled"] > 0, "log_ratio_vs_pooled"].sum())
    rows: list[dict] = []
    for n in (1, 3, 5, 10, 20):
        top = ordered.head(n)
        rows.append(
            {
                "top_n_worst": n,
                "sum_log_ratio": float(top["log_ratio_vs_pooled"].sum()),
                "share_of_positive_log_loss": (
                    np.nan if positive_total <= 0 else
                    float(top["log_ratio_vs_pooled"].clip(lower=0).sum() / positive_total)
                ),
            }
        )
    return pd.DataFrame(rows)


def _worst_cases(paired: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "series", "asset_class", "outer_number", "test_start_date", "test_end_date",
        "order", "window", "s_dynamic", "s_last", "s_pooled",
        "rmse_dynamic", "rmse_last", "rmse_pooled",
        "ratio_vs_last", "ratio_vs_pooled",
    ]
    return (
        paired.sort_values("ratio_vs_pooled", ascending=False)
        .head(25)[columns]
        .reset_index(drop=True)
    )


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
    diagnostics = run_dir / "diagnostics"
    paired = pd.read_csv(diagnostics / "paired_outer_results.csv")

    by_order = _order_summary(paired)
    tail = _tail_sensitivity(paired)
    concentration = _tail_concentration(paired)
    worst = _worst_cases(paired)

    by_order.to_csv(diagnostics / "mechanism_by_order.csv", index=False)
    tail.to_csv(diagnostics / "mechanism_tail_sensitivity.csv", index=False)
    concentration.to_csv(diagnostics / "mechanism_tail_concentration.csv", index=False)
    worst.to_csv(diagnostics / "mechanism_worst_cases.csv", index=False)

    report = [
        "# CP05 post-hoc mechanism diagnostics",
        "",
        "These diagnostics are explanatory. CP05 remains a frozen external",
        "validation result and is not redefined or retuned here.",
        "",
        "## By selected difference order",
        "",
        _markdown_table(by_order),
        "",
        "## Sensitivity to the worst dynamic/pooled outer blocks",
        "",
        _markdown_table(tail),
        "",
        "## Concentration of positive log-loss",
        "",
        _markdown_table(concentration),
        "",
        "## Worst 25 dynamic-versus-pooled outer blocks",
        "",
        _markdown_table(worst),
        "",
        "## Diagnostic interpretation",
        "",
        "The external-panel failure is strongly concentrated in higher-order",
        "continuations. In particular, d=4 can turn modest changes in normalized",
        "smoothness into extremely different cubic extrapolations over a 60-step",
        "horizon. The recency average often regularizes the even more extreme",
        "newest-minimum forecast, which explains its strong comparison with",
        "`last`, but pooled forecast-CV frequently stays much closer to S=1 and",
        "avoids the same explosive paths.",
        "",
        "This motivates a new mechanism/stability study rather than post-hoc",
        "retuning of CP05.",
        "",
    ]
    (run_dir / "mechanism_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {run_dir / 'mechanism_report.md'}")


if __name__ == "__main__":
    main()
