"""One-command, NO NEW SIMULATIONS, frozen three-paper retrospective report.

From repository root:
    python -m experiments.smoothness_cv.finalize_frozen_study \
      --original results/smoothness_cv/joint_formal_8h_v1 \
      --frozen results/smoothness_cv/joint_formal_8h_v1_FROZEN

If a completed old backup is named outcomes.sqlite.incomplete, validates it
and finalizes it. If no backup exists, FAILS SAFELY rather than silently
copying 31 GiB or running Monte Carlo. Use recover_campaign explicitly if
you need to create a fresh backup.

Once frozen, streams OLD rows only, produces compact P1/2/3 CSVs and
figures, and creates an actual-numbers REPORT_BRIEF.md for publication
review. No CUDA, no DGP generation, and no PyTorch imports.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import json

from .recover_campaign import freeze, inspect
from .analyze_frozen_compact import analyze
from .plot_frozen_compact import plot


def finalize(original:Path, frozen:Path, *, analyze_only:bool=False):
    original=Path(original)
    frozen=Path(frozen)
    if not (frozen/"manifest.json").is_file() or not (
        frozen/"outcomes.sqlite"
    ).is_file():
        if (frozen/"outcomes.sqlite.incomplete").is_file():
            if analyze_only:
                raise FileNotFoundError(
                    "A previous SQLite snapshot is not finalized. "
                    "Use this command without --analyze-only to validate "
                    "the existing .incomplete snapshot (not recopy it)."
                )
            print("Validating and promoting existing old 31-GiB copy, "
                  "NO new copy and NO simulation...",flush=True)
            freeze(original,frozen,inspect(original),finalize_incomplete=True)
        else:
            raise FileNotFoundError(
                f"Snapshot not ready at {frozen}; neither finalized SQLite "
                "nor previous .sqlite.incomplete is present. "
                "The original database is unaffected. To make a new "
                "consistent snapshot, explicitly run recover_campaign "
                "with --snapshot-dir first."
            )
    frozen_inv=inspect(frozen)
    if (original/"manifest.json").is_file() and (
        original/"outcomes.sqlite"
    ).is_file():
        source_inv=inspect(original)
        if (source_inv["original_manifest_sha256"]!=
            frozen_inv["original_manifest_sha256"]):
            raise RuntimeError("Manifest mismatch: frozen copy is NOT this campaign.")
        if (source_inv["completed_scenario_seed_tasks"]!=
            frozen_inv["completed_scenario_seed_tasks"]):
            raise RuntimeError("Original and frozen scenario/seed counts differ.")
    if frozen_inv["completed_scenario_seed_tasks"]<=0:
        raise ValueError("No frozen completed replications to analyze.")
    report_dir=frozen/"reports"/"frozen_compact"
    print("Snapshot verified: "
          f"{frozen_inv['completed_scenario_seed_tasks']:,} completed "
          "scenario/seed replications, "
          f"{frozen_inv['saved_method_rows_from_atomic_completed']:,} "
          "historical method rows. Analysis only.",flush=True)
    result=analyze(frozen,report_dir=report_dir)
    figures=plot(report_dir)
    print(
        "\nDONE: frozen analysis completed, NO simulations executed.\n"
        f"Report: {report_dir/'REPORT_BRIEF.md'}\n"
        f"Summary CSVs and figures: {report_dir}\n"
        f"Figures: {', '.join(figures)}",
        flush=True,
    )
    return result


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--original",required=True,type=Path)
    p.add_argument("--frozen",required=True,type=Path)
    p.add_argument("--analyze-only",action="store_true")
    args=p.parse_args(argv)
    finalize(args.original,args.frozen,analyze_only=args.analyze_only)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
