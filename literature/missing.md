# Missing literature

Last audited: 2026-09-30.

## Status

The canonical target list is `literature/manifest.csv`, which contains **40 references**.

The repository currently contains **40 PDF files** and **40 extracted Markdown files**, but these correspond to **34 of the 40 canonical references**. The difference is explained by supplemental/duplicate documents that are already in the corpus but are not separate entries in the canonical manifest.

Therefore:

- Canonical references: **40**
- Canonical references present: **34**
- Canonical references still missing: **6**
- PDF files currently stored: **40**

The older audit reported 16 missing references. Since then, **10 of those 16 have been added**.

## Still missing from the canonical 40

### High priority

1. **Guerrero & Galicia-Vázquez (2010)** — *Trend estimation of financial time series*
   - DOI: `10.1002/asmb.763`
   - Why it matters: closest direct antecedent for penalized trend estimation applied to financial time series.
   - Expected basename: `Guerrero-2010-trend_estimation_financial_time_series.pdf`

2. **Guerrero, Cortés-Toto & Reyes Cervantes (2018)** — *Effect of autocorrelation when estimating the trend of a time series via penalized least squares with controlled smoothness*
   - DOI: `10.1007/s10260-017-0389-8`
   - Why it matters: directly studies serial dependence/autocorrelation in the controlled-smoothness framework.
   - Expected basename: `Guerrero-2018-autocorrelation_controlled_smoothness.pdf`

3. **Racine (1997)** — *Feasible Cross-Validatory Model Selection for General Stationary Processes*
   - DOI: `10.1002/(SICI)1099-1255(199703)12:2<169::AID-JAE426>3.0.CO;2-P`
   - Why it matters: foundational cross-validation result for dependent stationary data.
   - Expected basename: `Racine-1997-cross_validation_stationary_processes.pdf`

4. **Racine (2000)** — *Consistent cross-validatory model-selection for dependent data: hv-block cross-validation*
   - DOI: `10.1016/S0304-4076(00)00030-0`
   - Why it matters: directly relevant to leakage-resistant validation for dependent time series.
   - Expected basename: `Racine-2000-hv_block_cross_validation.pdf`

### Foundational / supporting

5. **Brooks, Stone, Chan & Chan (1988)** — *Cross-validatory graduation*
   - DOI: `10.1016/0167-6687(88)90097-2`
   - Why it matters: early cross-validation treatment of graduation/smoothing.
   - Expected basename: `Brooks-1988-cross_validatory_graduation.pdf`

6. **Kitagawa & Gersch (1996)** — *Smoothness Priors Analysis of Time Series*
   - DOI: `10.1007/978-1-4612-0761-0`
   - Type: book / monograph rather than a journal paper.
   - Why it matters: foundational probabilistic/state-space treatment of smoothness priors.
   - Expected basename: `Kitagawa-1996-smoothness_priors_time_series.pdf`

## Previously missing, now present

The following items were on the older 16-item missing list and are now in the corpus:

- Franke, Kukacka & Sacht (2026) — data-driven HP smoothing parameter.
- Islas-Camargo & Zumaya Galván (2025) — exchange-rate predictability with controlled smoothness.
- Weinert (2007) — efficient Whittaker-Henderson smoothing.
- Hart (1994) — time-series cross-validation for dependent data.
- Burman, Chow & Nolan (1994) — cross-validation for dependent data.
- Tashman (2000) — out-of-sample forecast accuracy.
- Campbell & Thompson (2008) — excess stock-return prediction.
- Hodrick & Prescott (1997) — postwar U.S. business cycles.
- King & Rebelo (1993) — low-frequency filtering and real business cycles.
- Hamilton (1989) — nonstationary time series and the business cycle.

## About the older “~50 papers” list

No separate, authoritative approximately-50-item target list is currently stored in the repository. The durable canonical list that can be audited against files is the **40-reference manifest**. If the broader exploratory list is recovered later, it should be added as a separate `extended_manifest.csv` rather than mixed silently into the canonical 40.
