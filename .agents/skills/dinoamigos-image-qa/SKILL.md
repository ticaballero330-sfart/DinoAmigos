---
name: dinoamigos-image-qa
description: Use when reviewing Los DinoAmigos generated images, final image prompts, covers, coloring pages, storyboards, or promotional visuals and deciding whether they are approved, need correction, or must be rejected for continuity, color, silhouette, age safety, or coloring-book quality issues.
---

# DinoAmigos Image QA

Use this skill to judge whether DinoAmigos visual outputs can be used.

## Required reading

Read the relevant parts of:

- `AGENTS.md`
- `bible/10_character_design_color_rules.md`
- `bible/03_visual_style_guide.md`
- `bible/08_coloring_book_rules.md`
- `bible/continuity_matrix.md`
- `bible/editorial_checklist.md`
- The book's scene, prompt, or page file for intended content

## QA workflow

1. Identify intended use: color interior, cover, coloring page, storyboard, reference sheet, ad, or prompt.
2. Confirm book and timeline state.
3. For full-color images, check that the finish matches the cheerful luminous Book 1 final art style while preserving the official character palette. Judge lighting separately from palette: correct character colors do not approve an image if the scene is too dark.
4. Check character palette, silhouette, age, clothing, expression, powers, and required props.
5. Check composition: readable action, large characters, visible emotion, safe tone, simple background, clearly lit faces, high overall brightness, and soft cheerful color.
6. For coloring pages, check clean outlines, no grayscale shading, no heavy black fills, and enough open spaces.
7. Return a verdict and the smallest useful correction.

## Verdict format

Use exactly one of:

- `aprobada`
- `corregir`
- `rechazada`

Then include:

- `Motivos`: concrete reasons.
- `Correccion minima`: what to change.
- `Riesgo`: what breaks if used as-is.

## Immediate rejection rules

- A main character has the wrong base color.
- A full-color image ignores the Book 1 cheerful luminous storybook finish and drifts into a different visual style.
- A full-color image is too dark even if the character palette is correct: dark navy dominance, low-key lighting, moody cinematic shadows, dim blue cast, gloomy palette, or dramatic sci-fi darkness.
- A Dinoamigo looks adult, scary, aggressive, or realistic.
- Rexxie's mark appears before the end of Book 4 or is missing when it should persist.
- Mega is in a modern setting without water or the aquarium cart.
- Olic lacks cyan glowing markings or golden eyes in color.
- A coloring page uses gray shading, heavy black fills, or too much tiny detail.

## Bias

Prioritize continuity and luminous Book 1 color over spectacle. A quieter correct image is better than a dramatic inconsistent one. A beautiful image with wrong character colors, wrong silhouettes, or a dark gloomy finish is not production-ready.
