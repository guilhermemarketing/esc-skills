---
name: guimkt-google-ads
description: >
  Skill completa de Google Ads Search para geração de leads qualificados (SQLs).
  Pipeline sequencial em 4 fases: (1) ICP, (2) Keywords positivas, (3) Keywords negativas,
  (4) Anúncios responsivos (RSA). Cada fase pode ser executada individualmente.
  Use quando o usuário pedir para criar campanhas de Google Ads, definir ICP para mídia paga,
  gerar keywords para Google Ads, criar lista de keywords negativas, criar anúncios de texto
  responsivo, montar RSA, ou qualquer variação de "Google Ads", "campanha de pesquisa",
  "search ads", "keywords Google", "anúncios responsivos", "negativar palavras-chave",
  "ICP para tráfego pago", "gerar leads com Google", "campanha de busca".
  Suporta múltiplas marcas por cliente.
---

# guimkt-google-ads

Skill completa para criar campanhas de Google Ads Search focadas em geração de leads qualificados (SQLs). Pipeline de 4 fases sequenciais, cada uma executável individualmente.

## Pipeline Overview

```
Fase 1: ICP → Fase 2: Keywords → Fase 3: Keywords Negativas → Fase 4: Anúncios RSA
```

Cada fase produz um deliverable que alimenta a próxima. Executar na ordem; é possível pular para uma fase se os deliverables anteriores já existirem.

## Pre-flight: Coletar Briefing

Antes de executar qualquer fase, obter do usuário:

1. **Nome da empresa / marca(s)** — identificar se há múltiplas marcas
2. **Produto(s) / serviço(s)** e diferenciais por marca
3. **Mercado de atuação** (B2B / B2C / ambos)
4. **Público-alvo** declarado
5. **URLs dos sites** de cada marca
6. **Provas sociais** (números, cases, certificações)
7. **Tom de voz / posicionamento**

Se o usuário fornecer um documento de briefing (PDF, DOCX, etc.), extrair essas informações diretamente. **Compilar** um resumo de no máximo 80 linhas antes de executar qualquer fase.

> **Regra de ouro:** Nunca carregar briefing bruto no contexto de geração. Usar apenas o resumo compilado.

## Fase 1: Definição de ICP

### Objetivo
Definir o Ideal Customer Profile para orientar todas as campanhas.

### Inputs
- Briefing compilado do cliente

### Prompt de Geração

Executar o seguinte prompt usando **apenas** o briefing compilado:

> Pretendo criar campanhas para gerar SQLs para vender as soluções da **{{EMPRESA}}**.
>
> Com base nas informações do briefing fornecido, defina o ICP da **{{EMPRESA}}**.
>
> Escreva o ICP contendo as seguintes dimensões:
>
> | Dimensão | Descrição |
> |----------|-----------|
> | **Faixa Etária** | Idade típica do decisor |
> | **Profissão** | Área de atuação profissional |
> | **Cargo** | Posição hierárquica na empresa |
> | **Setor** | Segmentos de mercado prioritários |
> | **Formação** | Background educacional relevante |
> | **Objetivos** | O que busca alcançar profissionalmente |
> | **Dores** | Problemas e frustrações atuais |
> | **Necessidades** | O que precisa para resolver suas dores |
> | **Tópicos de Interesse** | Assuntos que consome e pesquisa |
>
> Enriqueça com perfil psicográfico: critérios de decisão de compra, nível de consciência sobre o problema, objeções comuns e canais de aquisição preferidos.

### Critérios de Qualidade
- Todas as 9 dimensões preenchidas
- Informações baseadas no briefing (não inventar dados)
- Linguagem clara e específica ao mercado do cliente
- Perfil psicográfico inclui: critérios de decisão, nível de consciência, objeções, canais

### Output
- Tabela com as 9 dimensões + bloco psicográfico
- Presentar ao usuário para revisão antes de avançar

---

## Fase 2: Keywords Positivas (30 por marca)

### Objetivo
Gerar lista estruturada de palavras-chave para Google Ads Search com foco em leads qualificados.

### Inputs
- ICP definido na Fase 1
- Briefing compilado

### Detecção de Marcas
Analisar o briefing e identificar quantas marcas/unidades de negócio existem:
- **Marca única** → 1 tabela com 30 keywords
- **N marcas** → N tabelas separadas com 30 keywords cada (total = N × 30)

### Prompt de Geração

> Agora você é um especialista sênior em campanhas de Google Ads Pesquisa.
>
> Com base no ICP definido e no briefing da **{{EMPRESA}}**, escreva **30 palavras-chave por marca** formatadas de acordo com sua correspondência, com objetivo de gerar leads qualificados (SQLs).
>
> **Regras de Correspondência (por marca):**
> - **Apenas 1 keyword será ampla** (escolha a mais estratégica por marca)
> - As demais distribuídas entre **frase** e **exata**
> - Priorize intenção de compra/contratação
>
> **Estrutura da Tabela:**
>
> | # | Palavra-chave | Correspondência | Formato | Justificativa |
> |---|---------------|-----------------|---------|---------------|
>
> **Categorias de Keywords:**
> 1. Keywords de Marca/Produto (se aplicável)
> 2. Keywords de Solução/Benefício
> 3. Keywords de Problema/Dor
> 4. Keywords de Concorrência (se relevante)
> 5. Keywords Locais (se aplicável)

### Formatos de Correspondência

| Tipo | Formato | Exemplo |
|------|---------|---------|
| Ampla | sem delimitadores | `software gestão` |
| Frase | entre aspas **retas** | `"sistema erp para empresas"` |
| Exata | entre colchetes | `[crm para vendas b2b]` |

> ⚠️ **OBRIGATÓRIO:** Keywords de correspondência de frase devem **sempre** usar aspas retas padrão (`"`). **Nunca** usar aspas tipográficas/curvas (`"`, `"`, `„`). Aspas tipográficas não são reconhecidas pelo Google Ads e invalidam a correspondência.

### Critérios de Qualidade
- Exatamente 30 keywords por marca
- Apenas 1 keyword ampla por marca
- Formatação correta por tipo de correspondência
- Foco em intenção de conversão (SQL), não informacional
- Se multi-marca: tabelas separadas com identificação visual distinta

### Output
- Tabela(s) de keywords com indicação da keyword ampla escolhida e justificativa
- Presentar ao usuário para revisão antes de avançar

---

## Fase 3: Keywords Negativas

### Objetivo
Avaliar e enriquecer lista de keywords negativas para qualificar o tráfego das campanhas.

### Inputs
- ICP (Fase 1)
- Keywords positivas (Fase 2)
- Briefing compilado

### Prompt de Geração

> Visando qualificar o tráfego da campanha de **{{EMPRESA}}**, gere uma lista completa e curada de keywords negativas.
>
> ### Lista Base de Keywords Negativas (ponto de partida)
>
> Ver referência completa em: `references/negative-keywords-base.md`
>
> **Instruções:**
> 1. **Avaliar criticamente** a lista base: remover silenciosamente keywords que possam excluir tráfego relevante para este cliente específico
> 2. **Adicionar 30+ novas keywords** contextualizadas: termos educacionais irrelevantes, emprego, entretenimento, soluções gratuitas, baixa intenção de compra, e termos que conflitem com as keywords positivas do cliente
> 3. **Consolidar tudo** em uma tabela única e limpa — apenas keywords que devem ser efetivamente negativadas
> 4. **Se houver múltiplas marcas:** avaliar se faz sentido separar tabelas por marca (separar apenas se existirem categorias exclusivas de uma marca; caso contrário, usar tabela única)
>
> **Formato de Saída:**
>
> | Categoria | Keyword Negativa | Justificativa |
> |-----------|------------------|---------------|

> **Importante:** A saída deve conter apenas a tabela consolidada final. Sem colunas de status (mantida/removida/adicionada). Usar separadores visuais entre categorias.

### Critérios de Qualidade
- Lista base avaliada criticamente (não manter cegamente)
- Mínimo 30 novas keywords contextualizadas
- Categorização clara (Gratuidade, Educacional, Emprego, Entretenimento, Baixa intenção, etc.)
- Multi-marca: tabela única salvo se existirem categorias exclusivas por marca

### Output
- Tabela consolidada com total de keywords e contagem por categoria
- Presentar ao usuário para revisão antes de avançar

---

## Fase 4: Anúncios Responsivos (RSA)

### Objetivo
Criar anúncios de texto responsivo completos para Google Ads Search.

### Inputs
- ICP (Fase 1)
- Keywords positivas (Fase 2)
- Keywords negativas (Fase 3, recomendado)
- Briefing compilado

### Multi-marca
Se o cliente possui múltiplas marcas, gerar **um bloco completo por marca** (16 headlines + 4 descriptions + 4 curtas + 6 extensões cada).

### Prompt de Geração

> Agora você é um especialista sênior em campanhas de Google Ads Pesquisa.
>
> Orientando-se pelo ICP e keywords da **{{EMPRESA}}**, crie anúncios de texto responsivo completos para gerar leads qualificados (SQLs).
>
> **Se houver múltiplas marcas, gerar um bloco completo por marca.**
>
> #### Headlines (16 títulos de até 30 caracteres, em Capitalized Case)
>
> | Posição | Tipo |
> |---------|------|
> | 1-4 | Alinhamento com palavra-chave e intenção de busca |
> | 5-7 | Características e benefícios do produto/serviço |
> | 8-9 | Números, indicadores e provas sociais |
> | 10-11 | Diferenciais competitivos |
> | 12 | Mensagem institucional ou de branding |
> | 13-14 | Calls to action relevantes |
> | 15-16 | Recursos dinâmicos (Keyword Insertion, location, countdown) |
>
> #### Descriptions (4 descrições de até 90 caracteres, em Capitalized Case)
>
> | Posição | Tipo |
> |---------|------|
> | 1-2 | Características e benefícios (frases curtas + CTA) |
> | 3 | Mensagem institucional da empresa |
> | 4 | Provas sociais e/ou indicadores numéricos |
>
> #### Descrições Curtas (4 de até 60 caracteres)
> Para uso em extensões e formatos alternativos.
>
> #### Extensões de Frase/Recursos (6 de até 25 caracteres)
> Sitelinks complementares para ampliar presença no SERP.

### Limites de Caracteres (rigorosos)

| Asset | Limite | Case |
|-------|--------|------|
| Headlines | 30 caracteres | Capitalized Case |
| Descriptions | 90 caracteres | Capitalized Case |
| Descrições curtas | 60 caracteres | Capitalized Case |
| Extensões | 25 caracteres | Capitalized Case |

### Ad Preview (recomendado)
Para cada marca, montar um preview simulando o anúncio no Google Search:
- **Título:** 3 headlines combinadas com ` | `
- **Descrição:** Description 1
- **Extensões:** 4 extensões da marca
- **URL:** Domínio real da marca

### Critérios de Qualidade
- 16 headlines de até 30 caracteres
- 4 descriptions de até 90 caracteres
- 4 descrições curtas de até 60 caracteres
- 6 extensões de até 25 caracteres
- Todos em Capitalized Case
- Diversidade de mensagens conforme estrutura
- Alinhamento com keywords definidas na Fase 2
- Ad preview coerente e realista

### Output
- Blocos completos de anúncios (por marca se multi-marca)
- Ad preview(s) para cada marca
- Resumo de conformidade de caracteres
- Presentar ao usuário para revisão

---

## Notas Gerais

- **Sequência:** Respeitar a ordem das fases. Cada fase depende das anteriores.
- **Isolamento:** Cada fase pode ser executada sozinha, desde que os inputs existam.
- **Informações reais:** Nunca inventar dados. Basear-se exclusivamente no briefing fornecido.
- **Multi-marca:** Sempre detectar e gerar deliverables separados por marca quando aplicável.
- **Revisão:** Sempre apresentar output ao usuário e aguardar aprovação antes de avançar.
- **Formato flexível:** O output pode ser em Markdown, HTML, ou outro formato conforme o contexto do projeto. A skill não impõe layout visual específico — apenas a estrutura de conteúdo.

## Referências

- **Lista base de keywords negativas:** Ver [negative-keywords-base.md](references/negative-keywords-base.md) para a lista completa de ~100 termos universais como ponto de partida.
- **Exemplos de output:** Ver [output-examples.md](references/output-examples.md) para exemplos de cada fase.
