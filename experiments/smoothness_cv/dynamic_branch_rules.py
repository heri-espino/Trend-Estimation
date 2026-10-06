from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class DynamicRuleSpec:
    name: str
    family: str
    k: int | None = None
    half_life: float | None = None


DEFAULT_RULES = (
    DynamicRuleSpec("last", "last"),
    DynamicRuleSpec("mean_k3", "recent_mean", k=3),
    DynamicRuleSpec("mean_k5", "recent_mean", k=5),
    DynamicRuleSpec("median_k3", "recent_median", k=3),
    DynamicRuleSpec("median_k5", "recent_median", k=5),
    DynamicRuleSpec("recency_hl3", "recency_weighted", half_life=3.0),
    DynamicRuleSpec("recency_hl5", "recency_weighted", half_life=5.0),
    DynamicRuleSpec("recency_hl10", "recency_weighted", half_life=10.0),
    DynamicRuleSpec("val2_weighted", "val2_weighted"),
    DynamicRuleSpec(
        "recency_val2_hl3",
        "recency_val2_weighted",
        half_life=3.0,
    ),
    DynamicRuleSpec(
        "recency_val2_hl5",
        "recency_val2_weighted",
        half_life=5.0,
    ),
    DynamicRuleSpec(
        "recency_val2_hl10",
        "recency_val2_weighted",
        half_life=10.0,
    ),
)


def _finite_history(
    smoothness: np.ndarray,
    val2_loss: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    s = np.asarray(smoothness, dtype=float)
    loss = np.asarray(val2_loss, dtype=float)
    keep = np.isfinite(s) & np.isfinite(loss) & (loss >= 0.0)
    return s[keep], loss[keep]


def _scaled_delta(loss: np.ndarray) -> float:
    positive = np.asarray(loss, dtype=float)
    positive = positive[np.isfinite(positive) & (positive > 0.0)]
    if positive.size == 0:
        return 1e-12
    scale = float(np.median(positive))
    return max(1e-12, 1e-8 * scale)


def _recent_values(
    history_s: np.ndarray,
    *,
    current_s: float,
    k: int,
) -> np.ndarray:
    if k < 1:
        raise ValueError("k must be positive.")
    values = np.concatenate(
        [
            np.asarray(history_s, dtype=float),
            np.asarray([float(current_s)], dtype=float),
        ]
    )
    values = values[np.isfinite(values)]
    if values.size == 0:
        raise ValueError("No finite smoothness values are available.")
    return values[-min(k, values.size) :]


def apply_rule(
    spec: DynamicRuleSpec,
    *,
    history_s: np.ndarray,
    history_val2_loss: np.ndarray,
    current_s: float,
) -> tuple[float, dict]:
    """Map one selected tracked branch into the smoothness used now.

    history_s and history_val2_loss contain only completed historical
    Validation-2 rows. current_s is the newest local minimum obtained from
    the final pre-test Validation-1 surface and therefore has no Validation-2
    loss yet.

    Recent mean/median and pure recency-weighted rules include current_s.
    Loss-weighted rules use only completed historical rows because assigning a
    Validation-2 weight to the current point would require the untouched outer
    test.
    """

    s, loss = _finite_history(history_s, history_val2_loss)
    current_s = float(current_s)
    if not np.isfinite(current_s):
        raise ValueError("current_s must be finite.")

    if spec.family == "last":
        return current_s, {
            "n_history_used": 0,
            "includes_current_s": True,
            "delta": np.nan,
            "rho": np.nan,
        }

    if spec.family == "recent_mean":
        values = _recent_values(s, current_s=current_s, k=int(spec.k))
        return float(np.mean(values)), {
            "n_history_used": int(max(values.size - 1, 0)),
            "includes_current_s": True,
            "delta": np.nan,
            "rho": np.nan,
        }

    if spec.family == "recent_median":
        values = _recent_values(s, current_s=current_s, k=int(spec.k))
        return float(np.median(values)), {
            "n_history_used": int(max(values.size - 1, 0)),
            "includes_current_s": True,
            "delta": np.nan,
            "rho": np.nan,
        }

    if spec.family == "recency_weighted":
        half_life = float(spec.half_life)
        if half_life <= 0.0:
            raise ValueError("half_life must be positive.")
        values = np.concatenate([s, np.asarray([current_s], dtype=float)])
        rho = float(2.0 ** (-1.0 / half_life))
        age = np.arange(values.size - 1, -1, -1, dtype=float)
        weights = rho**age
        selected = float(np.sum(weights * values) / np.sum(weights))
        return selected, {
            "n_history_used": int(s.size),
            "includes_current_s": True,
            "fallback_to_last": False,
            "delta": np.nan,
            "rho": rho,
        }

    if s.size == 0:
        return current_s, {
            "n_history_used": 0,
            "includes_current_s": True,
            "fallback_to_last": True,
            "delta": np.nan,
            "rho": np.nan,
        }

    delta = _scaled_delta(loss)

    if spec.family == "val2_weighted":
        weights = 1.0 / (loss + delta)
        selected = float(np.sum(weights * s) / np.sum(weights))
        return selected, {
            "n_history_used": int(s.size),
            "includes_current_s": False,
            "fallback_to_last": False,
            "delta": delta,
            "rho": np.nan,
        }

    if spec.family == "recency_val2_weighted":
        half_life = float(spec.half_life)
        if half_life <= 0.0:
            raise ValueError("half_life must be positive.")
        rho = float(2.0 ** (-1.0 / half_life))
        age = np.arange(s.size - 1, -1, -1, dtype=float)
        weights = (rho**age) / (loss + delta)
        selected = float(np.sum(weights * s) / np.sum(weights))
        return selected, {
            "n_history_used": int(s.size),
            "includes_current_s": False,
            "fallback_to_last": False,
            "delta": delta,
            "rho": rho,
        }

    raise ValueError(f"Unknown dynamic rule family: {spec.family}")


def evaluate_rule_set(
    branch_history: pd.DataFrame,
    *,
    current_s: float,
    val2_loss_column: str,
    rules: tuple[DynamicRuleSpec, ...] = DEFAULT_RULES,
) -> pd.DataFrame:
    """Evaluate every predeclared branch-to-smoothness rule on one branch."""

    matched = branch_history.loc[
        branch_history["status"].eq("matched")
    ].sort_values("origin_number")

    history_s = matched["smoothness"].to_numpy(dtype=float)
    history_loss = matched[val2_loss_column].to_numpy(dtype=float)

    rows: list[dict] = []
    for spec in rules:
        selected_s, meta = apply_rule(
            spec,
            history_s=history_s,
            history_val2_loss=history_loss,
            current_s=current_s,
        )
        rows.append(
            {
                "rule": spec.name,
                "rule_family": spec.family,
                "k": spec.k,
                "half_life": spec.half_life,
                "selected_s": float(np.clip(selected_s, 0.0, 1.0)),
                **meta,
            }
        )
    return pd.DataFrame(rows)
