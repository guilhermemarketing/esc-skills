---
description: Pipeline independente para gerar 10 conceitos criativos de performance para Meta Ads (Facebook/Instagram). Aciona diretamente a skill guimkt-meta-ads v3.0 com framework Hook → Hold → Offer, 40+ Creative Types, variações A/B de hook e mapeamento de funil. Não depende do /esc-start — funciona standalone com briefing direto.
---

# /esc-meta-ads-creatives — Conceitos de Performance para Meta Ads

Pipeline standalone que gera 10 conceitos criativos de **performance / direct response** para Meta Ads usando a skill `guimkt-meta-ads` v3.0.

> **Independente do `/esc-start`.** Este workflow funciona com briefing direto — não exige ICP prévio, wireframe ou LP. Ideal para demandas isoladas de criativos ou para clientes que já possuem esses ativos.

```
[0] Design System* → [1] Briefing + Customer Avatar → [2] Customer Journey Map →
[3] 10 Conceitos → [4] Desenvolver (Hook → Hold → Offer) →
[5] Validação → [6] Prompts de Imagem → [7] Criativos Visuais*

* Etapas condicionais
```

---

## Pre-flight: Coletar Briefing

Antes de iniciar, obter do usuário:

1. **Nome do cliente** (slug `{{CLIENTE}}`)
2. **Briefing** — texto livre, documento, URL do site, ou YAML estruturado:

```yaml
briefing:
  cliente: [Nome da empresa/marca]
  produto_servico: [O que está sendo anunciado]
  publico: [Quem — demográfico E psicográfico]
  dor: [Problema real que o produto resolve]
  diferencial: [O que diferencia das alternativas]
  prova: [Dados, depoimentos, resultados concretos]
  tom_de_voz: [Como a marca fala]
  objetivo: [leads | vendas | agendamentos | cadastros]
  restricoes: [O que NÃO pode ser dito/mostrado]
```

3. **Oferta:**

```yaml
offer:
  tipo: "[desconto | BOGO | bundle | garantia | GWP | frete grátis | trial]"
  detalhe: "[descrição da oferta]"
  urgencia: "[limitada | sazonal | evergreen]"
```

4. **Materiais opcionais:**
   - `icp-consolidado-{{CLIENTE}}.md` — se existir, enriquece avatar e ângulos
   - `design-system-{{CLIENTE}}.md` — se existir, governa paleta e tipografia
   - `message-mining-{{CLIENTE}}.md` — se existir, fornece linguagem real do cliente

Se o briefing for insuficiente, **PARAR e perguntar**. Não gerar conceitos com informação incompleta.

---

## Etapa 0 — Design System (Condicional)

**Condição:** Se `design-system-{{CLIENTE}}.md` existir, ler e extrair tokens visuais. Se não existir, seguir com cores e tom do briefing.

```yaml
design_system:
  cores_primarias: [hex values]
  cores_secundarias: [hex values]
  tipografia: [font families, weights]
  mood: [atmosfera]
  componentes: [estilos de botões, cards]
```

> Tokens DEVEM ser respeitados em todos os conceitos.

---

## Etapa 1 — Diagnóstico do Briefing + Customer Avatar

**Skill:** `guimkt-meta-ads` → Etapa 1

**Execução:**
1. Sintetizar briefing em bloco estruturado (produto, público, dor, diferencial, objetivo, oferta)
2. Construir **Customer Avatar Hooks**:
   - `why_want` — razões para comprar (solutions/goals/desires)
   - `why_not_want` — objeções e medos (pain/fear/objections)
   - `why_watch` — razões para prestar atenção (proof/credibility/comparison)
3. Validar **Checklist de viabilidade** — PARAR se:
   - Diferencial genérico ("qualidade e preço")
   - Público vago ("homens e mulheres 25-55")
   - Sem prova concreta — só promessa
   - Oferta inexistente ou fraca
4. Se `icp-consolidado-{{CLIENTE}}.md` existir, extrair avatar hooks do ICP (9 Dimensões + Psicográfico)
5. Se `message-mining-{{CLIENTE}}.md` existir, enriquecer hooks com verbatims reais

**Checkpoint:** Apresentar briefing sintetizado + avatar hooks ao usuário → aprovação antes de gerar conceitos.

---

## Etapa 2 — Customer Journey Mapping

**Skill:** `guimkt-meta-ads` → Etapa 2

Mapear quais hooks e Creative Types usar em cada estágio do funil:

```yaml
customer_journey:
  cold_tof:  # não conhece a marca
    hooks: [curiosidade, pain, shock, stat]
    creative_types: "[3-4 da tabela]"
  warm_mof:  # conhece o problema
    hooks: [benefit, feature, comparison, how-to]
    creative_types: "[3-4 da tabela]"
  hot_bof:  # pronto para agir
    hooks: [sale, review, credibility, offer]
    creative_types: "[3-4 da tabela]"
```

**Distribuição obrigatória nos 10 conceitos:**
- Mínimo 3 Cold (TOF)
- Mínimo 3 Warm (MOF)
- Mínimo 2 Hot (BOF)
- 2 flexíveis

Consultar `references/creative-types-hooks.md` para a tabela completa de 41 Creative Types.

---

## Etapa 3 — Anti-Clichê + Gerar 10 Conceitos

**Skill:** `guimkt-meta-ads` → Etapa 3

**Execução:**
1. Listar 3-5 clichês visuais do setor do cliente e descartá-los
2. Gerar 10 conceitos com **diversidade obrigatória de Creative Types**:
   - Mínimo **6 Creative Types diferentes** (dos 41 disponíveis)
   - Cobertura de **Cold/Warm/Hot** conforme mapeamento da Etapa 2
   - Cada conceito declara **1-2 Emotion Triggers**
   - Não repetir o mesmo Creative Type em mais de 2 conceitos

---

## Etapa 4 — Desenvolver Cada Conceito

**Skill:** `guimkt-meta-ads` → Etapa 4

Para cada um dos 10 conceitos, documentar 5 blocos:

1. **Estratégia** (YAML: creative_type, formato, funnel_stage, hook_type, emotion_triggers, copy_type)
2. **Hook → Hold → Offer** (tabela: o que para o scroll / mantém atenção / gera clique)
3. **Copy** (tabela com limites: headline ≤40, texto ≤125, descrição ≤30, CTA nativo)
4. **Conceito Visual** (YAML: ad_layout funcional, composição, cores, tipografia, overlay ≤5 palavras)
5. **Variações A/B** (3 variações de hook por conceito — obrigatório)

---

## Etapa 5 — Checklist de Validação

**Skill:** `guimkt-meta-ads` → Etapa 5

**Performance & Direct Response:**
- [ ] Cada conceito tem Creative Type distinto (mín. 6 tipos nos 10)
- [ ] Customer Journey coberto: mín. 3 Cold + 3 Warm + 2 Hot
- [ ] Hook claro — o que para o scroll em 1.7s?
- [ ] Offer clara — o que faz clicar?
- [ ] 3 variações A/B de hook por conceito
- [ ] Foco no CLIENTE e sua dor (não na marca)

**Copy & Compliance:**
- [ ] Headline ≤40 chars, texto ≤125, descrição ≤30
- [ ] Regra 20% texto respeitada
- [ ] Sem promessas exageradas

**Testes de Qualidade:**
- [ ] Uma ideia por peça — cabe em 1 frase?
- [ ] Teste do borrão — visto embaçado, parece interessante?
- [ ] Teste do logo trocado — funciona com concorrente? (se sim → refazer)

**Checkpoint:** Apresentar os 10 conceitos ao usuário → aprovação.

---

## Etapa 6 — Arquivo de Prompts de Imagem

**Skill:** `guimkt-meta-ads` → Etapa 6

**Obrigatória.** Consolidar todos os prompts em `prompts-imagens-{{CLIENTE}}.md`:

```markdown
# Prompts de Imagem — Meta Ads [Nome do Cliente]

> Gerado em: [data]
> Skill: guimkt-meta-ads v3.0
> Total de prompts: [N]

## Conceito 1 — [Nome]
**Creative Type:** [tipo]
**Funnel Stage:** [Cold/Warm/Hot]
**Estilo visual:** [fotografia | UGC | screenshot | tipográfico | misto]

### Prompt Principal
[prompt completo em inglês, incluindo --ar]

### Variações A/B
[prompts B e C]

---
[repetir para conceitos 2-10]
```

---

## Etapa 7 — Criativos Visuais (Condicional)

**Condição:** Apenas se o usuário solicitar geração de imagens.

**Execução:**
1. Usar `generate_image` com prompt base da seção "Geração de Imagens Finais" da skill
2. Aspect ratio padrão: **4:5** (1080×1350px)
3. Cada imagem = anúncio completo com headline, descrição e CTA integrados
4. Respeitar design system quando disponível
5. 1 imagem por conceito (sem carrossel, a menos que solicitado)

---

## Deliverables Finais

| Arquivo | Descrição | Obrigatório |
|---------|-----------|-------------|
| `conceitos-meta-{{CLIENTE}}.md` | 10 conceitos direct response | ✅ Sim |
| `prompts-imagens-{{CLIENTE}}.md` | Prompts de imagem consolidados | ✅ Sim |
| `conceitos-meta-{{CLIENTE}}.html` | HTML premium para apresentação | ❌ Sob demanda |
| Imagens geradas (4:5) | Criativos visuais finais | ❌ Sob demanda |

---

## Regras de Contexto

1. **BRIEFING RUIM → CRIATIVO RUIM** — Não pular Etapa 1. Se falta info, perguntar.
2. **DESIGN SYSTEM GOVERNA** — Se existe, respeitar. Não substituir por preferências do agente.
3. **DIVERSIDADE OBRIGATÓRIA** — Mín. 6 Creative Types, cobertura Cold/Warm/Hot. Sem isso, o output é genérico.
4. **VARIAÇÃO A/B É PADRÃO** — Cada conceito nasce com 3 hooks. Conceito sem variação é achismo.
5. **CONVERSÃO > ESTÉTICA** — Cada conceito deve ter caminho claro para ação mensurável.
6. **EVERGREEN > SAZONAL** — Criativos vencedores rodam 6-12 meses. Evitar datas/temporalidade.
7. **CHECKPOINT OBRIGATÓRIO** — Apresentar briefing sintetizado (Etapa 1) e conceitos finais (Etapa 5) ao usuário antes de avançar.
8. **FOCO NO CLIENTE** — Copy e visual falam sobre a DOR do cliente, não sobre a marca (a menos que household brand).

---

## Notas Operacionais

1. Este workflow é **standalone** — funciona sem `/esc-start`, `/esc-cro` ou qualquer outro pipeline
2. Se `icp-consolidado-{{CLIENTE}}.md` existir, usar para enriquecer — mas não é obrigatório
3. Se o cliente precisar de criativos para **outras plataformas** (Google, LinkedIn, TikTok), usar `/esc-start` Etapa 6 (`guimkt-classic-advertising-creative`) após este workflow
4. Para output HTML premium, usar template `references/conceitos-meta-template.html`
5. Hook Rate target: 30-50% | A/B test: mín. 5 dias, 3x AOV em ad spend
6. Se o usuário pedir menos de 10 conceitos, ajustar proporcionalmente mantendo a distribuição Cold/Warm/Hot
