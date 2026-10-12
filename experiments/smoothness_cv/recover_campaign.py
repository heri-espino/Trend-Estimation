"""Inspect and freeze an interrupted Monte Carlo campaign WITHOUT running simulations.

Usage from repository root:
    python -m experiments.smoothness_cv.recover_campaign \
      --run-dir results/smoothness_cv/joint_formal_8h_v1 \
      --snapshot-dir results/smoothness_cv/joint_formal_8h_v1_FROZEN

Reads old manifest and SQLite using mode=ro. If --snapshot-dir is supplied,
uses SQLite's online BACKUP API for a consistent frozen copy, including any
committed WAL transactions; never use shutil.copy on a live WAL database.

No imports from the simulation runner, no CUDA initialization, no changes to
the original database/manifest, and NO generation of new observations.
Reports exactly the completed task count, scenario coverage and checks
for stored optional Paper 3 and baseline tables.
"""
from __future__ import annotations

import argparse
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import sys
import time


CORE_TABLES = ("completed", "outcomes", "failures")
OPTIONAL_TABLES = ("numerical_diagnostics", "numerical_failures", "forecast_baselines")


def ro_connect(db: Path) -> sqlite3.Connection:
    """Open the existing database strictly READ ONLY; never create it."""
    db = Path(db).resolve()
    if not db.is_file():
        raise FileNotFoundError(f"Existing Monte Carlo database not found: {db}")
    connection = sqlite3.connect(db.as_uri() + "?mode=ro", uri=True, timeout=120)
    connection.execute("PRAGMA query_only=ON")
    connection.execute("PRAGMA busy_timeout=120000")
    return connection


def manifest_and_db(run_dir: Path) -> tuple[dict, Path]:
    path = Path(run_dir) / "manifest.json"
    db = Path(run_dir) / "outcomes.sqlite"
    missing = [str(p) for p in (path, db) if not p.is_file()]
    if missing:
        raise FileNotFoundError(
            "Missing campaign artifact(s): " + ", ".join(missing)
            + ". This tool does not create or re-run simulations."
        )
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if "configuration" not in manifest:
        raise ValueError(f"Unrecognized campaign manifest: {path}")
    return manifest, db


def inspect(run_dir: Path) -> dict:
    """Fast read-only evidence inventory. No heavy outcomes-table scan."""
    run_dir = Path(run_dir)
    manifest, database = manifest_and_db(run_dir)
    cfg = manifest["configuration"]
    expected = len(cfg.get("scenario_keys", [])) * int(cfg.get("seeds", 0))
    with closing(ro_connect(database)) as conn:
        tables = {
            row[0] for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        }
        missing = set(CORE_TABLES) - tables
        if missing:
            raise ValueError(f"Original database lacks core tables: {sorted(missing)}")
        finished = int(conn.execute("SELECT COUNT(*) FROM completed").fetchone()[0])
        failed = int(conn.execute("SELECT COUNT(*) FROM failures").fetchone()[0])
        # n_rows is recorded atomically with each completed replication.
        # Reading SUM(n_rows) avoids a long COUNT(*) scan over tens of
        # millions of WITHOUT ROWID outcome records.
        saved_method_rows = int(conn.execute(
            "SELECT COALESCE(SUM(n_rows),0) FROM completed"
        ).fetchone()[0])
        # There can be an interrupted (uncommitted) task at power loss,
        # but it is NOT counted as completed or evidence.
        study_rows = [
            dict(study=str(study), completed=int(count))
            for study, count in conn.execute(
                "SELECT substr(task_key,1,1),COUNT(*) FROM completed "
                "GROUP BY substr(task_key,1,1) ORDER BY 1"
            )
        ]
        per_scenario = [
            dict(scenario=str(scenario), completed=int(count))
            for scenario, count in conn.execute(
                "SELECT substr(task_key,1,instr(task_key,'__seed')-1),COUNT(*) "
                "FROM completed GROUP BY substr(task_key,1,instr(task_key,'__seed')-1) "
                "ORDER BY 1"
            )
        ]
        extra = {
            name: (
                int(conn.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0])
                if name in tables else None
            )
            for name in OPTIONAL_TABLES
        }
        # This validates that table names can be read without running
        # PRAGMA journal_mode=wal or any write-capable setup.
        row = conn.execute(
            "SELECT MIN(completed_utc),MAX(completed_utc) FROM completed"
        ).fetchone()
    sizes = {
        name: (run_dir / name).stat().st_size
        if (run_dir / name).is_file() else 0
        for name in ("outcomes.sqlite", "outcomes.sqlite-wal", "outcomes.sqlite-shm")
    }
    original_manifest_bytes = (run_dir / "manifest.json").read_bytes()
    return {
        # Keep paths portable and avoid publishing local Windows usernames
        # if this small inventory is later committed to a public repository.
        "source_dir": (
            str(run_dir.resolve().relative_to(Path.cwd().resolve())).replace("\\", "/")
            if run_dir.resolve().is_relative_to(Path.cwd().resolve())
            else run_dir.name
        ),
        "inspection_utc": datetime.now(timezone.utc).isoformat(),
        "original_manifest_sha256": hashlib.sha256(original_manifest_bytes).hexdigest(),
        "original_fingerprint": manifest.get("fingerprint"),
        "original_git_revision": cfg.get("git_revision"),
        "preset": cfg.get("preset"),
        "backend": cfg.get("backend"),
        "scenario_cells_declared": len(cfg.get("scenario_keys", [])),
        "seeds_per_cell_declared": cfg.get("seeds"),
        "expected_scenario_seed_tasks": expected,
        "completed_scenario_seed_tasks": finished,
        "not_completed_or_unconfirmed": max(0, expected - finished),
        "logged_failures": failed,
        "saved_method_rows_from_atomic_completed": saved_method_rows,
        "completed_scenario_cells": len(per_scenario),
        "min_completed_seeds_per_present_cell": min(
            (r["completed"] for r in per_scenario), default=0
        ),
        "max_completed_seeds_per_present_cell": max(
            (r["completed"] for r in per_scenario), default=0
        ),
        "study_completion": study_rows,
        "scenario_completion": per_scenario,
        "optional_tables": extra,
        "database_and_wal_bytes": sizes,
        "had_status_file": (run_dir / "run_status.json").is_file(),
        "scientific_status": (
            "partial_exploratory_frozen" if finished < expected
            else "tasks_complete_pending_scientific_audit"
        ),
        "no_new_simulations_executed": True,
    }


def _consistent_sqlite_backup(original: Path, target: Path) -> None:
    if target.exists():
        raise FileExistsError(f"Snapshot already exists; never overwrite: {target}")
    source_db = Path(original)
    wal_bytes = Path(str(source_db) + "-wal").stat().st_size if Path(
        str(source_db) + "-wal"
    ).is_file() else 0
    expected = source_db.stat().st_size + wal_bytes
    free = shutil.disk_usage(target.parent).free
    if free < int(expected * 1.10) + 100 * 1024 * 1024:
        raise OSError(
            f"Not enough free disk space for a safe SQLite snapshot: "
            f"available={free/2**30:.2f} GiB, "
            f"source+WAL={expected/2**30:.2f} GiB. "
            "Choose a --snapshot-dir on another drive. Original is intact."
        )
    tmp = target.with_suffix(".sqlite.incomplete")
    if tmp.exists():
        raise FileExistsError(
            f"An incomplete backup already exists: {tmp}. "
            "Inspect it manually before retrying; no files are removed."
        )
    print(
        f"Creating consistent SQLite snapshot, source+WAL ~{expected/2**30:.2f} GiB. "
        "This can take time for large simulations; source remains unchanged.",
        flush=True,
    )
    start = time.monotonic()
    last_progress = start
    try:
        # sqlite3.Connection.__exit__ commits/rolls back but DOES NOT
        # CLOSE the connection. Windows disallows os.replace() while the
        # destination SQLite file handle remains open, so always use
        # contextlib.closing around BOTH connections.
        with closing(ro_connect(source_db)) as original_conn:
            with closing(sqlite3.connect(str(tmp), timeout=120)) as target_conn:
                def progress(_status, remaining, total):
                    nonlocal last_progress
                    if time.monotonic() - last_progress > 12:
                        done = 100 * (1 - remaining / max(1,total))
                        print(
                            f"SQLite snapshot: {done:.1f}% "
                            f"({(time.monotonic()-start)/60:.1f} min)",
                            flush=True,
                        )
                        last_progress = time.monotonic()
                original_conn.backup(target_conn, pages=512, progress=progress, sleep=.2)
                target_conn.commit()
        os.replace(tmp, target)
        print(f"Snapshot complete: {target}", flush=True)
    except Exception:
        print(
            "Snapshot failed. The source database has NOT been modified. "
            f"An incomplete copy may remain at {tmp}.", file=sys.stderr, flush=True
        )
        raise


def _verify_candidate_snapshot(database: Path, inventory: dict) -> None:
    """Check an already-copied SQLite backup before trusting/promoting it.

    A user might have successfully copied 31 GiB but encountered WinError 32
    during the final rename on Windows, leaving outcomes.sqlite.incomplete.
    Do not trigger another 31 GiB copy. Never call a partial file recovered.
    """
    with closing(ro_connect(database)) as conn:
        integrity = conn.execute("PRAGMA quick_check(1)").fetchone()
        if not integrity or integrity[0] != "ok":
            raise RuntimeError(
                f"Existing candidate SQLite file failed quick_check: "
                f"{database}: {integrity}. Keep the original untouched."
            )
        necessary = set(CORE_TABLES)
        present = {
            row[0] for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        }
        if not necessary.issubset(present):
            raise RuntimeError(
                f"Snapshot missing required tables: {sorted(necessary-present)}"
            )
        expected_count = inventory["completed_scenario_seed_tasks"]
        count = int(conn.execute("SELECT COUNT(*) FROM completed").fetchone()[0])
        recorded_rows = int(conn.execute(
            "SELECT COALESCE(SUM(n_rows),0) FROM completed"
        ).fetchone()[0])
        if count != expected_count or recorded_rows != inventory[
            "saved_method_rows_from_atomic_completed"
        ]:
            raise RuntimeError(
                "Snapshot does NOT match old committed-work inventory. "
                f"Tasks source={expected_count} candidate={count}; "
                f"method rows source={inventory['saved_method_rows_from_atomic_completed']} "
                f"candidate={recorded_rows}. "
                "It may be an interrupted/incomplete copy; do not rename it."
            )
        for tablename, expected in inventory["optional_tables"].items():
            if expected is None:
                if tablename in present:
                    raise RuntimeError(
                        f"Snapshot has unexpected extra table {tablename}."
                    )
            else:
                if tablename not in present:
                    raise RuntimeError(
                        f"Snapshot missing optional table {tablename}."
                    )
                actual = int(conn.execute(
                    f"SELECT COUNT(*) FROM {tablename}"
                ).fetchone()[0])
                if actual != expected:
                    raise RuntimeError(
                        f"Snapshot {tablename} count differs: "
                        f"source={expected}, candidate={actual}"
                    )


def _finalize_prior_copy(
    source: Path, snapshot_dir: Path, inventory: dict
) -> Path:
    """Promote a validated old .incomplete backup WITHOUT recopying source.

    Only use after the previous backup PROCESS HAS EXITED. No process should
    be writing to outcomes.sqlite.incomplete during this action.
    """
    source, snapshot_dir = Path(source).resolve(), Path(snapshot_dir).resolve()
    if source == snapshot_dir or source in snapshot_dir.parents:
        raise ValueError("Snapshot directory must be OUTSIDE source run directory.")
    target = snapshot_dir / "outcomes.sqlite"
    pending = target.with_suffix(".sqlite.incomplete")
    if target.exists():
        raise FileExistsError(
            f"A finalized snapshot already exists: {target}. "
            "Do not overwrite it; analyze that existing snapshot."
        )
    if not pending.is_file():
        raise FileNotFoundError(
            f"No previous SQLite copy found at {pending}. "
            "Use --snapshot-dir WITHOUT --finalize-incomplete to create it."
        )
    print(
        f"VALIDATING existing {pending.stat().st_size/2**30:.2f} GiB "
        "SQLite backup WITHOUT copying new data. This may take several minutes.",
        flush=True,
    )
    _verify_candidate_snapshot(pending, inventory)
    # All SQLite handles from quick_check and count comparison are now closed
    # before Windows os.replace.
    os.replace(pending, target)
    print(f"Old backup validated and finalized: {target}", flush=True)
    return target


def freeze(
    source: Path, snapshot_dir: Path, inventory: dict, *,
    finalize_incomplete: bool = False
) -> Path:
    source, snapshot_dir = Path(source).resolve(), Path(snapshot_dir).resolve()
    if source == snapshot_dir or source in snapshot_dir.parents:
        raise ValueError("Snapshot directory must be OUTSIDE the source run directory.")
    # A small manifest-only inventory can always be done without a disk copy:
    # snapshot_dir is explicitly opt-in, and no prior snapshot is overwritten.
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    target = snapshot_dir / "outcomes.sqlite"
    if finalize_incomplete:
        _finalize_prior_copy(source, snapshot_dir, inventory)
    else:
        _consistent_sqlite_backup(source / "outcomes.sqlite", target)
    for name in ("manifest.json", "run_status.json", "sturm_exact_reference.txt"):
        raw = source / name
        if raw.is_file():
            dest = snapshot_dir / name
            if dest.exists():
                raise FileExistsError(f"Snapshot metadata already exists: {dest}")
            shutil.copy2(raw, dest)
    report = snapshot_dir / "recovery_inventory.json"
    report.write_text(json.dumps(inventory, indent=2, ensure_ascii=False),
                      encoding="utf-8")
    # Confirm the backup itself contains the same atomic completed tasks.
    with closing(ro_connect(target)) as db:
        frozen_count = int(db.execute(
            "SELECT COUNT(*) FROM completed"
        ).fetchone()[0])
    if frozen_count != inventory["completed_scenario_seed_tasks"]:
        raise RuntimeError(
            "Snapshot count mismatch. Do not treat it as a verified freeze. "
            f"Source={inventory['completed_scenario_seed_tasks']} "
            f"snapshot={frozen_count}."
        )
    return snapshot_dir


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run-dir", type=Path, required=True)
    p.add_argument(
        "--snapshot-dir", type=Path, default=None,
        help="Create separate consistent copy using SQLite backup, NEVER overwrite.",
    )
    p.add_argument(
        "--finalize-incomplete", action="store_true",
        help="Validate and promote an existing 31-GiB .sqlite.incomplete "
             "from the prior Windows rename failure; NO NEW DB COPY. "
             "ONLY use once the previous backup process has exited."
    )
    args = p.parse_args(argv)
    if args.finalize_incomplete and args.snapshot_dir is None:
        p.error("--finalize-incomplete requires --snapshot-dir")
    inventory = inspect(args.run_dir)
    headline = {key:inventory[key] for key in (
        "source_dir", "original_git_revision", "scenario_cells_declared",
        "expected_scenario_seed_tasks", "completed_scenario_seed_tasks",
        "not_completed_or_unconfirmed", "logged_failures",
        "saved_method_rows_from_atomic_completed",
        "completed_scenario_cells", "min_completed_seeds_per_present_cell",
        "max_completed_seeds_per_present_cell", "study_completion",
        "optional_tables", "database_and_wal_bytes", "scientific_status",
    )}
    print(json.dumps(headline, indent=2, ensure_ascii=False),flush=True)
    if args.snapshot_dir:
        frozen = freeze(
            args.run_dir, args.snapshot_dir, inventory,
            finalize_incomplete=args.finalize_incomplete,
        )
        print(f"RECOVERED, FROZEN, NO NEW SIMULATIONS: {frozen}",flush=True)
        print(
            "For reports later: python -m "
            "experiments.smoothness_cv.analyze_joint_campaign "
            f"--run-dir \"{frozen}\" --allow-partial",flush=True,
        )
    else:
        print(
            "Inventory only: database/manifest are intact. Add --snapshot-dir "
            "to create a safe SQLite copy before running analysis.",flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
