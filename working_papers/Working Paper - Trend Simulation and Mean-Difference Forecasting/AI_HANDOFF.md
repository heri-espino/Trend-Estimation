# Agent handoff — new mean-difference trend-forecasting paper

**2026-10-11. SCIENTIFIC PRIORITY OVER PAPER FORMATTING.**
Read [README.md](README.md), [notes/INDEX.md](notes/INDEX.md),
[notes/PROOF_LEDGER.md](notes/PROOF_LEDGER.md) and
[notes/SIMULATION_ATLAS.md](notes/SIMULATION_ATLAS.md) before editing.

## Do not conflate these scientific decisions

- Existing pure PLS (mu=0): \(\widehat\tau=H(S)x\),
  forward polynomial continuation with future d-th differences 0.
- Guerrero 2007: \(\widehat\mu_G(x)=\mathbf1^\top D_dx/(L-d)\),
  used in both fitted trend and affine future continuation.
  The mean is **training-only for each historical origin**.
- New forecast-CV profile: for each S, a **shared mu(S)**
  minimizes the weighted historical completed h-step MSE.
  Select S from the **profiled F(S)** and use its mu(S)
  to fit/forecast at present operational T.
- In-sample joint \(\min_{\tau,\mu}\) of PLS penalty is a
  fourth DIFFERENT estimator with \(Q^*=D^\top
  (I-11^\top/(L-d))D\) and (typically) **d+1 nullity**;
  it is NOT the above CV profiling and is NOT implemented here.

## Essential mathematical identities

\(p_j=\binom jd\) satisfies \(D_dp=1\).
\[
\widehat\tau_{\lambda,\mu}
=H_\lambda x+\mu (I-H_\lambda)p,\quad
\widehat z_t(S,\mu)=G H(S)x_t+
\mu\{G(I-H(S))p+g\}
=a_t(S)+\mu b(S).
\]
With normalized historical weights,
\(F(S,\mu)=A(S)-2C(S)\mu+B(S)\mu^2\),
\(\widehat\mu(S)=C(S)/B(S)\) for \(B>0\),
\(\widetilde F(S)=A-C^2/B\).
If B=0, mu is **unidentified** (no fabricated estimate).
Interior profiled curvature follows by chain rule:
\(\widetilde F_{SS}=F_{SS}-F_{S\mu}^2/F_{\mu\mu}\).

**EDF warning:** if \(\widehat\mu_G=c^\top x\), smoothing is
\(A=H+b_{\rm fit}c^\top\), so
\(\operatorname{tr}A=\operatorname{tr}H+c^\top b_{\rm fit}\).
The old S index based on trace(H) remains a penalty coordinate,
**not** the effective EDF of a data-estimated-mu procedure.

## Temporal non-leakage

Every historical \(\ell_{t_q}(S,\mu)\) can enter F at T only
when \(t_q+h\le T\). The test observations \(y_{T+1:T+h}\)
and latent \(\tau\) are **never used for tuning**.
This holds also for Guerrero plug-in means: each
\(\widehat\mu^G_q\) comes from \(x_q\), NOT its future.

The original CUDA 8h campaign uses only mu=0 and may be in progress.
**Do not modify its manuscript/result interpretation, manifest,
runner or existing SQLite** to retroactively include this work.
The new pilot is a standalone experiment and needs fresh seeds.

## Status (not claims)

- Historical Guerrero solver and affine G already existed.
- New exact mean-loading and forecast-CV profile API committed.
- New tests are committed but must pass on user's environment.
- Pilot code provides basic matched DGP/outer comparison; no formal
  study completed and no GPU integration claimed for this extension.
- Theoretical identities are algebraically derived here but not
  claimed original; literature search and simulation results pending.
- LaTeX is a placeholder until science is justified.
