---
name: guimkt-hero-videos
description: >
  Cria hero sections premium de websites e landing pages com vídeos no background — e, quando nenhum vídeo é fornecido, também gera o prompt de vídeo ideal para a seção. Use SEMPRE que o usuário pedir hero section com vídeo, hero section com videobg, landing page com vídeo de fundo, "seção hero cinematográfica", "hero com vídeo rodando atrás", "página com vídeo no background", "hero videobg", ou qualquer variação de hero + vídeo. Use também quando o usuário pedir apenas "crie o vídeo para o hero" ou "me dá o prompt de vídeo para o hero" sem fornecer URL — nesse caso ative apenas o módulo video-for-hero-pages. Os dois módulos desta skill funcionam juntos ou separados.
version: "1.0.0"
updated: "2026-03-17"
---

# HERO VIDEOS — Skill Completa

Esta skill tem dois módulos que se complementam:

| Módulo | O que faz | Quando usar |
|---|---|---|
| **hero-pages-videobg** | Gera o código HTML/CSS da hero section com vídeo no background | Sempre que a task for construir a hero section |
| **video-for-hero-pages** | Gera o prompt de vídeo ideal para ser usado no hero | Quando o usuário NÃO fornece uma URL de vídeo pronto |

---

## DECISÃO INICIAL — Leia isso primeiro

Antes de qualquer coisa, identifique o estado do input:

```
┌─ O usuário forneceu uma URL de vídeo? ──────────────────────────┐
│                                                                   │
│  SIM → Ir direto para [MÓDULO 1: hero-pages-videobg]             │
│                                                                   │
│  NÃO → Perguntar ao usuário:                                     │
│         "Você tem um vídeo pronto ou quer que eu gere            │
│          o prompt de vídeo ideal para o seu hero também?"        │
│                                                                   │
│         ├─ "Tenho o vídeo" → Pedir URL → [MÓDULO 1]             │
│         ├─ "Quero o prompt" → [MÓDULO 2] → depois [MÓDULO 1]   │
│         └─ "Só o código" → [MÓDULO 1] com {{VÍDEO_URL}}         │
│             como placeholder explícito                           │
└───────────────────────────────────────────────────────────────────┘
```

> **Regra de ouro:** Nunca assuma que o usuário quer os dois módulos, mas sempre ofereça o módulo de vídeo se ele não tiver um. A integração é opcional e inteligente.

---

## MÓDULO 1 — hero-pages-videobg

> Leia o arquivo completo em `references/hero-pages-videobg.md` antes de gerar qualquer código.

**Quando ativar:** o usuário quer construir a hero section (com ou sem vídeo definido).

**Input mínimo necessário:**
- Nome da marca/produto
- URL do vídeo (ou placeholder `{{VÍDEO_URL}}` se ainda não definida)

**Input opcional que melhora o output:**
- Paleta de cores
- Fonte preferida
- Links do menu
- Texto do headline
- CTAs

**Comportamento esperado:**
1. Ler `references/hero-pages-videobg.md`
2. Coletar os inputs necessários (via pergunta ou inferindo do contexto)
3. Gerar código HTML completo, funcional, responsivo
4. Entregar como artifact `.html` renderizável

---

## MÓDULO 2 — video-for-hero-pages

> Leia o arquivo completo em `references/video-for-hero-pages.md` antes de gerar qualquer prompt.

**Quando ativar:** o usuário não tem um vídeo pronto e quer criar um.

**Input mínimo necessário:**
- Nicho ou tipo de negócio (ex: "agência de vídeo", "SaaS B2B", "moda")

**Input opcional que melhora o output:**
- Paleta de cores da marca
- Mood/tom desejado
- Ferramenta de vídeo que vai usar (Runway, Sora, Kling, etc.)

**Comportamento esperado:**
1. Ler `references/video-for-hero-pages.md`
2. Identificar se há um nicho pré-definido nos exemplos do reference
3. Gerar o prompt completo com as 4 variáveis preenchidas
4. Incluir o checklist de validação pré-entrega
5. Após o prompt, perguntar: "Quer que eu já gere o código da hero section com o vídeo que você vai criar?"

---

## FLUXO COMBINADO (quando o usuário quer tudo)

Se o usuário pedir os dois módulos em sequência:

```
1. [MÓDULO 2] Gerar prompt de vídeo
   ↓
   "Aqui está o prompt. Depois de gerar o vídeo na ferramenta de
    sua escolha, me passe a URL e gero o código da hero section."
   ↓
2. [Usuário gera o vídeo externamente e retorna com a URL]
   ↓
3. [MÓDULO 1] Gerar código da hero section com a URL recebida
```

> **Não gere o código da hero section com URL fictícia** a não ser que o usuário explicitamente peça um placeholder.

---

## REFERÊNCIAS

- `references/hero-pages-videobg.md` — Especificações completas do código HTML da hero section
- `references/video-for-hero-pages.md` — Prompt completo para geração de vídeo + checklist + exemplos por nicho
