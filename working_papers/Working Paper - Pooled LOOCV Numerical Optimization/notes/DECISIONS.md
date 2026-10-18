# Research decisions and unresolved issues

## D001 — 2026-10-18 — Independent manuscript
**Decision:** new stand-alone working paper. Neither a section of the older Numerical Methods working paper nor an extension of the horizon-matched forecast CV paper. No forecasting language or objectives.

## D002 — 2026-10-18 — Exact selection target
**Decision:** first average LOOCV MSE scores over R comparable series *at a common smoothing parameter*, then minimize the pooled function. Do not average argmins. R=1 is the non-pooled classical comparator.

## D003 — 2026-10-18 — Index semantics
**Decision:** optimize in λ or log λ numerically, report normalized S∈[0,1], and present original Guerrero index separately. Fixed d and N within pools. Evaluate endpoint λ=0,∞ exactly, not by epsilon surrogates.

## D004 — 2026-10-18 — Numerical honesty
**Decision:** bounded Brent = local; multibracket derivative Brent = uncertified sign-changing-root search; exact Sturm = small rational inputs only. Dense grid = finite numerical reference. Classification and numerical completeness still need validation.

## D005 — 2026-10-18 — Source-inspired design
**Decision:** preserve the four primary factors of Cortés-Toto et al. (2017); treat R pooling as a transparent additional factor. Use independent seeds and preserve simulated latent trend exclusively for descriptive reconstruction/oracle diagnostics, never feasible tuning.

## D006 — 2026-10-18 — Financial example
**Decision:** potentially include an index and an exchange rate with documented adjusted-price/source/preprocessing and no forecasting or investment-return claim. Do not download unlicensed/raw market data into the repository automatically.

## Open decisions
- Is there a genuine improvement over existing *global* CV optimization algorithms?
- Which score scaling permits economically sensible multi-asset pooling?
- Whether derivative-sign-only bracketing is insufficient; consider certified interval methods if empirical misses are material.
- Whether the journal scope should emphasize computational algorithms or statistical simulation.
- Whether experiments favor LOOCV, GCV, or no difference: negative results must be documented.
