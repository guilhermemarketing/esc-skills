# Especificações Técnicas Meta Ads

Referência completa de formatos, limites e boas práticas da plataforma Meta Ads (Facebook + Instagram).

## Limites de Texto

| Elemento | Limite | Visibilidade | Notas |
|----------|--------|--------------|-------|
| **Headline** | 40 caracteres | Total | Trunca após 40 em alguns placements |
| **Texto principal** | 125 caracteres | Primeiros 125 visíveis | Total até 500, mas maioria não expande |
| **Descrição** | 30 caracteres | Varia por placement | Nem sempre exibida |
| **CTA** | Pré-definido | Sempre visível | Selecionar da lista nativa |

## CTAs Nativos Disponíveis

| CTA | Melhor para |
|-----|-------------|
| `Saiba mais` | Awareness, consideração |
| `Cadastre-se` | Lead gen, newsletters |
| `Fale conosco` | Serviços, B2B |
| `Obter oferta` | Promoções, descontos |
| `Solicitar orçamento` | Serviços de alto ticket |
| `Baixar` | Lead magnets, ebooks |
| `Agendar agora` | Consultas, demos |
| `Ver mais` | Catálogo, e-commerce |

## Formatos e Dimensões

| Formato | Aspect Ratio | Dimensão (px) | Placements |
|---------|--------------|---------------|------------|
| **Feed Quadrado** | 1:1 | 1080 × 1080 | Feed FB/IG, Marketplace |
| **Feed Vertical** | 4:5 | 1080 × 1350 | Feed FB/IG (maior área visual) |
| **Stories/Reels** | 9:16 | 1080 × 1920 | Stories, Reels, Audience Network |
| **Carrossel** | 1:1 | 1080 × 1080 | Feed FB/IG (2-10 cards) |
| **Landscape** | 1.91:1 | 1200 × 628 | Feed FB, Right Column, Search |

> **Recomendação:** Priorizar 1:1 (maior compatibilidade) ou 4:5 (maior área visual no feed).

## Zonas Seguras — Stories/Reels (9:16)

Manter elementos importantes fora das zonas de interface:

```
┌────────────────────────┐
│ ░░░ ZONA SUPERIOR ░░░░ │  ← 14% superior (250px): nome do perfil, ícones
│                        │
│                        │
│    ZONA SEGURA         │  ← 72% central: conteúdo principal
│    (conteúdo)          │
│                        │
│                        │
│ ░░░ ZONA INFERIOR ░░░░ │  ← 14% inferior (250px): CTA, swipe up
└────────────────────────┘
```

## Hierarquia Visual

```
1º NÍVEL: Elemento Hero (produto, pessoa, visual principal)
    ↓
2º NÍVEL: Headline / Proposta de valor
    ↓
3º NÍVEL: Elementos de suporte (benefícios, prova)
    ↓
4º NÍVEL: CTA / Logo
```

## Legibilidade Mobile

| Elemento | Mínimo recomendado | Notas |
|----------|-------------------|-------|
| Headline | 24px equivalente | Testar em tela de 375px |
| Corpo | 16px equivalente | Evitar textos longos |
| CTA | 44px touch target | Área clicável mínima |
| Contraste | 4.5:1 mínimo | WCAG AA para texto |

## Regra dos 20% de Texto

Meta não rejeita anúncios por excesso de texto, mas **penaliza alcance** quando texto ocupa mais de 20% da imagem.

**Boas práticas:**
- Concentrar texto em uma área (não espalhar)
- Preferir textos curtos e impactantes
- Usar campo "Texto principal" do anúncio para informações adicionais
- Logos com texto contam no cálculo

## Primeiros 3 Segundos (Vídeo/Reels)

Para vídeos, capturar atenção nos primeiros 3 segundos:

- Movimento imediato
- Contraste forte
- Rosto humano (se aplicável)
- Pattern interrupt visual
- Texto com gancho
- Teste do mudo: funciona sem áudio? (maioria assiste sem som)
- Texto na tela é obrigatório em todo o vídeo

## Variações por Objetivo de Campanha

### Awareness

| Aspecto | Recomendação |
|---------|--------------|
| Ângulo | Curiosidade, benefício amplo |
| Copy | Educativa, sem pressão |
| Visual | Impactante, memorável |
| CTA | Saiba mais, Ver mais |

### Consideração

| Aspecto | Recomendação |
|---------|--------------|
| Ângulo | Benefício específico, diferencial |
| Copy | Comparativa, prova social |
| Visual | Demonstração de uso |
| CTA | Saiba mais, Fale conosco |

### Conversão

| Aspecto | Recomendação |
|---------|--------------|
| Ângulo | Urgência, oferta clara |
| Copy | Direta, benefício + CTA |
| Visual | Produto em destaque |
| CTA | Cadastre-se, Obter oferta, Agendar |
