# Índice · Cuaderno de investigación de tendencias con media no nula

**Antes del paper publicable: completar demostraciones, fuentes y Monte Carlo.**

1. [RESEARCH_NOTEBOOK.md](RESEARCH_NOTEBOOK.md) — pregunta, antecedentes,
   razonamiento, formulación, algoritmo, justificación y límites.
2. [PROOF_LEDGER.md](PROOF_LEDGER.md) — lemas con hipótesis y prueba
   paso a paso; qué hizo Guerrero y qué es nuestra propuesta.
3. [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md) — generadores
   \(\tau+\xi+\epsilon\), seguimiento de la tendencia original,
   pasado vs futuro, niveles de ruido, gráficos/tablas y controles.
4. [LITERATURE_POSITIONING.md](LITERATURE_POSITIONING.md) —
   referencias existentes, auditoría de novedad pendiente.
5. [RESEARCH_LOG.md](RESEARCH_LOG.md) —
   registro cronológico de decisiones, implementaciones, fallos.
6. [README principal](../README.md) y
   [handoff](../AI_HANDOFF.md).

**Obsidian vault compartido**, antes de escribir el paper:
\`notes/conceptos/06-Media-de-diferencias-Guerrero.md\`,
\`notes/conceptos/07-Perfilamiento-de-mu-en-CV.md\`,
\`notes/conceptos/08-Nuevo-paper-tendencia-y-media.md\`.

**Fuente primaria:** Guerrero (2007), eqs. (2), (3), (12),
(16)–(18). La sección de pronóstico muestra d=1 y d=2.
El perfilado de mu según el MSE de pronóstico es propuesta de
este proyecto, **no aparece como resultado verificado del autor**.

**App actual:** \`streamlit run apps/mean_difference_forecasting.py\`,
una interfaz separada con S, μ(S), comparación Guerrero,
tendencia ajustada y pronóstico h-step, CSV/JSON exportables.

**Estado:** notas/estructura/código de primera versión.
**Estado:** notas/estructura/código de primera versión.
No hay todavía MSFE comparativos obtenidos ni journal decidido.
