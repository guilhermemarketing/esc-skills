# 📦 Product Photography

> 61+ prompts curados para fotografia de produtos, publicidade e criativos comerciais.

---

## Índice

- [Superhero Product Ads](#superhero-product-ads)
- [Beauty & Cosmetics](#beauty--cosmetics)
- [Beverage Photography](#beverage-photography)
- [Sneaker & Fashion Products](#sneaker--fashion-products)
- [Creative Product Concepts](#creative-product-concepts)

---

## Superhero Product Ads

### Marvel-Style Beverage Ads

**Descrição:** Produtos de bebida com elementos de super-heróis Marvel em composições épicas.

```json
[
  {
    "concept_id": "thor_sprite",
    "visual_breakdown": {
      "focus_object": "Sprite Bottle",
      "character_element": "Thor's Glowing Hand",
      "environment": "Storm/Lightning"
    },
    "artistic_direction": {
      "lighting": "Electric/Blue-Toned",
      "mood": "mythological"
    },
    "generation_command": {
      "aspect_ratio": "7:9",
      "concise_prompt": "Thor's glowing hand holding a floating Sprite bottle amidst crackling lightning and rain, Mjolnir in background, epic poster style. --ar 7:9"
    }
  },
  {
    "concept_id": "iron_man_coke",
    "visual_breakdown": {
      "focus_object": "Coca-Cola Can",
      "character_element": "Iron Man's Gauntlet",
      "environment": "Blurred City Skyline"
    },
    "artistic_direction": {
      "lighting": "Cinematic/Metallic",
      "mood": "technological"
    },
    "generation_command": {
      "aspect_ratio": "7:9",
      "concise_prompt": "Iron Man's gauntlet hovering below a floating Coca-Cola can, cinematic city background, dramatic movie poster lighting. --ar 7:9"
    }
  },
  {
    "concept_id": "hulk_pepsi",
    "visual_breakdown": {
      "focus_object": "Crushed Pepsi Can",
      "character_element": "Hulk's Giant Hand",
      "environment": "Smoky City Ruins"
    },
    "generation_command": {
      "concise_prompt": "Hulk's giant hand hovering over a crushed Pepsi can embedded in pavement, smoky ruins, explosive action movie style. --ar 7:9"
    }
  }
]
```

**Fonte:** [@YaseenK7212](https://x.com/YaseenK7212/status/2002013476370444766)

---

## Beauty & Cosmetics

### Nail Polish Beauty Shot

**Descrição:** Macro shot editorial de mulher segurando esmalte perto da câmera.

```json
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photorealistic_product_beauty_macro"
    },
    "creative_prompt": {
      "scene_summary": "Ultra photoreal editorial beauty macro shot. A woman holds a nail polish bottle extremely close to the camera with dramatic perspective. The bottle is the main focus (tack sharp), while the face is softly out of focus behind it. White seamless background.",
      "camera": {
        "type": "beauty macro / close-up product shot",
        "lens_look": "wide-close macro perspective (24-35mm equivalent feel)",
        "focus": "product label and bottle edges tack sharp; face slightly soft bokeh"
      },
      "product_design": {
        "object": "nail_polish_bottle",
        "bottle_material": "clear_glass_with_realistic_refraction",
        "polish_color": "vivid_orange",
        "label_design": {
          "base": "clean_modern",
          "logo": "Bagel symbol placed prominently",
          "brand_text": "BAGEL LABS printed clearly on the bottle label"
        }
      },
      "hands_and_nails": {
        "nails": {
          "shape": "almond",
          "color": "vivid_orange_match_product",
          "finish": "glossy"
        },
        "anatomy_rules": "perfect hands, five fingers each, no warping"
      }
    },
    "negative_prompt": ["watermark", "logo errors", "misspelled words", "extra hands", "warped hands", "plastic skin"]
  }
}
```

**Fonte:** [@astronomerozge1](https://x.com/astronomerozge1/status/2005967732781576583)

---

### Lip Gloss Contact Sheet

**Descrição:** Grid 3x3 de collage beauty campaign com modelo e produto.

```json
{
  "generation_request": {
    "task_type": "text_to_image_ultra_photoreal_beauty_contact_sheet_product_campaign",
    "output_settings": {
      "aspect_ratio": "4:5",
      "render_style": "ultra_photoreal_beauty_editorial"
    },
    "creative_prompt": {
      "scene_summary": "Ultra-photoreal beauty campaign contact sheet on pure white seamless background. A 3x3 grid collage of nine panels featuring ONE model with voluminous, glossy, long dark waves. Product: a sleek chrome lip product tube with 'BAGEL' printed clearly.",
      "panel_variety": [
        "Model holds chrome tube horizontally over eyes like visor",
        "Close-up applying lipstick with doe-foot applicator",
        "Model laughing wide-mouth with tube near face",
        "Beauty angle portrait holding tube near chin",
        "Extreme close-up smile with tube between teeth",
        "Wink + playful tongue-out with applicator",
        "Applying lipstick with elegant hand pose",
        "Kissy face wink with cheek highlight",
        "Tight crop smile with crisp lip texture"
      ],
      "hard_constraints": [
        "one model only, repeated across all 9 panels",
        "3x3 grid collage layout",
        "pure white background",
        "'BAGEL' text readable and spelled correctly"
      ]
    }
  }
}
```

**Fonte:** [@astronomerozge1](https://x.com/astronomerozge1/status/2005732191884488965)

---

## Beverage Photography

### Coca-Cola Premium Shot

**Descrição:** Fotografia comercial high-end de garrafa Coca-Cola com splash dinâmico.

```json
{
  "aspect_ratio": "1:1",
  "creative_direction": {
    "style": "High-end commercial photography, cinematic, hyper-realistic, luxurious.",
    "mood": "Intense refreshment, premium, energetic but controlled, dramatic.",
    "key_focus": "The irresistible coldness and explosive taste of the product."
  },
  "subject": {
    "hero": "A single glass bottle of Coca-Cola, center-stage.",
    "details": "Extreme condensation, real water droplets running down the glass, looks incredibly cold and frosty. The liquid inside glows with a rich caramel amber light."
  },
  "action_and_fx": {
    "splash": "A dynamic, sculptural arch of liquid and ice cubes erupting around and behind the bottle, framing it rather than obscuring it.",
    "ice": "Crystal clear, sharp ice cubes caught in motion, catching the light like diamonds.",
    "particles": "Fine mist and effervescent bubbles suspended in the air."
  },
  "lighting": {
    "type": "Dramatic, high-contrast cinematic lighting (Rembrandt lighting on bottle).",
    "colors": "Warm golden backlighting combined with cool, crisp key lighting on the front."
  },
  "environment": {
    "background": "Deep, dark, atmospheric mahogany and amber gradient. Subtle, luxurious bokeh effects.",
    "surface": "The bottle rests on a dark, wet, reflective surface."
  }
}
```

**Fonte:** [@ttmouse](https://x.com/ttmouse/status/1999892192790495237)

---

### Grape Soda Dynamic Splash

**Descrição:** Produto de bebida com splash crown dramático.

```json
{
  "prompt": {
    "positive": "Ultra-realistic luxury beverage product photography of a sleek aluminum can, centered in the frame. The can is deep midnight purple, featuring elegant illustrations of grape clusters and green leaves, heavily covered in fresh, cold condensation droplets. Prominently labeled 'Midnight Spark – Bold & Juicy' in premium typography. A dramatic, symmetrical crown-shaped splash of vivid purple grape juice erupts violently upward and outward from immediately behind the can. Studio lighting, high detail, 8k resolution, cinematic, macro lens focus.",
    "negative": "cartoon, low quality, blurry, flat lighting, amateur, distorted text, asymmetrical, dry can, plastic looking liquid, watermark",
    "style_preset": "photographic",
    "aspect_ratio": "2:3"
  }
}
```

**Fonte:** [@Strength04_X](https://x.com/Strength04_X/status/2005644381823615390)

---

### Strawberry Juice in Nature

**Descrição:** Garrafa de suco em cenário natural com ambiente temático.

```json
[
  {
    "id": "strawberry_mountain",
    "type": "photorealistic advertising shot",
    "subject": {
      "item": "strawberry juice bottle",
      "label_text": "NFC Strawberry Juice",
      "details": "emits condensation"
    },
    "environment": {
      "location": "mountains",
      "ground": "snow-kissed rocks",
      "atmosphere": "misty cold mountain air"
    },
    "surrounding_elements": ["strawberries scattered around the base"],
    "lighting": {
      "description": "warm sunlight gently breaks through the icy fog",
      "effects": "soft lens flares"
    },
    "style_descriptors": ["cinematic close-up", "high detail", "hyper-realistic textures"],
    "parameters": "--ar 9:16 --stylize 250"
  }
]
```

**Fonte:** [@YaseenK7212](https://x.com/YaseenK7212/status/2004930351584444801)

---

## Sneaker & Fashion Products

### Nike Air Force Cosmic

**Descrição:** Tênis Nike em ambiente espacial com efeitos de meteoro e energia.

```json
[
  {
    "id": 1,
    "main_subject": {
      "item": "Nike Air Force sneaker",
      "primary_material": "Dark carbon meteorite",
      "texture_description": "Meteorite material"
    },
    "illumination_details": {
      "type": "Glowing plasma threads",
      "placement": "Lined along the edges",
      "colors": ["Turquoise"]
    },
    "environment": {
      "location": "Space",
      "proximity_to": "Near a massive asteroid impact"
    },
    "dynamic_effects": {
      "action": "Fragments bursting outward",
      "effect_type": "Cinematic explosion effects"
    },
    "parameters": {
      "aspect_ratio": "2:3"
    }
  }
]
```

**Variações disponíveis:** Magma version, Emerald energy veins, Orange/Red explosion

**Fonte:** [@YaseenK7212](https://x.com/YaseenK7212/status/2003107440137539848)

---

### Chanel Perfume Grid Campaign

**Descrição:** Grid 3x3 de product shots de perfume luxury.

```json
{
  "campaign_details": {
    "project_name": "Pink Nike Sneaker & Silver Bow - High-End Commercial",
    "aspect_ratio": "3:4",
    "format": "3x3 Image Grid"
  },
  "global_directives": {
    "product_fidelity": "Product must remain identical in shape, proportions, materials across all frames.",
    "visual_style": "Hyperreal, cinematic, polished, high-end editorial advertising look."
  },
  "grid_layout": [
    {"row": 1, "column": 1, "concept": "Iconic Hero Still Life", "prompt_segment": "Product positioned centrally on polished marble pedestal with brushed silver accent edge."},
    {"row": 1, "column": 2, "concept": "Extreme Macro Detail", "prompt_segment": "Tight close-up focusing on metallic texture and intricate weave."},
    {"row": 1, "column": 3, "concept": "Dynamic Interaction", "prompt_segment": "Shoe suspended mid-air, splashing through glossy liquid burst."},
    {"row": 2, "column": 1, "concept": "Minimal Sculptural Scene", "prompt_segment": "Product amongst abstract, flowing organic forms of matte ceramic and polished chrome."},
    {"row": 2, "column": 2, "concept": "Floating Elements", "prompt_segment": "Product levitating weightlessly, surrounded by translucent silk ribbons and reflective spheres."},
    {"row": 2, "column": 3, "concept": "Sensory Close-up", "prompt_segment": "Manicured hand grazing the textured toe box, emphasizing tactility."}
  ]
}
```

**Fonte:** [@YaseenK7212](https://x.com/YaseenK7212/status/2001302056456339569)

---

## Creative Product Concepts

### Transparent Black Hyperrealism

**Descrição:** Objetos renderizados em vidro/polímero preto transparente com brilho interno.

```json
{
  "target_style": {
    "style_name": "ultra-modern transparent black hyperrealism",
    "visual_language": ["sleek", "futuristic", "minimalistic", "floating design", "high-gloss transparency"],
    "material_appearance": {
      "base_material": "transparent black glass or polymer",
      "texture_quality": "smooth and curved",
      "finish": "high-gloss with partial internal reflections"
    },
    "lighting_style": {
      "source_type": "rim light and directional top light",
      "shadows": "soft and diffuse glow underneath",
      "highlight_behavior": "sharp specular highlights across transparent surfaces"
    },
    "color_palette": {
      "dominant_colors": ["#000000", "#0d0d0d", "#1a1a1a"],
      "accent_colors": ["#ffffff", "#333333"],
      "contrast_level": "very high"
    },
    "rendering_style": {
      "dimensionality": "3D hyperrealistic",
      "depth_effects": "floating volumetric space with layered reflections"
    }
  },
  "output_settings": {
    "aspect_ratio": "1:1",
    "background_handling": "pure dark void"
  }
}
```

**Fonte:** [@azed_ai](https://x.com/azed_ai/status/2001932788023595077)

---

### Surreal Phone Pouring Ad

**Descrição:** Conceito surreal de mão real despejando líquido em copo dentro de tela de smartphone.

```json
{
  "meta": {
    "type": "Creative Brief",
    "genre": "Hyper-realistic Surrealism"
  },
  "realm_physical": {
    "active_agent": {
      "identity": "Human Hand (Real)",
      "action": "Pouring"
    },
    "held_object": {
      "item": "Bottle",
      "branding": {"logo_text": "Decamin"},
      "contents": {"substance": "Water", "color": "Light Green"}
    }
  },
  "realm_digital": {
    "container_device": {"model": "iPhone 17 Pro Max", "orientation": "Flat on surface"},
    "screen_content": {
      "subject": "Person holding glass with same branding",
      "setting": "Winter landscape"
    }
  },
  "surreal_bridge_event": {
    "action_type": "Trans-dimensional Fluid Dynamics",
    "physics_violation_rules": {
      "rule_1": "Liquid does not splash off the glass screen surface.",
      "rule_2": "Screen surface acts as a permeable membrane.",
      "rule_3": "Physical liquid transitions seamlessly into digital representation."
    }
  },
  "rendering_specifications": {
    "visual_fidelity": "Hyper-realistic",
    "resolution_target": "8K"
  }
}
```

**Fonte:** [@YaseenK7212](https://x.com/YaseenK7212/status/1996559154240967144)

---

### Vintage Software Box

**Descrição:** Simples e eficaz - transformar qualquer website em caixa de software dos anos 90.

```
{your website} into a product box with a CD-Rom as if it was from 1995
```

**Fonte:** [@levelsio](https://x.com/levelsio/status/1967593100676943892)

---

### Science of Comfort (Furniture in Pill Bottle)

**Descrição:** Catálogo conceitual com produto inesperado dentro de frasco de remédio.

```json
{
  "creative_id": "product_photography-749156f4",
  "creative_world": "product_photography",
  "deliverable_type": "catalog_cover",
  "core_tension": "comfort_vs_clinical",
  "twist_mechanisms": ["cutaway_logic", "function_misuse", "scale_mismatch"],
  "subject_kit": {
    "primary_subject": "a premium supplement bottle",
    "secondary_elements": ["tamper seal", "tiny lounge chair", "warning label sticker"]
  },
  "stage_context": "clean studio tabletop",
  "composition_rule": "centered, calm framing, high detail",
  "lighting_rule": "soft directional studio light, strong material definition"
}
```

**Fonte:** [@ttmouse](https://x.com/ttmouse/status/2003588959310660073)

---

## 🎨 Adaptação Neo-Brutalismo Pop

Para adaptar estes prompts ao estilo gui.marketing:

```
Product Photography Neo-Brutalist modifier:
"High-contrast studio lighting with electric lime (#C8FF00) and hot pink (#FF1BB3) 
gel accents. Bold graphic overlay elements, intentional grain, anti-corporate 
aesthetic with provocative messaging. Raw urban energy, streetwear influence."
```
