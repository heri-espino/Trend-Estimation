# Dynamic Branch Selection — independent notes

**Current design (2026-10-08):** track local minima of **temporally
weighted forecast-loss surfaces** by fixed method \(m\), order \(d\),
window \(L\), horizon \(h\). The current method does **not** use
the old Val1/Val2 transformed-loss branch definition.
See [shared protocol](../../WEIGHTED_SURFACE_PROTOCOL.md)
and [current mathematical specification](dynamic_tracked_smoothness.md).

## Cuaderno actual antes de LaTeX (2026-10-09)

**Orden de lectura prioritario para autores y agentes:**

1. [RESEARCH_NOTEBOOK.md](RESEARCH_NOTEBOOK.md) —
   pregunta, delimitación respecto a Paper 1, funciones F ponderadas,
   algoritmo de correspondencias, selección de rama y regla
   media-de-3 **después** del tracking.
2. [PROOF_LEDGER.md](PROOF_LEDGER.md) —
   teorema de función implícita bajo curvatura positiva,
   cota de desplazamiento de raíces con hipótesis explícitas,
   bifurcaciones, identificabilidad y cuestiones abiertas.
3. [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md) —
   comparar la misma tau/y a distintos ruidos, heatmaps F,
   ramas y tendencias extrapoladas; controles de una sola rama,
   escenarios estacionarios vs cambios, métricas y tablas.
4. [Guía de conversión a manuscrito](../../NOTES_TO_MANUSCRIPT.md).

Estas notas describen el **nuevo** tracking en funciones de pérdidas
weighted-F. Los datos CP04–CP08 y LaTeX legacy corresponden al
método antiguo Val1/Val2, se conservan como antecedentes históricos,
y NO deben emplearse como resultados de este procedimiento.

- [Research question and protocol](research_objective.md)
- [Tracked smoothness and V/psi/phi rules](dynamic_tracked_smoothness.md)
- [Temporal minima correspondence](temporal_minima_tracking.md)
- [Completed experiments and limitations](results_and_boundaries.md)
- [Legacy mathematical branch draft](tracked_minimum_smoothness_selection_legacy.tex)

All chronology and ownership are defined by this independent study.
Numbers from completed checkpoints are preserved, including negative findings.
Unrun matching experiments must never be treated as results.
