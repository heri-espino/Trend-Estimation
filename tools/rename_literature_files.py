#!/usr/bin/env python3
"""Rename literature files and repair exact references across the repository.

The default mode is a dry run. Use ``--apply`` to perform the migration and
``--check`` to verify that no old names or broken front-matter paths remain.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import re
import subprocess
import sys
from uuid import uuid4


OLD_CORE_PATTERN = re.compile(r"_\d{4}_")
MANAGED_SUFFIXES = {
    "pdf": ".pdf",
    "extracted": ".md",
    "references": ".references.md",
}
SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".superpowers",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "venv",
}
SKIP_FILES = {
    Path("tools/rename_literature_files.py"),
    Path("tests/test_rename_literature_files.py"),
}
SKIP_PREFIXES = (Path("docs/superpowers"),)
BINARY_SUFFIXES = {
    ".7z",
    ".doc",
    ".docx",
    ".eot",
    ".gif",
    ".gz",
    ".ico",
    ".jpeg",
    ".jpg",
    ".otf",
    ".pdf",
    ".png",
    ".pyc",
    ".tar",
    ".ttf",
    ".woff",
    ".woff2",
    ".xlsx",
    ".zip",
}
FRONT_MATTER_PATH_PATTERN = re.compile(
    r'^\s*(?:source_pdf|references_file):\s*["\']([^"\']+)["\']\s*$',
    re.MULTILINE,
)


class MigrationError(RuntimeError):
    """Raised when a migration plan cannot be applied safely."""


@dataclass(frozen=True)
class RenameOperation:
    source: Path
    target: Path


@dataclass(frozen=True)
class TextEdit:
    path: Path
    content: bytes


@dataclass(frozen=True)
class MigrationPlan:
    repo_root: Path
    renames: tuple[RenameOperation, ...]
    text_edits: tuple[TextEdit, ...]
    core_map: dict[str, str]


def swap_core(core: str) -> str:
    """Swap hyphens and underscores simultaneously in a literature core."""

    return core.translate(str.maketrans({"-": "_", "_": "-"}))


def split_managed_name(path: Path, kind: str) -> tuple[str, str] | None:
    """Return an old-format core and preserved suffix for a managed file."""

    try:
        suffix = MANAGED_SUFFIXES[kind]
    except KeyError as exc:
        raise ValueError(f"Unknown literature kind: {kind}") from exc
    if not path.name.endswith(suffix):
        return None
    core = path.name[: -len(suffix)]
    if not OLD_CORE_PATTERN.search(core):
        return None
    return core, suffix


def build_core_map(literature_dir: Path) -> dict[str, str]:
    """Discover every old-format literature core below the managed folders."""

    missing = [name for name in MANAGED_SUFFIXES if not (literature_dir / name).is_dir()]
    if missing:
        raise MigrationError(
            "Missing managed literature directories: " + ", ".join(sorted(missing))
        )

    mapping: dict[str, str] = {}
    for kind in MANAGED_SUFFIXES:
        for path in sorted((literature_dir / kind).iterdir()):
            if not path.is_file() or path.name.startswith(".rename-literature-"):
                continue
            parsed = split_managed_name(path, kind)
            if parsed is None:
                continue
            core, _ = parsed
            new_core = swap_core(core)
            previous = mapping.setdefault(core, new_core)
            if previous != new_core:
                raise MigrationError(f"Inconsistent mapping for {core!r}")
    return mapping


def replacement_pairs(core_map: dict[str, str]) -> list[tuple[str, str]]:
    """Return replacement pairs longest-first to protect related prefixes."""

    return sorted(core_map.items(), key=lambda item: len(item[0]), reverse=True)


def _repo_text_candidates(repo_root: Path) -> list[Path]:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo_root), "ls-files", "-co", "--exclude-standard", "-z"],
            check=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError):
        candidates: list[Path] = []
        for current, dirs, files in os.walk(repo_root):
            dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
            candidates.extend(Path(current) / name for name in files)
        return candidates

    return [
        repo_root / Path(raw.decode("utf-8"))
        for raw in completed.stdout.split(b"\0")
        if raw
    ]


def _is_skipped_text_path(path: Path, repo_root: Path) -> bool:
    try:
        relative = path.relative_to(repo_root)
    except ValueError:
        return True
    if relative in SKIP_FILES:
        return True
    if any(relative == prefix or prefix in relative.parents for prefix in SKIP_PREFIXES):
        return True
    if any(part in SKIP_DIRS for part in relative.parts[:-1]):
        return True
    return path.suffix.lower() in BINARY_SUFFIXES


def plan_migration(repo_root: Path) -> MigrationPlan:
    """Build and validate a complete migration plan without changing files."""

    repo_root = repo_root.resolve()
    literature_dir = repo_root / "literature"
    core_map = build_core_map(literature_dir)
    pairs = replacement_pairs(core_map)

    renames: list[RenameOperation] = []
    for kind, suffix in MANAGED_SUFFIXES.items():
        directory = literature_dir / kind
        for source in sorted(directory.iterdir()):
            if not source.is_file():
                continue
            parsed = split_managed_name(source, kind)
            if parsed is None:
                continue
            core, _ = parsed
            renames.append(RenameOperation(source, directory / f"{core_map[core]}{suffix}"))

    sources = {operation.source for operation in renames}
    targets: set[Path] = set()
    for operation in renames:
        if operation.target in targets:
            raise MigrationError(f"Multiple files map to {operation.target}")
        targets.add(operation.target)
        if operation.target.exists() and operation.target not in sources:
            raise MigrationError(f"Target already exists: {operation.target}")

    renamed_text_paths = {
        operation.source: operation.target
        for operation in renames
        if operation.source.suffix.lower() not in BINARY_SUFFIXES
    }
    text_edits: list[TextEdit] = []
    encoded_old = [old.encode("utf-8") for old, _ in pairs]
    for path in sorted(set(_repo_text_candidates(repo_root))):
        if not path.is_file() or _is_skipped_text_path(path, repo_root):
            continue
        data = path.read_bytes()
        if not any(old in data for old in encoded_old):
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        updated = text
        for old, new in pairs:
            updated = updated.replace(old, new)
        if updated != text:
            text_edits.append(
                TextEdit(renamed_text_paths.get(path, path), updated.encode("utf-8"))
            )

    return MigrationPlan(repo_root, tuple(renames), tuple(text_edits), core_map)


def apply_plan(plan: MigrationPlan) -> None:
    """Apply a validated plan using collision-safe two-phase renames."""

    temporary: list[tuple[Path, Path]] = []
    for operation in plan.renames:
        if not operation.source.exists():
            raise MigrationError(f"Source disappeared before apply: {operation.source}")
        temp = operation.source.with_name(f".rename-literature-{uuid4().hex}")
        operation.source.rename(temp)
        temporary.append((temp, operation.target))

    for temp, target in temporary:
        temp.rename(target)

    for edit in plan.text_edits:
        if not edit.path.exists():
            raise MigrationError(f"Text target missing after rename: {edit.path}")
        temp = edit.path.with_name(f".rename-literature-{uuid4().hex}")
        temp.write_bytes(edit.content)
        os.replace(temp, edit.path)


def validate_references(repo_root: Path) -> list[str]:
    """Return corpus naming and front-matter path problems."""

    repo_root = repo_root.resolve()
    literature = repo_root / "literature"
    problems: list[str] = []
    for kind in MANAGED_SUFFIXES:
        directory = literature / kind
        if not directory.is_dir():
            problems.append(f"Missing directory: {directory}")
            continue
        for path in directory.iterdir():
            if path.is_file() and split_managed_name(path, kind) is not None:
                problems.append(f"Old-format filename remains: {path.relative_to(repo_root)}")

    for subdir in ("extracted", "references"):
        directory = literature / subdir
        if not directory.is_dir():
            continue
        for path in directory.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            front_matter = text.split("---", 2)[1] if text.startswith("---") else ""
            for relative in FRONT_MATTER_PATH_PATTERN.findall(front_matter):
                target = (path.parent / relative).resolve()
                if not target.exists():
                    problems.append(
                        f"Broken metadata path in {path.relative_to(repo_root)}: {relative}"
                    )
    return problems


def _print_plan(plan: MigrationPlan) -> None:
    print(f"Planned renames: {len(plan.renames)}")
    print(f"Planned text updates: {len(plan.text_edits)}")
    for operation in plan.renames:
        print(
            f"  {operation.source.relative_to(plan.repo_root)}"
            f" -> {operation.target.relative_to(plan.repo_root)}"
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="apply the validated plan")
    parser.add_argument("--check", action="store_true", help="validate the migrated corpus")
    parser.add_argument("--repo-root", type=Path, help="repository root (mainly for testing)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = (args.repo_root or Path(__file__).resolve().parents[1]).resolve()
    if args.check:
        problems = validate_references(repo_root)
        if problems:
            for problem in problems:
                print(problem, file=sys.stderr)
            return 1
        print("Literature filename and metadata checks passed")
        return 0

    plan = plan_migration(repo_root)
    _print_plan(plan)
    if args.apply:
        apply_plan(plan)
        print("Literature migration applied")
    else:
        print("Dry run only; use --apply to make changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
