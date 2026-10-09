# Paper 3 · Cuaderno científico: geometría y recuperación numérica de mínimos de F(S)

**2026-10-09 · Documento previo al manuscrito definitivo.**
Comenzar con [resultados y pruebas](PROOF_LEDGER.md),
[simulaciones y figuras](SIMULATION_ATLAS.md),
[registros numéricos ya ejecutados](results.md),
[hipótesis/alcance](assumptions_and_claim_boundaries.md)
y [mini-certificado Sturm](sturm_minicheck.md).

## 0. Pregunta central

**Para una función ya fijada de pérdida de
pronóstico h-step \(F(S)\), ¿cómo localizar y
comparar correctamente todos sus mínimos
relevantes, incluidos S=0 y S=1, sin
confundir una grilla densa con una
prueba general de completitud?**

A diferencia del Paper 1,
aquí NO preguntamos cuál criterio
de validación es el mejor selector.
A diferencia del Paper 2,
NO seguimos una rama temporal
entre funciones sucesivas.
Este paper se concentra en
**una F fija, su geometría, sus
puntos estacionarios y la fiabilidad
del algoritmo de búsqueda**.

## 1. ¿Qué función es F y cuáles son los supuestos?

Con serie pasada de longitud L
en origen t,
\(x_t=y_{t-L+1:t}\),
pseudo-futuro histórico realizado
\(z_t=y_{t+1:t+h}\),
orden \(d\), horizonte \(h\),
suavizador \(H_\lambda=(I+\lambda
D_d^\top D_d)^{-1}\) y extrapolador G:
\[
\ell_t(\lambda)=\frac1h
\|z_t-G_{d,h}H_\lambda x_t\|_2^2.
\]
La F fija de estudio puede
ser una \(\ell_t\) sola o
un promedio de M folds
completados, uniformemente
o con pesos **predefinidos**
\(w_t\) constantes en lambda:
\[
F(\lambda)=
\sum_t\widetilde w_t\ell_t(\lambda),
\qquad
\sum_t\widetilde w_t=1.
\]
El objetivo en coordenada
S es \(F(\lambda(S))\) en
\([0,1]\), con S=1 como
límite exacto infinito.

Restricciones: PLS puro
\(V=I,\mu=0\), observaciones
equidistantes, L>d y
continuación polinomial
en orden d. No convertir
las hipótesis de cálculo
en supuestos universales
sobre independencia y ruido
de datos financieros.

## 2. ¿Por qué el problema no es simple minimización convexa?

El estimador de tau penalizado
tiene solución única para
lambda fijo (su Hessiano
es positivo definido).
Esto NO significa que la
función *externa*
\[
F(\lambda)=\frac1h\|z-GH_\lambda x\|^2
\]
sea convexa en lambda
o S. Cada modo espectral
se atenúa a ritmo
\((1+\lambda\delta_j)^{-1}\);
G puede amplificar
pequeñas diferencias
de pendiente/curvatura
hasta h pasos. Varias
componentes pueden
competir y producir
mínimos locales distintos
y candidatos cerca de S=1.

La cuestión no es
«¿cuál solver es más
rápido en un ejemplo?»,
sino detectar cuándo
un método **puede fallar**
por geometría, escala
o representación, y
con qué certeza identifica
los óptimos relevantes.

## 3. Derivadas sin aproximaciones por diferencia finita

Identidad estándar:
\[
H'_\lambda=-H_\lambda QH_\lambda,\qquad
H''_\lambda=2H_\lambda QH_\lambda QH_\lambda,
\quad
H_\lambda^{(n)}=(-1)^nn!H_\lambda(QH_\lambda)^n.
\]
Definiendo pronóstico
\(p=GH_\lambda x\) y
residual \(r=z-p\):
\[
p'=-GHQHx,\qquad
p''=2GHQHQHx,
\]
\[
\ell'=-\frac2h r^\top p',\quad
\ell''=\frac2h\bigl(\|p'\|^2-r^\top p''\bigr).
\]
Si F combina folds con
pesos fijos, agregar
derivadas de manera lineal.

Para 0<S<1:
\[
F_S=\frac{F_\lambda}{S_\lambda},
\qquad
F_{SS}=\frac{
F_{\lambda\lambda}S_\lambda-
F_\lambda S_{\lambda\lambda}}
{S_\lambda^3}.
\]
No calcular derivadas
en S=1 dividiendo por
un \(S_\lambda\to0\);
ese extremo debe
evaluarse por límite/
proyección exacta.

## 4. ¿Podemos saber cuántas raíces tiene F'?

**Estructura algebraica,
no novedad genérica:**
Para Q, G, x, z y pesos
**racionales/exactos**
fijos y L finito,
\((I+\lambda Q)^{-1}\)
es una matriz de
funciones racionales
en lambda (adjugata/
determinante), sin
polos para lambda≥0.
Por tanto F(\lambda)
y F'(\lambda) son
racionales. Tras
reducir:
\[
F'(\lambda)
=\frac{P(\lambda)}
{R(\lambda)},\quad
R(\lambda)>0
\text{ para }\lambda\ge0
\]
con P polinomio
(en representación
exacta). Los
estacionarios finitos
positivos corresponden
a raíces positivas P,
**salvo el caso
degenerado P≡0**,
donde F es constante
y toda lambda es
estacionaria.

Un conteo exacto de
raíces con Sturm
es posible para
instancias racionales
pequeñas; el costo
de álgebra simbólica
crece rápido.
No llamarlo solver
escalable general
ni asumir coeficientes
exactos para datos
IEEE float sin
construcción racional.

## 5. Estrategia numérica que estudiamos

**Referencia matemática ideal:** conocer
todos los estacionarios
del interior y candidatos
en extremos, evaluar F
en cada mínimo local/
extremo y seleccionar
el menor valor.

**Búsqueda implementada
adaptativa:** explorar
malla inicial en S,
examinar signos/
curvaturas de derivadas,
subdividir, usar Brent
en brackets apropiados,
refinar celdas próximas
a S=0 y S=1,
comparar endpoints
exactos y eliminar
duplicados según
tolerancia especificada.

**No confundir:**
- minimum de muestra en
  grilla con raíz exacta;
- bracket simple con
  todos los roots;
- mínimos con puntos
  estacionarios
  de inflexión;
- coincidencia con
  referencia densa con
  **teorema de
  completitud**;
- exactitud de una
  instancia Sturm con
  certificación de todas
  las series reales.

En una aplicación
relevante, registrar
\(\hat S\), \(F(\hat S)\),
todos los candidatos
hallados, distancias
a referencias, ratio
de evaluaciones y
fallos de delimitación.

## 6. ¿Por qué los endpoints merecen una sección propia?

\(S=0\) corresponde
a \(H_0=I\), sin
suavizado.
\(S=1\) corresponde
a proyección de
rango d, no a
una inversa de
\(I+\infty Q\).
Cuando lambda crece,
muchas raíces/cambios
en F pueden
comprimirse cerca de
S=1; una grilla
uniforme limitada
puede ignorarlos.
Además cerca de
lambda grande,
las direcciones
del kernel de Q
deben tener
autovalor exactamente
cero por
estructura, y
no solo "casi cero"
numéricamente.

Las notas [results.md](results.md)
registran una falla
histórica de raíces
perdidas cerca
del extremo y la
corrección de
normalizar el kernel
y refinar las celdas
de frontera. Mantener
el camino de
diagnóstico, no solo
las cifras finales.

## 7. Experimentos: tres niveles de verdad

**A. Funciones analíticas artificiales:**
objetivos construidos
con número/ubicación de
raíces y mínimos conocidos.
Sirven para detectar
errores del buscador,
inflexiones estacionarias,
raíces cercanas,
mínimos planos y
óptimos de frontera;
NO son F_PLS por
definición.

**B. Objetivos forecast-CV de
series sintéticas:**
generamos \(y=\tau+\xi+
\epsilon\) con tau
conocida y distintos
ruidos y h/d/L.
Construimos F **solo
desde y completada**.
La comparación numérica
usa grilla densa/
procedimiento exacto
solo cuando sea
factible; la tau
verdadera mide
recuperación
y muestra cómo
una elección
numéricamente errónea
afecta el pronóstico.
La grilla densa es
referencia **empírica**,
no verdad de raíces
certificadas.

**C. Objetivos de datos
aplicados:** series
públicas (GDP, ETF,
acción, BTC en
ensayos históricos)
con test reservado.
No se conoce tau;
reporte candidatos
y cambios de
pronóstico, sin
llamarlo «recuperación
de tendencia real».

## 8. Qué resultados están registrados, sin exagerarlos

En [results.md](results.md)
se documenta una
batería sintética
de 1,920 superficies
con 2,105 mínimos
interiores de
referencia densa
coincidentes (2,105/2,105)
y 240/240 mínimos/
extremos pertinentes
en ensayos
analíticos adversariales.
También se documenta
una prueba financiera
con 473/473
mínimos de referencia
densa asociados
en 384 superficies.
**Estos son matches a
referencias, NO
certificados de
todas las raíces de
todas las funciones F.**
El miniexperimento
Sturm para L=6,d=2,
h=2 cuenta
tres raíces positivas
en una instancia
exacta determinada.
No generalizar
por inducción
a dimensiones
arbitrarias.

## 9. Qué debe ver el lector

Ver [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md):
superponer \(\tau\),
y, tendencias
reconstruidas y
pronósticos resultantes
de **dos S que sean
mínimos locales
distintos de la
misma F**;
comparar ruido bajo/
medio/alto,
d y h, y dibujar
F(S), F_S y los
endpoints. Una
explicación visual
de por qué raíces
cerca de S=1
importan puede
ser más valiosa
que un solo
porcentaje de
concordancia
numérica.

## 10. Estructura tentativa del artículo

1. Problema de
   búsqueda de mínimos
   de una función
   h-step PLS,
   precedentes de
   búsqueda y PLS.
2. Estructura espectral
   y derivadas exactas
   (clásicas, citadas).
3. Condicionamiento/
   geometría de
   puntos estacionarios,
   límites y
   racionalidad finita
   bajo hipótesis.
4. Algoritmo adaptativo
   y sus límites,
   comparación con
   grilla/log-lambda/
   métodos analíticos.
5. Analíticos
   adversariales,
   simulaciones con
   tau conocida a
   varios ruidos
   y pruebas aplicadas.
6. Costo y fallos,
   no solo velocidad
   media; teoremas
   efectivamente
   probados.
7. Discusión,
   reproducibilidad,
   apéndices.

**Estado:** hay
evidencia numérica
histórica ya registrada;
al reusar el nuevo
F ponderado debe
verificarse
de nuevo la
equivalencia del
objetivo, los
pesos y los
extremos. No
fusionar esto con
el tracking
del Paper 2.
