"""Build the numerical-paper's presentation figures without rerunning experiments.

From repository root, with the trend-estimation environment active:
    python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group all

The benchmark/applied groups READ frozen CSV files. They never write to results/.
The concepts/algorithm groups only draw fixed pedagogical data or replay a tiny
already-documented exact-rational example. Output goes to presentation/figures/.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))

from _style import configure
import figures_concepts
import figures_algorithm
import figures_benchmarks
import figures_applied

GROUPS={
    "concepts":figures_concepts.FIGURES,
    "algorithm":figures_algorithm.FIGURES,
    "benchmarks":figures_benchmarks.FIGURES,
    "applied":figures_applied.FIGURES,
}
FIGURES={key:(group,func) for group,items in GROUPS.items()
         for key,func in items.items()}
if len(FIGURES)!=sum(len(x) for x in GROUPS.values()):
    raise RuntimeError("Duplicate figure IDs across modules.")


def parse_args():
    p=argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--group",choices=("all",*GROUPS),default="all",
                   help="Which family to build (default: all).")
    p.add_argument("--only",nargs="+",metavar="FIGURE_ID",
                   help="Build specific figure IDs (see --list).")
    p.add_argument("--format",choices=("both","pdf","png"),default="both")
    p.add_argument("--output-dir",type=Path,default=HERE/"figures")
    p.add_argument("--list",action="store_true",help="Show figure ID and category.")
    p.add_argument("--dry-run",action="store_true",help="Show planned figures; do not render.")
    return p.parse_args()


def main():
    args=parse_args()
    if args.list:
        for key,(group,_) in FIGURES.items():print(f"{group:11s} {key}")
        return 0
    selected=(
        list(args.only) if args.only
        else list(FIGURES) if args.group=="all" else list(GROUPS[args.group])
    )
    unknown=[x for x in selected if x not in FIGURES]
    if unknown:raise SystemExit("Unknown figure IDs: "+", ".join(unknown))
    if args.dry_run:
        for key in selected:print(f"[{FIGURES[key][0]}] {key}")
        print(f"Planned {len(selected)} figure(s). No data read or modified.")
        return 0
    configure(args.output_dir,args.format)
    print(f"Figure output: {args.output_dir.resolve()}")
    print(f"Selected {len(selected)} figure(s), formats={args.format}.")
    records=[]
    for key in selected:
        group,func=FIGURES[key]
        print(f"[{group}] {key}",flush=True)
        try:
            outputs=func()
        except (OSError,ValueError,RuntimeError,ImportError,TypeError) as err:
            print(f"\nFigure generation stopped at {key}: {err}",file=sys.stderr)
            print("No historical results were changed. "
                  "Use --group concepts or --list to generate a smaller subset.",file=sys.stderr)
            return 1
        records.append({
            "figure":key, "group":group,
            "type":"frozen results" if group in ("benchmarks","applied") else "pedagogical / small exact example",
            "paths":[str(p.resolve()) for p in outputs],
        })
    if records:
        # Keep the report with generated outputs. Never write into results/.
        out=args.output_dir.resolve()
        out.mkdir(parents=True,exist_ok=True)
        index=out/"figure_build_manifest.json"
        report={
            "generated_at_utc":datetime.now(timezone.utc).isoformat(),
            "source":"Working Paper - Numerical Methods / presentation",
            "numerical_studies_rerun":False,
            "frozen_results_overwritten":False,
            "figures":records,
        }
        index.write_text(json.dumps(report,indent=2),encoding="utf-8")
        print(f"Saved manifest: {index}")
    print(f"Generated {len(records)} figure(s).")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
