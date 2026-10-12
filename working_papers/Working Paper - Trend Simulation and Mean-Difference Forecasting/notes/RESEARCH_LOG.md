# Registro cronológico y de decisiones

## 2026-10-11 — Nacimiento del cuarto working paper

**Motivación:** al estudiar Guerrero (2007) reapareció
la media no nula de diferencias de orden d, que
el estudio forecast-CV anterior había fijado en
cero. Se decidió abrir un paper separado dedicado
a simulación de tendencias y elección h-step
de $(S,\mu)$ con perfilado exacto de $\mu$.

**Hallazgo al revisar el repositorio:** ya existían
\`GuerreroSpectralSolver\` con plug-in de eq. (17) y
\`finite_difference_forecast_operator\` con
\`drift_loading\`. No duplicarlos.

**Cambio nuevo:** \`mean_difference_cv.py\`
implementa representaciones afines exactas y
los modos zero/guerrero/profile, con tests.
Nueva carpeta de experimento separada.
**App propia:** `apps/mean_difference_forecasting.py` ahora permite
visualizar las tres políticas, la curva F(S), μ(S), ajuste y pronóstico.
Aún debe pasar las pruebas en el entorno del usuario.

**Literatura fuente consultada:** Guerrero (2007)
en PDF proporcionado al proyecto (pp. 1225–1229,
ecuaciones 2, 3, 12, 16–18). Las fórmulas
de perfilado y Hessiana concentrada son
álgebra estándar aplicada al nuevo criterio;
originalidad publicada NO verificada.

**Conservación:** los tres working papers y
sus campañas históricas se mantienen intactos.
No borrar resultados, no alterar ni mezclar la
campaña CUDA de \`mu=0\`.

**Pendiente:** ejecución y validación de tests,
piloto de distintas curvas verdaderas/ruido,
optimización GPU a posteriori, figurar
tendencia pasada/futura, comparación de
criterios estándar, auditoría bibliográfica,
teoría del mínimo perfilado y manuscrito final.
