# Estándar editorial y de pruebas

## El átomo del conocimiento

- `DEF-xxx`: **definición**; fija símbolos e hipótesis, no exige prueba.
- `RES-xxx`: **resultado** formal, siempre con `prueba: "[[DEM-xxx]]"` si su estado es `demostrado`.
- `DEM-xxx`: **demostración independiente**, desglosada por pasos, con `resultado: "[[RES-xxx]]"`.
- `LIT-xxx`: **ficha bibliográfica**; no representa una reproducción de un artículo ni pretende resumirlo exhaustivamente.
- `mapas/`: secuencias de lectura y delimitaciones de alcance, que no forman parte del DAG.
- `catalogos/*.base`: catálogos de Obsidian generados de las propiedades.

El campo `up` es **unidireccional**: «esta afirmación depende de estas páginas». Sólo se admiten enlaces a `DEF` o `RES` demostrados. Para obtener relaciones «utilizado por», usar Backlinks o Breadcrumbs en dirección inversa; no duplicar listas.

## Contrato mínimo

~~~yaml
---
id: "RES-007"
tipo: "resultado"
titulo: "..."
estado: "demostrado"
up: ["[[DEF-005]]", "[[RES-004]]"]
prueba: "[[DEM-007]]"
fuentes: ["[[LIT-001]]"]
tags: ["algebra-lineal"]
---
~~~

Un `DEM-007` requiere `tipo: "demostracion"`, `resultado: "[[RES-007]]"` y puede tener `up` con definiciones o lemas que use explícitamente. Las fichas `LIT` requieren `origen_repo` apuntando a un PDF existente si se declara, y `doi`/URL cuando se dispone de ellos. Los campos de esta primera versión emplean **YAML de una sola línea** (arrays en formato JSON/YAML flow); el validador de biblioteca estándar analiza ese subconjunto intencionadamente.

## Estados

- `demostrado`: prueba algebraica interna adjunta; el resultado puede ser clásico.
- `definido`: identidad notacional o convención declarada.
- `documentado`: referencia externa identificada sin atribuir un teorema propio.
- `pendiente`: conjetura/pregunta no verificada; *no* puede aparecer como prerrequisito probado.

## Política de demostraciones

1. Enunciar $L,d,h,\lambda$, intervalos, matrices y tamaño de las ventanas antes de manipular fórmulas.
2. No derivar propiedades de independencia a partir de covarianza nula.
3. Distinguir $H_\lambda$ (matriz) de $S(\lambda)$ (escalar).
4. Sólo usar $t+h\le T$ en una pérdida histórica disponible al origen $T$.
5. La definición de $G_{d,h}$ pertenece a la regla de continuación, no al estimador de Guerrero per se.
6. Derivadas y óptimos de $F$ no demuestran consistencia ni mejores pronósticos externos.
7. Las rutas a PDFs y extracciones son *externas al vault*; se abren como URLs a GitHub en la wiki.

## Formato matemático

Correcto para fórmula multilínea:

~~~markdown
$$
\begin{aligned}
a &= b+c\\
d &= e+f
\end{aligned}
$$
~~~

Nunca colocar un único `$` en una línea para abrir/cerrar un bloque. El validador lo rechaza.

## Flujo para añadir un teorema

1. Abrir [[_plantillas/Resultado|plantilla de resultado]] y crear el siguiente `RES-xxx` libre (ID estable).
2. Escribir enunciado, supuestos y prerequisitos `up` hacia páginas existentes.
3. Crear `DEM-xxx` a partir de [[_plantillas/Demostracion|plantilla de prueba]] y probar cada paso, enlazando explícitamente propiedades utilizadas.
4. Añadir en `RES` el `prueba` correspondiente y el `fuentes` bibliográfico. No inventar el `doi` ni la ubicación del PDF.
5. Ejecutar `python tools/validate_wiki.py`, actualizar [[mapas/Mapa de resultados]] y abrir el grafo de Breadcrumbs si está instalado.
