# ⚽ Sports & Action

> 28+ prompts curados para cenas esportivas, fitness, ação dinâmica e lifestyle ativo.

---

## Índice

- [Gym & Fitness Content](#gym--fitness-content)
- [Sports Action Shots](#sports-action-shots)
- [Lifestyle & Selfies](#lifestyle--selfies)

---

## Gym & Fitness Content

### Post-Workout Hydration Scene

**Descrição:** Cena de mulher após treino com atmosfera de academia.

```json
{
  "subject": {
    "description": "A young woman sitting on yoga mat, wiping sweat with towel, holding water bottle",
    "mirror_rules": "N/A - direct gym photo",
    "age": "late 20s",
    "expression": "accomplished, slight breathlessness, confident smile",
    "hair": {
      "color": "blonde with highlights",
      "style": "high ponytail, slightly messy with flyaways from workout"
    },
    "clothing": {
      "top": {
        "type": "sports bra",
        "color": "dusty rose pink",
        "details": "medium support, strappy back detail, moisture visible from sweat"
      },
      "bottom": {
        "type": "high-waisted leggings",
        "color": "black with mesh panels",
        "details": "ankle length, mesh cutouts on calves, compression fit"
      }
    },
    "face": {
      "preserve_original": true,
      "makeup": "minimal, dewy from workout, natural flushed cheeks, no eye makeup"
    }
  },
  "accessories": {
    "headwear": {"type": "none", "details": "hair pulled back in scrunchie"},
    "jewelry": {
      "earrings": "small diamond studs",
      "necklace": "none",
      "wrist": "rose gold fitness tracker, black hair ties on wrist",
      "rings": "none"
    },
    "device": {
      "type": "smartphone",
      "details": "propped against dumbbell, recording workout selfie"
    },
    "prop": {
      "type": "insulated water bottle",
      "details": "matte black 32oz bottle with motivational quote sticker, condensation visible"
    }
  },
  "photography": {
    "camera_style": "gym selfie aesthetic, smartphone front camera",
    "angle": "slightly above eye level, sitting position",
    "shot_type": "full upper body and crossed legs, centered composition",
    "aspect_ratio": "9:16 vertical",
    "texture": "crisp detail, bright gym lighting, energetic feel"
  },
  "background": {
    "setting": "modern gym studio",
    "wall_color": "light gray with motivational mural",
    "elements": [
      "purple yoga mat laid out",
      "set of dumbbells scattered nearby",
      "white towel draped over shoulder",
      "blurred gym equipment in background",
      "large mirror reflecting back wall",
      "resistance bands coiled on floor"
    ],
    "atmosphere": "energetic, accomplished, health-focused",
    "lighting": "bright overhead LED gym lighting, even coverage"
  }
}
```

**Fonte:** [@godofprompt](https://x.com/godofprompt/status/1994226363692171267)

---

## JSON Template Completo para Fitness

### Estrutura Base para Gym/Fitness Content

```json
{
  "subject": {
    "description": "[Action-based scene overview in one sentence]",
    "mirror_rules": "[Text handling for mirror selfies OR 'N/A - direct photo']",
    "age": "[Approximate age: early 20s, mid-20s, late 20s, young adult]",
    "expression": "[Emotion and gaze: accomplished smile, energetic, breathless]",
    "hair": {
      "color": "[Specific color with details: blonde with highlights, chestnut brown]",
      "style": "[Style with realistic imperfections: high ponytail slightly messy with flyaways]"
    },
    "clothing": {
      "top": {
        "type": "[sports bra, tank top, crop top]",
        "color": "[Specific color: dusty rose pink, heather gray]",
        "details": "[Fabric, fit, features: medium support, cropped fit]"
      },
      "bottom": {
        "type": "[high-waisted leggings, shorts, joggers]",
        "color": "[Color]",
        "details": "[Style details]"
      }
    },
    "face": {
      "preserve_original": true,
      "makeup": "[Match activity: minimal dewy for gym, natural sunkissed for casual]"
    }
  },
  "accessories": {
    "headwear": {"type": "[baseball cap, none]", "details": "[Color, logo, how worn]"},
    "jewelry": {
      "earrings": "[small diamond studs, none]",
      "necklace": "[thin gold chain, or none]",
      "wrist": "[fitness tracker, hair ties, or none]",
      "rings": "[none - gym safety]"
    },
    "device": {
      "type": "[smartphone]",
      "details": "[Phone brand/model, case color, how held]"
    },
    "prop": {
      "type": "[water bottle, towel, or none]",
      "details": "[Brand, size, color, specific features like condensation, stickers]"
    }
  },
  "photography": {
    "camera_style": "[smartphone front camera, mirror selfie aesthetic]",
    "angle": "[slightly above eye level, eye-level mirror reflection]",
    "shot_type": "[full upper body, waist-up, 3/4 body]",
    "aspect_ratio": "9:16 vertical",
    "texture": "[crisp detail bright lighting, natural indoor lighting warm tones]"
  },
  "background": {
    "setting": "[modern gym studio, home gym, outdoor workout]",
    "wall_color": "[light gray, plain white]",
    "elements": "[Specific observable items: scattered equipment, personal items]",
    "atmosphere": "[energetic accomplished, casual spontaneous]",
    "lighting": "[bright overhead LED, soft natural daylight]"
  }
}
```

---

## Scenario-Specific Guidelines

### Gym/Fitness Content Rules

- **Context:** Post-workout energy, athletic wear, minimal makeup
- **Accessories:** Fitness tracker, water bottle, towel, hair ties, NO luxury jewelry
- **Background:** Gym equipment, mirrors, yoga mats, weights
- **Expression:** Accomplished, breathless, energetic
- **Imperfections:** Flyaways, moisture from sweat, flushed cheeks
- **Makeup:** "minimal, dewy from workout, natural flushed cheeks, no eye makeup"

### Mirror Selfies

- **Context:** Casual bedroom/bathroom, lifestyle moment
- **CRITICAL:** Always include mirror_rules field
- **Accessories:** Phone case details, everyday jewelry, drink/prop in hand
- **Background:** Bed, nightstand, personal items (unmade bed adds realism)
- **Expression:** Playful, candid, relaxed
- **Action:** "biting straw", "hand on hip", "holding drink"
- **Position:** Often off-center (left or right side of frame)

### Car Selfies

- **Context:** On-the-go moment, casual comfort
- **Shot:** Close-up portrait (chest/face up)
- **Accessories:** Minimal (glasses perfect, simple jewelry)
- **Background:** Car ceiling, headrest, seatbelt, window with blur outside
- **Expression:** Candid, gentle, relaxed
- **Clothing:** Hoodie, casual top, comfortable
- **Lighting:** "soft natural window light illuminating the face"
- **Hand:** Often touching face, forehead, hair naturally

### Street/Outdoor Photos

- **Context:** Urban fashion, lifestyle
- **Shot:** Full body or 3/4 body
- **Action:** Walking, leaning against wall, sitting on steps
- **Accessories:** Bag/backpack common, sunglasses
- **Background:** Storefronts, brick walls, urban details, blurred people
- **Lighting:** Golden hour, overcast, bright midday
- **Hair:** Wind-blown, natural outdoor styling
- **Expression:** Confident, natural, candid (not posed)

---

## Example Prompts

### Gym Selfie

```json
{
  "subject": {
    "description": "Young woman sitting on gym floor after intense workout, drinking from water bottle",
    "age": "mid-20s",
    "expression": "accomplished, slightly breathless, satisfied smile",
    "hair": {
      "color": "brunette with caramel highlights",
      "style": "high messy ponytail with sweaty baby hairs"
    },
    "clothing": {
      "top": {"type": "sports bra", "color": "black", "details": "minimal padding, racerback"},
      "bottom": {"type": "high-waisted leggings", "color": "dark gray", "details": "sweat marks visible"}
    },
    "face": {
      "preserve_original": true,
      "makeup": "no makeup, natural post-workout glow, flushed cheeks"
    }
  },
  "accessories": {
    "wrist": "Apple Watch showing workout stats",
    "prop": {"type": "metal water bottle", "details": "blue hydroflask with gym stickers"}
  },
  "photography": {
    "camera_style": "selfie taken during rest",
    "shot_type": "upper body seated",
    "aspect_ratio": "9:16"
  },
  "background": {
    "setting": "commercial gym floor",
    "elements": ["weight rack behind", "other gym-goers blurred", "rubber flooring"]
  }
}
```

### Mirror Selfie

```json
{
  "subject": {
    "description": "Woman taking mirror selfie in bedroom, playfully biting straw of iced coffee",
    "mirror_rules": "Phone visible in mirror reflection, text on objects may appear reversed",
    "age": "early 20s",
    "expression": "playful, biting straw, slight eyebrow raise",
    "hair": {
      "color": "chocolate brown",
      "style": "loose waves, slightly messy bedhead look"
    },
    "clothing": {
      "top": {"type": "oversized band t-shirt", "color": "vintage black", "details": "cropped, worn-in texture"},
      "bottom": {"type": "high-waisted denim shorts", "color": "light wash", "details": "distressed"}
    }
  },
  "accessories": {
    "jewelry": {
      "earrings": "gold hoops",
      "necklace": "layered gold chains"
    },
    "device": {"type": "iPhone", "details": "held at waist level, clear case"},
    "prop": {"type": "iced coffee", "details": "Starbucks cup with cream visible, condensation on cup"}
  },
  "photography": {
    "camera_style": "mirror selfie aesthetic",
    "angle": "straight-on, standing off-center in frame",
    "aspect_ratio": "9:16"
  },
  "background": {
    "setting": "casual bedroom",
    "elements": ["unmade bed visible", "fairy lights", "posters on wall"]
  }
}
```

### Car Selfie

```json
{
  "subject": {
    "description": "Woman taking relaxed selfie in parked car, hand gently touching forehead",
    "age": "mid-20s",
    "expression": "gentle, relaxed, soft smile",
    "hair": {
      "color": "dirty blonde",
      "style": "loose, slightly wind-tousled"
    },
    "clothing": {
      "top": {"type": "cozy oversized hoodie", "color": "sage green", "details": "hood down, relaxed fleece"}
    }
  },
  "accessories": {
    "jewelry": {
      "earrings": "small gold studs",
      "necklace": "delicate gold chain"
    }
  },
  "photography": {
    "camera_style": "car selfie, close portrait",
    "shot_type": "face and shoulders only",
    "texture": "soft natural window light, slightly warm"
  },
  "background": {
    "setting": "interior of car",
    "elements": ["headrest visible", "seatbelt strap", "blurred trees outside window"]
  }
}
```

---

## Consistency Checklist

Before generating, verify:

- [ ] Accessories match setting (fitness tracker at gym, NOT diamond rings)
- [ ] Makeup matches activity (minimal/dewy for workout, natural for casual)
- [ ] Clothing appropriate for scenario (athleisure for gym, hoodie for car)
- [ ] Background elements realistic for setting
- [ ] Expression matches action (accomplished after workout, playful with drink)
- [ ] mirror_rules specified correctly if mirror selfie
- [ ] Imperfections included subtly
- [ ] Camera language simple, not technical
- [ ] Action described, not static pose

---

## 🎨 Adaptação Neo-Brutalismo Pop

Para adaptar estes prompts ao estilo gui.marketing:

```
Sports & Action Neo-Brutalist modifier:
"High-energy fitness aesthetic with electric lime (#C8FF00) and 
hot pink (#FF1BB3) accent lighting. Bold motivational text overlays 
in block typography, urban streetwear athletic style, 
gritty warehouse gym setting, anti-perfectionist sweat and effort visible. 
Rebellious athlete attitude, not polished influencer aesthetic."
```
