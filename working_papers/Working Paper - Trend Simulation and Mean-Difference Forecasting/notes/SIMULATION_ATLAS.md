# Atlas de simulación · Tendencia verdadera, ruido y media de diferencias

**Estado: PRE-REGISTRO EXPLORATORIO, sin resultados calculados**
(2026-10-11). Cualquier tabla/gráfica futuro debe indicar
escenario, ecuación, L,d,h, pesos, semilla y fecha/código.

## 1. Preguntas empíricas independientes

1. ¿Qué tanto separa \(\widehat\tau\) de \(\tau\) la
   penalización con $\mu$ fijada o estimada?
2. ¿El mejor S para recuperación pasada coincide con
   el S que minimiza pérdidas h-step de **y**?
3. ¿Tiene μ perfilada menor error futuro observado o
   mejor error frente a la tendencia latente futura?
4. ¿Se preservan los beneficios si aumenta h o cambia d?
5. ¿Cuántos mínimos tiene la función concentrada
   \(\widetilde F_T(S)\) y qué sucede con su curvatura?
6. ¿Cuándo perjudica μ perfilada el pronóstico por
   inestabilidad de extrapolación o sobreajuste histórico?

## 2. Generación y variables visibles

En cada DGP/semilla:
\[
y_t=\tau_t+\xi_t+\varepsilon_t,\quad t=1,\dots,N.
\]
La generación almacena por separado
\(\tau,\xi,\varepsilon,y\).
Los modelos **solo reciben y** durante selección; $\tau$
se usa para score, gráficos y **oráculos de diagnóstico**.
Si $\xi\ne0$, comparar error contra $\tau$ y
contra $\tau+\xi$; el pronosticador actual no
ajusta una estacionalidad explícita.

## 3. Baterías sugeridas (y por qué)

**A. Control de Guerrero / grados polinomiales:**
\(\tau_t=a+bt\) (d=1 puede mejorar con μ≠0),
\(\tau_t=a+bt+ct^2\) (d=2 puede mejorar con μ≠0),
\(\tau_t=a+bt+ct^2+et^3\) (d=3 puede mejorar
con μ≠0). Incluir d incorrecto para separar
estructura de suavidad. Generar misma τ bajo
σ baja/media/alta (p. ej. 0.25, 0.5, 1).

**B. DGP fuente (NO inventar cifras):**
Guerrero (2007) usa ejemplos reales y
Cortés-Toto et al. estudian selección de λ/S con
modelos y factoriales propios. Su reproducción
fiel usa full-N y permanece separada del nuevo
forecast-CV; reutilizar sus DGP no equivale a
reproducir sus resultados de pronóstico.

**C. Robustez:** pendiente que cambia, pulso de
curvatura, salto de nivel, sigmoide, sinusoidal,
tendencia latente estocástica, ruido iid/AR1/t5,
heterocedasticidad y contaminaciones raras.
μ común en el historial puede ser inadecuada
tras un cambio, por lo que incluir controles
negativos y fallos.

## 4. Tres reglas exactamente comparables

- \`zero\`: \(\mu=0\), elegir S usando
  pérdidas históricas h-step.
- \`guerrero\`: dentro de cada ventana de
  entrenamiento histórica, estimar
  \(\mu_q^G=\mathrm{mean}(D_dx_q)\);
  elegir S usando pérdidas h-step;
  en el origen final estimar
  \(\mu_T^G\) **solo del tramo final de y**.
- \`profile\`: para cada S, estimar
  \(\widehat\mu(S)\) con todos los folds históricos
  completados y pesos m normalizados;
  elegir S de la función concentrada.
  En T usar la misma μ seleccionada.

**No mezclar** con el cuarto procedimiento
\(\min_{\tau,\mu}\) de la penalización in-sample
sin identificarlo como otra familia.

## 5. Separación histórica / validación

Con y conocida hasta T, ventana L y h:
para cada \(t_q+h\le T\) tomar \(x_q\) de
L observaciones previas, estimar la tendencia
y emitir h pronósticos. Elegir S y μ sin
revelar \(y_{T+1:T+h}\).
Reajustar sobre últimos L de y[:T], pronosticar
h, evaluar fuera. Repetir a múltiples T y con
semillas independientes.

## 6. Métricas y seguimiento de tendencia

**Pasado:**
\[
R_{\rm past}=\frac1L\sum_{j=T-L+1}^{T}
(\widehat\tau_{j|T}-\tau_j)^2.
\]
**Futuro latente:**
\[
R_{\rm future,\tau}=\frac1h\sum_{k=1}^h
(\widehat y_{T+k|T}-\tau_{T+k})^2.
\]
**Futuro observado:**
\[
R_{\rm future,y}=\frac1h\sum_{k=1}^h
(\widehat y_{T+k|T}-y_{T+k})^2.
\]
**Futuro condicional (si \(\xi\ne0\)):**
\[
R_{\rm future,\tau+\xi}=\frac1h\sum_{k=1}^h
(\widehat y_{T+k|T}-\tau_{T+k}-\xi_{T+k})^2.
\]
Además guardar \(\widehat S,\widehat\mu\),
media verdadera promedio de diferencias en
la última ventana de $\tau$ (solo diagnóstico),
EDF penalizado, EDF plug-in,
MAE, error por lead k, porcentaje de extremos
S=0/1 y fallos.

**Estadística:** por cada celda, generar semilla
independiente; promediar pérdidas por origen
dentro de cada semilla, luego calcular efectos
pareados de método contra comparador por semilla,
intervalos de confianza y casos negativos.
No considerar folds overlapping independientes.

## 7. Figuras del eventual artículo

1. **Misma \(\tau\), tres ruidos:** observación y,
   tendencia real τ y $\widehat\tau$ de
   los tres selectores; misma escala/ejes.
2. **Cómo selecciona S:** curvas históricas
   \(F_0(S),F_G(S),\widetilde F(S)\), marcar
   respectivos mínimos y μ(S) sobre eje secundario.
3. **Pronóstico frente a verdad:** línea vertical
   en T, h puntos futuros, y futuro y τ futura
   visibles SOLO tras selección; mostrar errores
   bajo tres σ sin seleccionar solo ejemplo ganador.
4. **Geometría:** sección 2D \(F(S,\mu)\)
   y curva \(\mu^*(S)\), contornos y perfil;
   debajo $\widetilde F'(S)$ y mínimos.
5. **Rangos de h y d:** heatmaps de error,
   distribución de μ estimada vs verdadera,
   S y EDF, incluyendo fallos.
6. **Comparador:** intervalos de diferencias
   pareadas en MSFE frente a μ=0, Guerrero,
   CV/GCV/AICc/BIC y naive/drift/OLS,
   con identificación clara de criterios que
   NO ajustan μ.
7. **Stability / régimen:** selección de μ(S)
   cuando cambia la pendiente/curvatura,
   mostrando coste de usar demasiada historia.

## 8. Primera prueba ejecutable (pero aún sin resultados)

\`\`\`powershell
python -m pytest tests/test_mean_difference_forecast_cv.py -q
python -m experiments.mean_difference_forecasting.run_pilot --seeds 5 --max-cells 6 --grid-points 41
\`\`\`

El piloto se ejecuta en CPU para probar semántica y
fuga temporal, sin tocar la campaña CUDA previa.
Después podremos vectorizar/GPU únicamente las
matrices de pérdida, manteniendo idénticos
resultados de referencia. Un benchmark de hardware
no será el objeto del artículo.

## 9. Gate antes de la sección Results

No escribir «el modelo mejora», ni exportar cifras
seleccionadas post hoc, hasta verificar
el código, manifest del DGP, toda comparación
en las mismas réplicas/test y sensibilidad
a la nueva complejidad de μ. La búsqueda
bibliográfica de prioridad científica sigue abierta.
