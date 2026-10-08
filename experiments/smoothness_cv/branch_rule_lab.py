"""Exploratory multi-order, branch-and-rule CV with causal V matrices.

Each historical origin:
  1. Recover Validation-1 local minima independently for every order d.
  2. Match minima to persistent branches; initialize a bounded set of branches.
  3. For every (d, branch, rule), construct the applied S using current Val1
     minimum and only already-completed historical V rows of that *same rule*.
  4. Evaluate precisely this applied S on Val1 and then on Val2, without
     reselecting S. Val2 uses a fresh trend estimate at the Val2 forecast origin
     with the already-fixed d and S (not a new hyperparameter optimization).
  5. Select a branch and a rule on historical, pooled Val2 squared errors;
     map the final pretest Val1 minimum through that same rule, then test.

Original unweighted polynomial continuation is rule='last'.
This module never modifies frozen checkpoints or selects on the test targets.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

import trend_estimation as td
from experiments.smoothness_cv.dynamic_branch_rules import (
    DEFAULT_RULES, TRAJECTORY_RULES, apply_rule,
)
from experiments.smoothness_cv.live_lab import _candidates, _one_to_one

RULE_SPECS = {r.name: r for r in (*DEFAULT_RULES, *TRAJECTORY_RULES)}


@dataclass
class BranchLabResult:
    branches: pd.DataFrame
    evaluations: pd.DataFrame
    summary: pd.DataFrame
    historical_surfaces: pd.DataFrame
    surfaces: pd.DataFrame
    candidates: pd.DataFrame
    final_candidates: pd.DataFrame
    selected_order: int
    selected_branch: str
    selected_rule: str
    selected_s: float
    selected_lambda: float
    selected_val1_mse: float
    selected_val2_mse: float
    selected_val2_rmse: float
    selection_status: str
    method: str
    trend: np.ndarray
    forecast: np.ndarray
    evaluation_trend: np.ndarray
    evaluation_forecast: np.ndarray
    train_start: int
    val1_start: int
    val1_end: int
    val2_end: int
    pretest_end: int
    test_end: int
    forecast_start: int
    forecast_end: int
    future_horizon: int
    window: int
    horizon: int


def _mse(actual: np.ndarray, forecast: np.ndarray) -> float:
    a = np.asarray(actual, dtype=float)
    b = np.asarray(forecast, dtype=float)
    if a.shape != b.shape or not np.isfinite(b).all():
        return float("inf")
    delta = a - b
    scale = float(np.max(np.abs(delta)))
    if scale == 0.0:
        return 0.0
    with np.errstate(over="ignore"):
        return float((scale**2) * np.mean((delta / scale)**2))


def _score(y, *, origin: int, window: int, horizon: int, d: int, s: float):
    fit = td.PurePenalizedTrend(order=d, smoothness=s).fit(
        y[origin-window:origin]
    )
    forecast = np.asarray(fit.forecast(horizon), dtype=float)
    return _mse(y[origin:origin+horizon], forecast)


def _safe_rule(rule, *, current_s: float, prior: pd.DataFrame, observed_at: int):
    """History scores become available at Val2 end, never when they are made."""
    history = prior.loc[prior["val2_end"].le(observed_at)].sort_values("origin")
    # History S values are the Val1 local minima; historical losses refer to
    # THIS rule, hence weighted rules cannot use a different rule's score.
    s = history["s_minimo"].to_numpy(dtype=float)
    losses = history["val2_rmse"].to_numpy(dtype=float)
    raw, meta = apply_rule(
        rule, history_s=s, history_val2_loss=losses,
        current_s=current_s,
    )
    return float(np.clip(raw, 0, 1)), float(raw), meta, len(history)


def run_branch_lab(
    observed, *,
    orders: tuple[int, ...] = (1, 2, 3, 4),
    rules: tuple[str, ...] = ("last", "mean_k3", "recency_hl3", "val2_weighted"),
    window: int = 60,
    horizon: int = 5,
    step: int = 5,
    max_origins: int = 12,
    test_size: int = 5,
    future_horizon: int = 5,
    track_epsilon: float = 0.10,
    candidate_spacing: float = 0.02,
    max_branches: int = 5,
    min_support: float = 0.65,
    grid_points: int = 41,
    search_depth: int = 5,
) -> BranchLabResult:
    """Causally compare branch-to-S rules over multiple forecast origins.

    Test and final pretest Val1 data are excluded from historical model choice.
    Support is n_matched/n_historical_origins (missing origins not silently
    treated as zero loss). The selected candidate uses historical mean Val2 MSE.
    """
    y = np.asarray(observed, dtype=float)
    if y.ndim != 1 or not y.size or not np.all(np.isfinite(y)):
        raise ValueError("Las observaciones deben ser un vector numérico finito.")
    if not orders or len(set(orders)) != len(orders):
        raise ValueError("Seleccione órdenes de diferencias distintos.")
    if any(type(d) is not int or not 1 <= d <= 4 for d in orders):
        raise ValueError("Los órdenes deben pertenecer a 1, 2, 3, 4.")
    if not rules or len(set(rules)) != len(rules):
        raise ValueError("Seleccione al menos una regla distinta.")
    if any(rule not in RULE_SPECS for rule in rules):
        raise ValueError("Se desconoce alguna regla de agregación.")
    rules = ("last",) + tuple(r for r in rules if r != "last")
    if not all(isinstance(v, int) and v >= 1 for v in
               (horizon, step, max_origins, max_branches, test_size,
                future_horizon, grid_points)):
        raise ValueError("Los horizontes, conteos y tamaños deben ser positivos.")
    if window <= max(orders) or grid_points < 5 or search_depth < 0:
        raise ValueError("Se necesita L > d y una malla de al menos 5 valores.")
    if not 0 < track_epsilon < 1 or not 0 < candidate_spacing < 1:
        raise ValueError("Las distancias deben estar en (0, 1).")
    if not 0 < min_support <= 1:
        raise ValueError("El soporte mínimo debe estar en (0, 1].")
    if len(y) < window + 3*horizon + test_size:
        raise ValueError("Se necesitan al menos L + 3h + prueba observaciones.")

    pretest_end = len(y)-test_size
    hist_end = pretest_end-horizon
    paired = td.rolling_origin_splits(
        hist_end, initial_train=window, horizon=horizon,
        expanding=False, train_window=window, step=step,
    )
    paired = [
        s for s in paired
        if s.validation.stop + horizon <= hist_end
    ][-max_origins:]
    if not paired:
        raise ValueError("No hay orígenes históricos con ambas validaciones.")

    surface_rows: list[dict] = []
    branch_rows: list[dict] = []
    evaluations: list[dict] = []
    grid = np.linspace(0, 1, grid_points)
    n_origins = len(paired)

    for d in sorted(orders):
        # Branch identities stay local to each order: b1 at d=1 != b1 at d=2.
        last_s: dict[str, float] = {}
        birth_origin: dict[str, int] = {}
        next_id = 1
        for origin_no, split in enumerate(paired, 1):
            a = int(split.validation.start)
            b = int(split.validation.stop)
            c = b+horizon
            prepared = td.prepare_rolling_pure_forecast_objective(
                y[:b], [split], order=d
            )
            found = _candidates(
                prepared, d, window, candidate_spacing, search_depth
            )
            for s in grid:
                surface_rows.append({
                    "d": d, "origin": origin_no, "val1_start": a,
                    "val1_end": b, "val2_end": c,
                    "smoothness": float(s),
                    "val1_mse": float(prepared.evaluate(
                        td.smoothness_to_lambda(float(s), window, d)
                    ).value),
                })

            matches = _one_to_one(last_s, found, track_epsilon)
            used_idx = {index for index, _ in matches.values()}
            # New local minima can initiate new branches, up to max_branches
            # per order. Prefer lower Val1 loss when capacity is limited.
            unmatched = sorted(
                (i for i in range(len(found)) if i not in used_idx),
                key=lambda i: (found[i]["val1_mse"], found[i]["smoothness"]),
            )
            for idx in unmatched:
                if len(last_s) >= max_branches:
                    break
                branch = f"b{next_id}"
                next_id += 1
                last_s[branch] = float(found[idx]["smoothness"])
                birth_origin[branch] = origin_no
                matches[branch] = (idx, 0.0)

            for branch, (index, movement) in matches.items():
                cand = found[index]
                local_s = float(cand["smoothness"])
                last_s[branch] = local_s
                branch_rows.append({
                    "d": d, "rama": branch, "origin": origin_no,
                    "val1_start": a, "val1_end": b, "val2_end": c,
                    "s_minimo": local_s, "lambda_minimo": float(cand["lambda"]),
                    "ecm_minimo_val1": float(cand["val1_mse"]),
                    "movimiento_s": float(movement),
                    "nacimiento": birth_origin[branch],
                })

                for rule_name in rules:
                    prior = pd.DataFrame([
                        rec for rec in evaluations
                        if rec["d"] == d and rec["rama"] == branch
                        and rec["regla"] == rule_name
                    ])
                    if prior.empty:
                        prior = pd.DataFrame(columns=[
                            "val2_end", "origin", "s_minimo", "val2_rmse"
                        ])
                    used_s, raw_s, meta, used_n = _safe_rule(
                        RULE_SPECS[rule_name],
                        current_s=local_s, prior=prior, observed_at=b,
                    )
                    # The SAME rule-produced S is scored in both validations.
                    # Val1 loss uses the already-constructed origin forecast
                    # objective. Val2 refits at b but does NOT retune d or S.
                    lam = td.smoothness_to_lambda(used_s, window, d)
                    val1_loss = float(prepared.evaluate(lam).value)
                    val2_loss = _score(
                        y[:c], origin=b, window=window, horizon=horizon,
                        d=d, s=used_s,
                    )
                    evaluations.append({
                        "d": d, "rama": branch, "regla": rule_name,
                        "origin": origin_no, "val1_start": a, "val1_end": b,
                        "val2_end": c, "s_minimo": local_s,
                        "s_aplicado": used_s, "s_sin_recortar": raw_s,
                        "val1_mse": val1_loss, "val2_mse": val2_loss,
                        "val2_rmse": float(np.sqrt(val2_loss)),
                        "n_historial_disponible": used_n,
                        "n_historial_utilizado": meta.get("n_history_used", used_n),
                        "usa_s_actual": meta.get("includes_current_s"),
                        "fallback": meta.get("fallback_to_last", False),
                        "acotado": abs(used_s - raw_s) > 1e-12,
                    })

    branch_table = pd.DataFrame(branch_rows)
    v = pd.DataFrame(evaluations)
    if v.empty:
        raise ValueError("No se produjeron matrices V.")
    total_origins = len(paired)
    agg = (v.groupby(["d", "rama", "regla"], as_index=False)
           .agg(n_origenes=("val2_mse", "size"),
                n_validos=("val2_mse", lambda a: int(np.isfinite(a).sum())),
                ec_medio_val1=("val1_mse", "mean"),
                ec_medio_val2=("val2_mse", "mean"),
                re_cm_val2=("val2_mse", lambda a: float(np.sqrt(np.mean(a))))))
    agg["soporte"] = agg["n_origenes"]/total_origins
    agg["elegible"] = (
        agg["soporte"].ge(min_support)
        & agg["n_validos"].eq(agg["n_origenes"])
        & np.isfinite(agg["ec_medio_val2"])
    )
    eligibles = agg.loc[agg["elegible"]].copy()
    if eligibles.empty:
        raise ValueError(
            "Ninguna combinación alcanza el soporte mínimo y un ECM finito. "
            "Reduzca el soporte requerido o aumente el número de orígenes."
        )
    # Select by pooled squared error. Coverage is an explicit eligibility
    # criterion; ties favor higher coverage and the fixed 'last' baseline.
    eligibles["baseline_first"] = (eligibles["regla"] != "last").astype(int)
    eligibles = eligibles.sort_values(
        ["ec_medio_val2", "soporte", "baseline_first", "d", "rama", "regla"],
        ascending=[True, False, True, True, True, True],
        kind="mergesort",
    )
    best = eligibles.iloc[0]
    chosen_d, chosen_branch, chosen_rule = (
        int(best["d"]), str(best["rama"]), str(best["regla"])
    )

    # All orders receive an untouched final Val1 surface in the same period.
    final_a, final_b = pretest_end-horizon, pretest_end
    final_split = td.RollingOriginSplit(
        train=slice(final_a-window, final_a),
        validation=slice(final_a, final_b),
    )
    final_surfaces, final_minima = [], []
    for d in sorted(orders):
        prepared = td.prepare_rolling_pure_forecast_objective(
            y[:pretest_end], [final_split], order=d
        )
        minimum = _candidates(
            prepared, d, window, candidate_spacing, search_depth
        )
        for cand in minimum:
            final_minima.append({"d": d, "smoothness": cand["smoothness"],
                                 "val1_mse": cand["val1_mse"],
                                 "source": cand["source"]})
        for s in grid:
            final_surfaces.append({
                "d": d, "smoothness": float(s),
                "val1_mse": float(prepared.evaluate(
                    td.smoothness_to_lambda(float(s), window, d)
                ).value),
            })

    # Continue the historically selected branch to final validation-1.
    order_history = branch_table[branch_table["d"].eq(chosen_d)]
    last_positions = (order_history.sort_values("origin")
                      .groupby("rama")["s_minimo"].last().to_dict())
    final_for_order = [
        c for c in final_minima if int(c["d"]) == chosen_d
    ]
    final_matches = _one_to_one(
        last_positions, final_for_order, track_epsilon
    )
    if chosen_branch in final_matches:
        final_candidate = final_for_order[final_matches[chosen_branch][0]]
        current_s = float(final_candidate["smoothness"])
        status = "Rama histórica continuada en validación 1 final."
    else:
        # Disclose noncontinuation rather than disguising an old S as a new
        # observed local minimum. We can still apply the frozen rule based
        # on the latest historically available branch minimum.
        current_s = float(last_positions[chosen_branch])
        status = (
            "La rama seleccionada no continuó en la validación 1 final; "
            "se utilizó su último mínimo histórico conocido."
        )
    prior = v[
        v["d"].eq(chosen_d) & v["rama"].eq(chosen_branch)
        & v["regla"].eq(chosen_rule)
    ]
    applied_s, _, _, _ = _safe_rule(
        RULE_SPECS[chosen_rule], current_s=current_s, prior=prior,
        observed_at=pretest_end,
    )
    evaluation = td.PurePenalizedTrend(
        order=chosen_d, smoothness=applied_s
    ).fit(y[pretest_end-window:pretest_end])
    test_prediction = np.asarray(evaluation.forecast(test_size), dtype=float)

    final = td.PurePenalizedTrend(
        order=chosen_d, smoothness=applied_s
    ).fit(y[-window:])
    future = np.asarray(final.forecast(future_horizon), dtype=float)
    minima_df = pd.DataFrame(final_minima)
    minima_df["rank"] = np.where(
        minima_df["d"].eq(chosen_d)
        & np.isclose(minima_df["smoothness"], current_s, atol=1e-10),
        1, 2,
    )
    return BranchLabResult(
        branches=branch_table, evaluations=v, summary=agg.sort_values(
            ["ec_medio_val2", "d", "rama", "regla"],
            kind="mergesort",
        ).reset_index(drop=True),
        historical_surfaces=pd.DataFrame(surface_rows),
        surfaces=pd.DataFrame(final_surfaces),
        candidates=minima_df,
        final_candidates=minima_df,
        selected_order=chosen_d, selected_branch=chosen_branch,
        selected_rule=chosen_rule, selected_s=applied_s,
        selected_lambda=float(final.lambda_),
        selected_val1_mse=float(best["ec_medio_val1"]),
        selected_val2_mse=float(best["ec_medio_val2"]),
        selected_val2_rmse=float(best["re_cm_val2"]),
        selection_status=status,
        method="Continuación polinómica de mínimos cuadrados penalizados",
        trend=np.asarray(final.trend_, dtype=float).copy(),
        forecast=future,
        evaluation_trend=np.asarray(evaluation.trend_, dtype=float).copy(),
        evaluation_forecast=test_prediction,
        train_start=len(y)-window,
        val1_start=final_a, val1_end=final_b,
        val2_end=pretest_end,
        pretest_end=pretest_end, test_end=len(y),
        forecast_start=len(y), forecast_end=len(y)+future_horizon,
        future_horizon=future_horizon, window=window, horizon=horizon,
    )
