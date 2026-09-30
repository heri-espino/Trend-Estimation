# Wording Dictionary

This file is the manuscript wording guide for the active numerical paper.

The goal is to keep the language close to established literature and avoid
invented terminology, overclaiming, or ambiguous uses of familiar words.

## Preferred terminology

| Prefer | Avoid by default | Reason |
|---|---|---|
| **penalized least squares (PLS)** | regularized trend learner | PLS is the established term in the core literature. |
| **smoothing parameter \(\lambda\)** | hyperparameter, regularization knob | The literature consistently calls \(\lambda\) the smoothing parameter or smoothing constant. |
| **trend smoothness** | trend regularity score | Established wording. |
| **smoothness index** | smoothness metric, smoothness score | Established wording in Guerrero/Cortés-Toto. |
| **controlled smoothness approach** | controlled smoothing method | Matches the source literature. |
| **percentage of smoothness** | smoothness percentage score | Use only for the literature's percentage interpretation. |
| **normalized smoothness coordinate \(S\)** | percentage of smoothness | Distinguishes the active paper's exact \([0,1]\) normalization from historical variants. |
| **difference order \(d\)** | polynomial degree | They are related through the null space but are not interchangeable concepts. |
| **smoother matrix / smoothing matrix** | smoothness matrix | Standard linear-smoother terminology. |
| **effective degrees of freedom** | number of parameters | Trace-based effective dimension is not literal parameter count. |
| **forecast origin** | prediction date, cutoff point | Standard forecast-evaluation terminology. |
| **forecast horizon \(h\)** | lookahead | Standard terminology. |
| **rolling-origin evaluation** | temporal CV | More precise. |
| **rolling-window evaluation** | sliding CV | Standard term in the cited forecast-evaluation literature. |
| **rolling forecast-validation objective** | CV score | Makes clear that the objective is chronological and forecast-based. |
| **\(h\)-step-ahead forecast loss** | future error | Precise and conventional. |
| **trend forecasting / trend extrapolation** | predicting the smoother | Source-aligned wording. |
| **stationary point** | critical solution | Conventional calculus terminology. |
| **local minimum** | mode | Avoids confusion with probability distributions. |
| **multiple local minima** | multimodality | Clearer in a numerical-optimization paper. |
| **sign-change bracket** | root interval | More specific. |
| **Brent root refinement** | Brent optimization | Brent is only the root-refinement stage here. |
| **adaptive stationary-point search** | smart optimizer | Describes the actual procedure. |
| **endpoint-aware refinement** | boundary trick | Neutral and descriptive. |
| **dense reference grid** | ground truth | A finite grid is not exact truth. |
| **objective regret** | optimization loss | The latter is ambiguous with forecast loss. |
| **missed reference minimum** | algorithm failure | Use the more precise event; reserve failure for aggregate interpretation. |
| **smoothness-domain endpoint** | endpoint | Prevents confusion with temporal endpoints. |
| **time-series endpoint** | endpoint | Prevents confusion with \(S=0,1\). |
| **observed series** | raw signal | Source-aligned and neutral. |
| **estimated trend** | recovered truth | A trend estimate is not necessarily a true latent object. |

## Canonical explanatory phrases

Use these constructions freely, with normal rewriting to fit the surrounding
text.

### Penalized least squares

> The smoothing parameter trades off fidelity to the observed data against
> smoothness of the estimated trend.

This is the central intuitive sentence for \(\lambda\).

### Small and large \(\lambda\)

Prefer:

> As \(\lambda\to0\), the fitted trend approaches the observed series; as
> \(\lambda\to\infty\), increasing priority is given to smoothness.

When discussing the exact limiting estimator, continue with the null-space
description.

Avoid:

> Large \(\lambda\) removes all variation.

That is false for the unpenalized null-space component.

### Normalized smoothness

Prefer:

> We reparameterize the smoothing problem by a normalized smoothness coordinate
> \(S\in[0,1]\).

Then state the formula immediately.

Avoid:

> We introduce a new percentage of smoothness.

The literature already contains percentage-of-smoothness indices, and the
active paper's normalization should be distinguished from them.

### Relation to controlled smoothness

Prefer:

> The coordinate is motivated by the controlled-smoothness literature but is
> normalized here so that the two limiting smoothing regimes correspond exactly
> to \(S=0\) and \(S=1\).

Do not claim that the exact active-paper formula is Guerrero's original index
unless the algebraic normalization is stated explicitly.

### Forecast validation

Prefer:

> For fixed \((d,L,h)\), smoothness is selected by minimizing a rolling
> \(h\)-step-ahead forecast-validation objective.

Prefer:

> At each forecast origin, the trend is estimated using only information
> available at that origin.

Avoid:

> We use cross-validation on the time series.

That wording is too broad and hides the chronological design.

### Fixed window

Prefer:

> We use rolling-window evaluation with training-window length \(L\).

If the fit is re-estimated at every origin, say so.

Avoid:

> The model is trained on a moving validation window.

The training window and validation target are different objects.

### Multiple minima

Prefer:

> The forecast-validation objective can contain multiple local minima.

Avoid:

> The objective is always nonconvex.

The experiments establish multiple-minimum examples, not a universal theorem
of nonconvexity for every configuration.

### Numerical target

Prefer:

> The algorithm is designed to recover relevant local minima and exact boundary
> optima.

Avoid:

> The algorithm finds every stationary point.

That stronger statement is neither required nor established.

### Dense benchmark

Prefer:

> We benchmark the adaptive search against a dense reference grid.

Avoid:

> We compare against the exact solution.

The dense grid is a numerical reference. Continuous root refinement can even
produce a lower objective value between grid points.

### Regret

Prefer:

> Positive objective regret measures how much larger the selected objective
> value is than the dense-grid reference value.

If regret is negative, explain that continuous refinement found a point between
reference grid nodes.

### Efficiency

Prefer one of:

> The adaptive search used X% of the dense-grid objective evaluations.

> The adaptive search reduced the evaluation count by a factor of X.

For runtime:

> On this implementation and hardware, the observed wall-clock ratio was X.

Avoid:

> The method is X times faster.

unless the implementation/hardware qualifier is nearby.

### Robustness

Prefer:

> The result was stable over the tested orders, windows, horizons, and
> simulation regimes.

Avoid:

> The method is robust.

unless the tested scope is named.

### Financial series

Prefer:

> We use financial series as a real-data numerical geometry stress test.

Avoid:

> We validate financial predictability.

The numerical paper is not a forecasting-superiority or trading paper.

## Important distinctions

### Smoothing vs forecasting

**Smoothing** estimates the historical trend from observations.

**Forecasting/extrapolation** extends that estimated trend beyond the forecast
origin.

Do not use the two verbs interchangeably.

### Reconstruction CV/GCV vs forecast validation

Classical smoothing CV/GCV evaluates reconstruction or prediction properties of
the smoother under its own criterion.

The active paper evaluates **chronological future forecast loss**.

Write this distinction explicitly in the introduction and related-work section.

### Smoothness-domain endpoint vs time-series endpoint

Use:

- *time-series endpoint* for the beginning/end of the observed sample;
- *smoothness-domain endpoint* for \(S=0\) or \(S=1\).

Never use *endpoint problem* without qualification.

### Smoother matrix vs smoothness coordinate

Because the literature often uses \(S_\lambda\) for the smoothing matrix and
this project uses \(S\) for normalized smoothness, use \(H_\lambda\) for the
matrix in the active paper.

### Optimal vs selected

Use *selected smoothness* for a value returned by a finite numerical procedure.

Use *forecast-optimal smoothness* only after the objective has been specified,
for example:

> forecast-optimal with respect to the rolling \(h\)-step MSE objective.

Avoid an unqualified *optimal smoothing parameter* when several criteria
(CV, GCV, AICc, BIC, marginal likelihood, forecast loss) are possible.

## Claim-strength ladder

Use the weakest statement supported by the evidence.

1. **Observed:** “In the tested surfaces, ...”
2. **Stable within design:** “The result was stable across the tested ...”
3. **Numerical evidence:** “The benchmark provides numerical evidence that ...”
4. **Method claim:** “The proposed search recovered ... under the benchmark
   design.”
5. **Do not write without proof:** “The method guarantees recovery of all
   stationary points.”

## Terms reserved for specific contexts

### Hodrick-Prescott filter

Use *HP filter* only for the \(d=2\) special case and its established
econometric interpretation. The general PLS estimator should not be called the
HP filter.

### Whittaker-Henderson smoothing

Use *Whittaker-Henderson smoothing* when positioning the broader finite-
difference penalized-smoothing family, especially the actuarial/statistical
literature.

### Trend filtering

Use only when referring to the specific \(\ell_1\) trend-filtering literature,
such as Kim et al. (2009), not as a synonym for quadratic PLS.

## Source-aligned verbs

Prefer:

- *estimate a trend*;
- *smooth a time series*;
- *select / choose the smoothing parameter*;
- *attain / achieve a level of smoothness*;
- *fix a desired percentage of smoothness* when discussing controlled
  smoothness;
- *evaluate forecasts*;
- *advance / move the forecast origin*;
- *recalibrate / refit at each origin*;
- *extrapolate the trend*;
- *recover / detect local minima*;
- *refine a root bracket*;
- *compare with a dense reference*.

Avoid inflated verbs such as *discover*, *unlock*, *revolutionize*, or *solve
the smoothing problem* unless the sentence is literally about solving a
well-defined linear system.
