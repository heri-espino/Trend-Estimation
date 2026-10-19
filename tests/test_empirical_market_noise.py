"""Offline contracts: real-market-shape experiment never needs network in CI."""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiments.pooled_loocv_smoothness.run_empirical_market_noise import (
    METHODS, NOISE_MODES, MarketCalibration, _load_csv, draw_pool, execute,
    load_calibration, resample_noise, summarize,
)
from experiments.pooled_loocv_smoothness.objective import difference_matrix


def synthetic_calibration():
    rng=np.random.default_rng(80)
    r=.001+.013*rng.standard_t(5,size=700)
    dates=tuple(f"fixture_{i:05d}" for i in range(len(r)))
    return MarketCalibration(dates,r,"explicit_fixture","only_tests")


def test_historical_return_standardization_exact_marginal_moments():
    cal=synthetic_calibration()
    z=cal.standardized_empirical_shocks
    assert np.mean(z)==pytest.approx(0,abs=1e-12)
    assert np.mean(z**2)==pytest.approx(1,abs=1e-12)
    assert cal.metadata()["log_return_sha256"]==cal.data_sha256
    assert len(cal.data_sha256)==64


def test_resample_noise_modes_use_distribution_and_blocks():
    cal=synthetic_calibration()
    z=cal.standardized_empirical_shocks
    for mode in NOISE_MODES:
        noise=resample_noise(z,50,mode,np.random.default_rng(100))
        assert noise.shape==(50,)
        assert np.all(np.isfinite(noise))
    iid=resample_noise(z,50000,"empirical_iid",np.random.default_rng(333))
    assert float(iid.mean())==pytest.approx(0,abs=.02)
    assert float(iid.var())==pytest.approx(1,rel=.05)

    # Circular blocks use consecutive observed historical indices.
    simple=np.arange(400,dtype=float)
    block=resample_noise(simple,40,"circular_block_20",np.random.default_rng(800))
    increments=(np.diff(block[:20]) % len(simple))
    assert np.all(increments==1)
    with pytest.raises(ValueError):
        resample_noise(simple,20,"nonsense",np.random.default_rng(1))


@pytest.mark.parametrize("d",[1,2,3])
def test_nested_pool_and_same_latent_truth_across_modes_and_noise_scales(d):
    cal=synthetic_calibration()
    kwargs=dict(n=50,d=d,sigma_epsilon=.3,seed=518)
    y1,tau1=draw_pool(cal,R=1,sigma_eta=.5,mode="empirical_iid",**kwargs)
    y3,tau3=draw_pool(cal,R=3,sigma_eta=.5,mode="empirical_iid",**kwargs)
    np.testing.assert_array_equal(y1[0],y3[0])
    np.testing.assert_array_equal(tau1[0],tau3[0])
    yg,tg=draw_pool(cal,R=3,sigma_eta=.5,mode="gaussian_matched",**kwargs)
    np.testing.assert_array_equal(tau3,tg)
    yscaled,tscaled=draw_pool(cal,R=3,sigma_eta=2.0,mode="empirical_iid",**kwargs)
    np.testing.assert_array_equal(tau3,tscaled)
    np.testing.assert_allclose(yscaled-tscaled,4*(y3-tau3))
    # Generator order is exactly the penalized difference order.
    for series in tau3:
        innov=difference_matrix(50,d)@series
        assert np.all(np.isfinite(innov))


def test_csv_price_to_return_transform_and_loader(tmp_path):
    n=120
    idx=pd.date_range("2020-01-01",periods=n,freq="D")
    increments=.001+.0003*np.sin(np.arange(n)/6)
    prices=100*np.exp(np.cumsum(increments))
    filename=tmp_path/"prices.csv"
    pd.DataFrame({"Date":idx,"Adj Close":prices}).to_csv(filename,index=False)
    cal=_load_csv(filename,"prices_csv")
    assert len(cal.log_returns)==n-1
    np.testing.assert_allclose(cal.log_returns,increments[1:])
    assert cal.dates[0]=="2020-01-02"

    returns_file=tmp_path/"log_returns.csv"
    pd.DataFrame({"Date":idx,
                  "log_return":.001+np.random.default_rng(1).normal(size=n)}).to_csv(
        returns_file,index=False)
    cal=load_calibration("returns_csv","SPY","2020-01-01","2021-01-01",
                         csv_path=returns_file)
    assert len(cal.dates)==120


def test_bad_source_rejected_without_silent_fallback(tmp_path):
    bad=tmp_path/"bad.csv"
    pd.DataFrame({"Date":pd.date_range("2023-01-01",periods=120),
                  "log_return":np.ones(120)}).to_csv(bad,index=False)
    with pytest.raises(ValueError,match="zero empirical variation"):
        _load_csv(bad,"returns_csv")
    with pytest.raises(ValueError,match="requires --csv"):
        load_calibration("returns_csv","SPY","2020-01-01","2021-01-01")
    with pytest.raises(ValueError):
        MarketCalibration(tuple(f"fixture_{i:03d}" for i in range(101)),
                          np.array([np.nan]*101),"test","test")


def test_smoke_runs_all_modes_and_reports_fixture_not_financial_data(tmp_path):
    out=tmp_path/"smoke"
    kwargs=dict(preset="smoke",d=2,sigma_epsilon=.3,source="yfinance",
                ticker="SPY",start="2015-01-01",end="2026-01-01",
                csv_path=None,cache_dir=tmp_path/"cache",refresh=False,
                out_dir=out)
    assert not out.exists()
    manifest=execute(dry_run=True,**kwargs)
    assert manifest["expected_nested_pools"]==8
    assert manifest["expected_method_rows"]==16
    assert not out.exists()
    summary=execute(dry_run=False,**kwargs)
    assert summary["n_total_R1_and_R3_pools"]==8
    assert set(x["noise_mode"] for x in summary["by_mode_primary_R3"])==set(NOISE_MODES)
    saved=json.loads((out/"manifest.json").read_text())
    assert saved["calibration"]["source_kind"]=="synthetic_smoke_only"
    assert saved["actual_method_rows"]==16
    assert not (tmp_path/"cache").exists()
    assert (out/"method_comparison.csv").stat().st_size>100
    assert not (out/"empirical_return_histogram_vs_gaussian.png").exists()


def test_distribution_histogram_and_lag_chart_offline(tmp_path):
    from experiments.pooled_loocv_smoothness.run_empirical_market_noise import (
        _histogram_plots,
    )
    _histogram_plots(synthetic_calibration(),tmp_path)
    assert (tmp_path/"empirical_return_histogram_vs_gaussian.png").stat().st_size>100
    assert (tmp_path/"market_return_and_squared_return_acf.png").stat().st_size>100


def test_invalid_difference_order_fails_without_side_effects(tmp_path):
    with pytest.raises(ValueError):
        execute(preset="smoke",d=4,sigma_epsilon=.3,source="yfinance",
                ticker="SPY",start="2015-01-01",end="2026-01-01",
                csv_path=None,cache_dir=tmp_path,refresh=False,
                out_dir=tmp_path/"out")
