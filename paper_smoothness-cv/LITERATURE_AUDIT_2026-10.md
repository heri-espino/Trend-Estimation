# Literature and citation audit — October 2026

This note documents the reference revision of
\`paper_smoothness-cv/manuscript/\` for a possible submission to
*Communications in Statistics—Simulation and Computation* (CSSC).
It distinguishes sources already extracted under \`literature/extracted/\`
from articles verified through their publishers. It is not a claim of
exhaustive coverage of every CSSC issue.

## Central positioning

The PLS estimator, trace-based smoothness index, automatic choice of
penalty, and use of controlled-smoothness trends for forecasting
**predate this manuscript**. The defensible claim concerns chronological
tracking of multiple forecast-loss minima, the resulting branch histories,
and separated decisions for choosing a branch and mapping its history
to a fresh smoothing level. Forecast-optimal tuning itself is not novel.

The manuscript uses the rescaled index
\`S = [L/(L-d)] * (1 - trace(H)/L)\` for \`d>=1\`, so that the
upper endpoint is one. This is a monotone rescaling of Guerrero's
index, **not** a new PLS estimator or a claim of new spectral theory.

The strongest scientific difficulty remains the empirical result:
branch-based rules improve upon pooled CV only in the small
confirmation panel, not in the larger financial panel or most of
the controlled-roughness comparison. Citation revision cannot
establish a forecasting performance advantage that the data do not show.

## Highest-priority works

| Source | Why it matters | In extracted corpus? |
| --- | --- | --- |
| Guerrero (2007), *Statistics & Probability Letters*, DOI \`10.1016/j.spl.2007.03.006\` | PLS smoothing, statistical interpretation, original smoothness index | Yes |
| Guerrero (2008), *International Statistical Review*, DOI \`10.1111/j.1751-5823.2008.00047.x\` | Analyst-chosen smoothness | Yes |
| Cortés-Toto, Guerrero & Reyes (2017), **CSSC**, DOI \`10.1080/03610918.2015.1005236\` | Direct journal precedent: CV, GCV, AICc, BIC and attained smoothness | Yes |
| Guerrero, Cortés-Toto & Reyes (2018), *Statistical Methods & Applications*, DOI \`10.1007/s10260-017-0389-8\` | Autocorrelation changes controlled-smoothness estimation | No |
| Islas-Camargo, Guerrero & Silva (2019), *Romanian Journal of Economic Forecasting* 22(1):38–56 | Prior forecasting application with a controlled-smoothness trend | Yes |
| Islas-Camargo & Zumaya-Galván (2025), *Estudos Econômicos*, DOI \`10.1590/1980-53575516acjg\` | Controlled trends and exchange-rate forecasting | Yes |
| Franke, Kukacka & Sacht (2026), *Computational Economics*, DOI \`10.1007/s10614-026-11378-9\` | Modern HP tuning, but against a latent-trend recovery target | Yes |
| Biessy (2026 volume; online 2025), *ASTIN Bulletin*, DOI \`10.1017/asb.2025.10061\` | Modern Whittaker–Henderson smoothing, parameter selection, extrapolation | Yes |

## Target-journal references

| Article | Relevance |
| --- | --- |
| Cortés-Toto et al. (2017), DOI \`10.1080/03610918.2015.1005236\` | Direct PLS smoothness/optimality-criteria predecessor; indispensable |
| Vilar-Fernández & Cao (2007), DOI \`10.1080/03610910601158377\` | Nonparametric forecasting with smoothing-parameter selection on dependent time series |
| Bates, Lindstrom, Wahba & Yandell (1987), DOI \`10.1080/03610918708812590\` | Computational GCV benchmark and regularization parameter selection |

Additional CSSC paper screened but **not inserted**:
Dutta (2016), *Cross-validation Revisited*,
DOI \`10.1080/03610918.2013.862275\`. It concerns kernel-density
cross-validation under heavy-tailed distributions, rather than
penalized trend continuation. Inserting it solely for journal
representation would weaken topical relevance.

Nearby **different journal**: Guerrero, Islas-Camargo and
Ramírez-Ramírez (2017), *Communications in Statistics—Theory and
Methods*, DOI \`10.1080/03610926.2015.1133826\`.
This addresses controlled-smoothness **multivariate** trend estimation;
it is not in CSSC, and it is not cited because the present paper is
univariate.

## References not yet represented by extracted full-text files

The following are cited in the manuscript but not found in the
40-document \`literature/extracted/\` inventory reviewed:

- Bates et al. (1987), GCVPACK — \`10.1080/03610918708812590\`
- Vilar-Fernández & Cao (2007) — \`10.1080/03610910601158377\`
- Guerrero & Galicia-Vázquez (2010) — \`10.1002/asmb.763\`
- Guerrero, Cortés-Toto & Reyes (2018) — \`10.1007/s10260-017-0389-8\`
- Taylor (2004), smooth-transition exponential smoothing
- Zafar, Kellard & Vinogradov (2022), multi-stage forecasting filter
- Staněk (2023), optimal out-of-sample loss evaluation

These articles have verified bibliographic descriptions, but
the missing full texts should be obtained legally and added to the
corpus if a full-text reproducibility requirement is adopted.
**Do not automatically commit copyrighted publisher PDFs to a public
repository.**

## Citation and manuscript checks

- Every cited key must exist in \`manuscript/references.bib\`.
- Bibliographic items with no citation should be removed from the
  manuscript-specific \`.bib\` file; the general literature corpus
  should remain broader.
- All equations use named labels; existing \`cleveref\` usage remains.
- The article currently builds with \`plain\` BibTeX style. Before
  submission, check the journal's *current* author instructions
  for citation punctuation, bibliography style, and format. Do not
  mistake the source-based literature revision for journal-style
  compliance or for a successful full manuscript compilation.
