# Smoothness Cross Validation — research log

## Completed historical work

| Checkpoint | Focus | Evidence |
| --- | --- | --- |
| CP01 | Pooled future-block validation concept and design | Original exploratory work retained |
| CP02 | Simulation and algorithm design refinement | Original historical decisions retained |
| CP03 | Frozen 3,000-scenario simulation, 72,000 outer decisions | Horizon-matched pooled CV ratios versus one-step CV: 1.000 (h=1), 0.947 (h=3), 0.861 (h=6), 0.762 (h=12) |

These results are historical and specific to the frozen data-generating
conditions and solver. They are not assertions about a future redesigned
simulation or a proof of universal forecast dominance.

## Mathematical research notes — 2026-10-08

- \(\operatorname{rank}(D_d)=L-d\), so \(\dim\ker(D_d)=d\).
- \(Q=D_d^\top D_d\) has exactly the same kernel and is PSD.
- \(I+\lambda Q\) and \(H_\lambda\) are SPD and invertible for
  finite nonnegative \(\lambda\); the fitted trend is unique.
- \(S=1\) corresponds to the **exact** least-squares projection
  onto \(\ker(D_d)\); no \(1-\varepsilon\) approximation is needed.
- \(\operatorname{edf}=L-(L-d)S\), and the pooled forecast-loss
  curve attains a global minimum, possibly more than one.

## Research still in progress

Numerical precision/root-recovery choices, the final simulation
protocol, external forecast comparisons, and the exact
prior-art contribution must be verified before journal submission.
The manuscript is a dated working draft.
