---
description: Pipeline independente para gerar 10 conceitos criativos de performance para Meta Ads (Facebook/Instagram). Aciona a skill guimkt-meta-ads v3.1 com framework Hook → Hold → Offer. Funciona standalone — não depende do /esc-start.
---

# /esc-meta-ads-creatives — Meta Ads Performance Creatives

> Pipeline standalone que delega para `guimkt-meta-ads` v3.1. Este workflow apenas **coleta requisitos e orquestra** — toda a lógica criativa está na skill.

---

## Passo 1 — Coletar Requisitos

Perguntar ao usuário:

> "Para gerar os 10 conceitos criativos de Meta Ads, preciso dos seguintes itens:
>
> **Obrigatórios:**
> 1. **Nome do cliente** (slug para nomear arquivos, ex: `WTECH`)
> 2. **Briefing** — pode ser texto livre, documento .md, URL do site, ou dados estruturados (produto, público, dor, diferencial, prova, tom de voz, objetivo, restrições)
> 3. **Oferta** — tipo (desconto, bundle, garantia, trial, etc.), detalhe e urgência
>
> **Para o Design System** (escolha uma opção):
> - ✅ `design-system-{{CLIENTE}}.md` já existe → indicar o caminho
> - 📁 **Pasta com imagens de referência** da identidade visual (site, materiais, redes sociais) — mín. 3-5 imagens → vou extrair o design system automaticamente
>
> **Para geração de imagens** (se quiser criativos visuais):
> - 📁 **Pasta com logotipo** do cliente (PNG/SVG com fundo transparente)
>
> **Opcionais (enriquecem o resultado):**
> - `icp-consolidado-{{CLIENTE}}.md`
> - `message-mining-{{CLIENTE}}.md`"

**PARAR e aguardar** todos os itens obrigatórios antes de prosseguir.

---

## Passo 2 — Preparar Estrutura

Criar a pasta de entregas se não existir:

```
entregas/{{CLIENTE}}/05-criativos-meta/
├── referencias-visuais/    ← copiar imagens de referência aqui
├── logos/                  ← copiar logos aqui (se fornecidos)
├── design-system-{{CLIENTE}}.md    ← gerado ou pré-existente
├── conceitos-meta-{{CLIENTE}}.md   ← output principal
└── prompts-imagens-{{CLIENTE}}.md  ← prompts consolidados
```

Se o usuário forneceu pasta de referências visuais, copiar imagens para `referencias-visuais/`.

---

## Passo 3 — Executar a Skill

Ler e seguir **integralmente** a skill `guimkt-meta-ads` (Etapas 0 → 6), que contém:

- **Etapa 0:** Design System (extrair de referências ou ler existente)
- **Etapa 1:** Diagnóstico do Briefing + Customer Avatar
- **Etapa 2:** Customer Journey Mapping
- **Etapa 3:** Gerar 10 Conceitos
- **Etapa 4:** Desenvolver cada conceito (Hook → Hold → Offer)
- **Etapa 5:** Checklist de Validação
- **Etapa 6:** Arquivo de Prompts de Imagem

> A skill governa 100% da lógica criativa. Não inventar etapas adicionais.

---

## Passo 4 — Criativos Visuais (Sob Demanda)

Se o usuário solicitou geração de imagens:

1. Usar `generate_image` com prompts do arquivo `prompts-imagens-{{CLIENTE}}.md`
2. Aspect ratio padrão: **4:5** (1080×1350px)
3. Cada imagem = anúncio completo com headline, descrição e CTA integrados
4. Respeitar design system
5. 1 imagem por conceito

---

## Passo 5 — Output HTML (Sob Demanda)

Se o usuário pedir apresentação HTML:

1. Usar template `references/conceitos-meta-template.html`
2. Substituir placeholders `{{CLIENTE}}`, `{{DATA}}`, `{{MARCA_1}}`
3. Links UTM: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-meta-ads`

---

## Deliverables

| Arquivo | Obrigatório |
|---------|-------------|
| `conceitos-meta-{{CLIENTE}}.md` | ✅ Sempre |
| `prompts-imagens-{{CLIENTE}}.md` | ✅ Sempre |
| `design-system-{{CLIENTE}}.md` | ✅ Sempre (extraído ou pré-existente) |
| `conceitos-meta-{{CLIENTE}}.html` | ❌ Sob demanda |
| Imagens geradas (4:5) | ❌ Sob demanda |

---

## Notas

1. **Standalone** — funciona sem `/esc-start`, `/esc-cro` ou qualquer outro pipeline
2. Se `icp-consolidado-{{CLIENTE}}.md` existir, a skill o usa automaticamente
3. Para criativos **multi-plataforma** (Google, LinkedIn, TikTok), usar `guimkt-classic-advertising-creative` após este workflow
4. Se o usuário pedir menos de 10 conceitos, ajustar proporcionalmente mantendo distribuição Cold/Warm/Hot
