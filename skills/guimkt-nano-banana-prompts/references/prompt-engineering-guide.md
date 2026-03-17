# Prompt Engineering Guide — Nano Banana Prompts

> Referência técnica extraída de [Awesome Nano Banana Prompts](https://github.com/devanshug2307/Awesome-Nano-Banana-Prompts) e [antigravity.codes/nano-banana-prompts](https://antigravity.codes/nano-banana-prompts).

---

## JSON Structure Template (Padrão Completo)

Use esta estrutura para criar prompts avançados de portrait/lifestyle:

```json
{
  "subject": {
    "description": "[Cena em uma frase com ação]",
    "mirror_rules": "[Regras de espelhamento OU 'N/A - direct photo']",
    "age": "[early 20s, mid-20s, late 20s, young adult]",
    "expression": "[Emoção + direção do olhar: accomplished smile, playful biting straw]",
    "hair": {
      "color": "[Cor específica: blonde with highlights, chestnut brown]",
      "style": "[Estilo com imperfeições: high ponytail slightly messy with flyaways]"
    },
    "clothing": {
      "top": {
        "type": "[sports bra, ribbed cami, oversized hoodie]",
        "color": "[dusty rose pink, heather gray]",
        "details": "[Tecido, caimento: medium support, cropped fit, relaxed fleece]"
      },
      "bottom": {
        "type": "[high-waisted leggings, denim jeans, joggers]",
        "color": "[Cor]",
        "details": "[Detalhes de estilo]"
      }
    },
    "face": {
      "preserve_original": true,
      "makeup": "[Match activity: minimal dewy for gym, natural sunkissed for casual]"
    }
  },
  "accessories": {
    "headwear": {
      "type": "[baseball cap, none]",
      "details": "[Cor, logo, como usado]"
    },
    "jewelry": {
      "earrings": "[small diamond studs, large gold hoops, none]",
      "necklace": "[thin gold chain with pendant, none]",
      "wrist": "[fitness tracker, gold bangles, hair ties, none]",
      "rings": "[multiple gold rings, simple band, none]"
    },
    "device": {
      "type": "[smartphone]",
      "details": "[Marca/modelo, cor da case, como segurado]"
    },
    "prop": {
      "type": "[water bottle, iced beverage, none]",
      "details": "[Marca, tamanho, cor, features: condensation, stickers]"
    }
  },
  "photography": {
    "camera_style": "[smartphone front camera, mirror selfie, DSLR rear camera]",
    "angle": "[slightly above eye level, eye-level mirror, low angle]",
    "shot_type": "[full upper body, waist-up, close-up portrait, 3/4 body]",
    "aspect_ratio": "9:16 vertical",
    "texture": "[crisp detail bright lighting, natural indoor warm tones]"
  },
  "background": {
    "setting": "[modern gym studio, bright bedroom, car interior, urban sidewalk]",
    "wall_color": "[light gray, plain white, N/A]",
    "elements": [
      "[Itens observáveis específicos]",
      "[Equipamento, itens pessoais]",
      "[Detalhes ambientais]",
      "[Elementos desfocados ao fundo]"
    ],
    "atmosphere": "[energetic accomplished, casual spontaneous, relaxed daily]",
    "lighting": "[bright overhead LED, soft natural daylight, window light]"
  }
}
```

---

## Contextual Consistency Checklist

Antes de entregar um prompt, verificar:

- [ ] Acessórios compatíveis com o cenário (fitness tracker na academia, NÃO anéis de diamante)
- [ ] Maquiagem compatível com a atividade (minimal/dewy para workout, natural para casual)
- [ ] Roupa apropriada para o cenário (athleisure para gym, hoodie para carro)
- [ ] Elementos do background realistas para o setting
- [ ] Expressão compatível com a ação (accomplished após workout, playful com drink)
- [ ] `mirror_rules` especificado corretamente se for mirror selfie
- [ ] Imperfeições incluídas sutilmente (flyaways, pele natural)
- [ ] Integração de produto natural (se aplicável)
- [ ] Linguagem de câmera simples, não técnica
- [ ] Ação descrita, não pose estática

---

## Scenario-Specific Guidelines

### Gym / Fitness

- **Contexto:** Energia pós-treino, roupa atlética, maquiagem mínima
- **Acessórios:** Fitness tracker, garrafa d'água, toalha, elásticos de cabelo. SEM joias de luxo
- **Background:** Equipamentos, espelhos, yoga mats, halteres
- **Expressão:** Accomplished, breathless, energetic
- **Imperfeições:** Flyaways, umidade do suor, bochechas avermelhadas
- **Maquiagem:** "minimal, dewy from workout, natural flushed cheeks, no eye makeup"

### Mirror Selfies

- **Contexto:** Quarto/banheiro casual, momento lifestyle
- **CRÍTICO:** Sempre incluir campo `mirror_rules`
- **Acessórios:** Detalhes da capa do celular, joias do dia a dia, drink na mão
- **Background:** Cama, criado-mudo, itens pessoais, cama desarrumada adiciona realismo
- **Expressão:** Playful, candid, relaxed
- **Ação:** "biting straw", "hand on hip", "holding drink"
- **Posição:** Frequentemente off-center (lado esquerdo ou direito do frame)

### Car Selfies

- **Contexto:** Momento on-the-go, conforto casual
- **Shot:** Close-up portrait (peito/rosto para cima)
- **Acessórios:** Mínimos (óculos funciona, joias simples)
- **Background:** Teto do carro, apoio de cabeça, cinto, janela com blur
- **Expressão:** Candid, gentle, relaxed
- **Roupa:** Hoodie, top casual, confortável
- **Iluminação:** "soft natural window light illuminating the face"
- **Mão:** Frequentemente tocando rosto, testa, cabelo naturalmente

### Street / Outdoor

- **Contexto:** Fashion urbano, lifestyle
- **Shot:** Full body ou 3/4 body
- **Ação:** Walking, leaning against wall, sitting on steps
- **Acessórios:** Bolsa/mochila comum, óculos de sol
- **Background:** Lojas, paredes de tijolo, detalhes urbanos, pessoas desfocadas
- **Iluminação:** Golden hour, overcast, bright midday
- **Cabelo:** Wind-blown, styling natural outdoor
- **Expressão:** Confident, natural, candid (not posed)

---

## Variation Strategy

Ao gerar múltiplos prompts (5-10), variar sistematicamente:

| Dimensão | Variações |
|----------|-----------|
| **Cenários** | Gym → Mirror selfie → Car → Street → Indoor cafe |
| **Ações** | Wiping sweat → Biting straw → Hand on forehead → Walking → Sitting |
| **Ângulos** | Front camera → Mirror → Low angle → Eye level → Slightly above |
| **Iluminação** | Bright overhead → Soft window → Golden hour → Overcast → Mixed |
| **Expressões** | Accomplished → Playful → Relaxed → Confident → Candid |
| **Cabelo** | Ponytail → Down loose → Bun → Half-up → Braided |
| **Cores** | Neutrals → Pastels → Earth tones → Bold → Monochrome |

---

## Common Mistakes to Avoid

| ❌ Erro | ✅ Correto |
|---------|-----------|
| Jargão técnico: "3200K color temperature, f/1.8 aperture" | Linguagem simples: "soft natural window light" |
| Acessórios errados pro contexto: diamond rings at gym | Acessórios contextuais: fitness tracker, hair ties |
| Descrições estáticas: "Standing confidently" | Baseado em ação: "Wiping sweat with towel, holding water bottle" |
| Perfeito/staged: Everything pristine | Autêntico: Flyaways, unmade bed, moisture from sweat |
| Esquecer mirror_rules: Text on clothes reversed | Sempre especificar: "ignore mirror physics for text on clothing" |
| Product placement genérico: "Holding product" | Integração natural: "Playfully biting the straw of iced matcha latte" |

---

## Communication Style

Ao entregar prompts, ser direto e confiante:

| ❌ Evitar | ✅ Preferir |
|-----------|-----------|
| "Criei alguns prompts que podem funcionar" | "5 prompts de gym selfie otimizados para fotografia smartphone realista" |
| "Este prompt inclui especificações de iluminação" | "Capturando momento pós-treino com iluminação overhead natural" |
| "Primeiro você precisa copiar a estrutura JSON..." | "Cole o JSON no Nano Banana e gere" |

---

## Ferramentas Compatíveis

Testados e refinados para:

- **Gemini** (Google)
- **DALL-E** (OpenAI)
- **Midjourney**
- **Stable Diffusion**
- **Nano Banana Pro**
- **Grok** (xAI)
- **ChatGPT Image** (GPT-Image-1)
- **Flux**

---

## Galeria com Busca

Para navegar visualmente todos os 874+ prompts com preview de imagem:
👉 [antigravity.codes/nano-banana-prompts](https://antigravity.codes/nano-banana-prompts)

Para repositório open-source com todos os prompts em Markdown:
👉 [github.com/devanshug2307/Awesome-Nano-Banana-Prompts](https://github.com/devanshug2307/Awesome-Nano-Banana-Prompts)
