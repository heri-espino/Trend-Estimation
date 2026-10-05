> **Scope update (2026-10-05):** This file is the historical canonical objective for the broader adaptive \((d,L,S)\) paper, now parked at \`paper_forecast-optimal-smoothing/\`. It is **not** the global source of truth for the two active methodological papers. Start at root \`AI_HANDOFF.md\` and \`RESEARCH_MAP.md\`; use \`paper_smoothness-cv/notes/research_objective.md\` for the criterion paper and \`paper_numerical-methods/notes/research_objective.md\` for the numerical paper.

# Canonical Research Objective

Date clarified: 2026-09-22

This note is the **first scientific source of truth** for the active paper.
Read it before interpreting experiments, changing the roadmap, or editing the
manuscript.

## Canonical statement

> **Forecast-optimal trend estimation as an adaptive forecasting method, where
> smoothness, memory length and difference order depend on horizon and local
> regime.**

The project is not primarily an AR(1)-persistence paper, a new
cross-validation rule, or a fixed-\`lambda\` smoothing paper. Those are
components or diagnostics inside the larger forecasting problem.

## Formal object

At forecast origin \(T\) and horizon \(h\), define the forecasting-method
configuration

\[
\Theta_{T,h}=(d_{T,h},L_{T,h},S_{T,h}),
\]

where

- \(d\) is the finite-difference order;
- \(L\) is the finite-memory estimation-window length;
- \(S\) is normalized smoothness (with \(\lambda\) the numerical penalty
  parameter that induces it for a given \(d,L\)).

The central empirical object is

\[
\boxed{
\Theta^\star_{T,h}
=
\left(
d^\star_{T,h},
L^\star_{T,h},
S^\star_{T,h}
\right)
=
G(h,X_T,\mathcal C),
}
\]

where \(X_T\) contains observable local-state descriptors and \(\mathcal C\)
denotes the series class.

Candidate local descriptors include

\[
X_T=
(
\widehat\sigma_T,
\widehat\rho_{1,T},
\text{trend strength},
\text{break evidence},
\text{local roughness},
\ldots
).
\]

Do **not** reduce local regime to volatility alone or persistence alone unless
the evidence eventually supports that simplification.

## What "optimal" means here

The scientific target must be defined before a smoothing parameter is called
optimal. The active paper defines optimality by future forecast loss:

\[
\Theta^\star_{T,h}
=
\arg\min_{\Theta}
E\!\left[
\mathcal L\!\left(
Y_{T+1:T+h},
\widehat Y_{T+1:T+h\mid T}(\Theta)
\right)
\,\middle|\,
\mathcal F_T
\right],
\]

with \(\mathcal F_T=\sigma(Y_1,\ldots,Y_T)\).

This is distinct from at least two classical targets:

\[
\lambda^\star_{\rm recovery}
=
\arg\min_\lambda
E\|\widehat\tau_\lambda-\tau\|^2,
\]

and selectors such as GCV/AIC whose optimality is defined through their own
risk or information criteria.

The paper therefore studies a **forecasting method**, not merely a smoother.


## ML-style interpretation and protocol hyperparameters

The project can also be viewed as a structured, interpretable
**ML-style model-selection algorithm for learning a forecasting trend**.

The model-side configuration includes quantities such as \(d\), \(\mu\),
smoothness \(S\) / penalty \(\lambda\), and estimator-memory length \(L\).
The temporal selection protocol also has consequential design parameters,
including training-sample size, inner-validation / selector-memory length, and
the size and placement of later untouched evaluation blocks.

These quantities do not all play the same role:

- \(d,\mu,S,\lambda,L\) describe or constrain the candidate trend model;
- training and inner-validation sizes determine how much evidence is available
  to fit and select that model;
- \(h\) is normally a task condition, not something optimized;
- the final outer validation/test size is an evaluation-design parameter and
  must be fixed before inspection rather than tuned to improve reported
  performance.

Conceptually, one may write an expanded configuration

\[
\Theta
=
\left(
d,\mu,S,L_{\mathrm{fit}},M_{\mathrm{select}},
n_{\mathrm{train}},n_{\mathrm{val1}},\ldots
\right),
\]

while retaining \((d,L,S)\) as the smaller canonical coordinate of the
current adaptive paper when that narrower definition is required.

This makes the scientific interpretation explicit: each series, horizon,
frequency, and local regime can support a different configuration because each
configuration encodes assumptions about trend geometry, drift, memory,
noise-versus-signal tradeoff, and the amount of evidence required for stable
selection.

The full conceptual note is:

`notes/ml_style_interpretation.md`


### Recommended hyperparameter-selection view

For the broader adaptive algorithm, use **strictly chronological cross-validation
over an assumption-informed candidate grid** as the default conceptual
framework. The grid may include

\[
(d,S,L,n_{\rm train},n_{\rm val1},n_{\rm val2},h)
\]

or the appropriate subset for a particular experiment.

These quantities are not arbitrary bookkeeping choices. They encode assumptions
about trend geometry, regime duration, available estimation history, selector
memory, required external evidence, and forecast horizon. In particular,
\(n_{\rm train}\), \(n_{\rm val1}\), \(n_{\rm val2}\), and \(h\) can
materially change the selected method and the measured forecasting problem.

Use an interpretable grid first because the candidate values should come from
the data frequency, plausible cycle/regime scales, the application horizon,
and explicit modeling assumptions. Do not use an arbitrary grid merely to
search for favorable results.

Guardrail: \(n_{\rm val2}\) matters, but once it defines an untouched outer
evaluation block it is not to be tuned after seeing that block. Likewise, treat
\(h\) primarily as a task axis and re-select the forecasting configuration
conditional on each relevant horizon rather than choosing the horizon by
validation performance.



## Statistical assumptions and claim discipline

For the active numerical smoothness-selection paper, the canonical model is the
**zero-drift, identity-weighted** finite-difference PLS smoother,

[
widehat{	au}_{lambda,d}
=
argmin_{	au}
left{
|y-	au|_2^2+lambda|D_d	au|_2^2
ight},
]

that is, the special case (V=I) and (mu=0) of the broader Guerrero
formulation.

These are **modeling assumptions / design choices**, not empirical truths about
every series.

Important consequences:

- (V=I) gives an unweighted Euclidean data-fit criterion. Under a stochastic
  interpretation it corresponds to equal marginal observation-error variance
  and zero cross-time covariance. It does **not** imply independence without
  additional assumptions such as joint Gaussianity.
- (mu=0) centers the (d)-th difference penalty at zero and fixes the native
  continuation class: constant for (d=1), linear for (d=2), quadratic for
  (d=3), etc.
- Standard (D_d) assumes equally spaced time indices unless an appropriate
  irregular-time operator is introduced.
- For the numerical paper, (d,L,h) are fixed and the one-dimensional
  smoothness coordinate is optimized. Therefore "forecast-optimal" always
  means optimal **conditional on this model family, loss, horizon, window, and
  validation protocol**.
- The differentiated objective is forecast **MSE**. RMSE has the same minimizer
  for a fixed set of errors, but the analytic derivatives in the paper are
  those of MSE.
- Rolling-origin losses are generally dependent because windows and future
  blocks overlap. They may be averaged for selection, but should not be treated
  as i.i.d. observations for naive inference.
- Chronological CV assumes that past forecast performance is informative for
  the target future to some useful degree. Regime changes can break that
  relationship; validation-optimal and later-test-optimal configurations may
  differ.
- Brent is a **root-refinement method after bracketing**, not a global optimizer.
  The adaptive sampler, endpoint refinement, classification, and exact boundary
  checks form the full numerical search.
- A finite adaptive search cannot guarantee recovery of every stationary point
  of every smooth objective. Dense grids are numerical references, not
  mathematical truth.

The core numerical method does **not** require Gaussian errors, independent
errors, or a correct likelihood. Those stronger assumptions are needed only if
we invoke stronger probabilistic interpretations such as
(lambda=sigma_Z^2/sigma_arepsilon^2).

Claim guardrail: do not state that the selected trend is the "true trend", that
(mu=0) or (V=I) is empirically true, that Brent guarantees the global
optimum, that forecast-optimal smoothness is recovery-optimal smoothness, or
that the financial stress test establishes predictability or trading value.

Detailed note:

`paper_numerical-methods/notes/assumptions_and_claim_boundaries.md`

## Three-level scientific structure

### Level I — Target dependence

Establish that trend-recovery optimality and forecasting optimality need not
coincide:

\[
\Theta^\star_{\rm forecast}
\neq
\Theta^\star_{\rm recovery}.
\]

The first controlled simulations already provide provisional evidence for this
separation.

### Level II — Mechanisms

Explain why the forecast-optimal configuration changes. Candidate mechanisms
include:

- residual persistence and its sign;
- signal-to-noise structure;
- latent-trend roughness;
- forecast horizon;
- endpoints;
- structural breaks and regime changes.

Mechanism studies explain parts of \(G\); none of them individually defines the
paper.

### Level III — Adaptation value

Test whether the forecast-optimal method changes systematically with local
state and whether adapting to that state improves untouched future forecasts:

\[
\Theta^\star_{T,h}=G(h,X_T,\mathcal C),
\]

and

\[
E[L_{\rm adaptive}]
<
E[L_{\rm fixed}]
\]

where supported by the data.

This third level is established conditionally in controlled simulation. Its
external transfer to observed series remains unresolved.

## Role of the persistence experiment

\`notes/experiments/02_persistence-horizon-mechanism.md\` is a **mechanism
study** prompted by the first factorial simulation. It asks why strong serial
dependence changes selected smoothness.

Its provisional decomposition,

\[
S^\star_{\rm observed}
<
S^\star_{\rm AR}
<
S^\star_{\rm latent}
<
S^\star_{\rm recovery},
\]

in some high-positive-persistence regimes is evidence about one mechanism:
when predictable residual dynamics are omitted, a trend-only forecast can
absorb part of them by changing its smoothness.

This result must **not** be restated as the objective of the project.

The AR-aware forecast uses oracle \(\phi\) and is a diagnostic, not the proposed
real-data forecasting method.

## Why window length is a first-class parameter

Finite memory is not just a validation convenience. In a heterogeneous or
changing process, \(L\) trades estimation variance against contamination from
older regimes:

\[
L\uparrow
\Rightarrow
\begin{cases}
\text{more data and usually lower estimation variance},\\
\text{more exposure to observations from an obsolete regime}.
\end{cases}
\]

Thus \(L^\star_{T,h}\) is part of the adaptive forecasting object, alongside
difference order and smoothness.

## Experimental program

The intended progression is:

1. **Target study:** compare forecast-optimal and recovery-optimal choices.
2. **Mechanism studies:** persistence, horizon, roughness, signal-to-noise,
   endpoints.
3. **Within-series regime transitions:** change persistence, roughness, noise
   scale, level/slope, or break structure inside one series and measure how
   \(\Theta^\star_{T,h}\) adapts.
4. **Adaptation value:** compare adaptive selection with fixed configurations
   under untouched outer evaluation.
5. **External evidence:** macroeconomic series, then indices/ETFs, equities,
   and crypto.
6. **Forecast-comparison inference:** use appropriate unconditional and
   conditional predictive-ability tools where justified.

For within-series transitions, a useful estimand is adaptation delay:

\[
D_{\rm adapt}
=
\inf\left\{
k:
\Theta^\star_{T_0+k,h}
\approx
\Theta^\star_{\rm post}
\right\}.
\]

## Current evidence versus open claims

### Already implemented / supported

- exact pure penalized trend and derivatives;
- derivative-aware forecast-loss optimization;
- fixed-window and nested chronological selection;
- no-change benchmark;
- controlled latent-trend simulations;
- provisional evidence that forecast and recovery optima differ;
- persistence/horizon mechanism evidence robust to a much wider lambda-search
  domain;
- within-series persistence transitions in which the joint
  \((d^\star,L^\star,S^\star)\) configuration moves toward matched
  target-regime controls;
- evidence that selector memory and estimator memory are distinct: shortening
  inner-selector memory substantially reduces observed adaptation delay;
- under both M=20 and M=30 selector-memory protocols, adaptive
  re-selection beats frozen-pre hyperparameters in pooled OOS RMSE for both
  persistence-transition directions at every studied horizon;
- the persistence transition-specific excess adaptation-value sign pattern is
  robust to M=20 versus M=30: strongest and most consistent for high-to-low
  persistence, and positive for low-to-high persistence at short horizons;
- observation-noise scale is a second demonstrated regime mechanism: the joint
  configuration moves toward matched target controls when noise changes;
- noise-scale adaptation value is strongly directional: high-to-low noise has
  large direct and transition-specific gains, while low-to-high noise has weak
  or absent transition-specific value at the studied sample size;
- latent-trend roughness is a third distinct configuration mechanism: both
  transition directions move toward matched stationary target controls;
- smooth-to-rough transitions show large direct adaptive gains;
- the stronger frozen-all-pre comparator removes the major stationary
  high-roughness fragility of frozen-local-M20;
- smooth-to-rough adaptive gains remain large against frozen-all-pre, whereas
  rough-to-smooth becomes approximately a tie, clarifying the validity
  boundary of adaptation value.
- the final 1,000-seed Monte Carlo confirms these mechanism-,
  direction-, and horizon-dependent adaptation effects with substantially
  lower Monte Carlo noise; persistence high-to-low, noise high-to-low, and
  roughness smooth-to-rough are the clearest positive cases, while several
  opposite-direction/horizon cells are near-neutral or negative.
- the first observed-data screen, using the literal
  simulation-scale policy L={24,48,72}, M=20 across all frequencies, is mostly
  negative relative to frozen-all-pre and no-change; this is preserved as an
  external-validity boundary and motivates one pre-documented
  frequency-aware scale diagnostic rather than repeated post-hoc tuning.

### Not yet established

- whether the controlled-simulation adaptation gains transfer under a
  frequency-appropriate real-data scale policy;
- whether a frozen real-data protocol replicates on a separate held-out panel;
- vintage-correct macroeconomic performance using ALFRED real-time data;
- that any financial improvement is economically exploitable;
- final novelty relative to the complete literature target set.

## Selector-memory guardrail

The canonical coordinate (L) is the amount of past data supplied to the
fitted trend model. It must not be conflated with the amount of historical
forecast-validation evidence retained by the inner selector.

Let (M) denote, informally, the number of inner rolling origins retained by
the validation protocol. (M) is currently a protocol parameter, not a fourth
coordinate of (Theta^star).

Exploration 04 showed that the slow low-to-high persistence adaptation is close
to the time required for old-regime inner validation origins to leave the
selector. Exploration 04B confirmed that selector memory is a major source of
adaptation inertia.

For the controlled-simulation program, M=20 was the frozen adaptive-selector
memory because it remained within about 2.5% of the M=30 stable-control
reference while adapting materially faster. Retain M=30 as a simulation
robustness setting.

For real-data work, do not assume that M=20 has the same time-scale meaning
across quarterly, monthly, and daily series. The frequency-aware diagnostic
ties selector-history span to the candidate window scale.

Do not silently interpret (M) as (L), and do not add (M) to the canonical
adaptive object unless later evidence shows that it must itself be selected
adaptively.

## Numerical-search status

The original persistence study exposed many optima near the first
log-\(\lambda\) boundaries. The required wider-domain sensitivity was
completed using

\[
\log\lambda\in[-18,24]
\]

with a denser discovery grid, and the qualitative persistence/horizon
mechanism survived. The wide domain is now part of the active experimental
protocol rather than an outstanding prerequisite.

## Literature positioning

The literature workspace intentionally spans several blocks:

1. penalized smoothing and smoothing-parameter selection;
2. endpoints, causality, and time-series validation;
3. forecast comparison and conditional predictive ability;
4. structural change and regime heterogeneity;
5. financial and cryptocurrency applications;
6. numerical optimization.

The 40-paper target set is recorded in \`literature/manifest.csv\`. As of this
clarification, **24 papers are present in \`literature/extracted/\`**. Do not
claim that the full target literature audit is complete until the remaining
high-priority sources have been ingested and reviewed.

## Anti-drift rules for future agents

Before changing the scientific story:

1. read this file;
2. read \`notes/roadmap.md\` and \`notes/key_results.md\`;
3. distinguish the central objective from the most recent experiment;
4. treat persistence as one mechanism, not as the definition of regime;
5. keep \((d,L,S)\) together when describing the adaptive forecasting method;
6. distinguish forecast optimality from trend-recovery optimality;
7. distinguish a validation protocol from a scientific contribution;
8. do not make novelty claims from only the currently extracted 24 papers;
9. preserve strict information-set causality at every forecast origin;
10. use real-data benchmarks appropriate to the series class.

## Scope exclusions

The active paper is not primarily about:

- portfolio optimization or trading utility;
- decision-optimal smoothing;
- a universal new smoother;
- a universal new CV scheme;
- AR(1) persistence by itself.

Those may be robustness analyses, diagnostics, or future papers, but they must
not displace the canonical objective above.
