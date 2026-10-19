# Guerrero known-ratio comparison — first stochastic-model smoke

**Recorded:** 2026-10-18 (CI execution on October 19 UTC). **Status:** exploratory smoke evidence, not confirmatory results.

**Source:** [GitHub Actions run 39185627895](https://github.com/heri-espino/Trend-Estimation/actions/runs/39185627895), successful Pooled LOOCV paper checks; 23 isolated tests passed. Smoke output was generated and checked in temporary CI storage; user should run locally to save the underlying CSV/figures in the repository.

## Model and design

Follow the [Guerrero stochastic-noise protocol](GUERRERO_VARIANCE_RATIO_PROTOCOL.md): D_2 tau = epsilon, y = tau + eta; independent Gaussian disturbances of known variance. Known model-based smoothing penalty: lambda_G = sigma_eta^2 / sigma_epsilon^2.

Smoke: N=24, sigma_epsilon=0.25; observation-noise sigma_eta=0.5 or 2; two independent seeds per cell; R=1 and R=3 nested pools, totaling 8 paired pool cases and 32 method rows. Both R values at the same seed share their first realization. The statistical sample is extremely small.

## Actual run mean scores

| Method | Pooled observed LOOCV MSE | True latent trend MSE | Mean normalized S |
|---|---:|---:|---:|
| Guerrero, true known DGP variance ratio | 2.946546 | **0.296140** | 0.834168 |
| Single-start bounded Brent | **2.794600** | 0.316439 | 0.842752 |
| Multibracket derivative Brent | 2.797248 | 0.317799 | 0.832155 |
| Finite dense grid | 2.794933 | 0.315417 | 0.842128 |

Multibracket produced smaller observed LOOCV than the Guerrero ratio on 8/8 paired pool comparisons, but Guerrero gave smaller latent-trend MSE than multibracket in 5/8. On this smoke dataset single-start Brent scored slightly lower than multibracket, a warning against assuming multi-bracket is universally preferable or already globally complete.

For R=1 only (4 cases), mean true trend MSE was 0.321667 (Guerrero) and 0.342349 (multibracket). For R=3 only (4 cases), 0.270613 and 0.293249 respectively.

## Scope and interpretation

- Guerrero's known-ratio method is provided the *actual simulation variances*. No plug-in variance estimator is included.
- The two objectives differ: observed LOOCV MSE is not the same as recovery of the latent trend.
- With deterministic initial trend coefficients, the known-ratio smoother is an appropriate model-based benchmark, but broad conditional Bayesian optimality claims require diffuse-prior qualifications.
- Neither method comparison, sign-change root search, nor grid constitutes a universal guarantee of global optimization; the above are only means over 8 nested smoke pool cases.
- No forecasts, financial backtests, or observed future-data evaluation are involved.

## Follow-up

Run and commit the independent 12-scenario Guerrero pilot (N=50/200; sigma_eta=0.5/2; sigma_epsilon=0.1/0.3/1; 5 seeds; R=1/3); then analyze paired observed LOOCV and true trend MSE by ratio and sample size, with seed-level uncertainty. Do not launch the 100-seed confirmatory run until pilot quality and numerical robustness are reviewed.
