# Paper 2 · Registro de teoría de mínimos y ramas

**[CLÁSICO]** resultado estándar; **[DERIVADO]** argumento
completo; **[HIPÓTESIS]** no demostrada para la familia;
**[PENDIENTE]** teoría o experimento pendiente.
No llamar «teorema nuevo» a la aplicación de
una herramienta clásica sin establecer novedad.

## D1. ¿Por qué cada F_r tiene minimizador, pero no necesariamente ramas?
**[DERIVADO]** Para configuración fija
\((m,d,L,h)\), F_r es continua en
[0,1] por la continuidad de
H(S) incluso en el límite de
proyección. Por Weierstrass,
cada F_r tiene al menos un
mínimo global. Esto NO asegura
más de un mínimo local ni que
los mínimos consecutivos tengan
posiciones cercanas. La existencia
de un mínimo por F no es la
existencia de una rama persistente.

## D2. ¿Cuándo persiste localmente un mínimo interior?
**[CLÁSICO, IFT]** Considérese
una familia suave \(F(S,u)\)
en un entorno de \((S_0,u_0)\),
con S_0 interior,
\[
\partial_S F(S_0,u_0)=0,\qquad
\partial_{SS}F(S_0,u_0)>0.
\]
Definamos \(g(S,u)=\partial_S F(S,u)\).
\(g(S_0,u_0)=0\) y
\(\partial_S g=\partial_{SS}F>0\).
Por el teorema de la función
implícita, hay entornos y una
función diferenciable \(S^*(u)\)
tal que \(g(S^*(u),u)=0\) y
\(S^*(u_0)=S_0\).
Por continuidad del segundo
derivado, en un entorno menor
\(\partial_{SS}F>0\), así la
raíz continúa como mínimo local.
Formalmente:
\[
\frac{dS^*}{du}
=-\frac{\partial_{Su}F(S^*(u),u)}
{\partial_{SS}F(S^*(u),u)}.
\]
**Limitación:** los índices r
son discretos. Para aplicar IFT
se requiere introducir una
interpolación regular entre
F_r y F_{r+1}, y comprobar
que su curvatura no se anula
en la trayectoria. No asumir
automáticamente que todas las
funciones rolling cumplen
estas hipótesis.

## D3. ¿Existe una cota de salto si la curvatura está acotada?
**[DERIVADO, bajo condiciones explícitas]**
Sean f,g diferenciables en
un intervalo I, y sea
a raíz interior de f' y b raíz
interior de g' en I.
Si f''(S)≥c>0 para todo
S entre a y b y
\(\sup_{S\in I}|f'(S)-g'(S)|\le\delta\),
entonces
\[
|b-a|\le\delta/c.
\]
**Demostración:** f'(a)=0,
g'(b)=0. Por hipótesis,
\(|f'(b)|=|f'(b)-g'(b)|
\le\delta\).
El teorema del valor medio
da \(f'(b)-f'(a)=f''(\xi)(b-a)\)
para algún \(\xi\) entre a,b.
Su valor absoluto es ≥c|b-a|,
por tanto la desigualdad.
**No afirma existencia de b**:
solo acota distancia *si*
dos raíces existen en el
mismo intervalo de curvatura.

Interpretación: un radio fijo
epsilon no puede ser universal
cuando la curvatura de un valle
se aproxima a cero o la
perturbación de F' aumenta.
Anotar curvatura mínima y
cambio de derivada observado
como diagnósticos futuros.

## D4. ¿Por qué un mínimo puede nacer o desaparecer?
**[CLÁSICO, ejemplo construido]**
Considérese
\(f_u(S)=(S-a)^3/3-u(S-a)\)
en vecindario de a interior.
\[
f'_u(S)=(S-a)^2-u.
\]
Si u<0 no hay raíz interior.
Si u=0 hay una raíz degenerada
con \(f''=0\).
Si u>0 nacen dos raíces
\(S=a\pm\sqrt u\): un máximo
y un mínimo, respectivamente.
Esta es una ilustración
de bifurcación local **general**,
NO una afirmación de que la
pérdida PLS necesariamente
admita este polinomio.
Una construcción realizable
en F_PLS y su clasificación
es una cuestión de estudio.

## D5. ¿Cuándo es correcto emparejar ramas por distancia?
**[PENDIENTE / DECISIÓN ALGORÍTMICA]**
La regla actual prioriza
máximo número de enlaces
dentro de distancia ≤epsilon,
después mínimo costo total.
Puede emparejar consistentemente
si hay separación suficiente
entre posiciones de distintos
mínimos y movimientos pequeños,
pero **no** se garantiza esa
separación en general.
Demostrar una condición suficiente
de matching único sería posible,
por ejemplo cuando cada mínimo
r-1 tiene un único candidato
r a distancia <epsilon,
y esos candidatos son distintos.
Si existen dos emparejamientos
válidos del mismo costo, la
etiqueta no identifica una
trayectoria matemática única.
Registrar ambigüedad y
casos con cruces.

## D6. ¿Los pesos recientes cambian las ramas?
**[DERIVADO EN PRINCIPIO, EFECTO EMPÍRICO]**
Cambiar m cambia
\(F_r=\sum w^{(m)}_{r,q}\ell_q\).
Como sus derivadas son
\(F'_r=\sum w^{(m)}_{r,q}\ell'_q\),
las raíces y curvaturas de F
pueden cambiar. Pero si
todas las \(\ell_q\) tienen
mínimo único en el mismo S
y son estrictamente convexas,
cualquier promedio positivo
comparte el mismo minimizador.
Por tanto NO es cierto que
cada método m necesariamente
cree nuevas ramas.
El impacto real de m/d
debe medirse sobre DGP variados.

## D7. ¿Por qué «escoger la menor F histórica» no equivale a elegir la mejor rama?
**[DERIVADO COMO DISTINCIÓN ESTADÍSTICA]**
La pérdida interna F_r(S) se
calcula con pseudo-futuros
históricos completados y se
usa en la función de decisión
\(\psi\). El riesgo de prueba
se calcula en nuevo origen T
y horizonte futuro.
No son los mismos datos ni
la misma esperanza condicionada.
La desigualdad
\(F_r(S_a)<F_r(S_b)\)
no implica
\(E_{\mathrm{test}}(S_a)<
E_{\mathrm{test}}(S_b)\).
Construir contraejemplos de
régimen nuevo y ruido fuerte
para explicar discrepancias.
Evitar doble uso de test
para elegir \(\psi,\phi,m,d\).

## D8. ¿Qué propiedades de \(\phi\) son automáticas?
**[DERIVADO]** Si una rama j
tiene n≥1 mínimos en [0,1],
su media de los últimos
\(\min(3,n)\) está en [0,1],
por convexidad del intervalo.
Eso garantiza **admisibilidad**,
no optimalidad.
No hay prueba de que la
media de tres sea preferible
al último mínimo, mediana,
tendencia pronosticada o
mínimo global pooled.
Es el baseline operativo
que requieren simulaciones.

## D9. Teoría abierta y condiciones a buscar
**[HIPÓTESIS / PENDIENTE]**
- ¿Con qué regularidad las
  pérdidas F_PLS admiten
  múltiples mínimos interiores?
- ¿Qué geometría de F permite
  continuar una rama evitando
  intercambios?
- ¿El ratio perturbación/
  curvatura predice errores
  de correspondencia?
- ¿Qué relación existe entre
  persistencia y buen riesgo
  futuro, si el DGP tiene
  régimen persistente?
- ¿Puede el tracking empeorar
  sistemáticamente en un DGP
  estacionario donde weighted
  pooled ya usa toda información?
- ¿Cómo controlar la frecuencia
  de falsos nacimientos en
  grillas finitas?

Las proposiciones de D2-D4 son
herramientas clásicas generales;
**no bastan por sí solas
para una contribución original
sobre pérdidas PLS**.
