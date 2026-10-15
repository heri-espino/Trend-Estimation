# Possible Paper C — Forecast-optimal estimation of mean trend differences

**Research brief | 15 October 2026 | concept and already available evidence only.**

**Working title:** *Forecast-Optimal Estimation of Mean Trend Differences in Penalized Least Squares*

This is the prospective **fourth independent research paper** (the repository already has a dedicated working-paper folder). Retain the previous three papers, their mathematical derivations, existing simulation results and historical conventions.

## Publication priorities

| Order | Project | Distinctive question |
| --- | --- | --- |
| **A: now** | Paper 3 — Numerical Methods | How to find minima and stationary points of the potentially multimodal smoothness-validation objective? User's SMCCA submission target: **9 November 2026** |
| **B: next** | Paper 1 — Smoothness Cross Validation | How to select smoothness for horizon-specific forecasts under the restriction \(\mu=0\)? |
| **C: fourth paper, proposed** | Mean-Difference Forecasting (this project) | How to estimate the mean \(\mu\) of penalized trend differences specifically for forecasting? |
| **D: deferred** | Paper 2 — Dynamic Branch Selection | When does tracking persistent branches of local minima help beyond selecting global minima or averaging selected smoothness over time? |

**Editorial decision:** Do **not** automatically merge Paper 1 and the fourth paper. Their questions are distinct; independent publication remains conditional on a genuine contribution and external evidence. Postpone the branch-selection manuscript, not its scientific records.

## Central scientific question

Can a horizon-specific estimate of the mean of trend differences improve forecast performance relative to the restriction \(\mu=0\), Guerrero's difference-mean plug-in, and simple forecasting alternatives? When does the additional flexibility become unstable?

The Guerrero (2007) model already accommodates nonzero \(\mu\):

\[
\widehat\tau_{\lambda,\mu}
=\arg\min_{\tau\in\mathbb R^L}
\left\{\|x-\tau\|^2+
\lambda\|D_d\tau-\mu\mathbf1\|^2\right\},
\qquad\lambda\ge0.
\]

**Historical attribution:** Neither a nonzero penalty target nor fitting a historical difference mean is claimed as new. Algebraically profiling a quadratic parameter is also standard. The possible contribution lies in a specific historical \(h\)-step forecast-selection rule, its properties and carefully controlled empirical comparisons. The priority search against existing literature is unfinished.

## Comparison methods already defined and implemented

Three alternatives share an initial implementation in the repository ([research notebook](RESEARCH_NOTEBOOK.md), [source](../../../src/trend_estimation/forecasting/mean_difference_cv.py)):

1. **Zero mean:** fix \(\mu=0\), select normalized smoothness \(S\) by completed historical \(h\)-step forecast-CV.
2. **Guerrero plug-in:** for each origin's *training* window \(x_t\), compute \(\widehat\mu_t^G=\mathbf1^\top D_dx_t/(L-d)\). Use its forecast errors to select \(S\), then recompute the plug-in mean from the actual current training window.
3. **Profiled forecast-CV:** for every \(S\), estimate one common \(\widehat\mu_T(S)\) by minimizing the weighted losses at historical origins whose entire \(h\)-step blocks have finished. Then minimize the profile loss over \(S\).

**Potential additional comparisons — not results:** regularized/shrunk \(\mu\), alternative estimators of the difference mean, a separate in-sample joint penalty estimator, naive/drift/linear-OLS forecasts, and neighboring trend orders. In particular \((d=2,\mu\ne0)\) must be compared to \((d=3,\mu=0)\), since both may have quadratic limiting extrapolation.

## Mathematical results already derived (not asserted as novel)

The following identities are recorded in the [proof ledger](PROOF_LEDGER.md), with hypotheses, proofs and limitations.

Let \(Q=D_d^\top D_d\), \(H_\lambda=(I+\lambda Q)^{-1}\). With a particular vector \(p\) satisfying \(D_dp=\mathbf1\), for example \(p_j=\binom jd\) under consistent indexing, the unique conditional PLS fit is

\[
\boxed{\widehat\tau_{\lambda,\mu}=H_\lambda x+\mu(I-H_\lambda)p.}
\]

The proper native continuation must include the nonzero-difference drift term, rather than using the zero-difference extrapolator alone:

\[
\widehat z_t(S,\mu)=G_{d,h}\widehat\tau_t(S,\mu)+\mu g_{d,h}
=a_t(S)+\mu b(S),
\]
\[
a_t(S)=G_{d,h}H(S)x_t,\quad
b(S)=G_{d,h}(I-H(S))p+g_{d,h},
\quad g_{d,h}(k)=\binom{k+d-1}{d}.
\]

Given nonnegative normalized weights \(w_q\) for completed historical forecast origins \(t_q+h\le T\), define

\[
F_T(S,\mu)=\sum_q\frac{w_q}{h}
\big\|z_q-a_q(S)-\mu b(S)\big\|^2
=A(S)-2C(S)\mu+B(S)\mu^2,
\]
\[
A(S)=\sum_q\frac{w_q}{h}\|z_q-a_q(S)\|^2,\quad
C(S)=\sum_q\frac{w_q}{h}b(S)^\top[z_q-a_q(S)],\quad
B(S)=\sum_q\frac{w_q}{h}\|b(S)\|^2.
\]

If \(B(S)>0\), exact conditional minimization yields

\[
\boxed{\widehat\mu_T(S)=\frac{C(S)}{B(S)},\qquad
\widetilde F_T(S)=A(S)-\frac{C(S)^2}{B(S)},\qquad
\widehat S_T\in\arg\min_{S\in[0,1]}\widetilde F_T(S).}
\]

If \(B(S)=0\), \(\mu\) is not identified by that historical criterion. A lower loss on the same folds used to fit \(\mu\) **does not imply** a lower external forecast error.

For a twice differentiable criterion at an interior optimum with \(F_{\mu\mu}>0\), the standard envelope identity is

\[
\boxed{\widetilde F''(S)=F_{SS}-\frac{F_{S\mu}^2}{F_{\mu\mu}}}
\quad\text{evaluated at }\mu=\widehat\mu_T(S).
\]

The Guerrero plug-in fit is linear in the current training window: if \(c=D_d^\top\mathbf1/(L-d)\) and \(b_{\rm fit}=(I-H)p\), its effective degrees of freedom are

\[
\operatorname{edf}_{G}=\operatorname{tr}(H)+c^\top b_{\rm fit}.
\]

This is **not automatically** the EDF of the profile-CV estimator. Furthermore, minimizing the *training* PLS criterion jointly over \(\tau,\mu\) gives a different penalty matrix,
\(Q_*=D_d^\top[I-\mathbf1\mathbf1^\top/(L-d)]D_d\), whose nullity is \(d+1\) for the standard difference operator. Do not confuse this with forecast-CV profiling.

These identities do **not** establish statistical consistency, uniqueness of profile minima, novelty, or superiority on unseen data.

## Empirical results already available — and what they do NOT establish

### The historical frozen campaign concerns \(\mu=0\) only

The original Monte Carlo completed **100,848 of 144,000** independent scenario/seed tasks across all **144 DGP cells** (696–704 seeds per cell), with 50,424 archived numerical diagnostics. Its [retrospective audit](../../JOINT_FORMAL_8H_AUDIT_FINDINGS_2026-10-12.md) reports:

- Paper 1: across 10,080 scenario/method contrasts, Holm-adjusted inference favored the zero-mean pooled forecast-CV comparator in **7,791** and the classical/fixed comparator in **442**; other contrasts did not show a significant difference. These are contrasts, not seeds.
- Under \(d=3,h=12\), fixed \(S=1\) beat zero-mean forecast-CV in **82.4% of 136 compared DGP cells**, with median relative RMSE **0.9912**. Forecast-CV does not dominate all simple smoothing rules.
- The historical BIC specification tends to the near-interpolation boundary and is a problematic comparison; this should not be used to support a future claim about \(\mu\)-estimation.

**These numbers are historical context only. They do not evaluate any method allowing \(\mu\ne0\).**

### Nonzero-\(\mu\) project: implementation, not measured superiority

The existing [pilot runner](../../../experiments/mean_difference_forecasting/run_pilot.py), [dedicated app](../../../apps/mean_difference_forecasting.py), mathematical implementation and tests prepare comparisons of zero, Guerrero plug-in and profile modes. The [simulation atlas](SIMULATION_ATLAS.md) records proposed DGPs, metrics, figures, temporal CV controls and validation design.

**As of this note, no tracked numerical output or independently audited nonzero-\(\mu\) MSFE comparison is present in the GitHub results directory.** Hence no claim that profiling \(\mu\) is better (or worse) than Guerrero, \(\mu=0\), drift baselines or neighboring polynomial orders is currently supported. These are open empirical questions.

## Open questions (not completed results)

- Comprehensive literature comparison: has horizon-aware profiling of trend-difference drift already been studied under other names?
- Identifiability when \(B(S)\) is small, stability at \(S\)-endpoints, and profile-minimum geometry.
- Matched chronological external evaluation, including latent-trend recovery versus observed-future loss, horizon and noise sensitivity, negative cases and neighboring difference orders.
- Whether shrinkage helps when historical folds are scarce or regimes change.

**Scope of this update:** documentation only. No new simulations, fits, data modifications or changes to the existing three papers.
