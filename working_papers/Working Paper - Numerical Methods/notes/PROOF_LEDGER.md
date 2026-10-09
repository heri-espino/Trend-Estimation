# Paper 3 · Teoría y derivaciones numéricas verificables

**Estados:** [CLÁSICO], [DERIVADO],
[PENDIENTE] y [HIPÓTESIS].
Ejemplos exactos con
raíces certificadas
están en [sturm_minicheck.md](sturm_minicheck.md).

## N1. La inversión PLS no introduce polos admisibles
**[CLÁSICO, DERIVADO]**
Sea \(Q=D_d^\top D_d\succeq0\).
Para todo \(\lambda\ge0\),
\(z^\top(I+\lambda Q)z=
\|z\|^2+\lambda\|Dz\|^2>0\)
si z≠0. Por tanto
\(I+\lambda Q\) es
invertible y
\(\det(I+\lambda Q)>0\).
En particular el
mapa racional H
no tiene polos
en [0,∞).

## N2. Estructura racional de la pérdida
**[DERIVADO]**
Para dimensión L fija,
por fórmula de inversa
\[
H_\lambda
=\frac{\operatorname{adj}
(I+\lambda Q)}
{\det(I+\lambda Q)}.
\]
Cada entrada del
numerador y del
denominador es
polinomio en lambda
(si Q es matriz fija
finita). Así cada
componente de
\(GH_\lambda x\)
es racional.
Cada componente de
\(z-GH_\lambda x\)
también es racional;
cuadrados y sumas
con pesos fijos
son racionales.
Luego:
\[
F(\lambda)=A(\lambda)/B(\lambda),
\quad F'(\lambda)
=\frac{A'B-AB'}{B^2}.
\]
Tras simplificación,
el numerador
\(P(\lambda)\)
es un polinomio.
Si \(P\not\equiv0\),
hay un número finito
de raíces aisladas
positivas (contando
multiplicidades finitas)
y se pueden clasificar
sus estacionarios.
**Si \(P\equiv0\)**,
F es constante en
el dominio conexo:
todos los puntos
interiores son
estacionarios y
la finitud falla.
Esto puede ocurrir
en casos degenerados,
así que NO omitirlo.

Para determinar
raíces **exactamente**,
se requieren
representaciones
aritméticas exactas
de datos y operadores,
por ejemplo
coeficientes racionales.
Para matrices con
entradas float
solo hay aproximación
numérica a esa
estructura.

## N3. Derivar la inversa sin memorizar fórmula
**[CLÁSICO, DERIVADO]**
Partimos de
\((I+\lambda Q)H=I\).
Derivar:
\(QH+(I+\lambda Q)H'=0\).
Multiplicar a izquierda
por H:
\[
H'=-HQH.
\]
Derivar el lado
derecho:
\[
H''=-H'QH-HQH'
=HQHQH+HQHQH
=2HQHQH.
\]
Como Q conmuta
con H (ambos son
funciones del mismo
Q diagonalizable),
por inducción
\[
\boxed{H^{(n)}
=(-1)^nn!H(QH)^n.}
\]
Conmutable permite
reescrituras,
pero no hace falta
confundir multiplicación
matricial y productos
escalares.

## N4. Derivada de MSE h-step
**[DERIVADO]**
Sea \(p(\lambda)=GHx\),
\(r(\lambda)=z-p\).
\[
\ell(\lambda)=\frac1h r^\top r,\quad
r'=-p'.
\]
Derivar:
\[
\ell'=\frac1h(2r^\top r')
=-\frac2h r^\top p'.
\]
Otra derivada:
\[
\ell''=-\frac2h(r'^\top p'+r^\top p'')
=\frac2h(\|p'\|^2-r^\top p'').
\]
Como G, Q y x
son constantes al
diferenciar,
\[
p'=G H'x=-GHQHx,\quad
p''=G H''x=2GHQHQHx.
\]
Con F combinación
ponderada independiente
de lambda, la
derivada conmuta
con suma finita.
Estos resultados
son reglas clásicas
de cálculo matricial,
no una «nueva»
identidad original.

## N5. La cadena S↔lambda
**[DERIVADO]**
Para lambda>0 finito:
\[
S'(\lambda)=\frac1{L-d}
\sum_{\delta_j>0}
\frac{\delta_j}
{(1+\lambda\delta_j)^2}>0,
\]
\[
S''(\lambda)=-\frac2{L-d}
\sum_{\delta_j>0}
\frac{\delta_j^2}
{(1+\lambda\delta_j)^3}.
\]
Por \(dF/dS=(dF/d\lambda)/
(dS/d\lambda)\) se
obtiene
\[
F_{SS}=
\frac{F_{\lambda\lambda}S_\lambda-
F_\lambda S_{\lambda\lambda}}
{(S_\lambda)^3}.
\]
Como S' se hace
pequeño cuando
lambda crece,
esta división
puede estar
mal condicionada
cerca del extremo
S=1. Un método
numérico puede
preferir evaluar
directamente
límites o usar
una coordenada
alternativa.

## N6. Clasificación de estacionarios y extremos
**[CLÁSICO]**
Si interior S*,
\(F_S(S^*)=0\)
es condición necesaria
de mínimo
diferenciable.
\(F_{SS}(S^*)>0\)
es suficiente para
mínimo local estricto.
Si \(F_{SS}=0\),
la prueba de segundo
derivado no clasifica
por sí sola.
Los endpoints
pueden ser
mínimos unilaterales
sin derivada cero.
Global argmin en
compacto requiere
comparar F en
candidatos relevantes
**y en extremos**.
Detectar cambios
de signo de F'
NO garantiza hallar
raíces de multiplicidad
par o inflexiones
estacionarias.

## N7. ¿Qué permite la secuencia Sturm?
**[CLÁSICO, bajo datos exactos]**
Para polinomio real
con coeficientes
racionales exactos,
tras eliminar
multiplicidades
adecuadamente y
con extremos que
no sean raíces,
las variaciones
de signos de una
secuencia de Sturm
en a y b cuentan
raíces reales
distintas en (a,b).
Para nuestro P
no idénticamente
nulo, el conteo
positivo evalúa
variaciones en
0^+ e ∞.
El caso trabajado
L=6,d=2,h=2
en [sturm_minicheck.md](sturm_minicheck.md)
registra V(0+)=5,
V(∞)=2, y por
tanto 3 raíces
positivas para
**ese polinomio**.
No se sigue que
toda F tenga 3
raíces.

## N8. ¿Cuándo podemos certificar exhaustividad?
**[PENDIENTE para casos generales]**
Una malla uniforme
con K evaluaciones
puede omitir un
mínimo entre nodos.
Un buscador con
bracketing puede
omitir raíces que
no cambian de
signo. Un
algoritmo exhaustivo
requiere prueba
de que cada intervalo
no explorado carece
de raíces, por
ejemplo cotas
rigurosas de
derivadas/interval
arithmetic o
aislamiento
de raíces de P
en casos exactos.
**Los matches
2105/2105 con
una grilla densa
siguen siendo
validación empírica,
no el certificado.**

## N9. Condicionamiento / análisis por completar
**[HIPÓTESIS / PENDIENTE]**
Definir métricas
de dificultad como
\(\min |F_{SS}|\) en
mínimos simples,
distancia entre
raíces, distancia
a frontera,
magnitud de
residuos y
variación de h.
Probar cotas para
error en S y
regret de F
bajo errores de
ubicación de raíz
\(\hat S-S^*\).
Por Taylor, si
F'(S*)=0,
F'' es continua
y acotada localmente
\(|F''|\le C\),
entonces
\[
|F(\hat S)-F(S^*)|
\le\frac C2|\hat S-S^*|^2
\]
si el segmento
permanece en
esa vecindad.
**Esta cota local
clásica no justifica
errores de búsqueda
entre mínimos
globales diferentes.**

## N10. No confundir objetivos
Los «datos
generados con tau
conocida» permiten
comparar pronóstico/
recuperación de la
selección numérica.
La **verdad numérica**
de las raíces de
F no se obtiene de
conocer tau:
hace falta una
referencia exacta
o certificada de
F, o en su
defecto una
grilla densa
explícitamente
aproximada. Son
verdades distintas.

El paper debe
citar los hechos
clásicos y reservar
la contribución
real a garantías
nuevas bajo
hipótesis,
algoritmos
demostrablemente
mejores o
evidencia sólida
sobre geometría
específica de F.
