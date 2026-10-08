# Open questions and next experiments — living research agenda

**Status:** research planning, not an instruction to execute expensive runs or to replace existing frozen results.

## Priority A — exact problem and numerical correctness

**Question:** can our current implementation recover the best value of the *same* historical horizon-matched CV surface on \(S\in[0,1]\)?

1. Construct controlled short examples with known or high-precision stationary roots; include endpoint winners, multiple interior minima, nearly flat surfaces, and even-multiplicity stationary points.
2. Compare an exhaustive reference, adaptive derivative brackets + Brent, and the opt-in rational Sturm small-window implementation **on identical inputs**. Report positive root-count discrepancies, locations in \(S\), objective-value regret, and runtime.
3. For full-length windows, compare alternative stable methods that evaluate \(F,F',F''\) using spectral precomputation. Do not claim large-scale Sturm certification unless it actually exists and is verified.
4. Examine \(S\) inversion precision near 0 and 1, null-space projections, eigenvalue tolerances, and loss ties.
5. Decide how the selected *global minimum* is determined if several local minima and two boundaries compete. Track all roots only if it serves scientific insight or numerical search accuracy.

**Decision gate:** freeze an exact numerical algorithm/interface for a new statistical comparison only after the old-vs-new **same objective** check.

## Priority B — does forecast-based smoothness differ from recovery-based smoothness?

**Question:** when does minimizing later predictive MSE lead to a meaningfully different \(S\) from minimizing historical signal recovery or traditional CV/GCV?

- Include simple trend/noise sanity cases, non-polynomial curves, changes in slope, turning points, correlated noise, and heavy tails.
- Compare exactly the same \(d,L,h\) and outer origins across methods.
- Plot the entire \(F_{T,d,L,h}^{\mathrm{pool}}(S)\), competitor choices, and their genuine later forecast errors.
- Measure \(S\)-distance, difference in effective degrees of freedom, forecast loss, and latent-trend reconstruction loss separately.
- Confirm that any gain is not a side effect of different numerical accuracies or inappropriate endpoint exclusions.

## Priority C — is horizon matching essential?

**Question:** how does the best \(S\) change with \(h\)? Does using the \(h\)-step objective outperform a one-step tuned \(S\) on the same outer horizon?

- Fix the evaluation horizon before looking at its outer outcomes.
- Use paired seeds and paired origins.
- Separate benefits of the *forecast loss target* from benefits of denser numerical search.
- Investigate whether the effect survives different window lengths and continuation orders.
- Report failures and uncertainties, not only aggregate wins.

## Priority D — complexity and spectral acceleration

Benchmark cached eigendecomposition vs repeated factorizations; precomputation of the pooled quadratic form; $F,F',F''$ evaluation costs; memory for large L; and sensitivity to the number of historical origins \(M\). Require identical fitted forecasts and numerical tolerances before making speed claims. The prior paper's reported runtime ratios are not automatically those of a new algorithm.

## Priority E — historical multi-minimum geometry and tracking

This is an **open extension**, not the primary experiment. For historical completed forecast-loss surfaces:

- Count and visualize all local minima; characterize their objective values, curvatures, endpoint distance, and movement over time.
- Compare greedy tracking with a pairwise-optimal assignment when branch identity is needed; account for new, disappearing, merging, or crossing minima.
- Test whether tracking produces predictive information beyond pooled CV under explicit changing-roughness hypotheses.
- Use \(\psi\) for branch selection and \(\phi(V_j)\) for the next smoothness only under a declared model of temporal persistence. Preserve information and refit semantics.
- Keep CP04–CP08 negative/mixed results visible so a future study does not quietly cherry-pick a mapping.

## Priority F — novelty and manuscript synthesis

Before writing a final CSSC draft, read/check the closest work: Guerrero 2007/2008, Cortés-Toto et al. 2017, Islas et al. 2019, Islas Camargo & Zumaya Galván 2025, Hart 1994, Vilar-Fernández & Cao 2007, Franke et al. 2026, Biessy 2026. Verify if direct \(h\)-step forecast-CV for finite-difference trends was already studied.

Only **after** methods and experiments stabilize: choose which properties deserve propositions, regenerate figures and tables from new frozen results, decide whether the branch extension belongs in an appendix, write a coherent manuscript from the completed notes, and compile/review its PDF. A journal-compatible draft is not the primary research record while the method is evolving.

## Always keep this separation

- **Mathematical fact:** eigenvalues, monotonic map, resolvent derivatives, polynomial continuation.
- **Implemented computation:** a method tested in code on stated inputs with stated accuracy limits.
- **Numerical hypothesis:** that a new root algorithm is more accurate or cheaper for realistic windows.
- **Statistical hypothesis:** that choosing \(S\) by future-block CV gives better genuinely out-of-sample forecasting performance.
- **Research speculation:** that tracking individual minima and forecasting their trajectories can improve smoothness selection.

These categories cannot substitute for each other.
