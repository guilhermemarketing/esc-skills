# Brandformance Planning — Reference Frameworks

Especificações técnicas e frameworks para o agente consultar durante a geração do plano de brandformance.

---

## 1. Les Binet & Peter Field — The Long and the Short of It

### 1.1 Regra 60/40

```
Alocação ótima de investimento (média cross-category):
- 60% Brand Building (longo prazo, emocional, broad reach)
- 40% Sales Activation (curto prazo, racional, targeted)

Variações por categoria:
| Categoria        | Brand % | Activation % |
|------------------|:-------:|:------------:|
| B2C Mass Market  | 60%     | 40%          |
| B2C Premium      | 65%     | 35%          |
| B2B              | 46%     | 54%          |
| E-commerce       | 40%     | 60%          |
| Serviços locais  | 35%     | 65%          |
| Startups (<2 anos)| 25%    | 75%          |

⚠️ Estes são benchmarks. A proporção REAL depende da maturidade da marca.
```

### 1.2 Efeitos por Horizonte Temporal

```
Brand Building:
- Efeito visível: 6+ meses
- Peak effect: 2-3 anos
- Métricas: brand awareness, consideration, SOV, branded search, direct traffic
- Objetivo: criar mental availability (facilidade de lembrar da marca)

Sales Activation:
- Efeito visível: 0-6 meses
- Peak effect: imediato
- Métricas: leads, conversões, CAC, ROAS, CPA
- Objetivo: capturar demanda existente (bottom-of-funnel)

Brandformance (gui.marketing):
- Brand building que melhora performance
- Performance que gera sinais de marca
- Flywheel: marca forte → CAC menor → mais budget para marca → marca mais forte
```

---

## 2. Byron Sharp — How Brands Grow

### 2.1 Mental Availability

```
O que é: facilidade com que o comprador pensa na marca em situação de compra.

Como construir:
- Alcançar o MÁXIMO de potenciais compradores (broad reach)
- Criar Category Entry Points (CEPs) — situações que ativam a marca
- Consistência de branding (Distinctive Brand Assets)
- Frequência de exposição (SOV - Share of Voice)

CEPs — Exemplos por categoria:
- SaaS B2B: "preciso automatizar X", "meu time não escala", "concorrente faz melhor"
- E-commerce: "preciso de presente", "acabou o estoque em casa", "vi no Instagram"
- Serviços: "meu fornecedor atual não entrega", "preciso de parceiro", "foi indicado"
```

### 2.2 Physical Availability

```
O que é: facilidade com que o comprador encontra e compra da marca.

No digital:
- SEO (aparecer quando pesquisa)
- Ads (aparecer quando não pesquisa)
- Presença em marketplaces / diretórios
- Facilidade de conversão (LP otimizada, form simples)
- Velocidade de resposta (lead response time)
```

### 2.3 Leis do Marketing (Ehrenberg-Bass)

```
1. Double Jeopardy: Marcas menores têm menos compradores E compradores menos leais
2. Retention Double Jeopardy: Todas as marcas perdem clientes proporcionalmente ao tamanho
3. Pareto (Ajustada): Top 20% dos clientes = ~50% da receita (não 80%)
4. Natural Monopoly: Marcas grandes atraem desproporcionalmente mais light buyers
5. Duplication of Purchase: Compradores de uma marca compram de concorrentes proporcionalmente ao market share

Implicação: Crescimento vem de AQUISIÇÃO de novos compradores, não de loyalty programs.
```

---

## 3. Maturidade de Marca — Escala gui.marketing

### 3.1 Modelo de Maturidade (5 Níveis)

```
┌──────────────────────────────────────────────────────────────────┐
│ NÍVEL 1 — INVISÍVEL (Score 1-20)                                │
│ • Marca sem reconhecimento. Zero branded search.                 │
│ • 100% dependente de performance (Google Search, cold outbound)  │
│ • CAC alto e crescente. Sem efeito flywheel.                     │
│ • Recomendação: 80% activation / 20% brand awareness             │
├──────────────────────────────────────────────────────────────────┤
│ NÍVEL 2 — EMERGENTE (Score 21-40)                                │
│ • Algum tráfego direto. Branded search existe mas baixo.         │
│ • Reconhecimento no nicho. Primeiros cases e depoimentos.        │
│ • CAC estável. Performance funciona mas não escala.              │
│ • Recomendação: 65% activation / 35% brand building              │
├──────────────────────────────────────────────────────────────────┤
│ NÍVEL 3 — ESTABELECIDA (Score 41-60)                             │
│ • Branded search consistente. Tráfego direto > 15% do total.    │
│ • Reconhecimento regional ou de segmento.                        │
│ • CAC em tendência de queda. Efeito flywheel começando.          │
│ • Recomendação: 50% activation / 50% brand building              │
├──────────────────────────────────────────────────────────────────┤
│ NÍVEL 4 — REFERÊNCIA (Score 61-80)                               │
│ • Marca citada espontaneamente. Top 3 no segmento.              │
│ • Branded search forte. Indicação como fonte de lead.            │
│ • CAC baixo. Flywheel rodando. Word-of-mouth ativo.             │
│ • Recomendação: 40% activation / 60% brand building              │
├──────────────────────────────────────────────────────────────────┤
│ NÍVEL 5 — DOMINANTE (Score 81-100)                               │
│ • Market leader. Marca = categoria (genérico).                   │
│ • Maior SOV. CAC mais baixo do setor. Pricing power.            │
│ • Recomendação: 35% activation / 65% brand building              │
└──────────────────────────────────────────────────────────────────┘
```

### 3.2 Diagnóstico de Maturidade — Indicadores

```
| Indicador                    | Como medir                       | Fonte        |
|------------------------------|----------------------------------|--------------|
| Branded search volume        | Google Search Console/Ads         | Quantitativo |
| % tráfego direto             | GA4                              | Quantitativo |
| % tráfego orgânico branded   | GA4 + GSC                        | Quantitativo |
| SOV (Share of Voice)         | Auction Insights (Google Ads)    | Quantitativo |
| NPS (Net Promoter Score)     | Pesquisa com clientes            | Qualitativo  |
| Indicações como % de leads   | CRM                              | Quantitativo |
| CAC trend (últimos 6 meses)  | CRM + Ads                        | Quantitativo |
| Reconhecimento espontâneo    | Pesquisa de awareness            | Qualitativo  |
| Menções sociais (sem tag)    | Social listening                 | Quantitativo |
| Comparação com concorrentes  | Auction Insights, SEMrush/Ahrefs | Quantitativo |
```

---

## 4. Funil Invertido — gui.marketing

### 4.1 Conceito

```
Abordagem tradicional (de cima para baixo):
Awareness → Consideration → Conversion → Loyalty

Funil Invertido gui.marketing (de baixo para cima):
1. PRIMEIRO: Capturar demanda existente (bottom-funnel)
   → Google Search, retargeting, formulário direto
2. DEPOIS: Expandir para consideration (mid-funnel)
   → Content, comparação, cases, demonstração
3. POR ÚLTIMO: Investir em awareness (top-funnel)
   → Brand campaigns, vídeo, display, social

Por quê:
- Começar onde já há intenção = ROI imediato
- Revenue inicial financia expansão para awareness
- Dados de conversão informam messaging de awareness
- CAC do bottom-funnel = benchmark para medir branding
```

### 4.2 Flywheel

```
Brand forte → Branded search ↑ → CPC mais baixo → CAC ↓
→ Mais budget disponível → Mais brand → Branded search ↑↑
→ CPC ainda mais baixo → CAC ↓↓ → Flywheel acelerando

Sinais de Flywheel funcionando:
- Branded search crescendo mês a mês
- Direct traffic crescendo
- CAC geral caindo mesmo com volume crescendo
- % de leads por indicação subindo
- SOV crescendo sem aumento proporcional de budget
```

---

## 5. KPIs por Fase

### 5.1 Métricas de Brand (NÃO misturar com Performance)

```
| Métrica                  | O que mede                        | Frequência |
|--------------------------|-----------------------------------|:----------:|
| Branded Search Volume    | Demanda pela marca                | Semanal    |
| SOV (Share of Voice)     | Presença vs. concorrentes         | Semanal    |
| Direct Traffic %         | Recall da marca                   | Mensal     |
| Brand Lift (se disponível)| Awareness/consideration lift      | Por campanha|
| Organic branded clicks   | Busca pela marca no orgânico      | Mensal     |
| Menções sociais          | Buzz/word-of-mouth                | Mensal     |
| NPS                      | Satisfação e propensão a indicar  | Trimestral |
| Custo por 1.000 reached  | Eficiência de awareness           | Por campanha|
```

### 5.2 Métricas de Activation (Performance)

```
| Métrica        | O que mede                    | Frequência |
|----------------|-------------------------------|:----------:|
| CAC            | Custo por aquisição           | Semanal    |
| ROAS           | Retorno sobre investimento    | Semanal    |
| CPL/CPA        | Custo por lead/ação           | Semanal    |
| Conversion Rate| Taxa de conversão por estágio | Semanal    |
| LTV            | Valor do tempo de vida        | Mensal     |
| LTV:CAC ratio  | Eficiência de aquisição       | Mensal     |
| Payback Period | Tempo para recuperar CAC      | Mensal     |
| Pipeline Value | Valor total em negociação     | Semanal    |
```

### 5.3 Métricas Integradas (Brandformance)

```
| Métrica                       | O que mede                               |
|-------------------------------|------------------------------------------|
| CAC trend (6 meses)           | Efeito do branding no custo de aquisição |
| Branded search ↔ CAC corr.    | Correlação entre marca e eficiência      |
| % leads por indicação         | Word-of-mouth como canal de aquisição    |
| Organic ↔ Paid ratio          | Dependência de mídia paga                |
| Frequência ótima              | Ponto onde mais frequência = desperdício |
```

---

## 6. Cenários de Budget

### 6.1 Template de Cenários

```
| Cenário       | Budget Total | Brand % | Activation % | Resultado Esperado         |
|---------------|:----------:|:-------:|:------------:|----------------------------|
| Conservador   | R$ X       | Y%      | Z%           | Manter posição, CAC estável|
| Moderado      | R$ X       | Y%      | Z%           | Crescer 20-30%, CAC -10%  |
| Agressivo     | R$ X       | Y%      | Z%           | Crescer 50%+, market share↑|

Variáveis por cenário:
- Budget mensal por canal
- KPIs target por fase
- Timeline para efeito (brand = 6+ meses, activation = imediato)
- Riscos e mitigações
```

---

## 7. Micro-Bolhas de Marketing Digital — gui.marketing

### 7.1 Conceito

```
Definição: Pequenos grupos de audiência altamente segmentados, com mensagens
personalizadas que criam uma "bolha" envolvente para a marca no nicho.

Não é necessário investir milhares de reais para ser lembrado pelo público
potencial. A ideia de construir uma "bolha" visa construir um forte
relacionamento de forma gradual no nicho de mercado (potenciais clientes).

Diferente de pulverizar investimento para atingir todo o mercado de uma vez.
Estratégia: conquistar clientes gradualmente conforme o retorno.
```

### 7.2 Alocação Padrão

```
70% → Aquisição (tráfego pago para novos públicos com objetivo de conversão)
30% → Remarketing (com objetivo de educação e engajamento)

Por quê 30% basta para remarketing?
- Campanhas de "lembrança de marca", "alcance" e "envolvimento" têm
  custo por engajamento de centavos
- Se a segmentação de aquisição está bem montada, o remarketing mantém
  contato constante com o ICP
- Não é necessário investir tanto em remarketing quando o objetivo da campanha
  é lembrança de marca / alcance / envolvimento

A construção de bolhas segue o conceito de Brandformance e Flywheel Marketing:
- Aumenta reconhecimento da marca
- Enquanto gera leads qualificados ou solicitações de orçamento
- Remarketing melhora taxa de conversão leads→vendas, ROI, CAC e LTV
```

### 7.3 Como Construir Micro-Bolhas

```
1. Segmentação: Identifique características comuns (idade, comportamento, interesses)
2. Alcance: Expanda visibilidade entre o público-alvo certo
3. Remarketing + Frequência: Reengaje quem já interagiu com sua marca
   Garanta repetições suficientes para memorizarem sua marca
4. Mensuração: Avalie ROI, LTV, CAC continuamente

Benefícios:
- Personalização e relevância por segmento
- Reengajamento eficaz
- Redução do CPA
- Melhoria da relação LTV:CAC
```

---

## 8. Funil Invertido — Definição Completa gui.marketing

### 8.1 O Que É

```
"É uma forma de pensar diferente do 'funil clássico' que todo mundo ensina.
Ao invés de começar atraindo um monte de gente que nem sabe o que quer,
o Funil Invertido começa direto pelo fundo do funil, com quem já está
pronto pra comprar."

A lógica é simples:
1. Primeiro, atinge quem já tem intenção de compra
2. Depois, se preocupa com quem precisa de mais convencimento (escala)
3. Só no fim, entra com conteúdo educativo e branding
```

### 8.2 Etapas do Funil Invertido

```
1. DECISÃO DE COMPRA → Usuários com intenção clara de aquisição
   → Google Search (busca ativa), remarketing qualificado
   → Menor custo, resultados mais rápidos

2. CONSIDERAÇÃO DA SOLUÇÃO → Clientes cientes das soluções disponíveis
   → Comparação, cases, demonstração, content marketing

3. RECONHECIMENTO DO PROBLEMA → Clientes conscientes de seus problemas
   → Educação sobre sintomas e consequências

4. APRENDIZADO E DESCOBERTA → Público que precisa ser educado
   → Menos prioritário inicialmente
   → Branding, awareness campaigns
```

### 8.3 Conexão com Brandformance Flywheel

```
O Funil Invertido conversa com o Brandformance Flywheel porque:
1. Reduz desperdício de mídia (foco em intenção)
2. Acelera o payback (ROI imediato no bottom-funnel)
3. Cada ciclo de campanha fortalece a marca enquanto gera caixa

Três camadas operacionais:
1. Base Proprietária: audiência própria, comunidade, CRM e listas
   que já confiam na marca
2. Marketing Direto: compra de keywords com intenção de resolução,
   ofertas claras, mensuráveis, com promessa específica e prova forte
3. Expansão Controlada: só depois de validar mensagem e oferta com
   quem já te conhece, escalar para públicos frios
```

---

## 9. Janelas de Impacto — gui.marketing

```
⚡ Curto Prazo (30-45 dias) — Quick Wins
   → Correções de bugs de usabilidade, velocidade do site
   → Alinhamento básico de oferta
   → Efeito: melhoria imediata na conversão

📈 Médio Prazo (60-90 dias) — Maturação
   → Testes A/B e aprendizado de máquina das campanhas
   → CAC começa a estabilizar
   → Efeito: otimização baseada em dados reais

🔄 Longo Prazo (90+ dias) — Efeito Flywheel
   → Marca ganha força, LTV aumenta
   → CAC cai consistentemente pela autoridade construída
   → Efeito: ciclo auto-alimentado de crescimento

Disclaimer obrigatório: "Brandformance é construção de ativo, não mágica."
```

---

## 10. Três Pilares Interdisciplinares — gui.marketing

```
Uma campanha só performa quando integra três áreas que se retroalimentam:

1. MENSAGEM & OFERTA (Copywriting + Posicionamento)
   → O CTR, o CPM e o CPC começam na narrativa, não no botão do gerenciador
   → Não existe segmentação que salve uma promessa fraca
   → Posicionamento diferencia a marca ANTES do clique

2. UX & ENGENHARIA DE CONVERSÃO (CRO)
   → A melhor campanha desaba se a página não sustenta a intenção gerada
   → A taxa de conversão é a verdadeira alavanca de ROI, não o bid automático

3. TRACKING, DADOS & UNIT ECONOMICS
   → Escalar só faz sentido quando a conta fecha em ROI, CAC, LTV,
     margem, payback e viabilidade por canal
   → Sem instrumento técnico, trafegar vira aposta

"Quem domina apenas a ferramenta opera tráfego.
 Quem domina Copy, UX, Dados e Produto opera crescimento."

Implicação para Brandformance:
- Plano sem os 3 pilares é desperdício de budget
- A gestão moderna é interdisciplinar por necessidade
```

---

## 11. Proof Points gui.marketing (Cases Reais)

### 11.1 E-commerce

```
🏬 Iluminim (Iluminação)
   → Receita tráfego pago: R.99M → R.28M (+157,16%)
   → Transações: 21.251 → 68.771 (+223,61%)
   → Taxa de conversão: 1,50% → 3,78% (+152%)
   → Receita total da loja: R.81M → R.69M
   → Branded search disparou no Google Trends (efeito flywheel)
   → Táticas: Google Ads, Facebook Ads, Instagram Ads, análise de dados,
     teste A/B, machine learning aplicado a ads
```

### 11.2 B2B / Imobiliário

```
🏗️ BILD (Desenvolvimento Imobiliário)
   → Conversão leads digitais: 0,8% → 2,8%
   → 4 → 8 regionais em 2020, todas com vendas acima do esperado
   → Conversão de leads qualificados: +60%
   → Faturamento escalado em 221%, ROI em 75%
   → Depoimento: "Encerramos o ano dobrando o número de regionais
     e registrando venda em todas elas"

🏫 Escola da Inteligência (B2B)
   → ROI: 1668%
   → 81 mil leads gerados
   → Ciclo de vendas 2x mais rápido vs. outbound
   → Conversão digital 12% vs outbound 6% (103% superior)
```

### 11.3 Brand + Performance (Brandformance puro)

```
🎬 Rede de Cinemas
   → Clube Legacy: ROAS 14x, CAC Rzsh,48
   → Incremento de 400% no ROAS e melhoria de 66% no CAC
   → Novo Clube: ROAS 10x, CAC R,58 (LTV R)
   → Meta Ads: 11.8M usuários alcançados, CPM R,92,
     custo por engajamento Rzsh,01 (um centavo!)
   → Google Ads (Visitas Locais): custo por visita R,94,
     73.3M impressões, CPM R,96
   → Prova de brandformance: awareness campaigns com CPM baixo
     geraram visitas físicas mensuráveis e CAC ínfimo
```
