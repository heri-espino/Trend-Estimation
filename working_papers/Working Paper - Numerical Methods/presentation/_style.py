"""Shared presentation-figure I/O. Frozen inputs are read-only."""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PAPER = HERE.parent
RESULTS = ROOT / "results" / "numerical_smoothness_selection"
RUNS = {
    "adversarial": RESULTS / "20260930T113400Z_adversarial-paper_c8f4ab2",
    "synthetic": RESULTS / "20260930T113415Z_synthetic-paper_c8f4ab2",
    "sensitivity": RESULTS / "20260930T121654Z_sensitivity-paper_4a43fd5",
    "financial": RESULTS / "20260930T212604Z_financial-stress-paper_b40b192",
    "applied": RESULTS / "20261001T022610Z_applied-paper_72b8aaa",
}
BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
PURPLE = "#CC79A7"
GOLD = "#E69F00"
GREY = "#697586"
BLACK = "#202C39"
COLORS = [BLUE, ORANGE, GREEN, PURPLE, GOLD]
_OUTPUT = HERE / "figures"
_FORMAT = "both"


def configure(output_dir: Path | None = None, fmt: str = "both") -> None:
    global _OUTPUT, _FORMAT
    _OUTPUT = (HERE / "figures") if output_dir is None else Path(output_dir).resolve()
    _FORMAT = fmt
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 15,
        "axes.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
        "pdf.fonttype": 42,
        "axes.formatter.useoffset": False,
    })


def canvas(rows: int = 1, cols: int = 1, *, title: str = "", height: float = 7.1):
    fig, axs = plt.subplots(rows, cols, figsize=(12.8, height), constrained_layout=True)
    if title:
        fig.suptitle(title, fontsize=19, fontweight="bold", x=0.04, ha="left")
    return fig, np.asarray(axs, dtype=object).reshape(-1)


def finish(fig, name: str, note: str = "") -> list[Path]:
    if note:
        fig.text(0.015, 0.007, note, color=GREY, fontsize=8)
    _OUTPUT.mkdir(parents=True, exist_ok=True)
    formats = ("pdf", "png") if _FORMAT == "both" else (_FORMAT,)
    paths = []
    for fmt in formats:
        dest = _OUTPUT / (name + "." + fmt)
        fig.savefig(dest, format=fmt, dpi=180, bbox_inches="tight", pad_inches=0.18)
        paths.append(dest)
    plt.close(fig)
    print("  " + name + " -> " + ", ".join(str(x) for x in paths))
    return paths


def frozen_csv(name: str, file: str) -> pd.DataFrame:
    path = RUNS[name] / file
    if not path.is_file():
        raise FileNotFoundError(
            f"Required frozen file: {path}\n"
            "These scripts only read the committed historical results. "
            "Restore the file; do not replace it with a new simulation run."
        )
    return pd.read_csv(path)


def panel(ax, title: str, xlabel: str = "", ylabel: str = "") -> None:
    ax.set_title(title, loc="left", fontweight="semibold", pad=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.16, lw=0.7)


def annotate_kind(ax, x: float, y: float, label: str, color: str = BLUE) -> None:
    ax.scatter([x], [y], s=65, color=color, zorder=5, edgecolor="white")
    ax.annotate(label, (x, y), xytext=(7, 8), textcoords="offset points",
                color=color, fontsize=10, fontweight="semibold")
