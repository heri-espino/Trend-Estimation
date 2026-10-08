"""Controlled adjacent-origin matching diagnostic for the numerical paper.

The per-surface optimizer is not rerun. Known labeled minima isolate
correspondence behavior from root-recovery error. No forecasting labels
or validation scores are used to select assignments.

Run from the repository root:
  python experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py --preset smoke
  python experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py --preset paper
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from experiments.numerical_smoothness_selection.run_two_stage_order_validation import _match_branches


REGIMES = ("separated", "gradual_drift", "near_merger", "crossing", "birth_death")
EPSILONS = (0.03, 0.06, 0.10, 0.15)
N_TIMES = 42
OUT = Path("results/numerical_smoothness_selection/tracking_correspondence")


@dataclass(frozen=True)
class Candidate:
    label: str
    s: float


def _positions(regime: str, t: int, seed: int) -> dict[str, float]:
    """Ground-truth branch labels define identity; positions define observations."""
    u = t / (N_TIMES - 1)
    rng = np.random.default_rng(seed * 10000 + t + 37)
    wiggle = rng.normal(0.0, 0.002, size=4)

    if regime == "separated":
        return {
            "a": 0.20 + 0.02 * np.sin(2 * np.pi * u) + wiggle[0],
            "b": 0.50 + 0.02 * np.cos(2 * np.pi * u) + wiggle[1],
            "c": 0.80 + 0.02 * np.sin(3 * np.pi * u) + wiggle[2],
        }
    if regime == "gradual_drift":
        return {
            "a": 0.17 + 0.14 * u + wiggle[0],
            "b": 0.47 + 0.11 * u + wiggle[1],
            "c": 0.77 + 0.13 * u + wiggle[2],
        }
    if regime == "near_merger":
        # The first two labeled trajectories approach but do not cross.
        gap = 0.008 + 0.14 * abs(2 * u - 1)
        return {
            "a": 0.46 - gap / 2 + wiggle[0],
            "b": 0.46 + gap / 2 + wiggle[1],
            "c": 0.84 + wiggle[2],
        }
    if regime == "crossing":
        return {
            "a": 0.24 + 0.47 * u + wiggle[0],
            "b": 0.71 - 0.47 * u + wiggle[1],
            "c": 0.91 + 0.01 * np.sin(2 * np.pi * u) + wiggle[2],
        }
    if regime == "birth_death":
        result = {
            "b": 0.55 + 0.025 * np.sin(3 * np.pi * u) + wiggle[1],
            "c": 0.82 + wiggle[2],
        }
        if t < 26:
            result["a"] = 0.20 + 0.06 * u + wiggle[0]
        if t >= 15:
            result["d"] = 0.38 + 0.02 * (u - 0.35) + wiggle[3]
        return result
    raise ValueError(f"Unknown regime {regime}")


def _optimal_assignment(
    previous: dict[str, float],
    current: list[Candidate],
    *,
    epsilon: float,
) -> dict[str, tuple[int, float]]:
    """Exact *pairwise* max-cardinality, then minimum-distance matching.

    At most four minima occur in this benchmark; exhaustive enumeration
    avoids dependence on a separate assignment package. Unmatched
    branches are permitted. This is not a global multi-time tracker.
    """
    ids = sorted(previous)
    best_key: tuple | None = None
    best: dict[str, tuple[int, float]] = {}

    def dfs(i: int, used: frozenset[int], assignments: dict[str, tuple[int, float]]):
        nonlocal best_key, best
        if i == len(ids):
            distances = [v[1] for v in assignments.values()]
            mapping = tuple(assignments[k][0] if k in assignments else -1 for k in ids)
            key = (-len(assignments), round(sum(distances), 14), mapping)
            if best_key is None or key < best_key:
                best_key = key
                best = dict(assignments)
            return

        label = ids[i]
        dfs(i + 1, used, assignments)
        for j, candidate in enumerate(current):
            d = abs(previous[label] - candidate.s)
            if j in used or d > epsilon:
                continue
            assignments[label] = (j, float(d))
            dfs(i + 1, used | {j}, assignments)
            assignments.pop(label)

    dfs(0, frozenset(), {})
    return best


def _score_step(
    previous: dict[str, float],
    current: dict[str, float],
    *,
    epsilon: float,
    method: str,
) -> dict:
    candidates = [
        Candidate(label=k, s=float(v))
        for k, v in sorted(current.items(), key=lambda p: (p[1], p[0]))
    ]
    if method == "greedy":
        matches, _ = _match_branches(
            previous,
            [{"smoothness": p.s} for p in candidates],
            epsilon=epsilon,
        )
    elif method == "global_pairwise":
        matches = _optimal_assignment(previous, candidates, epsilon=epsilon)
    else:
        raise ValueError(method)
    expected = set(previous).intersection(current)
    correct = sum(
        1 for label, (idx, _) in matches.items()
        if label == candidates[idx].label
    )
    cost = sum(distance for idx, distance in matches.values())
    return {
        "matched": len(matches),
        "correct": correct,
        "wrong_identity": len(matches) - correct,
        "true_survivors": len(expected),
        "births": len(set(current) - set(previous)),
        "deaths": len(set(previous) - set(current)),
        "total_distance": float(cost),
    }


def _run_case(case: tuple[int, str, float]) -> list[dict]:
    seed, regime, epsilon = case
    rows: list[dict] = []
    for t in range(1, N_TIMES):
        previous = _positions(regime, t - 1, seed)
        current = _positions(regime, t, seed)
        for method in ("greedy", "global_pairwise"):
            rows.append({
                "seed": seed,
                "regime": regime,
                "epsilon": epsilon,
                "t": t,
                "method": method,
                **_score_step(previous, current, epsilon=epsilon, method=method),
            })
    return rows


def _summarize(frame: pd.DataFrame) -> pd.DataFrame:
    grouped = frame.groupby(["regime", "epsilon", "method"], sort=True)
    rows = []
    for (regime, epsilon, method), group in grouped:
        rows.append({
            "regime": regime,
            "epsilon": epsilon,
            "method": method,
            "n_transitions": int(len(group)),
            "n_true_survivals": int(group["true_survivors"].sum()),
            "n_matched": int(group["matched"].sum()),
            "n_correct": int(group["correct"].sum()),
            "n_wrong_identity": int(group["wrong_identity"].sum()),
            "n_birth_events": int(group["births"].sum()),
            "n_death_events": int(group["deaths"].sum()),
            "correct_survival_fraction": (
                float(group["correct"].sum() / max(1, group["true_survivors"].sum()))
            ),
            "fraction_steps_any_wrong_identity": float(
                np.mean(group["wrong_identity"].to_numpy() > 0)
            ),
            "mean_pairwise_distance_per_match": float(
                group["total_distance"].sum() / max(1, group["matched"].sum())
            ),
        })
    return pd.DataFrame(rows)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--preset", choices=("smoke", "paper"), default="smoke")
    p.add_argument("--output-dir", type=Path, default=None)
    args = p.parse_args()
    seeds = range(3) if args.preset == "smoke" else range(100)
    cases = list(product(seeds, REGIMES, EPSILONS))
    rows = [row for case in cases for row in _run_case(case)]
    frame = pd.DataFrame(rows)
    summary = _summarize(frame)
    folder = args.output_dir or (
        OUT / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
               + "_" + args.preset)
    )
    folder.mkdir(parents=True, exist_ok=True)
    frame.to_csv(folder / "paired_transitions.csv.gz", index=False, compression="gzip")
    summary.to_csv(folder / "summary.csv", index=False)
    metadata = {
        "study": "controlled_pairwise_minimum_correspondence",
        "preset": args.preset,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "n_seeds": len(seeds),
        "n_times": N_TIMES,
        "mechanisms": REGIMES,
        "track_epsilons": EPSILONS,
        "methods": ("greedy", "global_pairwise"),
        "conditioning": "previous identities reset to true labels at each step",
        "not_evaluated": (
            "per_surface_root_recovery",
            "multi_time_identity_error_accumulation",
            "automatic_birth_initialization",
            "forecasting_accuracy",
        ),
        "n_cases": len(cases),
        "n_rows": len(frame),
    }
    (folder / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    report = [
        "# Controlled numerical branch-correspondence benchmark",
        "",
        f"Preset: {args.preset}.",
        "",
        "Ground-truth labeled minima are supplied directly. This isolates",
        "one-step assignment from recovery errors and cumulative label drift.",
        "Greedy and exact max-cardinality/minimum-distance pairwise assignment",
        "are compared. Crossing paths need not be identifiable from position.",
        "",
        "## Summary",
        "",
        "```",
        summary.to_string(index=False),
        "```",
        "",
        "Do not report these as accuracy of full multi-origin tracking.",
        "",
    ]
    (folder / "checkpoint_report.md").write_text(
        "\n".join(report), encoding="utf-8"
    )
    (OUT / "LATEST.txt").write_text(folder.as_posix() + "\n", encoding="utf-8")
    print(f"{len(cases)} cases, {len(frame)} method-transition rows")
    print(summary.to_string(index=False))
    print(f"Saved to {folder}")


if __name__ == "__main__":
    main()
