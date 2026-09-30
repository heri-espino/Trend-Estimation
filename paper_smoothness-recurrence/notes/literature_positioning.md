# Literature Positioning — Forecast Selection, Likelihood, and Extrapolation

Last updated: 2026-09-29

## Closest antecedents

### Guerrero (2007)

Introduces penalized least-squares trend smoothing and a normalized smoothness
index. This is the origin of the smoothness coordinate used in this project.

### Cortes-Toto, Guerrero, and Reyes (2017)

Compares CV, GCV, AICc, and BIC for choosing the smoothing parameter in
penalized least squares. Therefore, "choose the PLS smoothing parameter by CV"
is not itself a novel contribution.

Their CV target is smoothing/reconstruction rather than the explicitly
h-step-ahead chronological forecast-loss objective used here.

### Biessy — Whittaker-Henderson smoothing revisited

A particularly close modern reference. It gives a probabilistic/Bayesian
interpretation of Whittaker-Henderson smoothing, selects smoothing parameters
through marginal likelihood/LAML, studies numerical optimization, and develops
an extrapolation procedure. In one dimension, difference-penalty extrapolation
continues as a polynomial of degree q-1.

Consequences for this paper:

- marginal-likelihood or REML selection must be treated as a benchmark, not as
  our novelty;
- extrapolation of penalized trends is not new by itself;
- the numerical contribution must remain focused on the forecast-loss objective
  in normalized smoothness space, its multiple local minima, and efficient
  stationary-point discovery;
- the empirical question is whether forecast-targeted selection improves
  validation/test h-step performance relative to likelihood-selected smoothing;
- financial recurrence is an application of the selected forecast trend, not
  the core methodological novelty.

## Proposed positioning

The paper should contrast two principles for defining a useful trend:

1. **probabilistic fit:** choose smoothing from likelihood / marginal likelihood;
2. **predictive fit:** choose smoothing from chronological h-step forecast loss.

For the proposed method,

\[
S^\star_{d,L,m,h}
=
\arg\min_{S\in[0,1]}CV_h(d,L,m,S),
\]

where the continuous objective may be multimodal. The numerical contribution is
to identify its relevant local minima efficiently rather than evaluate a dense
grid by default.

The strongest result would not merely be that forecast CV selects a different
S. It would show, on untouched data, when and by how much that different
selection improves h-step trend forecasting relative to likelihood selection.
