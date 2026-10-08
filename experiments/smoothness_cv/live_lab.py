"""Interactive, non-frozen laboratory for the dynamic smoothness-CV paper.

Uses the production penalized solver, derivative-aware stationary-point search,
rolling forecast objective and CP08 branch-to-smoothness rules. This module is
not part of the frozen CP03--CP08 experiments.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Callable

from trend_estimation.core.pure import cached_pure_solver

import numpy as np
import pandas as pd

import trend_estimation as td
from experiments.smoothness_cv.dynamic_branch_rules import (
    DEFAULT_RULES,
    TRAJECTORY_RULES,
    apply_rule,
)

RULES = {rule.name: rule for rule in (*DEFAULT_RULES, *TRAJECTORY_RULES)}
FUNCTIONS: dict[str, Callable] = {
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
    "abs": np.abs, "tanh": np.tanh, "where": np.where,
    "minimum": np.minimum, "maximum": np.maximum,
    "clip": np.clip,
}
BINARY_OPS = {
    ast.Add: np.add, ast.Sub: np.subtract, ast.Mult: np.multiply,
    ast.Div: np.divide, ast.Pow: np.power, ast.Mod: np.mod,
    ast.BitAnd: np.logical_and, ast.BitOr: np.logical_or,
}
COMPARE_OPS = {
    ast.Gt: np.greater, ast.GtE: np.greater_equal,
    ast.Lt: np.less, ast.LtE: np.less_equal, ast.Eq: np.equal,
    ast.NotEq: np.not_equal,
}


def synthetic_function(expression: str, n: int) -> np.ndarray:
    """Evaluate a restricted numerical expression; never execute user Python."""
    if not 30 <= n <= 3000:
        raise ValueError("Synthetic length must be between 30 and 3000.")
    t = np.arange(n, dtype=float)
    variables = {"t": t, "pi": np.pi, "e": np.e}

    def evaluate(node, depth=0):
        if depth > 30:
            raise ValueError("Expression is too deeply nested.")
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if abs(node.value) > 1e8:
                raise ValueError("Numerical constants must be within 1e8.")
            return float(node.value)
        if isinstance(node, ast.Name) and node.id in variables:
            return variables[node.id]
        if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPS:
            return BINARY_OPS[type(node.op)](evaluate(node.left, depth+1), evaluate(node.right, depth+1))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand, depth+1)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and type(node.ops[0]) in COMPARE_OPS:
            return COMPARE_OPS[type(node.ops[0])](evaluate(node.left, depth+1), evaluate(node.comparators[0], depth+1))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            func = FUNCTIONS.get(node.func.id)
            if func is not None and not node.keywords and len(node.args) <= 3:
                return func(*(evaluate(arg, depth+1) for arg in node.args))
        raise ValueError("Use only t, constants, arithmetic, comparisons and the documented functions.")

    if len(expression) > 500:
        raise ValueError("Expression is too long.")
    try:
        with np.errstate(all="raise"):
            result = np.broadcast_to(
                np.asarray(evaluate(ast.parse(expression, mode="eval").body), dtype=float),
                (n,),
            ).copy()
    except (SyntaxError, FloatingPointError, TypeError, OverflowError) as exc:
        raise ValueError(f"Invalid or numerically unstable expression: {exc}") from exc
    if not np.all(np.isfinite(result)):
        raise ValueError("The function must be finite everywhere.")
    return result


def make_synthetic(
    expression: str,
    n: int = 220,
    noise_sd: float = 0.35,
    noise: str = "Gaussian",
    phi: float = 0.0,
    seed: int = 42,
) -> pd.DataFrame:
    truth = synthetic_function(expression, n)
    rng = np.random.default_rng(seed)
    if noise_sd < 0 or not -0.99 < phi < 0.99:
        raise ValueError("noise_sd must be nonnegative and phi in (-0.99, 0.99).")
    if noise == "Gaussian":
        innovations = rng.normal(0.0, noise_sd, n)
    elif noise == "Laplace":
        innovations = rng.laplace(0.0, noise_sd / np.sqrt(2), n)
    elif noise == "Student-t (df=5)":
        innovations = rng.standard_t(5, n) * noise_sd / np.sqrt(5/3)
    elif noise == "Heteroskedastic":
        innovations = rng.normal(0.0, noise_sd, n) * (0.5 + np.arange(n) / n)
    else:
        raise ValueError("Unknown noise family.")
    errors = np.empty(n)
    errors[0] = innovations[0] / np.sqrt(1 - phi**2)
    for i in range(1, n):
        errors[i] = phi * errors[i-1] + innovations[i]
    return pd.DataFrame({"t": np.arange(n), "observed": truth + errors, "latent": truth})


def transform_observations(frame: pd.DataFrame, mode: str) -> pd.DataFrame:
    """Transform levels with the same dates. A first difference loses one row."""
    result = frame.copy()
    values = result["observed"].to_numpy(dtype=float)
    if mode in ("Log level", "Log return") and np.any(values <= 0):
        raise ValueError("Log transformations require strictly positive data.")
    if mode == "Level":
        transformed = values
    elif mode == "Log level":
        transformed = np.log(values)
    elif mode == "Indexed to 100":
        if values[0] == 0:
            raise ValueError("Cannot index a series beginning at zero.")
        transformed = 100 * values / values[0]
    elif mode == "Simple return":
        if np.any(values[:-1] == 0):
            raise ValueError("Simple returns require nonzero preceding values.")
        transformed = values[1:] / values[:-1] - 1
        result = result.iloc[1:].copy()
    elif mode == "Log return":
        transformed = np.diff(np.log(values))
        result = result.iloc[1:].copy()
    else:
        raise ValueError("Unknown transformation.")
    result["observed"] = transformed
    # Truth in the transformed space requires applying the SAME transformation.
    if "latent" in result:
        result = result.drop(columns=["latent"])
    if not np.all(np.isfinite(transformed)):
        raise ValueError("Transformed data are not finite.")
    return result.reset_index(drop=True)


def _candidates(prepared, order: int, window: int, spacing: float, depth: int):
    """Derivative-based search with the same endpoint logic as the paper experiment."""
    cache = {}

    def at_lambda(lam):
        key = float(lam)
        if key not in cache:
            cache[key] = prepared.evaluate(key)
        return cache[key]

    def callback(lam):
        val = at_lambda(lam)
        return val.value, val.first, val.second

    stationary = td.find_stationary_points_smoothness(
        callback, n_obs=window, order=order,
        initial_grid_size=9, max_depth=depth,
        min_interval=1e-3, endpoint_refinement_levels=4,
        derivative_tol=1e-8, curvature_tol=1e-8,
        near_zero_ratio=0.2, root_xtol=1e-10, boundary_margin=1e-6,
    )
    candidates = [
        {"smoothness": float(p.smoothness_), "lambda": float(p.lambda_),
         "val1_mse": float(p.objective_), "source": "interior"}
        for p in stationary.points_ if p.kind_ == "minimum"
    ]
    probe = 0.002
    if at_lambda(0.0).value <= at_lambda(td.smoothness_to_lambda(probe, window, order)).value:
        candidates.append({"smoothness": 0.0, "lambda": 0.0,
                           "val1_mse": float(at_lambda(0.0).value), "source": "S=0"})
    if at_lambda(np.inf).value <= at_lambda(td.smoothness_to_lambda(1-probe, window, order)).value:
        candidates.append({"smoothness": 1.0, "lambda": np.inf,
                           "val1_mse": float(at_lambda(np.inf).value), "source": "S=1"})
    if not candidates:
        candidates = [
            {"smoothness": s, "lambda": lam, "val1_mse": float(at_lambda(lam).value),
             "source": "boundary_fallback"}
            for s, lam in ((0.0, 0.0), (1.0, np.inf))
        ]
    distinct = []
    for c in sorted(candidates, key=lambda c: (c["val1_mse"], c["smoothness"])):
        if all(abs(c["smoothness"] - q["smoothness"]) >= spacing for q in distinct):
            distinct.append(c)
    return sorted(distinct, key=lambda c: c["smoothness"])


def _one_to_one(previous: dict, candidates: list, epsilon: float):
    pairs = sorted(
        (abs(old - float(c["smoothness"])), str(branch), i)
        for branch, old in previous.items()
        for i, c in enumerate(candidates)
    )
    matches, used = {}, set()
    for distance, branch, i in pairs:
        if distance <= epsilon and branch not in matches and i not in used:
            matches[branch] = (i, distance)
            used.add(i)
    return matches


@dataclass
class LabResult:
    tracks: pd.DataFrame
    candidates: pd.DataFrame
    surfaces: pd.DataFrame
    final_surface: pd.DataFrame
    summary: pd.DataFrame
    selected_branch: str
    final_s: float
    pooled_s: float
    final_lambda: float
    trend: np.ndarray
    forecast: np.ndarray
    pooled_trend: np.ndarray
    pooled_forecast: np.ndarray
    train_start: int
    pretest_end: int
    test_end: int
    selection_status: str


def run_lab(
    observed, *,
    order: int = 2,
    window: int = 60,
    horizon: int = 5,
    step: int = 5,
    max_origins: int = 12,
    test_size: int = 5,
    track_epsilon: float = 0.10,
    candidate_spacing: float = 0.02,
    max_minima: int = 5,
    rule: str = "recency_hl3",
    grid_points: int = 41,
    search_depth: int = 5,
) -> LabResult:
    """Apply two-stage chronological selection without touching reserved targets."""
    y = np.asarray(observed, dtype=float)
    if y.ndim != 1 or not np.all(np.isfinite(y)):
        raise ValueError("observed must be a one-dimensional finite series.")
    if not 1 <= order <= 4 or window <= order or not 1 <= horizon <= 30:
        raise ValueError("Require order 1..4, window > order, horizon 1..30.")
    if min(step, max_origins, test_size, max_minima) < 1:
        raise ValueError("Step, max origins, test size and max minima must be positive.")
    if not 0 < track_epsilon < 1 or not 0 < candidate_spacing < 1:
        raise ValueError("Matching radii must lie within (0,1).")
    if grid_points < 5 or rule not in RULES:
        raise ValueError("Invalid surface grid or rule.")
    if len(y) < window + 3 * horizon + test_size:
        raise ValueError("Need at least window + 3*horizon + test_size observations.")

    # The last test_size points are NEVER passed to a selection objective.
    pretest_end = len(y) - test_size
    historical_end = pretest_end - horizon  # reserve a distinct final Validation-1
    history = y[:historical_end]
    paired = td.rolling_origin_splits(
        len(history), initial_train=window, horizon=horizon,
        expanding=False, train_window=window, step=step,
    )
    paired = [sp for sp in paired if sp.validation.stop + horizon <= len(history)]
    paired = paired[-max_origins:]
    if not paired:
        raise ValueError("No historical paired Validation-1/Validation-2 origins.")

    grid = np.linspace(0, 1, grid_points)
    tracks, surface_rows = [], []
    last_s, branch_ids = {}, []
    for origin_number, split in enumerate(paired, start=1):
        prepared = td.prepare_rolling_pure_forecast_objective(history, [split], order=order)
        candidates = _candidates(prepared, order, window, candidate_spacing, search_depth)
        for s in grid:
            lam = td.smoothness_to_lambda(float(s), window, order)
            surface_rows.append({
                "origin": origin_number, "smoothness": float(s),
                "val1_mse": float(prepared.evaluate(lam).value),
            })
        if origin_number == 1:
            initial = sorted(candidates, key=lambda c: (c["val1_mse"], c["smoothness"]))[:max_minima]
            initial.sort(key=lambda c: c["smoothness"])
            branch_ids = [f"b{i+1}" for i in range(len(initial))]
            last_s = {b: float(c["smoothness"]) for b, c in zip(branch_ids, initial)}
            matches = {b: (next(i for i, c in enumerate(candidates)
                                if abs(c["smoothness"] - last_s[b]) < 1e-12), 0.0)
                       for b in branch_ids}
        else:
            matches = _one_to_one(last_s, candidates, track_epsilon)
        for branch in branch_ids:
            if branch not in matches:
                tracks.append({
                    "origin": origin_number, "branch_id": branch, "status": "missing",
                    "smoothness": np.nan, "lambda": np.nan,
                    "val1_mse": np.nan, "val2_mse": np.nan, "val2_rmse": np.nan,
                })
                continue
            index, delta = matches[branch]
            candidate = candidates[index]
            s = float(candidate["smoothness"])
            fit = td.PurePenalizedTrend(order=order, smoothness=s).fit(
                history[split.validation.stop-window:split.validation.stop]
            )
            prediction = np.asarray(fit.forecast(horizon), dtype=float)
            target = history[split.validation.stop:split.validation.stop+horizon]
            mse = float(np.mean((target - prediction)**2))
            tracks.append({
                "origin": origin_number, "branch_id": branch, "status": "matched",
                "smoothness": s, "lambda": float(candidate["lambda"]),
                "val1_mse": float(candidate["val1_mse"]),
                "val2_mse": mse, "val2_rmse": float(np.sqrt(mse)),
                "delta_s": float(delta),
            })
            last_s[branch] = s

    # A final Val1 surface is built with all pre-test information, no test data.
    last_split = td.RollingOriginSplit(
        train=slice(pretest_end-horizon-window, pretest_end-horizon),
        validation=slice(pretest_end-horizon, pretest_end),
    )
    prepared_final = td.prepare_rolling_pure_forecast_objective(
        y[:pretest_end], [last_split], order=order
    )
    final_candidates = _candidates(
        prepared_final, order, window, candidate_spacing, search_depth
    )
    final_surface = pd.DataFrame([
        {"smoothness": float(s), "val1_mse": float(
            prepared_final.evaluate(td.smoothness_to_lambda(float(s), window, order)).value
        )}
        for s in grid
    ])
    final_matches = _one_to_one(last_s, final_candidates, track_epsilon)
    tracks_frame = pd.DataFrame(tracks)
    summaries = []
    for branch in branch_ids:
        group = tracks_frame.loc[tracks_frame["branch_id"].eq(branch)]
        matched = group.loc[group["status"].eq("matched")].sort_values("origin")
        summaries.append({
            "branch_id": branch, "support": len(matched) / len(group),
            "mean_val2_rmse": float(matched["val2_rmse"].mean()),
            "mean_val2_mse": float(matched["val2_mse"].mean()),
            "last_historical_s": float(matched["smoothness"].iloc[-1]),
            "continued_to_final": branch in final_matches,
        })
    summary = pd.DataFrame(summaries)
    eligible = summary.loc[summary["continued_to_final"]].copy()
    pool = pd.DataFrame(surface_rows).groupby("smoothness", as_index=False)["val1_mse"].mean()
    pooled_s = float(pool.loc[pool["val1_mse"].idxmin(), "smoothness"])
    if not eligible.empty:
        complete = eligible.loc[np.isclose(eligible["support"], 1.0)]
        if not complete.empty:
            eligible = complete
        else:
            eligible = eligible.loc[np.isclose(eligible["support"], eligible["support"].max())]
        winner = eligible.sort_values(["mean_val2_rmse", "branch_id"]).iloc[0]
        branch = str(winner["branch_id"])
        current_s = float(final_candidates[final_matches[branch][0]]["smoothness"])
        past = tracks_frame.loc[
            tracks_frame["branch_id"].eq(branch) & tracks_frame["status"].eq("matched")
        ].sort_values("origin")
        raw_s, _ = apply_rule(
            RULES[rule],
            history_s=past["smoothness"].to_numpy(),
            history_val2_loss=past["val2_rmse"].to_numpy(),
            current_s=current_s,
        )
        final_s = float(np.clip(raw_s, 0, 1))
        status = "tracked" + (" (extrapolated smoothness clipped)" if raw_s != final_s else "")
    else:
        # Explicit diagnostic fallback; never use reserved test labels to select.
        branch, final_s = "none", pooled_s
        status = "no branch continued; grid-pooled baseline used"
    final_fit = td.PurePenalizedTrend(order=order, smoothness=final_s).fit(
        y[pretest_end-window:pretest_end]
    )
    pooled_fit = td.PurePenalizedTrend(order=order, smoothness=pooled_s).fit(
        y[pretest_end-window:pretest_end]
    )
    return LabResult(
        tracks=tracks_frame, candidates=pd.DataFrame(final_candidates),
        surfaces=pd.DataFrame(surface_rows), final_surface=final_surface, summary=summary,
        selected_branch=branch, final_s=final_s, pooled_s=pooled_s,
        final_lambda=float(final_fit.lambda_), trend=final_fit.trend_.copy(),
        forecast=np.asarray(final_fit.forecast(test_size), dtype=float),
        pooled_trend=pooled_fit.trend_.copy(),
        pooled_forecast=np.asarray(pooled_fit.forecast(test_size), dtype=float),
        train_start=pretest_end-window, pretest_end=pretest_end, test_end=len(y),
        selection_status=status,
    )


def smoothing_matrix(n: int, order: int, smoothness: float) -> np.ndarray:
    """H_lambda = Q diag[(1 + lambda * delta)^-1] Q.T."""
    if n > 250:
        raise ValueError("Display matrix capped at 250 observations.")
    solver = cached_pure_solver(n, order)
    lam = solver.lambda_from_s(smoothness)
    alpha = np.zeros_like(solver.eigvals) if np.isinf(lam) else 1 / (1 + lam * solver.eigvals)
    if np.isinf(lam):
        alpha[:order] = 1
    return (solver.eigvecs * alpha) @ solver.eigvecs.T
