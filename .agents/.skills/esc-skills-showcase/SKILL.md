---
name: esc-skills-showcase
description: >
  Gerencia o showcase website do ESC Skills em https://gui.marketing/skills/.
  Cobre rebuild de dados, ajustes de design/UX no index.html, adição de novas categories,
  customização de featured skills, troubleshooting do build-data.js, e otimização de
  performance/SEO da página. Use esta skill sempre que o usuário mencionar "showcase de skills",
  "site das skills", "gui.marketing/skills", "atualizar o showcase", "rebuild skills data",
  "ajustar site das skills", "adicionar skill ao showcase", "otimizar página das skills",
  ou qualquer variação de gestão e manutenção do website showcase do repositório esc-skills.
  Também use quando o usuário pedir para adicionar novas categories, alterar o design,
  corrigir bugs no site, ou fazer qualquer mudança que afete o site publicado.
  Para DEPLOY, use a skill `esc-skills-deploy` que contém credenciais e workflow de rsync.
---

# ESC Skills Showcase Manager

Skill para gerenciar o website showcase do ESC Skills.

**Live URL:** https://gui.marketing/skills/
**Repositório:** https://github.com/guilhermemarketing/esc-skills
**Diretório do site:** `site/`

## Arquitetura do Projeto

```
esc-skills/
├── skills/                  # 69+ skills (cada uma com SKILL.md)
├── site/
│   ├── build-data.js        # Script Node.js de extração de dados
│   ├── skills-data.js       # Gerado automaticamente (NÃO editar manualmente)
│   ├── index.html           # Página completa (HTML + CSS + JS inline)
│   ├── esc-badge.png        # Badge ESC
│   ├── esc-key.png          # ESC key image
│   ├── favicon.png          # Favicon
│   └── logo-guimarketing.gif # Logo
├── .agents/.skills/
│   ├── esc-skills-deploy/   # Skill de deploy (gitignored, contém credenciais)
│   └── esc-skills-showcase/ # Esta skill
├── README.md
└── install.sh
```

### Hosting

| Item | Detalhes |
|------|----------|
| Servidor | Cloudways (nginx), deploy via rsync |
| URL | https://gui.marketing/skills/ |
| Redirect | skills.gui.marketing → gui.marketing/skills/ (via gh-pages) |
| GitHub | Branch `main` = código fonte. Branch `gh-pages` = apenas redirect |

> [!IMPORTANT]
> O site NÃO usa mais GitHub Pages para hosting. O deploy é feito via rsync para Cloudways.
> A branch `gh-pages` contém apenas uma página de redirect para `gui.marketing/skills/`.
> Para deploy, use a skill `esc-skills-deploy`.

## Workflows Essenciais

### 1. Rebuild de Dados (após adicionar/editar skills)

Quando novas skills são adicionadas ou editadas no `skills/`:

```bash
cd site
node build-data.js
```

O script:
- Lê TODOS os `SKILL.md` de `../skills/`
- Extrai name/description do YAML frontmatter (suporta multiline `>`)
- Categoriza automaticamente por prefixo do nome
- Marca featured skills (lista hardcoded em `FEATURED_SKILLS`)
- Gera `skills-data.js` com array `SKILLS_DATA`, `CATEGORIES`, contadores

### 2. Deploy

Use a skill `esc-skills-deploy` para o deploy completo. Resumo:

1. `git add site/ && git commit && git push origin main`
2. `expect /tmp/rsync-deploy.exp` (rsync para Cloudways)

### 3. Testar Local

```bash
cd site
python3 -m http.server 8765
# Abrir http://localhost:8765
```

## i18n (EN/PT-BR)

O site tem toggle de idioma EN/PT no navbar.

- **Texto estático**: traduzido via dicionário `I18N` no JS do `index.html`
- **Skills**: campos `shortDescriptionPt` e `descriptionPt` em `skills-data.js`
- **FAQ**: 12 Q&As traduzidas, incluindo links contextuais para pillar content
- **Persistência**: `localStorage('esc-skills-lang')`
- **HTML lang**: atualizado para `en` ou `pt-BR`

## Customizações Comuns

### Adicionar/Remover Featured Skills

Editar array `FEATURED_SKILLS` em `site/build-data.js`:

```javascript
const FEATURED_SKILLS = [
  'guimkt-classic-ad-creative', 'guimkt-classic-ad-creative-final',
  'guimkt-design-system-extractor', 'guimkt-google-ads',
  'guimkt-gtm-expert', 'guimkt-gtm-expert-template', 'guimkt-landing-page',
  'guimkt-landing-page-optimization', 'guimkt-make-blueprint-expert', 'guimkt-meta-ads',
  'skill-creator', 'ui-ux-pro-max', 'guimkt-wireframe-landing-page'
];
```

Depois: `node build-data.js` + deploy.

### Multi-categoria (Extra Categories)

Skills podem pertencer a múltiplas categorias via `EXTRA_CATEGORIES` em `site/build-data.js`:

```javascript
const EXTRA_CATEGORIES = {
  'guimkt-design-system-extractor': [
    { id: 'design', label: '🎨 Design & UI', icon: '🎨' }
  ],
  'guimkt-meta-ads': [
    { id: 'ads', label: '📣 Ads & PPC', icon: '📣' },
    { id: 'copywriting', label: '✍️ Copywriting', icon: '✍️' },
    { id: 'design', label: '🎨 Design', icon: '🎨' }
  ]
};
```

O build gera `extraCategories` no JSON, e o index.html filtra e exibe todas.

> [!NOTE]
> O build preserva automaticamente traduções EN/PT existentes do `skills-data.js` anterior.

### Adicionar Nova Categoria

Editar array `CATEGORY_RULES` em `site/build-data.js`:

```javascript
{ id: 'new-cat', label: '🔥 New Category', icon: '🔥',
  match: (name, desc) => name.startsWith('prefix-') }
```

Rules avaliadas em ordem — primeira que der match ganha. Sem match → "📦 Other".

### Alterar Design/Layout

O `index.html` contém tudo inline. Cores principais em CSS variables:

- `--accent: #ff6b35` (ESC orange)
- `--bg: #000000`, `--bg-card: #111111`
- `--font-mono: 'JetBrains Mono'`, `--font-sans: 'Inter'`

## Troubleshooting

### Descrições mostrando ">" nos cards

Parser YAML em `build-data.js` usa parsing line-by-line para multiline `>` descriptions. Verificar `parseFrontmatter()`.

### Skills não aparecendo

1. Verificar se a skill tem `SKILL.md` com frontmatter YAML (`---` delimiters)
2. Rodar `node build-data.js` e checar output
3. Verificar `skills-data.js`

### FAQ links não renderizando

O FAQ updater usa `innerHTML` (não `textContent`) para suportar links HTML nos answers. Se links sumirem, verificar a função `setLanguage()` no JS.

## Boas Práticas

1. **Sempre rebuild antes de deploy** — `node build-data.js`
2. **Testar local primeiro** — `python3 -m http.server 8765` no dir `site/`
3. **Não editar skills-data.js manualmente** — auto-gerado
4. **Commitar no main** — source fica no `main`, deploy via rsync
5. **Manter FEATURED_SKILLS atualizado** — ao publicar skills novas
6. **Verificar SEO** — canonical tag, og:url, meta tags apontam para `gui.marketing/skills/`
7. **Manter i18n** — atualizar dicionário `I18N` ao adicionar/editar texto estático
