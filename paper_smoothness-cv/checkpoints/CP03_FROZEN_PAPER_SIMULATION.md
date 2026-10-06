# Checkpoint 03 — Frozen paper-scale simulation

**Status: IMPLEMENTED — awaiting execution.**

Checkpoint 02 has been reviewed and the simulation design is now frozen before
the paper-scale run.

## What CP02 established

CP02 showed:

- horizon-matched forecast-CV can materially outperform one-step tuning,
  especially at longer horizons and under AR(1) noise;
- the proposed selector wins the largest share of outer forecast blocks across
  the explored designs;
- the latent future forecast oracle is usually interior rather than pinned at
  S=1, so the forecasting problem is not intrinsically a boundary problem;
- recovery-optimal and future forecast-optimal smoothness are distinct targets;
- L=60 is a useful middle window and avoids making the main paper a joint
  window-selection study;
- BIC, under a global endpoint-inclusive implementation of the published score,
  is pinned to the left finite boundary and is therefore not a valid primary
  comparator without an additional domain restriction.

CP03 does not alter the design after observing paper-preset outcomes.

## Frozen primary design

Difference order:

\[
d=2.
\]

Window length:

\[
L=60.
\]

Forecast horizons:

\[
h\in\{1,3,6,12\}.
\]

Latent trend mechanisms:

1. linear — null-space sanity/control case;
2. smooth_curve — smooth nonlinear evolution;
3. oscillatory — repeated local slope changes;
4. recent_slope_change — late structural slope change;
5. terminal_bend — local terminal curvature.

The quadratic and turning-point CP02 mechanisms are dropped because they are
structurally redundant with the retained smooth nonlinear/local-curvature
cases, not because forecast-CV happened to perform poorly or well on them.

Noise models:

- iid Gaussian;
- AR(1), with the existing fixed persistence parameter;
- Student-t with finite variance as a heavy-tail robustness condition.

Marginal noise scales:

\[
\sigma\in\{0.3,0.7\}.
\]

Seeds:

\[
0,\ldots,99.
\]

Series length:

\[
N=360.
\]

Outer forecast origins:

\[
T\in\{228,252,276,300,324,348\}.
\]

The same origins are used for all horizons.

Smoothness grid:

\[
601
\]

equally spaced values on \([0,1]\).

## Mandatory inner-CV / outer-refit semantics

At every outer origin \(T\), the inner rolling folds are used only to choose the smoothness value \(\widehat S_{T,h}\). Their fitted trends are not candidates for the final outer forecast.

After selection, CP03 always performs a new fit using the most recent full window available before the outer test:

\[
\widehat\tau_T
=
H_{\lambda(\widehat S_{T,h})}y_{T-L+1:T}.
\]

The untouched outer forecast is then

\[
\widehat y_{T+1:T+h\mid T}=G_{d,h}\widehat\tau_T.
\]

Thus inner CV averages forecast losses across folds, not trend estimates. At later outer origins, data that have become observed are incorporated into the new history and the entire selection/refit cycle is repeated. This is a hard invariant; see `../notes/validation_semantics.md`.
## Feasible selectors

Primary feasible comparison set:

1. horizon-matched forecast-CV;
2. one-step forecast-CV;
3. ordinary CV;
4. GCV;
5. AICc.

BIC is excluded from CP03 primary performance comparisons for the reason
documented above. The CP02 audit remains in the repository.

## Simulation-only oracles

Two non-feasible benchmarks remain:

1. recovery oracle on the latent historical trend;
2. latent future forecast oracle.

They answer different scientific questions and must not be reported as
practical forecasting competitors.

## Common-random-number design

For a given seed, noise model, and noise scale, the same underlying innovation
stream is reused across trend mechanisms.

This improves paired comparisons but induces dependence across mechanisms.
Therefore:

\[
\boxed{\text{the bootstrap/resampling unit is the seed}}
\]

rather than an individual scenario row.

## Primary paper estimand

The main paired estimand is the forecast error ratio between horizon-matched
forecast-CV and a comparator.

For scale-free aggregation the analysis uses

\[
\exp\left[
\frac12
E\left\{
\log
\frac{\operatorname{MSFE}_{\mathrm{forecast-CV},h}}
     {\operatorname{MSFE}_{\mathrm{comparator}}}
\right\}
\right],
\]

which is a geometric RMSFE ratio.

Values below one favor the proposed selector.

Confidence intervals are nonparametric bootstrap intervals obtained by
resampling seeds.

## Main scientific comparisons

The paper-scale simulation must report:

1. forecast-CV h versus forecast-CV 1;
2. forecast-CV h versus CV;
3. forecast-CV h versus GCV;
4. forecast-CV h versus AICc;
5. results separately under iid, AR(1), and Student-t noise when conclusions differ;
6. selected smoothness by horizon;
7. recovery-optimal versus latent-forecast-optimal smoothness;
8. feasible forecast-CV versus latent future forecast oracle.

## Code

- experiments/smoothness_cv/run_checkpoint_03.py
- experiments/smoothness_cv/analyze_checkpoint_03.py
- experiments/smoothness_cv/make_checkpoint_03_figures.py

## Parallel execution

Checkpoint 03 is parallelized across complete simulation scenarios using
multiple worker processes. This is the correct level of parallelism for the
paper design because scenarios are independent once the frozen seed and DGP
configuration are specified.

By default, `--jobs 0` is used implicitly. It selects all but one logical CPU,
capped at 16 workers. Each worker is forced to one BLAS/OpenMP thread to avoid
nested oversubscription.

Useful options:

~~~bash
# automatic parallelism
python experiments/smoothness_cv/run_checkpoint_03.py --preset smoke

# explicit worker count
python experiments/smoothness_cv/run_checkpoint_03.py --preset paper --jobs 12

# serial debugging
python experiments/smoothness_cv/run_checkpoint_03.py --preset smoke --jobs 1
~~~

On Windows, do not run more than 61 workers. A practical starting point is
roughly 70--90% of the machine's logical CPUs; reduce the count if memory
pressure becomes noticeable.

Changing `--jobs` does not change the statistical design or random seeds. It
only changes execution order/speed.

## Run smoke first

From the repository root:

~~~bash
git pull
pip install -e .
pytest

python experiments/smoothness_cv/run_checkpoint_03.py --preset smoke
python experiments/smoothness_cv/analyze_checkpoint_03.py
python experiments/smoothness_cv/make_checkpoint_03_figures.py
~~~

Inspect that run only for code/IO failures.

## Paper-scale run

If smoke passes:

~~~bash
python experiments/smoothness_cv/run_checkpoint_03.py --preset paper --jobs 0
python experiments/smoothness_cv/analyze_checkpoint_03.py
python experiments/smoothness_cv/make_checkpoint_03_figures.py
~~~

The paper preset is expected to take substantially longer than CP02.

## Outputs

Each run writes:

- block_results.csv.gz — full outer-block results;
- series_results.csv — outer-origin aggregated series results;
- paired_method_comparisons.csv;
- oracle_comparisons.csv;
- objective_curves.csv;
- run_metadata.json;
- checkpoint_report.md after analysis;
- diagnostics/;
- paper_artifacts/ after figure generation.

The compressed block file prevents the final result bundle from exceeding
ordinary GitHub file-size limits.

## Stop rule

After the paper run is pushed, do not change:
- seeds;
- DGP set;
- noise set;
- horizons;
- window length;
- outer origins;
- smoothness grid;
- primary feasible comparator set.

The next checkpoint is manuscript integration and public-data evaluation, not
retuning the simulation because of an inconvenient result.
