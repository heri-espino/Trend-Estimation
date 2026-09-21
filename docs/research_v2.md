# Research design

The repository is a reusable research library that can support multiple papers. The current active paper is `paper_forecast-optimal-smoothing/`; the decision-aware/portfolio branch of the research program is paused.

## Active scientific question

Study whether forecast-optimal smoothness varies with forecast horizon, estimation-window length, and local stochastic regime:

\[
S^\star_{T,h}
=
g(h,L,\mathcal R_T,\text{series class}).
\]

The intended progression is simulations, macroeconomic series, market indices/ETFs, individual equities, and cryptocurrency.

## Canonical analytic model

\[
\widehat t_{\lambda,d}
=
(I+\lambda D_d^\top D_d)^{-1}y.
\]

This model is currently preferred for analytic sensitivity because the dependence on \(\lambda\) is explicit.

## Chronological validation invariant

At every forecast origin \(T\), fitting and hyperparameter selection may use only information available at or before \(T\). Future observations can score the forecast but may not construct it.

Use rolling/expanding origins. Random internal masks are a separate smoothing/reconstruction experiment, not the main forecasting protocol.

## Numerical direction

Work in \(\theta=\log\lambda\). The main planned selector brackets roots of the aggregate rolling-origin forecast derivative and solves each bracket with Brent's method. Newton and direct bounded minimization are benchmarks/refinements.

The exact derivations and current implementation map are maintained in:

- `notes/key_results.md`
- `notes/derivative.md`
- `notes/numerical_selection.md`
- `notes/model_definitions.md`

## Library-first rule

Paper folders should orchestrate experiments and typeset results. Reusable mathematics belongs in `src/trend_estimation/` and must have tests.

## Canonical roadmap

See `notes/roadmap.md`. That file supersedes older paper-specific planning documents.
