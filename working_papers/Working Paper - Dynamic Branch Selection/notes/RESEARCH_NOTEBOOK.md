# Paper 2 · Cuaderno científico: ramas de mínimos locales de F ponderada

**Actual: 2026-10-09 · Notas, NO paper final.**
Ruta de estudio: [libro de demostraciones](PROOF_LEDGER.md),
[atlas de simulación y figuras](SIMULATION_ATLAS.md),
[protocolo del algoritmo](dynamic_tracked_smoothness.md),
[evidencia histórica](results_and_boundaries.md).
Ver también [formulación común](../../WEIGHTED_SURFACE_PROTOCOL.md).

## 0. Pregunta en una frase

Dado que una función de error de pronóstico
\(F_r(S)\) puede tener **varios mínimos locales**,
¿podemos obtener información para escoger la
suavidad de mañana siguiendo **la evolución
temporal de esos mínimos** en lugar de
escoger siempre el mínimo global del último F?

Una rama NO es una tendencia económica,
una fuente causal o un estado de Markov
ya identificado. Es **una asociación matemática
y algorítmica de mínimos locales** de
funciones F sucesivas.

## 1. Delimitación frente al Paper 1 y versión histórica

**Paper 1:** una sola decisión
\(\widehat S_T^{pool}=\arg\min_S F_M(S)\).
No necesita identificar el mismo valle ayer
o la semana anterior.

**Paper 2:** para cada combinación
**fijada antes** \((m,d,L,h)\), conserva
las secuencias de funciones
\[
F_1^{(m,d,L,h)},\ldots,F_M^{(m,d,L,h)}
\]
y sus mínimos \(\mathcal M_1,\ldots,\mathcal M_M\);
intenta inferir qué mínimos persisten
y si el resultado puede ser una mejor
decisión operativa de S.

**No confundir con CP04–CP08:** los
experimentos históricos usaron
variantes Val1/Val2 y/o transformaciones
de S dentro de la función de pérdida.
Esa variante NO es el diseño actual.
El método nuevo no exige una Val2
interna: sí exige **outer test**, pues
puntuar en F histórico no es prueba
de mejor predicción posterior.

## 2. Empezamos con exactamente las mismas funciones

Para datos disponibles \(y_{1:T}\),
ventana L, orden d y horizonte h:
\[
\ell_{t_q}(S)=\frac1h
\|y_{t_q+1:t_q+h}-
G_{d,h}H_{d,L}(S)y_{t_q-L+1:t_q}\|^2
\]
con \(t_q+h\le T\).
El método m define qué folds completados
y qué pesos temporales
\(w_{r,q}^{(m)}\ge0\) usamos:
\[
\boxed{
F_r^{(m,d,L,h)}(S)
=\frac{\sum_{q\in I_m(r)}
w_{r,q}^{(m)}\ell_{t_q}(S)}
{\sum_{q\in I_m(r)}w_{r,q}^{(m)}}.
}
\]

**Primero ponderamos las FUNCIONES de error.**
Luego encontramos los mínimos de cada
F_r. No elegimos un S usando la
tendencia \(\tau\) simulada ni
promediamos S antes de F.
Distintos m y d pueden producir
cantidades de mínimos distintas,
pero NO se impone que siempre
existan varias ramas.

## 3. ¿Qué es exactamente un mínimo y qué es una rama?

Con \(F_r:[0,1]\to\mathbb R\):
\[
\mathcal M_r=\operatorname{LocalMin}
F_r,
\]
incluyendo extremos unilaterales
S=0,1 cuando corresponda.

La versión ideal ubicaría raíces de
\(F'_r(S)=0\) con pruebas
de curvatura y límites; nuestro
piloto actual registra **mínimos
candidatos de una grilla**.
No escribir que descubre
matemáticamente TODOS los valles.
Esto depende del Paper 3.

Una rama \(V_j\) es una lista
cronológica de puntos seleccionados
por el algoritmo de correspondencia:
\[
V_j=\{(r,t_r,S^*_{j,r},
 F_r(S^*_{j,r}))\}_{r\in\mathcal T_j}.
\]
La secuencia solo contiene un
mínimo por paso de esa rama;
puede nacer y terminar.

## 4. ¿Cómo seguimos una rama sin mirar el futuro?

En cada r observamos \(\mathcal M_r\),
calculamos distancias de S contra
los mínimos activos de r-1,
descartamos parejas con
\(|S^*_{r}-S^*_{r-1}|>\varepsilon\),
y resolvemos correspondencias **uno a uno**
priorizando el mayor número de
emparejamientos admisibles y
después menor distancia total.

- Emparejada: misma etiqueta de rama.
- Nuevo mínimo sin pareja: crear rama.
- Rama previa sin pareja: darla por
  terminada; si vuelve a aparecer
  después puede ser etiqueta nueva.
- Cruce de ramas, mínimo doble o empate:
  la identidad no es inequívoca;
  guardar diagnóstico de ambigüedad.

**El radio epsilon es una elección del
algoritmo, no una ley natural de F.**
Debe examinarse por sensibilidad y
escogerse fuera del test.

## 5. ¿Por qué tendría sentido el tracking?

Si al actualizar F con un nuevo
fold la perturbación de sus
derivadas es pequeña y un mínimo
interior tiene curvatura
estrictamente positiva, se puede
motivar una rama local continua:
los mínimos no cambian arbitrariamente
mientras se conserve la regularidad.
Esto viene del principio de
función implícita / estabilidad
local de raíces: **no prueba** que
todo F histórico sea tan regular,
que las ramas duren siempre o que
el mínimo seguido sea predictivo.

Si el ruido crece, hay saltos en
el DGP, el mínimo se hace casi plano
o cambia el número de valles,
la correspondencia puede fallar.
Registrar esos casos es tan
importante como los éxitos.

## 6. ¿Cómo convierte una rama en un pronóstico?

El tracking genera **candidatos**,
no el pronóstico final.
Necesitamos distinguir dos reglas
fijadas antes del outer test:

1. \(\psi\): escoger rama entre las
   activas mediante información de
   F histórico y soporte. El piloto
   puntúa el error reciente de
   cada rama evaluando el S
   operativo producido en cada
   paso histórico (sin Val2).
2. \(\phi\): convertir los últimos
   mínimos de la rama elegida en S
   operativo. Primer diseño:
\[
\boxed{
\phi_{\mathrm{mean3}}(V_j)
=\frac1{\min(3,n_j)}
\sum_{k=0}^{\min(3,n_j)-1}
S_{j,\mathrm{último}-k}^*.
}
\]
Un soporte de menos de tres usa
los disponibles, si la política
permite esa rama. La política de
soporte selecciona preferentemente
ramas activas con suficientes
observaciones; si no existen,
hay fallback documentado.

Finalmente:
\[
\widehat y_{T+1:T+h|T}^{track}
=G_{d,h}H_{d,L}(\widehat S_T^{track})
\,y_{T-L+1:T}.
\]

La \(\phi\) media tres S después
de identificar \(V_j\). NO
modifica la geometría de F_r;
la ponderación m sí puede cambiarla.

## 7. Un experimento crucial para demostrar valor añadido

Fijemos una misma y simulada,
**el mismo m**, d, L, h,
los mismos orígenes históricos
y el mismo outer test. Calculamos:

- pooled: \(\arg\min F_M^{(m)}\);
- dynamic: \(\psi\) entre ramas
  de \(F_1^{(m)},\ldots,F_M^{(m)}\)
  y \(\phi(V_{\hat j})\).

Comparamos MSE observado futuro,
MSE futuro de tau, recuperación
de tau pasada, S/EDF y variabilidad.
Esto evita atribuir a tracking
una mejora causada solamente por
dar mayor peso al pasado reciente.

Incluir controles:
- un F con **un solo mínimo**:
  registrar si tracking se
  reduce a una regla de filtrado
  de S que puede empeorar;
- régimen estacionario: no
  presumir ventaja;
- cambio de pendiente/curvatura
  reciente: posible caso favorable;
- ruido muy alto, F casi plano:
  puede crear ramas espurias;
- múltiples mínimos cercanos:
  ambigüedad de correspondencia.

## 8. Papel de las simulaciones

Usamos las mismas 16 celdas A +
384 formas B + 128 regímenes C
preparadas para Paper 1, con
réplicas/observaciones idénticas
para comparación pareada.
La simulación revela la
tendencia verdadera **solo a
quien evalúa**:
\(y_t=\tau_t+\xi_t+\varepsilon_t\).

El Paper 2 agrega diagnósticos
por m y d: cantidad de mínimos
por F, nacimientos/muertes,
longitud/curvatura de ramas,
saltos en S, soporte al elegir,
frecuencia de fallback y
sensibilidad a epsilon/resolución.
La campaña actual solo almacena
algunos recuentos y soporte;
el atlas distingue los demás
como instrumentos pendientes.

## 9. Figuras científicas imprescindibles

Ver [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md).
En la figura central recomendamos
filas por forma de tendencia y
columnas por nivel de ruido:
primer panel tau/y; segundo
F_r como heatmap origen×S con
mínimos; tercero ramas coloreadas
por ID; cuarto las tendencias
resultantes y pronóstico
outer de pooled vs tracking,
con T marcado.

Este panel debe mostrar tanto
**un caso con varias ramas como
uno con un único mínimo**,
sin que el lector crea que la
multiplicidad está garantizada.

Las figuras de robustez deben
mostrar fallos de matching, no
simplemente excluirlos.

## 10. Riesgos de interpretación y teoría pendiente

- Continuación matemática local
  de una raíz no equivale a
  continuidad de régimen económico.
- Branch score in-sample puede
  seleccionar un ganador que
  no repite desempeño fuera.
- La media de S de tres pasos
  no es derivada de una teoría
  predictiva óptima: es la regla
  inicial que debemos falsar.
- No existe garantía de
  identificación en cruces.
- Una grilla de 161 S puede
  perder mínimos estrechos.
- Múltiples métodos m y radios
  epsilon implican multiplicidad
  de comparaciones; no elegir
  retrospectivamente el mejor
  en el mismo outer test.
- Los CP04–CP08 dieron resultados
  mixtos/adversos al tracking
  anterior y **no validan el
  método nuevo**.

## 11. Esqueleto eventual del manuscrito

1. Por qué un selector de suavidad
   tradicional descarta la historia
   de los mínimos.
2. F ponderada, notación y
   diferencia matemática de Paper 1.
3. Mínimos locales, estabilidad
   condicional, matching, \(\psi\),
   \(\phi\), límites al identificar.
4. Control de errores numéricos
   y sesgo de selección temporal.
5. Simulación compartida con
   énfasis en persistencia y
   cambios de régimen.
6. Comparación **pareada**
   tracking vs global F y
   breakdown por escenarios.
7. Aplicaciones y por qué algunos
   resultados pueden ser negativos.
8. Apéndice: estabilidad local,
   cambios de cardinalidad,
   sensibilidad a epsilon.

No redactar conclusiones
de ganancia general ni material
de abstract antes de correr el
protocolo nuevo. GPU secundaria.
