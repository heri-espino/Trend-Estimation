from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze CP04 dynamic tracked-branch development results."
    )
    parser.add_argument("--run-dir", type=Path, default=None)
    return parser.parse_args()


def _resolve_run_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    latest = Path("results/smoothness_cv/checkpoint_04/LATEST.txt")
    if not latest.exists():
        raise FileNotFoundError("No completed Checkpoint 04 run was found.")
    return Path(latest.read_text(encoding="utf-8").strip())


def _geometric_mean(values: pd.Series) -> float:
    x = values.to_numpy(dtype=float)
    x = x[np.isfinite(x) & (x > 0.0)]
    if x.size == 0:
        return np.nan
    return float(np.exp(np.mean(np.log(x))))


def _markdown_table(frame: pd.DataFrame, digits: int = 4) -> str:
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


def _paired_table(decisions: pd.DataFrame, metric: str) -> pd.DataFrame:
    keys = ["series", "outer_number", "test_start_date", "test_end_date"]
    baseline_last = decisions.loc[
        decisions["rule"].eq("last"),
        keys + [metric],
    ].rename(columns={metric: "loss_last"})
    baseline_pooled = decisions.loc[
        decisions["rule"].eq("pooled_cv_same_config"),
        keys + [metric],
    ].rename(columns={metric: "loss_pooled"})

    dynamic = decisions.loc[
        ~decisions["rule"].isin(["last", "pooled_cv_same_config"])
    ].copy()
    dynamic = dynamic.merge(baseline_last, on=keys, validate="many_to_one")
    dynamic = dynamic.merge(baseline_pooled, on=keys, validate="many_to_one")
    dynamic["ratio_to_last"] = dynamic[metric] / dynamic["loss_last"]
    dynamic["ratio_to_pooled"] = dynamic[metric] / dynamic["loss_pooled"]
    dynamic["rmsfe_ratio_to_last"] = dynamic["ratio_to_last"]
    dynamic["rmsfe_ratio_to_pooled"] = dynamic["ratio_to_pooled"]
    return dynamic


def _rule_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for rule, group in paired.groupby("rule", sort=False):
        rows.append(
            {
                "rule": rule,
                "n_outer": int(len(group)),
                "geometric_rmsfe_vs_last": _geometric_mean(
                    group["rmsfe_ratio_to_last"]
                ),
                "geometric_rmsfe_vs_pooled": _geometric_mean(
                    group["rmsfe_ratio_to_pooled"]
                ),
                "win_rate_vs_last": float(np.mean(group["ratio_to_last"] < 1.0)),
                "win_rate_vs_pooled": float(
                    np.mean(group["ratio_to_pooled"] < 1.0)
                ),
                "median_abs_s_minus_current": float(
                    np.median(np.abs(group["s_minus_current"]))
                ),
                "mean_selected_s": float(group["selected_s"].mean()),
            }
        )
    out = pd.DataFrame(rows)
    if not out.empty:
        out = out.sort_values(
            ["geometric_rmsfe_vs_last", "geometric_rmsfe_vs_pooled", "rule"]
        ).reset_index(drop=True)
        out.insert(0, "development_rank", np.arange(1, len(out) + 1))
    return out


def _by_series_summary(paired: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for (series, rule), group in paired.groupby(["series", "rule"], sort=False):
        rows.append(
            {
                "series": series,
                "rule": rule,
                "n_outer": int(len(group)),
                "geometric_rmsfe_vs_last": _geometric_mean(
                    group["rmsfe_ratio_to_last"]
                ),
                "geometric_rmsfe_vs_pooled": _geometric_mean(
                    group["rmsfe_ratio_to_pooled"]
                ),
                "win_rate_vs_last": float(np.mean(group["ratio_to_last"] < 1.0)),
                "win_rate_vs_pooled": float(
                    np.mean(group["ratio_to_pooled"] < 1.0)
                ),
            }
        )
    return pd.DataFrame(rows).sort_values(["series", "rule"]).reset_index(drop=True)


def _baseline_summary(decisions: pd.DataFrame, metric: str) -> pd.DataFrame:
    frame = decisions.loc[
        decisions["rule"].isin(["last", "pooled_cv_same_config"])
    ].copy()
    rows: list[dict] = []
    for rule, group in frame.groupby("rule", sort=False):
        rows.append(
            {
                "rule": rule,
                "n_outer": int(len(group)),
                "geometric_loss": _geometric_mean(group[metric]),
                "mean_selected_s": float(group["selected_s"].mean()),
                "median_selected_s": float(group["selected_s"].median()),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    args = parse_args()
    run_dir = _resolve_run_dir(args.run_dir)
    metadata = json.loads((run_dir / "run_metadata.json").read_text(encoding="utf-8"))
    if metadata.get("confirmation_region_used", True):
        raise RuntimeError("CP04 development analysis must not use confirmation blocks.")

    decisions = pd.read_csv(run_dir / "decision_results.csv")
    metric = (
        "level_rmse"
        if metadata["selection_metric"] == "level_rmse"
        else "log_rmse"
    )
    paired = _paired_table(decisions, metric)
    rule_summary = _rule_summary(paired)
    by_series = _by_series_summary(paired)
    baselines = _baseline_summary(decisions, metric)

    diagnostics = run_dir / "diagnostics"
    diagnostics.mkdir(parents=True, exist_ok=True)
    paired.to_csv(diagnostics / "paired_dynamic_rules.csv", index=False)
    rule_summary.to_csv(diagnostics / "rule_summary.csv", index=False)
    by_series.to_csv(diagnostics / "rule_summary_by_series.csv", index=False)
    baselines.to_csv(diagnostics / "baseline_summary.csv", index=False)

    report = [
        "# Checkpoint 04 development report",
        "",
        f"Source run: {run_dir.as_posix()}",
        "",
        "This is a development-only comparison. The latest confirmation blocks",
        "remain untouched and must not be inspected before the dynamic rule is",
        "frozen.",
        "",
        "## Dynamic-rule ranking",
        "",
        "Geometric RMSFE ratios below one favor the dynamic rule over the named",
        "baseline. Ranking is descriptive and is used only to freeze the later",
        "confirmatory specification.",
        "",
        _markdown_table(rule_summary),
        "",
        "## Baselines",
        "",
        _markdown_table(baselines),
        "",
        "## By-series diagnostics",
        "",
        _markdown_table(by_series),
        "",
        "## Freeze discipline",
        "",
        "Do not run the reserved confirmation region yet. First inspect this",
        "development run, choose the final K/half-life rule family, and record",
        "that choice in CP04_DYNAMIC_BRANCH_RULES.md. The confirmation blocks",
        "must then be evaluated once under that frozen specification.",
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
