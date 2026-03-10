---
name: guimkt-design-system-extractor
description: Extrai design systems completos de websites para gerar arquivos .md que guiam agentes na criação de páginas com a identidade visual do site analisado. Captura cores, tipografia, componentes (botões, cards, navbar, footer), assets (logos, imagens de produto), layout/grid, animações, anti-patterns e gera CSS variables prontos para uso. Use quando o usuário pedir para "extrair design system", "criar design system de um site", "analisar identidade visual", "capturar estilo de um site", "design tokens de um site", "gerar guia visual de marca", ou qualquer variação de análise visual de website para replicação de identidade.
---

# Design System Extractor

Extrai design systems de websites e gera documentação Markdown pronta para guiar agentes na criação de páginas fiéis à identidade visual original.

## Output

- Arquivo `{marca}-design-system.md` no diretório `design-systems/`
- Pasta `{marca}-refs/` com screenshots de referência
- Design tokens, componentes CSS, assets URLs e checklist de implementação

## Workflow

### Fase 1: Acesso e Captura Visual

1. **Navegar ao site** via browser subagent
2. **Aceitar cookies/banners** para view limpo
3. **Capturar screenshots** das seções-chave (mínimo 6):

| Screenshot | O que capturar |
|---|---|
| Hero | Primeira dobra, headline, CTA principal |
| Header / Nav | Logo, menu items, estilo do menu |
| Produtos / Features | Grid ou carrossel de produtos/features |
| Conteúdo / Stories | Seção de artigos, blog, cases |
| CTA / Social Proof | Seções de conversão, depoimentos, parceiros |
| Footer | Links, copyright, layout do rodapé |

### Fase 2: Extração de Tokens via JavaScript

Executar no browser subagent para capturar tokens reais:

```javascript
// Extrair cores, tipografia e estilos computados
(function() {
    const body = document.body;
    const h1 = document.querySelector('h1');
    const btn = document.querySelector('button, [class*="btn"], [class*="cta"], a[class*="button"]');
    const card = document.querySelector('[class*="card"], [class*="Card"]');
    const nav = document.querySelector('nav, header');
    const footer = document.querySelector('footer');

    const getStyle = (el, props) => {
        if (!el) return null;
        const cs = getComputedStyle(el);
        const result = {};
        props.forEach(p => result[p] = cs.getPropertyValue(p));
        return result;
    };

    return JSON.stringify({
        body: getStyle(body, ['background-color', 'color', 'font-family', 'font-size', 'line-height']),
        h1: getStyle(h1, ['font-family', 'font-size', 'font-weight', 'color', 'letter-spacing', 'line-height']),
        button: getStyle(btn, ['background-color', 'color', 'border-radius', 'padding', 'font-family', 'font-size', 'font-weight', 'border']),
        card: getStyle(card, ['background-color', 'border-radius', 'box-shadow', 'padding']),
        nav: getStyle(nav, ['background-color', 'height', 'position']),
        footer: getStyle(footer, ['background-color', 'color', 'padding'])
    }, null, 2);
})();
```

### Fase 3: Extração de Assets

Executar no browser para capturar URLs de imagens e logos:

```javascript
// Extrair logo do header
(function() {
    const header = document.querySelector('header, nav');
    if (!header) return 'No header found';
    const imgs = header.querySelectorAll('img');
    const result = [];
    imgs.forEach(img => {
        result.push({ src: img.src, alt: img.alt, width: img.width, height: img.height });
    });
    return JSON.stringify(result, null, 2);
})();
```

```javascript
// Extrair todas as imagens notáveis (produtos, backgrounds, icons)
(function() {
    const all = [];
    document.querySelectorAll('img').forEach(img => {
        const src = img.src || img.currentSrc || '';
        if (src && src.startsWith('http')) {
            all.push({ src: src.split('?')[0], alt: img.alt || '' });
        }
    });
    return JSON.stringify([...new Map(all.map(i => [i.src, i])).values()], null, 2);
})();
```

### Fase 4: Organizar Arquivos

1. Criar diretório: `design-systems/{marca}-refs/`
2. Copiar screenshots para a pasta de refs
3. Referenciar imagens com paths relativos no markdown (`{marca}-refs/screenshot.png`)

### Fase 5: Escrever o Design System .md

Usar a estrutura abaixo. Todas as seções são obrigatórias exceto onde indicado.

## Estrutura do Arquivo .md

```markdown
# {Marca} Design System

> Design system extraído de [{url}]({url}) para guiar agentes na criação de páginas com a identidade visual {marca}.

## 1. Identidade Visual — Visão Geral
- Descrição da estética (3-4 linhas)
- Palavras-chave da estética
- Princípios de design (3-5 items)

## 1.1 Logo
- URL oficial (preferencialmente SVG)
- Variantes e uso
- Código HTML de exemplo

## 2. Paleta de Cores
### Cores Primárias (tabela com Token | Valor | Hex | Uso)
### Cores de Suporte (tabela)
### Cores de Produto/Contexto (se aplicável)

## 3. Tipografia
### Font Families (tabela com Token | Família | Peso | Uso)
### Escala Tipográfica (tabela H1→small com tamanhos e pesos)
### Regras de Tipografia (CSS snippet)
> Incluir fonts proprietárias + fallbacks de Google Fonts

## 4. Componentes
### 4.1 Botões (primary, secondary, ghost — com CSS completo)
### 4.2 Cards (todos os tipos encontrados — com CSS completo)
### 4.3 Navegação (header/navbar — com CSS)
### 4.4 Footer (com CSS)
> Cada componente: CSS snippet completo com hover states e transitions

## 5. Layout e Grid
- Tabela de seções com layout e colunas
- Container CSS
- Breakpoints responsivos (tabela)

## 6. Efeitos e Animações
- Hover effects
- Transições
- Scroll effects (se houver)

## 7. Anti-patterns — O que NÃO fazer (tabela ❌ vs ✅)

## 8. Assets — URLs Oficiais
### 8.1 Logo e Branding (tabela)
### 8.2 Produtos / Imagens-chave (tabela com URLs diretas)
### 8.3 Backgrounds / Ilustrações (se aplicável)
> Documentar parâmetros de redimensionamento da CDN quando houver

## 9. Referências Visuais
- Screenshots embeddados: ![descrição]({marca}-refs/screenshot.png)

## 10. CSS Variables — Resumo Rápido
- Bloco :root{} com TODAS as variáveis definidas

## 11. Checklist para Landing Pages
- Lista de verificação com [ ] items
```

## Regras Críticas

1. **Sempre use URLs originais** — nunca baixe e re-hoste assets. Documente a URL oficial do site
2. **CSS completo** — cada componente deve ter CSS copiável e funcional, incluindo `:hover`
3. **Fallback fonts** — sempre indique alternativas do Google Fonts para fontes proprietárias
4. **Mínimo 6 screenshots** — cubra todas as seções principais do site
5. **Tokens nomeados** — use convenção `--{marca}-{propriedade}` (ex: `--rb-red`, `--cw-navy`)
6. **Anti-patterns** — sempre inclua o que NÃO fazer, baseado nos padrões observados
7. **Redimensionamento** — documente parâmetros de CDN (Cloudinary, Imgix, etc.) quando encontrados
8. **Todas as variantes de botão** — capturar primary, secondary, ghost/outline no mínimo
9. **Cores de produto** — se o site tem variantes (sabores, planos, etc.), documentar cada cor
10. **Checklist final** — sempre terminar com checklist actionable para landing pages

## Exemplos Existentes

Consultar como referência de formato e profundidade:

- `design-systems/redbull-design-system.md` — exemplo com produtos, cores de sabor, fontes proprietárias
- `design-systems/cloudways-design-system.md` — exemplo SaaS com estética enterprise

## Trigger Phrases

- "extrair design system de {url}"
- "criar design system do site {url}"
- "analisar identidade visual de {url}"
- "capturar estilo visual de {url}"
- "design system de {marca}"
- "gerar guia visual baseado em {url}"
