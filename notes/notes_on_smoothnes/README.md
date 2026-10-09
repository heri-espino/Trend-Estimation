# Notes on smoothness — derivaciones matemáticas

Documento autónomo en LaTeX que reconstruye las notas manuscritas de suavizamiento y las conecta con el protocolo **forecast-optimal, horizon-matched rolling-origin CV** vigente en el repositorio.

- `main.tex`: fuente completa con preguntas, demostraciones, glosario, referencias y discusión de límites.
- `main.pdf`: se genera localmente al compilar; no es necesario versionarlo.

## Compilar

Desde la raíz del repositorio:

```powershell
cd notes/notes_on_smoothnes
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

O con `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

Requiere una instalación LaTeX estándar con KOMA-Script, amsmath, amsthm, mathtools, booktabs, hyperref, fancyhdr, lmodern, enumitem, microtype y babel en español. No depende de los assets de los working papers.

## Alcance y trazabilidad

El orden es: Guerrero (2007), especialización `mu=0, V=I`, núcleo de las diferencias, autovalores, EDF, índices de suavidad, extrapolación, derivadas y objetivo de validación temporal del **Working Paper - Smoothness Cross Validation**.

Referencias internas utilizadas:

- `working_papers/THEORETICAL_CONTRIBUTIONS.md`
- `working_papers/WEIGHTED_SURFACE_PROTOCOL.md`
- `working_papers/Working Paper - Smoothness Cross Validation/README.md`
- `notes/derivative.md`

La descomposición espectral, los grados de libertad efectivos, la fórmula de derivada inversa y la validación temporal son herramientas conocidas. El documento no afirma originalidad ni superioridad empírica de una regla de selección.

La elección global de suavidad del **Paper 1** se mantiene separada del seguimiento de mínimos locales del **Paper 2** y de la búsqueda numérica del **Paper 3**. La compilación PDF es manual, sin GitHub Actions.
