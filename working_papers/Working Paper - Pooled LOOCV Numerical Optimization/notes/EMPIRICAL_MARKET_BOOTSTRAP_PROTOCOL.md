# Pilot F — real-market-return-calibrated synthetic-noise Monte Carlo

**Design finalized 2026-10-19 (Mexico City time), before running the real-market pilot.** Source: [run_empirical_market_noise.py](../../../experiments/pooled_loocv_smoothness/run_empirical_market_noise.py). **Status: implemented, automated offline smoke only; the actual SPY experiment is NOT yet executed or committed.** Existing campaigns A–E and their output directories are untouched. Commit directly to the current paper branch, NO PR.

## 1. Scientific question

The earlier heavy-tail simulation varied *parametric* shock distributions: Student t(3), centered Gamma, skew-normal, Gaussian jumps, and Student-t GARCH. To avoid assuming a convenient parametric shock law, use **one real financial series as the calibration sample** for a centered empirical return distribution, then generate new synthetic observations whose true latent trend is known by construction.

**Do NOT identify a histogram with a stochastic process.** The empirical histogram describes a *marginal one-period distribution*, but contains no temporal ordering, lagged dependence, or volatility persistence. Compare i.i.d. resampling from the empirical distribution versus circular block resampling of the actual ordered historical returns. Block resampling retains some dependence *within* blocks, though it does not fit a correct conditional-volatility process or guarantee stationarity of the market sample.

**Do NOT assert the market stock price trend equals the arithmetic mean of adjusted prices or the mean return.** A mean daily log return \(\bar r\) is a summary drift of the historical return distribution, not a generally identified time-varying latent stock price trend. In the synthetic experiment below, the **conditional expectation** \(\mathbb E[Y_t\mid\tau]=\tau_t\) is our known trend, and this is the legitimate truth used in reconstruction MSE.

## 2. One frozen historical calibration source

**Default**: ticker SPY, daily adjusted close, fixed window `2015-01-01` inclusive to `2026-01-01` exclusive (2015–2025 full calendar years). Yahoo/yfinance `Ticker.history(start,end,interval="1d",auto_adjust=True,actions=False)`; the local user downloads adjusted closes (accounting for distributions/splits subject to source accuracy). Formula:

\[
r_t = \log P_t^{adj}-\log P_{t-1}^{adj}, \qquad
\bar r = \frac1T\sum_{t=1}^{T}r_t,\qquad
s_r^2=\frac1T\sum_{t=1}^{T}(r_t-\bar r)^2,
\quad z_t=(r_t-\bar r)/s_r.
\]

The finite empirical law assigns equal mass \(1/T\) to the observed values \(z_1,\ldots,z_T\). **By construction its population (finite empirical distribution) mean is zero and variance is one**. The model later multiplies by a *controlled synthetic* noise SD 0.5 or 2 in normalized arbitrary units. Consequently, measured MSE magnitudes are **not** real return-percentage or dollar forecast errors, and the scale intentionally differs from historical stock return SD.

We also record \(\bar r\), empirical SD, empirical skewness/excess kurtosis, sample dates, number of observations, and SHA256 digest of the exact (date, return) calibration sequence. The downloaded personal-use return snapshot is kept only on the user's PC in `data/market_calibration/`, excluded by `.gitignore`; don't commit licensed raw market data.

**Reproducibility limit:** GitHub stores SHA256 plus exact seeds and methods but NOT the return sequence. Exact replay on a different computer requires the *same local cached CSV* (or an authorized copy of the calibration dataset). The Yahoo provider can revise historic adjusted prices; `--refresh-data` deliberately re-downloads and may result in a new hash. A third-party CSV of prices or dated log returns may be provided with `--source prices_csv|returns_csv --csv path`; do not silently substitute a synthetic fixture if the real data download fails. Under `--preset smoke`, an **explicit synthetic Student-t5 fixture** tests code without any market-data API and is never described as empirical evidence.

## 3. Simulated data and four noise mechanisms

For each synthetic series \(r=1,\ldots,R\), generate a **new** latent stochastic trend with a fixed analyst-chosen difference order \(d\) (default \(d=2\)):

\[
D_d\tau^{(r)}=\varepsilon^{(r)},\qquad
\varepsilon^{(r)}_t\overset{iid}\sim N(0,\sigma_\varepsilon^2),
\quad \sigma_\varepsilon=0.3,\qquad
\tau_j^{(r)}=0.02(j-1),\ j\le d.
\]

Let \(\tilde z_t^{(r)}\) be the sampled standardized observation disturbance, independent of latent innovations and of other simulation series conditional on the fixed historical calibration sample. Then

\[
Y_t^{(r)}=\tau_t^{(r)}+\sigma_\eta\,\tilde z_t^{(r)},
\qquad \sigma_\eta\in\{0.5,2.0\}.
\]

The model's *conditional mean given the generated trend*, averaged across fresh sampling of noise, equals \(\tau_t\) at every \(t\). The latent trend is **never observed in real SPY prices**; it is deliberately constructed anew only so the simulation permits a true reconstruction-MSE benchmark.

Each of the four modes uses the **same sample-derived mean-zero/variance-one marginal** or its matched normal:
1. `gaussian_matched`: iid Gaussian \(N(0,1)\), with synthetic SD matched to empirical bootstrap.
2. `empirical_iid`: sample a historical \(z_j\) uniformly with replacement, independently over simulation time.
3. `circular_block_5`: sample random historical start positions, concatenate length-five consecutive return blocks with wrap-around and truncate to N.
4. `circular_block_20`: same with length-twenty blocks.

The two block procedures preserve within-block local serial and volatility dependence, which an empirical histogram alone cannot encode. They are *not* conditional likelihood models for the original SPY data.

## 4. Methodological comparison: fixed d and pooled lambda

**User's precise pooling objective** (from `objective.PooledLOOCV.score`):

\[
F_d(\lambda)=\frac1R\sum_{r=1}^{R}\mathrm{LOOCV}_r(\lambda),
\qquad
\widehat\lambda_{CV}=\arg\min_{\lambda\ge0}F_d(\lambda),\qquad
\widehat S_d=S_d(\widehat\lambda_{CV}),
\]

where

\[
S_d(\lambda)=\frac1{N-d}\sum_{j=1}^{N-d}
\frac{\lambda q_j}{1+\lambda q_j},
\]

and \(q_j>0\) are the nonzero eigenvalues of \(D_d^\top D_d\).

This is **not** averaging the R independently optimized smoothness values \(\widehat S_r\), which generally differs from minimizing a common pooled loss. The analyst fixes \(d\) before running. The simulator permits `--d 1`, `--d 2` or `--d 3` as **separate studies**, but NO joint d-selection or model order tuning is done here. Default fixed d=2 honors the original research objective.

We compare two **feasible methods using identical y and the same d**:

- Gaussian **difference-covariance contrast quasi-MLE** estimates \(\widehat a,\widehat b\) from \(D_dy\) under assumed \(\Sigma=aI+bD_dD_d^\top\) and chooses \(\widehat\lambda_{ML}=\widehat b/\widehat a\).
- Pooled **ordinary LOOCV** minimizes \(F_d(\lambda)\) with bounded Brent.

Each reconstructs \(\widehat\tau_{\lambda,d}=H_{\lambda,d}y\). Score **both** observed pooled LOOCV MSE and realized latent trend reconstruction MSE against the generated \(\tau\), plus median absolute error and variance-component estimates when available. Do NOT claim a realized smaller true-trend MSE means better stock market forecasting.

Normality is sufficient for the literal fitted normal likelihood but **not required for the basic covariance identity** if noise has zero mean and finite second moments. In an empirical iid bootstrap the covariance structure assumed by Gaussian **quasi**-ML is correct even if the marginal distribution is visibly heavy-tailed; under block sampling the temporal covariance is generally wrong. Therefore the naive expectation "Gaussian ML wins only for normal disturbances" need not hold even under proper methodology.

## 5. Paired Monte Carlo design, progress and scope

- **Offline CI smoke**: fixed \(d=2\), N=24, synthetic SD 0.5, one seed, R=1/3 nested, four noise modes = **8 pools, 16 method rows**. Uses a labelled *synthetic* t5 fixture and never accesses Yahoo.
- **Real-market pilot (manual)**: SPY 2015–2025 calibration, **fixed \(d=2\)**, N=50/200, synthetic observation SD 0.5/2, R=1 and 3, five independently seeded latent pools per N and four noise modes = **160 nested pool evaluations, 320 method rows**. Per noise mode **20 R3 pools**; the nested R1 groups are *not* independent extra samples.
- **Confirmatory (manual, unrun)**: same four conditions per N/scale with 100 fresh seeds, 3,200 nested pools and 6,400 rows (requires first inspecting pilot and dependence-aware validity).

Deterministic seed base **58600000** for pilot, **59600000** reserved for confirmatory. `seed = base + 10000*N_index + replicate`. For a fixed seed, *the very same generated latent trend* is used across all four noise modes and both observation-noise scales; observation draws are independent across noise modes. R1 shares the first of R3 exactly. This **common-random-number pairing** reduces Monte Carlo noise but **does not create independent replications across scale, regime or R**. This experiment is not a cross-sectional pool of three observed stocks; R denotes independent synthetic trajectories conditional on the same historical calibration distribution.

Keep original calibration dates and source provenance. Use fixed Yahoo adjusted-price window to avoid changing endpoints merely by rerunning at a later calendar date. User can run `--source returns_csv --csv data/market_calibration/...csv` for exact local replay.

## 6. Manual run, outputs, interpretation boundary

```powershell
conda activate trend-estimation
git switch paper/pooled-loocv-numerical-optimization
git pull --ff-only
python -m pip install -e ".[dev,finance]"
python -m pytest tests/test_empirical_market_noise.py -q
python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset smoke
python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset pilot --dry-run
python -m experiments.pooled_loocv_smoothness.run_empirical_market_noise --preset pilot --ticker SPY
```

Main artifact directory: `results/pooled_loocv_smoothness/empirical_market_noise/SPY/d2/pilot/`. Expected `manifest.json` (complete source SHA, calibration digest/dates), `method_comparison.csv` (320 per-method rows), `summary.json`, `empirical_return_histogram_vs_gaussian.png` and `market_return_and_squared_return_acf.png`. Source-return snapshot remains ignored at `data/market_calibration/`. Check the source digest, market-series sample size, and correct plot before committing generated **result artifacts only** on the same branch. Do not use `git add .`, create a PR or merge.

This is **retrospective synthetic reconstruction with empirical market-noise shape**, not a true-trend forecast evaluation on stock prices. A later true financial forecasting experiment must choose the validation target and leakage-safe backtesting protocol separately; a stock price does not reveal a privileged ground-truth trend.

**Relevant public methodology:** R. Cont (2001), *Empirical properties of asset returns: stylized facts and statistical issues*, *Quantitative Finance*, DOI 10.1080/713665670; empirical tails and dependence are distinctive concerns in return modeling. R. Davis et al. (2018), *Inference on the tail process with application to financial time series modeling*, *Journal of Econometrics* 205(2), 508–525; research motivation for block bootstrap under dependent heavy-tailed financial observations. The source URL and date are retained rather than incorrectly attributing this particular Monte Carlo protocol to either paper.
