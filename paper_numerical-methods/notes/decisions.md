> **2026-10-05 override:** Decision N001 ("sole active research paper") is superseded by the paper split. There are now two linked active methodological papers: \`paper_smoothness-cv/\` owns the forecast-optimal smoothness criterion, and \`paper_numerical-methods/\` owns its numerical solution. Decisions N002 onward remain in force unless explicitly contradicted by the new split documents.

# Decisions Log

## N001 — Sole active research paper

**Date:** 2026-09-30  
**Status:** frozen until this paper is finished.

paper_numerical-methods/ is the only active research paper.
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

## N012 — Confirmatory paper-scale benchmark passed

**Date:** 2026-09-30  
**Status:** frozen result.

Under the frozen N009 specification, the paper-scale synthetic benchmark
matched 2105/2105 dense-reference interior minima across 1920
forecast-validation surfaces. The adversarial paper benchmark detected 240/240
known relevant minima/boundary optima.

These results close the primary algorithm-validation phase. Subsequent
experiments must not change the N009 primary specification unless a genuine
implementation error is discovered.

## N013 — Epsilon spacing is post-processing only

**Date:** 2026-09-30  
**Status:** frozen.

The epsilon rule is applied only after stationary-point discovery and
classification. Candidate minima are sorted by objective value before spacing,
so the best detected local minimum is never removed.

The paper may use \(\varepsilon=0.10\) as a representative summary setting and
report sensitivity over
\(\{0,0.02,0.05,0.10,0.15\}\), but epsilon is not part of the primary
optimization algorithm.

## N014 — Numerical paper fixes the forecast continuation rule

**Date:** 2026-09-30  
**Status:** frozen scope decision.

The numerical paper uses the native finite-difference continuation associated
with the penalized trend model. Its controlled breadth varies \(d\), \(L\),
\(h\), and simulation regime.

Multiple forecast/extrapolation model comparisons (AR/ARIMA, state-space,
alternative trend continuation rules, and related model selection) belong to
the parked applied financial-trend paper. The numerical paper therefore writes
its objective as

\[
F_{d,L,h}(S)=CV_h(d,L,S),
\]

without a separate forecast-method index \(m\).

## N015 — Principal numerical experiments are complete

**Date:** 2026-09-30  
**Status:** frozen result.

The frozen N009 search matched:

- 240/240 relevant known adversarial minima/boundary optima;
- 2105/2105 dense-reference interior minima across 1920 synthetic
  forecast-validation surfaces;
- 473/473 dense-reference interior minima across 384 real financial
  forecast-validation surfaces.

No further primary numerical experiments or tuning are planned. Real financial
results are interpreted only as numerical geometry stress tests, not as evidence
of forecasting superiority, predictability, or trading value.


## N016 — Temporal local-minimum tracking is now in scope

**Date:** 2026-10-06  
**Status:** active extension.

The numerical paper no longer stops at solving each forecast-loss surface in isolation.
It also owns the numerical correspondence problem for local minima across adjacent
chronological surfaces.

For per-origin minimum sets

\[
\mathcal M_t=\{S_{1,t},\ldots,S_{K_t,t}\},
\]

the baseline temporal continuation rule is one-to-one matching under

\[
|S_{j,t}-S_{j,t-1}|\le\varepsilon.
\]

This `track_epsilon` is distinct from N013 candidate spacing, which acts only
within a single surface after root discovery.

The frozen N009 per-surface solver remains unchanged. Temporal tracking is a
new layer built on top of its recovered minima.

The forecasting decision rules applied to a tracked branch, including last,
mean/median, Validation-2 weighting, and recency weighting, belong to
`paper_smoothness-cv/` rather than this numerical paper.

## N017 — Only two papers are active

**Date:** 2026-10-06  
**Status:** active repository policy.

The only active papers are:

1. `paper_smoothness-cv/` — dynamic forecasting decision from tracked smoothness minima;
2. `paper_numerical-methods/` — recovery and temporal tracking of those minima.

Other paper directories are historical/parked and must not receive new research work
unless the user explicitly reactivates them.
