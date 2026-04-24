# Metodologias de Message Mining — Referência Técnica

Documento de referência para a Fase 1 do workflow de message mining.
Baseado em CXL/Peep Laja, VoC Playbook, e pesquisa qualitativa de conversão.

---

## 1. Review Mining (Fonte Primária)

### Objetivo
Capturar a "voz" do cliente encontrando golden nuggets, mensagens recorrentes e padrões reais de linguagem.

### Fontes
- Diretórios online: Trustpilot, G2, Capterra, Amazon, Clutch, Google Business
- Reviews de concorrentes nas mesmas plataformas
- Reviews de livros/cursos do nicho (Amazon, Udemy)

### Perguntas-Guia
- O que pensam sobre o problema?
- Que soluções alternativas estão considerando?
- Quais são as maiores hesitações?

### O que Extrair
| Categoria | Descrição | Exemplo |
|-----------|-----------|---------|
| Necessidades/Desejos | O que buscam como resultado | "Preciso de algo simples que funcione" |
| Pain Points | Dores específicas em linguagem crua | "code monkeys", "overhead absurdo" |
| Barreiras | O que impede ou quase impediu | "fusos horários", "curva de aprendizado" |
| Valores | O que valorizam no fornecedor | "abordagem europeia", "transparência" |
| Trigger Events | O que motivou a busca | "quando perdi meu terceiro cliente" |

### Processo de Extração
1. Ler review completo (não apenas título/rating)
2. Copiar trechos **literalmente** — aspas = transcrição exata
3. Marcar tom emocional: Frustrado / Esperançoso / Cético / Satisfeito
4. Contar frequência de cada tema → temas com 5+ menções = prioridade máxima
5. Para reviews de concorrentes: focar em ⭐1-3 (insatisfações revelam gaps de mercado)

### Uso em Copy
- Swiping verbatims para headlines (ex: "Se você acha que precisa de reabilitação, você precisa")
- Moldando propostas de valor usando o tom do cliente (nerdy, profissional, casual)
- Usar linguagem negativa (dor) > linguagem positiva (benefício) — o mercado fala mais do que quer evitar

---

## 2. Customer Surveys (Email & On-site)

### Objetivo
Entender buyer intelligence, trigger events e motivações que transformam prospects em clientes.

### Fontes
- Listas de email (clientes recentes — até 90 dias)
- Pop-up surveys on-site (Qualaroo, Hotjar)
- Listas de assinantes

### Perguntas-Chave
| Pergunta | O que revela |
|----------|-------------|
| "Quando percebeu que precisava de nós?" | Trigger event |
| "Que problema isso resolve para você?" | Dor principal percebida |
| "O que quase te impediu de comprar?" | Objeções reais |
| "Para quem recomendaria?" | Segmentação espontânea |
| "O que mais gosta?" | Top 3 benefícios percebidos |

### O que Extrair
- Segmentação de usuários (Iniciante vs. Pro, por ex.)
- Hierarquia de necessidades (ex: "buscar primeiro emprego na área")
- Top 3 benefícios mais elogiados pelos clientes

### Uso em Copy
- Refinar headlines para casar com objetivos do usuário
- Criar seções "Escolha-nos quando..." endereçando ansiedades específicas

---

## 3. Entrevistas com CS, Sales & Account Executives

### Objetivo
Aproveitar o conhecimento acumulado de equipes que lidam com milhares de interações diárias.

### Fontes
- Trocas de Customer Support
- Pitches de vendas, sessões de demo
- Entrevistas internas com staff

### Perguntas-Chave
- Quais as objeções mais comuns?
- Como você endereça essas objeções?
- Que aspectos geram mais entusiasmo?
- Qual metáfora/analogia funciona melhor para explicar o produto?

### O que Extrair
- Motivações comuns dos usuários
- Pontos de fricção emocional
- Linguagem específica que o staff usa para explicar o produto de forma simples

### Uso em Copy
- Endereçar objeções diretamente em seções de FAQ ou copy de vendas
- Usar metáforas de sucesso em sub-headlines
- Traduzir explicações do sales team para copy de LP

---

## 4. Feedback Polls (Sniper Surveys)

### Objetivo
Obter insights claros e acionáveis com mínima intrusão, disparados por comportamentos específicos.

### Fontes
- Polls de 1 pergunta em páginas de alta prioridade
- Polls pós-conversão (páginas de confirmação/obrigado)

### Perguntas-Chave
- "Qual o principal motivo da sua visita?" (em página de produto)
- "Você tem alguma pergunta não respondida?" (pré-conversão)
- "O que quase te impediu de comprar?" (pós-conversão)

### O que Extrair
- "Vazamentos" em páginas específicas de formulário
- Informações faltantes que quase causaram abandono
- Medos específicos que aparecem no momento da decisão

### Uso em Copy
- Adicionar "razões para acreditar" (depoimentos/dados) próximo a botões CTA
- Endereçar medos específicos identificados no poll diretamente na LP

---

## 5. Mineração de Reddit e Fóruns

### Objetivo
Capturar conselhos entre pares (mais autênticos que reviews direcionados) e identificar linguagem orgânica do nicho.

### Fontes
- Subreddits relevantes ao nicho
- Quora, Stack Overflow/Exchange (quando aplicável)
- Fóruns especializados do setor
- Grupos do Facebook (se acessível)

### Processo
1. Buscar threads com palavras-chave do nicho (produto, problema, alternativas)
2. Priorizar **posts com muitos upvotes** → validação da comunidade
3. Capturar conselhos peer-to-peer (linguagem mais crua e honesta)
4. Identificar soluções alternativas que a comunidade recomenda
5. Notar **tom predominante**: cético, entusiasta, técnico, casual

### O que Extrair
- Linguagem orgânica e jargão do nicho
- Soluções alternativas que a comunidade recomenda
- Objeções e ceticismos em estado bruto
- "Eu mudei de X para Y porque..." → razões de migração

---

## 6. Mouse Tracking / Heat Maps (Análise Comportamental)

### Objetivo
Visualizar padrões de engajamento e interação (cliques, scrolls, atenção).

### Fontes
- Click maps, scroll maps, session replays
- Ferramentas: Hotjar, Sessioncam, Clarity

### O que Revela
- Se os usuários rolam até a oferta principal ou param antes
- Que elementos recebem mais atenção
- Se estão clicando em elementos não-clicáveis (indicador de confusão)

### Aplicação em Message Mining
- Se scroll maps mostram que usuários não chegam ao fundo → mover mensagens críticas para cima
- Se clicam em algo não-clicável → indicador de interesse não atendido
- Informa hierarquia de informação para wireframe/LP

---

## 7. User Testing

### Objetivo
Identificar problemas de usabilidade e fontes de fricção observando pessoas reais.

### Fontes
- Sessões moderadas e não-moderadas com usuários de primeira vez
- Tarefas específicas ou exploração livre

### Perguntas-Guia
- Onde ficam travados?
- O que permanece confuso após a leitura?
- Taxa de conclusão de tarefas

### Aplicação em Message Mining
- Descobrir se usuários realmente entendem a proposta de valor
- Identificar instruções e declarações de valor que confundem
- Reestruturar hierarquia de informação e reescrever copy confuso

---

## Matriz de Priorização de Fontes

| Fonte | Riqueza da Linguagem | Facilidade de Acesso | Volume de Dados | Prioridade |
|-------|:-------------------:|:--------------------:|:---------------:|:----------:|
| Reviews online (próprios) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🔴 1 |
| Reviews de concorrentes | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🔴 2 |
| Transcrições de calls | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | 🔴 3 |
| Reddit/Fóruns | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | 🔴 4 |
| Surveys de clientes | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | 🟡 5 |
| Entrevistas CS/Sales | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | 🟡 6 |
| Feedback polls | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | 🟡 7 |
| Heat maps/session replays | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 🟢 8 |
| User testing | ⭐⭐⭐⭐ | ⭐ | ⭐ | 🟢 9 |

---

## Regras de Categorização

### Classificação de Frequência
- **Alta (10+):** Tema mencionado em 10 ou mais verbatims → PRIORIDADE MÁXIMA
- **Média (5-9):** Tema mencionado 5-9 vezes → incluir no output
- **Baixa (1-4):** Tema mencionado 1-4 vezes → incluir apenas se intensidade for Severa

### Classificação de Intensidade
- **🔴 Severa:** Linguagem emocional forte, urgência, frustração intensa
- **🟡 Moderada:** Incômodo claro, mas sem urgência extrema
- **🟢 Leve:** Nice-to-have, menção casual

### Regra de Ouro
> **Frequência Alta + Intensidade Severa = Headline Candidate.**
> Se 15 pessoas dizem a mesma coisa com emoção → isso é seu headline.

### Classificação de Objeções (Tipos)
1. **Preço** — "É caro demais", "Não cabe no orçamento"
2. **Confiança** — "Nunca ouvi falar", "Parece bom demais pra ser verdade"
3. **Timing** — "Agora não é o momento", "Preciso pensar"
4. **Complexidade** — "Parece complicado", "Não tenho equipe para isso"
5. **Comparação** — "O concorrente X oferece Y", "Por que não usar Z?"
6. **Risco** — "E se não funcionar?", "Tem garantia?"

---

## Exemplo de Verbatim Categorizado

```
Verbatim: "Eu gastava literalmente 3 horas por dia só tentando organizar as planilhas 
           de controle. Era enlouquecedor."
Fonte:    Review G2 (⭐5) — cliente há 6 meses
Categoria: Pain Point — Tempo perdido em tarefas manuais
Frequência: Alta (mencionado 12x em variações)
Intensidade: 🔴 Severa ("enlouquecedor")
Uso sugerido: Headline de LP → "Pare de perder 3 horas por dia com planilhas"
Segmento: Gestores operacionais de PMEs
```
