---
name: feedback-interpreter
description: >
  Interpreta e aplica feedbacks exportados do Feedback Studio (arquivo .md) em landing pages, wireframes e criativos.
  Use quando receber um arquivo .md de feedbacks com seletores CSS e posições, ou quando o usuário mencionar
  "aplicar feedbacks", "ajustar landing page com feedbacks", "feedback studio", "feedbacks exportados",
  "arquivo de revisões", ou "aplicar revisões da landing page".
---

# Feedback Interpreter

Você recebeu um arquivo `.md` exportado do **Feedback Studio** — uma ferramenta de revisão colaborativa onde clientes e equipes deixam comentários visuais diretamente sobre landing pages, wireframes e criativos de mídia paga.

## O que é o Feedback Studio

É um painel web onde:

1. Um projeto (landing page, wireframe ou display ad) é carregado dentro de um iframe
2. Revisores clicam em elementos da página para deixar comentários visuais
3. Cada comentário é ancorado a um **elemento HTML específico** via CSS selector
4. O sistema registra a posição exata (x/y em %) onde o clique foi feito dentro do elemento

## Formato do Arquivo de Feedbacks

O `.md` exportado segue esta estrutura:

```markdown
# Feedback Report — [Nome do Projeto]

> **Exported:** [ISO timestamp]
> **Open comments:** [N]
> **Project URL:** [URL da página alvo ou "Upload HTML"]
> **Project Type:** Landing Page | Wireframe | Display Ad

---

## Comment #N

| Field | Value |
|-------|-------|
| **Author** | Nome |
| **Date** | 2026-03-03 |
| **Status** | 🔴 Open |
| **Element Selector** | `div > section:nth-of-type(2) > h2` |
| **Position** | x: 45.2%, y: 12.8% |
| **Type** | text |

> Conteúdo do feedback aqui

### Replies

#### Reply #N.1 — Author (date)
> Resposta ao feedback
```

## Como interpretar cada campo

### Element Selector

CSS selector que identifica **exatamente** qual elemento HTML o revisor clicou. O formato é um caminho DOM completo:

```
html > body > div > section:nth-of-type(2) > div > h2
```

- Usa `tagname:nth-of-type(n)` quando há irmãos do mesmo tipo
- Usa `tagname#id` como atalho quando o elemento tem ID
- O path usa ` > ` (child combinator) — é **preciso e determinístico**

**Para localizar o elemento no HTML:** use o selector como path de navegação pelo DOM, ou busque com `document.querySelector(selector)`.

### Position (x, y)

Porcentagem relativa dentro do elemento selecionado. Indica **onde** no elemento o clique foi feito:

- `x: 0%` = borda esquerda, `x: 100%` = borda direita
- `y: 0%` = topo, `y: 100%` = base

Útil para saber se o feedback é sobre o lado esquerdo/direito de uma imagem, o início/fim de um texto, etc.

### Type

- `text` — comentário de texto puro
- `image` — feedback com imagem anexa (screenshot, referência visual)
- `audio` / `video` — mídia anexa (raro)

### Replies

Respostas ao comentário original. Frequentemente contêm esclarecimentos, contra-propostas ou confirmações do cliente. **Leia as replies — elas podem alterar ou refinar o que o comentário original pede.**

## Workflow para aplicar feedbacks

### 1. Ler o relatório completo primeiro

Antes de editar qualquer arquivo, leia **todos** os feedbacks para entender:

- O escopo total das mudanças
- Se há feedbacks contraditórios (priorize os mais recentes ou com replies de confirmação)
- Se há dependências entre feedbacks (ex: "mude o título" + "ajuste o espaçamento do título")

### 2. Localizar o arquivo HTML alvo

- O campo **Project URL** indica qual página recebeu os feedbacks
- Se diz "Upload HTML", o HTML foi carregado diretamente — busque o arquivo no workspace

### 3. Para cada feedback, na ordem

```
Para cada Comment:
  1. Leia o Element Selector → localize o elemento no HTML
  2. Leia a Position → entenda a área específica dentro do elemento
  3. Leia o Content + Replies → entenda O QUE precisa mudar
  4. Faça a alteração no código
```

### 4. Tipos comuns de ajustes

| Feedback diz... | Ação provável |
|-----------------|---------------|
| "Texto fraco", "reescrever", "copywriting" | Alterar conteúdo textual do elemento |
| "Cor estranha", "contraste", "destaque" | Ajustar CSS (color, background, opacity) |
| "Muito grande", "muito pequeno" | Ajustar font-size, padding, margin, width |
| "Mover para cima/baixo" | Reordenar elementos no DOM ou ajustar flex-order |
| "Remover", "tirar isso" | Deletar o elemento ou aplicar `display: none` |
| "Adicionar CTA", "botão aqui" | Criar novo elemento HTML |
| "Imagem não combina" | Substituir src da imagem |
| "Link quebrado" | Corrigir href |
| "Mobile quebrado" | Ajustar media queries ou responsive CSS |

### 5. Após aplicar todos os feedbacks

- Verifique se a página ainda renderiza corretamente
- Rode um build se aplicável
- Resuma as alterações feitas, referenciando os Comment # originais

## Particularidades por tipo de projeto

### Landing Page / Wireframe

- Os selectors apontam para elementos dentro do HTML da página
- Feedbacks podem ser sobre copy, layout, CTA, imagens, formulários, SEO

### Display Ad / Meta Ad

- O selector será `creative-image` (valor fixo) — significa que o feedback é sobre a imagem do criativo
- O campo **Position** indica onde na imagem o clique foi feito
- O campo **Creative** indica qual criativo (se houver múltiplos) e o formato (single/carousel)
- O campo **Card Index** indica qual card do carrossel

## Exemplo prático

Dado este feedback:

```
## Comment #3
| **Element Selector** | `html > body > div > section:nth-of-type(2) > div > h2` |
| **Position** | x: 50.0%, y: 50.0% |

> O título da seção 2 está genérico. Sugerir algo mais impactante com prova social.
```

**Ação:** Abra o HTML, encontre o `<h2>` dentro da segunda `<section>`, e reescreva o texto com uma headline que inclua prova social (números, depoimentos, resultados).
