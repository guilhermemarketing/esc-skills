# Output Templates

Templates de output para relatórios executivos de performance.

## Markdown Template

```markdown
# Executive Performance Report — {{CLIENTE}}

> **Período:** {{DATA_INICIO}} a {{DATA_FIM}}
> **Comparação:** {{PERIODO_COMPARACAO}} (ou "Modo Snapshot — sem comparação")
> **Gerado em:** {{DATA_GERACAO}}
> **Plataformas:** {{LISTA_PLATAFORMAS}}

---

## Resumo Executivo

1. **[Fato principal]** — [número] [variação ▲/▼] [implicação para o negócio]
2. **[Segundo insight]** — [número] [implicação]
3. **[Terceiro insight]** — [número] [implicação]
[Máximo 5 bullets, sempre profit-first]

---

## Unit Economics

| Métrica | Atual | Anterior | Var | Status |
|---------|-------|----------|-----|--------|
| **CAC** | R$ X | R$ Y | ▲/▼ Z% | 🟢/🟡/🔴 |
| **LTV** | R$ X | R$ Y | ▲/▼ Z% | 🟢/🟡/🔴 |
| **LTV:CAC** | X:1 | Y:1 | — | 🟢/🟡/🔴 |
| **ROI** | X% | Y% | — | 🟢/🟡/🔴 |
| **Payback** | X meses | Y meses | — | 🟢/🟡/🔴 |

> ⚠️ [Se CAC/LTV não disponíveis]: Dados de CRM não disponíveis. CPL usado como proxy. Recomenda-se integrar CRM para análise de Unit Economics real.

---

## Consolidado Cross-Platform

| Plataforma | Spend | Leads | CPL | CPL Var | SQLs | Custo/SQL | Veredito |
|-----------|-------|-------|-----|---------|------|-----------|---------|
| Google Ads | R$ X | N | R$ X | ▲/▼ Z% | N | R$ X | 🟢/🟡/🟠/🔴 |
| Meta Ads | R$ X | N | R$ X | ▲/▼ Z% | N | R$ X | 🟢/🟡/🟠/🔴 |
| LinkedIn | R$ X | N | R$ X | ▲/▼ Z% | N | R$ X | 🟢/🟡/🟠/🔴 |
| **TOTAL** | **R$ X** | **N** | **R$ X** | **▲/▼ Z%** | **N** | **R$ X** | — |

---

## Performance por Plataforma

### Google Ads — [VEREDITO]

**Overview:**
[Parágrafo de análise com números e tendência]

**Top Campaigns:**
| Campanha | Spend | Leads | CPL | Nota |
|----------|-------|-------|-----|------|
[Top 3-5 campanhas]

**Anomalias:**
- [Lista de anomalias detectadas]

**Decisão:** [Escalar/Manter/Otimizar/Pausar] — [justificativa em 1 frase]

---

### Meta Ads — [VEREDITO]

[Mesmo formato]

---

### LinkedIn Ads — [VEREDITO]

[Mesmo formato]

---

## Análise Flywheel

### 🧲 Atrair
[Qualidade do tráfego, eficiência de aquisição, brand search, Funil Invertido]

### 💡 Engajar
[TX conversão LP, bounce rate, message match, Micro-Bolhas de remarketing]

### ⭐ Encantar
[SQL rate, close rate, satisfação, recompra]

---

## 🔴 Desperdício Identificado

1. **[Tipo]:** [Descrição] — Impacto estimado: R$ X/mês
2. [...]

---

## 🟢 Oportunidades

1. **[Tipo]:** [Descrição] — Potencial estimado: +X leads/mês
2. [...]

---

## Decisões Recomendadas

| # | Canal / Campanha | Veredito | Ação | Impacto Esperado |
|---|-----------------|----------|------|-----------------|
| 1 | [nome] | 🟢 Escalar | [ação concreta] | [resultado esperado] |
| 2 | [nome] | 🔴 Pausar | [ação concreta] | [economia esperada] |
[...]

---

## Próximos Passos

### 📅 7 dias
- [ ] [Ação tática urgente 1]
- [ ] [Ação tática urgente 2]

### 📅 30 dias
- [ ] [Otimização 1]
- [ ] [Teste A/B 1]

### 📅 90 dias
- [ ] [Revisão estratégica 1]
- [ ] [Expansão/novo canal]

---

> Relatório gerado por [gui.marketing](https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-executive-performance-report&utm_content=footer) — Brandformance Flywheel
```

---

## HTML Design Specs

### Estrutura do HTML

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Executive Report — {{CLIENTE}}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@600;700;800&display=swap" rel="stylesheet">
  <style>/* inline styles */</style>
</head>
```

### Design Tokens

```css
:root {
  /* Background */
  --bg-primary: #f7f3ed;
  --bg-card: rgba(255, 255, 255, 0.7);
  --bg-dark: #1a1a2e;

  /* Accent */
  --accent: #864df9;
  --accent-light: #a78bfa;

  /* Status */
  --status-positive: #22c55e;
  --status-negative: #ef4444;
  --status-warning: #f59e0b;
  --status-neutral: #6b7280;

  /* Veredito */
  --escalar: #22c55e;
  --manter: #f59e0b;
  --otimizar: #f97316;
  --pausar: #ef4444;

  /* Typography */
  --font-body: 'Inter', sans-serif;
  --font-heading: 'Inter Tight', sans-serif;

  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;

  /* Glassmorphism */
  --glass-bg: rgba(255, 255, 255, 0.6);
  --glass-border: rgba(255, 255, 255, 0.3);
  --glass-blur: 12px;
}
```

### Componentes Visuais

#### Indicadores de Variação
```html
<!-- Positivo -->
<span class="var-positive">▲ 23.5%</span>

<!-- Negativo -->
<span class="var-negative">▼ 12.3%</span>

<!-- Neutro -->
<span class="var-neutral">— 0.0%</span>
```

#### Cards de Veredito
```html
<div class="verdict-card verdict-escalar">
  <div class="verdict-icon">🟢</div>
  <div class="verdict-label">ESCALAR</div>
  <div class="verdict-platform">Google Ads</div>
  <div class="verdict-action">Aumentar budget 30%</div>
</div>
```

#### Unit Economics Dashboard
```html
<div class="unit-economics-grid">
  <div class="metric-card">
    <div class="metric-label">CAC</div>
    <div class="metric-value">R$ 85</div>
    <div class="metric-var var-negative">▲ 12% vs anterior</div>
  </div>
  <!-- ... LTV, LTV:CAC, ROI, Payback -->
</div>
```

### Links UTM Padrão

| Posição | URL |
|---------|-----|
| Header logo | `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-executive-performance-report&utm_content=header-logo` |
| Footer | `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-executive-performance-report&utm_content=footer` |

### Responsividade

- Desktop: 2-3 colunas para métricas, tabelas completas
- Tablet: 2 colunas, tabelas com scroll horizontal
- Mobile: 1 coluna, cards empilhados
