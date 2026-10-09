"""Contracts for three independent current paper apps, not legacy Val1/Val2."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "apps"


@pytest.mark.parametrize("filename", [
    "pooled_forecast_cv.py",
    "dynamic_branch_cv.py",
    "numerical_methods.py",
])
def test_current_paper_apps_have_valid_syntax_and_unique_main(filename):
    path = APPS / filename
    source = path.read_text(encoding="utf-8")
    compile(source,str(path),"exec")
    assert "def main(" in source
    assert "if __name__" in source


def test_current_dynamic_app_is_not_the_legacy_val1_val2_launcher():
    source = (APPS / "dynamic_branch_cv.py").read_text(encoding="utf-8")
    assert "from apps.smoothness_lab import main" not in source
    assert "from apps.smoothness_lab_advanced import main" not in source
    assert "run_weighted_surface_study" in source
    assert "LossWeighting" in source
    assert "branch_plot" in source
    assert "tracked_branch" in source
    assert "val2_mse" not in source


def test_current_numeric_app_analyzes_one_fixed_objective_not_branches():
    source = (APPS / "numerical_methods.py").read_text(encoding="utf-8")
    assert "find_stationary_points_smoothness" in source
    assert "smoothness_derivatives" in source
    assert "weighted_analytic_objective" in source
    assert "track_grid_branches(" not in source
    assert "val2_mse" not in source


def test_current_pooled_app_aggregates_weighted_curves_and_global_argmin():
    source = (APPS / "pooled_forecast_cv.py").read_text(encoding="utf-8")
    assert "weighted_surface_history" in source
    assert "select_from_grid(" in source
    assert "fold_loss_at_lambda" in source
    assert "track_grid_branches(" not in source
    assert "argmin" in source


def test_one_app_per_active_paper_is_documented_for_new_agents():
    expected=("pooled_forecast_cv.py","dynamic_branch_cv.py","numerical_methods.py")
    for document in (
        ROOT/"AGENTS.md", ROOT/"AI_HANDOFF.md", APPS/"README.md",
        ROOT/"working_papers/THEORETICAL_CONTRIBUTIONS.md",
    ):
        text=document.read_text(encoding="utf-8")
        for filename in expected:
            assert filename in text, (document,filename)
    legacy=(APPS/"smoothness_lab.py").read_text(encoding="utf-8")
    assert "val2" in legacy.lower()


def test_weighted_derivative_callback_matches_finite_difference():
    pytest.importorskip("streamlit")
    from apps.numerical_methods import weighted_analytic_objective
    from trend_estimation.forecasting.objectives import (
        prepare_rolling_pure_forecast_objective,
    )
    from trend_estimation.validation.rolling_origin import RollingOriginSplit

    y=np.arange(60,dtype=float)*0.13+np.sin(np.arange(60)/7)
    d=2
    splits=[
        RollingOriginSplit(train=slice(t-20,t),validation=slice(t,t+3))
        for t in (30,36,42)
    ]
    prepared=prepare_rolling_pure_forecast_objective(
        y,splits,order=d,
    )
    weights=np.asarray([.15,.25,.60])
    callback=weighted_analytic_objective(prepared,weights)
    for lam in (.01,.5,3.):
        delta=1e-4*max(lam,1.)
        value,first,second=callback(lam)
        plus=callback(lam+delta)
        minus=callback(lam-delta)
        first_fd=(plus[0]-minus[0])/(2*delta)
        second_fd=(plus[0]-2*value+minus[0])/delta**2
        assert first==pytest.approx(first_fd,rel=1e-4,abs=1e-6)
        assert second==pytest.approx(second_fd,rel=3e-3,abs=1e-4)


def test_current_dynamic_and_numerical_streamlit_synthetic_smoke():
    st=pytest.importorskip("streamlit")
    from streamlit.testing.v1 import AppTest
    for filename in ("dynamic_branch_cv.py","numerical_methods.py"):
        path=APPS/filename
        report=AppTest.from_file(str(path),default_timeout=120).run()
        assert len(report.exception)==0,[
            (filename,exc.message) for exc in report.exception
        ]
