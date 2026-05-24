# Flujo manual Codex / ChatGPT Plus - Libro 2

## Regla principal

No usar API, `OPENAI_API_KEY`, CLI de generación ni scripts OpenAI. La generación debe hacerse desde la herramienta integrada de imagen de Codex o desde ChatGPT Plus en navegador.

## Prueba inicial

1. Abrir `generation_prompts/color/page_01_color.txt`.
2. Generar una imagen con la herramienta integrada de Codex.
3. Guardar el resultado como `images/finals/page_01_color.png`.
4. Abrir `generation_prompts/coloring/page_01_coloring.txt`.
5. Generar la versión de colorear.
6. Guardar el resultado como `images/coloring_pages/page_01_coloring.png`.
7. Aplicar `image_qa_matrix.md` antes de seguir.

## Producción

Generar por bloques de cuatro páginas:

- 01-04
- 05-08
- 09-12
- 13-16
- 17-20
- 21-24
- 25-28
- 29-32

Para cada página generar primero color y después blanco y negro. Actualizar `manual_production_tracker.md` con `aprobada`, `corregir` o `rechazada`.

## Fallback ChatGPT Plus

Si Codex no permite guardar el lote con control suficiente:

1. Abrir ChatGPT Plus en navegador.
2. Crear un chat nuevo llamado `Los Dinoamigos 2 - La Máquina del Tiempo`.
3. Pegar un prompt individual por mensaje.
4. Descargar cada resultado.
5. Guardarlo con el nombre exacto indicado en `kdp_image_production_prompts.md`.
6. Revisar con `image_qa_matrix.md`.

## Normalización KDP

Cuando sea posible, normalizar cada PNG a `2550 x 3300 px`, `300 dpi`. No añadir texto, logos, marcas de agua ni bordes decorativos.
