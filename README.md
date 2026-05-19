# Los Dinoamigos

Proyecto editorial infantil basado en las ideas originales de un niño de 6 años. La saga está dirigida a niños y niñas de 5 a 10 años y combina dinosaurios bebés, huevos mágicos, burbujas, viajes en el tiempo, platillos voladores, campamentos, mapas, retos, familias y amistad.

## Carpetas principales

- `bible/`: biblia global de continuidad, personajes, reglas del mundo, estilo visual, objetos, lugares, checklist y auditoría editorial.
- `book_01_los_dinoamigos_nacen/`: origen, nacimientos, burbujas, viaje al futuro y adopción.
- `book_02_la_maquina_del_tiempo/`: desaparición de Trici, huellas, Máquina del Tiempo y rescate.
- `book_03_el_secreto_del_platillo_azul/`: Luke, Olic, nave alienígena, Cofre Dorado y poderes.
- `book_04_la_isla_perdida_de_los_dinosaurios/`: isla, Baruk, padres dinosaurios, Aeron y marca de Rexxie.
- `book_05_en_busca_de_la_planta_secreta/`: Doctor Lumo, retos, Doctor Florio y aceptación de la marca.

## Cómo trabajar cada libro

1. Leer `bible/00_saga_overview.md`.
2. Revisar `bible/02_characters_master.md` y `bible/continuity_matrix.md`.
3. Abrir el libro correspondiente y trabajar desde `story/page_by_page.md`.
4. Usar `prompts/global_prompt_style.md` antes de generar imágenes.
5. Validar con `bible/editorial_checklist.md`.

## Estructura por libro

Cada libro contiene `story/`, `characters/`, `locations/`, `objects/`, `challenges/`, `scenes/`, `prompts/`, `images/` y `animation/`.

## Generación de prompts

Usar el prompt maestro visual, los prompts por personaje y los prompts por página. Para libro de colorear, usar siempre `prompts/coloring_book_prompts.md`.

## Reglas para no romper la historia

- No cambiar nombres normalizados.
- No eliminar personajes principales.
- No convertir la saga en ciencia ficción dura.
- No añadir violencia gráfica.
- No hacer que alienígenas o guardianes sean terroríficos.
- Mantener frases claras para 5 a 10 años.
- Mantener 32 páginas por libro.

## Cómo añadir nuevos libros

Crear una carpeta `book_XX_titulo/` con la misma estructura. Añadir el resumen a la biblia, actualizar la matriz de continuidad y definir un gancho suave desde el libro anterior.

## Validación antes de crear imágenes

Comprobar que cada página tiene acción clara, personajes grandes, emoción visible, fondo coloreable, prompt base y notas para libro de colorear.
