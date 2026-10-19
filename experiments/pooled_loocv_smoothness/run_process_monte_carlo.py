"""Manual seed replication of the nine curated pooled trend process examples.

Uses the SAME 11 feasible selectors as run_process_examples.py; this is a
mechanism-conditioned independent-seed study, NOT a new objective or solver.
Each seed shares underlying shocks across all mechanisms and nested R=1/R=3.
Observed-data tuning cannot access the simulated latent truth.

Compressed raw replicate shards are written atomically. The manifest permits
resuming completed chunks without re-running or duplicating saved seeds.
Heavy runs require explicit user commands; never launch automatically in CI.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.stats import t as student_t

from .run_process_examples import (
    DEFAULT_SEED, METHODS, make_examples, evaluate_example, _commit_sha,
)

METRICS = ("pool_mse", "pool_mae", "first_series_mse", "first_series_mae")
OUTPUT_FIELDS = (
    "replicate", "rng_seed", "case", "R", "method",
    *METRICS, "selected_lambda", "selected_s_nominal",
    "fitted_mu", "edf_total",
)
POOL_SIZES = (1, 3)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _validate(*, count: int, start: int, base_seed: int,
              chunk_size: int, n: int, scan_points: int,
              names: tuple[str, ...]) -> None:
    if count < 1 or start < 1 or base_seed < 0 or chunk_size < 1:
        raise ValueError("count/chunk-size >= 1, start >= 1, base-seed >= 0")
    if base_seed + start + count > np.iinfo(np.int64).max:
        raise ValueError("seed schedule exceeds supported integer range")
    if n < 32 or scan_points < 5:
        raise ValueError("n>=32, scan_points>=5 required")
    if not names or len(names) != len(set(names)):
        raise ValueError("select nonempty, unique cases")
    unknown = set(names) - set(make_examples(seed=DEFAULT_SEED, n=n))
    if unknown:
        raise ValueError("unknown cases: " + ", ".join(sorted(unknown)))


def _chunks(start: int, count: int, chunk_size: int):
    return [(first, min(first + chunk_size, start + count))
            for first in range(start, start + count, chunk_size)]


def _filename(first: int, stop: int) -> str:
    return f"rows_{first:08d}_{stop - 1:08d}.csv.gz"


def _atomic_json(path: Path, content: dict) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(content, indent=2, allow_nan=False) + "\n",
                   encoding="utf-8")
    os.replace(tmp, path)


def configuration(*, count: int, start: int, base_seed: int,
                  chunk_size: int, n: int, scan_points: int,
                  names: tuple[str, ...]) -> dict:
    return {
        "seed_start_inclusive": start,
        "seed_stop_exclusive": start + count,
        "base_seed": base_seed,
        "count": count,
        "chunk_size": chunk_size,
        "n": n,
        "d": 2,
        "scan_points": scan_points,
        "cases": list(names),
        "pool_sizes": list(POOL_SIZES),
        "methods": list(METHODS),
    }


def _draw_seed_rows(replicate: int, base_seed: int, n: int,
                    scan_points: int, names: tuple[str, ...]):
    rng_seed = base_seed + replicate
    examples = make_examples(seed=rng_seed, n=n)
    for name in names:
        case = examples[name]
        for r in POOL_SIZES:
            rows, fits = evaluate_example(case, r=r, scan_points=scan_points)
            for row in rows:
                residual_first = fits[row["method"]][0] - case.truth[0]
                yield {
                    "replicate": replicate, "rng_seed": rng_seed,
                    "case": name, "R": r, "method": row["method"],
                    "pool_mse": row["latent_trend_mse_EX_POST"],
                    "pool_mae": row["latent_trend_mae_EX_POST"],
                    "first_series_mse": float(np.mean(residual_first**2)),
                    "first_series_mae": float(np.mean(np.abs(residual_first))),
                    "selected_lambda": row["selected_lambda"],
                    "selected_s_nominal": row["selected_s_nominal"],
                    "fitted_mu": row["fitted_mu"],
                    "edf_total": row["edf_total"],
                }


def _write_chunk(out_dir: Path, first: int, stop: int, *, base_seed: int,
                 n: int, scan_points: int, names: tuple[str, ...]) -> None:
    final = out_dir / _filename(first, stop)
    temporary = out_dir / (final.name + ".partial")
    if final.exists():
        raise FileExistsError(f"refusing to overwrite finished shard {final}")
    try:
        with gzip.open(temporary, "wt", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=OUTPUT_FIELDS)
            writer.writeheader()
            for rep in range(first, stop):
                writer.writerows(
                    _draw_seed_rows(rep, base_seed, n, scan_points, names)
                )
        os.replace(temporary, final)
    finally:
        if temporary.exists():
            temporary.unlink()


def _mean_ci95(data: np.ndarray) -> tuple[float, float, float, float, float]:
    """Mean, SD, two-sided nominal 95% t interval, two-sided t p for mean=0.

    Independent units are entire RNG seed draws; paired differences are formed
    before invoking this. The interval is NOT multiplicity-adjusted.
    """
    x = np.asarray(data, dtype=float)
    if x.ndim != 1 or not len(x) or not np.isfinite(x).all():
        raise ValueError("nonempty finite 1D sample required")
    mean = float(np.mean(x))
    if len(x) == 1:
        return mean, float("nan"), float("nan"), float("nan"), float("nan")
    sd = float(np.std(x, ddof=1))
    if sd == 0:
        return mean, sd, mean, mean, 1.0 if mean == 0 else 0.0
    se = sd / np.sqrt(len(x))
    margin = float(student_t.ppf(0.975, len(x) - 1) * se)
    p = float(2 * student_t.sf(abs(mean / se), len(x) - 1))
    return mean, sd, mean - margin, mean + margin, p


def _holm_global(rows: list[dict]) -> None:
    """Exploratory 55 x 18 all-pairs family: adjust across ALL available pairs."""
    indexed = sorted(
        [(float(row["paired_t_p_uncorrected"]), i)
         for i, row in enumerate(rows)
         if row["paired_t_p_uncorrected"] is not None],
        key=lambda p: p[0]
    )
    n = len(indexed)
    previous = 0.
    for rank, (p, idx) in enumerate(indexed):
        previous = max(previous, min(1.0, (n - rank) * p))
        rows[idx]["paired_t_p_holm_all_processes"] = previous


def _load_matrix(out_dir: Path, cfg: dict):
    names, methods = cfg["cases"], cfg["methods"]
    count = cfg["count"]
    arr = np.full(
        (count, len(names), len(POOL_SIZES), len(methods), len(METRICS) + 3),
        np.nan, dtype=float
    )
    name_id = {name: i for i, name in enumerate(names)}
    method_id = {name: i for i, name in enumerate(methods)}
    columns = METRICS + ("selected_s_nominal", "fitted_mu", "edf_total")
    total = 0
    for first, stop in _chunks(cfg["seed_start_inclusive"],
                               count, cfg["chunk_size"]):
        file = out_dir / _filename(first, stop)
        if not file.is_file():
            raise FileNotFoundError(f"missing completed shard: {file}")
        with gzip.open(file, "rt", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != list(OUTPUT_FIELDS):
                raise ValueError(f"invalid field schema: {file}")
            for row in reader:
                replicate = int(row["replicate"])
                rng_seed = int(row["rng_seed"])
                if not first <= replicate < stop or rng_seed != cfg["base_seed"] + replicate:
                    raise ValueError(f"unexpected seed in {file}")
                slot = replicate - cfg["seed_start_inclusive"]
                try:
                    c, r, m = (name_id[row["case"]],
                               POOL_SIZES.index(int(row["R"])),
                               method_id[row["method"]])
                except (KeyError, ValueError) as exc:
                    raise ValueError(f"unexpected case/pool/method in {file}") from exc
                if not np.isnan(arr[slot, c, r, m, 0]):
                    raise ValueError(f"duplicate row in {file}: {row}")
                values = np.array([float(row[field]) for field in columns])
                if not np.isfinite(values).all():
                    raise ValueError(f"nonfinite result in {file}: {row}")
                arr[slot, c, r, m] = values
                total += 1
    expected = count * len(names) * len(POOL_SIZES) * len(methods)
    if total != expected or np.isnan(arr).any():
        raise ValueError(f"incomplete Monte Carlo grid: {total}/{expected}")
    return arr


def _write_csv(path: Path, data: list[dict]) -> None:
    if not data:
        raise ValueError("cannot export an empty summary")
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        with tmp.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def summarize_matrix(arr: np.ndarray, cfg: dict):
    names, methods = cfg["cases"], cfg["methods"]
    count = cfg["count"]
    summary = []
    paired = []
    pooling = []
    for ci, case in enumerate(names):
        for ri, r in enumerate(POOL_SIZES):
            x = arr[:, ci, ri, :, :]
            # An ex-post winner count is descriptive; ties get fractional credit.
            minima = np.min(x[:, :, 0], axis=1)
            ties = np.isclose(x[:, :, 0], minima[:, None], rtol=1e-12, atol=1e-14)
            fractional_wins = ties / np.sum(ties, axis=1, keepdims=True)
            for mi, method in enumerate(methods):
                mse, sd, lo, hi, _ = _mean_ci95(x[:, mi, 0])
                summary.append({
                    "case": case, "R": r, "method": method,
                    "n_independent_seeds": count,
                    "mean_pool_mse": mse, "sd_pool_mse": sd,
                    "mean_pool_mse_ci95_low_pointwise": lo,
                    "mean_pool_mse_ci95_high_pointwise": hi,
                    "median_pool_mse": float(np.median(x[:, mi, 0])),
                    "p90_pool_mse": float(np.quantile(x[:, mi, 0], 0.90)),
                    "mean_pool_mae": float(np.mean(x[:, mi, 1])),
                    "mean_first_series_mse": float(np.mean(x[:, mi, 2])),
                    "mean_first_series_mae": float(np.mean(x[:, mi, 3])),
                    "median_selected_s_nominal": float(np.median(x[:, mi, 4])),
                    "mean_fitted_mu": float(np.mean(x[:, mi, 5])),
                    "mean_edf_total": float(np.mean(x[:, mi, 6])),
                    "ex_post_seed_win_fraction": float(
                        np.mean(fractional_wins[:, mi])
                    ),
                    "mean_pool_mse_rank": 0,  # filled below
                })
            current = summary[-len(methods):]
            for rank, row in enumerate(sorted(current,
                                               key=lambda v: v["mean_pool_mse"]), 1):
                row["mean_pool_mse_rank"] = rank
            for ai, a in enumerate(methods):
                for bi in range(ai + 1, len(methods)):
                    b = methods[bi]
                    d = x[:, ai, 0] - x[:, bi, 0]
                    mean, sd, lo, hi, p = _mean_ci95(d)
                    paired.append({
                        "case": case, "R": r,
                        "method_A": a, "method_B": b,
                        "n_matched_independent_seeds": count,
                        "mean_mse_A_minus_B_negative_favors_A": mean,
                        "sd_paired_mse_difference": sd,
                        "ci95_low_pointwise": lo,
                        "ci95_high_pointwise": hi,
                        "fraction_seeds_A_better": float(np.mean(d < 0)),
                        "fraction_seeds_tied": float(np.mean(d == 0)),
                        "paired_t_p_uncorrected": p if np.isfinite(p) else None,
                        "paired_t_p_holm_all_processes": None,
                    })
        # Compare R3 against R1 for THE SAME FIRST SERIES and same seed.
        for mi, method in enumerate(methods):
            d = arr[:, ci, 1, mi, 2] - arr[:, ci, 0, mi, 2]
            mean, sd, lo, hi, p = _mean_ci95(d)
            pooling.append({
                "case": case, "method": method,
                "n_matched_independent_seeds": count,
                "mean_first_series_mse_R3_minus_R1_negative_favors_pooling": mean,
                "sd_paired_difference": sd,
                "ci95_low_pointwise": lo, "ci95_high_pointwise": hi,
                "fraction_seeds_pooling_helps_first_series": float(np.mean(d < 0)),
                "paired_t_p_uncorrected": p if np.isfinite(p) else None,
            })
    _holm_global(paired)
    return summary, paired, pooling


def run(*, out_dir: Path, count: int = 100, start: int = 1,
        base_seed: int = DEFAULT_SEED, chunk_size: int = 25,
        n: int = 80, scan_points: int = 31,
        names: tuple[str, ...] | None = None, resume: bool = False,
        preview: bool = False) -> dict:
    if names is None:
        names = tuple(make_examples(n=n))
    _validate(count=count, start=start, base_seed=base_seed,
              chunk_size=chunk_size, n=n,
              scan_points=scan_points, names=names)
    cfg = configuration(count=count, start=start, base_seed=base_seed,
                        chunk_size=chunk_size, n=n,
                        scan_points=scan_points, names=names)
    plan = {
        "status": "PLAN_ONLY_NO_SIMULATION" if preview else "IN_PROGRESS",
        "design": cfg,
        "expected_rows": count * len(names) * len(POOL_SIZES) * len(METHODS),
        "expected_chunks": len(_chunks(start, count, chunk_size)),
        "raw_shards_local_backup_required": True,
        "full_replications_independent": count,
        "scenario_and_nested_R_comparisons_paired_within_seed": True,
    }
    if preview:
        return plan
    out_dir = Path(out_dir)
    manifest_file = out_dir / "manifest.json"
    if resume:
        if not manifest_file.is_file():
            raise FileNotFoundError("cannot resume: no existing manifest")
        old = json.loads(manifest_file.read_text(encoding="utf-8"))
        if old["design"] != cfg:
            raise ValueError("resume settings do not match existing manifest")
        if old["status"] == "COMPLETE":
            raise ValueError("already COMPLETE: use a different seed window")
        plan = old
    else:
        if out_dir.exists() and any(out_dir.iterdir()):
            raise FileExistsError(f"refusing to overwrite {out_dir}")
        out_dir.mkdir(parents=True, exist_ok=True)
        plan.update({
            "created_utc": _utc_now(),
            "source_commit_at_start": _commit_sha(),
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "interpretation": [
                "Independent units are RNG seed draws, not method rows.",
                "All nine mechanisms and nested R use paired common random numbers.",
                "First series held fixed for pooling contrasts: R3 - R1 MSE.",
                "Multiple pairwise tests have a global Holm adjustment; intervals remain pointwise.",
                "The gallery may have informed mechanism/method selection: exploratory not independent confirmation.",
                "Synthetic realized latent truth appears ONLY in ex-post evaluation.",
                "This is retrospective reconstruction, NOT time-series h-step forecasting.",
                "Do not compare method raw CV/GCV/AICc/ML score values across criteria.",
                "Raw compressed replicates are user-local; commit compact audit summaries and manifest.",
            ],
        })
        _atomic_json(manifest_file, plan)
    chunks = _chunks(start, count, chunk_size)
    for i, (first, stop) in enumerate(chunks, 1):
        target = out_dir / _filename(first, stop)
        if not target.is_file():
            _write_chunk(out_dir, first, stop, base_seed=base_seed,
                         n=n, scan_points=scan_points, names=names)
        plan["finished_chunks"] = sum(
            (out_dir / _filename(a, b)).is_file() for a, b in chunks
        )
        plan["last_completed_utc"] = _utc_now()
        _atomic_json(manifest_file, plan)
        print(f"[PROCESS MC {i}/{len(chunks)}] seeds {first}..{stop - 1}: "
              f"{plan['finished_chunks']}/{len(chunks)} complete",
              flush=True)
    data = _load_matrix(out_dir, cfg)
    summary, paired, pooling = summarize_matrix(data, cfg)
    _write_csv(out_dir / "risk_by_process_method.csv", summary)
    _write_csv(out_dir / "paired_method_mse_differences.csv", paired)
    _write_csv(out_dir / "paired_pooling_first_series.csv", pooling)
    plan.update({
        "status": "COMPLETE",
        "completed_utc": _utc_now(),
        "finished_chunks": len(chunks),
        "actual_method_rows": int(data.shape[0] * data.shape[1] *
                                  data.shape[2] * data.shape[3]),
        "summary_rows": len(summary),
        "pairwise_rows": len(paired),
        "pooling_rows": len(pooling),
    })
    _atomic_json(manifest_file, plan)
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(
        "results/pooled_loocv_smoothness/process_examples/seed_study_001"
    ))
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--seed-start", type=int, default=1)
    parser.add_argument("--base-seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--chunk-size", type=int, default=25)
    parser.add_argument("--n", type=int, default=80)
    parser.add_argument("--scan-points", type=int, default=31)
    parser.add_argument("--cases", default="all")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args()
    names = (tuple(make_examples(n=args.n)) if args.cases == "all" else
             tuple(c.strip() for c in args.cases.split(",")))
    result = run(out_dir=args.out_dir, count=args.count, start=args.seed_start,
                 base_seed=args.base_seed, chunk_size=args.chunk_size,
                 n=args.n, scan_points=args.scan_points, names=names,
                 resume=args.resume, preview=args.preview)
    print(json.dumps({
        "status": result["status"],
        "independent_seeds": result["design"]["count"],
        "cases": result["design"]["cases"],
        "method_rows": result["expected_rows"],
        "output": str(args.out_dir),
        "summary_rows": result.get("summary_rows"),
        "pairwise_rows": result.get("pairwise_rows"),
    }, indent=2))


if __name__ == "__main__":
    main()
