from __future__ import annotations

from pathlib import Path


def test_tracked_minima_dashboard_compiles():
    path = Path(
        "experiments/numerical_smoothness_selection/"
        "dashboard_tracked_minima.py"
    )
    source = path.read_text(encoding="utf-8")
    compile(source, str(path), "exec")
