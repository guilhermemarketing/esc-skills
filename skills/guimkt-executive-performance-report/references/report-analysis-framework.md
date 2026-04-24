# Report Analysis Framework

Framework de análise para relatórios executivos de performance digital.

## Fórmulas de KPIs

### Nível 1 — Unit Economics

| Métrica | Fórmula | Interpretação |
|---------|---------|--------------|
| **CAC** | `Spend Total / Clientes Adquiridos` | Quanto custa trazer 1 cliente |
| **LTV** | `Ticket Médio × Frequência Compra × Tempo Retenção` | Valor total que o cliente gera |
| **LTV:CAC** | `LTV / CAC` | >3:1 saudável, 1-3 atenção, <1 insustentável |
| **ROI** | `(Receita - Investimento) / Investimento × 100` | Retorno sobre investimento |
| **ROAS** | `Receita / Spend Ads` | Return on Ad Spend |
| **Margem** | `(Receita - Custos) / Receita × 100` | Margem líquida da operação |
| **Payback** | `CAC / (LTV / Meses Retenção)` | Meses para recuperar CAC |

### Nível 2 — Funil de Conversão

| Métrica | Fórmula |
|---------|---------|
| **CPL** | `Spend / Leads` |
| **Custo por SQL** | `Spend / SQLs` |
| **TX Conversão LP** | `(Leads / Visits) × 100` |
| **TX Conversão Sales** | `(SQLs / Leads) × 100` |
| **Pipeline Value** | `Σ (SQLs × Ticket Médio × Probabilidade)` |

### Nível 3 — Diagnóstico Operacional

| Métrica | Fórmula |
|---------|---------|
| **CPM** | `(Spend / Impressions) × 1000` |
| **CTR** | `(Clicks / Impressions) × 100` |
| **Outbound CTR** | `(Outbound Clicks / Impressions) × 100` |
| **CPC** | `Spend / Clicks` |
| **Outbound CPC** | `Spend / Outbound Clicks` |
| **Frequency** | `Impressions / Reach` |

---

## Mapeamento Cross-Platform

### Google Ads → Padrão

| API Metric | Padrão | Nota |
|-----------|--------|------|
| `metrics.cost_micros` | Spend (BRL) | Dividir por 1.000.000 |
| `metrics.clicks` | Total Clicks | — |
| `metrics.impressions` | Impressions | — |
| `metrics.conversions` | Leads/Conversions | — |
| `metrics.cost_per_conversion` | CPL | — |
| `metrics.average_cpm` | CPM | — |
| `metrics.ctr` | CTR | Já em % |

### Meta Ads → Padrão

| API Metric | Padrão |
|-----------|--------|
| `spend` | Spend (BRL) |
| `outbound_clicks` | Outbound Clicks |
| `clicks` | Total Clicks |
| `impressions` | Impressions |
| `reach` | Reach |
| `frequency` | Frequency |
| `cpm` | CPM |
| `actions[type=lead]` | Leads |
| `cost_per_action_type[type=lead]` | CPL |

### LinkedIn Ads → Padrão

| API Metric | Padrão |
|-----------|--------|
| `costInLocalCurrency` | Spend (BRL) |
| `landingPageClicks` | Outbound Clicks |
| `clicks` | Total Clicks |
| `impressions` | Impressions |
| `externalWebsiteConversions` | Leads |

### TikTok Ads → Padrão (Manual/CSV)

| Export Field | Padrão |
|-------------|--------|
| `Cost` | Spend |
| `Impression` | Impressions |
| `Click` | Clicks |
| `Conversion` | Leads |
| `CPC` | CPC |
| `CPM` | CPM |

### Pinterest Ads → Padrão (Manual/CSV)

| Export Field | Padrão |
|-------------|--------|
| `Spend` | Spend |
| `Impressions` | Impressions |
| `Clicks` | Clicks |
| `Conversions` | Leads |

---

## Regras Heurísticas de Anomalia

Anomalias detectadas automaticamente quando variação > threshold:

| Anomalia | Threshold | Severidade | Ação Sugerida |
|----------|-----------|-----------|--------------|
| **CPL Spike** | CPL > 2× média do período anterior | 🔴 Alta | Investigar + considerar pausar |
| **Frequency Alta** | Frequency > 5 | 🟠 Média | Refresh de criativos |
| **CTR Drop** | CTR caiu > 30% | 🟠 Média | Revisar copy + criativos |
| **Budget Waste** | Campanha com > R$500 spend e 0 conversões | 🔴 Alta | Pausar imediatamente |
| **Quality Score Baixo** | QS < 4 (Google) | 🟠 Média | Revisar relevância keyword-ad-LP |
| **CAC Explosão** | CAC > 2× meta definida | 🔴 Alta | Revisar todo funil |
| **LTV:CAC < 1** | Ratio abaixo de 1 | 🔴 Crítica | Operação insustentável — parar e reestruturar |
| **Micro-Bolha Vazia** | Remarketing < 5% do spend total | 🟡 Baixa | Ativar remarketing / criar Micro-Bolha |
| **Saturação** | CPM subiu > 40% sem mudança de audience | 🟠 Média | Expandir audiência ou trocar criativos |
| **Conversão LP Drop** | TX conversão LP caiu > 25% | 🔴 Alta | Auditar LP (CRO) |

---

## Framework de Decisão por Canal

### Matriz de Veredito

```
                CPL ≤ Meta          CPL > Meta
              ┌─────────────────┬──────────────────┐
Volume OK     │ 🟢 ESCALAR      │ 🟠 OTIMIZAR     │
              │ +20-50% budget  │ Criativos/LP/Bid │
              ├─────────────────┼──────────────────┤
Volume Baixo  │ 🟡 MANTER       │ 🔴 PAUSAR       │
              │ Monitorar 7d    │ Realocar budget  │
              └─────────────────┴──────────────────┘
```

### Critérios de Escala (todos devem ser verdadeiros)

1. CPL ≤ meta do cliente
2. ROI positivo (se dados disponíveis)
3. Frequency < 4 (audiência não saturada)
4. LP conversion rate estável ou crescente
5. Budget < 50% do budget máximo disponível

### Critérios de Pausa (qualquer um é suficiente)

1. CPL > 2× meta por > 7 dias
2. Zero conversões com > R$500 gastos
3. Frequency > 7 (audiência esgotada)
4. LTV:CAC < 1

---

## Checklist de Análise por Plataforma

### Google Ads
- [ ] Campanhas habilitadas vs pausadas
- [ ] Search terms — keywords gastando sem converter?
- [ ] Quality Score das top keywords
- [ ] Impression Share — estamos perdendo por budget ou rank?
- [ ] Conversão por dispositivo (mobile vs desktop)
- [ ] Remarketing ativo? (Micro-Bolha)

### Meta Ads
- [ ] Breakdown por campanha/adset
- [ ] Frequency por adset — fadiga?
- [ ] Creative performance — qual visual performa?
- [ ] Outbound CTR vs CTR geral (clicks que saem da plataforma)
- [ ] Placement performance (feed vs stories vs reels)
- [ ] Lookalike vs interest audiences

### LinkedIn Ads
- [ ] CPL vs benchmark do segmento (LinkedIn é caro)
- [ ] Campanhas por formato (Single Image, Carousel, Video)
- [ ] Segmentação por cargo/senioridade — decisor vs influenciador?
- [ ] Lead Gen Forms vs Traffic campaigns

### TikTok Ads
- [ ] CPM e CTR vs benchmark TikTok (CPM tipicamente baixo)
- [ ] Engajamento do criativo (watch time, completion rate)
- [ ] Conversão — tráfego TikTok converte na LP?
- [ ] Audiência etária compatível com ICP

### Pinterest Ads
- [ ] Performance por formato de pin
- [ ] CTR e conversão
- [ ] Seasonal trends — sazonalidade forte no Pinterest

### Search Console
- [ ] Top queries orgânicas — complementam ou competem com paid?
- [ ] Branded vs non-branded traffic
- [ ] CTR orgânico das top pages
- [ ] Indexação de LPs — estão indexadas?

---

## Análise Flywheel

### Atrair (Topo)
- Qualidade do tráfego: % ICP quente vs tráfego frio
- Eficiência de aquisição: CAC por tipo de público
- Brand search trend: awareness gerando demanda orgânica?
- Funil Invertido: base proprietária sendo ativada primeiro?

### Engajar (Meio)
- Taxa de conversão da LP
- Bounce rate e tempo na página
- Message match: ad → LP → formulário consistentes?
- Micro-Bolhas: remarketing ativo e com budget adequado?

### Encantar (Fundo)
- SQL rate (Lead → SQL)
- Close rate (SQL → Cliente)
- NPS / satisfação (se disponível)
- Recompra / upsell / referral (se disponível)
- Offline Conversions feedback loop ativo?
