# Literature filename migration design

## Objective

Create a reusable repository tool that migrates the literature corpus from the
current `Author_Year_title-words` convention to the literal delimiter-swapped
`Author-Year-title_words` convention. For compound author tokens, this means,
for example, `Islas-Camargo_2019_forecasting-remittances-mexico` becomes
`Islas_Camargo-2019-forecasting_remittances_mexico`.

The migration must rename files consistently across `literature/pdf/`,
`literature/extracted/`, and `literature/references/`, update metadata and exact
path references throughout the repository, reject unsafe plans before making
changes, and be idempotent.

## Scope

The tool will manage:

- PDF filenames under `literature/pdf/`;
- extracted Markdown filenames under `literature/extracted/`;
- reference Markdown filenames under `literature/references/`;
- YAML front matter fields such as `id`, `source_pdf`, `source_filename`, and
  `references_file`;
- exact occurrences of migrated literature names and paths in repository text
  files, including notes, documentation, scripts, and generated Markdown
  bundles.

The tool will not rewrite ordinary prose punctuation, BibTeX citation keys,
directory names, or filenames outside the three managed literature
directories.

## Naming rule

A migratable core name is recognized by the old-format marker `_YYYY_`, where
`YYYY` is a four-digit year. The entire core name is transformed with a
simultaneous character translation:

- every underscore becomes a hyphen;
- every hyphen becomes an underscore.

Examples:

- `Baxter_1999_approximate-band-pass-filters` becomes
  `Baxter-1999-approximate_band_pass_filters`;
- `Islas-Camargo_2019_forecasting-remittances-mexico` becomes
  `Islas_Camargo-2019-forecasting_remittances_mexico`.

Extensions and technical suffixes are not part of the translated core. In
particular, `Baxter_1999_approximate-band-pass-filters.references.md` becomes
`Baxter-1999-approximate_band_pass_filters.references.md`.

Names already using `-YYYY-` do not match the old-format marker and are left
unchanged. This makes repeated execution idempotent rather than reversing the
migration.

## Command-line interface

The tool will be `tools/rename_literature_files.py`.

- Running it without mutation flags produces a dry-run plan.
- Running it with `--apply` applies the validated plan.
- The command exits nonzero when the corpus layout is missing, a target
  collision exists, mappings are inconsistent, or a planned text file cannot
  be updated safely.

The dry run reports the number of physical renames, text files requiring
updates, and any validation failures. A successful idempotence check reports
zero planned renames and zero planned text updates.

## Planning and validation

The tool first scans the three managed directories and builds a core-name map.
The same old core must map to the same new core in every directory. Before any
write, it validates that:

- all target paths are unique;
- no target already exists unless it is the same unchanged path;
- no two sources map to one target;
- managed directories exist;
- repository text updates can be decoded as UTF-8;
- a replacement cannot be partially shadowed by a shorter core mapping.

Replacement keys are applied longest-first so related names such as a paper
and its appendix cannot corrupt each other's paths.

## Text updates

The core-name map is used for exact string replacement throughout repository
text files. Replacing the old core inside a larger known value updates:

- extracted-document IDs;
- reference-document IDs while preserving the `-references` semantic suffix;
- `source_pdf` paths;
- `source_filename` values;
- `references_file` paths;
- exact literature links in notes and documentation;
- filename markers in generated Markdown bundles.

The tool scans Git-visible text files and skips `.git`, binary files, generated
paper build directories, virtual environments, and cache directories. Files
are changed only when they contain an exact old core from the migration map.

## Applying the migration

Physical renames use two phases within each directory:

1. rename each source to a unique temporary sibling name;
2. rename each temporary file to its validated final name.

This prevents Windows and case-insensitive filesystem collisions. Text files
are written through temporary sibling files followed by atomic replacement.
The complete plan is validated and all changed text is prepared in memory
before filesystem mutation begins.

The repository is expected to be under Git, which remains the recovery
mechanism for tracked corpus files if an external interruption occurs during
application.

## Verification

Automated tests will use an isolated temporary repository fixture and cover:

- simultaneous delimiter translation;
- preservation of `.references.md`;
- metadata and cross-directory path updates;
- repository-wide exact-reference updates;
- target-collision rejection before mutation;
- dry-run behavior;
- successful apply behavior;
- idempotence after migration.

After applying the tool to the real repository, verification will confirm:

- no managed filename retains the old `_YYYY_` marker;
- all expected PDFs, extracted Markdown files, and reference Markdown files
  retain their original counts;
- all `source_pdf` and `references_file` paths resolve from their Markdown
  files;
- no exact old core remains in repository text files;
- a second dry run reports zero changes;
- the existing literature bundle builder still succeeds.

## Expected migration size

At design time the corpus contains 41 PDFs, 40 extracted Markdown files, and
31 reference Markdown files. These counts are verification baselines, not
hard-coded limits; the tool discovers the current corpus dynamically.
