# Apuntes: de Guerrero a CV de pronóstico, raíces y ramas

**Notas de estudio en orden de construcción conceptual** (no tres manuscritos fusionados ni una revisión histórica exhaustiva). Cada bloque formula preguntas, muestra las demostraciones y termina con un checkpoint autocontenible que sirve para comprobar la comprensión.

## Ruta de la clase

1. **Guerrero (2007)**: modelo de componentes, estimación lineal de mínimo MSE, penalización general y especialización `V = I`, `mu = 0`.
2. **Motivación del pronóstico**: por qué el MSE de reconstrucción no equivale a MSE de futuro a horizonte `h`.
3. **Construcción matricial**: diferencias `D_d`, penalización `Q_d`, solución `H_lambda`, prueba del núcleo de dimensión `d` y de la simetría.
4. **Teorema espectral, con demostración**: cuándo se permite `Q=U Lambda U^T`, por qué los autovalores son reales/no negativos, `d` autovalores cero, contracción espectral, límites y grados de libertad efectivos.
5. **Índice de Guerrero y suavidad normalizada**: prueba de la biyección entre coordenadas `lambda` y `S`; no hay ninguna exigencia de inyectividad para las pérdidas.
6. **Working Paper — Smoothness Cross Validation**: continuación `G_(d,h)`, MSE de bloques futuros sin fuga, superficie agregada `f_T(lambda)` y la misma función `F_T(S)`; equivalencia de mínimos, derivadas de primer, segundo y orden n de `H`, derivadas de pérdidas y de `F` por cadena.
7. **Working Paper — Numerical Methods**: raíces y mínimos de una `F` fija; Brent para raíces frente a Brent para optimización; reducción racional a un polinomio estacionario; conteo y aislamiento mediante Sturm para instancias exactas restringidas.
8. **Working Paper — Dynamic Branch Selection**: sucesión cronológica de `F_r` completadas, emparejamiento de mínimos entre superficies adyacentes, persistencia local condicionada por el teorema de la función implícita, selector de rama y suavidad operativa.
9. **Integración**: algoritmo completo, pruebas de integridad temporal, supuestos, límites, preguntas abiertas y checkpoints.

La secuencia es **histórica en el sentido del descubrimiento lógico**: cada herramienta responde una pregunta surgida en la etapa anterior. El origen histórico de cada método se reconoce, pero no se atribuye originalidad a las identidades clásicas.

## Archivos y compilación

`main.tex` es el documento maestro. Desde la raíz:

```bash
cd notes/notes_on_smoothnes
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

El PDF se genera localmente y no se versiona; no se automatiza la compilación mediante CI. Requiere TeX Live o MiKTeX con KOMA-Script, babel español, amsmath, mathtools, lmodern, enumitem y hyperref.

## Fuentes de verdad del repositorio

- `working_papers/THEORETICAL_CONTRIBUTIONS.md`
- `working_papers/WEIGHTED_SURFACE_PROTOCOL.md`
- `working_papers/Working Paper - Smoothness Cross Validation/README.md`
- `working_papers/Working Paper - Numerical Methods/README.md`
- `working_papers/Working Paper - Dynamic Branch Selection/README.md`
- `notes/derivative.md`

### Límites importantes

Los tres proyectos comparten `H`, `S`, `G` y la familia de superficies de CV, pero son problemas independientes. El primer paper minimiza globalmente `F_M`. El numérico analiza raíces y extremos **en una superficie fija**. El dinámico empareja mínimos entre actualizaciones `F_r` y aplica una decisión posterior a cada rama. Un resultado de Sturm sobre un caso racionalizado no certifica automáticamente todos los mínimos del problema flotante original; una rama trazada no garantiza menor error de pronóstico. La comparación requiere un test temporal externo no utilizado en selección.