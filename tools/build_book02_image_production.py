import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book_02_la_maquina_del_tiempo"
PROMPTS = BOOK / "prompts"
IMAGES = BOOK / "images"
PRODUCTION = IMAGES / "production"
GEN_PROMPTS = PRODUCTION / "generation_prompts"


COLOR_BLOCK = """STRICT CHARACTER COLOR CONTINUITY. Do not redesign characters. Keep the same official colors in every image:
Rexxie is soft forest green with a warm cream belly, rounded teeth, big expressive eyes.
Dipo is warm pastel yellow with mint green spots, long neck, rounded body.
Trici is soft coral pink with a light lilac frill and ivory rounded horns.
Velo is bright turquoise with soft dark blue stripes, small agile baby raptor body.
Mega is ocean blue with a pale sky-blue belly and darker blue fins, cute baby megalodon, never scary.
Maxi is a cheerful brown-skinned boy with orange shirt, green explorer vest and blue shorts.
Luna is a blonde gentle girl with light blue shirt and soft yellow clothing accents.
Teo has curly hair, red soft shirt, green pants and explorer backpack.
Mía is an Asian-featured girl with violet shirt, light explorer vest and smart observant expression.
Leo is a red-haired boy with freckles, light green shirt and blue pants.
No alternate colors, no random palette, no redesign, no adult versions, no realistic scary dinosaurs."""


BW_BLOCK = """BLACK AND WHITE COLORING PAGE. Keep character identity by silhouette and fixed design: Rexxie small baby T-Rex with rounded teeth; Dipo long-neck baby Diplodocus; Trici baby Triceratops with three rounded horns and soft frill; Velo small agile baby raptor with stripe areas left blank for coloring; Mega cute baby megalodon with big friendly smile and bubbles. Clean bold outlines, no grayscale shading, no filled black areas, no tiny details, Amazon KDP coloring book ready."""


COLOR_STYLE = """FULL COLOR CHILDREN'S BOOK INTERIOR ILLUSTRATION. Amazon KDP print-ready portrait composition, 8.5 x 11 inch ratio, high resolution, 300 dpi target, clean readable shapes, safe margins, no embedded text, no watermark, no decorative border. Cute baby dinosaurs and diverse children explorers, large expressive characters, clear emotional action, simple recognizable background, magical but safe adventure for children ages 5 to 10."""


COLORING_STYLE = """Amazon KDP coloring book page, portrait 8.5 x 11 inch ratio, 300 dpi target, clean bold black outlines, white background, no color, no grayscale shading, no soft shadows, no heavy black fills, no tiny details, no text, no watermark, no decorative frame. Use 3 to 5 main visual elements only, large expressive characters, simple recognizable background, wide open spaces for coloring."""


TIMELINE = """BOOK 2 VISUAL TIMELINE: Designs remain from Book 1. No Cofre Dorado powers yet. Rexxie has no wings and no red mark. Trici has no armor. Velo has no glowing claws. Mega has no turbo fins. Luna has no glowing wings. Mía has no energy bracelets. Leo has no jump boots. Teo has no speed-power legs. Do not include Olic, Luke, the Cofre Dorado, or character powers. Do not show a blue flying saucer; only abstract blue light, portal glow, or distant mystery light is allowed."""


NEGATIVE = """NEGATIVE PROMPT: no horror, no realistic violence, no scary dinosaur teeth, no aggressive adult redesigns, no alternate colors, no text, no logo, no watermark, no decorative border, no muddy gray lighting, no hard science fiction, no Olic, no Luke, no Cofre Dorado, no powers, no wings on Rexxie, no red mark on Rexxie."""


PAGE_OVERRIDES = {
    1: {
        "main": "Rexxie, Dipo, Velo, Mega in a clear aquarium cart, Maxi, Mía, and a few children explorers; Trici represented only by small triceratops footprints leading toward the glowing time machine.",
        "focus": "Cover-like mystery composition: the Time Machine is the central object, a friendly circular machine with blue spiral light, clocks, buttons, and Trici footprints. Reserve a clean title area if this is used as a cover, but do not render text.",
        "simplify": "Large machine, a few large footprints, and the team in the foreground.",
    },
    2: {
        "main": "Rexxie, Dipo, Trici, Velo, Mega in his transparent aquarium cart, Maxi, and optional sleeping children in tents.",
        "focus": "Modern urban camp at night with tents and quiet lanterns, calm and safe.",
        "simplify": "Tents, moon, lantern, and sleeping characters only.",
    },
    3: {
        "main": "Dipo hugging a tree, Trici sleeping beside Mía, Mega making bubbles in his aquarium cart, Rexxie and Velo sleeping nearby.",
        "focus": "Tender group sleep before Trici disappears; this is the last clear calm scene with Trici before the search.",
        "simplify": "Sleeping group, tree, blanket, and aquarium cart.",
    },
    4: {
        "main": "Mía, Rexxie, Velo, Dipo, Mega in his aquarium cart, and the children waking up; Trici should not be clearly visible.",
        "focus": "First sunrise in the camp with a soft uneasy feeling, preparing the discovery that Trici is missing.",
        "simplify": "Sunrise, tents, worried faces, empty space near a blanket.",
    },
    5: {
        "main": "Mía pointing at Trici's empty blanket, Rexxie, Velo, Dipo, Mega in his aquarium cart, and worried children.",
        "focus": "Trici is missing and must not appear physically in the image.",
        "simplify": "Mía, empty blanket, three friends, and visible concern.",
    },
    6: {
        "main": "Rexxie sniffing the ground, Velo spotting a clue, Dipo watching, Mega in his aquarium cart, and children nearby.",
        "focus": "Beginning of the search around camp; Trici absent.",
        "simplify": "Ground clue, faces, tent edge, and aquarium cart.",
    },
    7: {
        "main": "Velo pointing at small triceratops footprints, Rexxie, Mía, and Dipo studying the trail; Mega in his aquarium cart nearby.",
        "focus": "Small clear Trici footprints in damp soil leading between trees; Trici absent.",
        "simplify": "Large footprints, simple path, a few tree trunks.",
    },
    8: {
        "main": "Maxi, Luna, Teo, Mía, Leo, Rexxie, Velo, Dipo, and Mega in his aquarium cart preparing explorer gear.",
        "focus": "Friendly rescue preparation with flashlights, map, rope, and notebook; no weapons and no Trici visible.",
        "simplify": "Map, flashlight, rope, notebook, and large character faces.",
    },
    9: {
        "main": "Velo leading, Dipo stretching his long neck to look ahead, Rexxie and children following, Mega rolling in his transparent aquarium cart.",
        "focus": "The team follows Trici footprints through a modern forest edge; Trici absent.",
        "simplify": "Path, footprints, three trees, and aquarium cart.",
    },
    10: {
        "main": "Rexxie, Velo, Mía, Teo, Dipo, and Mega in his aquarium cart at a tunnel entrance.",
        "focus": "Huge friendly roots with soft blue light underneath; Trici footprints enter the root tunnel.",
        "simplify": "Root arch, blue glow shapes, footprints, and a few characters.",
    },
    11: {
        "main": "Mía, Teo, Rexxie, Velo, Dipo, Mega in his aquarium cart, and the team facing the closed Time Machine.",
        "focus": "Closed circular Time Machine underground with clocks, a simple blue spiral, big buttons, and gentle magical technology.",
        "simplify": "Circular door, three clocks, spiral, and large buttons.",
    },
    12: {
        "main": "Teo surprised near large buttons, Mía warning gently, Rexxie wide-eyed, Velo curious, Mega in his aquarium cart.",
        "focus": "The Time Machine wakes up by itself; humor, not danger.",
        "simplify": "Teo, Mía, three big buttons, blue glow.",
    },
    13: {
        "main": "Rexxie nervous but brave, Velo, Mía, Dipo, and Mega in his aquarium cart watching footprints enter a blue portal.",
        "focus": "Trici footprints go into the blue portal; Trici remains absent.",
        "simplify": "Portal, footprints, Rexxie's expression, and simple machine frame.",
    },
    14: {
        "main": "Rexxie, Dipo, Velo, Mega in a water bubble or aquarium cart, Maxi, Luna, Teo, Mía, and Leo stepping into the portal together.",
        "focus": "The team crosses together to find Trici; Trici must not be with them yet.",
        "simplify": "Portal ring, linked hands, aquarium cart or water bubble.",
    },
    15: {
        "main": "Rexxie, Dipo, Velo, Mega in a water bubble or aquarium cart, and the children spinning safely through time.",
        "focus": "Dynamic time tunnel with big clocks, stars, and bubbles; Trici absent.",
        "simplify": "Few large clocks, bubbles, stars, and happy motion lines.",
    },
    16: {
        "main": "Rexxie, Dipo, Velo, Mega in his aquarium cart or beside a visible shallow pond, and the children landing on giant leaves.",
        "focus": "Arrival in the dinosaur era, surprised but safe; Trici absent.",
        "simplify": "Giant leaves, three trees, soft landing poses.",
    },
    17: {
        "main": "The search team looking at huge ancient trees, distant mountains, and giant footprints.",
        "focus": "Clear prehistoric landscape with wonder; do not introduce threatening dinosaurs.",
        "simplify": "Mountains, giant leaves, large footprints, open sky.",
    },
    18: {
        "main": "Mía kneeling with notebook, Velo analyzing tracks, Rexxie and Dipo watching, Mega near water or in cart.",
        "focus": "Trici's small footprints appear beside much larger tracks; tension stays soft and curious.",
        "simplify": "Two sizes of tracks, Mía, Velo, a simple ancient path.",
    },
    19: {
        "main": "Rexxie, Dipo, Velo, Mía, Leo, and Mega reacting to a large soft shadow behind leaves.",
        "focus": "A big rustling shadow suggests the Great T-Rex, but keep it gentle and non-horrific.",
        "simplify": "Big leaf shapes, one soft shadow, expressive faces.",
    },
    20: {
        "main": "Great adult T-Rex with warm protective eyes, Rexxie and the team looking up respectfully.",
        "focus": "The adult T-Rex is huge and serious but clearly protective, never scary or aggressive.",
        "simplify": "Large friendly T-Rex face/body, small team, open clearing.",
    },
    21: {
        "main": "Trici calm and alert behind the Great T-Rex, Mía and the team seeing her with relief.",
        "focus": "Trici reappears; she is safe, not tied, not hurt, and protected by the T-Rex.",
        "simplify": "Trici, Great T-Rex leg/body as shelter, relieved faces.",
    },
    22: {
        "main": "Great T-Rex standing protectively in front of Trici while a harmless comic danger retreats, with the team watching.",
        "focus": "Protection without violence: use a falling branch, startled little prehistoric critter, or shadow moving away, not combat.",
        "simplify": "T-Rex, Trici, one simple retreating shape, no fight.",
    },
    23: {
        "main": "Rexxie admiring the Great T-Rex, Dipo calmly explaining, and the team understanding.",
        "focus": "Emotional comprehension: someone big can be a protector, not an enemy.",
        "simplify": "Rexxie's face, Dipo, T-Rex silhouette, simple rocks.",
    },
    24: {
        "main": "Luna asking for patience, Mía waiting carefully, Rexxie, Velo, Dipo, Mega in cart or by water, and the team hidden softly at sunset.",
        "focus": "Prudence and care; no dangerous stealth or fear.",
        "simplify": "Sunset, gentle bushes, waiting team, distant T-Rex/Trici optional.",
    },
    25: {
        "main": "Great T-Rex sleeping peacefully under large stars, with the team waiting quietly nearby.",
        "focus": "Calm prehistoric night; the T-Rex must look peaceful, not threatening.",
        "simplify": "Sleeping T-Rex, big stars, simple moon, open ground.",
    },
    26: {
        "main": "Mía, Trici, Rexxie, Velo, Dipo, children, and Mega making a funny bubble or GLUP in his cart while everyone freezes silently.",
        "focus": "Comic silent rescue with the Great T-Rex asleep in the background; no terror.",
        "simplify": "Funny bubble, quiet poses, Trici close to Mía, sleeping T-Rex.",
    },
    27: {
        "main": "Mía hugging Trici, Rexxie and friends smiling, Great T-Rex sleeping peacefully in the background.",
        "focus": "Tender reunion; Trici is safe and still has no armor or powers.",
        "simplify": "Big hug, smiling faces, sleeping T-Rex silhouette.",
    },
    28: {
        "main": "Full team including Trici running safely toward a blue portal in the prehistoric jungle; Mega in water bubble/cart.",
        "focus": "Urgent but safe return path; no violent chase.",
        "simplify": "Blue portal, team motion, simple jungle shapes.",
    },
    29: {
        "main": "Full team including Trici traveling safely through the time tunnel; Mega in water bubble/cart.",
        "focus": "Return time travel with Trici recovered; joyful motion, clean composition.",
        "simplify": "Large bubbles, few clocks, stars, and grouped characters.",
    },
    30: {
        "main": "Full team back at camp with Trici present, Mía happy, Rexxie smiling, Mega in his transparent aquarium cart.",
        "focus": "Safe happy return to modern camp; Mega must have water/cart.",
        "simplify": "Tents, empty portal glow fading, group reunion.",
    },
    31: {
        "main": "Full team, including Trici and Mega in his aquarium cart, looking at a shooting star from camp.",
        "focus": "Hopeful night sky; the star must not look like a red mark on Rexxie.",
        "simplify": "Large sky, one shooting star, quiet silhouettes and faces.",
    },
    32: {
        "main": "Full team united at night, Trici safe, Mega in his aquarium cart, a small distant abstract blue light blinking far away.",
        "focus": "Gentle hook to the next book: only distant blue light, not a visible flying saucer, no Olic, no Luke.",
        "simplify": "Group, night sky, one small blue light shape, simple camp.",
    },
}


CHARACTER_PROMPTS = {
    "Rexxie": "Cute baby T-Rex, soft forest green, warm cream belly, rounded teeth, big expressive eyes, small body, brave and tender. Libro 2 only: no wings, no red mark, no star mark, no powers.",
    "Dipo": "Cute baby Diplodocus, warm pastel yellow, mint green spots, long neck, rounded body, gentle smile, calm posture. Libro 2 only: no glowing strong legs, no powers.",
    "Trici": "Cute baby Triceratops, soft coral pink, light lilac frill, three ivory rounded horns, protective and affectionate expression. Libro 2 only: no armor, no powers, never aggressive.",
    "Velo": "Cute baby raptor, bright turquoise, soft dark blue stripes, small agile body, playful runner posture, clever smile. Libro 2 only: no glowing claws, no dangerous talons, no powers.",
    "Mega": "Cute baby megalodon, ocean blue, pale sky-blue belly, darker blue fins, big friendly smile, bubbles, never scary. In modern scenes he must be in water or in a transparent aquarium cart. Libro 2 only: no turbo fins, no powers.",
    "Maxi": "Cheerful brown-skinned boy, orange shirt, green explorer vest, blue shorts, expressive happy face, caring companion for Mega.",
    "Luna": "Gentle blonde girl, light blue shirt, soft yellow clothing accents, calm caring expression. Libro 2 only: no glowing wings, no powers.",
    "Teo": "Curious child with curly hair, red soft shirt, green pants, explorer backpack, playful but safe body language. Libro 2 only: no speed-power legs, no powers.",
    "Mía": "Asian-featured girl, violet shirt, light explorer vest, smart observant expression, practical notebook or map. Libro 2 only: no energy bracelets, no powers.",
    "Leo": "Red-haired boy with freckles, light green shirt, blue pants, honest brave expression. Libro 2 only: no jump boots, no powers.",
    "Gran T-Rex protector": "Large adult T-Rex in the prehistoric era, imponente but kind and protective, warm eyes, rounded non-scary teeth, gentle guardian posture. Never realistic horror, never violent, not Orin by name in Libro 2.",
}


def parse_pages():
    text = (BOOK / "story" / "page_by_page.md").read_text(encoding="utf-8")
    parts = re.split(r"\n## Página (\d{2}) — (.+?)\n", text)
    pages = []
    for idx in range(1, len(parts), 3):
        number = int(parts[idx])
        title = parts[idx + 1].strip()
        body = parts[idx + 2]
        def field(name):
            match = re.search(rf"### {name}\n\n(.*?)(?=\n### |\Z)", body, flags=re.S)
            return match.group(1).strip() if match else ""
        characters = [
            line[2:].strip()
            for line in field("Personajes presentes").splitlines()
            if line.startswith("- ")
        ]
        pages.append({
            "page": number,
            "title": title,
            "text": field("Texto narrativo"),
            "visual": field("Descripción visual"),
            "characters_raw": characters,
            "setting": field("Entorno"),
            "emotion": field("Emoción principal"),
        })
    if len(pages) != 32:
        raise RuntimeError(f"Expected 32 pages, found {len(pages)}")
    return pages


def color_prompt(page):
    spec = PAGE_OVERRIDES[page["page"]]
    return "\n\n".join([
        COLOR_STYLE,
        TIMELINE,
        COLOR_BLOCK,
        f"PAGE {page['page']:02d} - {page['title']}. Scene: {page['visual']}",
        f"MAIN CHARACTERS AND PROPS: {spec['main']}",
        f"SETTING: {page['setting']}. EMOTION: {page['emotion']}.",
        f"CONTINUITY FOCUS: {spec['focus']}",
        "COMPOSITION: Characters must be large and readable, with one clear action, visible emotion, simple background shapes, and generous safe margins for print.",
        NEGATIVE,
    ])


def coloring_prompt(page):
    spec = PAGE_OVERRIDES[page["page"]]
    return "\n\n".join([
        BW_BLOCK,
        COLORING_STYLE,
        TIMELINE,
        f"PAGE {page['page']:02d} - {page['title']}. Scene: {page['visual']}",
        f"MAIN SILHOUETTES AND PROPS: {spec['main']}",
        f"SETTING: {page['setting']}. EMOTION: {page['emotion']}.",
        f"COLORING SIMPLIFICATION: {spec['simplify']} Keep broad white spaces for coloring.",
        "NEGATIVE PROMPT: no grayscale, no shading, no crosshatching, no dense foliage, no tiny gears, no dark filled sky, no realistic scary dinosaurs, no text, no logo, no watermark, no Olic, no Luke, no powers, no wings or mark on Rexxie.",
    ])


def write_prompt_markdowns(pages):
    scene_sections = ["# Prompts por escena - Libro 2 producción KDP\n"]
    coloring_sections = ["# Prompts para libro de colorear - Libro 2 producción KDP\n"]
    for page in pages:
        scene_sections.append(f"## Página {page['page']:02d} — {page['title']}\n\n{color_prompt(page)}\n")
        coloring_sections.append(f"## Página {page['page']:02d} — {page['title']}\n\n{coloring_prompt(page)}\n")
    (PROMPTS / "scene_prompts.md").write_text("\n".join(scene_sections), encoding="utf-8")
    (PROMPTS / "coloring_book_prompts.md").write_text("\n".join(coloring_sections), encoding="utf-8")


def write_character_prompts():
    parts = ["# Prompts de personajes - Libro 2\n", TIMELINE, COLOR_BLOCK]
    for name, desc in CHARACTER_PROMPTS.items():
        parts.append(f"## {name}\n\n{COLOR_STYLE}\n\nCharacter reference for {name}: {desc}\n\nConsistent children's book design, friendly expression, readable silhouette, no redesign.\n")
    (PROMPTS / "character_prompts.md").write_text("\n\n".join(parts), encoding="utf-8")


def write_cover_prompt(pages):
    page = pages[0]
    content = "\n\n".join([
        "# Prompt de portada - La Máquina del Tiempo",
        color_prompt(page),
        "COVER NOTE: Use a clean cover-ready composition with the Time Machine as the central object, the team in the foreground, and Trici indicated by footprints or a soft portal clue. Leave a clean title area; do not render final typography unless requested.",
        "## Versión line art",
        coloring_prompt(page),
    ])
    (PROMPTS / "cover_prompt.md").write_text(content, encoding="utf-8")


def write_production_files(pages):
    for folder in [PRODUCTION, GEN_PROMPTS / "color", GEN_PROMPTS / "coloring"]:
        folder.mkdir(parents=True, exist_ok=True)

    production_md = [
        "# Libro 2 - Paquete de producción de ilustraciones KDP",
        "",
        "Flujo objetivo: generación integrada desde Codex o ChatGPT Plus, sin API, sin `OPENAI_API_KEY`, sin CLI de generación. Salida final objetivo: PNG, 2550 x 3300 px, 300 dpi, sin texto incrustado, sin marcas de agua.",
        "",
        "Continuidad fija: Libro 2 no tiene poderes, Rexxie no tiene alas ni marca roja, Trici no tiene armadura, Mega requiere agua o carrito-acuario en mundo moderno, Olic y Luke no aparecen.",
        "",
    ]
    qa_md = [
        "# Libro 2 - Matriz QA de imagen",
        "",
        "Veredictos permitidos para cada imagen generada: `aprobada`, `corregir`, `rechazada`.",
        "",
        "| Página | Uso | Control editorial | QA color | QA blanco y negro |",
        "|---|---|---|---|---|",
    ]

    for page in pages:
        cp = color_prompt(page)
        bp = coloring_prompt(page)
        color_name = f"page_{page['page']:02d}_color.png"
        coloring_name = f"page_{page['page']:02d}_coloring.png"

        (GEN_PROMPTS / "color" / f"page_{page['page']:02d}_color.txt").write_text(cp, encoding="utf-8")
        (GEN_PROMPTS / "coloring" / f"page_{page['page']:02d}_coloring.txt").write_text(bp, encoding="utf-8")

        production_md.extend([
            f"## Página {page['page']:02d} — {page['title']}",
            "",
            f"Salida color: `images/finals/{color_name}`",
            "",
            f"Salida blanco y negro: `images/coloring_pages/{coloring_name}`",
            "",
            "### Color",
            "",
            cp,
            "",
            "### Blanco y negro",
            "",
            bp,
            "",
        ])
        qa_md.append(
            f"| {page['page']:02d} | color + colorear | {PAGE_OVERRIDES[page['page']]['focus']} | Revisar paleta oficial, sin poderes, sin marca de Rexxie, Mega con agua/carrito si aplica, escena legible. | Revisar líneas negras limpias, sin grises, sin rellenos negros, 3-5 elementos principales, espacios amplios. |"
        )

    tracker_rows = [
        "# Libro 2 - Tracker manual de producción",
        "",
        "Usar este archivo para marcar avances cuando se genere con Codex integrado o ChatGPT Plus. No usar API.",
        "",
        "| Página | Color | QA color | Colorear | QA colorear | Notas |",
        "|---|---|---|---|---|---|",
    ]
    for page in pages:
        tracker_rows.append(
            f"| {page['page']:02d} | pendiente | pendiente | pendiente | pendiente | {page['title']} |"
        )
    (PRODUCTION / "manual_production_tracker.md").write_text("\n".join(tracker_rows) + "\n", encoding="utf-8")
    (PRODUCTION / "kdp_image_production_prompts.md").write_text("\n".join(production_md), encoding="utf-8")
    (PRODUCTION / "image_qa_matrix.md").write_text("\n".join(qa_md) + "\n", encoding="utf-8")

    workflow = """# Flujo manual Codex / ChatGPT Plus - Libro 2

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
"""
    (PRODUCTION / "manual_generation_workflow.md").write_text(workflow, encoding="utf-8")


def main():
    pages = parse_pages()
    write_prompt_markdowns(pages)
    write_character_prompts()
    write_cover_prompt(pages)
    write_production_files(pages)
    print(f"Generated production prompt package for {len(pages)} pages in {PRODUCTION}")


if __name__ == "__main__":
    main()
