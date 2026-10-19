"""Empirical daily-return calibrated noise: synthetic mean-trend Monte Carlo.

The data source is real adjusted stock/ETF CLOSES, transformed to log returns.
This is NOT a backtest, nor a claim that actual SPY returns have a known trend.
The synthetic model is y_t=tau_t+eta_t with E[eta_t | tau]=0. We know the
synthetic tau exactly and evaluate posterior reconstruction MSE retrospectively.

The analyst FIXES d beforehand (default d=2). R separate series share a
single lambda chosen by minimizing the AVERAGE observed-series LOOCV loss.
Gaussian difference likelihood estimates variance components from D_d y;
the same H(lambda,d) reconstructs each trend. An empirical market histogram
provides the one-time MARGINAL shock law. Circular block resampling retains
within-block dependence, unlike iid histogram resampling.

The user-run Yahoo adjusted-return snapshot is LOCAL ONLY and ignored by git.
SHA256, dates, ticker, transform and package versions are recorded. Yahoo
historical data can be revised and are subject to source-provider terms.

Smoke tests use an EXPLICIT SYNTHETIC t5 calibration fixture without internet.
Full pilot requires a real source (yfinance or CSV); no fallback that fakes data.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy

from .objective import PooledLOOCV
from .search import bounded_brent
from .variance_estimation import estimate_gaussian_differences
from .run_tail_noise import integrate_differences


METHODS = ("estimated_gaussian_difference_ml", "pooled_loocv_bounded_brent")
NOISE_MODES = (
    "gaussian_matched",
    "empirical_iid",
    "circular_block_5",
    "circular_block_20",
)
SEED_BASE = 58600000
DEFAULT_N = (50, 200)
DEFAULT_SCALES = (0.5, 2.0)


@dataclass(frozen=True)
class MarketCalibration:
    dates: tuple[str, ...]
    log_returns: np.ndarray
    source_kind: str
    source_reference: str
    cache_path: str | None = None

    def __post_init__(self):
        values = np.asarray(self.log_returns, dtype=float)
        if (values.ndim != 1 or values.size < 100 or
                not np.all(np.isfinite(values))):
            raise ValueError("Require at least 100 finite historical log returns")
        if len(self.dates) != len(values):
            raise ValueError("Each log return must have a date")
        if len(set(self.dates)) != len(self.dates):
            raise ValueError("Repeated date in financial calibration")
        if tuple(self.dates) != tuple(sorted(self.dates)):
            raise ValueError("Financial calibration must be chronological")
        if float(np.std(values)) <= 0:
            raise ValueError("Historical returns have zero empirical variation")

    @property
    def mean(self):
        return float(np.mean(self.log_returns))

    @property
    def population_sd(self):
        # Probability law is the equally weighted finite return sample.
        return float(np.std(self.log_returns, ddof=0))

    @property
    def standardized_empirical_shocks(self):
        z = (self.log_returns - self.mean) / self.population_sd
        return z

    @property
    def data_sha256(self):
        # Stable content digest includes dates and full roundtrip precision.
        raw = "".join(f"{date},{value:.17g}\n"
                      for date, value in zip(self.dates, self.log_returns))
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def metadata(self):
        z = self.standardized_empirical_shocks
        return {
            "source_kind": self.source_kind,
            "source_reference": self.source_reference,
            "local_untracked_snapshot": self.cache_path,
            "log_return_sha256": self.data_sha256,
            "observation_count": len(self.dates),
            "first_return_date": self.dates[0],
            "last_return_date": self.dates[-1],
            "historical_log_return_mean": self.mean,
            "historical_log_return_std_ddof0": self.population_sd,
            "historical_log_return_skewness": float(np.mean(z**3)),
            "historical_log_return_excess_kurtosis": float(np.mean(z**4)-3),
            "histogram_only_cannot_identify_time_dependence": True,
            "market_data_are_not_committed": True,
        }


def _check_dates(dates: tuple[str, ...]):
    from datetime import date
    for d in dates:
        date.fromisoformat(d)


def _load_csv(path: Path, kind: str) -> MarketCalibration:
    import pandas as pd

    frame = pd.read_csv(path)
    fields = {str(c).strip().lower().replace(" ", "_"): c for c in frame.columns}
    date_col = fields.get("date") or fields.get("datetime")
    if date_col is None:
        raise ValueError("CSV must have a Date column")
    dates = pd.to_datetime(frame[date_col], errors="raise")
    if dates.isna().any():
        raise ValueError("Missing date")
    unique_dates = tuple(dates.dt.strftime("%Y-%m-%d"))
    _check_dates(unique_dates)
    if kind == "returns_csv":
        col = fields.get("log_return")
        if col is None:
            raise ValueError("returns CSV requires log_return column")
        vals = pd.to_numeric(frame[col], errors="raise").to_numpy(dtype=float)
    elif kind == "prices_csv":
        col = (fields.get("adj_close") or fields.get("adjusted_close") or
               fields.get("close"))
        if col is None:
            raise ValueError("prices CSV requires Adj Close or Close column")
        prices = pd.to_numeric(frame[col], errors="raise").to_numpy(dtype=float)
        if not np.all(np.isfinite(prices)) or np.any(prices <= 0):
            raise ValueError("Prices must be positive finite numbers")
        vals = np.diff(np.log(prices))
        unique_dates = unique_dates[1:]
    else:
        raise ValueError("Unsupported CSV type")
    return MarketCalibration(unique_dates, vals, kind, str(path.resolve()),
                             str(path.resolve()))


def load_calibration(source: str, ticker: str, start: str, end: str,
                     csv_path: Path | None = None,
                     cache_dir: Path = Path("data/market_calibration"),
                     refresh: bool = False) -> MarketCalibration:
    if source in ("returns_csv", "prices_csv"):
        if csv_path is None:
            raise ValueError(f"{source} requires --csv")
        return _load_csv(csv_path, source)
    if source == "synthetic_smoke_only":
        rng = np.random.default_rng(730129)
        # Synthetic fixture must NEVER be labelled an actual financial series.
        vals = .0004 + .01 * (rng.standard_t(5, 1300) * np.sqrt(3/5))
        dates = tuple(f"fixture_{i:05d}" for i in range(vals.size))
        return MarketCalibration(dates, vals,
                                 "synthetic_smoke_only", "offline_test_fixture")
    if source != "yfinance":
        raise ValueError("unknown calibration source")
    if not re.fullmatch(r"[A-Za-z0-9_.^=-]{1,24}", ticker):
        raise ValueError("Invalid ticker identifier")
    from datetime import date
    if date.fromisoformat(start) >= date.fromisoformat(end):
        raise ValueError("Start date must precede end date")
    cache_name = f"{ticker.upper().replace('^','INDEX_')}_{start}_{end}_adjusted_returns.csv"
    cache_file = cache_dir / cache_name
    if cache_file.is_file() and not refresh:
        calibrated = _load_csv(cache_file, "returns_csv")
        return MarketCalibration(calibrated.dates, calibrated.log_returns,
                                 "yfinance_cached_adjusted_close", 
                                 f"{ticker}: {start} to {end} (end exclusive)",
                                 str(cache_file.resolve()))
    try:
        import yfinance as yf
    except ImportError as exc:
        raise RuntimeError(
            'Install market-data dependency: python -m pip install -e ".[finance]"'
        ) from exc
    hist = yf.Ticker(ticker).history(
        start=start, end=end, interval="1d",
        auto_adjust=True, actions=False, raise_errors=True)
    if hist is None or hist.empty or "Close" not in hist:
        raise RuntimeError("Yahoo returned no adjusted daily Close prices")
    closes = hist["Close"].to_numpy(dtype=float)
    if not np.all(np.isfinite(closes)) or np.any(closes <= 0):
        raise ValueError("Yahoo adjusted Close contained invalid values")
    dates = tuple(hist.index.strftime("%Y-%m-%d"))
    if not all(start <= d < end for d in dates):
        raise ValueError("Data provider returned dates outside the frozen window")
    returns = np.diff(np.log(closes))
    calibration = MarketCalibration(
        dates[1:], returns, "yfinance_adjusted_close",
        f"{ticker}: {start} to {end} (end exclusive)")
    # Local user-side research cache: explicitly ignored by .gitignore.
    cache_dir.mkdir(parents=True, exist_ok=True)
    with cache_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(("Date", "log_return"))
        writer.writerows((d, f"{v:.17g}") for d,v in zip(calibration.dates,returns))
    return MarketCalibration(calibration.dates, calibration.log_returns,
                             calibration.source_kind,
                             calibration.source_reference, str(cache_file.resolve()))


def resample_noise(z: np.ndarray, n: int, mode: str,
                   rng: np.random.Generator) -> np.ndarray:
    """Unit-marginal-variance noise; block resampling retains some dependence."""
    if mode not in NOISE_MODES:
        raise ValueError("Unknown noise mode")
    if mode == "gaussian_matched":
        return rng.standard_normal(n)
    if mode == "empirical_iid":
        return z[rng.integers(0, len(z), size=n)]
    block = int(mode.rsplit("_", 1)[1])
    if block < 1 or len(z) < block:
        raise ValueError("Calibration sample is smaller than bootstrap block")
    offsets = np.arange(block, dtype=int)
    nblocks = (n + block - 1) // block
    starts = rng.integers(0, len(z), size=nblocks)
    indices = (starts[:, None] + offsets[None, :]) % len(z)
    return z[indices.ravel()[:n]]


def draw_pool(cal: MarketCalibration, *, n: int, R: int, d: int,
              sigma_eta: float, sigma_epsilon: float, seed: int,
              mode: str, trend_kind: str="stochastic"):
    if trend_kind not in ("stochastic","constant_mean"):
        raise ValueError("unknown trend kind")
    if n <= d + 2 or d not in (1, 2, 3) or R < 1:
        raise ValueError("Require d=1,2,3 and n>=d+3, R>=1")
    # Two independently seeded streams: every noise mode uses the same
    # latent trends for the same seed, n, d. Two sigma levels share the same
    # standardized noise draws, enabling paired scale comparisons.
    trend_rng = np.random.default_rng(np.random.SeedSequence([seed, d, 1701]))
    noise_rng = np.random.default_rng(np.random.SeedSequence(
        [seed, NOISE_MODES.index(mode), 8371]))
    z = cal.standardized_empirical_shocks
    truth, observed = [], []
    for _ in range(R):
        if trend_kind == "constant_mean":
            tau = np.full(n, cal.mean, dtype=float)
        else:
            eps = sigma_epsilon * trend_rng.standard_normal(n-d)
            tau = integrate_differences(eps, d)
        eta = sigma_eta * resample_noise(z, n, mode, noise_rng)
        truth.append(tau)
        observed.append(tau + eta)
    return np.asarray(observed), np.asarray(truth)


def compare_pool(y: np.ndarray, tau: np.ndarray, d: int):
    obj = PooledLOOCV(y, order=d)
    ml = estimate_gaussian_differences(y, obj.d, scan_points=81)
    br = bounded_brent(obj)
    pairs = (
        (METHODS[0], ml.lambda_ratio, ml),
        (METHODS[1], br.best.lam, None),
    )
    rows = []
    for method, lam, fitted in pairs:
        residual = obj.trend(lam) - tau
        rows.append({
            "method": method, "lambda": float(lam),
            "smoothness_s": obj.smoothness(lam),
            "observed_LOOCV_MSE": obj.score(lam),
            "realized_true_trend_MSE": float(np.mean(residual**2)),
            "realized_median_absolute_trend_error": float(
                np.median(np.abs(residual))),
            "estimated_sigma_eta2": (
                float(fitted.sigma_eta2) if fitted is not None else float("nan")),
            "estimated_sigma_epsilon2": (
                float(fitted.sigma_epsilon2) if fitted is not None else float("nan")),
        })
    return rows


def design(preset: str):
    if preset == "smoke":
        return (24,), (.5,), 1, (1,3)
    if preset == "pilot":
        return DEFAULT_N, DEFAULT_SCALES, 5, (1,3)
    if preset == "confirmatory":
        return DEFAULT_N, DEFAULT_SCALES, 100, (1,3)
    raise ValueError("unknown preset")


def summarize(results: list[dict]) -> dict:
    by_pool = {}
    for row in results:
        key = (row["noise_mode"],row["N"],row["sigma_eta"],row["replicate"],row["R"])
        methods = by_pool.setdefault(key,{})
        if row["method"] in methods:
            raise ValueError("duplicate method")
        methods[row["method"]] = row
    if not by_pool or any(set(p) != set(METHODS) for p in by_pool.values()):
        raise ValueError("Missing one of the matched selectors")
    out = []
    for mode in NOISE_MODES:
        sub = [x for k,x in by_pool.items() if k[0]==mode and k[-1]==3]
        out.append({
            "noise_mode": mode,
            "n_R3_pools": len(sub),
            "mean_realized_true_MSE_ML": float(np.mean([
                x[METHODS[0]]["realized_true_trend_MSE"] for x in sub])),
            "mean_realized_true_MSE_LOOCV": float(np.mean([
                x[METHODS[1]]["realized_true_trend_MSE"] for x in sub])),
            "median_realized_true_MSE_ML": float(np.median([
                x[METHODS[0]]["realized_true_trend_MSE"] for x in sub])),
            "median_realized_true_MSE_LOOCV": float(np.median([
                x[METHODS[1]]["realized_true_trend_MSE"] for x in sub])),
            "ML_lower_realized_true_MSE_count": sum(
                x[METHODS[0]]["realized_true_trend_MSE"] <
                x[METHODS[1]]["realized_true_trend_MSE"] for x in sub),
        })
    return {
        "status": "descriptive_only_not_realized_financial_forecast_performance",
        "design": "analyst_fixed_d_common_lambda_pooled_LOOCV",
        "n_total_R1_and_R3_pools": len(by_pool),
        "by_mode_primary_R3": out,
        "critical_limitations": [
            "Market returns supply only empirical noise shape, not a known true stock-price trend.",
            "Observed return histogram is a marginal distribution, not a joint time-series process.",
            "Block resampling preserves local dependence but is not a fitted conditional-volatility model.",
            "Gaussian quasi-ML is not generally invalid for non-Gaussian finite-variance shocks.",
            "Five replicate seeds are insufficient for a conclusive method ranking.",
            "Shared latent innovation seeds and nested R=1/3 permit paired comparisons, NOT independent across noise modes.",
            "All fitted trend orders d are fixed by the analyst; no automatic d-selection was performed.",
        ],
    }


def _histogram_plots(cal: MarketCalibration, out: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    z = cal.standardized_empirical_shocks
    fig, ax = plt.subplots(figsize=(9, 5))
    clipped = np.quantile(z, [.005,.995])
    ax.hist(z, bins=70, density=True, alpha=.55,
            label="Historical centered standardized log returns")
    grid = np.linspace(min(-4,clipped[0]), max(4,clipped[1]), 401)
    ax.plot(grid, norm.pdf(grid), label="Moment-matched standard Gaussian")
    ax.set_xlim(float(clipped[0]), float(clipped[1]))
    ax.set_xlabel("Standardized daily adjusted log return")
    ax.set_ylabel("Density")
    ax.set_title("Empirical return distribution vs Gaussian")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "empirical_return_histogram_vs_gaussian.png", dpi=160)
    plt.close(fig)

    def acf(series, k):
        x = series - np.mean(series)
        denom = np.dot(x,x)
        return np.array([1.]+[
            float(np.dot(x[:-lag],x[lag:])/denom) for lag in range(1,k+1)])
    fig, ax = plt.subplots(figsize=(9, 4.5))
    lags = np.arange(21)
    ax.plot(lags, acf(z, 20), marker="o", label="Returns")
    ax.plot(lags, acf(z**2, 20), marker="o", label="Squared returns")
    ax.axhline(0, lw=1)
    ax.set_xlabel("Trading-day lag")
    ax.set_ylabel("Sample autocorrelation")
    ax.set_title("Dependence diagnostics (not captured by histogram alone)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / "market_return_and_squared_return_acf.png",dpi=160)
    plt.close(fig)


def _git_sha():
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],
            text=True, stderr=subprocess.DEVNULL, timeout=3).strip()
    except (OSError,subprocess.SubprocessError):
        return None


def _write_csv(path: Path, data: list[dict]):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(data[0]))
        writer.writeheader()
        writer.writerows(data)


def execute(*, preset: str, d: int, sigma_epsilon: float, source: str,
            ticker: str, start: str, end: str, csv_path: Path | None,
            cache_dir: Path, refresh: bool, out_dir: Path,
            trend_kind: str="stochastic", dry_run: bool=False):
    if trend_kind not in ("stochastic","constant_mean"):
        raise ValueError("unknown trend kind")
    if d not in (1,2,3) or sigma_epsilon<=0:
        raise ValueError("Select fixed d=1,2,3 and positive innovation SD")
    ns, scales, reps, Rs = design(preset)
    base_seed = SEED_BASE if preset != "confirmatory" else SEED_BASE+1000000
    manifest = {
        "protocol": "real_market_log_return_shaped_synthetic_noise_v1",
        "status": "planned" if dry_run else "executed",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "preset": preset, "source": source, "ticker": ticker,
        "start_inclusive": start, "end_exclusive": end,
        "analyst_fixed_difference_order": d,
        "trend_kind": trend_kind,
        "sigma_epsilon_option": sigma_epsilon,
        "effective_trend_innovation_sd": 0.0 if trend_kind == "constant_mean" else sigma_epsilon,
        "synthetic_noise_population_sd": list(scales),
        "simulation_series_lengths": list(ns),
        "replicate_seeds_per_length": reps,
        "pool_sizes": list(Rs),
        "noise_modes": list(NOISE_MODES),
        "seed_base": base_seed,
        "seed_formula": "seed_base + 10000*N_index + replicate",
        "shared_trend_seed_across_noise_modes_and_scales": True,
        "nested_first_series_R1_in_R3": True,
        "methods": list(METHODS),
        "expected_nested_pools": len(ns)*len(scales)*reps*len(Rs)*len(NOISE_MODES),
        "expected_method_rows": len(ns)*len(scales)*reps*len(Rs)*len(NOISE_MODES)*len(METHODS),
        "trend_construction": ("constant tau_t=historical mean log return; D_d tau = 0" if trend_kind == "constant_mean" else "D_d tau = iid Gaussian innovation; tau_j=0.02*(j-1) j<=d"),
        "observations": "y_t=tau_t + sigma_eta * empirically shaped centered standardized return draw",
        "market_historical_mean_is_not_identified_stock_trend": True,
        "market_return_values_in_manifest": False,
        "data_sha256_required_for_reproducibility": True,
        "source_sha": _git_sha(), "python":platform.python_version(),
        "numpy":np.__version__, "scipy":scipy.__version__,
    }
    if dry_run:
        print(json.dumps(manifest,indent=2))
        return manifest
    calibration=load_calibration(
        "synthetic_smoke_only" if preset=="smoke" else source,
        ticker,start,end,csv_path,cache_dir,refresh)
    manifest["calibration"]=calibration.metadata()
    out_dir.mkdir(parents=True, exist_ok=True)
    rows=[]
    for ni,n in enumerate(ns):
        for scale in scales:
            for rep in range(reps):
                seed=base_seed+10000*ni+rep
                for mode in NOISE_MODES:
                    for R in Rs:
                        y,tau=draw_pool(calibration,n=n,R=R,d=d,
                                        sigma_eta=scale,
                                        sigma_epsilon=sigma_epsilon,
                                        seed=seed,mode=mode,trend_kind=trend_kind)
                        for method in compare_pool(y,tau,d):
                            rows.append({
                                "N": n,"d":d,"trend_kind":trend_kind,
                                "sigma_eta":scale,
                                "sigma_epsilon":sigma_epsilon,
                                "replicate":rep,"seed":seed,
                                "noise_mode":mode,"R":R,
                                "calibration_data_sha256":calibration.data_sha256,
                                **method,
                            })
    summary=summarize(rows)
    manifest["actual_method_rows"]=len(rows)
    _write_csv(out_dir/"method_comparison.csv",rows)
    (out_dir/"summary.json").write_text(
        json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    (out_dir/"manifest.json").write_text(
        json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    if preset!="smoke":
        _histogram_plots(calibration,out_dir)
    print(json.dumps({
        "status":"executed","source":manifest["calibration"]["source_kind"],
        "returns":calibration.metadata()["observation_count"],
        "output":str(out_dir),"summary":summary,
    },indent=2))
    return summary


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--preset", choices=("smoke","pilot","confirmatory"),
                   default="smoke")
    p.add_argument("--d",type=int,default=2)
    p.add_argument("--trend-kind",choices=("stochastic","constant_mean"),default="stochastic")
    p.add_argument("--sigma-epsilon",type=float,default=.3)
    p.add_argument("--source",choices=("yfinance","returns_csv","prices_csv"),
                   default="yfinance")
    p.add_argument("--ticker",default="SPY")
    p.add_argument("--start",default="2015-01-01")
    p.add_argument("--end",default="2026-01-01")
    p.add_argument("--csv",type=Path,default=None)
    p.add_argument("--cache-dir",type=Path,
                   default=Path("data/market_calibration"))
    p.add_argument("--refresh-data",action="store_true")
    p.add_argument("--out-dir",type=Path,default=None)
    p.add_argument("--dry-run",action="store_true")
    a=p.parse_args()
    base=(Path("results/pooled_loocv_smoothness/empirical_market_noise") / a.ticker / f"d{a.d}")
    out=a.out_dir or (base/a.preset if a.trend_kind=="stochastic" else base/"constant_mean"/a.preset)
    execute(preset=a.preset,d=a.d,sigma_epsilon=a.sigma_epsilon,
            source=a.source,ticker=a.ticker,start=a.start,end=a.end,
            csv_path=a.csv,cache_dir=a.cache_dir,refresh=a.refresh_data,
            out_dir=out,trend_kind=a.trend_kind,dry_run=a.dry_run)


if __name__=="__main__":
    main()
