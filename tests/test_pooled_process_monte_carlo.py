"""Deterministic small numerical fixtures; never launch an MC campaign in CI."""

import csv
import gzip
import json

import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.run_process_monte_carlo import (
    METHODS, _chunks, _holm_global, _mean_ci95, run,
)


def test_chunk_ranges_cover_only_requested_independent_seeds():
    assert _chunks(1, 6, 2) == [(1, 3), (3, 5), (5, 7)]
    assert _chunks(101, 2, 25) == [(101, 103)]


def test_mean_ci_and_holm_consistency():
    values = np.array([-0.5, -0.2, -0.4, 0.1, -0.1])
    mean, sd, lo, hi, p = _mean_ci95(values)
    assert lo <= mean <= hi
    assert sd > 0
    assert 0 < p <= 1
    with pytest.raises(ValueError):
        _mean_ci95(np.array([]))
    assert np.isnan(_mean_ci95(np.array([2.]))[2])
    rows = [
        {"paired_t_p_uncorrected": .001, "paired_t_p_holm_all_processes": None},
        {"paired_t_p_uncorrected": .04, "paired_t_p_holm_all_processes": None},
        {"paired_t_p_uncorrected": .02, "paired_t_p_holm_all_processes": None},
    ]
    _holm_global(rows)
    assert [row["paired_t_p_holm_all_processes"] for row in rows] == pytest.approx(
        [.003, .04, .04]
    )


def test_preview_writes_no_outputs_and_rejects_bad_parameters(tmp_path):
    folder = tmp_path / "dry"
    plan = run(out_dir=folder, count=200, names=("gaussian_reference",),
               preview=True)
    assert plan["status"] == "PLAN_ONLY_NO_SIMULATION"
    assert plan["expected_rows"] == 200 * 2 * len(METHODS)
    assert not folder.exists()
    for arg in ({"count": 0}, {"start": 0}, {"n": 16},
                {"chunk_size": 0}, {"scan_points": 3},
                {"names": ("invented",)}):
        with pytest.raises(ValueError):
            run(out_dir=folder, preview=True, **arg)


def test_one_small_completed_shard_and_resume_rejects_complete(tmp_path):
    # One genuine seed, one mechanism, nested R1/R3: 22 method-level fits.
    # This exercises the real selector code and both paired reporting paths.
    folder = tmp_path / "trial"
    result = run(out_dir=folder, count=1, start=7,
                 chunk_size=1, n=32, scan_points=7,
                 names=("gaussian_reference",))
    assert result["status"] == "COMPLETE"
    assert result["actual_method_rows"] == 2 * len(METHODS)
    assert result["summary_rows"] == 2 * len(METHODS)
    assert result["pairwise_rows"] == 2 * len(METHODS) * (len(METHODS) - 1) // 2
    assert result["pooling_rows"] == len(METHODS)
    assert json.loads((folder / "manifest.json").read_text())["design"]["seed_start_inclusive"] == 7
    raw_files = list(folder.glob("rows_*.csv.gz"))
    assert len(raw_files) == 1
    with gzip.open(raw_files[0], "rt", encoding="utf-8") as file:
        records = list(csv.DictReader(file))
    assert len(records) == 2 * len(METHODS)
    assert {int(row["rng_seed"]) for row in records} == {20261019 + 7}
    one = {row["method"]: row for row in records if row["R"] == "1"}
    three = {row["method"]: row for row in records if row["R"] == "3"}
    assert set(one) == set(three) == set(METHODS)
    for rec in one.values():
        assert float(rec["first_series_mse"]) == pytest.approx(
            float(rec["pool_mse"]), rel=0, abs=1e-12
        )
    for output in ("risk_by_process_method.csv",
                   "paired_method_mse_differences.csv",
                   "paired_pooling_first_series.csv"):
        assert (folder / output).is_file()
    with pytest.raises(ValueError, match="already COMPLETE"):
        run(out_dir=folder, count=1, start=7, chunk_size=1,
            n=32, scan_points=7, names=("gaussian_reference",), resume=True)
    with pytest.raises(FileExistsError):
        run(out_dir=folder, count=1, start=7, chunk_size=1,
            n=32, scan_points=7, names=("gaussian_reference",))
