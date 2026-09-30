from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


RESULT_ROOT = Path("results") / "numerical_smoothness_selection"
FROZEN_RUNS = {
    "adversarial": (
        RESULT_ROOT
        / "20260930T113400Z_adversarial-paper_c8f4ab2"
    ),
    "synthetic": (
        RESULT_ROOT
        / "20260930T113415Z_synthetic-paper_c8f4ab2"
    ),
    "sensitivity": (
        RESULT_ROOT
        / "20260930T121654Z_sensitivity-paper_4a43fd5"
    ),
    "financial": (
        RESULT_ROOT
        / "20260930T212604Z_financial-stress-paper_b40b192"
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate manuscript tables and figures from the frozen numerical "
            "smoothness-selection result directories."
        )
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("paper_numerical-smoothness-selection"),
    )
    return parser.parse_args()


def _require(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(
            f"Frozen paper input is missing: {path}. "
            "Do not silently substitute another result run."
        )
    return path


def _benchmark_summary() -> tuple[pd.DataFrame, dict[str, pd.DataFrame]]:
    adversarial_methods = pd.read_csv(
        _require(FROZEN_RUNS["adversarial"] / "method_summary.csv")
    )
    adversarial_detection = pd.read_csv(
        _require(FROZEN_RUNS["adversarial"] / "stationary_detection.csv")
    )
    synthetic = pd.read_csv(
        _require(FROZEN_RUNS["synthetic"] / "search_summary.csv")
    )
    financial = pd.read_csv(
        _require(FROZEN_RUNS["financial"] / "search_summary.csv")
    )

    relevant = adversarial_detection.loc[
        adversarial_detection["truth_kind"] != "stationary_inflection"
    ]
    adaptive_relevant = relevant.loc[
        relevant["method"].eq("adaptive_s")
    ]
    adaptive_adv = adversarial_methods.loc[
        adversarial_methods["method"].eq("adaptive_s")
    ]
    dense_adv = adversarial_methods.loc[
        adversarial_methods["method"].eq("dense")
    ]

    rows = [
        {
            "benchmark": "adversarial",
            "surfaces": int(len(adaptive_adv)),
            "reference_minima": int(len(adaptive_relevant)),
            "matched_minima": int(adaptive_relevant["detected"].sum()),
            "missed_minima": int((~adaptive_relevant["detected"]).sum()),
            "mean_adaptive_evaluations": float(
                adaptive_adv["n_evaluations"].mean()
            ),
            "mean_dense_evaluations": float(
                dense_adv["n_evaluations"].mean()
            ),
            "evaluation_fraction": float(
                adaptive_adv["n_evaluations"].mean()
                / dense_adv["n_evaluations"].mean()
            ),
            "max_s_error": float(
                adaptive_adv["best_s_distance_to_true"].max()
            ),
            "positive_regret_cases": int(
                (adaptive_adv["objective_regret"] > 1e-12).sum()
            ),
        },
        {
            "benchmark": "synthetic",
            "surfaces": int(len(synthetic)),
            "reference_minima": int(
                synthetic["n_dense_interior_minima"].sum()
            ),
            "matched_minima": int(
                synthetic["n_dense_interior_minima_matched"].sum()
            ),
            "missed_minima": int(
                synthetic["n_dense_interior_minima_missed"].sum()
            ),
            "mean_adaptive_evaluations": float(
                synthetic["adaptive_evaluations"].mean()
            ),
            "mean_dense_evaluations": float(
                synthetic["dense_evaluations"].mean()
            ),
            "evaluation_fraction": float(
                (
                    synthetic["adaptive_evaluations"]
                    / synthetic["dense_evaluations"]
                ).mean()
            ),
            "max_s_error": float(synthetic["best_s_abs_error"].max()),
            "positive_regret_cases": int(
                (synthetic["objective_regret"] > 1e-12).sum()
            ),
        },
        {
            "benchmark": "financial",
            "surfaces": int(len(financial)),
            "reference_minima": int(
                financial["n_dense_interior_minima"].sum()
            ),
            "matched_minima": int(
                financial["n_dense_interior_minima_matched"].sum()
            ),
            "missed_minima": int(
                financial["n_dense_interior_minima_missed"].sum()
            ),
            "mean_adaptive_evaluations": float(
                financial["adaptive_evaluations"].mean()
            ),
            "mean_dense_evaluations": float(
                financial["dense_evaluations"].mean()
            ),
            "evaluation_fraction": float(
                (
                    financial["adaptive_evaluations"]
                    / financial["dense_evaluations"]
                ).mean()
            ),
            "max_s_error": float(financial["best_s_abs_error"].max()),
            "positive_regret_cases": int(
                (financial["objective_regret"] > 1e-12).sum()
            ),
        },
    ]
    return pd.DataFrame(rows), {
        "adversarial_methods": adversarial_methods,
        "synthetic": synthetic,
        "financial": financial,
    }


def _latex_benchmark_table(frame: pd.DataFrame) -> str:
    display = frame.copy()
    display["benchmark"] = display["benchmark"].str.capitalize()
    display["recovery"] = (
        display["matched_minima"].astype(str)
        + "/"
        + display["reference_minima"].astype(str)
    )
    display["mean evals"] = display["mean_adaptive_evaluations"].map(
        lambda value: f"{value:.1f}"
    )
    display["dense evals"] = display["mean_dense_evaluations"].map(
        lambda value: f"{value:.0f}"
    )
    display["eval. fraction"] = display["evaluation_fraction"].map(
        lambda value: f"{100.0 * value:.2f}\\%"
    )
    display["max |dS|"] = display["max_s_error"].map(
        lambda value: f"{value:.2e}"
    )
    display = display[
        [
            "benchmark",
            "surfaces",
            "recovery",
            "positive_regret_cases",
            "mean evals",
            "dense evals",
            "eval. fraction",
            "max |dS|",
        ]
    ].rename(
        columns={
            "benchmark": "Benchmark",
            "surfaces": "Surfaces",
            "recovery": "Minima recovered",
            "positive_regret_cases": "Positive regret",
        }
    )
    return display.to_latex(
        index=False,
        escape=False,
        column_format="lrrrrrrr",
    )


def _latex_sensitivity_table(frame: pd.DataFrame) -> str:
    display = frame.copy()
    display["Specification"] = np.where(
        display["is_primary"],
        "Primary",
        display["parameter"].astype(str)
        + "="
        + display["setting"].astype(str),
    )
    display["Mean evals"] = display["mean_evaluations"].map(
        lambda value: f"{value:.1f}"
    )
    display["Max |dS|"] = display["max_abs_s_error"].map(
        lambda value: f"{value:.2e}"
    )
    display = display[
        [
            "Specification",
            "missed_minima",
            "positive_regret_cases",
            "Mean evals",
            "Max |dS|",
        ]
    ].rename(
        columns={
            "missed_minima": "Missed minima",
            "positive_regret_cases": "Positive regret",
        }
    )
    return display.to_latex(
        index=False,
        escape=False,
        column_format="lrrrr",
    )


def _plot_evaluation_efficiency(
    benchmark: pd.DataFrame,
    raw: dict[str, pd.DataFrame],
    path: Path,
) -> None:
    synthetic = benchmark.loc[benchmark["benchmark"].eq("synthetic")].iloc[0]
    financial = benchmark.loc[benchmark["benchmark"].eq("financial")].iloc[0]
    adv = raw["adversarial_methods"].groupby("method")["n_evaluations"].mean()

    labels = [
        "Synthetic\nAdaptive",
        "Synthetic\nDense",
        "Adversarial\nAdaptive",
        "Adversarial\nlog-lambda",
        "Adversarial\nDense",
        "Financial\nAdaptive",
        "Financial\nDense",
    ]
    values = [
        synthetic["mean_adaptive_evaluations"],
        synthetic["mean_dense_evaluations"],
        float(adv.loc["adaptive_s"]),
        float(adv.loc["log_lambda"]),
        float(adv.loc["dense"]),
        financial["mean_adaptive_evaluations"],
        financial["mean_dense_evaluations"],
    ]

    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    ax.bar(np.arange(len(labels)), values)
    ax.set_yscale("log")
    ax.set_ylabel("Mean objective/derivative evaluations")
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_title("Evaluation cost across frozen benchmarks")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def _plot_optimum_agreement(
    synthetic: pd.DataFrame,
    financial: pd.DataFrame,
    path: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.scatter(
        synthetic["dense_best_s"],
        synthetic["adaptive_best_s"],
        s=8,
        alpha=0.30,
        label="Synthetic",
    )
    ax.scatter(
        financial["dense_best_s"],
        financial["adaptive_best_s"],
        s=13,
        alpha=0.45,
        label="Financial",
    )
    ax.plot([0.0, 1.0], [0.0, 1.0], linewidth=1.0)
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.01, 1.01)
    ax.set_xlabel("Dense-reference selected smoothness")
    ax.set_ylabel("Adaptive selected smoothness")
    ax.set_title("Selected-smoothness agreement")
    ax.legend(frameon=False)
    ax.grid(alpha=0.20)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def _plot_sensitivity_tradeoff(frame: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.scatter(
        frame["mean_evaluations"],
        frame["missed_minima"],
        s=45,
    )

    for _, row in frame.iterrows():
        label = (
            "primary"
            if bool(row["is_primary"])
            else f"{row['parameter']}={row['setting']}"
        )
        ax.annotate(
            label,
            (row["mean_evaluations"], row["missed_minima"]),
            xytext=(3, 3),
            textcoords="offset points",
            fontsize=7,
        )

    ax.set_xlabel("Mean adaptive evaluations")
    ax.set_ylabel("Missed dense-reference minima")
    ax.set_title("One-factor search-design sensitivity")
    ax.grid(alpha=0.20)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    args = parse_args()
    table_dir = args.output_dir / "tables"
    figure_dir = args.output_dir / "figures"
    table_dir.mkdir(parents=True, exist_ok=True)
    figure_dir.mkdir(parents=True, exist_ok=True)

    benchmark, raw = _benchmark_summary()
    sensitivity = pd.read_csv(
        _require(FROZEN_RUNS["sensitivity"] / "sensitivity_summary.csv")
    )

    benchmark.to_csv(table_dir / "benchmark_summary.csv", index=False)
    sensitivity.to_csv(table_dir / "sensitivity_summary.csv", index=False)
    (table_dir / "benchmark_summary.tex").write_text(
        _latex_benchmark_table(benchmark),
        encoding="utf-8",
    )
    (table_dir / "sensitivity_summary.tex").write_text(
        _latex_sensitivity_table(sensitivity),
        encoding="utf-8",
    )

    _plot_evaluation_efficiency(
        benchmark,
        raw,
        figure_dir / "evaluation_efficiency.pdf",
    )
    _plot_optimum_agreement(
        raw["synthetic"],
        raw["financial"],
        figure_dir / "optimum_agreement.pdf",
    )
    _plot_sensitivity_tradeoff(
        sensitivity,
        figure_dir / "sensitivity_tradeoff.pdf",
    )

    print(f"Wrote frozen manuscript evidence under {args.output_dir}")


if __name__ == "__main__":
    main()
