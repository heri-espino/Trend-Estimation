# Key Results

This file is the short canonical list of mathematical results currently used by the active research program. Detailed derivations live in separate notes.

## 1. Pure penalized trend

Let

\[
Q=D_d^\top D_d,
\qquad
S_\lambda=(I+\lambda Q)^{-1}.
\]

Then

\[
\boxed{
\widehat t_\lambda=S_\lambda y
}
\]

solves

\[
\min_t\;\|y-t\|_2^2+\lambda\|D_dt\|_2^2.
\]

**Library mapping:** `core/pure.py`, `models/pure_penalized.py`.

**Status:** implemented and tested.

## 2. Smoother sensitivity

\[
\boxed{
S_\lambda'=-S_\lambda Q S_\lambda
}
\]

\[
\boxed{
\widehat t_\lambda'=-S_\lambda Q\widehat t_\lambda
}
\]

\[
\boxed{
\widehat t_\lambda''
=
2S_\lambda Q S_\lambda Q\widehat t_\lambda.
}
\]

**Library mapping:** `core/derivatives.py::pure_trend_derivatives`.

**Status:** implemented and tested against centered finite differences.

## 3. Forecast residual at origin T

For horizon \(h\), let \(H\) denote the linear continuation operator used by the pure model:

\[
r_T(\lambda)
=
y_{T+1:T+h}
-
H S_\lambda y_{\mathrm{past}}.
\]

Then

\[
\boxed{
r_T'(\lambda)
=
H S_\lambda Q S_\lambda y_{\mathrm{past}}.
}
\]

**Library mapping:** `forecasting/extrapolation.py`, `forecasting/objectives.py`.

**Status:** derived and implemented.

## 4. Forecast MSE derivatives

With

\[
f_T(\lambda)=\frac{1}{h}r_T(\lambda)^\top r_T(\lambda),
\]

\[
\boxed{
f_T'(\lambda)
=
\frac{2}{h}
r_T^\top
H S_\lambda Q S_\lambda y_{\mathrm{past}}.
}
\]

Also,

\[
\boxed{
f_T''(\lambda)
=
\frac{2}{h}
\left[
\|H S_\lambda Q S_\lambda y_{\mathrm{past}}\|_2^2
-
2r_T^\top
H S_\lambda Q S_\lambda Q S_\lambda y_{\mathrm{past}}
\right].
}
\]

**Library mapping:** `core/derivatives.py::mse_from_prediction_derivatives`, `forecasting/objectives.py::pure_forecast_loss_derivatives`.

**Status:** implemented with finite-difference tests.

Detailed derivation: `notes/derivative.md`.

## 5. Rolling-origin aggregate objective

For origins \(T_1,\ldots,T_M\),

\[
\boxed{
CV(\lambda)
=
\frac{\sum_j h_j f_{T_j}(\lambda)}
{\sum_j h_j}.
}
\]

and

\[
\boxed{
CV'(\lambda)
=
\frac{\sum_j h_j f_{T_j}'(\lambda)}
{\sum_j h_j},
\qquad
CV''(\lambda)
=
\frac{\sum_j h_j f_{T_j}''(\lambda)}
{\sum_j h_j}.
}
\]

**Library mapping:** `validation/rolling_origin.py`, `forecasting/objectives.py::rolling_pure_forecast_loss_derivatives`.

**Status:** implemented and tested against explicit weighted aggregation.

## 6. Log-lambda transformation

Set

\[
\theta=\log\lambda,
\qquad
g(\theta)=f(e^\theta).
\]

Then

\[
\boxed{
g'(\theta)=\lambda f'(\lambda)
}
\]

and

\[
\boxed{
g''(\theta)
=
\lambda f'(\lambda)+\lambda^2f''(\lambda).
}
\]

Thus

\[
g'(\theta)=0
\iff
f'(\lambda)=0.
\]

**Library mapping:** `selection/numerical.py`.

**Status:** implemented.

## 7. Bracketed stationary-point strategy

On a bounded log-penalty domain:

\[
\boxed{
\text{coarse log-grid}
\rightarrow
\text{bracket sign changes in }g'
\rightarrow
\text{Brent roots}
\rightarrow
\text{classify}
\rightarrow
\text{evaluate stationary points and boundaries}.
}
\]

**Library mapping:** `selection/numerical.py::find_stationary_points_log_lambda`.

**Status:** implemented and tested on a known multimodal objective.

**Important limitation:** a finite discovery grid can miss multiple roots inside one interval or a tangential root with no sign change. Dense/adaptive diagnostic scans remain part of validation.

Detailed note: `notes/numerical_selection.md`.


## 7A. Rational structure of fixed-configuration forecast loss

For fixed \(d,L,h\), let \(\delta_1,\ldots,\delta_r>0\) be the distinct
positive eigenvalues of \(Q=D_d^\top D_d\), where \(r\le L-d\), and define

\[
D(\lambda)=\prod_{j=1}^{r}(1+\lambda\delta_j).
\]

Because every spectral attenuation factor is
\((1+\lambda\delta_j)^{-1}\), the pooled chronological forecast MSE can be
written as

\[
\boxed{
f(\lambda)=\frac{P(\lambda)}{D(\lambda)^2}
}
\]

for a polynomial \(P\) with degree at most \(2r\).

Therefore

\[
\boxed{
f'(\lambda)
=
\frac{R(\lambda)}{D(\lambda)^3},
\qquad
R(\lambda)=P'(\lambda)D(\lambda)-2P(\lambda)D'(\lambda).
}
\]

On \(\lambda\ge0\), \(D(\lambda)>0\), so there are no poles or singularities.
If \(R\not\equiv0\), all interior stationary points are roots of a finite-degree
polynomial and hence are finite in number. A crude degree bound is

\[
\deg R\le 3r-1\le3(L-d)-1.
\]

The monotone mapping from \(\lambda\) to normalized smoothness \(S\) preserves
the interior stationary-point set.

**Interpretation:** the numerical objective is a structured rational function,
not an arbitrary smooth black box. Pathological infinite oscillation is not the
relevant failure mode. The current practical limitation is finite-sampler root
discovery, especially multiple/even-multiplicity roots that may not generate a
sampled derivative sign change.

**Status:** structural result documented; exhaustive certified polynomial-root
isolation is a proposed extension, not yet implemented.

Detailed note: notes/numerical_selection.md.

## 8. Active scientific object

The active paper studies **forecast-optimal trend estimation as an adaptive
forecasting method**. The primary object is the full configuration

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
G(h,X_T,\mathcal C).
}
\]

Here (d) is difference order, (L) is finite-memory window length, (S) is
normalized smoothness, (X_T) describes the local regime, and (mathcal C)
denotes the series class.

The scientific claim is not merely that one tuning parameter varies. The paper
asks whether the complete forecast-optimal method changes systematically with
horizon and local state, and whether that adaptation produces untouched
out-of-sample skill relative to strong fixed configurations.

The persistence/horizon experiment is a **mechanism study** for one component
of this object. It must not be promoted to the definition of the project.

**Canonical source:** `notes/research_objective.md`.

**Library mapping:** experiment-level object assembled from reusable library components.

**Status:** controlled-simulation adaptation value established conditionally; external transfer remains under evaluation.


## 9. Guerrero (2007) plug-in drift

For the literature-aligned feasible estimator,

\[
\widehat m_y
=
\frac{1}{N-d}\mathbf1^\top D_dy,
\]

and

\[
\widehat\tau_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}
\left(
y+\lambda\widehat m_yD_d^\top\mathbf1
\right).
\]

With the observed data fixed,

\[
\boxed{
\partial\widehat m_y/\partial\lambda=0.
}
\]

**Library mapping:** `core/solvers.py::GuerreroSpectralSolver`, `models/guerrero.py::GuerreroTrend`.

**Status:** source definition verified; default library implementation corrected and tested. The historical iterated-drift algorithm is explicit as `IteratedDriftTrend`.


## 10. Fixed lambda is not fixed smoothness when N changes

The normalized smoothness index depends on sample size:

\[
s_d(\lambda;N)
=
\frac{
1-N^{-1}\operatorname{tr}(I+\lambda D_d^\top D_d)^{-1}
}{
1-d/N
}.
\]

Therefore, generally,

\[
\boxed{
s_d(\lambda;N_1)\neq s_d(\lambda;N_2)
}
\]

for \(N_1\neq N_2\).

For the active object \(S^\star_{T,h,L}\), inner validation therefore uses fixed-width windows \(L\) when one common \(\lambda\) is optimized across origins.

**Library mapping:** `core/smoothness.py`, `validation/rolling_origin.py`, `selection/forecast_optimal.py::select_fixed_window_pure_smoothness`.

**Status:** design implication documented and fixed-window selector implemented.

Detailed note: `notes/window_and_smoothness.md`.


## 11. Nested outer evaluation

At outer origin \(T\), define

\[
\mathcal I_T=\{y_1,\ldots,y_T\}.
\]

All hyperparameter selection must be measurable with respect to \(\mathcal I_T\). The implemented information flow is

\[
\boxed{
y_{1:T}
\to
\text{inner selection}
\to
\widehat y_{T+1:T+h\mid T}
\to
\text{reveal future}
\to
\text{score}.
}
\]

Changing only the untouched future block while keeping \(y_{1:T}\) fixed must leave the selected \((d,L,\lambda)\) and forecast unchanged.

**Library mapping:** `validation/nested_forecast.py::nested_rolling_pure_forecast`.

**Status:** implemented and tested by direct future-perturbation invariance.

Detailed note: `notes/nested_validation.md`.

## 12. Oracle recovery objective for simulations

When the latent trend \(\tau\) is known in simulation, define

\[
R(\lambda)
=
\frac1N
\|\tau-S_\lambda y\|_2^2.
\]

Let

\[
\widehat t_\lambda=S_\lambda y,
\qquad
\widehat t_\lambda'=-S_\lambda Q S_\lambda y,
\qquad
\widehat t_\lambda''=2S_\lambda Q S_\lambda Q S_\lambda y.
\]

Then the generic squared-error derivative identities give

\[
R'(\lambda)
=
-\frac{2}{N}
(\tau-\widehat t_\lambda)^\top
\widehat t_\lambda',
\]

and

\[
R''(\lambda)
=
\frac{2}{N}
\left[
\|\widehat t_\lambda'\|_2^2
-
(\tau-\widehat t_\lambda)^\top
\widehat t_\lambda''
\right].
\]

This defines the oracle quantity \(\lambda^\star_{\rm recovery}\), which can be compared with forecast-optimal \(\lambda^\star_{\rm forecast}\) only in simulations.

**Library mapping:** `selection/recovery.py`.

**Status:** implemented, derivative checked against centered finite differences.

## 13. Mandatory no-change benchmark for level forecasts

For a level series,

\[
\widehat y^{(0)}_{T+k\mid T}=y_T,
\qquad k=1,\ldots,h.
\]

The nested evaluator reports

\[
\boxed{
RMSFE_{rel}
=
\frac{RMSFE_{method}}{RMSFE_{no-change}}.
}
\]

For price-level experiments, \(RMSFE_{rel}<1\) means lower pooled level RMSFE than the no-change forecast; it is not by itself evidence of trading profitability.

**Library mapping:** `benchmarks/naive.py`, `validation/nested_forecast.py`.

**Status:** implemented.

## 14. Final paper-scale adaptation result

The final controlled Monte Carlo uses 1,000 seeds per mechanism with
persistence, observation-noise scale, and latent-trend roughness regime
changes. The primary fixed comparator is frozen-all-pre.

The main empirical result is qualified rather than universal:

\[
\boxed{
\text{adaptation value}=q(\text{mechanism},\text{direction},h)
}
\]

Clear positive transition-specific cases include:

- persistence high-to-low at all studied horizons;
- observation-noise high-to-low at all studied horizons;
- latent roughness smooth-to-rough at all studied horizons.

Important boundaries include:

- persistence low-to-high becomes negative at horizons 6 and 12 after
  subtracting the matched stationary-control advantage;
- noise low-to-high is negative at horizon 1 and only modestly positive later;
- roughness rough-to-smooth has near-zero mean transition-specific excess even
  when direct adaptive/fixed ratios improve at longer horizons;
- strong positive persistence at horizon 1 can still favor the no-change
  benchmark over the adaptive trend method.

The complete result is documented in
`notes/checkpoints/2026-09-29_final-1000-seed-monte-carlo-results.md`.

**Status:** paper-scale controlled-simulation evidence established; external
validation remains open.

## 15. First real-data external-validation result

The first observed-data screen transferred the simulation-scale protocol
directly to 16 macro/ETF/stock/crypto series:

[
Lin{24,48,72},qquad M=20.
]

Across 49 series/horizon cells and 10,160 untouched OOS forecast blocks,
adaptive re-selection generally underperformed frozen-all-pre and no-change.

Class-level median adaptive/frozen-all-pre RMSFE was approximately:

- macro: 1.357;
- ETFs: 1.108;
- stocks: 1.122;
- crypto: 1.100.

The result is therefore an external-validity boundary, not evidence of broad
real-data superiority.

A design diagnostic revealed that identical observation-count windows have very
different calendar meanings across quarterly, monthly, and daily classes. A
pre-documented frequency-aware sensitivity is the next experiment; the original
negative result remains preserved.

Full checkpoint:
`notes/checkpoints/2026-09-29_real-data-exploratory-results.md`.

**Status:** first external-transfer screen completed and preserved.

## 16. Frequency-aware external-validity boundary

The pre-documented frequency-aware scale policy uses class-appropriate
estimator windows and selector memory:

[
L_{m quarterly}in{12,24,48},quad
L_{m monthly}in{24,60,120},quad
L_{m daily}in{63,126,252}.
]

Compared with the literal observation-scale transfer, 44 of 49
series/horizon cells improve. Median adaptive/frozen-all-pre RMSFE becomes:

- macro: 1.068;
- ETFs: 1.050;
- stocks: 1.022;
- crypto: 1.003.

Thus class-aware time scale materially improves transfer, but the median
adaptive method still does not beat the strong fixed comparator in any class.

For stocks and crypto, frozen-all-pre is essentially no-change: every studied
cell is within 1% of the no-change benchmark. Adaptive choices overwhelmingly
use d=1 in market data, so the empirical boundary is consistent with the pure
model approaching a constant price-level forecast when first-difference
continuation is combined with very low smoothing.

**Status:** development-panel protocol frozen; confirmatory financial evidence
requires a held-out replication panel.

Full checkpoint:
`notes/checkpoints/2026-09-29_frequency-aware-real-data-results.md`.

## 17. Broad financial external-validity boundary

The frequency-aware financial evidence now spans 92 distinct series across
three panels:

- 32 ETFs;
- 48 stocks;
- 12 crypto assets.

Combined median adaptive/frozen-all-pre RMSFE is approximately:

[
1.032 	ext{(ETF)},qquad
1.022 	ext{(stock)},qquad
1.014 	ext{(crypto)}.
]

The strong frozen-all-pre comparator remains approximately equal to no-change
at the class median.

The result is therefore not that adaptive re-selection never helps, but that
**broad unconditional superiority is not supported for observed financial price
levels**. Gains are series- and horizon-specific, while local re-selection
often moves away from the conservative no-change-like configuration selected by
long historical validation.

One especially clear horizon boundary is stock h=20, where adaptive beats
frozen-all-pre in only 1 of 48 series across the frequency-aware panels.

Full breadth checkpoint:
`notes/checkpoints/2026-09-29_large-universe-financial-results.md`.

**Status:** cross-sectional financial boundary strongly supported; denser
paper-origin and numerical grid sensitivities remain.

