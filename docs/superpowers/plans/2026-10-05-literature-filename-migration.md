# Literature Filename Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and apply an idempotent CLI that migrates the literature corpus to the literal delimiter-swapped filename convention and repairs exact references across the repository.

**Architecture:** A single standard-library Python module separates pure filename mapping, migration planning, validation, and application. It discovers old-format cores using `_YYYY_`, prepares all text edits before mutation, performs two-phase renames, and exposes dry-run and `--apply` modes.

**Tech Stack:** Python 3.10+, `argparse`, `dataclasses`, `pathlib`, `tempfile`, `os.replace`, `pytest`.

**Spec:** `docs/superpowers/specs/2026-10-05-literature-filename-migration-design.md`

## Global Constraints

- Translate `_` to `-` and `-` to `_` simultaneously within old-format literature cores.
- Recognize old names only through the `_YYYY_` marker; never reverse names already using `-YYYY-`.
- Preserve file extensions and the technical `.references.md` suffix.
- Update only exact old core occurrences; do not rewrite ordinary prose punctuation or BibTeX keys.
- Validate the complete plan before writes and use two-phase filesystem renames.
- Use only the Python standard library in the production tool.
- Default to dry-run; require `--apply` for mutation.

## Review Focus

- Related paper and appendix names must use longest-first replacement without partial corruption; Task 1 tests this ordering.
- A pre-existing destination or two-to-one mapping must abort before mutation; Task 2 tests both failure modes.
- Binary and non-UTF-8 files outside the managed rename set must be skipped safely; Task 2 tests binary skipping.
- Interrupted-looking temporary names must never be treated as source literature; Task 2 tests discovery exclusions.
- A second run after application must plan zero renames and zero edits; Task 2 tests end-to-end idempotence.

---

### Task 1: Pure naming and replacement planning

**Files:**
- Create: `tools/rename_literature_files.py`
- Create: `tests/test_rename_literature_files.py`

**Interfaces:**
- Produces: `swap_core(core: str) -> str`
- Produces: `split_managed_name(path: Path, kind: str) -> tuple[str, str] | None`
- Produces: `build_core_map(literature_dir: Path) -> dict[str, str]`
- Produces: `replacement_pairs(core_map: dict[str, str]) -> list[tuple[str, str]]`

- [ ] **Step 1: Write failing tests for simultaneous translation and suffix preservation**

  Assert that `Baxter_1999_approximate-band-pass-filters` maps to
  `Baxter-1999-approximate_band_pass_filters`, the Islas-Camargo example maps
  exactly as specified, new-format names are not migratable, and
  `.references.md` is kept outside the translated core.

- [ ] **Step 2: Run the focused tests and verify they fail because the module does not exist**

  Run: `pytest tests/test_rename_literature_files.py -q`
  Expected: collection/import failure for `tools.rename_literature_files`.

- [ ] **Step 3: Implement the pure naming interfaces**

  Use a compiled `_\d{4}_` recognition pattern and `str.translate` for the
  simultaneous swap. Discover cores from the three managed directories and
  return replacement pairs sorted by descending old-core length.

- [ ] **Step 4: Add and run tests for consistent cross-directory maps and appendix-first ordering**

  Expected: all Task 1 tests pass.

- [ ] **Step 5: Commit Task 1**

  Commit only the tool skeleton and focused tests with message
  `Add literature filename mapping primitives`.

### Task 2: Safe migration planning, application, and CLI

**Files:**
- Modify: `tools/rename_literature_files.py`
- Modify: `tests/test_rename_literature_files.py`

**Interfaces:**
- Consumes: Task 1 mapping functions.
- Produces: immutable `RenameOperation`, `TextEdit`, and `MigrationPlan` dataclasses.
- Produces: `plan_migration(repo_root: Path) -> MigrationPlan`
- Produces: `apply_plan(plan: MigrationPlan) -> None`
- Produces: `validate_references(repo_root: Path) -> list[str]`
- Produces: `main(argv: list[str] | None = None) -> int`

- [ ] **Step 1: Write failing fixture tests for dry-run planning and repository-wide metadata/path edits**

  Create temporary `literature/pdf`, `extracted`, and `references` trees plus
  an external Markdown note. Assert the plan includes three renames, updates
  `id`, `source_pdf`, `source_filename`, `references_file`, and the external
  note, while leaving ordinary prose hyphens unchanged.

- [ ] **Step 2: Implement immutable plan dataclasses and `plan_migration`**

  Enumerate Git-visible text candidates when Git is available, with a safe
  filesystem fallback for isolated tests. Skip `.git`, caches, virtual
  environments, paper build directories, managed PDFs, and undecodable binary
  files. Prepare changed UTF-8 text fully in memory.

- [ ] **Step 3: Write failing tests for collisions, temporary-name exclusion, and binary skipping**

  Assert planning raises a descriptive `MigrationError` for an occupied
  target and duplicate target, ignores tool-generated temporary siblings, and
  does not fail on a binary file containing arbitrary bytes.

- [ ] **Step 4: Implement validation and two-phase application**

  Validate all source and destination paths before mutation. Rename sources to
  UUID-bearing sibling names, rename temporaries to final targets, then write
  prepared text through sibling temporary files and `os.replace`.

- [ ] **Step 5: Write and pass CLI and idempotence tests**

  Assert default invocation prints a non-mutating plan, `--apply` performs the
  migration, relative metadata paths resolve, and a second plan contains no
  renames or edits.

- [ ] **Step 6: Run focused and full tests**

  Run: `pytest tests/test_rename_literature_files.py -q`
  Expected: pass.

  Run: `pytest -q`
  Expected: existing suite passes; report any unrelated pre-existing failure.

- [ ] **Step 7: Commit Task 2**

  Commit the completed tool and tests with message
  `Add safe literature filename migration tool`.

### Task 3: Apply and verify the real corpus migration

**Files:**
- Rename: managed files under `literature/pdf/`, `literature/extracted/`, and `literature/references/`
- Modify: exact-reference-containing text files discovered by the tool
- Regenerate: `literature/bundle.md`

**Interfaces:**
- Consumes: Task 2 CLI and validation functions.
- Produces: migrated repository corpus with no old-format managed names or broken front-matter paths.

- [ ] **Step 1: Capture the dry-run plan**

  Run: `python tools/rename_literature_files.py`
  Expected: 112 physical renames across the 41/40/31 baseline files, plus the
  discovered text-edit count, with zero validation errors.

- [ ] **Step 2: Apply the migration**

  Run: `python tools/rename_literature_files.py --apply`
  Expected: successful summary with the same rename and edit counts.

- [ ] **Step 3: Verify idempotence and front-matter links**

  Run: `python tools/rename_literature_files.py`
  Expected: zero renames and zero edits.

  Run: `python tools/rename_literature_files.py --check`
  Expected: no old `_YYYY_` managed names and no unresolved `source_pdf` or
  `references_file` paths.

- [ ] **Step 4: Regenerate and verify the literature bundle**

  Run: `python tools/build_literature_bundle.py`
  Expected: successful bundle generation using migrated extracted filenames.

- [ ] **Step 5: Run regression tests and inspect Git changes**

  Run: `pytest tests/test_rename_literature_files.py -q`
  Expected: pass.

  Run: `git status --short` and `git diff --check`
  Expected: renames are visible, no whitespace errors, and unrelated user
  changes remain untouched.

- [ ] **Step 6: Commit the corpus migration**

  Commit only the literature renames, exact-reference updates, regenerated
  bundle, tool, and tests with message `Migrate literature filename convention`.
