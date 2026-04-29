---
description: Pipeline de CRO (Conversion Rate Optimization) — ciclo contínuo de otimização pós-launch. LPO Audit → Message Mining → Experimentation Engine → Implementação → Conversion QA (post-implementation). Orquestra 4 skills em ciclo recorrente com filosofia research-first e handoff de contexto via arquivos .md consolidados.
---

# /esc-cro — Pipeline de CRO (Ciclo Contínuo)

Pipeline **cíclico** de otimização de conversão para clientes com operação já rodando (pós-`/esc-start`). Diferente do `/esc-start` que é linear (etapa 0→9 uma vez), o `/esc-cro` é um **ciclo recorrente**: cada iteração descobre problemas, gera hipóteses, testa e valida.

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

| Requisito | Por quê | Verificação |
|-----------|---------|-------------|
| LP publicada e recebendo tráfego | Sem dados, sem CRO | URL acessível + GA4 com dados |
| GA4 + GTM configurados | Base de dados quantitativos | Property ID + Container ID |
| Tracking validado | Dados confiáveis | `conversion-qa-{{CLIENTE}}.md` aprovado |
| ICP definido | Contexto de público | `icp-consolidado-{{CLIENTE}}.md` |
| GTM conforme template gui.marketing | Tracking robusto | Folder 📊 guimarketing data-stack presente no container |
| ≥ 30 dias de dados | Baseline estatístico | GA4 com ≥ 1 mês de tráfego |

---

## Pre-flight: Intake do Ciclo

Antes de cada iteração, coletar:

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

Se iteração subsequente, carregar `experiment-backlog-{{CLIENTE}}.md` do ciclo anterior.

---

## Etapa 1 — LPO Audit (Diagnóstico)

**Skill:** `guimkt-landing-page-optimization`

**Input:** URL da LP + `icp-consolidado-{{CLIENTE}}.md` + `measurement-plan-{{CLIENTE}}.md` (se existir) + `message-mining-{{CLIENTE}}.md` (se existir) + dados de GA4 + heatmaps (se disponíveis)
**Output:** `lpo-audit-{{CLIENTE}}-ciclo{{N}}.md` (+ HTML se solicitado)

Executar a skill integralmente. O output é o **input primário** para a Etapa 3 — cada problema identificado é candidato a hipótese de teste.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 2 — Message Mining (Opcional)

**Skill:** `guimkt-sales-page-message-mining`

**Condição:** Roda se houver **novas fontes de VoC** desde o último ciclo (ou desde o `/esc-start`). Se não → **pular para Etapa 3** e usar `message-mining-{{CLIENTE}}.md` anterior (se existir).

**Input:** Material de VoC novo
**Output:** `message-mining-{{CLIENTE}}.md` (atualizado ou novo)

Executar a skill integralmente. Se versão anterior existir, **enriquecer** (não substituir). Cruzar novos verbatims com problemas da Etapa 1.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 3 — Experimentation Engine (Hipóteses + Backlog)

**Skill:** `guimkt-experimentation-engine`

**Input:** `lpo-audit-{{CLIENTE}}-ciclo{{N}}.md` + `icp-consolidado-{{CLIENTE}}.md` + `message-mining-{{CLIENTE}}.md` (se existir) + `experiment-backlog-{{CLIENTE}}.md` (do ciclo anterior, se existir) + dados de tráfego/conversões
**Output:** `experiment-backlog-{{CLIENTE}}.md` + `.html`

Executar a skill integralmente. Pontos críticos pipeline-level:

1. **ROAR Gate** — determinar viabilidade ANTES de gerar hipóteses:
   - < 100 conv/mês → **NÃO fazer A/B**, usar métodos alternativos (Etapa 2B da skill)
   - 100-1.000 → Testes simples, MDE alto
   - 1.000+ → Programa completo
2. Marcar **top 3 hipóteses** como "próximo sprint"

**Checkpoint:** Aguardar aprovação. Após aprovação:

### 🔧 Etapa 3.5 — Implementação dos Testes

> **Fora do escopo do pipeline** — mas o pipeline deve guiar.

1. O usuário/dev implementa o(s) teste(s) aprovados na ferramenta de A/B testing
2. O teste roda pelo período calculado (sample size atingido)
3. **NÃO fazer peeking** — esperar conclusão completa
4. Quando o teste concluir, voltar ao pipeline para Etapa 4

---

## Etapa 4 — Conversion QA (Pós-Implementação)

**Skill:** `guimkt-conversion-qa-auditor` → **Modo Post-Implementation**

**Input:** URL da LP (com teste ativo ou mudança implementada) + `measurement-plan-{{CLIENTE}}.md` + `experiment-backlog-{{CLIENTE}}.md` + resultados do teste (se A/B concluído)
**Output:** `conversion-qa-{{CLIENTE}}-ciclo{{N}}.md` + `.html`

Executar a skill integralmente no Modo Post-Implementation. Adicionalmente, validar:
- Tracking do teste está funcionando (eventos de variação, GA4 Audiences)
- Se teste A/B concluiu: significância ≥ 95%, sample size atingido, duração ≥ 7 dias (2 business cycles), novelty effect descartado

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 5 — Documentação e Fechamento do Ciclo

**Skill:** `guimkt-experimentation-engine` → **Etapas 6-7 (ANALYZE + COMBINE + TELL)**

**Input:** Resultados do teste + `experiment-backlog-{{CLIENTE}}.md` + `conversion-qa-{{CLIENTE}}-ciclo{{N}}.md`
**Output:**
- `experiment-backlog-{{CLIENTE}}.md` (atualizado com resultados + próximas hipóteses)
- `experiment-results-{{CLIENTE}}-ciclo{{N}}.md` (resultados isolados deste ciclo)

Retomar a skill para documentar resultados. Decisão de próximo ciclo:
- Se vencedor → implementar em produção → agendar próximo ciclo
- Se flat → implementar o mais simples → testar próxima hipótese
- Se perdedor → documentar aprendizado → repensar abordagem

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
11. **TEMPLATE É GUARD-RAIL** — Na Etapa 4, verificar conformidade do container GTM com template gui.marketing.

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
