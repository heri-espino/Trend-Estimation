# Checkpoint — Search-Boundary Sensitivity Results

Date: 2026-09-22

Status: **PASS**

Run:

`results/forecast_optimal_smoothing/20260923T050020Z_persistence-mechanism_boundary_78a516d/`

Commit containing the run: `2510be3` (`ran`).

## Design

Exploration 03 repeated Exploration 02 with the same 30 seeds, DGP grid,
orders, windows, horizons, and outer origins. Only the numerical search changed:

\[
\log\lambda: [-10,16]\rightarrow[-18,24],
\qquad
n_{\rm grid}:161\rightarrow321.
\]

The run contains 1,350 seed/phi/h configurations and 26,730 outer-origin rows.
Elapsed time was about 2,487 s (41.5 min).

## Main scientific result is invariant

The aggregate persistence/horizon pattern is essentially unchanged.

For phi=0.8 and h=1:

| objective | old search | wide search |
|---|---:|---:|
| observed | 0.3386 | 0.3386 |
| AR-aware | 0.5932 | 0.5931 |
| latent forecast | 0.7983 | 0.7984 |
| recovery | 0.9403 | 0.9407 |

For phi=0.9 and h=1, the old/new observed smoothness is 0.3447/0.3447.
For phi=0.95 and h=1, it is 0.3928/0.3928.

Averaging over persistence values, the old/new mean observed smoothness is:

| h | old | wide |
|---:|---:|---:|
| 1 | 0.6718 | 0.6719 |
| 2 | 0.7263 | 0.7263 |
| 3 | 0.7741 | 0.7743 |
| 6 | 0.8423 | 0.8429 |
| 12 | 0.8954 | 0.8960 |

The horizon pattern therefore survives the much wider numerical domain.

## Cell-level sensitivity

Across all 1,350 seed/phi/h summary cells:

- observed smoothness median absolute change: about 2.1e-5;
- observed 95th percentile absolute change: about 0.0010;
- AR-aware median absolute change: about 2.6e-5;
- AR-aware 95th percentile absolute change: about 0.0018;
- latent median absolute change: below 1e-6;
- recovery median absolute change: effectively zero;
- only 2 of 1,350 cells changed whether the full ordering
  observed < AR < latent < recovery held.

Large cell-level outliers exist, but they are rare and do not alter the
aggregate mechanism.

## Boundary behavior

Under the wide search, boundary counts across 26,730 outer origins are:

| objective | lower | upper |
|---|---:|---:|
| observed | 2,391 | 1,803 |
| latent | 632 | 868 |
| AR-aware | 2,146 | 2,188 |
| recovery | 0 | 584 |

Compared with the old domain, upper-boundary selections fall substantially for
observed, latent, and AR-aware objectives. The lower-boundary counts for
observed/latent/AR remain almost unchanged even though the lower numerical
limit moved from exp(-10) to exp(-18).

That persistence is structured rather than diffuse: lower-boundary choices
concentrate in strong positive persistence (especially phi=0.8, 0.9, 0.95),
whereas observed upper-boundary choices are concentrated in negative
persistence. This is consistent with genuine limiting preferences in those
regimes rather than the original boundary alone creating the effect.

Recovery has no lower-boundary selections and only about 2.2% upper-boundary
selections under the wide domain. These do not materially affect aggregate
recovery smoothness.

## Decision

The numerical-domain caveat is closed for the qualitative persistence/horizon
mechanism. Exact limiting lambda values should still be described carefully,
but the mechanism is not an artifact of the original [-10,16] search box.

The project should now move to a within-series regime-transition experiment.
The next object is the path

\[
T\mapsto
\Theta^\star_{T,h}
=
(d^\star_{T,h},L^\star_{T,h},S^\star_{T,h}),
\]

with a known change point and paired stationary controls.

## Next experiment

Exploration 04 will begin with persistence transitions while holding latent
roughness and observation-noise scale fixed. It will compare:

- stable low persistence: 0 -> 0;
- low-to-high persistence: 0 -> 0.8;
- high-to-low persistence: 0.8 -> 0;
- stable high persistence: 0.8 -> 0.8.

This permits a direct estimate of adaptation after the regime point and makes
window length L a first-class part of the empirical response.