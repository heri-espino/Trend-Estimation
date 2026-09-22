# Exploration 03 — Search-Boundary Sensitivity

## Role in the active paper

This is a **numerical validity experiment**, not a new scientific mechanism.

The canonical research object remains

\[
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h})
=
G(h,X_T,\mathcal C).
\]

Exploration 02 produced a strong persistence/horizon pattern, but a material
fraction of the selected optima occurred at the finite search boundaries
\(\log\lambda\in[-10,16]\). Before interpreting exact smoothness levels or
moving to within-series regime transitions, we must determine whether those
boundary selections are numerical truncation or genuine limiting preferences.

## Controlled comparison

Repeat **exactly the same Explore-02 DGP grid and seeds**:

- 30 seeds;
- \(\phi\in\{-0.8,-0.4,0,0.2,0.4,0.6,0.8,0.9,0.95\}\);
- \(h\in\{1,2,3,6,12\}\);
- \(\sigma_{\rm slope}=0.01\);
- \(\sigma_\varepsilon=0.5\);
- orders \(\{1,2,3\}\);
- windows \(\{24,48,72\}\).

Change only the numerical search:

\[
\log\lambda:\ [-10,16]\longrightarrow[-18,24],
\]

and

\[
n_{\rm grid}:\ 161\longrightarrow321.
\]

This isolates numerical-domain sensitivity from changes in the scientific
design.

## Command

From the repository root:

~~~powershell
python experiments\forecast_optimal_smoothing\run_persistence_mechanism.py --preset boundary
~~~

For a one-seed syntax/runtime check first:

~~~powershell
python experiments\forecast_optimal_smoothing\run_persistence_mechanism.py --preset boundary --n-seeds 1
~~~

The boundary preset uses the full Explore-02 \((\phi,h)\) grid, 30 seeds,
321 discovery points, and \(\log\lambda\in[-18,24]\).

## Additional outputs

The mechanism grid now records the four selected penalties explicitly:

- lambda_observed_forecast;
- lambda_latent_forecast_oracle;
- lambda_ar_residual_oracle;
- lambda_recovery_oracle.

The run summary now also records lower/upper-boundary fractions for every
objective. This makes the boundary comparison auditable without reconstructing
it from the full row-level output.

## Questions

1. Do the sign/persistence/horizon patterns from Exploration 02 survive?
2. Do old boundary optima move to interior stationary minima?
3. Which regimes still select the new lower or upper boundary?
4. Are those persistent boundary choices compatible with genuine
   \(\lambda\to0\) or \(\lambda\to\infty\) limiting preferences?
5. Does the ordering
   \[
   S^\star_{\rm observed}
   <
   S^\star_{\rm AR}
   <
   S^\star_{\rm latent}
   <
   S^\star_{\rm recovery}
   \]
   survive in the positive-persistence/short-horizon regions where it was
   previously observed?
6. Are the conclusions stable across selected \(d\) and \(L\)?

## Decision rule

If the qualitative persistence/horizon conclusions survive and most suspicious
old boundary selections become interior or remain coherently limiting under the
wider domain, close the numerical caveat and proceed to the first
**within-series regime-transition** experiment.

If the scientific ordering changes materially under the wider domain, do not
proceed to regime transitions. First diagnose the objective geometry and root
discovery in the affected regimes.

## What follows if this passes

Exploration 04 should change a regime **inside a single series** and track

\[
T\mapsto
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}).
\]

The first transition should change persistence, e.g.

\[
\phi_t=
\begin{cases}
0,&t<t_0,\\
0.8,&t\ge t_0,
\end{cases}
\]

followed separately by changes in noise scale and latent-trend roughness. The
main new estimand is adaptation delay and the next substantive question is
whether the adaptive configuration improves untouched OOS forecasts relative
to fixed configurations.
