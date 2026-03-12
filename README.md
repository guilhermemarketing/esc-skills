# 🧠 ESC Skills

Coleção de skills para agentes AI (Gemini, Claude Code, Cursor, Windsurf, Cline, etc.) focadas em **desenvolvimento web, DevOps, design, SEO, performance, segurança e arquitetura**.

## 📦 Skills Disponíveis

| Skill | Descrição |
|-------|-----------|
| **3d-web-experience** | Three.js, React Three Fiber, Spline, WebGL — experiências 3D para web |
| **accessibility** | Audit e melhoria de acessibilidade WCAG 2.1 |
| **animation-systems** | Motion product-grade estilo Stripe, Linear, Apple, Vercel |
| **animejs** | Anime.js v4 — timelines, SVG, scroll, draggable, stagger |
| **aws-advisor** | Consultoria AWS — arquitetura, segurança, implementação |
| **best-practices** | Boas práticas de segurança, compatibilidade e qualidade de código |
| **cloudflare-deploy** | Deploy em Cloudflare Workers, Pages e serviços |
| **coding-guidelines** | Guidelines comportamentais para reduzir erros comuns de LLMs |
| **component-common-domain-detection** | Detecta funcionalidade duplicada entre componentes |
| **component-flattening-analysis** | Identifica e corrige hierarquias de componentes |
| **component-identification-sizing** | Identifica componentes e calcula métricas de tamanho |
| **confluence-assistant** | Operações Confluence via Atlassian MCP |
| **core-web-vitals** | Otimização de Core Web Vitals (LCP, INP, CLS) |
| **css-border-gradient** | Gradient borders CSS com pseudo-element mask |
| **cursor-subagent-creator** | Cria subagents para Cursor editor (.cursor/agents/) |
| **decomposition-planning-roadmap** | Plans e roadmaps de decomposição de monolitos |
| **docs-writer** | Escrita e revisão de documentação (.md) |
| **domain-analysis** | Identifica subdomínios e bounded contexts (DDD Strategic Design) |
| **domain-identification-grouping** | Agrupa componentes em domínios lógicos |
| **feedback-interpreter** | Interpreta e aplica feedbacks exportados do Feedback Studio |
| **figma** | Integração com Figma MCP — design context, screenshots, assets |
| **figma-implement-design** | Traduz nodes Figma em código production-ready (1:1 fidelity) |
| **frontend-design** | Interfaces frontend distintas e production-grade |
| **frontend-ui-ux** | Designer-turned-developer — stunning UI/UX sem mockups |
| **gh-address-comments** | Endereça review/issue comments em PRs do GitHub |
| **gh-fix-ci** | Debug e fix de checks de CI falhando no GitHub Actions |
| **gsap** | GSAP — timelines, ScrollTrigger, stagger, transforms |
| **guimkt-gtm-expert** | Criar, editar, validar containers GTM JSON |
| **guimkt-gtm-expert-template** | Template GTM Leads 2025 para novos clientes |
| **guimkt-classic-ad-creative** | Conceitos criativos para Meta Ads e Google Ads |
| **guimkt-design-system-extractor** | Extrai design systems completos de websites |
| **guimkt-landing-page-optimization** | Landing Page Optimization (LPO) — análise, auditoria, criação, copy, frameworks de copywriting, fórmula de conversão |
| **interaction-design** | Microinterações, motion design, transições |
| **javascript-typescript** | JS/TS com ES6+, Node.js, React, frameworks modernos |
| **jira-assistant** | Operações Jira via Atlassian MCP |
| **guimkt-make-blueprint-expert** | Criar, editar, debugar e otimizar blueprints Make.com via JSON. HTTP modules, routers, roleta, Facebook Lead Ads |
| **matterjs** | Matter.js — física 2D, Engine/World, bodies e constraints |
| **netlify-deploy** | Deploy em Netlify via CLI |
| **nx-ci-monitor** | Monitor Nx Cloud CI com self-healing |
| **nx-generate** | Gerar código com Nx generators |
| **nx-run-tasks** | Rodar tasks em workspaces Nx |
| **nx-workspace** | Configurar e otimizar monorepos Nx |
| **perf-astro** | Performance Astro para 95+ Lighthouse |
| **perf-lighthouse** | Rodar audits Lighthouse via CLI/Node |
| **perf-web-optimization** | Otimização web — Core Web Vitals, bundle, imagens, cache |
| **playwright-skill** | Automação de browser com Playwright |
| **pricing-page** | Design de pricing pages SaaS de alta conversão |
| **progressive-blur** | Progressive blur CSS com backdrop-filter layers |
| **render-deploy** | Deploy em Render com render.yaml Blueprints |
| **responsive-design** | Layouts responsivos — container queries, fluid typography, CSS Grid |
| **run-nx-generator** | Rodar Nx generators com priorização de plugins |
| **security-best-practices** | Reviews de segurança por linguagem/framework |
| **security-ownership-map** | Topologia de ownership por segurança via git history |
| **security-threat-model** | Threat modeling grounded em repositório |
| **sentry** | Inspecionar issues e eventos Sentry via API |
| **seo** | Otimização SEO — meta tags, structured data, sitemap |
| **skill-creator** | Guia para criar skills AI (SKILL.md format) |
| **subagent-creator** | Guia para criar subagents com contexto isolado |
| **technical-design-doc-creator** | Criar Technical Design Documents (TDD) |
| **threejs-animation** | Three.js animation — keyframes, skeletal, morph targets |
| **tlc-spec-driven** | Planejamento de projeto em 4 fases: Specify, Design, Tasks, Implement |
| **ui-ux-pro-max** | UI/UX intelligence — 50 estilos, 21 paletas, 9 stacks |
| **vantajs** | Vanta.js — backgrounds WebGL animados |
| **vercel-deploy** | Deploy em Vercel |
| **web-quality-audit** | Audit completo de qualidade web (performance, a11y, SEO) |

## 🚀 Instalação

### Opção 1: Script rápido (recomendado)

```bash
curl -sL https://raw.githubusercontent.com/guilhermemarketing/esc-skills/main/install.sh | bash
```

### Opção 2: Git Submodule

```bash
# Adicionar como submodule (mantém sincronizado)
git submodule add https://github.com/guilhermemarketing/esc-skills.git .agent/external-skills

# Atualizar no futuro
git submodule update --remote
```

### Opção 3: Clone manual

```bash
git clone https://github.com/guilhermemarketing/esc-skills.git /tmp/esc-skills
cp -r /tmp/esc-skills/skills/* .agent/skills/
rm -rf /tmp/esc-skills
```

## 🤖 Configuração para Agentes AI

Adicione ao `.instructions` ou arquivo de configuração do seu projeto:

```markdown
## External Skills
Custom skills estão disponíveis em `.agent/skills/` (ou `.agent/external-skills/skills/` se usando submodule).
Antes de iniciar qualquer tarefa, verifique se existe uma skill relevante.
Carregue skills com `view_file` no arquivo SKILL.md correspondente.
```

## 🔄 Atualizações

Novas skills serão adicionadas conforme a necessidade. Para receber atualizações:

- **Submodule:** `git submodule update --remote`
- **Script:** Re-execute o `install.sh`
- **Clone:** Re-clone o repositório

## 📄 Licença

Uso interno — © ESC / guimarketing
