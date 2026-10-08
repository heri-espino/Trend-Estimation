# Claim boundaries — facts, interpretations, hypotheses

**Current as of 2026-10-08. Supersedes all “dynamic tracking is central” overrides.** This paper has its own independent statistical question; its research notes will be used to write a new final manuscript once the study stabilizes.

## Established mathematical facts (under stated model)

- For standard consecutive differences \(1\le d<L\), rank-nullity gives \(\operatorname{rank}(D_d)=L-d\), \(\dim\ker(D_d)=d\); the identity \(x^\top Qx=\|D_dx\|^2\) proves \(\ker(Q)=\ker(D_d)\), hence \(\operatorname{nullity}(Q)=d\).
- For each finite \(\lambda\ge0\), \(I+\lambda Q\succ0\) and \(H_\lambda\succ0\) are invertible; the penalized least-squares fit exists and is unique for all data.
- At \(S=1\), \(H_\infty=U_0U_0^\top\) is singular (rank \(d\), nullity \(L-d\)), but its constrained least-squares fitted trend remains unique. This is an exact projection limit, not a finite matrix inverse or \(1-\varepsilon\) approximation.
- The PLS estimator is \(H_\lambda x\) with \(H_\lambda=(I+\lambda Q)^{-1}\).
- Orthogonal diagonalization of \(Q\) yields scalar spectral shrinkage and an exact polynomial null-space limit.
- The normalized Guerrero-type index \(S\) is continuous, monotone, maps \([0,\infty]\) onto \([0,1]\), and satisfies \(\operatorname{edf}=L-(L-d)S\).
- \(S\) and \(\lambda\) yield the **same fitted estimator family** and interior/global optimum for a fixed objective, including limit endpoints.
- With \(G_{d,h}\) fixed, the derivative identities for \(H\), the prediction, and squared forecast loss are analytic and exact.
- A continuous pooled loss has at least one global minimizer on compact \(S\in[0,1]\); it need not be unique.

## Correct statistical interpretation

- Tuning at \(T\) **does not know the future of \(T\)**. It knows past origins' subsequently observed outcomes.
- The procedure uses past pseudo-out-of-sample future blocks to choose a hyperparameter, then refits and predicts an untouched block.
- It selects smoothness for the **specified** \(d,L,h,G\), loss and historical origin protocol, not an intrinsic timeless property of a series.
- A selected PLS trend extrapolates a polynomial of degree at most \(d-1\). Tuning \(S\) alters polynomial **coefficients**, not \(d\) or the degree.
- Historical latent-trend recovery and future predictive error are different loss targets; whether their minimizers differ depends on data.

## Completed but provisional empirical observations

CP01–CP03 were completed, with preserved artifacts. The historical CP03 simulation showed lower aggregate RMSFE for horizon matching under its frozen DGPs, especially at longer horizons. **These are historical findings**, not predictions of a changed solver or simulation protocol.

## Open hypotheses

- Accurate multi-minimum recovery may matter for choosing the best forecast smoothness.
- Spectral precomputation and analytic derivatives may provide speed/accuracy benefits for large windows.
- Horizon-matched future-block CV may outperform traditional criteria under some or many, but not necessarily all, DGPs.
- The exact originality of the **specific** PLS normalized-index multi-step procedure remains to be determined through more focused prior-art review.

## Do NOT claim

- “We predict the genuinely unseen future during validation.”
- “Forecast-based smoothing, CV, controlled-smoothness forecasting, or Guerrero's \(S\) index was invented here.”
- “Rescaling to \(S\) changes the mathematical optimum or guarantees a unique minimum.”
- “Every (H(S)) is invertible,” “(S=1) has no fitted solution,” or “we must subtract an epsilon at (S=1).”
- “Using future MSE automatically recovers the true trend.”
- “The same optimizer produces the same statistical results when we changed the objective or data.”
- “Every stationary root was found by an unverified Brent/grid search”; or “large-window global minima are rigorously Sturm-certified.”
- “Numerical root completeness implies a certified exact ordering of objective values.”
- “The old simulations are invalid because we plan new ones.”
- “Financial stock/ETF examples demonstrate market predictability or profitable trading.”
- “The current CSSC manuscript has been rebuilt and is submission-ready” unless compiled, visually checked and editorially verified.

## When editing the paper

Keep the main contribution the direct historical future-block MSE selector for \(S\); include spectral and derivative mathematics insofar as they explain efficient evaluation and competing minima. Maintain full outer-test chronology. Cite the closest literature honestly.

See [research_log_2026-10.md](research_log_2026-10.md), [literature_positioning.md](literature_positioning.md), and [next_experiments.md](next_experiments.md).
