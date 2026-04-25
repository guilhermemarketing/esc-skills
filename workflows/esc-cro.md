---
description: Pipeline de CRO (Conversion Rate Optimization) — ciclo contínuo de otimização pós-launch. LPO Audit → Message Mining → Experimentation Engine → Implementação → Conversion QA (post-implementation). Orquestra 4 skills em ciclo recorrente com filosofia research-first e handoff de contexto via arquivos .md consolidados.
---

# /esc-cro — Pipeline de CRO (Ciclo Contínuo)

Pipeline **cíclico** de otimização de conversão para clientes com operação já rodando (pós-`/esc-start`). Diferente do `/esc-start` que é linear (etapa 0→8 uma vez), o `/esc-cro` é um **ciclo recorrente**: cada iteração descobre problemas, gera hipóteses, testa e valida.

```
┌──────────────────────────────────────────────────────────────────┐
│                      /esc-cro — Ciclo CRO                        │
│                                                                  │
│   [1] LPO Audit ──→ [2] Message Mining* ──→ [3] Experiment       │
│        ▲                                        Engine           │
│        │                                          │              │
│        │                                          ▼              │
│   [5] Re-Audit ◄── [4] Conversion QA ◄── Implementar vencedor   │
│                                                                  │
│   * Etapa 2 opcional — roda se houver novas fontes de VoC        │
└──────────────────────────────────────────────────────────────────┘
```

## Filosofia

> **Research-Led CRO > Opinion-Led CRO**
>
> A otimização começa com dados (quantitativos e qualitativos), não com "acho que devemos testar o botão verde".
> Metodologia FACT & ACT: Find → Analyze → Create → Test → Analyze → Combine → Tell.

> **Ciclo, não projeto.**
>
> CRO não termina. Cada ciclo gera aprendizados que alimentam o próximo. O backlog de experimentos é vivo.

---

## Pré-requisitos

Antes de iniciar o `/esc-cro`, o cliente DEVE ter:

| Requisito | Por quê | Verificação |
|-----------|---------|-------------|
| LP publicada e recebendo tráfego | Sem dados, sem CRO | URL acessível + GA4 com dados |
| GA4 + GTM configurados | Base de dados quantitativos | Property ID + Container ID |
| Tracking validado | Dados confiáveis | `conversion-qa-{{CLIENTE}}.md` aprovado |
| ICP definido | Contexto de público | `icp-consolidado-{{CLIENTE}}.md` |
| GTM conforme template gui.marketing | Tracking robusto | Folder 📊 guimarketing data-stack presente no container |
| ≥ 30 dias de dados | Baseline estatístico | GA4 com ≥ 1 mês de tráfego |

**Se o cliente não passou pelo `/esc-start`:** verificar se os pré-requisitos estão atendidos de outra forma. O `/esc-cro` é independente — não exige `/esc-start`, mas exige dados.

---

## Pre-flight: Intake do Ciclo

Antes de cada iteração do ciclo CRO, coletar:

1. **Nome do cliente** (slug `{{CLIENTE}}`)
2. **URL(s) da(s) LP(s)** a otimizar
3. **Iteração #** (primeiro ciclo? segundo? terceiro?)
4. **Dados disponíveis:**
   - GA4 com acesso? Property ID?
   - Heatmaps/recordings? (Hotjar, Clarity, VWO)
   - Surveys on-site rodando?
   - Ferramenta de teste A/B? (VWO, Optimizely, Convert, nenhuma)
5. **Novas fontes de VoC?** (reviews recentes, calls, pesquisas, Reddit)
6. **Resultados do ciclo anterior** (se não for o primeiro)
7. **Tráfego mensal** e **conversões/mês** (para ROAR Gate)
8. **Ticket médio / LTV** (para calcular impacto financeiro)

Se for a **primeira iteração**, não haverá ciclo anterior. Se for iteração subsequente, carregar `experiment-backlog-{{CLIENTE}}.md` do ciclo anterior.

---

## Etapa 1 — LPO Audit (Diagnóstico)

**Skill:** `guimkt-landing-page-optimization`

**Objetivo:** Identificar problemas e oportunidades de conversão na LP atual com dados, não opinião.

**Input:**
- URL da LP publicada
- `icp-consolidado-{{CLIENTE}}.md` (contexto de público)
- `measurement-plan-{{CLIENTE}}.md` (se existir — entender tracking)
- `message-mining-{{CLIENTE}}.md` (se existir — enriquecer com VoC)
- Dados de GA4 (bounce rate, scroll depth, device split, conversion rate por segmento)
- Heatmaps/recordings (se disponíveis)

**Execução:**
1. Invocar a skill `guimkt-landing-page-optimization`
2. Ler `references/ux-conversion-dimensions.md`
3. Aplicar as **6 Características de LP Eficaz** como framework de análise
4. Diagnosticar usando as **5 Dimensões de UX** (Motivação, Proposta de Valor, Incentivo, Fricção, Incerteza)
5. Avaliar **nível de consciência** do público vs. conteúdo da página
6. Categorizar findings por **tipo de fricção** (interação, cognitiva, emocional)
7. Aplicar a **fórmula C=4m+3v+2(i-f)-2a** para priorizar
8. Aplicar **7 Níveis de Conversão** (André Morys) para avaliação complementar
9. Gerar lista de problemas priorizados com evidência (dados VIEW + VOICE)
10. Apresentar ao usuário → aprovação

**Output:** `lpo-audit-{{CLIENTE}}-ciclo{{N}}.md` (+ HTML se solicitado)

> 💡 Este output é o **input primário** para a Etapa 3 (Experimentation Engine). Cada problema identificado é candidato a hipótese de teste.

**Checkpoint:** Aguardar aprovação do usuário antes de avançar.

---

## Etapa 2 — Message Mining (Opcional)

**Skill:** `guimkt-sales-page-message-mining`

**Condição:** Roda se houver **novas fontes de VoC** desde o último ciclo (ou desde o `/esc-start`). Se não houver material novo, **pular para Etapa 3** e usar o `message-mining-{{CLIENTE}}.md` anterior (se existir).

**Input:** Material de VoC novo fornecido pelo usuário

**Execução:**
1. Invocar a skill `guimkt-sales-page-message-mining`
2. Se `message-mining-{{CLIENTE}}.md` anterior existir, usar como base e **enriquecer** (não substituir)
3. Executar Fases 0-3 conforme workflow da skill
4. Cruzar novos verbatims com problemas identificados na Etapa 1 (LPO Audit)
5. Apresentar ao usuário → aprovação

**Output:** `message-mining-{{CLIENTE}}.md` (atualizado ou novo)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 3.

---

## Etapa 3 — Experimentation Engine (Hipóteses + Backlog)

**Skill:** `guimkt-experimentation-engine`

**Objetivo:** Transformar os problemas da LPO Audit em hipóteses testáveis, priorizar e planejar estatisticamente.

**Input:**
- `lpo-audit-{{CLIENTE}}-ciclo{{N}}.md` (problemas priorizados)
- `icp-consolidado-{{CLIENTE}}.md` (segmentos para testes)
- `message-mining-{{CLIENTE}}.md` (se existir — verbatims para fundamentar hipóteses)
- `experiment-backlog-{{CLIENTE}}.md` (do ciclo anterior, se existir — learnings acumulados)
- Dados de tráfego e conversões (para ROAR Gate e sample size)

**Execução:**
1. Invocar a skill `guimkt-experimentation-engine`
2. Executar **Etapa 0 — Intake** (tráfego, baseline, ferramenta de teste)
3. Aplicar **ROAR Gate** — determinar se A/B testing é viável:
   - < 100 conv/mês → NÃO fazer A/B, usar métodos alternativos (Etapa 2B da skill)
   - 100-1.000 → Testes simples, MDE alto
   - 1.000+ → Programa completo
4. Executar **Etapa 1 — Pesquisa** (5V's: VIEW, VOICE, VALIDATED, VERIFIED, VALUE)
   - VIEW: dados de analytics da LPO Audit
   - VOICE: dados do Message Mining
   - VALIDATED: resultados de testes anteriores (se ciclo > 1)
5. Executar **Etapa 2A — Análise Heurística** (7 Níveis + LIFT + MECLABS)
6. Executar **Etapa 3 — Geração de Hipóteses** no formato estruturado:
   - "Se [mudança] entre [segmento], então [comportamento] porque [fundamento]."
7. Executar **Etapa 4 — Priorização** (PIPE e/ou PXL)
8. Executar **Etapa 5 — Planejamento Estatístico** (sample size, duração, tipo de teste)
9. Marcar **top 3 hipóteses** como "próximo sprint"
10. Apresentar backlog priorizado ao usuário → aprovação

**Output:** `experiment-backlog-{{CLIENTE}}.md` + `experiment-backlog-{{CLIENTE}}.html`

**Checkpoint:** Aguardar aprovação do usuário. Após aprovação:

### 🔧 Etapa 3.5 — Implementação dos Testes

> **Fora do escopo do pipeline** — mas o pipeline deve guiar.

1. O usuário/dev implementa o(s) teste(s) aprovados na ferramenta de A/B testing
2. O teste roda pelo período calculado (sample size atingido)
3. **NÃO fazer peeking** — esperar conclusão completa
4. Quando o teste concluir, voltar ao pipeline para Etapa 4

**Outputs esperados da implementação:**
- Screenshot das variações implementadas
- Confirmação de que tracking está capturando dados do teste
- Dados brutos de resultados (quando o teste concluir)

---

## Etapa 4 — Conversion QA (Pós-Implementação)

**Skill:** `guimkt-conversion-qa-auditor` → **Modo 2: Post-Implementation**

**Objetivo:** Validar que o teste e/ou as mudanças implementadas não quebraram o tracking existente, e que os resultados são confiáveis.

**Input:**
- URL da LP (com teste ativo ou mudança implementada)
- `measurement-plan-{{CLIENTE}}.md`
- `experiment-backlog-{{CLIENTE}}.md` (para saber o que foi testado)
- Resultados do teste (se A/B concluído)

**Execução:**
1. Invocar a skill `guimkt-conversion-qa-auditor` no **Modo Post-Implementation**
2. Executar **Etapa 1.5 — Verificação de Conformidade com Template** (se container gui.marketing)
3. Executar **Etapa 2 — Checklist QA** (dataLayer, GA4, tags, consent, sGTM, UTMs)
4. Executar **Etapa 3 — Testes End-to-End** (formulário com UTMs, WhatsApp, consent denied)
4. Verificar que o **tracking do teste** está funcionando (eventos de variação, GA4 Audiences)
5. Se teste A/B concluiu, validar interpretação dos resultados:
   - Significância ≥ 95%?
   - Sample size atingido?
   - Duração ≥ 7 dias (2 business cycles)?
   - Novelty effect descartado?
6. Executar **Etapa 4 — Scoring e Veredicto**
7. Apresentar relatório ao usuário → aprovação

**Output:** `conversion-qa-{{CLIENTE}}-ciclo{{N}}.md` + `conversion-qa-{{CLIENTE}}-ciclo{{N}}.html`

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 5 — Documentação e Fechamento do Ciclo

**Skill:** `guimkt-experimentation-engine` → **Etapas 6-7 (ANALYZE + COMBINE + TELL)**

**Objetivo:** Documentar resultados, extrair aprendizados e alimentar o próximo ciclo.

**Input:**
- Resultados do teste (dados brutos)
- `experiment-backlog-{{CLIENTE}}.md`
- `conversion-qa-{{CLIENTE}}-ciclo{{N}}.md`

**Execução:**
1. Retomar a skill `guimkt-experimentation-engine`
2. Executar **Etapa 6 — Análise de Resultados**:
   - Interpretar significância (≥95% → implementar, 90-95% → considerar, <90% → flat)
   - Verificar armadilhas (confirmation bias, peeking, novelty effect, Simpson's paradox)
   - Segmentar resultados (device, source, new/returning)
3. Executar **Etapa 7 — Documentação**:
   - Preencher template de experimento por hipótese testada
   - Status: 🟢 Vencedor / 🔴 Perdedor / ⚪ Flat
   - Aprendizado: o que explica o resultado
4. Atualizar `experiment-backlog-{{CLIENTE}}.md` com:
   - Resultados dos testes deste ciclo
   - Próximas hipóteses priorizadas para o ciclo seguinte
   - Knowledge base acumulada
5. **Decisão de próximo ciclo:**
   - Se vencedor → implementar em produção → agendar próximo ciclo
   - Se flat → implementar o mais simples → testar próxima hipótese
   - Se perdedor → documentar aprendizado → repensar abordagem
6. Apresentar ao usuário → aprovação

**Output:**
- `experiment-backlog-{{CLIENTE}}.md` (atualizado com resultados + próximas hipóteses)
- `experiment-backlog-{{CLIENTE}}.html` (atualizado)
- `experiment-results-{{CLIENTE}}-ciclo{{N}}.md` (resultados isolados deste ciclo)

> ✅ **Ciclo completo.** Após a Etapa 5, o backlog está atualizado e o próximo ciclo pode iniciar da Etapa 1.

---

## Regras de Contexto (Inegociáveis)

1. **DADOS ANTES DE OPINIÃO** — Hipótese sem dado é opinião. Opinião não entra no backlog.
2. **ROAR GATE** — < 100 conversões/mês = NÃO fazer A/B. Usar métodos alternativos. Sem exceção.
3. **ICP É CONTEXTO** — O `icp-consolidado-{{CLIENTE}}.md` é referência para segmentação e linguagem.
4. **LPO AUDIT É FUNDAÇÃO** — Não gerar hipóteses sem auditoria prévia neste ciclo.
5. **MÍNIMO DE CONTEXTO** — Cada etapa recebe no máximo 3 arquivos + dados de analytics.
6. **CHECKPOINT OBRIGATÓRIO** — Apresentar output e aguardar aprovação antes de avançar.
7. **NÃO INVENTAR DADOS** — Se falta info, PARAR e perguntar ao usuário.
8. **NAMING CONSISTENTE** — Todos os arquivos: `[tipo]-{{CLIENTE}}-ciclo{{N}}.md`
9. **ACUMULAR, NÃO SUBSTITUIR** — Cada ciclo enriquece o backlog, nunca apaga.
10. **DOCUMENTAR TUDO** — Vitória sem documentação é acidente. Derrota sem documentação é desperdício.
11. **TEMPLATE É GUARD-RAIL** — Na Etapa 4 (QA), verificar conformidade do container GTM com o template `guimkt-gtm-expert-template`. Container fora do padrão = tracking não confiável = resultados de teste duvidosos.

---

## Mapa de Dependências de Arquivos

```
icp-consolidado-{{CLIENTE}}.md ──────────────────────────────────┐ (contexto universal)
                                                                 │
measurement-plan-{{CLIENTE}}.md ──────────────────────────┐      │
                                                          │      │
message-mining-{{CLIENTE}}.md ─────────────────┐          │      │
                                               ▼          ▼      ▼
Etapa 1: LPO Audit ──→ lpo-audit-{{CLIENTE}}-ciclo{{N}}.md
                                               │
Etapa 2: Message Mining* ──→ message-mining-{{CLIENTE}}.md (atualizado)
                                               │
Etapa 3: Experimentation ──→ experiment-backlog-{{CLIENTE}}.md
                                               │
         [IMPLEMENTAÇÃO]                       │
                                               ▼
Etapa 4: Conversion QA ──→ conversion-qa-{{CLIENTE}}-ciclo{{N}}.md
                                               │
Etapa 5: Documentação ──→ experiment-results-{{CLIENTE}}-ciclo{{N}}.md
                          └──→ experiment-backlog-{{CLIENTE}}.md (atualizado)
                                               │
                                    ┌──────────┘
                                    ▼
                              PRÓXIMO CICLO (volta para Etapa 1)
```

---

## Notas Operacionais

1. **Frequência recomendada:** ciclo mensal para clientes com volume (>1.000 conv/mês), bimestral para volume médio
2. Se o pipeline for interrompido, pode ser retomado de qualquer etapa — basta ter os `.md` anteriores
3. Se o cliente tiver múltiplas LPs, processar uma LP por ciclo (foco > dispersão)
4. O `experiment-backlog-{{CLIENTE}}.md` é um **documento vivo** — cresce a cada ciclo
5. Este workflow funciona em qualquer agente que suporte as skills do repositório ESC Skills
6. A Etapa 3.5 (implementação dos testes) é responsabilidade do usuário/dev — o pipeline guia mas não executa
7. Se o ROAR Gate indicar < 100 conv/mês, o ciclo pula a Etapa 3 e foca em otimizações diretas (redesign, usabilidade)
8. Resultados de testes devem ser compartilhados com o time de mídia para ajustar campanhas
9. Se `utm-governance-{{CLIENTE}}.md` existir, verificar alinhamento na Etapa 4
10. Para clientes novos sem histórico, o primeiro ciclo será mais longo (mais pesquisa, menos teste)
