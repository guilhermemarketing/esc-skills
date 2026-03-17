# 🎭 Character Design

> 32+ prompts curados para design de personagens, avatares, retratos estilizados e ilustrações.

---

## Índice

- [3D Character Renders](#3d-character-renders)
- [Photo to Character](#photo-to-character)
- [Stylized Portraits](#stylized-portraits)
- [Superhero & Sci-Fi Characters](#superhero--sci-fi-characters)

---

## 3D Character Renders

### Cute Chibi 3D Character

**Descrição:** Personagem 3D estilo chibi com estética de toy/claymorphism.

```json
{
  "subject": {
    "type": "chibi-style 3D character",
    "gender": "female",
    "features": {
      "hair": "pastel pink bob cut with soft bangs, stylized 3D strands",
      "eyes": "large expressive dark eyes, looking upward and to the side",
      "expression": "dreamy, slightly surprised, open mouth",
      "skin": "fair with soft pink blush on cheeks",
      "accessories": ["small gold hoop earrings", "delicate gold necklace with heart pendant"]
    },
    "outfit": {
      "top": "tight-fitting dark brown long-sleeved crop top",
      "bottom": "high-waisted peach-colored joggers or harem pants",
      "shoes": "brown and tan platform sneakers"
    }
  },
  "art_style": {
    "type": "3D render / C4D / Octane Render",
    "aesthetic": "soft claymorphism, smooth textures, toy-like aesthetic",
    "lighting": "soft cinematic lighting, warm sunlight, gentle shadows",
    "camera": "full body shot, eye-level, shallow depth of field (bokeh)"
  },
  "environment": {
    "background": "blurred Mediterranean-style street, soft orange and cream buildings",
    "color_palette": ["pastel pink", "peach", "warm brown", "cream"]
  }
}
```

**Fonte:** [@Just_sharon7](https://x.com/Just_sharon7/status/2006344057728242177)

---

### 3D Pixar-Style Twin

**Descrição:** Pessoa real ao lado de versão Pixar 3D de si mesma.

```json
{
  "prompt": "Hyper-realistic studio photo of a stylish person using the uploaded reference face with exact facial likeness. The person is standing casually with legs crossed at the ankles, one arm wrapped around a giant Pixar-style 3D version of themselves. Outfit: navy blue hoodie, beige chinos, cream-colored sneakers. The Pixar 3D character has a slim, athletic body (NOT chubby), identical outfit, same height scale, same confident stance, one hand on hip. The Pixar character has the SAME playful facial expression as reference: clear mischievous smile with a DISTINCT wink (one eye closed, one eye open). Clean soft pink backdrop, studio lighting.",
  "negative_prompt": "fat body, chubby Pixar character, oversized head, wrong face shape, missing wink, different pose",
  "size": "4:5",
  "reference": "100% use uploaded image for face, pose, body proportions"
}
```

**Fonte:** [@r4jjesh](https://x.com/r4jjesh/status/2006967151056531681)

---

## Photo to Character

### Photo to Vector Art Split

**Descrição:** Imagem dividida com metade fotorrealista e metade cartoon vetorial.

```json
{
  "prompt": "64K DSLR ultra-sharp split-reality street art portrait using the uploaded image as exact face reference. Vertical frame, man leaning against a light-gray concrete wall. Left side photorealistic: red cap, black hoodie, loose gray knee-length shorts, white crew socks, red Nike sneakers, arms crossed, one foot on wall, natural soft daylight, realistic shadows, asphalt ground. Right side illustrated: same pose, outfit, proportions, stylized 2D cartoon with bold black outlines.",
  "negative_prompt": "blurry, low quality, distorted, extra limbs, bad anatomy, watermark",
  "aspect_ratio": "9:16",
  "face_restoration": true,
  "control_net": {
    "type": "face_id",
    "strength": 1.0
  }
}
```

**Fonte:** [@Strength04_X](https://x.com/Strength04_X/status/2005480949660938596)

---

### Doodle Art Portrait

**Descrição:** Retrato transformado em estilo doodle art com anotações e elementos gráficos.

```json
{
  "image_generation_task": {
    "task_type": "img2img",
    "input_source": "uploaded_user_image",
    "constraint": "preserve_full_likeness",
    "base_configuration": {
      "medium": {
        "substrate": "lined notebook paper",
        "tools": ["ballpoint pen", "neon markers", "ink"],
        "texture_details": ["realistic ink absorption", "layered pen pressure", "stained edges", "smudges"]
      },
      "art_style": {
        "genre": ["doodle art", "comic annotations", "sketch"],
        "line_work": "thick-thin variation, loose freestyle, messy strokes, dynamic hatch shading",
        "atmosphere": "chaotic, energetic, spontaneous, dense"
      }
    },
    "composition_elements": {
      "framing": "portrait with thick border line around head",
      "surrounding_elements": ["messy arrows", "stars", "underlines", "speech bubbles", "checkboxes"],
      "iconography": ["lightning bolt", "lightbulb", "music note"],
      "typography": {
        "style": "handwritten comic notes",
        "sound_effects": ["ZAP!", "WHOOSH!"]
      }
    },
    "style_variations": [
      {"id": "variant_01_pop_bold", "color_palette": ["bold cyan", "magenta"]},
      {"id": "variant_02_neon_highlight", "color_palette": ["neon pink", "neon yellow"]},
      {"id": "variant_03_electric_graffiti", "color_palette": ["hot electric blue", "neon red"]}
    ]
  }
}
```

**Fonte:** [@YaseenK7212](https://x.com/YaseenK7212/status/1999470440008339551)

---

### Bratz-Style Scrapbook Portrait

**Descrição:** Ilustração semi-realista com estética de recortes e scrapbook.

```json
{
  "image_generation": {
    "face_preservation": {
      "preserve_original": true,
      "accuracy": "100% identical to the reference photo"
    },
    "subject": {
      "hair": {"style": "messy bun with soft loose front strands"},
      "expression": "calm, confident, gentle",
      "clothing": {
        "top": {"type": "white cropped T-shirt", "print": "Bratz Rock Angelz graphic"},
        "outerwear": {"type": "beige knitted cardigan", "style": "loose, slightly falling off shoulders"},
        "pants": {"type": "olive or dark-green joggers"}
      }
    },
    "illustration_style": {
      "type": "vibrant semi-realistic illustration",
      "character_design": "realistic face with soft cartoon outlines on body",
      "shading": "smooth semi-realistic shading blended with stylized line art"
    },
    "background": {
      "type": "scrapbook collage aesthetic",
      "elements": ["torn paper edges", "tape strips", "pastel color blocks"],
      "doodles": ["small clouds", "tiny stars", "hand-drawn hearts"],
      "text": [{"content": "IMAGINE!", "style": "crayon-like scribble"}, {"content": "NOW!", "style": "bold marker"}]
    },
    "aesthetic": {
      "mood": "creative, expressive, soft yet bold",
      "palette": ["warm brown", "creamy beige", "soft pinks", "muted greens"]
    }
  }
}
```

**Fonte:** [@ZaraIrahh](https://x.com/ZaraIrahh/status/1996032358408224869)

---

## Stylized Portraits

### Volcanic Rock Bust

**Descrição:** Busto escultural em rocha vulcânica fragmentada com brilho de brasa.

```json
{
  "task": "image_to_image_style_transfer",
  "input_image": "{{USER_IMAGE}}",
  "prompt": "Reimagine the subject as a hyper-real fragmented volcanic basalt construct, assembled from jagged, sharply defined basalt plates suspended in space. Each fragment is fully separated with clearly visible gaps, never touching or fused. Material: deep charcoal-black basalt with layered volcanic textures, rough porous surfaces, chipped edges. Within the gaps only, a subtle internal glow radiates in rich ember tones—burnt orange, molten amber, hints of crimson and gold. Lighting: cinematic studio setup with cool blue-grey top key light, soft warm under-fill reflecting ember colors. Background: smooth dark neutral studio grey. Ultra-realistic, 8K clarity.",
  "negative_prompt": "lava flow, molten surfaces, surface glow, fantasy creature, cartoon, face distortion",
  "params": {
    "style_strength": 0.8,
    "identity_preservation": 0.92,
    "internal_glow": "subtle_multicolor_ember"
  }
}
```

**Fonte:** [@Sheldon056](https://x.com/Sheldon056/status/2005628752802517441)

---

### Pop Culture Character Mashup

**Descrição:** Pessoa real posando com personagens icônicos da cultura pop.

```json
{
  "scene_1_woody_buzz": {
    "prompt": "A hyperrealistic, editorial fashion photograph in studio setting. A real human model with natural, confident expression stands between giant, photorealistic 3D animated characters, Woody and Buzz Lightyear. The human wears chunky knitted sweater in warm yellow and blue tones, high-waisted dark blue jeans, and clean white minimalist sneakers. Buzz Lightyear, rendered with incredible detail in space ranger suit showing realistic plastic and scuff textures. Woody has relaxed stance, tipping his hat with highly detailed fabric textures. Background: clean, split studio backdrop of sky blue and warm brown. 3/4 body framing, magazine-cover quality."
  },
  "scene_2_charizard": {
    "prompt": "A hyperrealistic premium fashion photograph. A real human model with confident, defiant expression stands next to a massive, imposing 3D animated Charizard, rendered in photorealistic quality. Human wears dark charcoal knitted sweater, dark black jeans, and white sneakers. Charizard looms powerfully with highly realistic leathery orange skin texture, formidable claws, detailed flame burning at tail tip. Background: dark slate grey with subtle warm orange light accents. Editorial aesthetic."
  }
}
```

**Fonte:** [@oggii_0](https://x.com/oggii_0/status/2006579641264595235)

---

## Superhero & Sci-Fi Characters

### Black Panther Style Character

**Descrição:** Retrato de personagem em traje futurista inspirado em Wakanda.

```json
{
  "image_type": "Ultra-photorealistic studio portrait",
  "theme": "Wakanda Forever",
  "subject_details": {
    "view": "full body",
    "attire": {
      "outfit": "sleek black futuristic bodysuit",
      "accessories": "vibrant purple energy lines glowing through the suit",
      "footwear": "combat boots with metallic finish"
    },
    "hairstyle": "braided ponytail with subtle purple highlights",
    "makeup": "bold eyeliner and metallic shimmer"
  },
  "setting_and_action": {
    "prop": "panther throne",
    "pose": {
      "action": "confident and powerful",
      "details": "one hand resting on throne, other on hip"
    },
    "lighting": {
      "source": "neon purple glow with rim light effect"
    },
    "background": {
      "color": "deep black",
      "detail": "glowing 3D Black Panther emblem behind"
    }
  }
}
```

**Fonte:** [@rowanali09](https://x.com/rowanali09/status/1985276454116983129)

---

### Watercolor Fashion Portrait

**Descrição:** Retrato em aquarela realista sendo pintado em sketchbook.

```json
{
  "image_generation": {
    "type": "hyper_realistic_cinematic_ultra_close_up",
    "camera": {
      "angle": "top-down",
      "focus": "extreme close-up",
      "sharp_focus_on": ["painted watercolor details", "paper grain", "wet pigment textures"]
    },
    "subject": {
      "object": "white sketchbook lying half-open on artist's wooden desk",
      "illustration": {
        "style": "soft watercolor fashion illustration",
        "subject_match": {
          "reference_person": true,
          "description": "The illustration shows the same person from the uploaded photo in same outfit and pose, painted in flowing watercolor strokes."
        }
      }
    },
    "environment": {
      "setting": "artist's wooden desk",
      "lighting": {
        "source": "warm natural daylight",
        "effects": ["light streaming from side", "reflections on wet paint"]
      }
    },
    "mood": "artistic, serene, tactile, cinematic watercolor-in-progress aesthetic"
  }
}
```

**Fonte:** [@ZaraIrahh](https://x.com/ZaraIrahh/status/1993833382695022774)

---

## 🎨 Adaptação Neo-Brutalismo Pop

Para adaptar estes prompts ao estilo gui.marketing:

```
Character Design Neo-Brutalist modifier:
"Bold graphic character with electric lime (#C8FF00), hot pink (#FF1BB3), 
and cyan (#00D4FF) accents. Thick black outlines, exaggerated proportions, 
urban streetwear aesthetic, anti-establishment attitude, provocative expression. 
Graffiti-influenced background elements, intentional imperfections."
```
