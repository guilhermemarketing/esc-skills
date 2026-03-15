# Log de Atualizações — ESC Skills

## 2026-03-15 — Recategorização geral + Multi-categoria

### Mudanças
- **Eliminada** a categoria genérica "Marketing" — todas as skills do repo são de marketing, então era redundante
- **Novas categorias:** 📣 Ads & PPC, 📈 Analytics & Tracking, 🎯 CRO & LPO, 🔍 SEO, ✍️ Copywriting
- **Sistema multi-categoria** adicionado via `EXTRA_CATEGORIES` em `build-data.js`
- **Redistribuição** de 12 skills ex-Marketing para categorias específicas:
  - `guimkt-classic-ad-creative-final`, `guimkt-google-ads`, `guimkt-meta-ads` → Ads & PPC
  - `guimkt-gtm-expert`, `guimkt-gtm-expert-template` → Analytics & Tracking
  - `guimkt-landing-page`, `guimkt-landing-page-optimization`, `guimkt-wireframe-landing-page`, `pricing-page` → CRO & LPO
  - `guimkt-design-system-extractor` → Design & UI
  - `guimkt-make-blueprint-expert` → Integrations
  - `seo` → SEO
- **`guimkt-classic-ad-creative-final`** adicionada como skill Featured + renomeada no `gui-marketing-skills` repo
- **Preservação de traduções** — build-data.js agora preserva EN/PT overrides entre rebuilds
- **UX:** botões de categorias em flex-wrap (sem scroll horizontal)
- **Cache-busting:** renomeado `skills-data.js` para `skills-data-v5.js` (Cloudflare CDN)

### Arquivos alterados
- `site/build-data.js` — CATEGORY_RULES, EXTRA_CATEGORIES, FEATURED_SKILLS, merge de traduções
- `site/index.html` — filtro multi-categoria, flex-wrap, script src v5
- `site/skills-data-v5.js` — dados regenerados
- `.agents/.skills/esc-skills-showcase/SKILL.md` — docs atualizados
- `gui-marketing-skills` repo: `guimkt-classic-ad-creative/SKILL.MD` — name corrigido

## 2026-03-15 — Correções de UX do site

### Mudanças
- **Idioma toggle:** corrigido bug onde Featured Skills desapareciam ao alternar idioma
- **Descrições PT/EN:** garantido que todas as key strings respeitam o idioma selecionado
- **Animações:** removida reinicialização de animações ao trocar idioma
- **Hero CLI snippet:** corrigido overflow no mobile
- **Botão Copy:** fundo roxo sólido + texto/contornos brancos
