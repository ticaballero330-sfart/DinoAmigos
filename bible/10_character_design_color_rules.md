# Reglas estrictas de diseño y color de personajes

Este documento es obligatorio para cualquier ilustración a color, portada, anuncio, mockup, storyboard coloreado o imagen promocional de Los Dinoamigos.

## Problema detectado

En algunas imágenes generadas los colores de los dinosaurios cambian porque los prompts actuales describen bien la especie, la personalidad y el estilo general, pero no fijan una paleta cerrada por personaje. Si el prompt dice solo "cute baby T-Rex" o "cute baby dinosaur", el generador decide el color por su cuenta y puede convertir al mismo personaje en verde, naranja, azul o morado entre páginas.

## Regla editorial principal

Cada personaje debe mantener siempre el mismo color base, los mismos acentos, la misma forma corporal y los mismos rasgos de identificación. No se permiten rediseños entre páginas.

## Estilo oficial de acabado

El estilo de color deseado para toda la saga es el look alegre y luminoso de
las imagenes finales del Libro 1 (`book_01_los_dinoamigos_nacen/images/finals/`):
acabado de cuento infantil animado, colores vivos pero suaves, luz calida
preferida y azul magico solo como acento pequeno, fondos ricos pero legibles,
contornos limpios y personajes redondeados.

Este estilo se aplica a iluminacion, acabado, saturacion, alegria y atmosfera.
No se aplica a identidad. Si el generador propone una imagen hermosa pero
cambia colores, silueta, edad, ropa base, especie, poderes o accesorios de un
personaje, la imagen debe rechazarse.

## LUMINOUS BOOK 1 COLOR STYLE

La luminosidad del Libro 1 es obligatoria en toda imagen a color: brillo global
alto, alegria visual, saturacion suave, sombras minimas, personajes y rostros
bien iluminados, fondos claros o pastel cuando la escena lo permita y contraste
suave.

El brillo azul magico no debe dominar la imagen. Usarlo como acento de burbuja,
portal, nave, cristal o energia, manteniendo el resto de la pagina clara y
alegre. En escenas nocturnas, cuevas, ruinas, niebla, camaras o espacio, usar
"noche luminosa infantil": cielo azul claro o morado suave, estrellas grandes,
linternas calidas, brillos pastel y lectura clara de personajes.

No permitir dark navy dominance, low-key lighting, moody cinematic shadows, dim
blue cast, gloomy palette, dramatic sci-fi darkness ni fondos apagados que
alejen el acabado del Libro 1.

## Paleta oficial de Dinoamigos

| Personaje | Color base obligatorio | Color secundario | Rasgos fijos | No permitir |
|---|---|---|---|---|
| Rexxie | verde bosque suave | barriga crema cálida | T-Rex bebé, ojos grandes, dientes redondeados, mejillas suaves | Rexxie rojo, azul, morado, con dientes agresivos o cuerpo adulto |
| Dipo | amarillo pastel cálido | manchas verde menta | Diplodocus bebé, cuello largo, sonrisa dulce, cuerpo redondeado | Dipo verde oscuro, gris, con cuello corto o aspecto adulto |
| Trici | rosa coral suave | escudo facial lila claro, cuernitos marfil | Triceratops bebé, tres cuernos redondeados, expresión protectora | Trici marrón, gris, cuernos afilados o aspecto agresivo |
| Velo | turquesa brillante | rayas azul oscuro suaves | Velociraptor bebé pequeño, ágil, postura de corredor, sonrisa traviesa | Velo verde genérico, rojo, garras peligrosas o mirada feroz |
| Mega | azul océano | barriga celeste clara, aletas azul más oscuro | Megalodón bebé, sonrisa grande tierna, burbujas, carrito-acuario en mundo moderno | Mega gris realista, tiburón amenazante, dientes terroríficos |
| Olic | azul verdoso | marcas luminosas cian, ojos dorados | dinosaurio volador, alas grandes, cuerpo noble, brillo suave | Olic rojo, marrón, negro, sin marcas luminosas |

## Paleta oficial de niños

| Personaje | Rasgos obligatorios | Ropa base sugerida | No permitir |
|---|---|---|---|
| Maxi | niño moreno, alegre, expresivo | camiseta naranja, chaleco explorador verde, pantalón corto azul | cambiarlo a rubio o hacerlo serio |
| Luna | niña rubia, dulce, mirada tranquila | camiseta celeste, falda o pantalón cómodo amarillo suave | cambiar cabello oscuro sin justificación |
| Teo | niño con pelo rizado | camiseta roja suave, mochila, pantalón verde | pelo liso o postura demasiado quieta |
| Mía | niña con rasgos asiáticos, inteligente, ordenada | camiseta violeta, chaleco claro, libreta o brazaletes desde Libro 3 | borrar sus rasgos o cambiar su rol visual |
| Leo | niño pelirrojo o con pecas | camiseta verde clara, pantalón azul, botas desde Libro 3 | quitar pecas o cambiar cabello a negro |
| Luke | niño aventurero | ropa azul de explorador aéreo, visor espacial azul desde Libro 3 | hacerlo adulto o demasiado serio |

## Evolución visual por libros

## Libro 1

Los Dinoamigos aparecen sin poderes. Rexxie no tiene alas ni marca. Mega solo tiene carrito-acuario después de llegar al futuro.

## Libro 2

Mantener diseños del Libro 1. No añadir poderes todavía.

## Libro 3

Aparecen poderes:

- Rexxie: alas pequeñas de energía roja suave.
- Dipo: patas con brillo dorado suave.
- Trici: armadura brillante rosa-dorada.
- Velo: garras veloces con brillo cian no peligroso.
- Mega: aletas turbo con brillo azul.
- Luna: alas luminosas.
- Maxi: poder acuático.
- Teo: patas veloces.
- Mía: brazaletes de energía.
- Leo: botas de salto gigante.
- Luke: visor espacial azul.

## Libro 4

Rexxie recibe la marca alienígena roja al final. Antes de esa escena no debe aparecer.

## Libro 5

La marca de Rexxie sigue roja, deja de doler y al final parece una pequeña estrella roja. No desaparece.

## Prompt obligatorio para color

Usar este bloque en todas las imágenes a color:

```text
STYLE LOCK. Match the luminous cheerful full-color storybook style of Book 1 final art: polished animated children's book look, joyful magical atmosphere, soft saturated colors, clean bold outlines, rounded cute characters, expressive eyes, rich but readable backgrounds, high readability for children ages 5 to 10. Use this style for lighting, finish, color harmony and mood only; do not use it to redesign characters.

LUMINOUS BOOK 1 COLOR STYLE. Keep high overall brightness, cheerful soft-saturated color, clearly lit faces, minimal shadows, bright readable backgrounds, and a warm animated storybook feeling. Prefer warm sunlight. Use friendly blue magical glow only as a small accent; it must not become the dominant palette or darken the image. For night, cave, ruins, mist, chamber, and space scenes, use child-friendly luminous night: light blue or soft violet sky, large stars, warm lanterns, pastel glows, and readable characters. No dark navy dominance, no low-key lighting, no moody cinematic shadows, no dim blue cast, no gloomy palette, no dramatic sci-fi darkness.

STRICT CHARACTER COLOR CONTINUITY. Do not redesign characters. Keep the same official colors in every image:
Rexxie is soft forest green with a warm cream belly, rounded teeth, big expressive eyes.
Dipo is warm pastel yellow with mint green spots, long neck, rounded body.
Trici is soft coral pink with a light lilac frill and ivory rounded horns.
Velo is bright turquoise with soft dark blue stripes, small agile baby raptor body.
Mega is ocean blue with a pale sky-blue belly and darker blue fins, cute baby megalodon, never scary.
Olic is teal blue-green with glowing cyan markings and golden eyes.
Maxi is a cheerful brown-skinned boy with orange shirt, green explorer vest and blue shorts.
Luna is a blonde gentle girl with light blue shirt and soft yellow clothing accents.
Teo has curly hair, red soft shirt, green pants and explorer backpack.
Mía is an Asian-featured girl with violet shirt, light explorer vest and smart observant expression.
Leo is a red-haired boy with freckles, light green shirt and blue pants.
Luke wears blue aerial explorer clothes and a blue space visor.
No alternate colors, no random palette, no redesign, no adult versions, no realistic scary dinosaurs.
```

## Prompt obligatorio para blanco y negro

En páginas de colorear no se exige color, pero sí identidad por forma:

```text
BLACK AND WHITE COLORING PAGE. Keep character identity by silhouette and fixed design: Rexxie small baby T-Rex with rounded teeth; Dipo long-neck baby Diplodocus; Trici baby Triceratops with three rounded horns and soft frill; Velo small agile baby raptor with stripe areas left blank for coloring; Mega cute baby megalodon with big friendly smile and bubbles; Olic flying dinosaur with large wings and marking shapes. Clean bold outlines, no grayscale shading, no filled black areas, no tiny details, Amazon KDP coloring book ready.
```

## Reglas de control de calidad

- Si el color base de un Dinoamigo cambia, la imagen debe rechazarse.
- Si el personaje parece adulto, agresivo o realista, la imagen debe rechazarse.
- Si Rexxie tiene marca antes del final del Libro 4, la imagen debe rechazarse.
- Si Rexxie no tiene marca después del Libro 4, la imagen debe corregirse.
- Si Mega aparece en ciudad moderna sin agua o sin carrito-acuario, la imagen debe corregirse.
- Si Olic aparece sin marcas luminosas cian u ojos dorados en imágenes a color, la imagen debe corregirse.
- Si una página a color no coincide con la paleta oficial, no usarla para Amazon, portada, interiores ni publicidad.
- Si una página a color respeta la paleta pero queda oscura, apagada, azul marino dominante, cinematica o gloomy, debe rechazarse o regenerarse.

## Flujo recomendado para el agente diseñador

1. Crear primero una hoja de modelo de personajes a color.
2. Aprobar la hoja de modelo antes de generar páginas.
3. Usar esa hoja como referencia visual en todas las escenas.
4. Generar cada página en dos versiones: color y blanco y negro.
5. Comparar cada resultado con esta biblia de color.
6. Rechazar o regenerar cualquier imagen que cambie la paleta.
