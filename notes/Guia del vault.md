# Guía del vault de Obsidian

## Abrir el vault

1. Clonar o actualizar `Trend-Estimation` mediante Git.
2. Abrir Obsidian → **Open folder as vault** → seleccionar exactamente la carpeta `notes/` (no la raíz del repositorio).
3. Abrir [[Inicio]]. Las páginas existentes y sus wikilinks forman la red de conocimiento.
4. En Settings → Core plugins, activar **Backlinks**, **Graph view**, **Outline** y **Templates** para navegación. Para plantillas, el directorio incluido es `_plantillas/`.

No requiere Dataview, Git community plugin, MathJax externo ni servicios de sincronización. Git sigue siendo la fuente de control de versiones.

## Qué se debe editar en cada lugar

| Contenido | Lugar autorizado |
| --- | --- |
| Demostración pedagógica completa y PDF de estudio | `notes_on_smoothnes/main.tex` |
| Fichas de conceptos y enlaces a pruebas | `conceptos/` |
| Derivadas, definiciones e implementaciones históricas del proyecto | notas Markdown de nivel superior |
| Resultados y afirmaciones de cada artículo activo | `../working_papers/Working Paper - .../notes/` |
| Checkpoints y bitácoras anteriores | `checkpoints/` y `experiments/` |

Los enlaces a `working_papers/` apuntan a GitHub porque esa carpeta está **fuera** del vault. No copiar automáticamente esos documentos dentro de `notes/`: se crearían versiones divergentes. Los archivos `.tex` también se conservan sin conversión mecánica; Obsidian no es un compilador LaTeX.

## Matemáticas en Markdown

Obsidian renderiza la notación matemática con delimitadores `$...$` (en línea) y `$$...$$` (en bloque). Por ejemplo:

$$
Q_d = D_d^\top D_d \succeq 0,\qquad
\operatorname{edf}(\lambda)=\operatorname{tr}(I+\lambda Q_d)^{-1}.
$$

Para nuevas páginas usar esos delimitadores, y no ``\( ... \)`` ni ``\[ ... \]``, que son habituales en antiguos Markdown de investigación y pueden no renderizarse de forma consistente. Para comandos personales definidos en LaTeX (p. ej. `\EE`, `\norm`) usar equivalentes estándar en las fichas: `\mathbb E`, `\lVert\cdot\rVert`.

## Regla editorial

Cada afirmación matemática debería presentar **pregunta → supuestos → derivación o referencia exacta → resultado → interpretación → implementación/prueba → estado**. Si el resultado sólo se ha observado empíricamente, indicarlo. No reinterpretar un checkpoint antiguo como evidencia actual ni atribuir un teorema de un paper al otro.

## LaTeX y git

Desde la raíz del repo:

~~~bash
cd notes/notes_on_smoothnes
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
~~~

El PDF y auxiliares de compilación se generan localmente. Los ajustes de vista personales de Obsidian (`.obsidian/workspace*.json`), la papelera y archivos temporales quedan fuera de Git; `.obsidian/app.json` y `.obsidian/templates.json` se comparten.

Para sincronizar cambios: `git pull --ff-only` antes de editar y `git add notes/ && git commit && git push` cuando el conjunto de cambios esté listo.

## Crear una nueva demostración

Crear una nota en `conceptos/` desde [[_plantillas/Nota matematica|Plantilla matemática]]. Enlazar conceptos con `[[derivative]]` y añadir en la página correspondiente un enlace de vuelta.
