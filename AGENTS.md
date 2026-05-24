# DinoAmigos Agent Guide

Este archivo es el contrato de trabajo para cualquier agente que edite, revise o genere contenido de Los DinoAmigos. La prioridad del proyecto es mantener consistencia editorial y visual en todos los libros, prompts, escenas, paginas de colorear, arte final y material de animacion.

## Lectura obligatoria

Antes de tocar historia, prompts, imagenes o reglas visuales, leer en este orden:

1. `README.md`
2. `bible/00_saga_overview.md`
3. `bible/02_characters_master.md`
4. `bible/03_visual_style_guide.md`
5. `bible/10_character_design_color_rules.md`
6. `bible/continuity_matrix.md`
7. `bible/editorial_checklist.md`

Para trabajos especificos de un libro, leer tambien su `README.md`, `story/page_by_page.md`, `story/continuity_notes.md` y los prompts dentro de `prompts/`.

## Reglas globales

- Publico objetivo: ninos y ninas de 5 a 10 anos.
- Tono: tierno, aventurero, colorido, magico, familiar y seguro.
- Mantener 32 paginas por libro salvo instruccion explicita del usuario.
- Usar frases cortas, accion clara por pagina y emociones visibles.
- Preservar la imaginacion infantil; ordenar sin endurecer la historia.
- No convertir la saga en ciencia ficcion dura, drama oscuro, terror o violencia grafica.
- Alienigenas, guardianes, robots y peligros deben sentirse como retos magicos o comicos, no como amenazas realistas.
- No cambiar nombres normalizados ni eliminar personajes principales.

## Reglas de diseno visual

- Book 1 final art style lock: las imagenes finales a color de
  `book_01_los_dinoamigos_nacen/images/finals/` son la referencia estetica
  oficial para toda la saga. Imitar su acabado alegre, luminoso, pulido,
  colorido y de cuento infantil animado en los 5 libros.
- El estilo del Libro 1 controla luz, acabado, alegria, contraste suave,
  riqueza de color y sensacion magica; no autoriza cambiar la paleta,
  cuerpo, edad, especie, ropa, poderes o accesorios de ningun personaje.
- Personajes grandes, ojos expresivos, contornos claros y siluetas reconocibles.
- Fondos simples pero identificables, con formas amplias aptas para colorear.
- Paleta oficial estricta por personaje en cualquier imagen a color.
- No improvisar colores, cuerpos, edades, rasgos, poderes ni ropa base.
- No usar versiones adultas, agresivas, realistas o terrorificas de los Dinoamigos.
- Para imagenes a color, aplicar siempre las reglas de `bible/10_character_design_color_rules.md`.
- Todo prompt a color debe incluir un bloque `STYLE LOCK` basado en el Libro 1
  y el bloque `STRICT CHARACTER COLOR CONTINUITY`.
- Para paginas en blanco y negro, preservar identidad por silueta, rasgos fijos y zonas coloreables limpias.
- La espectacularidad nunca debe romper la continuidad visual.

## Continuidad que debe comprobarse

Antes de crear o revisar una escena, prompt o imagen:

- Confirmar el libro y el punto de la linea temporal.
- Confirmar si los poderes ya existen: no aparecen antes del Libro 3.
- Confirmar la marca de Rexxie: no aparece antes del final del Libro 4; despues del Libro 5 queda como pequena estrella roja.
- Confirmar Mega en mundo moderno: debe tener agua o carrito-acuario.
- Confirmar Olic en color: azul verdoso, marcas cian luminosas y ojos dorados.
- Confirmar que el objeto central del libro sea consistente: huevos, Maquina del Tiempo, Platillo Azul, isla o Jardin/Planta Secreta.
- Confirmar que la escena respeta la matriz de continuidad y no contradice libros anteriores.

## Criterios de rechazo visual

Rechazar o corregir cualquier imagen, prompt o descripcion visual si:

- Cambia el color base o rasgos fijos de un personaje.
- Hace que un Dinoamigo parezca adulto, agresivo, realista o aterrador.
- Muestra a Rexxie con marca fuera de continuidad.
- Omite la marca/estrella roja de Rexxie cuando ya corresponde.
- Muestra a Mega en ciudad o campamento moderno sin agua ni carrito-acuario.
- Muestra a Olic sin marcas cian u ojos dorados en color.
- Satura una pagina de colorear con detalles pequenos, sombreado gris o fondos confusos.
- Rompe el tono seguro, luminoso y familiar de la saga.

## Flujo recomendado

1. Identificar tipo de tarea: editorial, visual, QA de imagen, prompts, libro de colorear o animacion.
2. Leer la biblia global y los archivos del libro afectado.
3. Hacer cambios minimos y consistentes con la estructura existente.
4. Validar contra `bible/editorial_checklist.md`.
5. Si el trabajo afecta imagenes a color, validar contra `bible/10_character_design_color_rules.md`.
6. Si el trabajo afecta paginas de colorear, validar contra `bible/08_coloring_book_rules.md`.

## Agentes del proyecto

- `Editorial Continuity`: continuidad narrativa, estructura por libro, tono, edad objetivo y reglas de historia.
- `Visual Continuity`: diseno, paleta, prompts visuales, evolucion por libro y consistencia de personajes.
- `Image QA`: revision de imagenes o prompts finales con veredicto `aprobada`, `corregir` o `rechazada`.

Las instrucciones versionadas de estos agentes viven en `.agents/agents/` y sus skills en `.agents/skills/`.
