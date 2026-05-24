# Producción de imágenes - Libro 2 sin API

Este paquete prepara las 32 páginas de `Los Dinoamigos 2: La Máquina del Tiempo` en dos líneas:

- Color: `images/finals/page_XX_color.png`
- Blanco y negro: `images/coloring_pages/page_XX_coloring.png`

La estrategia de producción es Codex integrado o ChatGPT Plus. No usar `OPENAI_API_KEY`, API, CLI de generación ni scripts de OpenAI.

## Archivos

- `kdp_image_production_prompts.md`: prompts completos por página.
- `generation_prompts/color/`: prompts individuales a color.
- `generation_prompts/coloring/`: prompts individuales para colorear.
- `manual_generation_workflow.md`: pasos de generación con Codex o ChatGPT Plus.
- `manual_production_tracker.md`: avance manual por página y QA.
- `image_qa_matrix.md`: matriz de revisión con criterios por página.

## Flujo

1. Hacer una prueba con `page_01_color.txt` y `page_01_coloring.txt` desde Codex integrado.
2. Si Codex genera y permite guardar correctamente, continuar por bloques de 4 páginas.
3. Si Codex no permite guardar bien el lote, abrir ChatGPT Plus en navegador y pegar los prompts individuales.
4. Guardar con nombres exactos:
   - `images/finals/page_XX_color.png`
   - `images/coloring_pages/page_XX_coloring.png`
5. Marcar cada resultado en `manual_production_tracker.md`.
6. Revisar cada imagen con `image_qa_matrix.md`.

Cuando sea posible, normalizar la salida a PNG de `2550 x 3300 px` a `300 dpi`, compatible con interior 8.5 x 11 de Amazon KDP.

## QA

Aplicar `image_qa_matrix.md` después de generar. Regenerar cualquier imagen con:

- colores incorrectos,
- poderes del Libro 3,
- Rexxie con alas o marca roja,
- Trici visible antes de su reaparición narrativa,
- Mega sin agua o carrito-acuario en mundo moderno,
- Gran T-Rex aterrador o agresivo,
- página de colorear con grises, sombras pesadas o microdetalle.
