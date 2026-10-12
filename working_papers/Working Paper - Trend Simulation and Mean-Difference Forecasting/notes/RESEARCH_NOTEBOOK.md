# Research notebook · Forecasting trends with a nonzero mean difference

## 1. ¿Qué pregunta NO respondían los borradores anteriores?

Los primeros estudios asumían \(D_d\tau\approx0\), es decir,
penalizaban la diferencia d-ésima alrededor de cero.
El criterio de validación podía elegir \(S\), pero **no podía
alterar** el comportamiento de continuación impuesto
por el modelo: constante si d=1, lineal si d=2, cuadrática
si d=3. En presencia de aceleración continua o crecimiento
medio, escoger menor S no equivale a estimar explícitamente
el nivel central de las diferencias. El modelo de Guerrero
permite \(\mu\neq0\) y formula ese nivel de referencia.

## 2. Delimitación y atribución histórica

Guerrero (2007) propone
\[
\min_\tau \|x-\tau\|^2+
\lambda\|D_d\tau-\mu\mathbf1\|^2
\]
y un estimador plug-in de \(\mu\) basado en la media de las
diferencias observadas. **Nuestra hipótesis NO es que
esa idea o sus fórmulas sean nuevas.** Nos preguntamos si
\(\mu\) debe ajustarse mirando el desempeño **de pronósticos
históricos a horizonte h**, y qué propiedades tiene el
nuevo criterio perfilado \(F(S,\widehat\mu(S))\).

## 3. Modelo y estimador (paso lógico)

Sean \(Q=D_d^\top D_d\), \(H=(I+\lambda Q)^{-1}\).
Por la condición de primer orden:
\[
\widehat\tau=H x+\lambda\mu HD_d^\top\mathbf1.
\]
Sea \(p_j=\binom jd\), entonces \(D_dp=\mathbf1\) y
\(\lambda H D_d^\top\mathbf1=(I-H)p\).
Así,
\[
\boxed{\widehat\tau(S,\mu)=H(S)x+\mu[I-H(S)]p.}
\]

Es una representación numéricamente útil también en S=1.
La extrapolación no se debe calcular con un G «puro»:
\[
\boxed{
\widehat z(S,\mu)=
G_{d,h}\widehat\tau(S,\mu)+\mu g_{d,h},
}
\]
donde \(g_{d,h}(k)=\binom{k+d-1}d\).
Esto separa una parte sin μ y un vector multiplicador de μ.

## 4. ¿Por qué perfilar mu es posible?

Para cada origen histórico completado \(t_q\) obtenemos
\(\widehat z_q=a_q(S)+\mu b(S)\). Elegimos pesos
\(\widetilde w_q\) solo desde el pasado:
\[
F_T(S,\mu)=
\sum_q\widetilde w_q h^{-1}
\|z_q-a_q(S)-\mu b(S)\|^2.
\]
La pérdida es cuadrática en μ:
\[
F=A-2C\mu+B\mu^2,\qquad
\mu^*(S)=C/B\quad(B>0).
\]
Al sustituir:
\[
\boxed{\widetilde F_T(S)=A(S)-C(S)^2/B(S).}
\]
Luego minimizamos en \(S\in[0,1]\). Como ahora S
es el único parámetro de búsqueda no lineal, se pueden
reutilizar herramientas de mínimos locales y raíz estacionaria,
aunque **su geometría puede cambiar**.

## 5. ¿Cómo pronostica en producción?

En tiempo T:
1. Declarar d,L,h, pesos y familia de candidatos S **sin
   mirar observaciones futuras**.
2. Construir orígenes pasados completados \(t_q+h\le T\).
3. Para cada S calcular \(a_q(S),b(S)\);
   estimar μ(S) de los pseudo-futuros ya conocidos.
4. Comparar los tres selectores (μ=0, Guerrero, perfilado)
   usando exactamente los mismos pseudo-futuros y pesos.
5. Cada método selecciona su S minimizando **su** F.
6. Reajustar a \(y_{T-L+1:T}\), aplicar μ elegido:
   μ=0; media de diferencias de esa última ventana;
   o μ*(S) perfilada de histórico.
7. Pronosticar \(y_{T+1:T+h}\) antes de revelarlo.
8. Evaluar contra futuro observado y tendencia latente (solo
   en simulación), reportar recuperación de \(\tau\) pasada.

Si elegimos entre estas tres reglas observando el test exterior,
ese mismo test deja de ser confirmatorio. Se necesitan nuevas
semillas/periodos para confirmar.

## 6. ¿Por qué podría tener sentido?

Si d=1, μ controla la pendiente extrapolada, y
si d=2, μ controla la segunda diferencia y la
aceleración extrapolada. El futuro puede requerir un
nivel de referencia diferente del promedio del historial
si hubo cambios recientes. Pero perfilar μ sobre pocos
pseudo-futuros puede generar gran varianza y
extrapolaciones explosivas para h alto.
Tanto éxitos como fallos son parte del estudio.

## 7. Primera batería de simulaciones (no resultados)

Con \(\tau\) conocida, ruido bajo/medio/alto y misma
forma generadora, comparar:
- crecimiento lineal: ¿resuelve d=1,μ libre vs d=2,μ=0?
- curvatura cuadrática: ¿resuelve d=2,μ libre vs d=3,μ=0?
- cúbicas, no polinomiales, cambios de pendiente/curvatura;
- componentes de ruido iid, AR, t, heterocedásticos;
- h corto vs largo, L y peso reciente vs uniforme;
- medias estimadas μ frente a media verdadera de
  \(\Delta^d\tau\) como **diagnóstico, no entrenamiento**.

Métricas:
\[
R_{\rm past}=\tfrac1L\|\widehat\tau_{T-L+1:T}-\tau_{T-L+1:T}\|^2,
\]
\[
R_{\rm future,\tau}=
\tfrac1h\|\widehat z_{T,h}-\tau_{T+1:T+h}\|^2,
\quad
R_{\rm future,y}=\tfrac1h
\|\widehat z_{T,h}-y_{T+1:T+h}\|^2.
\]
El criterio de selección es el MSE histórico de **y**
observado, no un riesgo futuro de τ inaccesible.

## 8. Por qué este paper podría sustituir otros borradores, o no

El nuevo trabajo integra cuestiones de suavidad,
extrapolación y simulación con una decisión de μ que antes
no existía. Aun así, esta combinación podría estar
estudiada en smoothing/forecasting de modelos de tendencia;
sin una auditoría bibliográfica no sabemos su novedad.
Conservar provisionalmente los borradores anteriores permite
reutilizar pruebas clásicas, contrastes y fallos,
sin hacer afirmaciones prematuras de publicación.

## 9. Resultados de teoría/experimento que faltan

- Teoremas de regularidad y límites del perfilado cuando B se
  aproxima a cero.
- Relación precisa de EDF plug-in vs coordenada S.
- Derivadas analíticas y métodos numéricos para \(\widetilde F\).
- Tracking de ramas bajo perfilado, sin confundirlo con el caso μ=0.
- Riesgo poblacional/consistencia bajo dependencia y régimen cambiante.
- Comparación con Gupta/Guerrero/Whittaker/HP/forecasting-PPLS
  y otros antecedentes según referencias reales, no adivinadas.
- Experimentos out-of-sample ejecutados y reportados con
  semillas independientes; no hay aún cifras que sustenten mejora.

**Procedimiento editorial:** [NOTES_TO_MANUSCRIPT.md](../../NOTES_TO_MANUSCRIPT.md)
y [SIMULATION_ATLAS.md](SIMULATION_ATLAS.md) antes de revisar LaTeX.
