# Literature still needed

The current repository corpus contains strong finite-difference, smoothing-spline, P-spline, and trend-filtering references, but it does not yet contain the direct Bézier/Bernstein and spline-forecasting papers required for a defensible novelty claim.

## Priority 0 — must acquire/read before claiming novelty

| Priority | Reference | Why necessary | Local corpus |
|---|---|---|---|
| P0 | Kim, Kim, Park, Hong & Jeong (1999), Smoothing techniques via the Bezier curve, DOI 10.1080/03610929908832374 | Direct statistical Bézier smoothing; closest historical prior | MISSING |
| P0 | Farouki (2012), The Bernstein polynomial basis: A centennial retrospective, DOI 10.1016/j.cagd.2012.03.001 | Authoritative Bernstein/Bézier mathematics and endpoint derivatives | MISSING |
| P0 | Wang & Ghosh (2012), Shape restricted nonparametric regression with Bernstein polynomials, DOI 10.1016/j.csda.2012.02.018 | Modern statistical Bernstein regression and constrained LS | MISSING |
| P0 | Lukoseviciute et al. (2018), Bernstein polynomials for adaptive evolutionary prediction of short-term time series, DOI 10.1016/j.asoc.2018.01.002 | Direct Bernstein time-series forecasting | MISSING |
| P0 | Bak, Shin & Koo (2022/2023), Intrinsic spherical smoothing method based on generalized Bézier curves and sparsity inducing penalization, DOI 10.1080/02664763.2022.2054962 | Direct penalized Bézier smoothing/control-point selection | MISSING |
| P0 | A Study on Metal Futures Price Prediction Based on Piecewise Cubic Bézier Filtering for TCN (2025), DOI 10.3390/app15179792 | Recent direct financial Bézier filtering precedent | MISSING |
| P0 | Currie, Durban & Eilers (2004), Smoothing and forecasting mortality rates, DOI 10.1191/1471082X04st080oa | P-spline smoothing plus forecasting | MISSING |
| P0 | Ugarte et al. (2009), Spline smoothing in small area trend estimation and forecasting, DOI 10.1016/j.csda.2009.02.027 | Direct trend estimation, basis extension, forecasting, forecast MSE | MISSING |
| P0 | Blöchl (2014), Penalized Splines as Frequency Selective Filters — Reducing the Excess Variability at the Margins, DOI 10.5282/ubm/epub.20687 | Direct endpoint/margin instability literature | MISSING |

## Priority 1 — basis equivalence and endpoint theory

Search and add literature on:

- Bernstein–Bézier versus B-spline change-of-basis matrices;
- Bézier extraction and conversion of spline segments to Bernstein form;
- penalized Bernstein regression;
- difference penalties under nonorthogonal basis transformations;
- equivalent kernels/effective degrees of freedom for penalized basis smoothers;
- endpoint behavior and boundary bias of smoothing splines and P-splines;
- spline extrapolation and derivative-constrained continuation;
- \(C^1\) and \(C^2\) continuation of piecewise cubic Bézier curves;
- stable extrapolation from Bernstein polynomials outside \([0,1]\).

## Priority 2 — forecasting and dependence

Search for:

- spline-based trend extrapolation in time series;
- P-spline forecasting after 2009;
- smoothing-spline forecasting;
- Bernstein-basis forecasting after 2018;
- Bézier financial filters after 2025;
- forecast-horizon-specific tuning of spline/control-point penalties;
- penalized splines under serially correlated errors;
- data-driven smoothing selection under time-series dependence.

## Questions every new paper must answer

For each candidate reference, record:

1. Is the target smoothing/reconstruction or forecasting?
2. Is validation chronological?
3. What basis is used?
4. Where does the penalty act: fitted values, derivatives, coefficients, control points, or velocity differences?
5. Is the model global or piecewise?
6. How is complexity/order chosen?
7. How are endpoints treated?
8. How is extrapolation defined?
9. Is there a closed-form linear smoother?
10. Are derivatives with respect to the smoothing parameter available?
11. What is genuinely left for this paper?

## Local-corpus integration rule

Once PDFs are legally obtained, place them under the existing literature PDF workflow, extract them with the repository extraction pipeline, and regenerate literature/extracted/bundle.md. Do not hand-edit the generated bundle.
