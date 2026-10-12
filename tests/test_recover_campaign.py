"""Safety: a stopped CUDA campaign can be frozen without running jobs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sqlite3
from contextlib import closing

import pytest

from experiments.smoothness_cv.recover_campaign import (
    freeze, inspect, manifest_and_db, ro_connect,
)


def _sample_run(folder: Path):
    folder.mkdir()
    config={
        "preset":"formal8h","backend":"cuda",
        "scenario_keys":["A__linear__N50","B__quadratic__N180"],
        "seeds":10,"git_revision":"original-locked-commit",
    }
    (folder/"manifest.json").write_text(
        json.dumps({"configuration":config,"fingerprint":"old-fingerprint"}),
        encoding="utf-8",
    )
    path=folder/"outcomes.sqlite"
    connection=sqlite3.connect(str(path))
    connection.execute("PRAGMA journal_mode=WAL")
    connection.executescript("""
    CREATE TABLE completed (
      task_key TEXT PRIMARY KEY,
      n_rows INTEGER NOT NULL,
      elapsed_sec REAL NOT NULL,
      completed_utc TEXT NOT NULL
    );
    CREATE TABLE outcomes (
      task_key TEXT, origin INTEGER, selector TEXT, value REAL
    );
    CREATE TABLE failures (
      task_key TEXT PRIMARY KEY, message TEXT, occurred_utc TEXT
    );
    CREATE TABLE numerical_diagnostics (
      scenario TEXT, payload TEXT
    );
    CREATE TABLE forecast_baselines (
      scenario TEXT, payload TEXT
    );
    """)
    connection.execute(
        "INSERT INTO completed VALUES (?,?,?,?)",
        ("A__linear__N50__seed000000",8,5.2,"2026-10-12T00:00Z")
    )
    connection.execute(
        "INSERT INTO completed VALUES (?,?,?,?)",
        ("B__quadratic__N180__seed000000",10,7.0,"2026-10-12T00:01Z")
    )
    connection.execute(
        "INSERT INTO outcomes VALUES (?,?,?,?)",
        ("A__linear__N50__seed000000",30,"pooled_uniform_all",.5),
    )
    connection.execute(
        "INSERT INTO numerical_diagnostics VALUES (?,?)",
        ("A__linear__N50",'{"numerical":true}')
    )
    connection.commit()
    # Keep source DB connection open so there is a real WAL on disk
    # while the read-only online backup is running.
    return connection


def test_read_only_inventory_and_online_frozen_snapshot_with_live_wal(tmp_path):
    original=tmp_path/"source"
    writer=_sample_run(original)
    try:
        wal=Path(str(original/"outcomes.sqlite")+"-wal")
        assert wal.is_file()
        old_manifest=(original/"manifest.json").read_bytes()
        before=inspect(original)
        assert before["completed_scenario_seed_tasks"]==2
        assert before["saved_method_rows_from_atomic_completed"]==18
        assert before["expected_scenario_seed_tasks"]==20
        assert before["completed_scenario_cells"]==2
        assert before["study_completion"]==[
            {"study":"A","completed":1},{"study":"B","completed":1}
        ]
        assert before["optional_tables"]["numerical_diagnostics"]==1
        assert before["no_new_simulations_executed"]
        with ro_connect(original/"outcomes.sqlite") as read:
            with pytest.raises(sqlite3.OperationalError):
                read.execute("INSERT INTO completed VALUES ('fake',1,1,'now')")
        dest=tmp_path/"frozen"
        assert freeze(original,dest,before)==dest.resolve()
        assert (dest/"outcomes.sqlite").is_file()
        assert (dest/"recovery_inventory.json").is_file()
        assert (dest/"manifest.json").read_bytes()==old_manifest
        with ro_connect(dest/"outcomes.sqlite") as clone:
            assert clone.execute("SELECT COUNT(*) FROM completed").fetchone()[0]==2
            assert clone.execute("SELECT COUNT(*) FROM numerical_diagnostics").fetchone()[0]==1
        assert inspect(original)["completed_scenario_seed_tasks"]==2
        assert (original/"manifest.json").read_bytes()==old_manifest
        with pytest.raises(FileExistsError):
            freeze(original,dest,before)
    finally:
        writer.close()


def test_existing_windows_unrenamed_snapshot_can_be_verified_without_copy(tmp_path):
    source=tmp_path/"source"
    writer=_sample_run(source)
    try:
        before=inspect(source)
        destination=tmp_path/"frozen"
        destination.mkdir()
        pending=destination/"outcomes.sqlite.incomplete"
        # Recreate a successful SQLite online backup that was not renamed,
        # e.g. a Windows WinError 32 from an OPEN destination connection.
        with closing(ro_connect(source/"outcomes.sqlite")) as conn:
            with closing(sqlite3.connect(str(pending))) as dest:
                conn.backup(dest)
        assert pending.is_file()
        assert not (destination/"outcomes.sqlite").exists()
        assert freeze(source,destination,before,finalize_incomplete=True)==destination.resolve()
        assert not pending.exists()
        assert (destination/"outcomes.sqlite").exists()
        with closing(ro_connect(destination/"outcomes.sqlite")) as db:
            assert db.execute("SELECT COUNT(*) FROM completed").fetchone()[0]==2
        with pytest.raises(FileExistsError,match="finalized snapshot"):
            freeze(source,destination,before,finalize_incomplete=True)
    finally:
        writer.close()


def test_truncated_prior_windows_snapshot_is_not_promoted(tmp_path):
    source=tmp_path/"source"
    writer=_sample_run(source)
    try:
        before=inspect(source)
        destination=tmp_path/"frozen"
        destination.mkdir()
        pending=destination/"outcomes.sqlite.incomplete"
        pending.write_bytes(b"not a sqlite database")
        with pytest.raises((sqlite3.DatabaseError,RuntimeError)):
            freeze(source,destination,before,finalize_incomplete=True)
        assert pending.exists()
        assert not (destination/"outcomes.sqlite").exists()
        assert inspect(source)["completed_scenario_seed_tasks"]==2
    finally:
        writer.close()


def test_missing_original_does_not_create_empty_sqlite(tmp_path):
    source=tmp_path/"missing"
    with pytest.raises(FileNotFoundError,match="Missing campaign"):
        manifest_and_db(source)
    assert not source.exists()


def test_freeze_refuses_any_destination_inside_original_run_dir(tmp_path):
    root=tmp_path/"source"
    connection=_sample_run(root)
    try:
        before=inspect(root)
        with pytest.raises(ValueError,match="OUTSIDE"):
            freeze(root,root/"subdirectory",before)
        assert not (root/"subdirectory").exists()
    finally:
        connection.close()
