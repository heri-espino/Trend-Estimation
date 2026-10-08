from __future__ import annotations

import numpy as np

from experiments.numerical_smoothness_selection.run_tracking_correspondence_benchmark import (
    Candidate,
    EPSILONS,
    N_TIMES,
    REGIMES,
    _optimal_assignment,
    _positions,
    _run_case,
    _score_step,
)


def test_exact_pairwise_assignment_can_recover_two_when_greedy_only_matches_one():
    # Nearest individual edge is A -> X, but then B has no admissible match.
    previous = {"a": 0.40, "b": 0.48}
    current = {"a": 0.34, "b": 0.43}
    greedy = _score_step(previous, current, epsilon=0.10, method="greedy")
    global_pairwise = _score_step(
        previous, current, epsilon=0.10, method="global_pairwise"
    )
    assert greedy["matched"] == 1
    assert global_pairwise["matched"] == 2
    assert global_pairwise["correct"] == 2


def test_global_pairwise_never_returns_two_matches_to_same_candidate():
    assignment = _optimal_assignment(
        {"a": 0.40, "b": 0.48},
        [Candidate("b", 0.43), Candidate("a", 0.34)],
        epsilon=0.10,
    )
    ids = [index for index, distance in assignment.values()]
    assert len(ids) == len(set(ids))


def test_position_sets_stay_normalized_and_birth_death_events_are_known():
    assert set(_positions("birth_death", 0, 42)) == {"a", "b", "c"}
    assert set(_positions("birth_death", 20, 42)) == {"a", "b", "c", "d"}
    assert set(_positions("birth_death", N_TIMES - 1, 42)) == {"b", "c", "d"}
    for regime in REGIMES:
        for t in range(N_TIMES):
            values = np.asarray(list(_positions(regime, t, 4).values()))
            assert values.size > 0
            assert np.all(np.isfinite(values))
            assert np.all((values >= 0) & (values <= 1))


def test_all_benchmark_presets_produce_chronological_rows():
    for regime in REGIMES:
        for epsilon in EPSILONS:
            rows = _run_case((0, regime, epsilon))
            assert len(rows) == 2 * (N_TIMES - 1)
            assert all(r["method"] in {"greedy", "global_pairwise"} for r in rows)
