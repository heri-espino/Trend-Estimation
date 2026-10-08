"""Manual reproducible pilot for Papers 1 and 2, using identical weighted F.

From the repository root:
    python -m experiments.smoothness_cv.run_weighted_surface_study --quick

No large experiment runs in CI. Does not change frozen CP01--CP08.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from .weighted_surface_study import LossWeighting, run_weighted_surface_study


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Weighted historical F: pooled vs tracked.")
    p.add_argument("--quick", action="store_true", help="Small, fast synthetic smoke experiment.")
    p.add_argument("--csv", type=Path, help="Optional local CSV data file.")
    p.add_argument("--column", default="observed", help="Numeric series column in CSV.")
    p.add_argument("--seed", type=int, default=13)
    p.add_argument("--n", type=int, default=150)
    p.add_argument("--noise-sd", type=float, default=0.35)
    p.add_argument("--orders", default="2", help="Comma-separated orders, e.g. 1,2,3.")
    p.add_argument("--window", type=int, default=32)
    p.add_argument("--horizon", type=int, default=3)
    p.add_argument("--stride", type=int, default=3)
    p.add_argument("--max-folds", type=int, default=18)
    p.add_argument("--grid-points", type=int, default=101)
    p.add_argument("--lookback", type=int, default=8)
    p.add_argument("--decay", type=float, default=.80)
    p.add_argument("--track-radius", type=float, default=.10)
    p.add_argument("--branch-min-support", type=int, default=3)
    p.add_argument("--branch-decision-k", type=int, default=3)
    p.add_argument("--branch-score-k", type=int, default=3)
    p.add_argument("--no-holdout", action="store_true")
    p.add_argument("--no-refine", action="store_true")
    p.add_argument("--output", type=Path, default=Path("results/weighted_surface_pilot"))
    args = p.parse_args(argv)
    if args.noise_sd < 0:
        p.error("--noise-sd must be nonnegative.")
    if args.csv:
        table = pd.read_csv(args.csv)
        if args.column not in table:
            p.error(f"Missing column {args.column!r} in CSV.")
        series = pd.to_numeric(table[args.column], errors="coerce").dropna().to_numpy(float)
        data_description = f"csv={args.csv};column={args.column}"
    else:
        n = 94 if args.quick else args.n
        t = np.arange(n, dtype=float)
        rng = np.random.default_rng(args.seed)
        latent = 8 + .025 * t + .85 * np.sin(t / 11) + .022 * np.maximum(t - n*.58, 0)
        series = latent + args.noise_sd * rng.standard_normal(n)
        data_description = f"synthetic_seed={args.seed};n={n};noise_sd={args.noise_sd}"

    methods = (
        LossWeighting("uniform_all", "uniform"),
        LossWeighting("recent_uniform", "uniform", lookback=args.lookback),
        LossWeighting("recent_linear", "linear", lookback=args.lookback),
        LossWeighting("recent_exponential", "exponential",
                      lookback=args.lookback, decay=args.decay),
    )
    orders = tuple(int(piece.strip()) for piece in args.orders.split(",") if piece.strip())
    study = run_weighted_surface_study(
        series, methods=methods, orders=orders,
        window=22 if args.quick else args.window,
        horizon=2 if args.quick else args.horizon,
        stride=4 if args.quick else args.stride,
        max_folds=6 if args.quick else args.max_folds,
        grid_points=21 if args.quick else args.grid_points,
        refine_pooled=not args.no_refine,
        track_radius=args.track_radius,
        branch_min_support=args.branch_min_support,
        branch_decision_k=args.branch_decision_k,
        branch_score_k=args.branch_score_k,
        holdout=not args.no_holdout,
    )
    args.output.mkdir(parents=True, exist_ok=True)
    study.summary.to_csv(args.output / "decisions_and_outer_test.csv", index=False)
    study.branches.to_csv(args.output / "tracked_local_minima.csv", index=False)
    for (method, d), surfaces in study.surfaces.items():
        filename = f"weighted_F_{method}_d{d}.csv"
        frame = pd.DataFrame(surfaces, columns=[f"S={s:.6f}" for s in study.grid])
        frame.insert(0, "origin", study.origins)
        frame.to_csv(args.output / filename, index=False)
    (args.output / "PROVENANCE.txt").write_text(
        f"{data_description}\n"
        f"orders={orders};horizon={study.horizon};window={22 if args.quick else args.window}\n"
        f"outer_test_isolation={not args.no_holdout}\n"
        f"surface_minima=grid_detected_not_certified\n"
        f"methods={methods}\n"
        f"branch_selection=historical_F_of_mean_last_K_s;no_val2\n"
        "WARNING: comparison uses one outer block and is a pilot, not publication evidence.\n",
        encoding="utf-8",
    )
    print(study.summary.to_string(index=False))
    print(f"\nPilot outputs: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
