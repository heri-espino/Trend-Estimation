# Applied case-study design

## Motivation

The current manuscript establishes that the adaptive method can recover the
relevant minima of a multimodal rolling forecast-validation objective.

What it does not yet make visually clear is **what two different local minima
mean for the estimated trend and its extrapolation**.

The applied section should answer:

> If two smoothness values are both local minima of forecast CV, what changes
> in the trend estimate, what changes in the forecast path, and how do those
> choices behave on data that were not used to select them?

## Proposed data families

Use already tracked snapshots whenever possible.

### Macroeconomic

**Series:** FRED `GDPC1` — U.S. real GDP, quarterly.

Role: demonstrate a relatively smooth macroeconomic series with structural
changes and a natural multi-quarter forecast horizon.

### ETF

**Series:** SPY or QQQ, daily log price.

Role: broad market trend with persistent local movement and high-frequency
noise.

### Stock

**Series:** AAPL or XOM, daily log price.

Role: firm-specific trend geometry distinct from a broad ETF.

### Cryptocurrency

**Series:** BTC-USD or ETH-USD, daily log price.

Role: high-volatility series where rough and smooth trend estimates can imply
substantially different continuation paths.

## Experimental separation

For each series split time chronologically into:

1. **development/selection region** — used for rolling forecast CV and local
   minimum discovery;
2. **final untouched test block** — never used to choose (S), example,
   epsilon, (d), (L), or (h).

The test block is for interpretation only.

The example-selection rule must depend only on the development region. A
possible deterministic rule is:

1. evaluate a pre-specified set of ((d,L,h));
2. retain configurations with at least two epsilon-separated local minima;
3. among them choose the configuration with the largest smoothness separation
   between its two best local minima;
4. break ties lexicographically by ((d,L,h)).

This deliberately selects a visually informative multimodal example **without
using test performance**.

## Candidate smoothness values

For a chosen configuration, retain:

- the global minimum of rolling forecast CV;
- up to two additional epsilon-separated local minima;
- exact (S=0) or (S=1) only if one is itself competitive/relevant;
- optional GCV-selected smoothness as a literature reference.

Do not call the alternatives “wrong” minima. They are different local optima of
the same validation criterion.

## What to plot

### Panel A — objective geometry

Plot

[
Smapsto F_{d,L,h}(S)
]

with:

- dense reference curve for visualization;
- adaptive evaluation points;
- detected local minima;
- global selected minimum;
- optional GCV choice.

This panel shows why a single unimodal scalar optimizer can be insufficient.

### Panel B — fitted trends

At the final development origin, fit the trend using every retained candidate
(S_k) on exactly the same training window.

Plot:

- observations;
- (widehat	au_{S_1},widehat	au_{S_2},ldots).

This shows the scale of variation each local optimum preserves.

### Panel C — forecast and untouched test

Continue each fitted trend using the same native finite-difference continuation
rule.

Plot:

- forecast origin;
- candidate forecast paths;
- untouched test observations.

Report test MSE underneath or in a compact accompanying table.

The test result illustrates consequences of the candidates; it does not
retroactively select or tune them.

## Why several minima can arise

With eigendecomposition

[
Q=Uoperatorname{diag}(delta_j)U^	op,
]

the smoother acts component-wise through

[
alpha_j(lambda)
=
rac{1}{1+lambdadelta_j}.
]

Changing (lambda) therefore changes different penalized components at
different rates.

For in-sample smoothing this already creates a nonlinear criterion profile. In
forecast validation there is another layer: the continuation operator maps the
smoothed endpoint level and finite differences into future observations.

Two smoothing levels can therefore represent distinct compromises:

- a rougher trend follows recent movements and extrapolates a stronger local
  slope/curvature;
- a smoother trend suppresses those movements and extrapolates a more stable
  low-frequency path.

Across rolling origins, the squared forecast errors from these compromises can
cross repeatedly. Their average need not be convex or unimodal, so several
local minima can appear.

This is an interpretation of the numerical mechanism, not evidence that each
minimum corresponds to a distinct latent economic regime.

## Expected manuscript role

This section should probably replace part of the current “financial geometry
stress test” narrative rather than simply adding pages.

The numerical benchmark establishes correctness and efficiency.

The case studies establish **why the multiple-minimum problem matters in
practice**.

Together the paper becomes:

[
	ext{forecast-CV smoothness selection}
ightarrow
	ext{multiple meaningful candidate trends}
ightarrow
	ext{need for reliable multi-minimum search}
ightarrow
	ext{validated adaptive method}.
]
