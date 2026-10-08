# AI handoff — living forecast-smoothness cross-validation research

**UPDATED 2026-10-08. READ THIS BEFORE MODIFYING THE FORECASTING PROJECT.**

## Current priority / how to work

**The completed notes are the research source of truth. The existing LaTeX manuscript is a CSSC-oriented working draft, NOT a finalized article or an instruction to reuse CP03 results unchanged in the final submission.** The plan is to finish the conceptual, numerical, prior-art and experimental work, then rewrite the final paper from the notes. Do not opportunistically patch the manuscript to fit whatever preliminary result looks favorable.

Start with:
1. notes/INDEX.md — notes/navigation.
2. notes/research_objective.md — scientific objective.
3. notes/mathematical_foundations.md — eigendecomposition, index, forecast MSE, analytic derivatives, roots.
4. notes/validation_semantics.md — chronology, no future leakage, mandatory refit.
5. notes/claim_boundaries.md — evidence versus conjecture.
6. notes/research_log_2026-10.md — completed experiment history.
7. notes/next_experiments.md and notes/roadmap.md — next decision gates.
8. notes/literature_positioning.md — closest prior literature.

## The actual question

A smoothing penalty makes a historical PLS trend appear regular. But which smoothing value gives the best **forecast** of the trend's continuation over a declared horizon \(h\)? We investigate choosing the **normalized smoothness index** \(S\in[0,1]\) using MSE on the subsequently realized future blocks of *previous historical forecast origins*. Today's actual future remains unknown.

For length-\(L\) history \(x_t\), \(d\)th-difference penalty \(Q=D_d^\top D_d\), and smoothing matrix \(H_\lambda=(I+\lambda Q)^{-1}\), the normalized spectral index is

\[
S(\lambda)=1-\frac1{L-d}\sum_{j=1}^{L-d}(1+\lambda\delta_j)^{-1}.
\]

\(S\) maps the full penalty range \([0,\infty]\) to \([0,1]\), including the exact limiting polynomial least-squares projection. It is a monotone rescaling of an established Guerrero-type index, **not a new smoothing operator or an optimizer that changes the exact fitted-trend optimum by itself**.

For historical origins \(t_m\) whose validation blocks have ended by \(T\):

\[
F^{\mathrm{pool}}_{T,d,L,h}(S)=\frac1{Mh}\sum_m
\|y_{t_m+1:t_m+h}-G_{d,h}H_{\lambda(S)}x_{t_m}\|_2^2,
\]

with the \(S=1\) endpoint defined by the projection limit, and

\[
\widehat S_{T,d,L,h}^{\mathrm{FCV}}\in\arg\min_{S\in[0,1]}
F^{\mathrm{pool}}_{T,d,L,h}(S).
\]

After selecting \(S\), **discard historical fits**, refit on \(y_{T-L+1:T}\), and use \(G_{d,h}\) to forecast the as-yet-unobserved \(y_{T+1:T+h}\). With fixed \(d\), the continuation is a polynomial of degree at most \(d-1\); choosing \(S\) changes its fitted coefficients, **not its degree**.

## Mathematical elements to carry forward

- \(Q\) is PSD, with \(d\) zero eigenvalues and \(L-d\) positive eigenvalues. Spectral shrinkage of \(H_\lambda\) gives an intuitive interpretation and permits reuse across candidate smoothness.
- Effective degrees of freedom: \(\operatorname{edf}=L-(L-d)S\).
- The forecast error has a quadratic expansion in \(GH_\lambda x\), but is not generally a quadratic/convex function of \(S\).
- Matrix resolvent derivatives:
  \[
  H_\lambda'=-H_\lambda QH_\lambda,\quad
  H_\lambda''=2H_\lambda QH_\lambda QH_\lambda,\quad
  H_\lambda^{(n)}=(-1)^n n!\,H_\lambda(QH_\lambda)^n.
  \]
- The forecast MSE gradient/Hessian and \(S\)-chain rule are derived in notes/mathematical_foundations.md. Use analytic derivatives where possible.
- Multiple minima are possible. All recovered interior candidates and the *exact* endpoints must be considered. The pooled optimum need not equal an average of individual-origin minima.
- Small exact-rational Sturm isolation is a possible numerical diagnostic. Do not confuse small-case algebraic root completeness with proof of global minimum ordering or scalable certified root-finding.

## Experimental facts, status and priorities

The old runs are **real and remain preserved**, not “not executed” or “wrong”:

| Checkpoint(s) | Historical finding | Current interpretation |
| --- | --- | --- |
| CP01–CP02 | Developed/adjusted the original simulation design | Historical, not independent final evidence |
| CP03 | 3,000 scenarios / 72,000 outer decisions; matched-horizon FCV favored vs one-step CV in the frozen aggregate at longer \(h\) | **Provisional old method/results**; preserve exact artifacts, do not automatically reuse as final simulation |
| CP04 | Small four-series held-out test favored a recency branch rule | Exploratory, limited generality |
| CP05 | 64-series external panel disfavored that branch rule versus pooled CV | Important negative result |
| CP06 | Post-hoc continuation-order instability diagnosis | Mechanism study, not new confirmation |
| CP07 | Changing-roughness experiment did not favor recency versus pooled CV | Negative/limited extension evidence |
| CP08 | Demonstrated many possible \(\phi(V_j)\) smoothness maps without a universal winner | Optional method-family illustration |

**Next:** (1) test old and new numerical solvers on *exactly the same* forecast-loss surfaces; (2) evaluate spectral caching, analytic gradients and endpoint/minimum recovery; (3) decide/freeze a new statistical simulation design only after solver comparison; (4) investigate the closest prior art; (5) only then write the final paper from the notes.

A new solver may change approximate solutions and even empirical outcomes, but **must not be credited with changing the true exact optimum for an identical objective**. Do not interpret the historical numbers as guaranteed values under a new implementation, or erase them in expectation of a new run.

## Optional branch histories — independent of primary CV

Previous explorations tracked historical single-origin minimum locations and losses into \(V_j=[S_{j,t},\ell^{(1)}_{j,t},\ell^{(2)}_{j,t}]_t\). Under an explicit persistence assumption, a branch selector \(\psi\) and rule \(\phi(V_j)\) can choose current \(S\). This is **not required** for pooled forecast-CV and is not universally better in existing experiments. Tracking identity is ambiguous near crossings and births; origin \(T\)'s unseen test data must never enter the branch state.

Detailed formulas: notes/dynamic_tracked_smoothness.md. Prior runners, frozen parameters and exact panel results remain documented in checkpoints/ and results/smoothness_cv/.

## Literature and journal

Working outlet: *Communications in Statistics—Simulation and Computation*. Closest work: Guerrero (2007, 2008); Cortés-Toto et al. (2017); Islas, Guerrero and Silva (2019); Islas Camargo and Zumaya Galván (2025); Hart (1994); Vilar-Fernández and Cao (2007); Franke et al. (2026); Biessy (2026).

**Do not claim that smoothing for forecasting, selecting smoothing by prediction error, PLS, or normalized smoothness are independently new.** Whether the *precise* finite-difference PLS \(h\)-step CV criterion is novel is an open literature question. Distinguish target recovery from future observation MSE.

## Safe editing instructions

- If the user requests notes, modify notes and handoff/docs; do not silently rerun simulations or rewrite final paper.
- Preserve originals in checkpoints and results; historical “next” instructions are archival.
- Use GitHub as source of truth; document any new methodology, parameters, and protocol changes.
- Report what is derived, implemented, tested, and still merely a hypothesis as different statuses.
- The current manuscript is not submission-ready merely because a CSSC-oriented draft exists.
