"""Safely commit/push ONLY small frozen Monte Carlo REPORTS, never SQLite.

  python -m experiments.smoothness_cv.publish_frozen_review --report-dir \
      results/smoothness_cv/joint_formal_8h_v1_FROZEN/reports/frozen_compact --push

Requires an already completed analysis and normal Git credentials.
Refuses other staged changes, unknown branch, large files, or hidden DBs.
Does NOT execute any simulation, re-analyze results, or initialize CUDA.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess


EXPECTED=(
    "ANALYSIS_MANIFEST.json",
    "REPORT_BRIEF.md",
    "README_RESULTS.md",
    "README_FIGURES.md",
    "coverage_by_scenario.csv",
    "paper1_forecast_cv_vs_classical.csv",
    "paper2_tracking_vs_matched_pooled.csv",
    "paper3_numerical_summary_compact.csv",
)
GRAPH_STEMS=(
    "paper1_classical_relative_rmse",
    "paper2_matched_tracking_relative_rmse",
    "paper3_numerical_regret",
    "coverage_independent_seeds",
)
MAX_FILE=16*1024**2
MAX_TOTAL=32*1024**2


def review_paths(report_dir:Path, repo_root:Path) -> list[str]:
    report_dir=Path(report_dir).resolve()
    repo_root=Path(repo_root).resolve()
    if not report_dir.is_relative_to(repo_root):
        raise ValueError("Review folder must be inside the current Git checkout.")
    manifest=report_dir/"ANALYSIS_MANIFEST.json"
    if not manifest.is_file():
        raise FileNotFoundError("No completed frozen review manifest. Analyze first.")
    obj=json.loads(manifest.read_text(encoding="utf-8"))
    if obj.get("simulation_tasks_executed")!=0 or (
        obj.get("status")!="PARTIAL — EXPLORATORY, nonconfirmatory"
    ):
        raise ValueError("Refusing publication without verified frozen provenance.")
    paths=[
        *(report_dir/name for name in EXPECTED),
        *(report_dir/(stem+ext) for stem in GRAPH_STEMS for ext in (".pdf",".png")),
    ]
    missing=[str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            "Expected comparison/figure files missing: "+", ".join(missing)
        )
    total=0
    selected=[]
    for path in paths:
        if path.is_symlink() or not path.resolve().is_relative_to(report_dir):
            raise ValueError(f"Unsafe symlink/link path: {path}")
        size=path.stat().st_size
        if size>=MAX_FILE:
            raise ValueError(f"Review file too large for small Git commit: {path}")
        total+=size
        selected.append(path.relative_to(repo_root).as_posix())
    if total>MAX_TOTAL:
        raise ValueError(
            f"Review bundle {total/2**20:.1f} MiB exceeds {MAX_TOTAL/2**20:.1f} "
            "MiB. Archive larger data externally rather than Git."
        )
    print(
        f"Curated review: {len(selected)} files / {total/2**20:.2f} MiB. "
        "NO raw SQLite, no unaggregated forecast rows.",flush=True
    )
    return selected


def run_git(args,*,cwd):
    return subprocess.run(
        ["git",*args],cwd=cwd,
        capture_output=True,text=True,encoding="utf-8",
        errors="replace",
    )


def publish(report_dir:Path, *, push:bool=False, root:Path|None=None):
    if root is None:
        root=Path(__file__).resolve().parents[2]
    root=Path(root).resolve()
    paths=review_paths(report_dir,root)
    # Refuse to commit unrelated staged work.
    branch=run_git(["branch","--show-current"],cwd=root)
    if branch.returncode or branch.stdout.strip()!="main":
        raise RuntimeError("Please use the 'main' branch before publishing.")
    staged=run_git(["diff","--cached","--name-only"],cwd=root)
    if staged.returncode:
        raise RuntimeError(staged.stderr)
    if staged.stdout.strip():
        raise RuntimeError(
            "There are already staged changes; refusing to include "
            "unrelated files in the results commit. Unstage/review first."
        )
    add=run_git(["add","--",*paths],cwd=root)
    if add.returncode:
        raise RuntimeError(f"git add failed: {add.stderr}")
    changes=run_git(["diff","--cached","--name-only"],cwd=root)
    if changes.returncode:
        raise RuntimeError(changes.stderr)
    unexpected=set(changes.stdout.splitlines())-set(paths)
    if unexpected:
        raise RuntimeError(f"Unexpected staged paths: {sorted(unexpected)}")
    if not changes.stdout.strip():
        print("Curated review is already committed, no new Git commit.",flush=True)
    else:
        saved=run_git(
            ["commit","-m",
             "results: frozen 100848-task exploratory three-paper review"],
            cwd=root,
        )
        if saved.returncode:
            raise RuntimeError(f"git commit failed: {saved.stderr}\n{saved.stdout}")
        print(saved.stdout,flush=True)
    if push:
        out=run_git(["push","origin","main"],cwd=root)
        if out.returncode:
            raise RuntimeError(f"git push failed: {out.stderr}\n{out.stdout}")
        print("Curated review published to GitHub main.",flush=True)
    else:
        print("Curated review committed locally; use --push to publish.",flush=True)
    return paths


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report-dir",required=True,type=Path)
    p.add_argument("--push",action="store_true",
                   help="Commit small curated files and push main to origin.")
    a=p.parse_args(argv)
    publish(a.report_dir,push=a.push)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
