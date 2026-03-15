# Formatos de Output — /esc-start

Formatos de consolidação para cada etapa do pipeline. Cada arquivo `.md` gerado deve seguir o template abaixo para garantir handoff eficiente entre etapas.

> **HTML Output:** Além dos `.md`, cada etapa gera uma versão HTML estilizada para apresentação ao cliente usando os templates em `html-templates/`. O `.md` é o artefato-ponte; o `.html` é para exibição.

---

## Etapa 1 — `icp-consolidado-{{CLIENTE}}.md`

A skill `guimkt-icp-ideal-customer-profile` gera 2 arquivos:

1. `icp-consolidado-{{CLIENTE}}.html` — versão visual premium com table-tools e botões de cópia
2. `icp-consolidado-{{CLIENTE}}.md` — versão Markdown para consumo pelas próximas skills:

```markdown
# ICP — {{CLIENTE}}

## 📊 9 Dimensões
[Tabela markdown com as 9 dimensões por marca]

## 🧠 Perfil Psicográfico
### Critérios de Decisão
### Consciência do Problema
### Objeções Comuns
### Canais de Aquisição

## 🎯 ICP Real vs. Aspiracional
[Tabela markdown de filtro — cargo, dor, maturidade, porte, sinal comportamental]

## 💡 Modelos Mentais
[4 modelos com aplicação prática ao contexto]
```

> ⚠️ O arquivo `.md` é o **artefato-ponte universal** — será enviado para TODAS as etapas seguintes.

**HTML:** Usar `html-templates/icp-template.html` → salvar como `icp-{{CLIENTE}}.html`

---

## Etapa 2 — `google-ads-consolidado-{{CLIENTE}}.md`

```markdown
# Google Ads Consolidado — {{CLIENTE}}

## Keywords Positivas
[Tabela(s) com 30 keywords por marca — #, Palavra-chave, Correspondência, Formato, Justificativa]

## Keywords Negativas
[Tabela consolidada — Categoria, Keyword Negativa, Justificativa]
[Total: X keywords em Y categorias]

## Anúncios RSA
[Por marca:]
### Headlines (16)
[Tabela — Posição, Tipo, Headline, Caracteres]

### Descriptions (4)
[Tabela — Posição, Tipo, Description, Caracteres]

### Descrições Curtas (4)
[Tabela]

### Extensões (6)
[Tabela]

### Ad Preview
[Preview simulado]
```

**HTML:** Usar `html-templates/keywords-template.html`, `keywords-negativas-template.html`, `anuncios-google-template.html` → salvar como `keywords-{{CLIENTE}}.html`, `negativas-{{CLIENTE}}.html`, `anuncios-{{CLIENTE}}.html`

---

## Etapa 3 — `wireframe-tabela-{{CLIENTE}}.md`

```markdown
# Wireframe-Tabela — {{CLIENTE}}

## Framework Selecionado
- **Framework:** [nome]
- **Justificativa:** [por que este e não outros]
- **Awareness Level:** [frio/morno/quente]

## Espectro da Proposta de Valor
1. **Nível Empresa:** ...
2. **Nível Persona:** ...
3. **Nível Produto:** ...
4. **Nível Aquisição:** ...

## Wireframe-Tabela

| Seção | Framework | Elemento | Conteúdo | Notas para Designer |
|-------|-----------|----------|----------|---------------------|
| Hero | [etapa] | H1 | [headline real] | [instrução visual] |
| ... | ... | ... | ... | ... |

## Defesa do Wireframe
[Justificativa + frameworks descartados + fórmula de conversão]
```

> Se o Wireframe-Sketch (HTML) for gerado, salvar separadamente como `wireframe-sketch-{{CLIENTE}}.html`

**HTML:** Usar `html-templates/wireframe-framework-tabela-template.html` → salvar como `wireframe-tabela-{{CLIENTE}}.html`

---

## Etapa 4 — `landing-page-{{CLIENTE}}.html` + `design-system-{{CLIENTE}}.md`

O output principal é o arquivo HTML auto-contido da LP premium.

Adicionalmente, salvar resumo do design system:

```markdown
# Design System — {{CLIENTE}}

- **Style:** [liquid-glass / glassmorphism / etc.]
- **Mode:** [dark / light]
- **Primary:** [cor]
- **Accent:** [cor]
- **Font Display:** [fonte]
- **Font Body:** [fonte]
- **Efeitos:** [blur, grain, orbs, etc.]
```

---

## Etapa 5 — `meta-ads-conceitos-{{CLIENTE}}.md`

```markdown
# Conceitos Criativos Meta Ads — {{CLIENTE}}

## Briefing Sintetizado
[Extraído do ICP consolidado — máx 8 linhas]

## Clichês Descartados
> [3-5 visuais/abordagens comuns descartados]

## Insight Central
> "[verdade humana — 1 frase]"

## Conceito 1 — [Nome]
### Estratégia
[YAML: formato, objetivo, ângulo, psicologia]
### Copy
[Tabela: Headline ≤40, Texto ≤125, Descrição ≤30, CTA]
### Conceito Visual
[YAML: estilo, mood, composição, cores, tipografia]
### Adaptações por Placement
[Tabela: Stories, Feed, Reels]

[... Conceitos 2-6 ...]

## Análise Comparativa
[Recomendação de qual testar primeiro]
```

**HTML:** Usar `html-templates/conceitos-meta-template.html` → salvar como `conceitos-meta-{{CLIENTE}}.html`

---

## Etapa 6 — `criativos-classicos-{{CLIENTE}}.md`

```markdown
# Conceitos Criativos Clássicos — {{CLIENTE}}

## Briefing Sintetizado
[Extraído do ICP consolidado — máx 8 linhas]

## Clichês Descartados
> [Inclui os já descartados em Meta Ads + novos]

## Insight Central
> "[verdade humana — complementar ao insight de Meta Ads]"

## Conceito 1 — [Nome]
[Estrutura completa conforme skill]

[... Conceitos 2-3+ ...]

## Análise Comparativa
[Recomendação fundamentada]
```

**HTML:** Usar `html-templates/conceitos-classicos-template.html` → salvar como `criativos-classicos-{{CLIENTE}}.html`
