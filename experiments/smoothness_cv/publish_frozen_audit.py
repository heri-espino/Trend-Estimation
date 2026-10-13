"""Publish only small, completed read-only frozen audit reports to GitHub.

No model training, data generation, Monte Carlo or GPU.
Usage: python -m experiments.smoothness_cv.publish_frozen_audit --audit-dir PATH --push
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from .publish_frozen_review import run_git

FILES=(
    "AUDIT_MANIFEST.json",
    "AUDIT_OVERVIEW.md",
    "PAPER1_AUDIT.md",
    "PAPER2_AUDIT.md",
    "PAPER3_AUDIT.md",
    "comparison_tests.csv",
    "group_heterogeneity.csv",
    "extreme_cases.csv",
    "smoothing_edf_diagnostics.csv",
    "numerical_paired_summary.csv",
)


def publish(audit_dir:Path,*,push:bool,root:Path|None=None):
    root=(root or Path(__file__).resolve().parents[2]).resolve()
    audit_dir=Path(audit_dir).resolve()
    if not audit_dir.is_relative_to(root):
        raise ValueError("Audit directory must be inside Git checkout")
    manifest=audit_dir/"AUDIT_MANIFEST.json"
    if not manifest.is_file():
        raise FileNotFoundError(f"Audit manifest not found: {manifest}")
    meta=json.loads(manifest.read_text(encoding="utf-8"))
    if (meta.get("status")!="RETROSPECTIVE_EXPLORATORY_AUDIT"
        or meta.get("no_new_simulations") is not True
        or meta.get("source_original_git_revision")!=
           "21bd563146e04eb545cae56b46393d93a9d98212"):
        raise ValueError("Cannot publish unverifiable historical audit")
    paths=[audit_dir/name for name in FILES]
    missing=[p.name for p in paths if not p.is_file()]
    if missing:
        raise FileNotFoundError("Audit files missing: "+", ".join(missing))
    sizes=[p.stat().st_size for p in paths]
    if any(p.is_symlink() for p in paths):
        raise ValueError("Refusing symlink file")
    if max(sizes)>=16*1024**2 or sum(sizes)>=32*1024**2:
        raise ValueError("Audit outputs too large for a small Git review")
    names=[p.relative_to(root).as_posix() for p in paths]
    branch=run_git(["branch","--show-current"],cwd=root)
    if branch.returncode or branch.stdout.strip()!="main":
        raise RuntimeError("Expected Git branch main")
    staged=run_git(["diff","--cached","--name-only"],cwd=root)
    if staged.returncode or staged.stdout.strip():
        raise RuntimeError("Refusing to mix with other staged Git files")
    added=run_git(["add","--",*names],cwd=root)
    if added.returncode:
        raise RuntimeError(added.stderr)
    changes=run_git(["diff","--cached","--name-only"],cwd=root)
    if changes.returncode or set(changes.stdout.splitlines())-set(names):
        raise RuntimeError("Unexpected Git staged paths")
    if changes.stdout.strip():
        committed=run_git(
            ["commit","-m","audit: frozen original P1/P2/P3 Monte Carlo review"],
            cwd=root,
        )
        if committed.returncode:
            raise RuntimeError(committed.stderr+"\n"+committed.stdout)
        print(committed.stdout,flush=True)
    if push:
        pushed=run_git(["push","origin","main"],cwd=root)
        if pushed.returncode:
            raise RuntimeError(pushed.stderr+"\n"+pushed.stdout)
        print("Curated audit reports pushed to GitHub.",flush=True)
    return names


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-dir",type=Path,required=True)
    parser.add_argument("--push",action="store_true")
    a=parser.parse_args(argv)
    publish(a.audit_dir,push=a.push)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
