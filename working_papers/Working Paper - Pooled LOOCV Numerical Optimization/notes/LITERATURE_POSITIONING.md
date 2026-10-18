# Literature and priority audit — independent numerical LOOCV paper

**Date:** 2026-10-18. This list is an audit agenda and source-grounded position, not an exhaustive novelty search.

| Source | Established point relevant to this work | Consequence |
|---|---|---|
| Guerrero (2007), *Time series smoothing by penalized least squares*, Statistics & Probability Letters 77, 1225–1234 | Statistical PLS formulation and smoothness index, allows nonzero differenced mean | Do not claim index/PLS or μ≠0 idea |
| Cortés-Toto, Guerrero & Reyes (2017), *Trend smoothness achieved by penalized least squares with the smoothing parameter chosen by optimality criteria*, Communications in Statistics—Simulation and Computation 46(2), 1492–1507, DOI 10.1080/03610918.2015.1005236 | CV, GCV, AICc, BIC under 2^4 factorial; attained smoothness studied | Primary direct predecessor and DGP source |
| Craven & Wahba (1979), generalized cross-validation | Classical GCV for linear smoothing | GCV not novel |
| Weinert (2007), *Efficient computation for Whittaker–Henderson smoothing*, Computational Statistics & Data Analysis 52, 959–974 | Fast evaluation of smoother and GCV | Computational comparisons must consider efficient alternatives |
| Mohammadzadeh & Kent, *Global Optimization of the Generalized Cross-Validation Criterion* (user-provided manuscript) | Modified Brent-based global search for GCV | Mere use of Brent for CV global selection is not novelty |
| Hall & Marron (1991), *Local Minima in Cross-validation Functions*, JRSS B 53(1), 245–252 | CV surfaces can have multiple minima, in a different kernel-density setting | No claim first recognition of multimodal CV |
| Biessy (2026), *Whittaker–Henderson smoothing revisited*, ASTIN Bulletin | Modern likelihood/Bayesian framework and parameter selection | Evaluate whether modern smoothers/algorithms are a better benchmark |

**Required source checking before submission:** locate precise bibliographic publication status of the Mohammadzadeh–Kent manuscript; review existing exact rational smoothing-CV optimizers and global polynomial root solvers; verify actual SMCCA venue scope, formatting and policy. Bibliographic metadata not present in supplied source must not be invented.

## Contribution statement to test, not to assert

Proposed: objective-specific stationary-point analysis and numerical recovery for **pooled LOOCV of discrete PLS smoothers**, showing the difference between purely numerical claims and exact small-instance certificates. Only claim a meaningful advance if it survives matched baselines, correctness controls, and prior-art comparison.

## Reference rights

Use existing project literature citations and bibliographic links. Do NOT commit restricted PDFs to this paper, republish manuscripts without permission, or invent new source results.
