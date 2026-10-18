"""Retrospective financial time-series illustration of pooled LOOCV.

Loads a user-provided CSV, never downloads market data or predicts prices.
Samples are treated as consecutive trading observations, not equal calendar
time steps. Multiple heterogeneous columns require explicit standardization.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .objective import PooledLOOCV
from .search import bounded_brent, dense_reference, multibracket_brent


def load_columns(csv_path: Path, columns: list[str], date_col: str | None,
                 transform: str, standardize: bool) -> tuple[np.ndarray, int]:
    """Read R comparable aligned series, R x N; do not pool raw units."""
    frame = pd.read_csv(csv_path)
    if len(set(columns)) != len(columns) or not columns:
        raise ValueError("pass one or more distinct --columns")
    needed = columns + ([date_col] if date_col else [])
    missing = [c for c in needed if c not in frame.columns]
    if missing:
        raise ValueError(f"missing CSV columns: {missing}")
    if date_col:
        frame = frame.assign(**{date_col: pd.to_datetime(frame[date_col])})
        frame = frame.sort_values(date_col)
        if frame[date_col].duplicated().any():
            raise ValueError("duplicate observation dates must be resolved first")
    data = frame[columns].apply(pd.to_numeric, errors="coerce").dropna().to_numpy(dtype=float)
    if len(data) < 8:
        raise ValueError("need at least eight complete, aligned observations")
    if transform == "log-level":
        if np.any(data <= 0):
            raise ValueError("log-level requires strictly positive values")
        data = np.log(data)
    elif transform == "log-return":
        if np.any(data <= 0):
            raise ValueError("log-return requires strictly positive values")
        data = np.diff(np.log(data), axis=0)
    elif transform != "level":
        raise ValueError("unknown transform")
    if len(columns) > 1 and not standardize:
        raise ValueError("pooling different financial columns requires --standardize")
    if standardize:
        std = data.std(axis=0, ddof=1)
        if np.any(std <= 0):
            raise ValueError("cannot standardize a constant column")
        data = (data - data.mean(axis=0)) / std
    return data.T, len(data)


def execute(csv_path: Path, columns: list[str], out_dir: Path, date_col: str | None,
            transform: str, standardize: bool) -> None:
    series, n = load_columns(csv_path, columns, date_col, transform, standardize)
    obj = PooledLOOCV(series, order=2)
    searches = [bounded_brent(obj), multibracket_brent(obj), dense_reference(obj)]
    selected = searches[1].best
    out_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "data_source": str(csv_path), "columns": columns, "n": n,
        "R": len(columns), "date_column": date_col, "transform": transform,
        "standardized": standardize, "smoothing_order": 2,
        "disclaimer": "retrospective PLS reconstruction, no forecast or backtest",
        "methods": [m.as_dict() for m in searches],
    }
    (out_dir / "financial_case.json").write_text(json.dumps(record, indent=2))
    grid = np.exp(np.linspace(-20, 35, 301))
    curve = [(lam, obj.smoothness(float(lam)), obj.score(float(lam))) for lam in grid]
    with (out_dir / "financial_loss_curve.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["lambda", "smoothness_s", "pooled_loocv_mse"])
        writer.writerows(curve)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
    fitted = obj.trend(selected.lam)
    for i, name in enumerate(columns):
        ax1.plot(series[i], label=f"{name} observed", alpha=0.45)
        ax1.plot(fitted[i], label=f"{name} smoothed")
    ax1.set_ylabel(transform + (" (standardized)" if standardize else ""))
    ax1.set_xlabel("Consecutive observed trading index")
    ax1.legend(fontsize=8, ncol=2)
    ax2.plot([c[1] for c in curve], [c[2] for c in curve])
    ax2.axvline(selected.s, linestyle="--", label="Selected pooled S")
    ax2.scatter([0, 1], [obj.score(0), obj.score(float("inf"))],
                label="Exact endpoints", s=24)
    ax2.set_xlabel("Normalized smoothness S")
    ax2.set_ylabel("Pooled LOOCV MSE")
    ax2.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "financial_reconstruction.png", dpi=150)
    plt.close(fig)
    print(f"Retrospective illustration saved to {out_dir}; selected S={selected.s:.6g}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=Path)
    parser.add_argument("--columns", nargs="+", required=True)
    parser.add_argument("--date-column", default=None)
    parser.add_argument("--transform", choices=("level", "log-level", "log-return"),
                        default="level")
    parser.add_argument("--standardize", action="store_true")
    parser.add_argument("--out-dir", type=Path,
                        default=Path("results/pooled_loocv_smoothness/finance"))
    args = parser.parse_args()
    execute(args.csv, args.columns, args.out_dir, args.date_column,
            args.transform, args.standardize)


if __name__ == "__main__":
    main()
