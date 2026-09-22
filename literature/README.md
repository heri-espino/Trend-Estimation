# Literature Workspace

This directory is the metadata/RAG entry point for the Trend Estimation research program.

## Files

- `manifest.csv` — master list of target references and reading status.
- `references.bib` — shared BibTeX used by manuscripts.
- `pdfs/` — local paper PDFs; intentionally ignored by Git.
- `extracted/` — text/Markdown extracted from papers when useful for RAG.
- `notes/` — per-paper structured reading notes when a paper needs more than metadata.

## PDF policy

Do not commit closed-access or institutionally licensed PDFs. Keep them locally under `literature/pdfs/`. Open-access files may still be left local by default; the manifest should store the DOI and source URL so they are reproducible.

## Current audit status

The target set in `manifest.csv` contains **40 references**. As of
2026-09-22, **24 papers are present in `literature/extracted/`** and that
extracted corpus has been reviewed for the active objective. The target audit
is therefore not complete.

Do not convert findings from the extracted subset into final novelty claims.
Prioritize the remaining sources closest to smoothing under autocorrelation,
forecast-oriented penalized trends, data-driven HP/smoothing choices, and
time-varying or structural-change forecasting.

## RAG workflow

For each paper:

1. record DOI/title/authors/link in `manifest.csv`;
2. save the local PDF path if available;
3. extract text/math/tables carefully;
4. create a structured note for high-priority papers;
5. mark claims that are safe to cite with page/section location;
6. update `references.bib` only after metadata is verified.

Recommended structured fields:

- research question;
- model/estimator;
- parameter-selection rule;
- temporal validation design;
- forecasting versus smoothing;
- horizon/window;
- data;
- regime definition;
- result;
- limitations;
- overlap with our active paper;
- remaining gap;
- useful equations;
- pages/sections.

The active novelty audit should focus first on the closest work listed in `notes/roadmap.md`.
