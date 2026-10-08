"""Launcher: CV dinámico con seguimiento de mínimos y matrices V.

Entrypoint recomendado:
    streamlit run apps/dynamic_branch_cv.py

El nombre anterior, apps/smoothness_lab.py, permanece por compatibilidad.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from apps.smoothness_lab import main


if __name__ == "__main__":
    main()
