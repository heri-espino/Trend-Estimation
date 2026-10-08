"""Exploratory multi-order, branch-and-rule CV with causal V matrices.

Each historical origin:
  1. Fix an order d and a rule r BEFORE both validations.
  2. For each history-specific branch, find minima of the rule-transformed
     Validation-1 loss E1(phi_r(V_history, s)), and match those minima to
     the PREVIOUS APPLIED smoothness of that very (d, r) branch.
  3. Use the very same (d, r, applied S) to evaluate Validation 1 and
     Validation 2. A new trend fit is allowed at the new forecast origin;
     choosing a new S or r is NOT allowed between V1 and V2.
  4. Keep one V matrix per (d, rule, branch). Only completed prior V2 losses
     can enter the rule and its method-specific V1 objective.
  5. Select (d, rule, branch) by historical V2 MSE and evaluate the held-out
     test without retuning. The 'last' polynomial baseline is unchanged.

For rules independent of the current S, E1(phi_r(...)) is flat: its
minimum is unidentifiable. We represent one history-driven solution and
label it explicitly instead of claiming a newly discovered local minimum.

Original unweighted polynomial continuation is rule='last'.
This module never modifies frozen checkpoints or selects on the test targets.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

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
    losses = history["val2_mse"].to_numpy(dtype=float)
    raw, meta = apply_rule(
        rule, history_s=s, history_val2_loss=losses,
        current_s=current_s,
    )
    return float(np.clip(raw, 0, 1)), float(raw), meta, len(history)



def _method_minima(
    prepared, *,
    order: int,
    window: int,
    rule,
    history: pd.DataFrame,
    observed_at: int,
    spacing: float,
    depth: int,
    last_input: float | None = None,
) -> list[dict]:
    """Find minima of E1(phi_r(V_past, input_s)), not E1(input_s).

    The derivative-based pure method is retained without approximation for
    'last' and any history-free start. General transformations are evaluated
    on a grid with bounded local refinement. Each candidate retains its
    input S and the transformed (applied) S used in both validations.
    """
    known = history.loc[
        history["val2_end"].le(observed_at)
    ].sort_values("origin")
    if rule.family == "last" or known.empty:
        roots = _candidates(prepared, order, window, spacing, depth)
        return [
            {
                "s_minimo": float(p["smoothness"]),
                "s_aplicado": float(p["smoothness"]),
                "val1_mse": float(p["val1_mse"]),
                "source": str(p["source"]),
                "objetivo_plano": False,
            }
            for p in roots
        ]

    cache = {}
    s_hist = known["s_minimo"].to_numpy(float)
    errors = known["val2_mse"].to_numpy(float)

    def evaluate(input_s):
        key = round(float(np.clip(input_s, 0, 1)), 12)
        if key not in cache:
            output, _ = apply_rule(
                rule, history_s=s_hist,
                history_val2_loss=errors, current_s=key,
            )
            used = float(np.clip(output, 0, 1))
            value = float(prepared.evaluate(
                td.smoothness_to_lambda(used, window, order)
            ).value)
            cache[key] = (value, used)
        return cache[key]

    # 31 points give a visual/numerical search scaffold, and Brent bounded
    # refinement locates strict minima. The pure-last solver remains exact.
    x = np.linspace(0.0, 1.0, 31)
    loss = np.asarray([evaluate(z)[0] for z in x])
    finite = loss[np.isfinite(loss)]
    tol = 1e-10 * max(1.0, float(np.max(np.abs(finite)))) if finite.size else 1e-10
    if not finite.size:
        return []
    if np.max(finite) - np.min(finite) <= tol:
        chosen = float(last_input) if last_input is not None else 0.5
        val, applied = evaluate(chosen)
        return [{
            "s_minimo": chosen, "s_aplicado": applied,
            "val1_mse": val, "source": "objetivo_plano",
            "objetivo_plano": True,
        }]

    points = []
    for i, val in enumerate(loss):
        if not np.isfinite(val):
            continue
        if i == 0:
            local = val < loss[i+1]-tol
        elif i == len(loss)-1:
            local = val < loss[i-1]-tol
        else:
            local = (
                val <= loss[i-1]+tol and val <= loss[i+1]+tol
                and (val < loss[i-1]-tol or val < loss[i+1]-tol)
            )
        if not local:
            continue
        candidate = float(x[i])
        if 0 < i < len(x)-1:
            opt = minimize_scalar(
                lambda z: evaluate(z)[0],
                bounds=(float(x[i-1]), float(x[i+1])),
                method="bounded", options={"xatol": 1e-7},
            )
            if opt.success and np.isfinite(opt.fun) and opt.fun <= val+tol:
                candidate = float(opt.x)
        score, applied = evaluate(candidate)
        points.append({
            "s_minimo": candidate, "s_aplicado": applied,
            "val1_mse": score, "source": "minimo_metodo",
            "objetivo_plano": False,
        })
    if not points:
        ix = int(np.nanargmin(loss))
        score, applied = evaluate(x[ix])
        points.append({
            "s_minimo": float(x[ix]), "s_aplicado": applied,
            "val1_mse": score, "source": "mejor_punto_de_malla",
            "objetivo_plano": False,
        })
    filtered = []
    for point in sorted(points, key=lambda v: v["val1_mse"]):
        if all(
            abs(point["s_aplicado"]-other["s_aplicado"]) >= spacing
            for other in filtered
        ):
            filtered.append(point)
    return sorted(filtered, key=lambda v: v["s_aplicado"])


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
        # Share the expensive original V1 objective/minimum recovery across
        # rules, but NEVER share rules' branch states or transformed optima.
        prepared_by_origin = {}
        # The raw ECM surface is retained for scientific comparison by d.
        # Branch identities and minima are SPECIFIC to (d, rule).
        for rule_name in rules:
            rule = RULE_SPECS[rule_name]
            last_applied: dict[str, float] = {}
            last_input: dict[str, float] = {}
            birth_origin: dict[str, int] = {}
            next_id = 1

            for origin_no, split in enumerate(paired, 1):
                a, b = int(split.validation.start), int(split.validation.stop)
                c = b+horizon
                if origin_no not in prepared_by_origin:
                    prepared = td.prepare_rolling_pure_forecast_objective(
                        y[:b], [split], order=d
                    )
                    raw_minima = _candidates(
                        prepared, d, window, candidate_spacing, search_depth
                    )
                    prepared_by_origin[origin_no] = (prepared, raw_minima)
                prepared, raw_minima = prepared_by_origin[origin_no]
                if rule_name == rules[0]:
                    for s_value in grid:
                        s_value = float(s_value)
                        surface_rows.append({
                            "d": d, "origin": origin_no, "val1_start": a,
                            "val1_end": b, "val2_end": c,
                            "smoothness": s_value,
                            "val1_mse": float(prepared.evaluate(
                                td.smoothness_to_lambda(s_value, window, d)
                            ).value),
                        })
                used_s: list[float] = []
                matches: list[tuple[str, dict, float, pd.DataFrame]] = []
                # The method-specific transformed objective is built from
                # the particular branch's completed history only.
                for branch, previous_s in last_applied.items():
                    prior = pd.DataFrame([
                        record for record in evaluations
                        if record["d"] == d and record["regla"] == rule_name
                        and record["rama"] == branch
                    ])
                    options = _method_minima(
                        prepared, order=d, window=window, rule=rule,
                        history=prior, observed_at=b,
                        spacing=candidate_spacing, depth=search_depth,
                        last_input=last_input[branch],
                    )
                    possible = [
                        p for p in options
                        if abs(p["s_aplicado"]-previous_s) <= track_epsilon
                        and all(abs(p["s_aplicado"]-u) >= candidate_spacing
                                for u in used_s)
                    ]
                    if not possible:
                        continue
                    cand = min(
                        possible,
                        key=lambda p: (
                            abs(p["s_aplicado"]-previous_s),
                            p["val1_mse"],
                        ),
                    )
                    distance = abs(cand["s_aplicado"]-previous_s)
                    used_s.append(cand["s_aplicado"])
                    matches.append((branch, cand, distance, prior))
                # Unmatched current raw minima start NEW method-specific
                # branches (with empty history, phi_r(empty, s) = s).
                # Thus 'last' recovers the original polynomial benchmark.
                for point in sorted(
                    raw_minima,
                    key=lambda p: (p["val1_mse"], p["smoothness"]),
                ):
                    if len(last_applied) >= max_branches:
                        break
                    candidate_s = float(point["smoothness"])
                    if any(abs(candidate_s-s0) < candidate_spacing
                           for s0 in used_s):
                        continue
                    branch = f"b{next_id}"
                    next_id += 1
                    birth_origin[branch] = origin_no
                    last_applied[branch] = candidate_s
                    last_input[branch] = candidate_s
                    new = {
                        "s_minimo": candidate_s,
                        "s_aplicado": candidate_s,
                        "val1_mse": float(point["val1_mse"]),
                        "source": str(point["source"]),
                        "objetivo_plano": False,
                    }
                    used_s.append(candidate_s)
                    matches.append((
                        branch, new, 0.0,
                        pd.DataFrame(columns=[
                            "origin", "val2_end", "s_minimo", "val2_mse"
                        ]),
                    ))

                for branch, cand, distance, prior in matches:
                    input_s = float(cand["s_minimo"])
                    applied_s, raw_s, meta, used_n = _safe_rule(
                        rule, current_s=input_s,
                        prior=prior, observed_at=b,
                    )
                    if not np.isclose(applied_s, cand["s_aplicado"],
                                      atol=1e-8):
                        raise AssertionError(
                            "La regla ha cambiado la S fijada en validación 1."
                        )
                    last_applied[branch] = applied_s
                    last_input[branch] = input_s
                    lam = td.smoothness_to_lambda(applied_s, window, d)
                    val1_loss = float(prepared.evaluate(lam).value)
                    val2_loss = _score(
                        y[:c], origin=b, window=window,
                        horizon=horizon, d=d, s=applied_s,
                    )
                    branch_rows.append({
                        "d": d, "regla": rule_name, "rama": branch,
                        "origin": origin_no, "val1_start": a,
                        "val1_end": b, "val2_end": c,
                        "s_minimo": input_s, "s_aplicado": applied_s,
                        "lambda_minimo": float(td.smoothness_to_lambda(
                            input_s, window, d
                        )),
                        "ecm_minimo_val1": val1_loss,
                        "movimiento_s": float(distance),
                        "nacimiento": birth_origin[branch],
                        "origen_minimo": cand["source"],
                        "objetivo_plano": bool(cand["objetivo_plano"]),
                    })
                    evaluations.append({
                        "d": d, "rama": branch, "regla": rule_name,
                        "origin": origin_no, "val1_start": a,
                        "val1_end": b, "val2_end": c,
                        "s_minimo": input_s, "s_aplicado": applied_s,
                        "s_sin_recortar": raw_s,
                        "val1_mse": val1_loss, "val2_mse": val2_loss,
                        "val2_rmse": float(np.sqrt(val2_loss)),
                        "n_historial_disponible": used_n,
                        "n_historial_utilizado": meta.get(
                            "n_history_used", used_n
                        ),
                        "usa_s_actual": meta.get("includes_current_s"),
                        "fallback": meta.get("fallback_to_last", False),
                        "acotado": abs(applied_s-raw_s) > 1e-12,
                        "objetivo_plano": bool(cand["objetivo_plano"]),
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

    # The frozen (d, rule, branch) must also define the final V1 minimum.
    # Never match a branch from another rule or just from the same d.
    prior = v[
        v["d"].eq(chosen_d) & v["rama"].eq(chosen_branch)
        & v["regla"].eq(chosen_rule)
    ]
    previous = prior.sort_values("origin").iloc[-1]
    last_applied_s = float(previous["s_aplicado"])
    last_input_s = float(previous["s_minimo"])
    final_prepared = td.prepare_rolling_pure_forecast_objective(
        y[:pretest_end], [final_split], order=chosen_d
    )
    final_options = _method_minima(
        final_prepared, order=chosen_d, window=window,
        rule=RULE_SPECS[chosen_rule], history=prior,
        observed_at=pretest_end, spacing=candidate_spacing,
        depth=search_depth, last_input=last_input_s,
    )
    possible = [
        item for item in final_options
        if abs(float(item["s_aplicado"])-last_applied_s) <= track_epsilon
    ]
    if possible:
        current = min(
            possible,
            key=lambda item: (
                abs(item["s_aplicado"]-last_applied_s),
                item["val1_mse"],
            ),
        )
        current_s = float(current["s_minimo"])
        status = (
            "Rama de (d, regla) continuada en validación 1 final."
            if not current["objetivo_plano"] else
            "La regla generó una función plana en V1 final; "
            "se mantuvo la solución determinada por el historial."
        )
    else:
        current_s = last_input_s
        status = (
            "No hubo mínimo de la regla compatible con la rama en V1 final; "
            "se mantuvo su último valor de entrada histórico."
        )
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
    minima_df["rank"] = 2
    # The selected applied S can differ from every raw F_d minimum:
    # show it as a separate, correctly labelled point on the original curve.
    minima_df = pd.concat([
        minima_df,
        pd.DataFrame([{
            "d": chosen_d, "smoothness": applied_s, "rank": 1,
            "val1_mse": float(final_prepared.evaluate(
                td.smoothness_to_lambda(applied_s, window, chosen_d)
            ).value),
            "source": "regla_aplicada",
        }]),
    ], ignore_index=True)
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
