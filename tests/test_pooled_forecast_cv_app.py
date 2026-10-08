"""Smoke-test the new independent Streamlit page with its offline synthetic default."""
from __future__ import annotations

from pathlib import Path

import pytest


APP = Path(__file__).resolve().parents[1] / "apps" / "pooled_forecast_cv.py"


def test_standalone_pooled_app_compiles():
    # The scientific engine has separate mathematical regression tests.
    compile(APP.read_text(encoding="utf-8"), str(APP), "exec")


def test_standalone_pooled_app_renders_synthetic_defaults():
    pytest.importorskip("streamlit")
    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file(str(APP), default_timeout=90).run()
    assert len(at.exception) == 0, [e.message for e in at.exception]
    assert at.title and "CV · Promedio histórico de F(S)" in at.title[0].value
    assert at.metric and any("Pooled selected S" in x.label for x in at.metric)
