# Trend Estimation — wiki matemática

Este directorio es un **vault de Obsidian independiente**. Su propósito es hacer consultable y comprobable la cadena de resultados matemáticos del proyecto: cada resultado tiene una ficha breve, su demostración en otro archivo, requisitos matemáticos explícitos y fuentes de literatura.

- `wiki/`: enciclopedia de conocimiento verificado y sus dependencias, *no* un cuarto working paper.
- `notes/`: cuadernos, notas de estudio y bitácoras (incluido `notes_on_smoothnes/main.tex`).
- `literature/`: PDFs originales, extracción, metadatos y referencias.
- `working_papers/`: protocolos vigentes, pruebas específicas y evidencia de los tres artículos.

Para usarla, abrir en Obsidian **exactamente `Trend-Estimation/wiki/`** con *Open folder as vault*. Abrir [[Inicio]].

## Principios editoriales

1. **Resultados atómicos.** Un archivo `RES-xxx.md` declara un enunciado, supuestos y consecuencias. Su propiedad `prueba` enlaza un `DEM-xxx.md` con una demostración completa.
2. **Dependencias reales.** El campo `up` y la sección «Necesita» apuntan hacia definiciones y resultados *previos*. No enlazar como requisito algo que se está usando circularmente para demostrarse. «Utilizado por» se obtiene por backlinks, no se mantiene a mano.
3. **Fuentes trazables.** `fuentes` enlaza fichas `LIT-xxx`; cada ficha contiene DOI y, cuando existe en nuestro corpus, enlace al PDF y a su extracción bajo `../literature/`. Los vínculos a fuentes fuera del vault son URLs de GitHub, no enlaces internos de Obsidian.
4. **No confundir autoridad.** Una prueba nuestra de una identidad clásica no constituye automáticamente una contribución original. Las afirmaciones sobre superioridad predictiva requieren estudios externos.
5. **Notación estable.** Usamos $D_d,Q_d,H_\lambda$ para matrices; $S(\lambda)$ para suavidad escalar; $G_{d,h}$ para la continuación; $F_r$ para la superficie. Matemáticas en línea `$...$`; bloques `$$...$$`.
6. **Los plugins son opcionales.** El contenido, los wikilinks y las pruebas no dependen de ellos. Nunca versionar archivos de sesión, caché o código de plugins.

## Plugins y navegación

| Herramienta | Uso | Preparación |
| --- | --- | --- |
| **Bases** (core) | Tablas filtrables de resultados, pruebas y literatura | Activar *Bases* en Core plugins; se incluyen archivos `catalogos/*.base` |
| **Backlinks/Graph/Outline** (core) | Uso inverso de un resultado, navegación y estructura | Activar en Core plugins |
| **Breadcrumbs** (community) | Grafo **dirigido**: `up` señala los prerrequisitos | Instalar desde Community plugins; si es necesario, configurar `up` como edge field y ejecutar *Rebuild graph* |
| **Templates** (core) | Fichas editables sin scripts | Activar Templates; carpeta `_plantillas` ya configurada |
| **Fileclass** (opcional) | Formularios para metadatos tipados | Instalar si conviene; requiere indicar manualmente la carpeta de clases. No es requisito de integridad |
| **Templater** (opcional) | Automatización más avanzada de plantillas | No requerido para las plantillas incluidas; las de aquí son del plugin Core Templates |

Instalación de community plugins requiere una acción del usuario **dentro de su Obsidian**. El repo no descarga, ejecuta ni instala código de terceros.

Documentación: [Bases](https://obsidian.md/help/bases), [Breadcrumbs](https://community.obsidian.md/plugins/breadcrumbs), [Fileclass](https://github.com/mdelobelle/fileclass).

## Verificación reproducible

Desde la raíz:

~~~bash
python tools/validate_wiki.py
python -m pytest tests/test_wiki.py
~~~

El validador usa sólo la biblioteca estándar: comprueba tipos, IDs y nombres únicos, enlaces internos, existencia y dirección de demostraciones, DAG de dependencia sin ciclos, rutas de literatura y delimitadores matemáticos de bloque. **No demuestra la corrección matemática de una prueba** ni garantiza que Obsidian haya representado visualmente todo igual.

Véase [[Estandar editorial]] y el [[mapas/Mapa de resultados|índice pedagógico]].
