from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]

STYLE = (
    "Children's coloring book illustration, cute baby dinosaurs and children explorers, "
    "expressive faces, clean bold outlines, simple shapes, magical adventure atmosphere, "
    "friendly fantasy science fiction, suitable for children ages 5 to 10, no scary horror, "
    "no realistic violence, whimsical, playful, high readability, large characters, clear composition, "
    "black and white line art version for coloring book, optional full color version for cover and animation reference."
)

MAGIC = (
    "Add glowing bubbles, blue magical light, soft stars, flying sparkles, friendly blue flying saucer, "
    "dreamy time travel atmosphere, child-safe fantasy science fiction, colorful but clean composition, "
    "clear outlines, magical but not scary."
)

COLORING = (
    "Black and white coloring book page for children ages 5 to 10, clean bold outlines, simple readable shapes, "
    "large expressive characters, cute baby dinosaurs, friendly children explorers, magical adventure scene, "
    "no shading overload, no tiny excessive details, clear background spaces for coloring."
)

BOOKS = {
    "book_01_los_dinoamigos_nacen": {
        "num": "01",
        "title": "Los Dinoamigos nacen",
        "theme": "nacimiento, amistad, burbujas mágicas, llegada al futuro y adopción tierna",
        "hook": "Una luz azul misteriosa parpadea en el cielo.",
        "pages": [
            ("Portada", "Los Dinoamigos nacen.", "Cinco huevos brillan en un valle prehistórico con montañas suaves y una luz azul lejana.", "huevos mágicos", "asombro"),
            ("El mundo antiguo", "Hace muchísimo tiempo, el mundo estaba lleno de montañas, ríos y árboles enormes. Algo mágico iba a pasar.", "Valle prehistórico amplio con helechos, río y volcanes lejanos.", "valle prehistórico", "maravilla"),
            ("Los huevos misteriosos", "Cinco huevos aparecieron en lugares distintos. Todos brillaban como pequeñas lunas.", "Composición con huevos en valle, pradera, rocas, selva y océano.", "cinco lugares", "misterio suave"),
            ("Nace Rexxie", "Crac, crac, crac. Del primer huevo salió Rexxie, un T-Rex bebé con ojos enormes.", "Rexxie rompiendo el cascarón con dientes redondeados.", "valle", "ternura"),
            ("El rugido pequeño", "Rexxie quiso rugir fuerte. —¡Rawr! Sonó tan pequeño que él mismo se sorprendió.", "Rexxie intentando parecer feroz mientras aves lo miran.", "valle", "humor"),
            ("Nace Dipo", "En una pradera verde nació Dipo, un Diplodocus bebé de cuello largo y sonrisa dulce.", "Dipo saliendo del huevo entre flores grandes.", "pradera", "calma"),
            ("Dipo mira lejos", "Dipo estiró el cuello y vio montañas. —Tal vez allí encuentre amigos.", "Dipo mirando hacia montañas lejanas.", "pradera", "esperanza"),
            ("Nace Trici", "Entre rocas y flores, Trici rompió su cascarón con tres cuernitos redondos.", "Trici saliendo con energía y cascarón alrededor.", "zona rocosa", "energía"),
            ("Trici protege", "—Yo voy a cuidar de todos —dijo Trici. Luego tropezó con su cola y se rio.", "Trici cayendo suavemente sin daño.", "zona rocosa", "humor"),
            ("Nace Velo", "En la selva, Velo salió del huevo casi corriendo. —¡Soy rápido!", "Velo saliendo entre hojas y raíces.", "selva", "alegría"),
            ("Velo explora", "Velo saltó raíces, dio vueltas y buscó a alguien con quien jugar.", "Velo corriendo por la selva.", "selva", "curiosidad"),
            ("Nace Mega", "Bajo el mar, un huevo dentro de una burbuja se abrió. Nació Mega, el Megalodón bebé.", "Mega bajo el agua con peces y burbujas.", "océano", "sorpresa"),
            ("Mega saluda", "Mega sonrió. —¡Glu-glu, hola! Los peces se escondieron, pero él solo quería jugar.", "Mega sonriendo con peces tímidos.", "océano", "humor"),
            ("Caminos que se juntan", "Sin saberlo, todos avanzaron hacia el mismo lugar.", "Mapa sencillo con cinco caminos que se unen.", "mapa prehistórico", "expectativa"),
            ("Primer encuentro", "Rexxie, Dipo, Trici, Velo y Mega se miraron en silencio.", "Los cinco bebés dinosaurios viéndose por primera vez.", "claro junto al río", "sorpresa"),
            ("Somos amigos", "Cada uno dijo su nombre. Mega hizo burbujas. Desde ese momento fueron amigos.", "Los cinco juntos sonriendo.", "claro", "alegría"),
            ("El gran viaje", "Decidieron buscar un lugar seguro. Cada Dinoamigo ayudó a su manera.", "Grupo avanzando por montes verdes.", "montes", "compañerismo"),
            ("Las montañas", "Las montañas eran altas, pero Trici dijo: —Podemos subir juntos.", "Dinosaurios subiendo con ayuda mutua.", "montañas", "valentía"),
            ("El río brillante", "Al otro lado había un río ancho. Mega saltó feliz. —¡Glu-glu! ¡Yo ayudo!", "Mega en el agua junto al grupo.", "río", "confianza"),
            ("Cruce divertido", "Dipo hizo de puente, Velo saltó piedras y Rexxie cruzó despacito.", "Escena cómica cruzando el río.", "río", "humor"),
            ("El cielo cambia", "Esa noche el cielo se puso rojo y una bola de fuego apareció muy lejos.", "Meteorito lejano visto con asombro.", "noche prehistórica", "miedo suave"),
            ("El meteorito lejano", "El meteorito cayó lejos. Hizo BOOOM, pero los Dinoamigos corrieron juntos.", "Explosión lejana no terrorífica.", "camino", "urgencia"),
            ("La cueva brillante", "Se refugiaron en una cueva con cristales azules. Se abrazaron hasta que pasó el temblor.", "Cueva luminosa con cristales y grupo unido.", "cueva brillante", "ternura"),
            ("La luz azul", "Cuando todo quedó tranquilo, una luz azul apareció. No era una estrella.", "Platillo Azul visto desde la cueva.", "entrada de cueva", "misterio"),
            ("El Platillo Azul", "El platillo bajó despacio y soltó burbujas mágicas de muchos colores.", "Platillo amigable lanzando burbujas.", "cielo", "maravilla"),
            ("Burbujas mágicas", "Una burbuja rodeó a cada Dinoamigo. —¡Hace cosquillas! —dijo Dipo.", "Dinosaurios dentro de burbujas luminosas.", "cueva", "alegría"),
            ("Viaje al futuro", "Las burbujas giraron. Las montañas cambiaron. Los Dinoamigos viajaron al futuro.", "Túnel con estrellas, relojes y burbujas.", "túnel temporal", "asombro"),
            ("Llegada al parque", "POP. Aparecieron en un parque moderno, pequeños como mascotas. Mega tenía un carrito-acuario.", "Dinoamigos pequeños en parque moderno nocturno.", "parque moderno", "sorpresa"),
            ("Niños exploradores", "Cerca había cinco niños exploradores: Maxi, Luna, Teo, Mía y Leo.", "Niños con linternas, mapa y mochilas.", "campamento urbano", "curiosidad"),
            ("El descubrimiento", "Niños y dinosaurios se asustaron a la vez. Luego se miraron mejor.", "Primer encuentro entre niños y Dinoamigos.", "arbustos del parque", "sorpresa divertida"),
            ("Promesa de amistad", "Los niños prometieron cuidarlos. Cada niño encontró a su Dinoamigo.", "Abrazos tiernos de adopción.", "campamento", "ternura"),
            ("Paseo por la ciudad", "Conocieron semáforos, fuentes, autobuses y helados. De noche, una luz azul parpadeó.", "Paseo urbano y cierre con luz azul en el cielo.", "ciudad moderna", "misterio feliz"),
        ],
        "characters": ["Rexxie", "Dipo", "Trici", "Velo", "Mega", "Maxi", "Luna", "Teo", "Mía", "Leo"],
        "locations": ["valle prehistórico", "pradera", "selva", "océano", "cueva brillante", "parque moderno", "campamento urbano"],
        "objects": ["huevos mágicos", "Platillo Azul", "burbujas mágicas", "carrito-acuario de Mega"],
        "challenges": ["cruzar montañas", "cruzar el río", "refugiarse del meteorito lejano", "confiar en nuevos amigos"],
    },
    "book_02_la_maquina_del_tiempo": {
        "num": "02",
        "title": "La Máquina del Tiempo",
        "theme": "búsqueda, huellas, primer viaje temporal y rescate silencioso",
        "hook": "Una estrella fugaz concede el deseo de más aventuras y la luz azul vuelve a parpadear.",
        "pages": [
            ("Portada", "Los Dinoamigos 2: La Máquina del Tiempo.", "Equipo frente a una máquina luminosa con huellas de Trici.", "Máquina del Tiempo", "misterio"),
            ("Noche en el campamento", "Después del paseo por la ciudad, todos durmieron muy cansados.", "Campamento nocturno con tiendas y linternas apagadas.", "campamento urbano", "calma"),
            ("Todos duermen", "Dipo abrazaba un árbol. Mega hacía burbujas. Trici dormía junto a Mía.", "Escena tierna de sueño grupal.", "campamento", "ternura"),
            ("Amanece", "El sol salió despacito. Pero algo no estaba bien.", "Primeras luces del día en el campamento.", "campamento", "inquietud"),
            ("Trici desaparece", "Mía miró su manta. —¡Trici no está!", "Mía señalando el lugar vacío.", "campamento", "preocupación"),
            ("Todos se preocupan", "El equipo despertó. Rexxie olfateó el suelo y Velo vio algo.", "Grupo buscando alrededor.", "campamento", "urgencia"),
            ("Las huellas", "—¡Huellas! —gritó Velo. Las marcas de Trici entraban entre los árboles.", "Huellas pequeñas en tierra húmeda.", "sendero", "curiosidad"),
            ("Equipo explorador", "Los niños tomaron linternas, mapa, cuerda y libreta. —Vamos por Trici.", "Niños preparándose.", "campamento", "decisión"),
            ("Siguiendo el rastro", "Velo fue delante, Dipo miró lejos y Mega avanzó en su carrito-acuario.", "Equipo siguiendo huellas.", "bosque", "concentración"),
            ("Túnel de raíces", "Las huellas llegaron a raíces enormes con luces azules debajo.", "Entrada al túnel brillante.", "túnel de raíces", "misterio"),
            ("Puerta secreta", "Al final había una puerta circular con relojes y una espiral azul.", "Máquina del Tiempo cerrada.", "subsuelo", "asombro"),
            ("La máquina despierta", "Teo se acercó. Mía dijo: —No toques nada. La máquina se encendió sola.", "Teo sorprendido ante botones.", "Máquina del Tiempo", "humor"),
            ("Huellas al portal", "Las huellas de Trici entraban en el portal. Rexxie tragó saliva.", "Huellas entrando en luz azul.", "portal", "valentía"),
            ("Entrando juntos", "Uno por uno, todos cruzaron. Nadie se quedó atrás.", "Grupo entrando en la máquina.", "portal", "unión"),
            ("Viaje temporal", "Todo giró con estrellas, relojes y burbujas. Mega gritó: —¡Glu-glu-glu!", "Túnel de tiempo dinámico.", "túnel temporal", "diversión"),
            ("Caída en el pasado", "POP. Cayeron sobre hojas gigantes. Rexxie dijo: —Ya no estamos en el parque.", "Grupo en selva prehistórica.", "era de los dinosaurios", "sorpresa"),
            ("Mundo antiguo", "Había árboles enormes, montañas y huellas más grandes que una bicicleta.", "Paisaje prehistórico claro.", "selva antigua", "maravilla"),
            ("Más huellas", "Mía encontró marcas de Trici. Velo susurró: —Y no está sola.", "Mía y Velo analizando rastros.", "sendero antiguo", "tensión suave"),
            ("El rugido", "BUM, BUM, BUM. Un rugido movió las hojas. —Ese no fui yo —dijo Rexxie.", "Sombras grandes entre árboles.", "selva", "miedo suave"),
            ("Gran T-Rex", "Apareció un T-Rex enorme. Era serio, pero sus ojos no parecían malos.", "T-Rex adulto imponente y protector.", "claro", "respeto"),
            ("Trici está allí", "Trici estaba detrás del T-Rex. No parecía indefensa: estaba tranquila y alerta.", "Trici protegida detrás del T-Rex.", "claro", "alivio"),
            ("El protector", "El T-Rex se puso delante de Trici para cuidar de ella.", "T-Rex alejando un peligro sin daño.", "claro", "protección"),
            ("No es enemigo", "Dipo dijo: —A veces alguien grande solo quiere cuidar.", "Rexxie observando con admiración.", "rocas", "comprensión"),
            ("Esperar la noche", "Mía quería correr, pero Luna pidió paciencia. Lo harían sin asustar a nadie.", "Equipo escondido esperando.", "atardecer", "prudencia"),
            ("Noche prehistórica", "Las estrellas eran enormes. El gran T-Rex se quedó dormido.", "T-Rex dormido bajo estrellas.", "claro", "calma"),
            ("Rescate silencioso", "Caminaron pasito a pasito. Mega hizo GLUP y todos se quedaron quietos.", "Rescate cómico en silencio.", "claro", "suspenso divertido"),
            ("Trici vuelve", "Mía abrazó a Trici. —Sabía que vendrían —dijo Trici.", "Abrazo con T-Rex dormido al fondo.", "claro", "ternura"),
            ("Al portal", "Velo encontró el camino. Todos corrieron hacia la luz azul.", "Equipo regresando al portal.", "selva", "urgencia"),
            ("Regreso temporal", "Relojes, burbujas y estrellas giraron otra vez.", "Viaje temporal con Trici recuperada.", "túnel temporal", "emoción"),
            ("De vuelta", "POP. El campamento seguía allí. Y Trici también.", "Regreso feliz al campamento.", "campamento", "alegría"),
            ("Estrella fugaz", "Esa noche vieron una estrella fugaz. Luna susurró: —Pidamos un deseo.", "Grupo mirando estrella fugaz.", "campamento", "esperanza"),
            ("Más aventuras", "Todos pidieron más aventuras. Muy lejos, una luz azul parpadeó.", "Grupo unido con luz azul lejana.", "cielo nocturno", "gancho"),
        ],
        "characters": ["Rexxie", "Dipo", "Trici", "Velo", "Mega", "Maxi", "Luna", "Teo", "Mía", "Leo", "Gran T-Rex protector"],
        "locations": ["campamento urbano", "túnel de raíces", "Máquina del Tiempo", "era de los dinosaurios"],
        "objects": ["Máquina del Tiempo", "huellas de Trici", "linternas", "mapa"],
        "challenges": ["seguir huellas", "cruzar el portal", "entender al T-Rex protector", "rescatar a Trici sin asustar"],
    },
    "book_03_el_secreto_del_platillo_azul": {
        "num": "03",
        "title": "El Secreto del Platillo Azul",
        "theme": "descubrimiento del platillo, Luke y Olic, alienígenas traviesos y poderes del Cofre Dorado",
        "hook": "El equipo descubre que no está solo en el universo.",
        "pages": [
            ("Portada", "Los Dinoamigos 3: El Secreto del Platillo Azul.", "Rexxie, Leo, Luke y Olic frente al Platillo Azul.", "ruinas y cielo", "asombro"),
            ("Campamento tranquilo", "Después del deseo, todos volvieron a dormir. La noche parecía quieta.", "Campamento nocturno.", "campamento", "calma"),
            ("Rexxie despierta", "Rexxie vio algo azul moviéndose en el cielo.", "Rexxie mirando por encima de la tienda.", "campamento", "curiosidad"),
            ("Vuelve el platillo", "No era una estrella. Era el Platillo Azul.", "Platillo redondo y brillante.", "cielo", "misterio"),
            ("Despierten", "Rexxie corrió. —¡El Platillo Azul volvió!", "Rexxie despertando al grupo.", "campamento", "urgencia"),
            ("Todos miran", "Maxi abrió la boca. Mía observó la ruta. Leo susurró: —Nos llama.", "Grupo mirando al cielo.", "campamento", "asombro"),
            ("Rastro azul", "El platillo dejó una línea azul y desapareció tras las montañas.", "Rastro luminoso.", "cielo", "expectativa"),
            ("Camino nocturno", "Tomaron mochilas y siguieron la luz. Mega hizo burbujas de emoción.", "Equipo avanzando de noche.", "sendero", "aventura"),
            ("Ruinas antiguas", "Llegaron a piedras con símbolos azules que antes no brillaban.", "Ruinas circulares.", "ruinas", "misterio"),
            ("Alas de luz", "En el centro flotaban alas hechas de luz azul.", "Alas misteriosas brillando.", "ruinas", "maravilla"),
            ("Sombra voladora", "Una sombra cruzó la luna. No era el platillo.", "Silueta de Olic.", "cielo", "sorpresa"),
            ("Aparece Olic", "Un dinosaurio volador aterrizó. Sobre él iba Luke.", "Olic y Luke aterrizando.", "ruinas", "presentación"),
            ("Nuevo amigo", "—Soy Luke. Y él es Olic. —Skreee.", "Luke saludando al grupo.", "ruinas", "alegría"),
            ("Es una nave", "Luke explicó que la luz azul era una nave. Todos gritaron: —¿Una nave?", "Luke señalando el cielo.", "ruinas", "sorpresa"),
            ("Rampa azul", "El Platillo Azul bajó y abrió una rampa luminosa.", "Platillo sobre las ruinas.", "ruinas", "asombro"),
            ("Entramos juntos", "Trici dijo: —Si entramos, entramos juntos.", "Grupo subiendo la rampa.", "rampa", "valentía"),
            ("Interior redondo", "Había botones grandes, pantallas y tubos con burbujas. Teo miró un botón.", "Interior amigable de nave.", "nave", "humor"),
            ("Alienígenas traviesos", "Aparecieron alienígenas pequeños. —¡Protejan el cofre!", "Alienígenas cómicos con cascos.", "nave", "diversión"),
            ("Redes de luz", "Las redes brillaban, pero no hacían daño. Velo corrió entre ellas.", "Acción con redes luminosas.", "pasillo", "juego"),
            ("Pelea cómica", "Trici empujó un robot pequeño. Mega lanzó agua. Nadie se lastimó.", "Batalla caricaturesca.", "nave", "humor"),
            ("Puerta secreta", "Mía leyó símbolos. —Esto se piensa. Tocó tres luces azules.", "Mía abriendo puerta.", "pasillo", "inteligencia"),
            ("Cofre Dorado", "En una sala circular brillaba el Cofre Dorado.", "Cofre con dibujos de alas y estrellas.", "sala secreta", "maravilla"),
            ("Llave del equipo", "Solo se abrió cuando todos pusieron manos, patas, aletas y garras.", "Todos tocando el cofre.", "sala secreta", "unión"),
            ("Lluvia de luces", "El cofre soltó luces doradas y azules. Fue bonito, no peligroso.", "Luces rodeando al equipo.", "sala secreta", "magia"),
            ("Poderes Dinoamigos", "Rexxie recibió alas pequeñas, Dipo patas fuertes, Trici armadura, Velo garras veloces y Mega aletas turbo.", "Transformación de Dinoamigos.", "sala", "emoción"),
            ("Poderes niños", "Maxi recibió poder acuático, Luna alas luminosas, Teo patas veloces, Mía brazaletes, Leo botas de salto y Luke visor espacial.", "Niños con poderes.", "sala", "alegría"),
            ("Prueba de poderes", "Usaron sus poderes con cuidado. Rexxie gritó: —¡Mis alas funcionan!", "Equipo probando poderes.", "nave", "diversión"),
            ("Alienígenas se rinden", "Los alienígenas levantaron una banderita blanca. —Ya no lanzaremos redes.", "Rendición cómica.", "nave", "humor"),
            ("La nave parpadea", "Las luces se apagaban. Luke dijo: —¡Tenemos que salir!", "Grupo saliendo.", "rampa", "urgencia"),
            ("Vuelo sobre la ciudad", "Olic voló, Luna planeó y Mega rodó feliz en su carrito-acuario.", "Regreso nocturno a la ciudad.", "cielo urbano", "alegría"),
            ("Luke se une", "Luke preguntó si podía quedarse. Todos dijeron: —¡Claro!", "Grupo integrado en campamento.", "campamento", "amistad"),
            ("No estamos solos", "Miraron las estrellas. Ahora sabían que el universo guardaba más aventuras.", "Grupo unido bajo cielo estrellado.", "campamento", "gancho"),
        ],
        "characters": ["Rexxie", "Dipo", "Trici", "Velo", "Mega", "Olic", "Maxi", "Luna", "Teo", "Mía", "Leo", "Luke", "alienígenas traviesos"],
        "locations": ["campamento urbano", "ruinas de las alas", "Platillo Azul", "nave alienígena"],
        "objects": ["Platillo Azul", "alas misteriosas", "Cofre Dorado", "poderes"],
        "challenges": ["seguir la luz", "entrar en la nave", "superar redes de luz", "abrir el Cofre Dorado en equipo"],
    },
    "book_04_la_isla_perdida_de_los_dinosaurios": {
        "num": "04",
        "title": "La Isla Perdida de los Dinosaurios",
        "theme": "familias perdidas, mapa, retos de isla, rescate familiar, Aeron y marca alienígena",
        "hook": "Rexxie queda con una marca roja y deben buscar la Planta Secreta.",
        "pages": [
            ("Portada", "Los Dinoamigos 4: La Isla Perdida de los Dinosaurios.", "Equipo ante una isla mágica con Baruk en la entrada.", "isla perdida", "aventura"),
            ("Noche inquieta", "Todos dormían, pero Luke empezó a moverse en su saco.", "Campamento nocturno con Luke inquieto.", "campamento", "inquietud"),
            ("Pesadilla de Luke", "Luke soñó con una isla, padres atrapados y una puerta enorme.", "Sueño con isla y luces.", "sueño", "misterio"),
            ("Luke despierta", "—¡Despierten! —dijo Luke. Olic levantó la cabeza preocupado.", "Luke despertando con Olic.", "campamento", "alarma suave"),
            ("Padres atrapados", "Luke contó que vio a los padres de los Dinoamigos atrapados.", "Grupo escuchando a Luke.", "campamento", "preocupación"),
            ("Mapa dibujado", "Luke mostró un mapa con montañas, ríos, lagos y una isla escondida.", "Primer plano del mapa.", "campamento", "decisión"),
            ("Debemos ir", "Rexxie dijo: —Si nuestras familias están allí, no podemos esperar.", "Equipo decidido.", "campamento", "valentía"),
            ("Mochilas listas", "Prepararon linternas, cuerdas y comida. Maxi preguntó por pizza.", "Preparativos divertidos.", "campamento", "humor"),
            ("Montes verdes", "Salieron al amanecer siguiendo el mapa de Luke.", "Grupo caminando por montes.", "montes", "aventura"),
            ("Montañas y ríos", "Dipo miró lejos y Mega ayudó en el río.", "Montaña y río en composición clara.", "montañas y río", "trabajo en equipo"),
            ("Lago escondido", "Encontraron un lago brillante. Mía dijo: —La isla debe estar cerca.", "Lago con Olic volando.", "lago", "expectativa"),
            ("La isla aparece", "La niebla se abrió y apareció la Isla Perdida de los Dinosaurios.", "Isla mágica entre niebla.", "isla", "maravilla"),
            ("Baruk guardián", "Baruk, un oso guardián grande pero noble, bloqueó la entrada.", "Baruk imponente y amable.", "entrada de Baruk", "respeto"),
            ("Advertencia", "Baruk avisó que la isla tenía retos. Leo respondió: —Iremos juntos.", "Diálogo ante la entrada.", "entrada", "decisión"),
            ("Prueba del corazón", "Mía dijo: —Venimos por amor, no por tesoros. Baruk se apartó.", "Baruk dejando pasar.", "entrada", "confianza"),
            ("Primera trampa", "Rexxie pisó una piedra. CLICK. Todos se quedaron quietos.", "Piedra-trampa activada.", "sendero de isla", "suspenso"),
            ("Martillo Dormilón", "Un martillo blando bajó con BOOOM. El equipo esquivó sin daño.", "Trampa caricaturesca.", "sendero", "humor"),
            ("Descanso de Teo", "Teo resbaló y descansó con Luna y Dipo hasta sentirse mejor.", "Cuidado suave de Teo.", "isla", "cuidado"),
            ("Laberinto de las Risas", "Una estatua seria pidió que la hicieran reír.", "Laberinto con estatua.", "laberinto", "reto divertido"),
            ("Mega hace reír", "Mega explotó una burbuja en su nariz. La estatua se rio.", "Mega y estatua riendo.", "laberinto", "humor"),
            ("Puentes Saltarines", "Piedras flotantes subían y bajaban. Mía iluminó las correctas.", "Lago con piedras flotantes.", "lago", "concentración"),
            ("Cruce en equipo", "Olic llevó a Leo, Trici cruzó firme y Rexxie probó sus alas.", "Cruce dinámico.", "lago", "alegría"),
            ("Cámara de Protectores", "Guardianes de roca y musgo despertaron para probarlos.", "Guardianes mágicos no malvados.", "cámara", "respeto"),
            ("¿Por qué vienen?", "Cada Dinoamigo explicó que buscaba a su familia.", "Dinoamigos hablando ante guardianes.", "cámara", "emoción"),
            ("Reto de musgo", "Las lianas intentaron detenerlos, pero el equipo respondió sin hacer daño.", "Acción con lianas blandas.", "cámara", "valentía"),
            ("Rexxie se levanta", "Rexxie cayó sobre musgo suave y se levantó. —Estoy bien.", "Trici ayudando a Rexxie.", "cámara", "resiliencia"),
            ("Palabra secreta", "En la puerta dorada leyeron: lo que se busca con miedo se encuentra con amor. Dijeron: —Familia.", "Puerta dorada abriéndose.", "puerta familiar", "ternura"),
            ("Padres en luz", "Dentro estaban Orin, Tricero, Brachio y Crick en círculos luminosos.", "Padres dinosaurios atrapados sin dolor.", "cámara familiar", "alivio"),
            ("Reencuentro", "Orin abrazó a Rexxie. Tricero, Brachio y Crick abrazaron a sus hijos.", "Abrazo familiar grande.", "cámara", "alegría"),
            ("Falta Aeron", "Olic miró alrededor. Aeron no estaba. Orin dijo que estaba en el espacio.", "Olic triste con Luke.", "cámara", "preocupación"),
            ("Salto espacial", "Luke usó su visor y una burbuja azul llevó al equipo a una nave lejana.", "Burbuja espacial frente a nave.", "espacio", "asombro"),
            ("Aeron y la marca", "Rescataron a Aeron. Una chispa dejó en Rexxie una marca roja. Doctor Lumo dijo: —Busquen la Planta Secreta.", "Aeron reunido con Olic y Rexxie mirando su marca.", "regreso al campamento", "gancho"),
        ],
        "characters": ["Rexxie", "Dipo", "Trici", "Velo", "Mega", "Olic", "Luke", "Baruk", "Orin", "Tricero", "Brachio", "Crick", "Aeron", "Doctor Lumo"],
        "locations": ["campamento urbano", "Isla Perdida de los Dinosaurios", "entrada de Baruk", "laberinto de las risas", "cámara de los protectores", "espacio"],
        "objects": ["mapa de Luke", "visor espacial azul", "círculos de luz", "marca alienígena de Rexxie"],
        "challenges": ["convencer a Baruk", "Martillo Dormilón", "Laberinto de las Risas", "Puentes Saltarines", "Cámara de Protectores", "rescate espacial"],
    },
    "book_05_en_busca_de_la_planta_secreta": {
        "num": "05",
        "title": "En busca de la Planta Secreta",
        "theme": "sanación, retos, inteligencia, amistad y aceptación de la marca",
        "hook": "La marca de Rexxie deja de doler y queda como símbolo de valentía.",
        "pages": [
            ("Portada", "Los Dinoamigos 5: En busca de la Planta Secreta.", "Rexxie con marca roja frente a camino, pared dorada y jardín mágico.", "camino al jardín", "esperanza"),
            ("Mañana en el campamento", "El sol salió. Rexxie descansaba junto a Leo y su marca brillaba suave.", "Campamento de día.", "campamento", "calma"),
            ("Trici recuerda", "Trici abrió los ojos. —¡Tenemos que buscar la Planta Secreta!", "Trici despertando al equipo.", "campamento", "urgencia"),
            ("Rexxie y la marca", "La marca no era una herida, pero a veces molestaba. Leo tomó su patita.", "Leo cuidando a Rexxie.", "campamento", "ternura"),
            ("Primero un mapa", "Mía dijo que debían preguntar al Doctor Lumo. Mega estuvo de acuerdo: —Glu-glu, mejor mapa.", "Equipo planificando.", "campamento", "inteligencia"),
            ("Doctor Lumo", "Doctor Lumo abrió su laboratorio. —Sabía que vendrían.", "Laboratorio luminoso.", "laboratorio", "confianza"),
            ("Sótano secreto", "Bajaron a un sótano con cajas, ruedas, linternas y mapas viejos.", "Sótano curioso.", "sótano secreto", "misterio"),
            ("Mapa verde y dorado", "Doctor Lumo entregó el mapa. —Los llevará al Jardín de la Planta Secreta.", "Mapa brillante.", "sótano", "asombro"),
            ("Advertencia amable", "—Algunos retos se ganan pensando —dijo Doctor Lumo.", "Equipo escuchando.", "laboratorio", "atención"),
            ("Empieza el viaje", "Atravesaron ríos y montañas. Maxi preguntó si la planta se escondía.", "Camino de aventura.", "ríos y montañas", "humor"),
            ("Rugo guardián", "Rugo bloqueó una puerta. —Para pasar, necesito el susto más enorme.", "Rugo y guardianes dinosaurio.", "puerta de Rugo", "reto"),
            ("Susto divertido", "Velo corrió, Mega hizo burbujas y Dipo se puso alto. Rugo no se asustó.", "Intentos cómicos.", "puerta", "humor"),
            ("Rugido de Rexxie", "Rexxie rugió y aparecieron siluetas luminosas. Rugo dijo: —¡Miedo divertido!", "Rexxie con siluetas mágicas.", "puerta", "valentía"),
            ("Red mágica", "Una red brillante atrapó a Trici sin hacerle daño.", "Trici en red de luz.", "bosque", "suspenso"),
            ("Nubo aparece", "Nubo dijo: —Para encontrar una planta que ayuda, aprendan a ayudar.", "Nubo junto a la red.", "bosque", "sabiduría"),
            ("Olic libera a Trici", "Olic cortó cuerdas con cuidado. Mía iluminó nudos y Luna ayudó.", "Rescate de Trici.", "bosque", "trabajo en equipo"),
            ("Cuidar a Olic", "Olic se golpeó suavemente una pata. Nubo puso una hoja fresca.", "Luke cuidando a Olic.", "bosque", "cuidado"),
            ("Pared Dorada", "Dorán dijo: —Para pasar, deben romperme. La pared no se movió.", "Pared dorada gigante.", "pared dorada", "reto"),
            ("La contraseña", "Mía leyó letras pequeñas. Teo recordó: —Unidos somos más fuertes.", "Pared abriéndose.", "pared dorada", "inteligencia"),
            ("Sombrín", "Sombrín pidió que dijeran su miedo verdadero.", "Guardián violeta suave.", "sala violeta", "miedo suave"),
            ("Intentos", "Maxi y Teo probaron respuestas. Solo quedaba una oportunidad.", "Equipo pensando.", "sala violeta", "tensión suave"),
            ("Miedo verdadero", "Leo dijo: —Tememos que Rexxie se haga daño. Sombrín abrió la puerta.", "Leo y Rexxie juntos.", "sala violeta", "honestidad"),
            ("Reto del agua", "Flotón preguntó si beber mucha agua hacía flotar como globo. Mega dijo que sí.", "Flotón en burbuja.", "sala de agua", "humor"),
            ("Maxi responde", "Maxi explicó que para flotar se necesita nadar, aire o ayuda.", "Maxi respondiendo.", "sala de agua", "sentido común"),
            ("Pregunta trampa", "Flotón preguntó cuántos dinosaurios vivos hay en el mundo moderno. Mía pensó.", "Mía ante pregunta.", "sala de agua", "curiosidad"),
            ("Respuesta inteligente", "Mía dijo que para los humanos están extintos, pero ellos saben que algunos siguen aquí.", "Puerta acuática abriéndose.", "sala de agua", "inteligencia"),
            ("T-Rex robots", "El último reto era una sala de T-Rex robots que decían: RAAWR-BIP.", "Robots cómicos.", "sala final", "sorpresa"),
            ("Batalla divertida", "El equipo apagó robots con agua, símbolos y trabajo en equipo. Salía humo en forma de flor.", "Acción no violenta contra robots.", "sala final", "diversión"),
            ("Orin ayuda", "Orin apareció. —Rugamos juntos. Padre e hijo apagaron los robots.", "Orin y Rexxie rugiendo.", "sala final", "familia"),
            ("Jardín secreto", "Encontraron un jardín vivo con flores azules, raíces luminosas y hojas que cantaban.", "Jardín mágico.", "Jardín de la Planta Secreta", "maravilla"),
            ("Doctor Florio", "Doctor Florio explicó: —La Planta Secreta es un jardín vivo.", "Doctor Florio en el jardín.", "jardín", "descubrimiento"),
            ("La marca ya no duele", "Florio tocó la marca con una hoja dorada. No desapareció, pero dejó de doler y brilló como una estrella roja.", "Rexxie feliz con todos alrededor.", "jardín", "aceptación"),
        ],
        "characters": ["Rexxie", "Dipo", "Trici", "Velo", "Mega", "Olic", "Maxi", "Luna", "Teo", "Mía", "Leo", "Luke", "Doctor Lumo", "Doctor Florio", "Nubo", "Rugo", "Dorán", "Sombrín", "Flotón", "Orin"],
        "locations": ["laboratorio del Doctor Lumo", "sótano secreto", "puerta de Rugo", "Pared Dorada", "sala de Sombrín", "Jardín de la Planta Secreta"],
        "objects": ["mapa de la Planta Secreta", "marca alienígena de Rexxie", "hoja dorada", "T-Rex robots"],
        "challenges": ["Sustazo de Rugo", "red mágica de Trici", "contraseña de Dorán", "Guardián de los Miedos", "preguntas de Flotón", "T-Rex robots"],
    },
}

PAIRINGS = {
    "Rexxie": "Leo", "Dipo": "Luna", "Trici": "Mía", "Velo": "Teo", "Mega": "Maxi", "Olic": "Luke"
}

CHARACTERS = {
    "Rexxie": ("Dinosaurio principal", "Libro 1", "T-Rex bebé valiente, protector, curioso y un poco dramático.", "Pequeño, ojos expresivos, dientes redondeados, alas de energía desde Libro 3, marca roja desde Libro 4.", "Valiente, sensible, teatral.", "Corazón emocional de la saga y compañero de Leo.", "Se apoya en Leo y aprende de Orin.", "Alas pequeñas de energía; rugido valiente.", "¡Rawr! Espera... ¿eso sonó pequeño?", "La marca roja queda como pequeña estrella desde el final del Libro 5."),
    "Dipo": ("Dinosaurio principal", "Libro 1", "Diplodocus bebé dulce y observador.", "Cuello largo, cuerpo redondeado, sonrisa amable, patas fuertes desde Libro 3.", "Tranquilo, amable, cuidadoso.", "Calma al grupo y ayuda a mirar lejos.", "Dinoamigo de Luna.", "Patas fuertes y cuello útil para ayudar.", "Respiremos. Podemos verlo desde arriba.", "Mantener silueta de cuello largo y gesto dulce."),
    "Trici": ("Dinosaurio principal", "Libro 1", "Triceratops bebé fuerte y cariñosa.", "Tres cuernitos redondeados, escudo suave, armadura brillante desde Libro 3.", "Protectora, cabezota, valiente.", "Activa misiones en Libros 2 y 5.", "Dinoamiga de Mía.", "Armadura brillante protectora.", "Si vamos, vamos juntos.", "Nunca mostrar cuernos agresivos; siempre redondeados."),
    "Velo": ("Dinosaurio principal", "Libro 1", "Velociraptor bebé rápido e inquieto.", "Pequeño, ágil, postura de corredor, garras veloces desde Libro 3.", "Travieso, inteligente, impulsivo.", "Explorador y rastreador.", "Dinoamigo de Teo.", "Velocidad y garras veloces no dañinas.", "¡Yo pruebo el camino!", "Debe parecer veloz, no feroz."),
    "Mega": ("Dinosaurio principal", "Libro 1", "Megalodón bebé alegre y glotón.", "Tiburón prehistórico bebé con carrito-acuario transparente y aletas turbo desde Libro 3.", "Bromista, hambriento, tierno.", "Humor acuático y apoyo en agua.", "Dinoamigo de Maxi.", "Burbujas, nado, aletas turbo.", "¡Glu-glu! ¿Eso se come?", "Siempre necesita agua o carrito-acuario en el mundo moderno."),
    "Olic": ("Dinosaurio principal", "Libro 3", "Dinosaurio volador noble y protector.", "Alas grandes, azul verdoso, marcas luminosas, ojos dorados.", "Serio al principio, leal, veloz.", "Introduce a Luke y el arco de Aeron.", "Dinoamigo de Luke; hijo de Aeron.", "Vuelo rápido y rescate aéreo.", "Skreee.", "Mantener marcas luminosas y tamaño suficiente para llevar a Luke."),
    "Maxi": ("Niño principal", "Libro 1", "Niño moreno, alegre y expresivo.", "Ropa cómoda de explorador, sonrisa grande.", "Divertido, energético, exagerado.", "Aporta humor y cuida de Mega.", "Compañero de Mega.", "Poder acuático desde Libro 3.", "¿Alguien trajo merienda?", "Puede llamarse Maximiliano en futuro, pero usar Maxi."),
    "Luna": ("Niña principal", "Libro 1", "Niña rubia, soñadora y dulce.", "Cabello claro, mirada calma, alas luminosas desde Libro 3.", "Sensible, observadora, tranquilizadora.", "Ayuda a regular el miedo del grupo.", "Compañera de Dipo.", "Alas luminosas.", "Respiremos. Estamos juntos.", "Mantener gesto sereno y postura cuidadora."),
    "Teo": ("Niño principal", "Libro 1", "Niño con pelo rizado y mucha curiosidad.", "Pelo rizado, mochila, patas veloces desde Libro 3.", "Inquieto, aventurero, impulsivo.", "Gag de querer tocar botones.", "Compañero de Velo.", "Patas veloces.", "Prometo no tocar nada... casi nada.", "Su impulsividad debe ser cómica, no peligrosa."),
    "Mía": ("Niña principal", "Libro 1", "Niña con rasgos asiáticos, inteligente y analítica.", "Ropa de exploradora ordenada, brazaletes de energía desde Libro 3.", "Lógica, valiente, observadora.", "Resuelve símbolos y acertijos.", "Compañera de Trici.", "Brazaletes de energía.", "Esperen. Esto no se rompe. Se piensa.", "Mantener diversidad y rol de inteligencia práctica."),
    "Leo": ("Niño principal", "Libro 1", "Niño pelirrojo o con pecas, valiente y noble.", "Pecas, expresión expresiva, botas de salto desde Libro 3.", "Valiente, gracioso, honesto con el miedo.", "Acompaña emocionalmente a Rexxie.", "Compañero de Rexxie.", "Botas de salto gigante.", "Tengo miedo, pero voy igual.", "Su valentía incluye decir la verdad sobre el miedo."),
    "Luke": ("Niño principal", "Libro 3", "Niño aventurero y algo misterioso.", "Ropa de explorador aéreo, visor espacial azul desde Libro 3.", "Valiente, tecnológico, observador.", "Conecta al grupo con Olic, Aeron y el espacio.", "Compañero de Olic.", "Visor espacial azul.", "Mi visor dice que esto no es normal.", "No debe parecer adulto ni demasiado serio."),
    "Orin": ("Padre dinosaurio", "Libro 4", "Padre T-Rex de Rexxie, grande y protector.", "T-Rex adulto amable, mirada cálida.", "Protector, firme.", "Apoya a Rexxie en Libro 5.", "Padre de Rexxie.", "Rugido protector.", "Rugamos juntos.", "Imponente pero nunca terrorífico."),
    "Tricero": ("Padre dinosaurio", "Libro 4", "Padre de Trici.", "Triceratops adulto con cuernos redondeados.", "Fuerte, cariñoso.", "Reencuentro familiar.", "Padre de Trici.", "Protección.", "Mi pequeña protectora.", "No llamarlo Triceratops como nombre propio."),
    "Brachio": ("Padre dinosaurio", "Libro 4", "Padre de Dipo.", "Diplodocus adulto de cuello largo.", "Calmado, sabio.", "Reencuentro familiar.", "Padre de Dipo.", "Mirada lejana.", "Siempre hay camino.", "Silueta alta y dulce."),
    "Crick": ("Padre dinosaurio", "Libro 4", "Padre de Mega.", "Megalodón adulto amable, burbujas grandes.", "Alegre, acuático.", "Reencuentro familiar de Mega.", "Padre de Mega.", "Burbujas gigantes.", "Glu-glu grande.", "Evitar aspecto amenazante."),
    "Aeron": ("Padre dinosaurio", "Libro 4", "Padre volador de Olic.", "Dinosaurio volador adulto con marcas luminosas.", "Noble, paciente.", "Motivo del rescate espacial.", "Padre de Olic.", "Vuelo protector.", "Skreee profundo.", "Mantener vínculo visual con Olic."),
    "Baruk": ("Aliado guardián", "Libro 4", "Oso guardián de la Isla Perdida.", "Oso grande, collar de piedra, mirada noble.", "Serio, protector, no villano.", "Advierte y prueba al grupo.", "Guardián de la entrada.", "Autoridad mágica.", "La isla prueba el corazón.", "No hacerlo terrorífico."),
    "Doctor Lumo": ("Aliado", "Libro 4", "Médico de tecnología mágica.", "Bata clara, luces azules, herramientas amables.", "Sabio, calmado.", "Indica buscar la Planta Secreta y entrega mapa.", "Ayuda a Rexxie.", "Lectura de energía alienígena.", "Necesitarán un mapa.", "Debe parecer médico mágico infantil."),
    "Doctor Florio": ("Aliado", "Libro 5", "Médico del Jardín de la Planta Secreta.", "Ropa verde, hoja dorada, sonrisa serena.", "Tierno, sabio.", "Cierra el arco de sanación.", "Cuida plantas y ayuda a Rexxie.", "Escucha plantas especiales.", "Algunas marcas se aprenden a llevar sin dolor.", "Nunca presentar como curandero oscuro."),
    "Nubo": ("Guardián mágico", "Libro 5", "Dinosaurio raro que enseña ayuda mutua.", "Formas suaves, nube luminosa cerca.", "Juguetón, sabio.", "Reto de la red mágica.", "Ayuda a liberar a Trici.", "Hojas suaves.", "Primero aprendan a ayudar.", "Aspecto amable."),
    "Rugo": ("Guardián mágico", "Libro 5", "Guardián del susto enorme.", "Dinosaurio grande con expresión teatral.", "Dramático, divertido.", "Reto de valentía de Rexxie.", "Prueba al equipo.", "Susto mágico seguro.", "¡Miedo divertido!", "El susto debe ser cómico."),
    "Dorán": ("Guardián mágico", "Libro 5", "Voz de la Pared Dorada.", "Rostro grabado en pared dorada.", "Bromista, enigmático.", "Reto de contraseña.", "Prueba a Mía y Teo.", "Abre paso con frase correcta.", "Correcto.", "No mostrar como amenaza."),
    "Sombrín": ("Guardián mágico", "Libro 5", "Guardián de los Miedos.", "Sombra violeta suave, ojos amables.", "Sereno, profundo.", "Permite nombrar el miedo real.", "Ayuda a Leo y Rexxie.", "Puerta emocional.", "Ese sí es un miedo verdadero.", "Miedo suave, nunca terror."),
    "Flotón": ("Guardián mágico", "Libro 5", "Guardián de preguntas acuáticas.", "Personaje redondo dentro de burbuja.", "Divertido, lógico.", "Reto de preguntas trampa.", "Prueba a Maxi y Mía.", "Burbujas de agua.", "Incorrecto, pero divertido.", "Debe sentirse como juego."),
}


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def people_for(book, page_index):
    if book["num"] == "01":
        if page_index <= 28:
            return [c for c in ["Rexxie", "Dipo", "Trici", "Velo", "Mega"] if c in book["characters"]]
        if page_index == 29:
            return ["Maxi", "Luna", "Teo", "Mía", "Leo"]
        return ["Rexxie", "Dipo", "Trici", "Velo", "Mega", "Maxi", "Luna", "Teo", "Mía", "Leo"]
    base = book["characters"][:]
    if page_index <= 3:
        return [c for c in base if c in ("Rexxie", "Dipo", "Trici", "Velo", "Mega", "Olic", "Maxi", "Luna", "Teo", "Mía", "Leo", "Luke")][:6] or base[:4]
    return base[:10]


def page_by_page(book):
    out = [f"# {book['title']} - page by page", "", "Cada página mantiene una acción clara, emoción visible y una composición apta para ilustración y libro de colorear."]
    for idx, (title, text, visual, env, emotion) in enumerate(book["pages"], start=1):
        chars = people_for(book, idx)
        prompt = f"{STYLE} Scene: {visual} Environment: {env}. Emotion: {emotion}. {MAGIC if any(w in visual.lower() or w in env.lower() for w in ['azul','platillo','tiempo','mágic','nave','espacio','jardín']) else ''}".strip()
        out += [
            "",
            f"## Página {idx:02d} — {title}",
            "",
            "### Texto narrativo",
            "",
            text,
            "",
            "### Descripción visual",
            "",
            visual,
            "",
            "### Personajes presentes",
            "",
            *[f"- {c}" for c in chars],
            "",
            "### Entorno",
            "",
            env,
            "",
            "### Emoción principal",
            "",
            emotion,
            "",
            "### Prompt visual base",
            "",
            prompt,
            "",
            "### Notas para libro de colorear",
            "",
            "- contornos claros",
            "- personajes grandes",
            "- evitar exceso de detalles",
            "- emoción fácil de leer",
        ]
    return "\n".join(out)


def synopsis(book):
    return f"""
    # {book['title']} - sinopsis

    ## Concepto

    Libro {book['num']} de la saga Los Dinoamigos. El foco editorial es {book['theme']}.

    ## Resumen breve

    {book['pages'][0][1]} La aventura avanza desde {book['pages'][1][3]} hasta {book['pages'][-1][3]}, con retos pensados para niños de 5 a 10 años, humor visual, peligro suave y resolución por amistad.

    ## Problema principal

    El equipo debe resolver una misión clara sin perder la ternura de la historia original.

    ## Resolución

    {book['hook']}

    ## Puente de continuidad

    Este libro conserva los nombres oficiales, refuerza los vínculos niño-Dinoamigo y prepara el siguiente paso de la temporada sin convertir la saga en ciencia ficción dura.
    """


def full_story(book):
    paragraphs = [f"# {book['title']} - cuento completo", "", f"Este cuento está editado para lectura en voz alta, con frases cortas, escenas visuales y emoción clara.", ""]
    for idx, (_, text, _, _, _) in enumerate(book["pages"], start=1):
        if idx == 1:
            continue
        paragraphs.append(text)
    paragraphs.append("")
    paragraphs.append(f"Y así termina esta aventura: {book['hook']}")
    return "\n\n".join(paragraphs)


def dialogues(book):
    common = """
    # Diálogos

    Diálogos cortos, repetibles y útiles para cuento ilustrado o animación.

    Rexxie:
    —¡Rawr! Espera... ¿eso sonó pequeño?

    Mega:
    —¡Glu-glu! ¿Eso se come?

    Teo:
    —Prometo no tocar nada... casi nada.

    Mía:
    —Esperen. Esto no se rompe. Se piensa.

    Luna:
    —Respiremos. Estamos juntos.

    Leo:
    —Tengo miedo, pero voy igual.

    Maxi:
    —¿Alguien trajo merienda?

    Luke:
    —Mi visor dice que esto no es normal.

    Olic:
    —Skreee.
    """
    extracted = [f"- —{p[1].split('—')[-1].strip()}" for p in book["pages"] if "—" in p[1]]
    extras = "\n\n## Frases específicas del libro\n\n" + "\n".join(extracted[:12])
    return common + extras


def continuity(book):
    return f"""
    # Notas de continuidad

    ## Nombres normalizados

    Usar Rexxie, Dipo, Trici, Velo, Mega y Olic. Usar Maxi, Luna, Teo, Mía, Leo y Luke. No usar Rexy, Trexy, Olick ni variantes.

    ## Estado del libro

    - Tema central: {book['theme']}.
    - Gancho final: {book['hook']}.
    - Objetos principales: {', '.join(book['objects'])}.
    - Lugares principales: {', '.join(book['locations'])}.

    ## Reglas visuales

    Los dinosaurios son tiernos, expresivos y reconocibles. Los peligros son suaves, mágicos o caricaturescos. Las escenas deben poder convertirse en imagen a color y en página de colorear.

    ## Riesgos evitados

    - No violencia gráfica.
    - No terror realista.
    - No explicaciones científicas complejas.
    - No alienígenas aterradores.
    """


def prompts(book):
    chars = "\n\n".join(f"## {c}\n\n{STYLE} Character reference for {c}: {CHARACTERS.get(c, ('', '', c, 'rasgos claros', '', '', '', '', '', ''))[3] if c in CHARACTERS else c}. Consistent children's book design, friendly expression, readable silhouette." for c in book["characters"])
    scenes = "\n\n".join(f"## Página {i:02d} — {p[0]}\n\n{STYLE} {p[2]} Environment: {p[3]}. Emotion: {p[4]}." for i, p in enumerate(book["pages"], start=1))
    coloring = "\n\n".join(f"## Página {i:02d} — {p[0]}\n\n{COLORING} Scene: {p[2]}." for i, p in enumerate(book["pages"], start=1))
    cover = f"""
    # Prompt de portada - {book['title']}

    {STYLE}

    Full color illustrated children's book cover for "{book['title']}". {book['pages'][0][2]} Large friendly title area, readable composition, magical adventure tone, cute baby dinosaurs, diverse children explorers, no scary horror, no realistic violence.

    ## Versión line art

    {COLORING} Cover composition for "{book['title']}", large central characters and clear background shapes.
    """
    global_style = f"""
    # Estilo global de prompts

    ## Prompt maestro

    {STYLE}

    ## Escenas mágicas

    {MAGIC}

    ## Escenas modernas

    Modern city park, children explorer camp, tents, flashlights, backpacks, friendly urban environment, buses, crosswalks, fountains, buildings, ice cream shop, joyful children walking small pet-sized dinosaurs, clean bold outlines, children's coloring book style.

    ## Libro de colorear

    {COLORING}
    """
    return {
        "global_prompt_style.md": global_style,
        "character_prompts.md": "# Prompts de personajes\n\n" + chars,
        "scene_prompts.md": "# Prompts por escena\n\n" + scenes,
        "coloring_book_prompts.md": "# Prompts para libro de colorear\n\n" + coloring,
        "cover_prompt.md": cover,
    }


def readme_book(book):
    return f"""
    # {book['title']}

    Libro {book['num']} de Los Dinoamigos.

    ## Foco editorial

    {book['theme']}.

    ## Archivos clave

    - `story/synopsis.md`: resumen editorial.
    - `story/full_story.md`: cuento completo para lectura.
    - `story/page_by_page.md`: estructura obligatoria de 32 páginas.
    - `story/dialogues.md`: voces y frases útiles para animación.
    - `story/continuity_notes.md`: reglas del libro y puente de saga.
    - `prompts/`: prompts de estilo, personajes, escenas, colorear y portada.
    - `animation/`: outline, storyboard, shot list y notas de movimiento.

    ## Cierre

    {book['hook']}
    """


def animation_docs(book):
    return {
        "episode_outline.md": f"""# Outline de episodio - {book['title']}

## Acto 1
Presentación del problema y decisión del equipo.

## Acto 2
Viaje, retos y descubrimientos. La dificultad se resuelve con cooperación, humor e inteligencia.

## Acto 3
Clímax visual, cierre emocional y gancho suave.

## Gancho final
{book['hook']}
""",
        "storyboard_notes.md": f"""# Notas de storyboard - {book['title']}

- Mantener planos claros con personajes grandes.
- Usar primeros planos para emociones: sorpresa, ternura, miedo suave y alegría.
- Los retos deben leerse visualmente sin explicación larga.
- Repetir burbujas, luces azules y mapas como signos de saga.
""",
        "shot_list.md": "# Shot list\n\n" + "\n".join(f"{i:02d}. {p[0]}: plano general claro, acción principal legible, cierre emocional en expresión de personajes." for i, p in enumerate(book["pages"], start=1)),
        "character_motion_notes.md": f"""# Notas de movimiento

- Rexxie se mueve con valentía torpe y gestos dramáticos.
- Dipo se mueve despacio, estable y amable.
- Trici avanza firme y protectora.
- Velo entra y sale de plano con energía.
- Mega genera humor con burbujas y movimientos acuáticos.
- Olic vuela con movimientos amplios y nobles cuando aparece.
""",
    }


def simple_index(title, items):
    return f"# {title}\n\n" + "\n\n".join(f"## {item}\n\nDocumento de referencia para producción visual y continuidad. Mantener estilo infantil, claro y apto para colorear." for item in items)


def build_books():
    for folder, book in BOOKS.items():
        root = ROOT / folder
        write(root / "README.md", readme_book(book))
        write(root / "story" / "synopsis.md", synopsis(book))
        write(root / "story" / "full_story.md", full_story(book))
        write(root / "story" / "page_by_page.md", page_by_page(book))
        write(root / "story" / "dialogues.md", dialogues(book))
        write(root / "story" / "continuity_notes.md", continuity(book))
        for name, content in prompts(book).items():
            write(root / "prompts" / name, content)
        for name, content in animation_docs(book).items():
            write(root / "animation" / name, content)
        for sub in ["characters", "locations", "objects", "challenges"]:
            write(root / sub / "README.md", simple_index(sub.title(), book[sub]))
        for sub in ["images/references", "images/drafts", "images/finals", "images/coloring_pages", "scenes"]:
            write(root / sub / "README.md", f"# {sub}\n\nCarpeta de trabajo para {book['title']}. Mantener nombres claros y relación con `story/page_by_page.md`.\n")


def bible_docs():
    chars_master = ["# Personajes maestro"]
    for name, data in CHARACTERS.items():
        fields = ["Tipo de personaje", "Primera aparición", "Descripción breve", "Rasgos visuales", "Personalidad", "Rol narrativo", "Relación con otros personajes", "Poderes o habilidades", "Frases típicas", "Reglas de continuidad visual"]
        chars_master.append(f"\n## {name}\n")
        for field, value in zip(fields, data):
            chars_master.append(f"### {field}\n\n{value}\n")
    objects = [
        "huevos mágicos", "Platillo Azul", "burbujas mágicas", "Máquina del Tiempo", "carrito-acuario de Mega", "mapa de Luke", "Cofre Dorado", "alas misteriosas", "mapa de la Planta Secreta", "marca alienígena de Rexxie", "Jardín de la Planta Secreta",
        "alas de Rexxie", "patas fuertes de Dipo", "armadura de Trici", "garras veloces de Velo", "aletas turbo de Mega", "alas luminosas de Luna", "poder acuático de Maxi", "patas veloces de Teo", "brazaletes de Mía", "botas de salto de Leo", "visor espacial de Luke",
    ]
    powers = ["# Poderes y objetos"]
    for item in objects:
        powers.append(f"""
## {item}

### Primera aparición

Ver matriz de continuidad.

### Descripción

Elemento mágico-tecnológico de fantasía infantil.

### Función narrativa

Ayuda a activar aventura, resolver un reto o mostrar crecimiento emocional.

### Reglas de uso

Debe usarse con trabajo en equipo y límites claros.

### Límites

No resuelve todo solo, no causa daño realista y no vuelve invencible al grupo.

### Riesgos de continuidad

No cambiar nombre, forma principal ni primera aparición sin anotarlo.

### Prompt visual base

{STYLE} Visual object reference for {item}, clear silhouette, friendly magical technology, coloring book compatible.
""")
    locations = ["valle prehistórico", "pradera", "selva", "océano", "cueva brillante", "parque moderno", "campamento urbano", "túnel de raíces", "Máquina del Tiempo", "era de los dinosaurios", "ruinas de las alas", "Platillo Azul", "nave alienígena", "Isla Perdida de los Dinosaurios", "entrada de Baruk", "laberinto de las risas", "cámara de los protectores", "espacio", "laboratorio del Doctor Lumo", "sótano secreto", "Jardín de la Planta Secreta"]
    matrix_rows = [
        ("Rexxie", "nace", "busca a Trici", "recibe alas", "busca a Orin y recibe marca", "marca sana", "valiente con estrella roja"),
        ("Dipo", "nace", "ayuda a rastrear", "recibe patas fuertes", "encuentra a Brachio", "apoya retos", "calma del grupo"),
        ("Trici", "nace", "desaparece y vuelve", "recibe armadura", "encuentra a Tricero", "recuerda misión y es rescatada", "protectora activa"),
        ("Velo", "nace", "rastrea huellas", "recibe garras veloces", "explora retos", "ayuda contra robots", "aprende a pensar"),
        ("Mega", "nace", "aporta humor", "recibe aletas turbo", "encuentra a Crick", "resuelve humor acuático", "gag de burbujas"),
        ("Olic", "-", "-", "aparece con Luke", "busca a Aeron", "libera a Trici", "Dinoamigo del equipo"),
        ("Niños", "adoptan", "rescatan", "reciben poderes", "viajan a isla", "superan acertijos", "equipo completo"),
        ("Platillo Azul", "lleva al futuro", "parpadea", "revela nave", "permite espacio", "referencia mágica", "misterio abierto"),
        ("Máquina del Tiempo", "-", "primer uso", "regla de magia temporal", "-", "-", "herramienta controlada"),
        ("Cofre Dorado", "-", "-", "da poderes", "poderes se usan", "poderes se usan", "poderes limitados"),
        ("Poderes", "-", "-", "aparecen", "ayudan en retos", "ayudan en cura", "activos con límites"),
        ("Padres dinosaurios", "-", "T-Rex protector anticipa tema", "-", "rescatados", "Orin ayuda", "familias reunidas"),
        ("Marca de Rexxie", "-", "-", "-", "aparece", "deja de doler", "estrella roja de valentía"),
        ("Planta Secreta", "-", "-", "-", "mencionada", "jardín vivo", "símbolo de sanación"),
    ]
    matrix = "# Matriz de continuidad\n\n| Elemento | Libro 1 | Libro 2 | Libro 3 | Libro 4 | Libro 5 | Estado final |\n|---|---|---|---|---|---|---|\n" + "\n".join("| " + " | ".join(r) + " |" for r in matrix_rows)
    return {
        "README.md": """# Biblia de Los Dinoamigos

Carpeta global de continuidad, reglas editoriales, estilo visual, personajes, objetos, lugares y adaptación a animación. Usar antes de escribir nuevos libros, prompts o escenas.
""",
        "00_saga_overview.md": """# Vista general de la saga

## Concepto general

Los Dinoamigos es una saga infantil nacida de la imaginación de un niño de 6 años. Combina dinosaurios bebés, huevos mágicos, burbujas, campamentos, mapas, viajes en el tiempo, platillos voladores y amistad.

## Público objetivo

Niños y niñas de 5 a 10 años.

## Tono

Tierno, aventurero, colorido, mágico, familiar y seguro.

## Formato

Libro ilustrado, libro de colorear, storyboard y miniserie animada.

## Resumen de los 5 libros

1. Los Dinoamigos nacen: nacen, sobreviven a un meteorito lejano, viajan al futuro y son adoptados.
2. La Máquina del Tiempo: buscan a Trici, viajan al pasado y conocen a un T-Rex protector.
3. El Secreto del Platillo Azul: descubren la nave, conocen a Luke y Olic y reciben poderes.
4. La Isla Perdida de los Dinosaurios: rescatan a los padres y Rexxie recibe una marca.
5. En busca de la Planta Secreta: curan el dolor de la marca y la convierten en símbolo de valentía.

## Propuesta de temporada 1

Cinco episodios largos con arco de origen, descubrimiento, familia y aceptación.

## Promesa narrativa

Cada aventura empieza con asombro y termina con el equipo más unido.
""",
        "01_world_rules.md": f"""# Reglas del mundo

## Naturaleza del mundo

La saga es fantasía infantil con tecnología mágica. No debe convertirse en ciencia ficción dura.

## Platillo Azul

Es una nave amigable y misteriosa. Puede generar burbujas, luces azules y rutas espaciales, pero no resuelve misiones por sí sola.

## Máquina del Tiempo

Funciona como portal mágico-tecnológico. Se activa con huellas, luz azul y necesidad narrativa. No se usa para cambiar tragedias ni explicar paradojas complejas.

## Burbujas mágicas

Protegen, transportan y hacen cosquillas. Son memorables, suaves y visuales.

## Tamaño mascota en el futuro

El viaje en burbujas adapta a los Dinoamigos para vivir seguros junto a niños en el mundo moderno.

## Dinosaurios en el futuro

Existen por magia temporal y por el cuidado de los niños. Para el mundo humano común siguen siendo un secreto maravilloso.

## Cofre Dorado

Da poderes de ayuda, no de ataque. Solo se abre con cooperación.

## Marca de Rexxie

Puede brillar y molestar, pero no es una herida gráfica. Tras Libro 5 deja de doler y queda como estrella roja.

## Guardianes mágicos

No son villanos. Son pruebas de humor, pensamiento, valentía y cuidado.

## Alienígenas

Traviesos, pequeños y cómicos. Nunca terroríficos.

## Seguridad

Nada de sangre, muerte explícita, armas realistas ni sufrimiento prolongado.
""",
        "02_characters_master.md": "\n".join(chars_master),
        "03_visual_style_guide.md": f"""# Guía visual

## Estilo general

Infantil, luminoso, tierno y legible. Personajes grandes, ojos expresivos, contornos claros y siluetas reconocibles.

## Full color

Colores brillantes pero limpios: azules mágicos, verdes de aventura, dorados suaves y acentos rojos para la marca de Rexxie.

## Line art

Líneas limpias, fondos simples, espacios amplios para colorear y pocas texturas pequeñas.

## Portadas

Mostrar el objeto o lugar central del libro en primer plano narrativo: huevos, Máquina del Tiempo, Platillo Azul, isla o jardín.

## Personajes

Dinosaurios tiernos y reconocibles. Niños diversos con rasgos constantes.

## Escenarios

Fondos coloreables con formas grandes: montañas, ríos, tiendas, mapas, ruinas, nave y jardín.

## Alienígenas

Traviesos, pequeños, redondos, con cascos transparentes.

## Tecnología mágica

{MAGIC}

## Acción segura

Batallas caricaturescas, robots que se apagan con BIP y humo en forma de flor.
""",
        "04_continuity_timeline.md": """# Línea temporal

## Antes del Libro 1

Los huevos mágicos aparecen en el mundo prehistórico y el Platillo Azul observa desde lejos.

## Libro 1 — Los Dinoamigos nacen

Nacen Rexxie, Dipo, Trici, Velo y Mega. Viajan al futuro en burbujas y conocen a Maxi, Luna, Teo, Mía y Leo.

## Entre Libro 1 y Libro 2

Los Dinoamigos viven como mascotas fantásticas en el campamento urbano.

## Libro 2 — La Máquina del Tiempo

Trici desaparece, el grupo viaja al pasado y aprende que lo grande también puede proteger.

## Libro 3 — El Secreto del Platillo Azul

Luke y Olic se unen. El Cofre Dorado entrega poderes limitados al equipo.

## Libro 4 — La Isla Perdida de los Dinosaurios

El grupo rescata a Orin, Tricero, Brachio, Crick y Aeron. Rexxie recibe la marca alienígena roja.

## Libro 5 — En busca de la Planta Secreta

Doctor Florio calma la marca. Rexxie aprende a llevarla sin miedo.

## Estado final tras Libro 5

Equipo completo, familias recuperadas, poderes activos y marca de Rexxie integrada.

## Ganchos abiertos para Libro 6

Origen real del Platillo Azul, nuevos mapas, reglas de los alienígenas traviesos y posibles huevos futuros.
""",
        "05_powers_and_objects.md": "\n".join(powers),
        "06_locations_master.md": "# Lugares maestro\n\n" + "\n\n".join(f"## {l}\n\nLugar visual de la saga. Debe tener formas claras, escala infantil y potencial de coloreado." for l in locations),
        "07_editorial_rules.md": """# Reglas editoriales

- Preservar la imaginación infantil.
- Evitar lenguaje adulto innecesario.
- Mantener frases cortas.
- Cada página debe tener una acción clara.
- Cada libro debe tener un problema central.
- Cada libro debe cerrar emocionalmente.
- Cada final debe abrir suavemente el siguiente libro.
- Evitar violencia gráfica.
- Evitar explicar demasiado la ciencia.
- Mantener magia, aventura y humor.
- No convertir la saga en ciencia ficción dura.
- No convertir la saga en drama oscuro.
""",
        "08_coloring_book_rules.md": """# Reglas para libro de colorear

- Máximo recomendado: 3 a 5 elementos principales por escena.
- Personajes grandes.
- Fondos simples.
- Líneas claras.
- Emociones visibles.
- Evitar escenas confusas.
- Evitar exceso de texto por página.
- Usar acciones concretas.
- Mantener siluetas reconocibles.
- Permitir páginas de actividad.

## Páginas extras propuestas

- laberinto
- encuentra las huellas
- colorea los huevos
- une cada niño con su Dinoamigo
- diseña tu propio platillo
- encuentra las diferencias
- mapa de aventura
- colorea la Planta Secreta
- crea tu propio dinosaurio
""",
        "09_animation_rules.md": """# Reglas de animación

## Duración sugerida

11 a 22 minutos por episodio, según nivel de producción.

## Estructura por actos

Acto 1: problema. Acto 2: viaje y retos. Acto 3: clímax, abrazo emocional y gancho.

## Opening recurrente

Mapa, burbujas, Platillo Azul y presentación niño-Dinoamigo.

## Cierre recurrente

El equipo mira el cielo o el mapa y aparece un pequeño misterio.

## Música

Aventura luminosa, percusión suave, campanas mágicas y motivos cómicos para Mega.

## Voces

Infantiles, expresivas y claras. Guardianes con voces cálidas, no terroríficas.

## Ritmo visual

Ágil, con pausas para ternura y comprensión de acertijos.

## Gags recurrentes

- Mega pregunta por comida o hace burbujas.
- Rexxie intenta parecer feroz y suena pequeño.
- Teo quiere tocar botones.
- Velo corre antes de pensar.
""",
        "continuity_matrix.md": matrix,
        "season_01_editorial_map.md": """# Temporada 1 — Los Dinoamigos

## Arco general

El equipo nace, se encuentra, descubre tecnología mágica, recupera familias y aprende a transformar una marca dolorosa en valentía.

## Libro 1 — Nacimiento y adopción

Origen de los cinco primeros Dinoamigos y vínculo con los niños.

## Libro 2 — Primer viaje temporal

Trici desaparece y el equipo aprende a buscar sin juzgar al gran T-Rex protector.

## Libro 3 — Descubrimiento del platillo y poderes

Luke y Olic se unen. El Cofre Dorado entrega poderes con límites.

## Libro 4 — Familias perdidas y marca alienígena

La isla revela a los padres y el espacio deja en Rexxie la marca roja.

## Libro 5 — Cura, aceptación y cierre emocional

La Planta Secreta calma la marca y Rexxie aprende a llevarla.

## Estado final de la temporada

El equipo está completo, las familias están reunidas y la marca de Rexxie ya no duele.

## Ganchos para temporada 2

Nuevos huevos, secretos del Platillo Azul, mapas de otros mundos y guardianes aliados.
""",
        "editorial_checklist.md": """# Checklist editorial

## Historia

- [ ] El problema principal es claro.
- [ ] El inicio engancha.
- [ ] El final cierra emocionalmente.
- [ ] Hay puente al siguiente libro.

## Edad objetivo

- [ ] Lenguaje apto para 5 a 10 años.
- [ ] No hay violencia gráfica.
- [ ] El miedo es suave.
- [ ] Hay humor.

## Visual

- [ ] Cada escena puede ilustrarse.
- [ ] Cada página puede convertirse en imagen coloreable.
- [ ] Los personajes son reconocibles.
- [ ] No hay exceso de detalles.

## Continuidad

- [ ] Los nombres son consistentes.
- [ ] Los poderes se mantienen.
- [ ] Los objetos respetan sus reglas.
- [ ] No hay contradicciones fuertes.

## Prompts

- [ ] Hay prompt de portada.
- [ ] Hay prompts por escena.
- [ ] Hay prompts de personajes.
- [ ] Hay versión para colorear.
""",
        "editorial_audit.md": """# Auditoría editorial de Los Dinoamigos

## Evaluación general

La saga tiene una identidad muy clara: dinosaurios bebés, magia, mapas, familia, burbujas y aventuras inventadas con libertad infantil. La estructura de 5 libros funciona como primera temporada.

## Fortalezas de la saga

- Conceptos visuales memorables: huevos, burbujas, Platillo Azul, Máquina del Tiempo, isla y jardín.
- Parejas niño-Dinoamigo fáciles de recordar.
- Humor recurrente de Mega, Teo, Velo y Rexxie.
- Potencial alto para libro de colorear y animación.

## Riesgos narrativos

- Exceso de objetos mágicos si no se documentan reglas.
- Confusión de nombres si vuelven variantes como Rexy, Trexy u Olick.
- Retos que pueden sentirse bruscos si no se presentan como juegos mágicos.
- Marca de Rexxie debe ser emocional, no gráfica.

## Ajustes recomendados

- Mantener 32 páginas por libro.
- Usar frases breves.
- Hacer que cada reto tenga objetivo, mecánica y resolución visible.
- Repetir gags con moderación para dar identidad.

## Problemas de continuidad detectados

- Faltaban documentos globales con nombres exactos de biblia.
- Faltaban carpetas `locations`, `objects`, `challenges` e `images` en varios libros.
- Faltaban prompts de portada homogéneos.
- Algunos archivos tenían codificación dañada; se regeneraron los principales en UTF-8.

## Reglas editoriales finales

Preservar la imaginación del niño, ordenar sin endurecer, suavizar peligro, potenciar claridad visual y mantener la aventura como juego compartido.

## Recomendaciones por libro

### Libro 1

Potenciar nacimientos, burbujas y adopción tierna. El meteorito debe quedar lejano y seguro.

### Libro 2

Trici debe verse capaz. El T-Rex gigante es protector, no villano.

### Libro 3

Alienígenas traviesos y Cofre Dorado con poderes limitados.

### Libro 4

Baruk y guardianes son pruebas mágicas, no enemigos oscuros. Rescate espacial rápido y claro.

### Libro 5

Retos como acertijos. Robots en lugar de dinosaurios vivos para evitar violencia. Final de aceptación positiva.
""",
    }


def build_bible():
    for name, content in bible_docs().items():
        write(ROOT / "bible" / name, content)


def build_root_readme():
    write(ROOT / "README.md", """# Los Dinoamigos

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
""")


if __name__ == "__main__":
    build_books()
    build_bible()
    build_root_readme()
    print("Editorial build complete.")
