# Paper 2 · Simulaciones sobre persistencia de mínimos y pronóstico

**2026-10-09 · Diseños y figuras pendientes de resultados del método nuevo.**
Ver [evaluación compartida](../../SIMULATION_EVALUATION_PROTOCOL.md),
[algoritmo](../../../experiments/smoothness_cv/weighted_surface_study.py),
[generador](../../../experiments/smoothness_cv/simulation_dgps.py) y
[protocolo de correspondencias numéricas](../../../experiments/numerical_smoothness_selection/run_tracking_correspondence_benchmark.py).

## Extensión formal CUDA/Study D (2026-10-09)

Se añadieron **720 celdas factoriales difíciles**,
para un total \`mega\` de 1,248 (124,800 escenario–semilla
a 100 semillas por celda). Incluir saltos cerca del futuro
pronosticado, recuperaciones, pulsos y picos transitorios,
oscilaciones no estacionarias, tendencia latente estocástica
y contaminación rara por outliers. Son pruebas críticas
de persistencia espuria: un mínimo que «continúa»
algorítmicamente no necesariamente predice la tendencia
tras un cambio abrupto.

**Nuevo diseño de figura:** la misma \(\tau\) irregular bajo
tres niveles \(\sigma\), observada y ruidosa, con
un panel paralelo para geometría \(F_r(S)\),
los mínimos detectados, los IDs de ramas y el
pronóstico outer de \(\arg\min F_M\) vs tracking.
La comparación usa exactamente el mismo
\(m,d,L,h\) y test oculto; no atribuir diferencias
de política de ponderación al tracking.

El cálculo de matrices de pérdidas histórico puede
hacerse en GPU float32; matching de ramas,
decisión, classical baselines y evaluación externa
siguen en CPU. **Solo una prueba inicial** de
precisión contra CPU; ninguna comparación recurrente
durante experimentos formales. Ver
[CAMPAIGN_README.md](../../../experiments/smoothness_cv/CAMPAIGN_README.md).
**No resultados todavía del Estudio D.**

## 1. ¿Qué se simula, y cuál es el control justo?

Igual que en Paper 1:
\[
y_t=\tau_t+\xi_t+\epsilon_t
\]
con \(\tau\) lineal/cuadrática/
cúbica y curvaturas complejas,
distintos ruidos y regímenes.
El algoritmo recibe SOLO \(y\).
Se construyen funciones
\(F_r^{(m,d,L,h)}(S)\)
**desde pérdidas ya observadas**,
y se siguen sus mínimos.

Dos selectores sobre exactamente
las MISMAS F_r:
\[
S_T^{pool}=\arg\min_SF_M(S),\quad
S_T^{track}=\phi(V_{\psi(\{V_j\})}).
\]
Sus pronósticos se comparan
en las mismas observaciones
posteriores a T. La diferencia
no se debe a usar otra
función de pérdida o
otra extrapolación G.

## 2. ¿Qué significa conocer una rama verdadera?

En una simulación de series
económicas/temporales sabemos
la **tendencia latente tau**,
pero **no** existe en general
un ID de rama «verdadero» dado
por el DGP. Nuestras etiquetas
son inferencias del algoritmo.
Para evaluar matching aislado,
hay que construir **familias
sintéticas F(S,u) con trayectorias
de mínimos conocidas**,
separadas de las F_PLS
generadas por series.
Ese benchmark de
correspondencia sintética
mide errores de tracker, no
prueba predicción sobre
series reales.

Proponemos dos ensayos
complementarios:
- Tracking controlado: valles
  con trayectorias definidas,
  nacimientos, muertes, cruces,
  separaciones y curvaturas.
  Ground truth de identidades
  explícitamente predefinido.
- Tracking sobre F_PLS:
  DGP con tau conocida;
  las ramas NO tienen
  verdad externa automática.
  Medimos estabilidad
  del detector, reproducibilidad
  y error de pronóstico.
  No adjudicar «accuracy
  de identidad verdadera»
  si no construimos
  esa verdad.

## 3. Tipos de DGP del ensayo grande

**A · referencia:** los 16
escenarios lineal/Beta +
estacionalidad + sigma +
N fuente. No son un
«tracking benchmark original»
del artículo Cortés-Toto;
solo son generadores
comunes para una extensión.

**B · dificultad de tendencia:**
384 celdas para lineal,
cuadrática, cúbica y otras
formas, N, sigma y ruido.
Objetivo: estudiar si
la complejidad de tau
modifica cardinalidad/
posición de mínimos
y ventaja de seguirlos.

**C · evolución temporal:**
128 celdas con control
estable, ruptura de
pendiente/curvatura, cambio
de varianza, transición
suave o transitoria;
objetivo: separar
adaptación real de
matching espurio.

**Un solo mínimo** no es
un escenario desechable:
es un control negativo
para ver si la media
temporal de S puede
perjudicar sin ofrecer
opciones de rama.

## 4. Qué métricas necesitamos

**Futuro h-step**:
MSFE observado,
MSFE de tau futura,
RMSE e intervalos de
contrastes *pareados*
contra pooled del
mismo m,d,L,h.

**Recuperación**:
MSE frente a tau pasada
y EDF/S seleccionado.
La mejor rama en F
histórico no es por
definición la mejor
para tau futura.

**Geometría/ramas**:
- mínimo, mediana,
  máximo del número
  de mínimos por F;
- porcentaje de pasos
  con ≥2 mínimos;
- nacimientos/muertes,
  duración de ramas,
  soporte de seleccionada;
- distancia \(|S_{r}-S_{r-1}|\),
  aceleración y cruces;
- diferencia de pérdidas
  de ramas candidatas;
- gaps de F'' (curvatura)
  cuando la derivada
  pueda estimarse con
  estabilidad;
- sensibilidad a
  epsilon y grilla 101/
  161/321/501;
- porcentajes de
  fallback y de límites
  S=0/1.

**Estado implementado:**
\`simulation_evaluation.py\`
incluye columnas de soporte,
número de ramas y de
mínimos históricos detectados.
No confundir esos **recuentos
acumulados** con número de
mínimos activos en cada paso.
Nacimientos, muertes,
crossings, F'' y medidas
de matching aún exigen
salidas/experimentos
adicionales.

## 5. Figuras concretas para el artículo

**Figura 1. Mecanismo: del ruido a las ramas.**
Para la misma tau simulada,
filas lineal, cuadrática
o cambio de pendiente,
columnas sigma baja,
media y alta.
En cada panel: tau e y,
con T vertical.
Al lado, heatmap de
\(F_r^{(m)}(S)\) en
origen×S y puntos de
mínimos; debajo, gráfica
de ramas por ID
sobre ese mismo dominio.

**Figura 2. m cambia la geometría.**
Misma serie, d,L,h,
cuatro bandas para
uniform-all, last-K,
linear, exp.
Comparar número y
posición de mínimos
para evidenciar que
**m pondera funciones**,
no S. Mencionar que
en algunos casos las
ramas pueden coincidir
o haber una sola.

**Figura 3. De branch S al futuro.**
Una rama seleccionada
y sus últimos tres S
marcados, S operativo
\(\phi\) y S pooled.
Dos líneas de tendencia
estimada sobre ventana
L; ambas se continúan
a h pasos y se muestran
con tau futura conocida
y observaciones futuras.
No trazar un ajuste
usando el futuro como
pronóstico válido.

**Figura 4. Tracking robusto vs
frágil.** Dos ejemplos
preseleccionados:
mínimo bien curvado
que se desplaza suave,
y mínimos casi
degenerados/cruzados
que cambian ID con
epsilon. Indicar si
son F_PLS reales o
F(S,u) sintéticas de
ground-truth. No
llamarlo «estable»
sin referencia.

**Figura 5. Resultado externo.**
Forest plot de
\(\Delta\mathrm{MSFE}=
\mathrm{MSFE}_{track}-
\mathrm{MSFE}_{pool}\)
para cada m y
forma/ruido/regímen,
con intervalos
por semilla independiente.
Incluir negativos y
positivos.

**Figura 6. Diagnóstico predictor.**
Frecuencia de ≥2
mínimos vs cambio
de régimen/ruido,
y error de tracking
vs radio epsilon;
no correlacionar de
modo causal sin análisis.

## 6. Tablas que responden a preguntas

- T1: política \(m,d,L,h\),
  epsilon, \(\psi,\phi\),
  fallback y definición
  de ramas activas.
- T2: cardinalidad de
  mínimos/vida de ramas
  según DGP y ruido.
- T3: tracking vs
  pooled **pareados**
  por método m (ambos
  comparten exactamente F).
- T4: ablación de
  epsilon, paso de
  malla y mean-last-K;
  no escoger retrospectivo
  por outer test.
- T5: perfiles de
  pérdida ante
  ruptura/estacionario,
  con tasas de
  fracaso/fallback.

## 7. Diseño de visualización sin cherry-picking

Seleccionar semillas y
formas representativas
ANTES de mirar
efectos externos o
usar reglas automáticas
de quantiles empíricos
predefinidas para
ejemplos extremos.
Si se decide ilustrar
peor/mejor caso
después de analizar
resultados, etiquetarlo
como **análisis post hoc**.
En cualquier figura
de pérdida mostrar
qué validez temporal
tiene cada F (sus
pseudo-futuros se
completaron hasta T).

## 8. Límites científicos del estudio actual

- El hecho de mantener
  ramas no prueba que
  tengan contenido
  de forecast.
- Diferencias en d
  cambian la
  extrapolación G;
  no atribuirlo solo
  a matching.
- La comparación
  principal fija m
  para ambos métodos.
- Heterocedasticidad,
  autocorrelación y
  estacionalidad
  desafían la validez
  predictiva sin
  cambiar el
  funcional V=I.
- Resultado negativo
  sostenido también
  es información
  científica valiosa.
- **Resultados CP04–CP08
  del algoritmo anterior
  son históricos**, no
  resultados de este
  nuevo tracking.

Los gráficos para
publicación descritos
aquí deben generarse,
verificarse y conservar
proveniencia; no
prometer que ya existen.
