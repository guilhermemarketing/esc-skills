# 👗 Fashion Photography

> 50+ prompts curados para fotografia de moda, lookbooks e editorial fashion.

---

## Índice

- [Editorial Fashion](#editorial-fashion)
- [Streetwear & Urban](#streetwear--urban)
- [Activewear & Fitness](#activewear--fitness)
- [E-commerce & Catalog](#e-commerce--catalog)

---

## Editorial Fashion

### High Fashion Editorial

**Descrição:** Foto de moda editorial high-end.

```json
{
  "subject_identity": {
    "face_match": "100% match to reference image",
    "body_proportions": "maintain exact reference proportions"
  },
  "pose_and_styling": {
    "posture": "High-fashion editorial pose, confident",
    "gaze": "Direct to camera or editorial away gaze"
  },
  "wardrobe_composition": {
    "ensemble_type": "[Full outfit description]",
    "outerwear": {
      "item": "[garment type]",
      "color": "[color]",
      "tailoring": "[fit description]",
      "styling": "[how worn]"
    },
    "innerwear": {
      "item": "[undergarment/layer]",
      "color": "[color]",
      "style": "[style notes]"
    },
    "bottoms": {
      "fit": "[pants/skirt description]"
    },
    "accessories": "[shoes, bags, jewelry]"
  },
  "environmental_context": {
    "setting": {
      "location": "[studio/outdoor/architectural]",
      "background_surface": "[color/material]"
    },
    "lighting_conditions": {
      "source": "[lighting type]",
      "characteristics": ["[quality1]", "[quality2]"]
    }
  },
  "photographic_execution": {
    "genre": "High Fashion Editorial",
    "mood": "[emotional descriptor]",
    "framing": "[shot type]",
    "focus": "Sharp focus on subject, distinct separation from background"
  }
}
```

---

### Runway-Style Photo

**Descrição:** Foto estilo passarela/desfile.

```json
{
  "subject": {
    "pose": "mid-stride, walking movement",
    "expression": "neutral, confident, model stare",
    "body_position": "full body, walking towards camera"
  },
  "wardrobe": {
    "outfit": "[Designer/brand look description]",
    "shoes": "[footwear, crucial for runway]",
    "accessories": "[minimal, designer pieces]"
  },
  "photography": {
    "style": "runway photography",
    "shot_type": "full body, capturing movement",
    "aspect_ratio": "3:4 or 2:3 vertical"
  },
  "environment": {
    "setting": "neutral runway or studio backdrop",
    "lighting": "bright, even, no harsh shadows"
  }
}
```

---

## Streetwear & Urban

### Street Style Photo

**Descrição:** Foto de estilo urbano/street fashion.

```json
{
  "subject": {
    "description": "Street style photo of person in urban setting",
    "expression": "confident, slightly candid",
    "pose": "natural, relaxed, authentic street moment"
  },
  "wardrobe": {
    "style": "contemporary streetwear",
    "elements": "[list key pieces: oversized jacket, sneakers, etc.]",
    "brands": "[optional: brand references]"
  },
  "photography": {
    "style": "street fashion photography",
    "camera": "35mm or 50mm aesthetic",
    "shot_type": "full body or 3/4"
  },
  "environment": {
    "setting": "urban street, architectural backdrop",
    "elements": ["graffiti walls", "industrial doors", "city streets"],
    "lighting": "natural daylight or golden hour"
  },
  "mood": "authentic, cool, urban edge"
}
```

---

## Activewear & Fitness

### Gym Fashion Shot

**Descrição:** Foto de moda fitness/activewear.

```json
{
  "subject": {
    "physique": "Fit, toned",
    "expression": "Confident, energetic",
    "pose": "Athletic, dynamic or power pose"
  },
  "apparel": {
    "upper_body": {
      "item": "[Sports bra/tank/crop]",
      "color": "[color]",
      "fit": "Athletic/Compression"
    },
    "lower_body": {
      "item": "[Leggings/shorts]",
      "color": "[color]",
      "texture": "[Fabric details]"
    },
    "footwear": "Athletic sneakers"
  },
  "environment": {
    "setting_type": "Indoor Gym / Outdoor / Studio",
    "props": "[Equipment visible]",
    "lighting": "Bright, high-key fitness aesthetic"
  },
  "photography": {
    "framing": "Full body or medium shot",
    "style": "Commercial activewear campaign",
    "focus": "Sharp on subject, workout environment context"
  }
}
```

**Fonte:** Repositório Nano Banana

---

## E-commerce & Catalog

### Product Flat Lay

**Descrição:** Flat lay de produtos de moda.

```
Professional e-commerce flat lay of [PRODUCT CATEGORY].

Layout: Organized grid or styled arrangement
Items: [list items with colors and details]

Background: Pure white or neutral surface
Lighting: Soft, even, product photography standard
Style: Clean, commercial, catalog-ready

Technical: High resolution, true-to-color representation.
```

---

### Model with Product Focus

**Descrição:** Modelo usando produto com foco comercial.

```json
{
  "subject": {
    "role": "Product model",
    "expression": "neutral or brand-appropriate",
    "pose": "showcasing the product naturally"
  },
  "product_focus": {
    "item": "[specific product being featured]",
    "visibility": "clearly visible and prominent",
    "details": "[key features to highlight]"
  },
  "photography": {
    "style": "e-commerce/catalog",
    "framing": "depends on product - full body for clothing",
    "focus": "product in sharp focus"
  },
  "background": "clean, simple, non-distracting",
  "lighting": "even, bright, accurate color representation"
}
```

---

## Template Completo para Fashion

```json
{
  "subject_identity": {
    "face_match": "100% match to reference if provided",
    "body_proportions": "maintain reference proportions"
  },
  "pose_and_styling": {
    "posture": "[pose description]",
    "gaze": "[direction]",
    "hands": "[hand position]",
    "stance": "[feet/body position]"
  },
  "wardrobe_composition": {
    "ensemble_type": "[overall style]",
    "outerwear": {"item": "", "color": "", "styling": ""},
    "top": {"item": "", "color": "", "fit": ""},
    "bottom": {"item": "", "color": "", "fit": ""},
    "footwear": {"item": "", "color": ""},
    "accessories": {"bags": "", "jewelry": "", "other": ""}
  },
  "environmental_context": {
    "setting": {"location": "", "background": ""},
    "lighting_conditions": {"source": "", "quality": ""}
  },
  "photographic_execution": {
    "genre": "[photography style]",
    "mood": "[emotional tone]",
    "framing": "[shot type]",
    "aspect_ratio": "[ratio]"
  },
  "constraints": {
    "negative_prompt": ["things to avoid"]
  }
}
```

---

## 🎨 Adaptação Neo-Brutalismo Pop

```
Fashion Neo-Brutalist modifier:
"Bold fashion photography with electric lime (#C8FF00) and 
hot pink (#FF1BB3) accent elements. Street style meets high fashion, 
anti-luxury rebellion aesthetic, graffiti integration, 
punk influence, provocative styling, raw urban energy."
```
