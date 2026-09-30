# Literature Workspace

This directory is the metadata/RAG entry point for the Trend Estimation research program.

## Files

- `manifest.csv` — master list of target references and reading status.
- `references.bib` — shared BibTeX used by manuscripts.
- `pdf/` — original paper PDFs used by the research project; intentionally
  versioned in Git.
- `extracted/` — text/Markdown extracted from papers for RAG; intentionally
  versioned in Git.
- `notes/` — per-paper structured reading notes when a paper needs more than metadata.

## Naming convention

Paper artifacts use the same canonical basename across subfolders:
`Author_Year_short-title` (for example, `Guerrero_2007_time-series-smoothing-penalized-least-squares`).
The PDF is the canonical source for identifying author, publication year, and short title; matching extracted and references Markdown files reuse that basename.

## PDF policy

For this project, the working literature corpus is part of the research
archive. Original PDFs used by the project and their extracted text are
intentionally committed to the repository rather than kept only on individual
workstations.

When adding a paper:

1. keep the original PDF under `literature/pdf/`;
2. keep the extracted representation under `literature/extracted/` when
   available;
3. record DOI/title/authors/source metadata in `manifest.csv`;
4. do not silently delete a PDF or extraction while the paper is active.

This repository-level preservation policy is separate from questions of source
licensing or redistribution rights, which remain the responsibility of the
repository maintainer.

## Current audit status

The canonical target set in `manifest.csv` contains **40 references**. As of
2026-09-30, the repository contains **40 PDFs** and **40 extracted Markdown
files**, but these cover **34 of the 40 canonical references**; the remaining
files include supplemental or duplicate documents outside the manifest.

The **6 canonical references still missing** are tracked in
[`missing.md`](missing.md). Do not infer corpus completeness from the raw PDF
count alone.

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
