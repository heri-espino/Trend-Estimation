# Dynamic Branch Selection — independent notes

**Current design (2026-10-08):** track local minima of **temporally
weighted forecast-loss surfaces** by fixed method \(m\), order \(d\),
window \(L\), horizon \(h\). The current method does **not** use
the old Val1/Val2 transformed-loss branch definition.
See [shared protocol](../../WEIGHTED_SURFACE_PROTOCOL.md)
and [current mathematical specification](dynamic_tracked_smoothness.md).

- [Research question and protocol](research_objective.md)
- [Tracked smoothness and V/psi/phi rules](dynamic_tracked_smoothness.md)
- [Temporal minima correspondence](temporal_minima_tracking.md)
- [Completed experiments and limitations](results_and_boundaries.md)
- [Legacy mathematical branch draft](tracked_minimum_smoothness_selection_legacy.tex)

All chronology and ownership are defined by this independent study.
Numbers from completed checkpoints are preserved, including negative findings.
Unrun matching experiments must never be treated as results.
