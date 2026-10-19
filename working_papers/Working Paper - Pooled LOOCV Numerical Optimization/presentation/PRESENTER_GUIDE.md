# Presenter guide — teaching with the Study M.2 Marp deck

**Audience:** senior undergraduate / MSc statistics, econometrics, actuarial science or applied mathematics.  
**Format:** mathematically explicit lecture, approximately 90–120 minutes in full; split into two classes for detailed questions.  
**Slides:** [001_process_diversity_lecture.md](001_process_diversity_lecture.md).  
**Research evidence:** [source-pinned 1000-seed results](../notes/STUDY_M2_1000_SEED_PROCESS_RESULTS_2026-10-19.md).

The lecture is deliberately structured as a sequence of **questions and mathematical answers**, not an unsupported general introduction to time series.

## Lesson A — Mathematical construction (opening through methods)

**Question 1: What exactly is the target?**

Distinguish the random *realized* latent trend from its conditional expectation and from a future forecast. We observe \(y\), estimate the realized \(\tau\), and only simulation lets us calculate \(\|\widehat\tau-\tau\|^2\). A retrospective trend estimator can be useful but is not an established forecast at horizon \(h\).

**Question 2: Why is the penalty quadratic and what does it imply?**

Starting from

\[
J(\tau)=\|y-\tau\|_2^2+\lambda\tau^\top Q\tau,\qquad Q=D_d^\top D_d,
\]

differentiate coordinatewise; the Hessian is \(2(I+\lambda Q)\succ0\), so the minimizer is unique for every finite \(\lambda\ge0\). Show \(\dim\ker(Q)=d\) by recalling the finite-difference annihilation of degree-\((d-1)\) polynomials. That is why d=2 means intercept and slope can survive infinite smoothing, and why \(Q\) alone cannot be inverted.

**Question 3: What does changing lambda do to eigencomponents?**

Eigenvectors \(u_j\) of \(Q\) are multiplied by \(1/(1+\lambda q_j)\). On the spectrum slide, ask the audience why the zero eigenvalues never shrink. Differentiate \(S(\lambda)=\{N-\mathrm{tr}(H_\lambda)\}/(N-d)\) to see it is nondecreasing; remind students this is *nominal* S, not full EDF after fitting a common mean.

**Question 4: Why consider \(\mu\neq0\)?**

A constant \(d\)-th difference mean corresponds to a polynomial trend component of degree \(d\), not to a constant mean of \(y\). The particular polynomial \(p_t={t\choose d}\) solves \(D_dp=\mathbf1\). Present the shift \(\tilde\tau=\tau-\mu p\) as a coordinate change rather than a new physical signal.

**Question 5: Why does the fitted mean alter CV and GCV?**

Profiling \(\mu\) from the quadratic form gives \(\widehat\mu=(b^\top\bar y)/k\), with \(b=QH_\lambda p\), \(k=p^\top QH_\lambda p\). Its low-rank hat-matrix update increases total EDF by \(\lambda\|b\|^2/k\). An observation-deletion CV that freezes an all-data plug-in mean is **not** deletion-honest. Present the exact PRESS denominator, and ask which term would disappear if the common mean were truly known externally.

**Question 6: Which criterion is 'best'?**

Avoid asking whether CV-score numbers and AICc-score numbers can be compared directly: they have different units/scales. CV, GCV, AICc and Gaussian contrast likelihood are *selection policies*, not realized latent MSE. The Study M.2 experiment fits each using observed \(y\) only and later evaluates against simulated tau. Fixed S=.5/.8 are analyst-declared baselines; their apparent success does not mean they are universally optimal.

## Lesson B — Experimental design and interpretation (nine mechanisms onward)

**Question 7: Why nine different processes rather than one Gaussian simulation?**

The study perturbs either (i) the actual latent trend (cycle, slope change, true level jump), (ii) the observed noise (spikes, AR1, time-changing variance), or (iii) the sharing assumptions among series (heterogeneous variances, common observation shock). The same random shocks are reused **within one seed**, allowing informative contrasts; this does not make the nine case outcomes independent. Refer to the process-generating source for exact amplitudes rather than improvising parameter values.

**Question 8: Why 1,000 independent seeds?**

The first gallery shows 198 specific fits on one random draw. The follow-up creates 1,000 new draws; 198,000 is the count of dependent method evaluations. Emphasize seed-level paired method differences, interval width, and Holm correction. Ask: how would an incorrect analysis inflate sample size if it treated 198,000 rows as independent?

**Question 9: Is there an overall best method?**

No. Gaussian GLS/ML and pooled plug-in have near-identical R3 mean risk across several DGPs; under the baseline plug-in minus GLS is only \(-0.00001653\) with 95% paired interval spanning zero. At R3, the true-jump S=.5 and AR1 S=.8 win distinctly against the second-place candidate under *global* Holm. Do not confuse 'lowest sample mean MSE' with a proof of dominance.

**Question 10: How could a real jump and an outlier require opposite decisions?**

Under a true latent jump, capturing some discontinuity is important: fixed S=.5 R3 MSE .31671 vs GCV zero .33395 and Gaussian ML .41371. Under measurement-only outliers, tracking a spike creates bias: one-series AICc wins on mean MSE and single-series GLS has p90 MSE .69367 (versus AICc .25455). These contrasts do not establish that any method is a robust changepoint or outlier estimator.

**Question 11: Why does AR1 correlated observation error hurt point-deletion CV?**

With phi=.85, observations adjacent to a deleted point retain correlated noise; the deletion score can reward following that noise. Ordinary CV/GCV choose median S near .445/.422 versus fixed S=.8, and their latent MSE is higher. **Caution:** covariance ML also uses a wrong covariance. Identifying the *unique* causal source of this failure would require blocked CV or correct covariance estimation, so teach this as a testable mechanism, not a proof.

**Question 12: How should pooling be evaluated?**

For a clean target series, compare its reconstruction under R1 with its own reconstruction under R3 with identical first y/tau. In unequal noise SDs (.25, .8, 1.5), pooled GLS drives median S from .758 to .888, and the first series' MSE grows .01701 to .04037. Explain why comparing the **R3 pooled average** to **R1 first-series** MSE would be logically invalid: the additional two series are noisier and have a different loss distribution.

## Mini-exercises and answers

1. **Nullity.** Show that d=3 gives three null directions. **Answer:** constant, linear, quadratic discrete polynomials; rank \(N-3\). This does not imply a cubic drift when \(\mu\) is fixed at zero.
2. **Two parameter decisions.** Under d=2 with fitted \(\mu\), what is the limiting pooled EDF? **Answer:** \(2R+1\) rather than \(2R\). The extra common quadratic coefficient remains.
3. **Same series target.** In heterogeneous pools, GLS loses \(0.04037-0.01701=0.02336\) first-series MSE. What is the sign convention? **Answer:** positive R3-R1 means pooling harms.
4. **False precision.** Is plug-in ML statistically better than GLS in the Gaussian R3 case? **Answer:** no evidence from these contrasts; Holm p=1 and paired CI straddles zero.
5. **External validity.** Can any slide establish the best trend for Bitcoin, equities or government bonds? **Answer:** no. The true latent trends are only known in these synthetic data-generating processes, and this is not forecasting.

## How to present the graphics

- **Lecture-specific vector figures** were added for teaching: they are either explicitly schematic or generated from committed compact CSVs. Schematic plots are not raw seed traces.
- **Nine R3 gallery PNGs** are genuine one-seed simulations. They are illustrations, not population risk estimates.
- **R1/R3 heatmaps** normalize risk by each process row's best method. White/lightness means closer to *that row's own* mean-MSE minimum and does not encode p-values.
- **Runner-up gap graph** combines mean-risk magnitude with global Holm flags; exact numbers and multiple comparisons remain in the source CSVs.
- **Pooling forest plot** shows GLS first-series R3-R1 paired means with *pointwise* 95% intervals. These are not Holm-adjusted intervals.

## Source control and reproducibility

No presentation is a replacement for the dated original results note. The exact run was source SHA fda4e69d64d47675e5bd126bf7332aa22a3d68fc and results upload commit 47392dbc4d11ca63d2e856fc9d974e4a24a11021. The GitHub compact audit checked aggregate identities, not the 40 ignored raw gzip shards. Preserve those locally. Keep Marp exports under ignored presentation/build/; generated SVGs and deck markdown should remain versioned. New lecture figures should be regenerated via the two Node generators, not manually substituted with aesthetically nicer but incorrect images.
