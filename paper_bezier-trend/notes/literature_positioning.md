# Literature positioning

Last audit: 2026-10-05.

This note separates established prior work from the candidate gap.

## A. Literature already in the repository corpus

### Whittaker (1923)

Historical origin of finite-difference penalized least squares / graduation.

Role here: baseline lineage for penalties on sampled trend values.

### Guerrero (2007), Time series smoothing by penalized least squares

Already in the local corpus.

Role here: direct time-series PLS foundation and controlled-smoothness interpretation.

### Cortés-Toto, Guerrero & Reyes (2017)

Already in the local corpus.

Role here: compares smoothing-parameter criteria in finite-difference PLS and explicitly connects the \(d=2\) PLS problem to cubic smoothing splines.

### Eilers & Marx (1996), Flexible Smoothing with B-splines and Penalties

Already in the local corpus.

DOI: 10.1214/ss/1038425655

Critical implication: P-splines already use a spline basis and difference penalties on neighboring basis coefficients. Therefore

\[
\|D_q\beta\|^2
\]

on a Bernstein/Bézier coefficient vector is not automatically a new idea.

This is the most important conceptual rival.

### Kim et al. (2009), l1 Trend Filtering

Already in the local corpus.

Role here: rival regularization geometry. It penalizes trend differences with an \(\ell_1\) norm and yields piecewise-polynomial structure.

## B. Direct Bézier/Bernstein literature found in the novelty audit

### Kim, Kim, Park, Hong & Jeong (1999)

**Smoothing techniques via the Bezier curve.**
Communications in Statistics — Theory and Methods 28(7), 1577–1597.

DOI: 10.1080/03610929908832374

Establishes explicit statistical Bézier smoothing for density and regression functions, including smoothing parameters and asymptotic MISE analysis.

Consequence: do not claim first statistical Bézier smoother.

### Farouki (2012)

**The Bernstein polynomial basis: A centennial retrospective.**
Computer Aided Geometric Design 29(6), 379–419.

DOI: 10.1016/j.cagd.2012.03.001

Role: authoritative mathematical/computational reference for Bernstein basis, Bézier geometry, derivatives, numerical stability, and control-point interpretation.

### Wang & Ghosh (2012)

**Shape restricted nonparametric regression with Bernstein polynomials.**
Computational Statistics & Data Analysis 56(9), 2729–2741.

DOI: 10.1016/j.csda.2012.02.018

Establishes Bernstein-basis regression with constrained least squares and asymptotic analysis.

Consequence: basis regression itself is not novel.

### Lukoseviciute, Palivonaite, Howard & Ragulskis (2018)

**Bernstein polynomials for adaptive evolutionary prediction of short-term time series.**
Applied Soft Computing 65, 47–57.

DOI: 10.1016/j.asoc.2018.01.002

Establishes direct Bernstein-polynomial short-term time-series prediction, including financial examples and adaptive smoothing/model selection.

Consequence: do not claim first Bernstein time-series forecasting method.

### Bak, Shin & Koo (2022/2023)

**Intrinsic spherical smoothing method based on generalized Bézier curves and sparsity inducing penalization.**
Journal of Applied Statistics 50(9), 1942–1961.

DOI: 10.1080/02664763.2022.2054962

Establishes penalized Bézier smoothing. Their setting is spherical/Riemannian data and their local velocity-difference penalty induces control-point sparsity/order selection.

Consequence: do not claim first penalized Bézier curve.

### Applied Sciences (2025) metal-futures application

**A Study on Metal Futures Price Prediction Based on Piecewise Cubic Bézier Filtering for TCN.**
Applied Sciences 15(17), 9792.

DOI: 10.3390/app15179792

Establishes piecewise cubic Bézier filtering explicitly as a financial time-series trend/filtering component before a forecasting model.

Consequence: do not claim first Bézier filter for financial forecasting.

## C. P-spline forecasting literature that directly challenges the candidate contribution

### Currie, Durban & Eilers (2004)

**Smoothing and forecasting mortality rates.**
Statistical Modelling 4(4), 279–298.

DOI: 10.1191/1471082X04st080oa

Shows P-spline smoothing and forecasting in a time-indexed setting and treats forecasting as a natural extension of the smoothing construction.

### Ugarte, Goicoa, Militino & Durbán (2009)

**Spline smoothing in small area trend estimation and forecasting.**
Computational Statistics & Data Analysis 53(10), 3616–3629.

DOI: 10.1016/j.csda.2009.02.027

Directly studies penalized spline trend estimation and future forecasting, including explicit extension of the B-spline basis beyond the observed domain and forecast MSE.

This is a mandatory comparator for any endpoint/extrapolation claim.

### Blöchl (2014)

**Penalized Splines as Frequency Selective Filters — Reducing the Excess Variability at the Margins.**
Munich Discussion Paper.

DOI: 10.5282/ubm/epub.20687

Directly studies excessive variability at time-series endpoints/margins and proposes time-varying penalization to improve the most recent trend estimates.

This directly overlaps with the endpoint motivation.

### Data-driven P-spline smoother for time series (2025/2026 literature)

A recent paper studies penalized spline smoothing for deterministic trends with time-series errors and data-driven smoothing-parameter selection, including financial volatility applications.

This literature must be audited before claiming that forecast-oriented tuning or dependent-error treatment is new.

## D. Candidate gap after this audit

The still-plausible gap is narrower:

1. a direct mathematical comparison between finite-difference regularization in sampled-trend space and regularization in a Bernstein/Bézier control space;
2. explicit endpoint continuation constructed from terminal Bernstein/Bézier derivative geometry;
3. leakage-free chronological tuning of both smoothing and continuation;
4. matched benchmarking against P-splines and smoothing splines so any observed gain cannot be attributed merely to switching basis;
5. theory characterizing when the two regularization spaces are equivalent, approximately equivalent, or genuinely different.

This is a hypothesis, not a novelty claim.

## E. Thesis / antithesis / synthesis

### Thesis

A control representation may offer a low-dimensional, geometrically interpretable description of endpoint level, slope, and curvature and may stabilize trend forecasts.

### Antithesis

P-splines already regularize basis coefficients, Bernstein regression is established, P-splines already forecast beyond the sample, and Bézier filtering has already appeared in financial forecasting.

### Synthesis

The paper is worth pursuing only if endpoint continuation or the regularization geometry creates a distinct reproducible forecasting problem after matching effective degrees of freedom and spline baselines.
