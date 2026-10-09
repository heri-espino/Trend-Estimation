"""New prospective protocol shared by Paper 1 and Paper 2.

For each order d and predeclared temporal weighting scheme m:
  - produce *causally completed* horizon-h fold losses L_t(S);
  - form F_t^(m)(S) from past and present completed folds only;
  - Paper 1 minimizes the latest F_t^(m) globally;
  - Paper 2 finds and tracks all *grid-detected* local minima of F_t^(m)
    and chooses a persistent branch without a second validation block.

An untouched outer holdout is used only to score final forecasts.
Legacy CP01--CP08 runs and older two-stage labs are NOT changed.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment

from experiments.smoothness_cv.pooled_lab import (
    all_grid_fold_losses,
    chronological_origins,
    fit_window_forecast,
    fold_loss_at_lambda,
    select_from_grid,
)
from trend_estimation.core.smoothness import smoothness_to_lambda
from trend_estimation.forecasting.objectives import prepare_rolling_pure_forecast_objective
from trend_estimation.validation.rolling_origin import RollingOriginSplit
from trend_estimation.validation.time_weights import make_time_weights


@dataclass(frozen=True)
class LossWeighting:
    """One preregistered way to aggregate *forecast losses*, never S values.

    lookback=None includes every completed origin up to the current one.
    Exponential decay applies across retained **origins**, not calendar time.
    """
    name: str
    scheme: str = "uniform"  # uniform, linear, exponential
    lookback: int | None = None
    decay: float = 0.85

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("The weighting method needs a name.")
        if self.scheme not in {"uniform", "linear", "exponential"}:
            raise ValueError("Invalid weighting scheme.")
        if self.lookback is not None and self.lookback < 1:
            raise ValueError("lookback must be positive or None.")
        if self.scheme == "exponential" and not (0 < self.decay <= 1):
            raise ValueError("Exponential decay must be in (0, 1].")

    def weights(self, n_available: int) -> tuple[int, np.ndarray]:
        """Return start index and weights in oldest-to-newest order."""
        self.validate()
        if n_available < 1:
            raise ValueError("At least one completed fold is required.")
        start = 0 if self.lookback is None else max(0, n_available - self.lookback)
        weights = make_time_weights(
            n_available - start, scheme=self.scheme, decay=self.decay
        )
        return start, weights


def weighted_surface_history(
    fold_losses: np.ndarray, method: LossWeighting
) -> np.ndarray:
    """Build each F_t from completed L_u, u <= t; no look-ahead.

    The input rows must already be sorted by historical origin, and all
    target blocks corresponding to supplied rows must have finished.
    """
    values = np.asarray(fold_losses, dtype=float)
    if values.ndim != 2 or 0 in values.shape or not np.all(np.isfinite(values)):
        raise ValueError("Expected a finite, non-empty (folds, grid) loss matrix.")
    if np.any(values < 0):
        raise ValueError("Forecast squared-error losses must be nonnegative.")
    result = np.empty_like(values)
    for index in range(len(values)):
        start, weights = method.weights(index + 1)
        result[index] = weights @ values[start:index + 1]
    return result


def grid_local_minima(grid: np.ndarray, losses: np.ndarray) -> list[tuple[float, float]]:
    """Report all strict-grid valleys plus admissible endpoint minima.

    Plateau ties are deduplicated toward the lowest S. These are grid
    candidates, *not* certified stationary roots or all true local minima.
    """
    grid = np.asarray(grid, dtype=float)
    losses = np.asarray(losses, dtype=float)
    if grid.ndim != 1 or losses.shape != grid.shape or grid.size < 3:
        raise ValueError("Need matching 1D grid and loss arrays (>=3 points).")
    if np.any(np.diff(grid) <= 0) or not np.all(np.isfinite(losses)):
        raise ValueError("Grid must increase and losses must be finite.")
    selected: list[tuple[float, float]] = []
    for i, val in enumerate(losses):
        left = losses[i - 1] if i else np.inf
        right = losses[i + 1] if i + 1 < len(losses) else np.inf
        is_valley = (
            val < right if i == 0 else
            val < left if i + 1 == len(losses) else
            val <= left and val <= right and (val < left or val < right)
        )
        if is_valley:
            if selected and i > 0 and np.isclose(
                selected[-1][1], val, atol=1e-12, rtol=1e-12
            ) and np.isclose(selected[-1][0], grid[i - 1]):
                continue
            selected.append((float(grid[i]), float(val)))
    return selected


def track_grid_branches(
    grid: np.ndarray,
    surfaces: np.ndarray,
    *,
    radius: float = 0.10,
) -> pd.DataFrame:
    """One-to-one maximum-cardinality matching across adjacent surfaces.

    A newly appearing valley starts a branch. A disappearing valley retires
    its branch. Matching distance is in normalized S, not in lambda.
    Assignment maximizes the number of feasible matches before minimizing
    total S distance. Identities remain ambiguous at crossings.
    """
    if not (0 <= radius <= 1):
        raise ValueError("radius must be in [0,1].")
    curves = np.asarray(surfaces, dtype=float)
    if curves.ndim != 2 or curves.shape[1] != len(grid):
        raise ValueError("surfaces must have shape (time, smoothness grid).")
    records: list[dict] = []
    previous: list[tuple[int, float]] = []
    next_id = 0
    for time_index, curve in enumerate(curves):
        minima = grid_local_minima(grid, curve)
        matches: dict[int, int] = {}  # current minimum index -> branch id
        if previous and minima:
            distances = np.abs(
                np.subtract.outer(
                    np.asarray([item[1] for item in previous]),
                    np.asarray([item[0] for item in minima]),
                )
            )
            nr, nc = distances.shape
            # All previous branches can be left unmatched via their private
            # dummy columns. A high dummy cost maximizes feasible matches;
            # the finite distance breaks ties among equal-cardinality matches.
            penalty = float(nr + nc + 2)
            costs = np.full((nr, nc + nr), penalty * 100.0)
            costs[:, :nc] = np.where(distances <= radius, distances, penalty * 100.0)
            for i in range(nr):
                costs[i, nc + i] = penalty
            rows, cols = linear_sum_assignment(costs)
            for old, new in zip(rows, cols):
                if new < nc and distances[old, new] <= radius:
                    matches[int(new)] = previous[int(old)][0]
        current = []
        for index, (s, f) in enumerate(minima):
            if index in matches:
                branch_id = matches[index]
            else:
                branch_id = next_id
                next_id += 1
            records.append({
                "step": int(time_index),
                "branch": int(branch_id),
                "s_local": float(s),
                "F_local": float(f),
            })
            current.append((branch_id, s))
        previous = current
    return pd.DataFrame(records, columns=["step", "branch", "s_local", "F_local"])


def select_tracked_branch(
    records: pd.DataFrame,
    surfaces: np.ndarray,
    grid: np.ndarray,
    *,
    min_support: int = 3,
    decision_k: int = 3,
    score_k: int = 3,
) -> tuple[float, int | None, float, int]:
    """Choose active branch by recent *historical F*; then mean last K S.

    F is scored at the *actual operational S* produced by mean-K, using
    linear interpolation of the precomputed grid. No Val2 is required.
    Active branches with sufficient consecutive support are preferred.
    When none qualify, fall back to available active branches. The loss
    history and policy are fitted on completed inner folds, never outer test.
    """
    if min(min_support, decision_k, score_k) < 1:
        raise ValueError("Support and lookback parameters must be positive.")
    if records.empty:
        idx = int(np.argmin(surfaces[-1]))
        return float(grid[idx]), None, float(surfaces[-1, idx]), 0

    last_step = len(surfaces) - 1
    active = records[records["step"] == last_step]
    if active.empty:
        idx = int(np.argmin(surfaces[-1]))
        return float(grid[idx]), None, float(surfaces[-1, idx]), 0

    proposals = []
    for branch_id in active["branch"].unique():
        history = records[records["branch"] == branch_id].sort_values("step")
        last = history.tail(decision_k)
        candidate = float(last["s_local"].mean())
        # Evaluate the actual mean-K rule at each historical step where this
        # branch existed, always using only its own S history available then.
        scores = []
        for p in range(len(history)):
            row = history.iloc[max(0, p - decision_k + 1):p + 1]
            s_operational = float(row["s_local"].mean())
            step = int(history.iloc[p]["step"])
            scores.append(float(np.interp(s_operational, grid, surfaces[step])))
        score = float(np.mean(scores[-score_k:]))
        proposals.append((
            int(len(history) >= min_support),
            score,
            -int(len(history)),
            candidate,
            int(branch_id),
            int(len(history)),
        ))

    if any(item[0] == 1 for item in proposals):
        proposals = [item for item in proposals if item[0] == 1]
    _, score, _, smoothness, branch_id, support = min(
        proposals, key=lambda item: (item[1], item[2], item[3], item[4])
    )
    return smoothness, branch_id, score, support


@dataclass
class WeightedSurfaceStudy:
    """Same per-origin loss data, two genuinely different decision rules."""
    summary: pd.DataFrame
    branches: pd.DataFrame
    surfaces: dict[tuple[str, int], np.ndarray]
    grid: np.ndarray
    origins: np.ndarray
    selected_origin: int
    horizon: int


def run_weighted_surface_study(
    observed,
    *,
    methods: tuple[LossWeighting, ...] = (
        LossWeighting("uniform_all", "uniform", lookback=None),
        LossWeighting("recent_uniform", "uniform", lookback=8),
        LossWeighting("recent_linear", "linear", lookback=8),
        LossWeighting("recent_exponential", "exponential", lookback=8, decay=0.8),
    ),
    orders: tuple[int, ...] = (2,),
    window: int = 30,
    horizon: int = 3,
    stride: int = 3,
    max_folds: int = 18,
    grid_points: int = 101,
    refine_pooled: bool = True,
    track_radius: float = 0.10,
    branch_min_support: int = 3,
    branch_decision_k: int = 3,
    branch_score_k: int = 3,
    holdout: bool = True,
    precomputed_grid_losses: dict[int, np.ndarray] | None = None,
) -> WeightedSurfaceStudy:
    """Compare Paper 1 pooled and Paper 2 tracking on identical historical folds.

    A method specifies weighting of F curves, *not* weighting of S.
    Paper 2 finds local minima of each method-specific rolling F and matches
    their positions; the post-tracking mean-K is an independent decision map.
    Orders and methods are evaluated separately, not secretly retuned by
    the untouched test block. Comparing candidate (method,d) choices using
    their outer-test errors is prohibited.
    """
    y = np.asarray(observed, dtype=float)
    if y.ndim != 1 or y.size == 0 or not np.all(np.isfinite(y)):
        raise ValueError("observed must be a finite one-dimensional series.")
    if not methods or len({method.name for method in methods}) != len(methods):
        raise ValueError("Methods must be nonempty with unique names.")
    if not orders or any(d < 1 or d >= window for d in orders):
        raise ValueError("All orders must satisfy 1 <= d < window.")
    if grid_points < 11 or grid_points > 501:
        raise ValueError("grid_points must be between 11 and 501.")
    T = len(y) - horizon if holdout else len(y)
    origins = chronological_origins(T, window, horizon, stride, max_folds)
    splits = [
        RollingOriginSplit(
            train=slice(int(t) - window, int(t)),
            validation=slice(int(t), int(t) + horizon),
        )
        for t in origins
    ]
    grid = np.linspace(0, 1, grid_points)
    summaries: list[dict] = []
    tables: list[pd.DataFrame] = []
    surface_map: dict[tuple[str, int], np.ndarray] = {}

    for d in orders:
        # The CUDA campaign prepares precisely these completed-origin losses
        # outside this function. All statistical operations after this point
        # (F weights, global minimization, branches and outer refit) are shared
        # by CPU and CUDA backends.
        if precomputed_grid_losses is not None:
            if d not in precomputed_grid_losses:
                raise ValueError(f"Missing precomputed fold losses for order d={d}.")
            base_losses = np.asarray(precomputed_grid_losses[d], dtype=float)
            if base_losses.shape != (len(origins), len(grid)):
                raise ValueError("Precomputed losses must match completed origins and S grid.")
            if not np.all(np.isfinite(base_losses)) or np.any(base_losses < 0):
                raise ValueError("Precomputed forecast losses must be finite and nonnegative.")
            prepared = None if not refine_pooled else prepare_rolling_pure_forecast_objective(
                y[:T], splits, order=d
            )
        else:
            prepared = prepare_rolling_pure_forecast_objective(y[:T], splits, order=d)
            base_losses = all_grid_fold_losses(prepared, grid, window, d)
        for method in methods:
            surfaces = weighted_surface_history(base_losses, method)
            surface_map[(method.name, d)] = surfaces
            start, weights = method.weights(len(origins))
            latest = surfaces[-1]

            def pooled_exact(s):
                if prepared is None:
                    raise RuntimeError("Exact pooled refinement needs a prepared objective.")
                values = fold_loss_at_lambda(
                    prepared, smoothness_to_lambda(float(s), window, d)
                )
                return float(weights @ values[start:])

            pooled_s, pooled_mse = select_from_grid(
                grid, latest, pooled_exact, refine=refine_pooled
            )
            branches = track_grid_branches(grid, surfaces, radius=track_radius)
            branch_s, branch_id, branch_score, support = select_tracked_branch(
                branches, surfaces, grid, min_support=branch_min_support,
                decision_k=branch_decision_k, score_k=branch_score_k,
            )
            if not branches.empty:
                branches.insert(0, "method", method.name)
                branches.insert(1, "d", int(d))
                branches["origin"] = origins[branches["step"].to_numpy(int)]
                tables.append(branches)

            results = {}
            for label, s in (("pooled", pooled_s), ("tracked", branch_s)):
                _, forecast = fit_window_forecast(
                    y[:T], origin=T, window=window, order=d,
                    horizon=horizon, smoothness=float(s),
                )
                results[f"{label}_test_mse"] = (
                    float(np.mean((y[T:T + horizon] - forecast)**2))
                    if holdout else np.nan
                )
            summaries.append({
                "method": method.name, "scheme": method.scheme,
                "lookback": method.lookback, "decay": method.decay,
                "d": int(d), "L": int(window), "h": int(horizon),
                "n_folds": int(len(origins)),
                "pooled_s": float(pooled_s),
                "pooled_historical_mse": float(pooled_mse),
                "tracked_s": float(branch_s),
                "tracked_branch": branch_id,
                "tracked_support": int(support),
                "tracked_historical_score": float(branch_score),
                **results,
            })

    branch_table = (
        pd.concat(tables, ignore_index=True)
        if tables else pd.DataFrame(
            columns=["method", "d", "step", "branch", "s_local", "F_local", "origin"]
        )
    )
    return WeightedSurfaceStudy(
        summary=pd.DataFrame(summaries), branches=branch_table,
        surfaces=surface_map, grid=grid, origins=origins,
        selected_origin=T, horizon=horizon,
    )
