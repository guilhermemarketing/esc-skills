# hero-pages-videobg — Referência Completa

## O que é

Gera hero sections premium com vídeo no background. Sem color overlays — o contraste é garantido pelo próprio vídeo e pela tipografia.

---

## PROMPT BASE (adaptar conforme o input do usuário)

```
Build a premium, high-end hero section for [NOME_DA_MARCA] with the following specifications:

Background: Implement a full-screen, looping video background using this URL: [VÍDEO_URL]. The video must be muted, autoplaying, and set to object-cover to fill the section without any color overlays.

Navigation Bar: A floating [COR_NAV] navigation bar with rounded-[16px] and a subtle shadow.
- Left: The brand/agency logo.
- Center: A menu with links for [LINKS_MENU] using 14px Barlow Medium font.
- Right: A [COR_CTA] primary CTA button labeled '[TEXTO_CTA]' featuring a unique 45-degree arrow icon in a circular housing.

Typography & Hero Content:
- Primary Headline: Centered layout. First line '[LINHA_1_HEADLINE]' — bold/medium Barlow font, tight tracking (tracking-[-4px]). Second line '[LINHA_2_HEADLINE]' — large Instrument Serif italic (text-[84px]).
- Subtext: '[SUBTEXT]' in Barlow Medium, 18px, centered.
- Secondary CTA: A large white pill-shaped button labeled '[TEXTO_CTA_SECUNDARIO]' with a small play icon on the left.

Overall Aesthetic: Minimal, ultra-modern, responsive. All text and buttons layered on top of the video with clear visibility and proper spacing (min-h-[90vh]).
```

---

## VARIÁVEIS E VALORES PADRÃO

| Variável | Padrão se não fornecido |
|---|---|
| `[NOME_DA_MARCA]` | Nome fornecido pelo usuário (obrigatório) |
| `[VÍDEO_URL]` | `{{VÍDEO_URL}}` como placeholder |
| `[COR_NAV]` | `white` |
| `[LINKS_MENU]` | `About, Works, Services, Testimonial` |
| `[COR_CTA]` | `dark (#222)` |
| `[TEXTO_CTA]` | `Book A Free Meeting` |
| `[LINHA_1_HEADLINE]` | Inferir da marca |
| `[LINHA_2_HEADLINE]` | Inferir da marca — usar Instrument Serif italic |
| `[SUBTEXT]` | Inferir do nicho |
| `[TEXTO_CTA_SECUNDARIO]` | `See Our Workreel` / `Watch Demo` |

---

## REQUISITOS TÉCNICOS OBRIGATÓRIOS

### Vídeo background
```html
<video
  autoplay
  muted
  loop
  playsinline
  class="absolute inset-0 w-full h-full object-cover"
>
  <source src="[VÍDEO_URL]" type="video/mp4" />
</video>
```

- `autoplay` + `muted` + `loop` + `playsinline` — todos obrigatórios
- `object-cover` — preenche sem distorção
- **Sem overlay de cor** (`background-color`, `opacity` layer, gradiente) sobre o vídeo

### Navbar flutuante
- `position: fixed` ou `absolute` com `z-index` alto
- `border-radius: 16px`
- `box-shadow` sutil
- Fundo branco ou translúcido

### Typography stack
```css
/* Fonte display */
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&display=swap');

/* Fonte corpo */
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&display=swap');
```

### Headline pattern
```html
<!-- Linha 1: Barlow bold, tracking tight -->
<p class="font-barlow font-bold tracking-[-4px] text-[32px] text-white">
  Agency that makes your
</p>

<!-- Linha 2: Instrument Serif italic, grande -->
<h1 class="font-instrument-serif italic text-[84px] text-white leading-none">
  videos & reels viral
</h1>
```

### CTA primário (navbar)
```html
<button class="bg-[#222] text-white px-5 py-2.5 rounded-full flex items-center gap-2 text-sm font-medium">
  Book A Free Meeting
  <!-- Ícone: seta 45° em housing circular -->
  <span class="w-6 h-6 rounded-full bg-white flex items-center justify-center">
    <svg class="w-3 h-3 text-[#222] rotate-45" ...>↑</svg>
  </span>
</button>
```

### CTA secundário (pill)
```html
<button class="bg-white text-[#111] px-8 py-4 rounded-full flex items-center gap-3 text-lg font-medium">
  <span class="w-8 h-8 rounded-full bg-[#111] flex items-center justify-center">
    <!-- play icon -->
  </span>
  See Our Workreel
</button>
```

### Layout geral
```html
<section class="relative min-h-[90vh] flex flex-col overflow-hidden">
  <!-- Vídeo (z-0) -->
  <!-- Navbar (z-20, position absolute top) -->
  <!-- Conteúdo centralizado (z-10, flex-1 flex items-center justify-center) -->
</section>
```

---

## CHECKLIST ANTES DE ENTREGAR O CÓDIGO

- [ ] Vídeo tem `autoplay muted loop playsinline`?
- [ ] Nenhum overlay de cor sobre o vídeo?
- [ ] Fonte Instrument Serif carregada e aplicada na linha 2 do headline?
- [ ] Navbar com `rounded-[16px]` e shadow?
- [ ] CTA primário com ícone de seta 45°?
- [ ] CTA secundário em pill shape com play icon?
- [ ] `min-h-[90vh]` aplicado na section?
- [ ] Responsivo (mobile)?
- [ ] `z-index` correto (vídeo atrás, texto na frente)?

---

## EXEMPLO DE ADAPTAÇÃO POR NICHO

### Agência de vídeo / Logoisum (exemplo original)
- Headline 1: "Agency that makes your"
- Headline 2: "videos & reels viral"
- Subtext: "Short-form video editing for Influencers, Creators and Brands"
- CTA navbar: "Book A Free Meeting"
- CTA secundário: "See Our Workreel"

### SaaS
- Headline 1: "The platform that turns"
- Headline 2: "data into decisions"
- Subtext: "Business intelligence for teams that move fast"
- CTA navbar: "Start Free Trial"
- CTA secundário: "Watch Product Demo"

### E-commerce / Moda
- Headline 1: "Fashion that speaks"
- Headline 2: "before you say a word"
- Subtext: "Premium collections for the ones who set the standard"
- CTA navbar: "Shop Now"
- CTA secundário: "Watch Lookbook"
