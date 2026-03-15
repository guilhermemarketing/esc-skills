# ESC Skills — Contexto do Projeto

> Este documento é a fonte de verdade para qualquer agente que trabalhe neste projeto.
> Leia-o por completo antes de executar qualquer tarefa.

---

## Identidade do Projeto

| Campo | Valor |
|-------|-------|
| **Nome** | ESC Skills |
| **Repositório** | [guilhermemarketing/esc-skills](https://github.com/guilhermemarketing/esc-skills) |
| **Site Live** | [gui.marketing/skills/](https://gui.marketing/skills/) |
| **Servidor** | Cloudways (nginx), IP `64.176.18.212` |
| **Dono** | Guilherme Lacerda — [gui.marketing](https://gui.marketing) |
| **Propósito** | Showcase público de 69+ AI agent skills para profissionais de marketing |

## Estrutura de Diretórios

```
esc-skills/
├── skills/                       # 69+ skills (cada um com SKILL.md)
│   ├── guimkt-*/                 # Skills customizadas gui.marketing
│   ├── skill-creator/
│   ├── ui-ux-pro-max/
│   └── ...
├── site/                         # Arquivos do website (source of truth)
│   ├── index.html                # Página completa (HTML + CSS + JS inline)
│   ├── skills-data.js            # AUTO-GERADO — NÃO editar manualmente
│   ├── skills-data-v5.js         # Versão cache-busted (Cloudflare CDN)
│   ├── build-data.js             # Script Node.js que gera skills-data.js
│   ├── esc-badge.png
│   ├── esc-key.png
│   ├── favicon.png
│   └── logo-guimarketing.gif
├── .agents/.skills/              # Skills do agente deste projeto
│   ├── esc-skills-showcase/      # Gestão do site (design, rebuild, i18n)
│   └── esc-skills-deploy/        # Deploy Cloudways + GitHub (GITIGNORED — contém credenciais)
├── README.md
├── install.sh
├── esc-skills-repo.md            # Workflow legado de gestão do repo
├── .gitignore
└── docs/                         # Memória e logs do projeto
    ├── contexto-projeto.md       # ESTE ARQUIVO
    ├── log-updates.md            # Log de atualizações
    └── bugs-aprendizados.md      # Bugs e aprendizados
```

## Branches do Git

| Branch | Conteúdo | Propósito |
|--------|----------|-----------|
| `main` | Skills, site/ (source), README, install.sh | Código-fonte |
| `gh-pages` | Apenas `index.html` de redirect | Redireciona `skills.gui.marketing` → `gui.marketing/skills/` |

> **O gh-pages NÃO hospeda mais o site.** Contém apenas um redirect. Não o modifique.

## Hosting e Deploy

O site é hospedado no **Cloudways** (servidor nginx compartilhado com o WordPress de `gui.marketing`).

- **Path no servidor:** `/home/1473804.cloudwaysapps.com/cjdzhnfmqs/public_html/skills/`
- **Deploy:** via `rsync` com `expect` script (password auth)
- **Credenciais:** na skill `.agents/.skills/esc-skills-deploy/SKILL.md` (gitignored)
- **WordPress coexistence:** o `/skills/` é um diretório estático servido pelo nginx ANTES do WordPress processar. Não criar página WordPress em `/skills/`

### Workflow completo de deploy

1. Fazer as edições em `site/`
2. Se skills mudaram: `cd site && node build-data.js`
3. `git add site/ && git commit -m "..." && git push origin main`
4. Ler e seguir a skill `esc-skills-deploy` para rsync ao Cloudways

## i18n (EN/PT-BR)

O site tem toggle de idioma EN/PT no navbar.

- **Toggle UI:** botões `EN | PT` no navbar com CSS `.lang-toggle`
- **Dicionário:** objeto `I18N` no JS do `index.html` (~50+ keys estáticos + 12 FAQ Q&As)
- **Skills:** campos `shortDescriptionPt` e `descriptionPt` em `skills-data.js`
- **Persistência:** `localStorage('esc-skills-lang')`
- **HTML lang:** atualizado para `en` ou `pt-BR`
- **Fallback:** se PT não existir, usa EN

### Ao adicionar texto novo ao site

1. Adicionar `data-i18n="chave_unica"` ao elemento HTML
2. Adicionar entrada no dicionário `I18N` com `{ en: '...', pt: '...' }`
3. Para FAQ: o updater usa `innerHTML` (não `textContent`) — suporta links HTML

## FAQ com Links para Pillar Content

5 das 12 perguntas do FAQ têm links contextuais para pillar content do gui.marketing:

| FAQ | Link |
|-----|------|
| Q1 (What are AI skills) | `/operacao-de-marketing-ia-first/` |
| Q2 (Prevent SLOP) | `/blog/copywriting-na-era-da-ia/` |
| Q4 (Global Rules) | `/playbook-de-copywriting/` |
| Q5 (Why adopt) | `/brandformance/` |
| Q9 (What tasks) | `/planejamento-marketing-digital/` |

Links traduzidos em EN e PT. CSS class: `.faq-link`.

## SEO

- **Canonical:** `<link rel="canonical" href="https://gui.marketing/skills/" />`
- **og:url:** `https://gui.marketing/skills/`
- **Title:** `ESC Skills — 69+ AI Agent Skills for Marketing Professionals`
- **FAQ rich snippets:** 12 perguntas com schema markup via classe `.faq-item`
- **Target keywords:** "AI Agent Marketing Skills", "marketing skills claude ia agents"
- **Redirect SEO:** `skills.gui.marketing` redireciona para `gui.marketing/skills/` (meta refresh + JS + canonical)

## Rebuild de Dados (skills-data.js)

Quando novas skills são adicionadas ou editadas em `skills/`:

```bash
cd site
node build-data.js
cp skills-data.js skills-data-v5.js   # cache-bust para Cloudflare
```

O script:
- Lê todos os `SKILL.md` de `../skills/`
- Extrai name/description do YAML frontmatter (suporta multiline `>`)
- Categoriza por prefixo do nome (regras em `CATEGORY_RULES`)
- Aplica extra categorias (regras em `EXTRA_CATEGORIES`) — multi-categoria
- Marca featured skills (lista em `FEATURED_SKILLS`)
- Preserva traduções EN/PT existentes do build anterior
- Gera `skills-data.js` com `SKILLS_DATA`, `CATEGORIES`, contadores

**NÃO editar `skills-data.js` manualmente** — sempre rodar `build-data.js`.

> **Cache-busting:** O Cloudflare CDN cacheia agressivamente. Sempre copiar
> para `skills-data-vN.js` (incrementar N) e atualizar a referência em `index.html`.
> Versão atual: **v5**.

## Customizações Comuns

### Featured Skills

Editar array `FEATURED_SKILLS` em `site/build-data.js`. Depois: `node build-data.js` + deploy.

### Multi-categoria (Extra Categories)

Editar `EXTRA_CATEGORIES` em `site/build-data.js`. Permite skills em múltiplas categorias.
O index.html filtra e exibe todas as tags no card footer.

### Categorias

16 categorias (mar/2026): Ads & PPC, Analytics & Tracking, Animation, Architecture, Cloud, Copywriting, CRO & LPO, Deploy, Design & UI, Development, DevOps & CI, Docs & Planning, Integrations, Performance, Security, SEO.

Editar `CATEGORY_RULES` em `site/build-data.js`. Rules avaliadas em ordem — primeira match ganha.

### Design

Tudo inline no `index.html`. CSS variables:
- `--accent: #ff6b35` (ESC orange)
- `--bg: #000000`, `--bg-card: #111111`
- `--font-mono: 'JetBrains Mono'`, `--font-sans: 'Inter'`

## Relação com gui-toolbox

O projeto `gui-toolbox` é o workspace principal do Guilherme. Ele **não** gerencia mais o ESC Skills.

- Skills do gui-toolbox ficam em `/Users/guilhacerda/Documents/Antigravity Macbook/gui-toolbox/.agent/skills/`
- Skills do ESC Skills ficam em `skills/` (as 69+ do showcase) + `.agents/.skills/` (skills do agente)
- Ao criar skills novas, perguntar ao usuário se vai para gui-toolbox, esc-skills, ou ambos
- O workflow antigo `esc-skills-repo.md` na raiz é legado — usar as skills em `.agents/.skills/`

## Convenções

- **Prefixo de skills:** Skills customizadas do gui.marketing usam prefixo `guimkt-`
- **Commits:** Conventional Commits (`feat:`, `fix:`, `chore:`, `seo:`, `security:`)
- **Deploy:** sempre commitar no `main` antes de rsync para Cloudways
- **Testar local:** `cd site && python3 -m http.server 8765`
- **Dados sensíveis:** nunca commitar credenciais SSH — usar `.gitignore`
