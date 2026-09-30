# Decisions Log

## N001 — Sole active research paper

**Date:** 2026-09-30  
**Status:** frozen until this paper is finished.

paper_numerical-smoothness-selection/ is the only active research paper.
The adaptive and financial-recurrence papers are parked.

## N002 — Main contribution is numerical

The paper is judged on the numerical problem and algorithm. Finance may provide
example surfaces, but financial recurrence/model comparison is not required for
the central claim.

## N003 — Smoothness is the scientific coordinate

Search on \(S\in[0,1]\). \(\lambda\) remains the internal estimator
coordinate and derivative coordinate where convenient.

## N004 — Do not assume unimodality

Return multiple stationary points/local minima. The global candidate is selected
only after all detected minima and boundaries are compared.

## N005 — Maximum five epsilon-separated representative minima

After root discovery, rank detected local minima by objective value and greedily
keep at most five. When a minimum at \(s\) is retained, suppress worse minima
within \([s-\varepsilon,s+\varepsilon]\).

Initial sensitivity:
\[
\varepsilon\in\{0,0.02,0.05,0.10,0.15\}.
\]

This spacing is post-processing; it must not alter stationary-point discovery.

## N006 — Dense grid is a reference, not the proposed method

Dense evaluation is used to estimate missed-minimum risk and optimum agreement.
It is not the algorithmic contribution.

## N007 — No universal root-discovery guarantee without assumptions

Do not claim that a finite adaptive sampler finds every stationary point of an
arbitrary smooth objective.

## N008 — Discrete \(d,L,m,h\) variation is stress testing

The numerical paper may repeat the continuous \(S\)-search across discrete
configurations, but it does not claim joint adaptive optimization of those
quantities.


## N009 — Freeze primary numerical search before paper-scale runs

**Date:** 2026-09-30  
**Status:** frozen.

The primary adaptive-\(S\) search is frozen with

\[
\begin{aligned}
\text{initial grid size} &= 9,\\
\text{endpoint refinement levels} &= 6,\\
\text{maximum adaptive depth} &= 8,\\
\text{minimum interval width} &= 10^{-3},\\
\text{derivative tolerance} &= 10^{-8},\\
\text{curvature tolerance} &= 10^{-8},\\
\text{near-zero derivative ratio} &= 0.2,\\
\text{Brent root tolerance} &= 10^{-10},\\
\text{interior boundary margin} &= 10^{-6}.
\end{aligned}
\]

Exact \(S=0\) and \(S=1\) are always evaluated separately and compared with all
detected interior local minima.

This specification was frozen after the endpoint-aware quick benchmark recovered
227/227 dense-reference interior minima across 216 synthetic
forecast-validation surfaces with zero positive objective regret.

## N010 — Paper-scale benchmark is confirmatory for the frozen search

Paper-scale benchmark results may characterize performance, failure rate,
accuracy, and computational cost, but must not be used to retune N009.

Search-design sensitivity may still be reported as a robustness analysis. If
an alternative setting performs differently, it is reported as sensitivity;
the primary algorithm remains N009 unless a genuine implementation error is
discovered.

## N011 — Stationary inflections are outside the primary optimization claim

The target is recovery of relevant local minima and exact boundary optima.
The paper does not claim certified recovery of every stationary point of an
arbitrary smooth objective. In particular, a tangential stationary inflection
that is not a local minimum is not counted as an optimization failure.
