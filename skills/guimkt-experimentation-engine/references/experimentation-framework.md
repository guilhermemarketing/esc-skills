# Experimentation Framework Reference

Especificações técnicas de frameworks, fórmulas e checklists para o Experimentation Engine.

## 1. Framework FACT & ACT (CXL / Ton Wesseling)

```
Phase 1 — FACT (Pesquisa → Teste):
  F — FIND: Coletar dados (5V's: View, Voice, Validated, Verified, Value)
  A — ANALYZE: Analisar comportamento, identificar padrões e gargalos
  C — CREATE: Criar hipóteses e designs de teste
  T — TEST: Executar experimento com rigor estatístico

Phase 2 — ACT (Resultado → Conhecimento):
  A — ANALYZE: Interpretar resultados, segmentar, verificar validade
  C — COMBINE: Integrar aprendizado na knowledge base organizacional
  T — TELL: Comunicar resultados para stakeholders e equipe
```

## 2. Modelo ROAR (Maturidade de Experimentação)

| Nível | Conversões/mês | Foco | Métodos |
|-------|:--------------:|------|---------|
| **Re-think** | < 100 | Validação qualitativa | Usabilidade, heurística, surveys, comparação períodos |
| **Optimize** | 100-1.000 | Testes de alto impacto | A/B simples, MDE >20%, mudanças radicais |
| **Automate** | 1.000-10.000 | Programa contínuo | A/B completo, MDE 5-15%, múltiplos testes simultâneos |
| **Redefine** | > 10.000 | Inovação | MVT, personalização, micro-otimizações, ML |

## 3. Os 7 Níveis de Conversão (André Morys / konversionsKRAFT)

Baseado no modelo de Rubicon e 10+ anos de pesquisa. Testes baseados neste framework geram uplifts típicos de 40-60%.

| Nível | Pergunta Implícita | Elementos de Página | Red Flags |
|:-----:|---------------------|---------------------|-----------|
| 1. Relevância | "Página certa pra mim?" | Headline = busca, imagens contextuais | Message mismatch com ad |
| 2. Confiança | "Posso confiar?" | Logos, depoimentos, certificações, mídia | Sem prova social alguma |
| 3. Orientação | "Onde clico?" | Hierarquia visual, CTA claro, navigation | CTAs competindo, layout confuso |
| 4. Estímulo | "Por que agora?" | Urgência, escassez, benefício exclusivo | Sem razão para agir agora |
| 5. Segurança | "É seguro?" | Garantias, políticas, selos de segurança | Sem HTTPS, sem garantia |
| 6. Conveniência | "Será fácil?" | Form simples, poucos passos, auto-fill | Form longo, sem validação |
| 7. Confirmação | "Fiz certo?" | Thank you page, email, próximos passos | Página genérica pós-conversão |

## 4. LIFT Model (WiderFunnel)

```
                    ↑ RELEVÂNCIA
                    ↑ CLAREZA
   ← URGÊNCIA →  [PROPOSTA DE VALOR]  ← URGÊNCIA →
                    ↓ ANSIEDADE
                    ↓ DISTRAÇÃO
```

- **Proposta de Valor** = veículo central (peso máximo)
- **Relevância** = match entre expectativa e conteúdo
- **Clareza** = facilidade de entender a oferta
- **Urgência** = propulsor (por que agora?)
- **Ansiedade** = freio (medo, incerteza)
- **Distração** = freio (elementos irrelevantes)

## 5. Fórmula MECLABS

```
C = 4m + 3v + 2(i - f) - 2a

Onde:
  C = Probabilidade de conversão
  m = Motivação do usuário (peso 4×) — NÃO controlável
  v = Proposta de valor (peso 3×) — CONTROLÁVEL
  i = Incentivo (peso 2×) — CONTROLÁVEL
  f = Fricção (peso 2×) — CONTROLÁVEL
  a = Ansiedade (peso -2×) — CONTROLÁVEL

Implicação: Motivação é o fator mais forte. Página perfeita com
público errado = zero conversão. Público certo com página ruim =
ainda converte algo.
```

## 6. Cálculo de Sample Size

### Fórmula Simplificada

```
n = (Z_α/2 + Z_β)² × 2p(1-p) / δ²

Onde:
  n = sample size por variação
  Z_α/2 = 1.96 (para 95% de significância)
  Z_β = 0.84 (para 80% de power)
  p = baseline conversion rate
  δ = MDE (minimum detectable effect) em pontos absolutos
```

### Tabela de Referência Rápida

| Baseline CR | MDE 5% relativo | MDE 10% relativo | MDE 20% relativo |
|:-----------:|:---------------:|:-----------------:|:----------------:|
| 1% | ~600k/var | ~160k/var | ~40k/var |
| 3% | ~200k/var | ~50k/var | ~13k/var |
| 5% | ~120k/var | ~30k/var | ~8k/var |
| 10% | ~60k/var | ~15k/var | ~4k/var |
| 20% | ~25k/var | ~6.5k/var | ~1.6k/var |

### Duração Estimada

```
Duração (dias) = Sample size por variação × Nº variações / Sessões por dia

Regras:
- Mínimo: 7 dias (capturar dia-da-semana)
- Ideal: 2+ business cycles (14 dias)
- Máximo prático: 60 dias
- Se > 60 dias → aumentar MDE ou desistir do teste
```

## 7. Correção para Múltiplas Métricas

Se testar N métricas simultaneamente, aplicar correção:

### Holm-Bonferroni (recomendado)

```
1. Ordenar p-values do menor para o maior
2. Para o menor p-value: rejeitar se p < α/N
3. Para o 2º menor: rejeitar se p < α/(N-1)
4. Continue até falhar em rejeitar
```

### Šidák

```
α_ajustado = 1 - (1 - α)^(1/N)

Para 2 métricas com α=0.05: α_ajustado = 0.0253
Para 3 métricas com α=0.05: α_ajustado = 0.0170
```

## 8. Níveis de Consciência (Schwartz) — Para Segmentação de Testes

| Nível | Descrição | Implicação para Teste |
|-------|-----------|----------------------|
| **Unaware** | Não sabe que tem o problema | Testar educação vs. nada |
| **Problem-Aware** | Sabe do problema, não da solução | Testar agitação da dor |
| **Solution-Aware** | Conhece soluções, não seu produto | Testar diferenciação |
| **Product-Aware** | Conhece seu produto, indeciso | Testar prova social e garantias |
| **Most-Aware** | Quer comprar, precisa de empurrão | Testar oferta e urgência |

## 9. Template de Hipótese

```
ID: EXP-{{CLIENTE}}-{{NNN}}
Data: {{YYYY-MM-DD}}
Autor: {{nome}}

HIPÓTESE:
"Se [aplicarmos {{mudança específica}}]
entre [{{segmento de usuários}}],
então [{{comportamento esperado}} na métrica {{KPI}}]
porque [{{fundamento: dado + princípio psicológico}}]."

EVIDÊNCIA:
- VIEW: {{dado analytics / heatmap}}
- VOICE: {{dado qualitativo / survey}}
- VERIFIED: {{princípio/paper/heurística}}

PRIORIZAÇÃO (PIPE):
- Potential: {{1-5}} | Impact: {{1-5}} | Power: {{1-5}} | Ease: {{1-5}}
- Score: {{média}}

PLANEJAMENTO:
- Tipo: A/B | A/B/n | Sequential | Smoke test
- Página: {{URL}}
- KPI primário: {{métrica}} (baseline: {{X%}})
- Guardrails: {{métricas secundárias}}
- MDE: {{Y%}}
- Sample size: {{N por variação}}
- Duração estimada: {{D dias}}
- Ferramenta: {{VWO/Optimizely/Convert/GTM+GA4}}
```

## 10. Checklist Pré-Teste

```
□ Hipótese documentada com fundamento (dado + psicologia)
□ KPI primário definido e BINÁRIO
□ Baseline medido (últimos 14-30 dias, mesmo segmento)
□ Sample size calculado
□ Duração mínima definida (≥ 7 dias, ≥ 2 business cycles)
□ Tracking validado (GA4 events, GTM tags, conversões)
□ Variações implementadas e QA'd
□ Sem conflitos com outros testes ativos
□ Stakeholders informados (não vão "ajudar" mexendo na página)
□ Documento de teste criado no backlog
```
