# Paper 3 · Atlas de pruebas analíticas, series sintéticas y figuras

**2026-10-09 · Incluye benchmarks históricos ya anotados y planes
nuevos sin ejecutarse.** Leer
[results.md](results.md),
[applied_case_studies.md](applied_case_studies.md)
y [sturm_minicheck.md](sturm_minicheck.md).

## Extensión experimental para objetivos F con nuevas series irregulares

El generador común de Papers 1 y 2 ahora incluye
un Study D de 720 formas/combinaciones más difíciles
(saltos, impulsos, chirps, outliers y dos clases de
tendencia latente estocástica). Son candidatos para
ampliar **después** el benchmark numérico de
\(F'(S)=0\), en especial raíces muy cercanas,
mínimos planos y cambios de curvatura.
El actual \`--preset mega --backend cuda\` calcula
*superficies de pérdida y decisiones de Papers 1/2*;
NO está conectado a la búsqueda de raíces
certificadas ni a la reproducción Sturm de Paper 3.
Esa integración es una tarea futura, explícitamente
separada de la presente campaña formal.

Al analizar futuros casos D en este paper,
mostrar \(\tau\) verdadero, y contaminado,
\(\hat\tau\) para S de mínimos distintos,
pronóstico h, funciones F y derivadas. Distinguir
verdad de \(\tau\) y verdad de raíces de F.

## Comparación numérica integrada en la simulación formal de ocho horas

El [protocolo conjunto](../../JOINT_FORMAL_8H_PROTOCOL.md)
toma una muestra predeclarada de las
**mismas funciones F ponderadas históricas**
sobre las que Papers 1 y 2 seleccionan
suavidad. En cada muestra compara:
grilla gruesa, refinamiento Brent acotado
por **cada valle local detectado** (más extremos
exactos) y búsqueda adaptativa de
raíces con derivadas analíticas.
La referencia de 401 puntos en S
es **numérica, no exhaustividad matemática**.

Cada candidato seleccionado produce
un **pronóstico externo de y y \(\tau\)**
y su error frente a \(\tau\) pasada,
para relacionar fallo numérico con
calidad de pronóstico/reconstrucción.
Un único ejemplo racional pequeño se
analiza con Sturm EXACTO, fuera
de las grandes series Monte Carlo;
no atribuimos a Sturm la
certificación de cada F grande.

El motor CUDA calcula pérdidas
de validación por lotes, mientras
Brent/derivadas/Sturm siguen en
CPU. La comparación CUDA/CPU
de velocidad NO se repite
durante la prueba formal.

## 1. Este paper necesita dos tipos distintos de simulación

**(I) Funciones de prueba con mínimos
conocidos por construcción.**
La verdad disponible es la
posición y tipo de cada
punto estacionario.
No necesitan proceder
de PLS. Miden
fiabilidad del
detector:
- mínimo único simple;
- dos mínimos
  próximos y de
  diferentes profundidades;
- mínimo muy plano;
- punto estacionario
  de inflexión
  (no mínimo);
- óptimo en frontera
  S=0 o S=1;
- mínimo muy cercano
  a S=1;
- raíces de derivada
  con paridad que no
  induce cambio de signo.
No declarar éxito
de «recuperación
completa de raíces»
si el algoritmo
solo busca mínimos.

**(II) Funciones F obtenidas
de series simuladas.**
Generamos
\(y_t=\tau_t+\xi_t+\epsilon_t\)
con tau conocida
(lineal, cuadrática,
cúbica, sinusoidal,
cambios de pendiente),
varios ruidos, L/d/h,
validación temporal
y F definida por el
pronóstico real.
La verdad de tau
NO determina
las raíces de F;
solo ayuda a
interpretar el
efecto práctico
de un mínimo
numérico correcto
o perdido.

Además: **(III) casos
aplicados observados**
(GDPC1, SPY, AAPL,
BTC-USD en
ensayos ya anotados)
sin tau latente
conocida, con
test reservado.

## 2. Serie latente y ruido: figura fundamental

Usar cuatro DGP
con ecuación y
semilla fijas:
- \(\tau_t=a+bt\):
  tendencia lineal
  de referencia.
- \(\tau_t=a+bt+ct^2\):
  curvatura/parábola,
  estudiar d=2 vs 3.
- \(\tau_t=a+bt+ct^2+et^3\):
  cúbica, estudiar
  d=2,3,4.
- \(\tau_t\) con
  pendiente que cambia:
  curvas de F y
  minimizadores
  potencialmente
  sensibles a h.

Para cada tau,
mantener mismo
tiempo/escala
subyacente,
mostrar \(\sigma\)
baja/media/alta,
p.ej. .25/.5/1
de la batería B.
Fijar sigma en
unidades definidas
y mostrar línea
tau, puntos y,
ajuste \(\hat\tau\)
en la ventana
y extrapolación
hasta T+h.
Panel con ruido
AR(1) o t5
separado de
ruido iid para
no cambiar dos
factores a la vez.

**Preguntar:**
¿el mínimo global
numérico correcto
corresponde a
una tendencia que
separe visualmente
ruido de señal?
¿Puede una
pequeña
diferencia en S
cambiar mucho el
pronóstico h largo?
¿Cuándo escoger
un valle falso/
perder un valle
material cambia
el error externo?

## 3. Matriz factorial para F_PLS

Los scripts históricos
en
\`experiments/numerical_smoothness_selection/\`
han probado varias
combinaciones de
orden d, largo L
y horizonte h
(incluyendo h largo
y d alto) bajo
DGP generados.
El nuevo ensayo
por planificar
debe añadir:
- grilla de
  \(d\in\{1,2,3,4\}\),
  \(L\in\{48,72,126,252\}\)
  cuando N disponible,
  \(h\in\{1,3,6,12,20\}\);
- N, curvatura de
  tau y \(\sigma\);
- ruido iid,
  AR1, Student-t5,
  heterocedástico;
- esquema F
  uniform vs
  weighted recent
  fijado, pues las
  derivadas
  combinadas usan
  pesos constantes;
- tolerancias,
  malla, depth y
  epsilon predefinidos;
- casos degenerados/
  extremales para
  refutar garantías
  demasiado amplias.

Una grilla tan
grande es
**propuesta**, no
combinación ya
implementada en
un runner único
ni justificación
para ejecutar un
producto cartesiano
sin objetivo.
Balancear factores
para poder
interpretar.

## 4. Qué comparamos exactamente

Algoritmos/candidatos:
1. búsqueda adaptativa
   en S con derivadas
   analíticas y
   cuidado de extremos;
2. grilla uniforme
   en S (referencia
   aproximada,
   compararla con
   varios K);
3. grilla en
   log-lambda
   con sus límites;
4. refinamiento
   Brent desde
   brackets;
5. conteo Sturm
   en casos
   racionales
   pequeños, exactos;
6. posibles
   algoritmos de
   aislamiento
   certificados
   si se logran
   implementar
   y demostrar.

**Medidas numéricas:**
- cantidad de
  estacionarios
  correctos/no
  correctos según
  verdad disponible;
- fracción de
  mínimos de
  referencia
  recuperados;
- error en
  posición de S,
  error en lambda
  (cuando finita),
  error de F y
  regret vs
  referencia;
- falsos mínimos,
  duplicados,
  clasificación
  equivocada;
- precisión
  fronteriza,
  tolerancia y
  raíces cercanas;
- número de
  evaluaciones de
  F/F'/F'',
  tiempo, fallos
  de convergencia;
- impacto de
  \(\hat S\) sobre
  recuperación
  de tau y
  pronóstico
  outer (cuando
  corresponde),
  sin usar el
  test para
  localizar raíces.

## 5. Figuras propuestas

**Figura 1. «Por qué F puede tener valles».**
Para una tau con
ruido bajo/alto,
mostrar tau,
y, 2–3 tendencias
\(\hat\tau\) en
mínimos locales
distintos de F
y sus diferentes
extrapolaciones
hasta T+h.
Panel de
F(S) con mínimos
señalados;
otra subfigura
de F_S cruzando
o tocando cero.

**Figura 2. «Límites de la grilla».**
Mismo F, grillas
de diferente
resolución y
búsqueda adaptativa;
ampliación alrededor
de S≈1, con
índice en ambos
ejes. Mostrar
al menos un
ejemplo histórico
en que hubo
fallo antes de
refinamiento, y
el diseño reparado.

**Figura 3. «Polinomio racional exacto».**
Instancia pequeña
L=6,d=2,h=2
con P(lambda),
conteo Sturm y
posiciones de 3
raíces positivas
(consultar la
derivación exacta
en sturm_minicheck).
Marcar qué raíces
son mínimos o
máximos, no
inferir 3 mínimos
por 3 raíces.

**Figura 4. «Geometría numérica contra horizonte».**
Heatmap/diagrama
de dispersión
de cantidad de
mínimos,
separación
mínima, cercanía
al extremo y
F'' local por
d,h,L y ruido.

**Figura 5. «Costo vs exactitud».**
Eje x: evaluaciones/
tiempo; eje y:
mínimos detectados
vs referencia y
regret. Facetas
por d y h;
intervalos por
semilla cuando
las unidades de
comparación
son independientes.

**Figura 6. «Aplicación real y test».**
Por cada familia
aplicada,
F(S) con
candidatos de
rango CV-1/2/3,
tendencias sobre
la misma ventana
y extrapolaciones
con test reservado.
Etiquetas de
ranking se
conservan como
CV-rank aunque
el ranking
test sea distinto.

## 6. Registro de resultados históricos disponibles

[results.md](results.md)
describe experimentos
históricos concretos:
- 1,920 superficies
  sintéticas,
  2,105 mínimos
  interiores de
  referencia densa
  emparejados
  (2,105/2,105);
- 240/240 mínimos/
  extremos relevantes
  en pruebas
  analíticas
  adversariales;
- 384 superficies
  financieras,
  473 mínimos
  de referencia
  densa emparejados;
- fallos previos
  de extremos y
  canonicalización
  de kernel
  documentados
  para entender
  el rediseño;
- miniexperimento
  exacto con
  3 raíces positivas
  contado por
  Sturm en una
  instancia, no
  resultado genérico.

**No promocionar
esos conteos a
garantía de todas
las raíces**.
No decir que
estos números
representan el
protocolo nuevo
ponderado m si
los escenarios
y código
anteriores no
lo utilizaban.

## 7. Tabla de resultados por crear

- T1: familia de F,
  construcción,
  d,L,h,K malla,
  supuestos
  e indicadores
  de verdad exacta
  vs referencia.
- T2: clase analítica
  × algoritmo,
  sensibilidad,
  mínimos encontrados,
  inflexiones
  recuperadas/no
  y frontera.
- T3: simulaciones
  F_PLS × d/h/L/
  ruido, costo,
  error de S/regret
  y raíz de referencia.
- T4: F local
  muy plano/casi
  doble/near-endpoint;
  tasas de
  fallo y
  remedios.
- T5: comparación
  de pronóstico
  entre dos
  mínimos locales
  **con el mismo
  modelo y outer
  test**, con
  inferencia
  prudente.

## 8. Estado de implementación y próximos ensayos

Actualmente:
\`src/trend_estimation/selection/smoothness_numerical.py\`
contiene un buscador
adaptativo;
\`run_synthetic_benchmark.py\`,
\`run_adversarial_benchmark.py\`,
\`run_financial_stress_test.py\`
y \`run_sturm_minicheck.py\`
producen pruebas
históricas
reproducibles;
la app
\`apps/numerical_methods.py\`
muestra F, derivadas
y candidatos
para un ejemplo.

**Falta para
afirmaciones más
fuertes:** garantizar
el alcance de
raíces detectadas,
crear las figuras
interpretativas
con tau/y a
distintos ruidos,
estudiar los
casos degenerate
y comparar con
certificación
exacta en más
configuraciones.
GPU es apoyo
de evaluación
de F, no
argumento de
corrección de
búsqueda.
