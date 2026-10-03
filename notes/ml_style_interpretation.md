# ML-Style Interpretation of Forecast-Optimal Trend Estimation

Date added: 2026-10-03

## Why this note exists

The project can be interpreted as an **ML-style model-selection algorithm for
learning a forecasting trend**, provided we keep the statistical meaning of
each configuration choice explicit.

The central idea is not merely to estimate one smoothed curve. We define a
family of trend-forecasting procedures and use chronological validation to learn
which member of that family is most useful for the forecasting task.

## Three layers of quantities

It is useful to separate three kinds of quantities.

### 1. Structural model choices

These define the class of trends and continuations being considered:

\[
d,\qquad \mu,\qquad \lambda\;\text{or}\;S.
\]

Interpretation:

- \(d\): finite-difference / continuation order; it determines which
  polynomial-like components lie in the penalty null space.
- \(\mu\): reference drift of the \(d\)-th difference. The current pure
  numerical model uses \(\mu=0\).
- \(\lambda\) or normalized smoothness \(S\): strength of penalization
  around the assumed difference structure.

These are analogous to model hyperparameters, but unlike many black-box ML
hyperparameters they have direct statistical interpretations.

### 2. Temporal-memory and selection-protocol choices

The learned forecasting rule also depends on how much data are supplied to the
estimator and to the selector. Important quantities include

\[
L_{\text{fit}},
\qquad
M_{\text{select}},
\qquad
n_{\text{train}},
\qquad
n_{\text{val1}},
\qquad
n_{\text{val2}},
\]

together with the placement and spacing of rolling forecast origins.

Interpretation:

- \(L_{\text{fit}}\): estimator memory; how much recent history is used to fit
  the trend at an origin.
- \(M_{\text{select}}\) or \(n_{\text{val1}}\): selector memory; how much
  past forecast evidence is used to choose the configuration.
- \(n_{\text{train}}\): amount of data available to estimate each candidate.
- \(n_{\text{val2}}\): amount of untouched outer evidence used to compare
  already-selected procedures or assess stability/generalization.

These quantities should be viewed as **protocol hyperparameters** or design
parameters. They can materially change the selected trend because they encode
assumptions about regime persistence, sample size, and how quickly obsolete
history should be forgotten.

However, an untouched outer validation/test block must not be tuned after
inspection. Its size is a design choice fixed before evaluation, not a quantity
to optimize against its own outcomes.

### 3. Task conditions

The forecast horizon

\[
h
\]

is usually not a hyperparameter to be optimized. It is part of the forecasting
task: the user asks for a one-step, five-step, twenty-step, etc. forecast.

The optimal configuration can nevertheless depend strongly on \(h\):

\[
\Theta^\star_{T,h}
\neq
\Theta^\star_{T,h'}
\quad\text{for}\quad h\neq h'.
\]

Thus the algorithm should be understood as learning a configuration
**conditional on the horizon**, not as selecting the horizon itself.

## Expanded configuration view

For conceptual purposes, the learned forecasting rule can be written as

\[
\Theta^\star_{T,h}
=
\arg\min_{\Theta}
\operatorname{Loss}_{\text{future}}(\Theta;h),
\]

with an expanded configuration such as

\[
\Theta
=
\left(
d,
\mu,
S,
L_{\text{fit}},
M_{\text{select}},
n_{\text{train}},
n_{\text{val1}},
\ldots
\right).
\]

The exact canonical coordinate used in a given paper can remain smaller
(e.g. \((d,L,S)\)); this expanded expression is a conceptual description of
the complete learning system.

The method therefore has two nested learning problems:

1. **trend learning:** estimate \(\widehat\tau\) within a candidate
   penalized-smoothing family;
2. **configuration learning:** use chronological future-block loss to select
   the structural and memory choices that define the forecasting procedure.

This is why the project is closer to an adaptive ML-style forecasting
algorithm than to a fixed classical filter.

## Assumptions encoded by the configuration

Each configuration choice expresses a different assumption about the data:

\[
\begin{array}{rcl}
d &:& \text{what shape/evolution is considered structurally smooth?}\\
\mu &:& \text{what systematic drift is allowed in that difference?}\\
L_{\text{fit}} &:& \text{how much historical regime is still relevant?}\\
M_{\text{select}} &:& \text{how much past forecast evidence should guide selection?}\\
S,\lambda &:& \text{how much local movement is treated as signal versus noise?}\\
h &:& \text{how far ahead must the resulting trend extrapolate?}
\end{array}
\]

Therefore no universal configuration should be expected across all series,
frequencies, horizons, or regimes.

## Sample size matters mathematically, not only statistically

The number of observations \(N\) affects more than estimator variance. The
controlled-smoothness mapping itself depends on sample size because

\[
S_d(\lambda;N)
=
1-
\frac{\operatorname{tr}(H_\lambda)}{N}
\]

(up to the normalized version used in the active numerical paper).

Hence the same numerical \(\lambda\) does not represent the same attained
smoothness when \(N\) changes. Window size and sample size therefore alter
both the information available to the estimator and the geometry of the
smoother.

## Important distinction: learning the trend versus evaluating the learner

The chronology must remain nested:

\[
\text{train}
\rightarrow
\text{val1 / inner selection}
\rightarrow
\text{freeze configuration}
\rightarrow
\text{val2 or untouched outer test}.
\]

The outer block is evidence about generalization. It must not be recycled to
choose \(d\), \(L\), \(S\), selector memory, or any other configuration
after its outcomes are observed.

This distinction is essential if we describe the method using ML language:
the project is a hyperparameter-selection algorithm only when the information
sets remain strictly chronological and outer evaluation remains untouched.


## Recommended ML-style selection strategy

For the broader adaptive method, the repository should treat the procedure as
an **interpretable hyperparameter-selection algorithm** rather than as a
single fixed smoother.

A natural implementation is chronological cross-validation over a deliberately
chosen candidate grid. For example,

\[
\mathcal G
=
\mathcal D
\times
\mathcal L
\times
\mathcal S
\times
\mathcal N_{\rm train}
\times
\mathcal N_{\rm val1}
\times
\mathcal N_{\rm val2}
\times
\mathcal H,
\]

where the axes are not arbitrary numbers. Each grid is chosen from assumptions
about the series, sampling frequency, plausible regime duration, expected trend
geometry, and the forecasting task.

For a candidate configuration \(\theta\in\mathcal G\), the chronological
workflow is conceptually

\[
\text{fit on train}
\rightarrow
\text{select / score on val1}
\rightarrow
\text{freeze}
\rightarrow
\text{compare on val2},
\]

with all blocks ordered in time.

A grid is attractive here because the parameters are low-dimensional and
highly interpretable. It lets the analyst encode scientifically plausible
choices instead of pretending that every configuration is equally meaningful.
For example:

- candidate \(d\) values encode assumptions about trend geometry and native
  continuation;
- candidate \(L\) or \(n_{\rm train}\) values encode assumptions about how
  long the current regime remains informative;
- candidate \(n_{\rm val1}\) values encode how much recent forecasting
  evidence should be required before changing the selected configuration;
- candidate \(n_{\rm val2}\) values encode how much later evidence is used
  to assess whether a frozen choice generalizes;
- candidate \(h\) values represent the forecast horizons that matter for the
  application;
- candidate \(S\) or \(\lambda\) values encode the signal-versus-noise
  tradeoff.

Thus \(n_{\rm train}\), \(n_{\rm val1}\), \(n_{\rm val2}\), and \(h\)
**matter materially**. They are not random bookkeeping choices. They determine
what information the learner sees, what evidence the selector uses, how
generalization is measured, and what forecasting problem is being solved.

At the same time, their roles differ:

- \(n_{\rm train}\) and \(n_{\rm val1}\) may legitimately be compared as
  candidate protocol hyperparameters inside a nested chronological design;
- \(h\) is best treated as an application-defined task axis, so the method may
  be re-selected separately for each relevant horizon;
- \(n_{\rm val2}\) is an outer-evaluation design choice. Its value matters
  and should be justified, but once the outer block is designated it must not
  be repeatedly changed after inspecting its outcomes.

Therefore the recommended default is **assumption-informed grid search with
strict temporal CV**, not unconstrained random search. Random search or other
optimizers can be useful later when the configuration space becomes large, but
the first scientific implementation should keep the grid small, interpretable,
and tied to explicit assumptions about the data.

A useful conceptual distinction is

\[
\boxed{
\text{candidate grid}
=
\text{scientific assumptions translated into testable configurations}
}
\]

rather than

\[
\text{candidate grid}
=
\text{arbitrary combinations tried until one wins}.
\]

This point should be stated explicitly when the project is described as an
ML-style trend-learning algorithm.

## Wording for future papers

Safe framing:

> We treat penalized trend forecasting as a structured model-selection
> problem. Difference order and smoothness determine the trend class, finite
> memory determines the information supplied to the estimator, and
> chronological validation determines which configuration is preferred for a
> given horizon and local regime.

Also safe:

> The procedure can be viewed as an interpretable ML-style forecasting
> algorithm in which both the trend and the configuration used to extrapolate
> it are learned from temporally ordered data.

Avoid saying that every data split size is automatically a scientific
hyperparameter. Some are **protocol design parameters**, especially the final
untouched evaluation size, and must remain fixed rather than optimized after
inspection.
