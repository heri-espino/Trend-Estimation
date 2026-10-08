# Proposed final manuscript outline — CSSC (not yet frozen)

**2026-10-08:** The present \`manuscript/\` is a *working CSSC-oriented draft* based on old frozen runs. We will assemble the final research article only after validating the new numerical approach and conducting the chosen comparisons. This outline is a plan, not evidence that a new run has happened.

**Working topic:** *Horizon-Matched Cross-Validation for Forecast-Optimal Penalized Trend Smoothness*. Title is provisional.

## Intended narrative

1. **Introduction — the counterfactual future problem.** The smoothness producing the best retrospective trend is not necessarily the one producing the best forecast. At \(T\), we cannot see future \(y_{T+1:T+h}\). We can score forecasts made at past origins after their futures have been observed. Define the horizon-matched problem.
2. **Closest literature and novelty limits.** Guerrero (2007/08), Cortés-Toto et al. (2017) in CSSC, Hart (1994), Vilar-Fernández and Cao (2007) in CSSC, Islas et al. (2019), Islas Camargo and Zumaya Galván (2025), Franke et al. (2026), Biessy (2026). Do not overclaim the index, PLS, predictive tuning or trend forecasting.
3. **PLS smoothing and spectral interpretation.** \(D_d,Q,U,\delta,H_\lambda\), rank-nullity and \(\ker(Q)=\ker(D_d)\), strict convexity and invertibility at finite penalty, the exact singular-but-well-defined constrained least-squares endpoint \(S=1\), why diagonalization is useful computationally.
4. **Normalized index \(S\in[0,1]\).** Relation to trace/edf, monotone mapping, inverse \(\lambda(S)\), meaning of a bounded common optimization domain. Explicit caveat: equivalent global estimator to \(\lambda\) tuning.
5. **Future continuation and chronological CV.** Native \(G_{d,h}\), polynomial degree \(d-1\), candidate future-block loss, pooled \(F_{T,d,L,h}^{\mathrm{pool}}(S)\), information availability, mandatory final refit.
6. **Mathematical analysis of forecast-MSE objective.** Quadratic-in-predictions expansion; resolvent \(H',H'',H^{(n)}\); analytic \(f',f''\) and chain rule to \(S\). Examples of multiple extrema, endpoints, existence and nonuniqueness. Separate method and numerical guarantees clearly.
7. **Numerical experiments and implementation diagnostics (to redesign).** Same-objective algorithm comparisons, eigen-based speed/correctness, endpoint and multi-root cases; describe *only what has actually been run*.
8. **Statistical simulation evidence (to decide and freeze).** Horizon-matched vs one-step CV, ordinary CV/GCV/AICc, latent reconstruction and future oracles; paired outer origins, noise/trend mechanisms and horizon dependence.
9. **Discussion.** Loss target versus recovery; what changes with \(d\), \(L\), \(h\); failures; literature limits; optional temporal tracking as further question.
10. **Conclusion.** Exactly what has been demonstrated, with reproducibility and caveats. Appendix only if tracking \(V_j\) has a clear role after new tests.

## Figures worth considering (not promises)

- \(S(\lambda)\), eigenvalue shrinkage and edf for a fixed \((L,d)\);
- several fitted historical trends and their *future continuations* from the same origin as \(S\) changes;
- forecast-MSE \(F_h(S)\) across horizons, with **all** recovered minima and both endpoints;
- same-input old vs new numerical method: objective regret, root recovery, runtime;
- paired outer-test forecast ratios and selected \(S\) by horizon/mechanism;
- latent-recovery vs forecast-selected \(S\), clearly marked oracle data.

Avoid a manuscript dominated by lengthy CP04–08 branches unless they answer the current statistical question. Their archived figures/results remain accessible separately.

## Reader should leave knowing

- Why it makes sense to choose \(S\) by **historically observed futures** rather than by the future we cannot observe now.
- How \(H(S)\), eigenshrinkage, terminal differences and future polynomial forecasts fit together.
- How/why we differentiate and numerically minimize an MSE surface with potentially many minima.
- What was genuinely better in outer forecasting and under what assumptions.
- Which aspects were already in the literature and what remains conjectural.

[Research objective](research_objective.md) · [Mathematical foundations](mathematical_foundations.md) · [Next experiments](next_experiments.md)
