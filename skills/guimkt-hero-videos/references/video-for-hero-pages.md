# video-for-hero-pages — Referência Completa

## O que é

Gera prompts de vídeo otimizados para uso no `hero-pages-videobg`. O vídeo gerado precisa funcionar **sem color overlay** — então contraste, luminosidade e loopability são requisitos técnicos, não estéticos.

---

## PROMPT PRINCIPAL (Cole na ferramenta de vídeo IA)

```
Generate a cinematic background video for a premium web hero section with the following strict technical and aesthetic requirements:

TECHNICAL SPECS (non-negotiable):
- Aspect ratio: 16:9 (landscape, full-screen web)
- Duration: 6–12 seconds, seamlessly loopable (first and last frames must be visually compatible for a smooth loop)
- Resolution: 1920x1080 minimum
- Motion: Slow, deliberate camera movement only — no fast cuts, no flash transitions, no abrupt changes
- Audio: None (will be muted on web)

CONTRAST & READABILITY REQUIREMENTS (critical — no color overlay will be applied):
- The center-vertical zone of the frame must have naturally darker or more uniform tones to allow white and dark text to be readable without any overlay
- Avoid high-contrast edges, busy patterns, or bright focal points in the top-center and center areas where headlines and CTAs will be placed
- Ideal luminosity: the overall frame should tend toward darker midtones (not black, not blown-out bright) — cinematic, moody, controlled
- If the scene contains light sources (sun, neon, studio lights), position them at the edges or corners of the frame

VISUAL DIRECTION:
- Style: {{STYLE}}
- Subject/Scene: {{SUBJECT_OR_SCENE}}
- Color palette: {{COLOR_PALETTE}}
- Mood: {{MOOD}}

MOVEMENT CONSTRAINTS:
- Camera movement: Slow dolly, subtle parallax, or locked-off with organic in-frame motion only
- No zoom-in that causes sudden brightness shifts
- Loop point: The video must end in a way that can cut back to frame 1 without a visible jump

WHAT TO AVOID:
- Fast cuts or montage-style editing
- Flashing or strobe effects
- Large bright white areas in the center of the frame
- Text, watermarks, or UI elements
- Faces as the primary focal point
- Oversaturated neon unless edge-contained

OUTPUT GOAL:
A video that functions as an atmospheric, breathing backdrop — present but subordinate. The viewer's eye should land on the text overlaid on top, not fight it.
```

---

## VARIÁVEIS — GUIA DE PREENCHIMENTO

| Variável | O que definir |
|---|---|
| `{{STYLE}}` | Estética geral do vídeo (ex: `dark editorial studio`, `cinematic urban night`) |
| `{{SUBJECT_OR_SCENE}}` | O que aparece no vídeo (ex: `slow pan over dark creative workspace`) |
| `{{COLOR_PALETTE}}` | 2–3 cores dominantes (ex: `near-black, deep navy, silver highlights`) |
| `{{MOOD}}` | Emoção evocada (ex: `powerful, premium, silent confidence`) |

---

## VARIAÇÕES POR NICHO (prontas para usar)

### Agência de Vídeo / Criação de Conteúdo
```
Style: dark cinematic studio
Subject: slow dolly through professional video equipment — cameras, lenses, monitors with subtle blue glow — all in near darkness
Palette: deep charcoal, matte black, cold blue accent
Mood: premium, technical, confident
```

### SaaS / Tecnologia
```
Style: abstract data motion
Subject: dark digital particles slowly forming and dissolving, like a neural network breathing
Palette: near-black background, electric indigo and teal particles
Mood: intelligent, calm, futuristic
```

### Agência de Marketing / Growth
```
Style: editorial urban night
Subject: slow aerial drift over a city at night, lights below, dark sky above
Palette: warm amber streetlights against navy blue darkness
Mood: energetic, aspirational, premium
```

### Produto de Luxo / Moda
```
Style: luxury product slow-mo
Subject: dark fabric texture shifting slowly, with a single light source creating a moving highlight
Palette: pure black, silk gray, silver
Mood: silent luxury, restrained, desirable
```

### Fitness / Lifestyle
```
Style: high-contrast slow motion
Subject: abstract athletic movement — water droplets, fabric in slow motion — against dark background
Palette: near-black, electric white highlights, single warm tone
Mood: powerful, kinetic, aspirational
```

### Imobiliário / Arquitetura
```
Style: architectural minimalism
Subject: slow camera glide through a dark, dramatically lit interior space — concrete, glass, light shafts
Palette: warm concrete gray, deep shadow, single warm light source
Mood: exclusive, calm, considered
```

---

## CHECKLIST PRÉ-ENTREGA

Antes de usar a URL do vídeo no `hero-pages-videobg`:

- [ ] Loop sem salto visual perceptível entre final e início?
- [ ] Área central do frame tem ton escuro/uniforme para texto legível sem overlay?
- [ ] Nenhum flash, corte ou mudança brusca de luminosidade?
- [ ] Movimento suave — sem agitação ou câmera tremida?
- [ ] Sem rostos centralizados, texto embutido, ou objetos em movimento rápido no centro?
- [ ] Aspect ratio 16:9, sem barras?
- [ ] Duração entre 6–12 segundos?

---

## FERRAMENTAS RECOMENDADAS

| Ferramenta | Configuração sugerida | Ponto forte |
|---|---|---|
| **Runway Gen-4** | Motion Brush: baixo / Camera: Slow Dolly | Controle de câmera |
| **Sora** | Loop mode ON, duration: 10s | Looping nativo |
| **Kling 1.6** | Standard mode, 10s, Professional | Realismo cinematográfico |
| **Pika 2.2** | Camera motion: subtle | Controle granular |
| **Hailuo (MiniMax)** | Slow motion preset | Slow-mo orgânico |

> Gere 3–5 variações do mesmo prompt e selecione a que melhor passa no checklist.

---

## NOTAS TÉCNICAS CRÍTICAS

**Por que sem overlay importa:**
O `hero-pages-videobg` renderiza o vídeo sem camada de opacidade — isso é intencional para visual premium, mas toda a responsabilidade de contraste cai sobre o vídeo. Um vídeo claro ou agitado no centro torna headline e CTA ilegíveis.

**Sobre looping:**
Prefira cenas com movimento contínuo e lento (partículas, névoa, câmera lenta) em vez de cenas com eventos discretos (um carro passando). O loop de eventos discretos é sempre perceptível.

**Sobre duração:**
6–8 segundos é o sweet spot. Curto demais = loop frequente e visível. Longo demais = arquivo pesado, impacto na performance de carregamento da landing page.
