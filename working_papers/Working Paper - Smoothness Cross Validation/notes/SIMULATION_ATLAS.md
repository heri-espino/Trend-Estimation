# Paper 1 · Atlas de simulación, visualización y tablas

**Plan de figuras + correspondencia al código (2026-10-09).
NO son resultados ejecutados del protocolo nuevo.**
Referencias:
[protocolo común](../../SIMULATION_EVALUATION_PROTOCOL.md),
[generador](../../../experiments/smoothness_cv/simulation_dgps.py),
[evaluación](../../../experiments/smoothness_cv/simulation_evaluation.py),
[ejecución](../../../experiments/smoothness_cv/CAMPAIGN_README.md).

## Ampliación formal (2026-10-09): nuevos DGP difíciles en CUDA

El protocolo ahora añade **Estudio D** con **720 celdas factoriales**:
12 formas de \(\tau\), N=300/600, tres intensidades de ruido,
cinco distribuciones (incluyendo outliers poco frecuentes),
y presencia/ausencia de estacionalidad. La batería \`mega\`
contiene **1,248** celdas (528 originales + 720 nuevas);
100 semillas por celda son 124,800 instancias, no observaciones
globalmente independientes. Las nuevas series incluyen
saltos de nivel, recuperación, pulsos, cambio de frecuencia,
oscilaciones, tendencias estocásticas de nivel y pendiente.
**No introducir estas realizaciones en una demostración de
superioridad universal;** son pruebas adicionales para refutar
hipótesis demasiado optimistas.

**Las figuras deben separar** para estas formas irregulares:
trayectoria latente \(\tau\) conocida, ruido/estacionalidad,
datos observados y, serie PLS estimada, y su extrapolación
h-step con test oculto durante selección. Mismo tipo de
figura a ruido débil/moderado/fuerte. Analizar cuándo
\(\hat\tau\) parece fiel visualmente pero el forecast falla
por salto irreversible o cambio de pendiente.

Se implementó \`--backend cuda\` para computar por lotes las
pérdidas de validación, pero **la decisión PLS es idéntica**
y otras etapas siguen CPU. Una auditoría inicial de precisión
se realiza una vez; la campaña formal evita repetidas comparaciones
CPU/GPU. Ver [manual](../../../experiments/smoothness_cv/CAMPAIGN_README.md).
Aún no hay resultados del nuevo Study D ejecutados/verificados.

## Corrida conjunta de ocho horas: protocolo más defendible

[JOINT_FORMAL_8H_PROTOCOL.md](../../JOINT_FORMAL_8H_PROTOCOL.md)
define un **panel predeclarado de 144 escenarios**, más
interpretable que terminar un porcentaje arbitrario de las
1,248 celdas de exploración. En B se conservan tres
intensidades de ruido **con la misma forma y escala latente
verdadera**; nuevas figuras PDF/PNG comparan \(\tau\), y,
\(\widehat\tau\) pasada y pronóstico h-step, para pooled
vs tracking usando la **misma ponderación F**.

Además de CV/GCV/AICc/BIC y S fijo, el protocolo agrega
comparadores de pronóstico ingenuo, deriva, ingenuo
estacional y extrapolación OLS lineal. Como esos
métodos no tienen S ni EDF, sus métricas van a una
tabla separada. Se evalúan en los mismos orígenes
externos, sin usar el test para ajustar parámetros.

Los diagnósticos numéricos del Paper 3 se hacen
sobre **esas mismas funciones F** en una
submuestra predeclarada; el artículo 1 describe
el método de refinamiento y las salvaguardas de
mínimos de manera breve, reservando la evaluación
numérica detallada para el Paper 3.

La ventana de ocho horas es un límite **suave**:
si la corrida termina con celdas incompletas,
resultados explícitamente **exploratorios**,
nunca una confirmación factorial balanceada.

## 1. ¿Qué simulamos y qué conoce el algoritmo?

\[
y_t=\tau_t+\xi_t+\varepsilon_t,\qquad t=1,\ldots,N.
\]
La simulación almacena \(\tau,\xi,\varepsilon,y\)
en componentes separados, pero el selector PLS recibe
**solo observaciones y**. \(\tau\) se usa para
dibujar y medir error latente *después* de predecir;
ningún método realizable conoce la tendencia.

Todos los métodos se comparan sobre la **misma
realización de y** y los mismos orígenes externos.
La semilla es réplica Monte Carlo dentro de una
celda DGP; varios h y T dentro de la réplica
son observaciones pareadas, no nuevas semillas.

## 2. Simulación A: benchmark de Cortés-Toto

El artículo original estudia **un factorial 2^4**,
no dos pruebas de pronóstico separadas:
- \(\tau_t=4t/N\) vs
  \(\tau(u)=.6\beta_{30,17}(u)+.4\beta_{3,11}(u)\)
  (densidades Beta, \(u=t/N\));
- sin/con estacionalidad trimestral
  \((1,-.5,-2.5,2)\);
- desviación \(\sigma\in\{.5,2\}\) de
  errores gaussianos iid;
- \(N\in\{50,200\}\).

**Dos productos diferentes:**
(a) reproducción de selectores clásicos sobre
N completo, \(d=2\), índice fuente \(S_G\),
con \`run_cortes_toto_replication.py\`;
(b) nuestra **extensión** a TSCV y futuro
h-step, con L=22 si N=50, L=60 si N=200,
que NO es un experimento del paper fuente.
Separar la tabla de reproducción de la
tabla de pronóstico original.

Preguntas: ¿cómo cambian S/EDF y recuperación
al introducir ruido, estacionalidad, N?
¿La selección dirigida a forecast supera
los selectores originales en un test futuro?
No inferir respuesta antes de ejecutar.

## 3. Simulación B: ¿qué pasa cuando crece la complejidad de tau?

**Código actual:** 16 formas B × N {180,360} ×
sigma {.25,.5,1} × ruido {iid, AR1, t5,
heterocedástico} = **384 celdas**.

Formas: lineal, cuadrática convexa,
cuadrática con punto de giro, cúbica-S,
cúbica con curvatura, cuártica,
sinusoidal lenta/rápida, mezcla Beta,
sigmoide, dos cambios de pendiente
(temprano/tardío), dos rupturas,
curvatura terminal, tendencia plana y
oscilatoria. Las formas no planas en B
se reescalan a rango dinámico cuatro
en la serie completa; la mezcla Beta de
A NO se reescala por fidelidad al estudio fuente.

**Cruces importantes para interpretar causalmente
una simulación diseñada (no causalidad de datos reales):**
- Mantener d=2 y comparar tau lineal,
  cuadrática y cúbica; el pronóstico sigue
  siendo lineal aun cuando tau no lo es.
- Por separado d=1/2/3/4 para distinguir
  error de suavidad frente a error de clase
  de extrapolación.
- h={1,3,6,12} cuando existe historia suficiente:
  contrastar error por lead k, no solo MSE global.
- Misma forma tau / semilla / h /
  d / L con varios niveles sigma:
  aislar el aumento de ruido observacional.
- Errores iid frente a AR(1), t5 y
  heterocedásticos para probar robustez a
  especificación \(V=I\).

## 4. Simulación C: cambios temporales

8 mecanismos C × N {240,400} ×
sigma {.25,.8} × 4 ruidos = **128 celdas**.
Control de forma estable, cambio
abrupto de pendiente, cambio de
curvatura, curvatura gradual,
cambio de varianza, régimen transitorio,
dos cambios de régimen.
Esta prueba del Paper 1 analiza si
**ponderar F reciente** ayuda al
pronóstico o aumenta varianza cuando
la serie es estable.

## 5. El procedimiento de forecasting a dibujar

Dado un origen operacional T elegido sin
mirar las últimas observaciones:
1. Con datos \(y_{\le T}\), localizar
   orígenes \(t_q+h\le T\) y ajustar
   siempre L observaciones previas.
2. Para cada S, calcular
   \(G_{d,h}H(S)y_{t_q-L+1:t_q}\)
   y su MSE frente a los h posteriores,
   ya realizados para aquel origen.
3. Agregar funciones según m y minimizar
   el F más reciente completo.
4. Refitear sobre \(y_{T-L+1:T}\).
5. Extender a T+1,...,T+h y **entonces**
   dibujar/medir y futuro.
6. En simulación, dibujar en otra capa
   la \(\tau\) verdadera pasada y
   futura; queda prohibido usarla
   para ajustar S.

**Nunca** dibujar un suavizado que usa
y_{T+1:T+h} y titularlo
«forecast fuera de muestra».
Si se muestra un suavizado global
retrospectivo, marcarlo como
reconstrucción descriptiva.

## 6. Plan concreto de figuras (no elegir solo ganadores)

**Figura 1. «De tau a observaciones».**
Misma forma generadora \(\tau_t\) en
tres columnas de \(\sigma\) bajo la
misma distribución de ruido y una
semilla fijada antes de ver la salida.
Trazar \(\tau\) continua, \(y\) tenue
y, si corresponde, \(\tau+\xi\)
con leyenda distinta. Cada panel debe
indicar sigma, N, forma y seed.
Repetir una fila lineal, cuadrática,
cúbica o Beta según espacio del paper.

**Figura 2. «Estimación, no solo F».**
Mismos datos de Figura 1; superponer
\(\hat\tau\) seleccionada por
pooled uniforme, weighted reciente,
CV/GCV/AICc/BIC y S fijo razonable.
Separar izquierda (última ventana L)
y derecha (futuro h); línea vertical
de origen T. Mostrar tau verdadera
en ambos periodos. Limitar curvas
por panel para evitar 10 superposiciones;
usar small multiples con ejes comunes.

**Figura 3. «Cómo se elige S».**
Mostrar individual \(\ell_{t_q}(S)\)
en gris, \(\bar F\) uniforme y
F reciente con colores diferenciables,
mínimos respectivos, S normalizado
y edf. Acompañar con heatmap origen×S.
NO graficar ramas (eso es Paper 2).

**Figura 4. «S contra h/d».**
Distribución de \(\hat S_{T,m,d,L,h}\)
sobre semillas, con bandas/violines
y proporción de extremos; separar
d=2 base y estudio de órdenes.
Mostrar d/h de forma legible.

**Figura 5. «Error de forecast vs
recuperación».**
Dispersión o curvas por escenario de
MSFE observado contra error de
\(\hat\tau\) pasada, con íconos
para método y tamaño de muestras;
línea de diferencia/oráculo
solo si está correctamente etiquetado.

**Figura 6. «Ganancias y pérdidas».**
Forest plot del contraste **pareado**
\(E^{method}-E^{uniform}\) por forma
y ruido, con 95% CI a nivel seed;
incluir controles negativos,
outliers y fallos.

**Figura 7. «Horizonte mal alineado».**
Comparar selector entrenado en
h=1 y usado para pronóstico h>1
con selector entrenado al mismo
h del test. Separación de h es
indispensable para una afirmación
específica sobre horizon matching.
**Ablación aún debe implementarse**
en la nueva campaña si no figura
en el código actual.

## 7. Tablas por publicar: definición, no números inventados

- T1: ecuaciones DGP y celdas, N/L/d/h,
  ley de ruido, S-grid/optimizador, seeds.
- T2: reproducción fiel del 2^4
  (S Guerrero, S normalizado, EDF,
  efectos factoriales) por CV/GCV/AICc/BIC.
- T3: MSFE/RMSE y latente future/past
  vs métodos, con IC pareado; distinguir
  entre 16 celdas source, 384 B, 128 C.
- T4: S/EDF y extremos vs forma/ruido/h.
- T5: significancia/interacciones
  forma×d, ruido×m, régimen×m,
  condicionadas a comparaciones predefinidas.
- Apéndice: grilla de todas las
  formas/ruidos y casos no favorables.

## 8. Salidas reales del repositorio y lo que NO hacen

\`simulation_dgps.py\` genera y almacena
componentes verdaderos.
\`simulation_evaluation.py\` mide errores
observados, latentes y criterios S/EDF;
\`run_simulation_campaign.py\` produce
SQLite reanudable, no figuras finales.
\`analyze_simulation_campaign.py\`
produce resúmenes por factores y
contrastes pareados.
\`inspect_simulation_case.py\` regenera
los datos y matrices \(F\) de un caso
y opcionalmente un HTML básico.
**Todavía falta** un generador de
figuras de publicación automático
para las siete figuras arriba,
su selección predeclarada de casos
representativos, y una validación
de extremo a extremo del ensayo.
No decir que todas estas figuras
están ya construidas.

## 9. Lectura correcta de los resultados

«MSE menor en la media de F» es
pérdida de entrenamiento/selección,
**no** prueba de superioridad futura.
Si el modelo logra pequeña
recuperación de tau pero gran
MSFE, discutir error de
extrapolación; si pronostica y
bien pero tau mal en presencia
de ruido/estacionalidad, distinguir
objetivos. Mostrar que se
pierde frente a S fijo o BIC
cuando ocurra. Evitar afirmar
que un estudio factorial con
múltiples celdas demuestra
uniformidad de resultados.

**Situación al escribir estas
notas:** atlas prospectivo.
La campaña nueva debe ejecutarse,
auditarse y analizarse antes
de redactar la sección Results.
