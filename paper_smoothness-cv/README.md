# Forecast-optimal smoothness by chronological forecast validation

**Status: ACTIVE — manuscript rewritten for Journal of Forecasting on 2026-10-05.**

**Primary target journal:** *Journal of Forecasting*.

**Working title:** *Forecast-Optimal Smoothness for Penalized Trend Estimation*.

## Scientific question

For a fixed finite-difference trend family and forecast horizon, what amount of smoothness should be selected when the tuning target is genuinely future forecast performance?

The paper defines

\[
S^\star_{d,L,h}
\in
\arg\min_{S\in[0,1]}
F_{d,L,h}(S),
\]

where \(F_{d,L,h}\) is chronological rolling future-block MSE.

## Direct lineage

The paper should be narrated primarily as

\[
\text{Guerrero controlled smoothness}
\longrightarrow
\text{forecast-selected smoothness}.
\]

Guerrero supplies finite-difference PLS, the trace-based smoothness interpretation, and trend continuation. The new step is to select the smoothness percentage from forecast performance instead of specifying it exogenously.

Hart (1994) is an important predictive-smoothing precedent, not the direct model foundation. More recent *Journal of Forecasting* papers by Taylor, Zafar et al., Staněk, Wolff and Echterling, Franjic and Schweikert, and Xu et al. establish a journal-facing literature on forecast-oriented smoothing, tuning, and out-of-sample evaluation.

## Core model

\[
\widehat\tau_\lambda
=
H_\lambda y,
\qquad
H_\lambda=(I+\lambda D_d^\top D_d)^{-1}.
\]

Normalized smoothness:

\[
S(\lambda)
=
1-\frac{1}{L-d}
\sum_{\delta_j>0}
\frac{1}{1+\lambda\delta_j}.
\]

At origin \(T\),

\[
\widehat z_T(S)
=
G_{d,h}H_{\lambda(S)}x_T.
\]

For rolling origins,

\[
F_{d,L,h}(S)
=
\frac{1}{Mh}
\sum_{j=1}^M
\left\|
z_{T_j}
-
G_{d,h}H_{\lambda(S)}x_{T_j}
\right\|^2.
\]

The exact effective-degrees-of-freedom relation is

\[
\operatorname{edf}
=
L-(L-d)S.
\]

## Paper ownership

This paper owns:
- the definition and interpretation of forecast-optimal smoothness;
- the normalized \(S\)-coordinate;
- the chronological future-block tuning criterion;
- horizon dependence;
- forecast-optimal versus recovery-optimal smoothness;
- the scientific forecasting evaluation.

It does **not** own:
- Brent/adaptive root search/Sturm certification — paper_numerical-methods/;
- post-selection bias/variance/inference — paper_statistical-properties-penalized-trend/;
- joint adaptive selection of \((d,L,S)\) — paper_forecast-optimal-smoothing/.

## Manuscript

The active Wiley manuscript is:

paper_smoothness-cv/manuscript/main.tex

The inherited WTI/Journal of Futures Markets text that was accidentally copied with the Wiley template has been removed from this paper.

Current manuscript structure:

1. Introduction
2. Related work and positioning
3. Finite-difference penalized trend estimation
4. Forecast-optimal smoothness
5. Basic properties
6. Evaluation protocol
7. Scope, interpretation, and implications
8. Conclusion

The manuscript deliberately contains **no fabricated empirical results**. Section 6 freezes the intended comparison protocol before the final test results are generated.

## Build

Compiler-free structure check:

~~~bash
python paper_smoothness-cv/build.py --check
~~~

Compile locally with XeLaTeX/BibTeX available:

~~~bash
python paper_smoothness-cv/build.py
~~~

Expected output:

paper_smoothness-cv/EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf

GitHub Actions also has a manual smoothness-cv target under **Build papers**. Heavy paper compilation remains manual-only.

## Final empirical package still required

The current manuscript is method/theory plus a prespecified evaluation protocol. Before submission, run and freeze:
- forecast-CV versus CV/GCV/AICc/BIC;
- forecast-optimal versus recovery-optimal smoothness in controlled simulations;
- one-step tuning versus horizon-matched \(h\)-step tuning;
- public multi-series forecast evaluation;
- submission-grade real-time macro vintages if macro backtests are retained.

Current-vintage FRED histories are exploratory only for historical macroeconomic evaluation; use real-time vintages for paper-final backtests.

## Read first

1. manuscript/main.tex
2. AI_HANDOFF.md
3. notes/research_objective.md
4. notes/literature_positioning.md
5. notes/journal_of_forecasting_positioning.md
6. notes/claim_boundaries.md
7. notes/roadmap.md

## Current execution checkpoint

Checkpoint 01 empirical code is implemented. Read `checkpoints/CP01_EMPIRICAL_CORE.md` and `notes/empirical_roadmap.md` before running simulations. Run smoke first, then quick, commit the generated `results/smoothness_cv/checkpoint_01/` directory, and stop for review before the paper preset.
